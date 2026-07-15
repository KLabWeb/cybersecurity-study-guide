#!/usr/bin/env python3
"""
step_dedup_check.py  --  Cross-step duplicate detector for the Study Plan.

Invoked by the chat command:  STEP DEDUP CHECK   (or runs automatically inside GENERATE PDF)
Run directly:                 python3 step_dedup_check.py
Self-test:                    python3 step_dedup_check.py --selftest

It parses every step in every phase and runs THREE independent detectors:

  1. RESOURCE duplicates (hard).  A "completable resource" is a PortSwigger topic / learning-path,
     a PortSwigger /web-security lab anchor, a Burp Suite tool/doc page, or a TryHackMe room/module.
     Each bullet's action on a resource is graded FULL (a completion/study verb with no subset
     qualifier) or PART (apprentice-only, "remaining", "review your", "re-read", "first N",
     "read the ... material", orientation). When the SAME resource is treated FULL in >= 2 distinct
     steps, that is a hard duplicate (you would do the same thing twice). FULL + PART is the
     intended intro-then-mastery pattern and is reported as INFO, not a duplicate.

  2. BOOK duplicates (hard).  The same book title read in >= 2 steps with OVERLAPPING chapter ranges.

  3. CONTENT near-duplicates (review).  Two bullets in DIFFERENT steps whose normalised wording
     overlaps heavily (and which are not an explicit cross-phase staged reference). This catches
     repeated instructions the URL matcher cannot see -- e.g. "work through the official Burp
     documentation: Proxy, Repeater, Intruder" written in two phases, or a boilerplate instruction
     copied between steps. Reported for human review.

Why both URL and content passes exist: the URL pass alone missed a real duplicate (the same Burp
documentation studied in Phase II and Phase IV) because the two bullets linked different Burp URLs
and used the verb "work through", which the old grader did not recognise. The content pass is a
backstop that does not depend on links or on a fixed verb list.

check() returns 1 if any HARD duplicate (resource or book) is found, else 0, so GENERATE PDF can warn.
"""
import re, sys, os
from collections import defaultdict

SRC_DEFAULT = os.path.join(os.path.dirname(__file__), "appsec_content.py")

# ---- resource topic mapping ------------------------------------------------
ANCHOR2TOPIC = {
    "sql-injection": "sql-injection",
    "access-control-vulnerabilities": "access-control",
    "business-logic-vulnerabilities": "business-logic",
    "authentication": "authentication",
    "api-testing": "api-testing",
    "cross-origin-resource-sharing-cors": "cors",
    "cross-site-request-forgery-csrf": "csrf",
    "server-side-request-forgery-ssrf": "ssrf",
    "xml-external-entity-xxe-injection": "xxe",
    "cross-site-scripting": "cross-site-scripting",
    "os-command-injection": "os-command-injection",
    "server-side-template-injection": "server-side-template-injection",
    "insecure-deserialization": "deserialization",
    "file-upload-vulnerabilities": "file-upload",
    "path-traversal": "path-traversal",
    "jwt": "jwt",
    "oauth-authentication": "oauth",
}
# topic-page slug -> canonical topic (so /web-security/<slug> and the matching all-labs anchor collide)
SLUG2TOPIC = {
    "logic-flaws": "business-logic",
    "csrf": "csrf", "ssrf": "ssrf", "xxe": "xxe",
    "file-path-traversal": "path-traversal", "file-upload": "file-upload",
    "deserialization": "deserialization",
}

# completion / study intent (an action that consumes the whole resource)
FULL_RE = re.compile(
    r'\b(complete[ds]?|completely|in full|all (?:the )?(?:apprentice and practitioner )?labs|'
    r'all apprentice and practitioner|work(?:ed|ing)? through|work the|go(?:ing)? through|'
    r'study|studied|do the|learn)\b', re.I)
# subset / staged qualifiers that downgrade FULL -> PART
SUBSET_RE = re.compile(
    r'\b(apprentice-level|apprentice labs|the remaining|remaining (?:practitioner|labs)|'
    r'review your|re-?read|first \d|subset|orientation|read the|skim|notes\b)', re.I)
# an explicit cross-phase staged reference / cross-reference (intentional) -> not a content dup
STAGE_RE = re.compile(
    r'(follow in phase|review your|the remaining|re-?read|first \d|apprentice-level|'
    r'phase (?:0|i|ii|iii|iv|v|vi|vii|viii|ix)\b|your phase|notes,? then|see \u201c|see ")', re.I)

STOP = set((
    "a an the and or of to in on for with as at by from into your you we i will would should could "
    "this that these those it its their them they then than each any all use using used uses through "
    "throughout be is are was were been being do does done can may might not no nor so such only own "
    "same other more most some here there when where which who what how why off up down out over under "
    "again further also but if while about against between during without within per via you'll").split())


def _deesc(s):
    s = s.replace('\\"', '"')
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)


def _phases(lines):
    bans = [(i, m.group(1)) for i, l in enumerate(lines)
            for m in [re.search(r'banner\("([^"]*)"', l)] if m]
    out = []
    for k, (ln, rom) in enumerate(bans):
        end = bans[k + 1][0] if k + 1 < len(bans) else len(lines)
        out.append((rom.strip(), ln, end))
    return out


def _step_calls(lines, a, b):
    i = a
    while i < b:
        if re.match(r'\s*step\(', lines[i]):
            buf = [lines[i]]; depth = lines[i].count('(') - lines[i].count(')'); j = i
            while depth > 0 and j + 1 < b:
                j += 1; buf.append(lines[j]); depth += lines[j].count('(') - lines[j].count(')')
            yield "\n".join(buf); i = j + 1
        else:
            i += 1


def _bullets(call):
    idx = call.find('[')
    body = call[idx + 1:] if idx >= 0 else call
    out, cur = [], []
    for ln in body.split("\n"):
        m = re.findall(r'"((?:[^"\\]|\\.)*)"', ln)
        if m:
            cur.append("".join(m))
        if ln.rstrip().endswith(('",', '"]', '"),', '])')):
            if cur:
                out.append(_deesc("".join(cur))); cur = []
    if cur:
        out.append(_deesc("".join(cur)))
    return out


def parse_steps(text):
    """Return a list of dicts: {phase, num, label, bullets:[raw bullet strings]}."""
    lines = text.split("\n")
    steps = []
    for rom, a, b in _phases(lines):
        for c in _step_calls(lines, a, b):
            h = re.search(r'step\("(\d+)",\s*"([^"]*)"', c)
            steps.append({
                "phase": rom,
                "num": h.group(1) if h else "?",
                "label": _deesc(h.group(2)) if h else "",
                "bullets": _bullets(c),
            })
    return steps


def topic_of(url):
    if "portswigger.net/burp/" in url or re.search(r'/burp(/|$)', url):
        return "burp-suite"
    m = re.search(r'/web-security/all-labs#([a-z0-9-]+)', url)
    if m:
        return ANCHOR2TOPIC.get(m.group(1), m.group(1))
    m = re.search(r'/web-security/([a-z0-9-]+)', url)
    if m and m.group(1) != "all-labs":
        slug = m.group(1)
        return SLUG2TOPIC.get(slug, slug)
    m = re.search(r'/(?:room|module|path)/([a-z0-9-]+)', url)
    if m:
        return "thm:" + m.group(1)
    return None


def _chaprange(text):
    rng = set()
    for m in re.finditer(r'Ch\.?\s*(\d+)\s*(?:[-\u2013]\s*(\d+))?', text):
        lo = int(m.group(1)); hi = int(m.group(2)) if m.group(2) else lo
        rng |= set(range(lo, hi + 1))
    return rng


def _tokens(bullet):
    t = re.sub(r'<[^>]+>', ' ', bullet)          # strip HTML tags (keeps link TEXT, drops href)
    t = re.sub(r'https?://\S+', ' ', t)          # drop any bare URLs
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return [w for w in t.split() if len(w) > 1 and w not in STOP]


# ---- core detection (pure; operates on parsed steps so it is unit-testable) ----
def detect(steps,
           oc_threshold=0.6, min_tokens=6, min_shared_distinctive=4):
    findings = {"resource": [], "book": [], "content": []}

    # 1) RESOURCE ------------------------------------------------------------
    res = defaultdict(list)        # topic -> [(phase,num,label,bullet,full)]
    for s in steps:
        for bt in s["bullets"]:
            full = bool(FULL_RE.search(bt)) and not SUBSET_RE.search(bt)
            for u in re.findall(r'href="([^"]+)"', bt):
                t = topic_of(u)
                if t:
                    res[t].append((s["phase"], s["num"], s["label"], bt, full))
    for t, hits in res.items():
        full_steps = []
        seen = set()
        for p, n, l, bt, f in hits:
            if f and (p, n) not in seen:
                seen.add((p, n)); full_steps.append((p, n, l))
        if len(full_steps) >= 2:
            findings["resource"].append((t, full_steps, hits))

    # 2) BOOKS ---------------------------------------------------------------
    books = defaultdict(list)      # title -> [(phase,num,chapters,bullet)]
    for s in steps:
        for bt in s["bullets"]:
            for bm in re.finditer(r'<i>([^<]+)</i>', bt):
                title = bm.group(1).strip().strip("\u201c\u201d\"")
                if re.search(r'\b(Read|Complete|Work through|Study)\b', bt) and "Ch" in bt:
                    books[title].append((s["phase"], s["num"], _chaprange(bt), bt))
    for title, hits in books.items():
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                ov = hits[i][2] & hits[j][2]
                if ov and (hits[i][0], hits[i][1]) != (hits[j][0], hits[j][1]):
                    findings["book"].append((title, hits[i], hits[j], sorted(ov)))

    # 3) CONTENT near-duplicates --------------------------------------------
    # flatten bullets with provenance + token sets
    flat = []
    for s in steps:
        for bt in s["bullets"]:
            flat.append((s["phase"], s["num"], bt, set(_tokens(bt))))
    # document frequency for "distinctive" weighting
    df = defaultdict(int)
    for _, _, _, toks in flat:
        for w in toks:
            df[w] += 1
    nb = max(1, len(flat))
    # a token is "distinctive" only if it is rare document-wide; this excludes sentence-frame
    # words (complete, learning, path, portswigger, labs, apprentice, practitioner, read, notes...)
    # that recur across many bullets, leaving genuinely identifying tokens (proper nouns, tool names).
    distinct_max = max(3, round(0.04 * nb))
    res_pairs = {frozenset([(p, n) for p, n, _ in fs]) for _, fs, _ in findings["resource"]}
    for i in range(len(flat)):
        pi, ni, bi, ti = flat[i]
        if len(ti) < min_tokens:
            continue
        for j in range(i + 1, len(flat)):
            pj, nj, bj, tj = flat[j]
            if (pi, ni) == (pj, nj):           # same step -> skip
                continue
            if len(tj) < min_tokens:
                continue
            inter = ti & tj
            if not inter:
                continue
            oc = len(inter) / min(len(ti), len(tj))
            shared_distinct = [w for w in inter if df[w] <= distinct_max]
            if oc >= oc_threshold and len(shared_distinct) >= min_shared_distinctive:
                if STAGE_RE.search(bi) or STAGE_RE.search(bj):
                    continue                   # intentional cross-phase staged reference
                findings["content"].append(
                    ((pi, ni), (pj, nj), round(oc, 2), sorted(shared_distinct), bi, bj))
    return findings


def check(src=SRC_DEFAULT):
    steps = parse_steps(open(src, encoding="utf-8").read())
    f = detect(steps)
    print("================  STEP DEDUP CHECK  ================\n")

    print("-- RESOURCE: same completable resource done FULL in >1 step --")
    if not f["resource"]:
        print("  none")
    for t, full_steps, hits in sorted(f["resource"]):
        print(f"  {t}:  DUPLICATE -> full in " + ", ".join(f"P{p} step{n}" for p, n, l in full_steps))
        for p, n, l, bt, fl in hits:
            print(f"      P{p} step{n} [{'FULL' if fl else 'part'}] {bt[:74]}")
    print()

    print("-- BOOKS: same title, overlapping chapters, >1 step --")
    if not f["book"]:
        print("  none")
    for title, h1, h2, ov in sorted(f["book"]):
        print(f"  '{title}': P{h1[0]} step{h1[1]} & P{h2[0]} step{h2[1]} overlap Ch {ov}")
    print()

    print("-- CONTENT: near-identical instruction in >1 step (review) --")
    if not f["content"]:
        print("  none")
    for (a, b, oc, shared, bi, bj) in f["content"]:
        print(f"  P{a[0]} step{a[1]}  ~=  P{b[0]} step{b[1]}   (overlap {oc}; shared: {', '.join(shared[:8])})")
        print(f"      A: {bi[:90]}")
        print(f"      B: {bj[:90]}")
    print()

    hard = len(f["resource"]) + len(f["book"])
    review = len(f["content"])
    print("================  SUMMARY  ================")
    print(f"  steps: {len(steps)} | hard duplicates: {hard} | content items to review: {review}")
    if hard:
        print("  HARD DUPLICATES FOUND -- resolve so each resource is completed once "
              "(earlier phase = intro, later phase = review + remainder).")
    elif review:
        print("  No hard duplicates. \u2713  (content items above are advisory -- review manually.)")
    else:
        print("  No duplicate steps. \u2713")
    return 1 if hard else 0


# ============================ SELF-TEST ====================================
def _mk(phase, num, *bullets, label="STEP"):
    return {"phase": phase, "num": num, "label": label, "bullets": list(bullets)}


def selftest():
    PS = "https://portswigger.net"
    cases = []  # (name, steps, expect_resource_topics:set, expect_book:bool, expect_content_pairs:int_min)

    # P1 hard resource dup: same PortSwigger path completed in two phases
    cases.append(("dup_same_path", [
        _mk("II", "01", f'Complete the PortSwigger <a href="{PS}/web-security/sql-injection">SQL injection</a> learning path and all the <a href="{PS}/web-security/all-labs#sql-injection">labs</a>'),
        _mk("III", "02", f'Complete the PortSwigger <a href="{PS}/web-security/sql-injection">SQL injection</a> learning path in full, every <a href="{PS}/web-security/all-labs#sql-injection">labs</a>'),
    ], {"sql-injection"}, False, 0))

    # P2 the real Burp case (different burp URLs + "work through")
    cases.append(("dup_burp", [
        _mk("II", "01", f'Work through the official Burp Suite documentation \u2014 <a href="{PS}/burp/documentation/desktop/tools/proxy">Proxy</a>, <a href="{PS}/burp/documentation/desktop/tools/repeater">Repeater</a>, and <a href="{PS}/burp/documentation/desktop/tools/intruder">Intruder</a> \u2014 the primary tools you will use throughout this phase'),
        _mk("IV", "01", f'Install <a href="{PS}/burp/communitydownload">Burp Suite Community Edition</a>. Work through the official documentation: Proxy, Repeater, Intruder, Decoder, Comparer'),
    ], {"burp-suite"}, False, 1))

    # P3 book overlap
    cases.append(("dup_book", [
        _mk("I", "01", 'Read <i>Real-World Bug Hunting</i> Ch. 1\u20135 for context'),
        _mk("I", "03", 'Complete <i>Real-World Bug Hunting</i> Ch. 4\u20136 hands-on'),
    ], set(), True, 0))

    # N1 intro/mastery on same topic -> NOT a hard dup (apprentice then remaining)
    cases.append(("ok_intro_mastery", [
        _mk("II", "05", f'Complete the PortSwigger <a href="{PS}/web-security/sql-injection">SQL injection</a> learning path, then work the apprentice-level <a href="{PS}/web-security/all-labs#sql-injection">labs</a>; the practitioner labs follow in Phase III'),
        _mk("III", "01", f'Re-read the PortSwigger <a href="{PS}/web-security/sql-injection">SQL injection</a> learning path and your Phase II notes, then complete the remaining practitioner <a href="{PS}/web-security/all-labs#sql-injection">labs</a>'),
    ], set(), False, 0))

    # N2 access-control intro/mastery -> NOT a hard dup
    cases.append(("ok_access_control", [
        _mk("II", "04", f'Read the PortSwigger <a href="{PS}/web-security/access-control">Access control</a> path, then work the apprentice-level <a href="{PS}/web-security/all-labs#access-control-vulnerabilities">labs</a>; the practitioner labs follow in Phase III'),
        _mk("III", "05", f'Review your Phase II <a href="{PS}/web-security/access-control">Access control</a> notes, then complete the remaining practitioner <a href="{PS}/web-security/all-labs#access-control-vulnerabilities">labs</a>'),
    ], set(), False, 0))

    # N3 same book, non-overlapping chapters -> NOT a dup
    cases.append(("ok_book_nonoverlap", [
        _mk("II", "01", 'Read <i>WAHH</i> Ch. 1\u20133 as foundational context'),
        _mk("II", "02", 'Read <i>WAHH</i> Ch. 6 and Ch. 7'),
    ], set(), False, 0))

    # N4 unrelated steps -> nothing
    cases.append(("ok_unrelated", [
        _mk("0", "01", 'Set up a Kali Linux virtual machine and configure networking'),
        _mk("V", "02", 'Deploy a vulnerable cloud bucket and enumerate its IAM policy'),
    ], set(), False, 0))

    # C1 content-only duplicate (boilerplate instruction, no shared resource link)
    cases.append(("content_boilerplate", [
        _mk("I", "02", 'For each module: exploit it, write your standard documentation (what, why, fix, code review pattern)'),
        _mk("III", "01", 'For each lab: exploit it, write your standard documentation (what, why, fix, code review pattern)'),
    ], set(), False, 1))

    # P4 THM room completed in two steps -> hard dup
    cases.append(("dup_thm_room", [
        _mk("I", "02", 'Complete the TryHackMe <a href="https://tryhackme.com/room/burpsuitebasics">Burp Suite Basics</a> room in full'),
        _mk("IV", "01", 'Complete the <a href="https://tryhackme.com/room/burpsuitebasics">Burp Suite Basics</a> room again, every task'),
    ], {"thm:burpsuitebasics"}, False, 0))

    # P5 "study" / "do the" recognised as completion verbs
    cases.append(("dup_study_verb", [
        _mk("II", "02", f'Study the PortSwigger <a href="{PS}/web-security/jwt">JWT</a> learning path completely'),
        _mk("III", "07", f'Study the PortSwigger <a href="{PS}/web-security/jwt">JWT</a> material and do the labs'),
    ], {"jwt"}, False, 0))

    # N5 same topic FULL once + PART once -> intro/mastery, NOT a hard dup
    cases.append(("ok_full_then_part", [
        _mk("II", "02", f'Complete the PortSwigger <a href="{PS}/web-security/authentication">Authentication</a> path and all apprentice and practitioner <a href="{PS}/web-security/all-labs#authentication">labs</a>'),
        _mk("III", "09", f'Review your Phase II <a href="{PS}/web-security/authentication">Authentication</a> notes; no new labs'),
    ], set(), False, 0))

    passed = 0; failed = 0
    for name, steps, exp_res, exp_book, exp_content_min in cases:
        f = detect(steps)
        got_res = {t for t, _, _ in f["resource"]}
        got_book = len(f["book"]) > 0
        got_content = len(f["content"])
        ok = (got_res == exp_res) and (got_book == exp_book) and (got_content >= exp_content_min)
        # for the "ok_*" negatives we also require NO hard dup
        if name.startswith("ok_"):
            ok = ok and not got_res and not got_book
        # for content_boilerplate we require it is NOT a resource/book hard dup
        if name == "content_boilerplate":
            ok = ok and not got_res and not got_book
        flag = "PASS" if ok else "FAIL"
        if ok: passed += 1
        else:  failed += 1
        print(f"  [{flag}] {name:22} resource={sorted(got_res)} book={got_book} content={got_content}"
              + ("" if ok else f"   (expected resource={sorted(exp_res)} book={exp_book} content>={exp_content_min})"))
    print(f"\n  SELFTEST (synthetic): {passed} passed, {failed} failed")

    # ---- corpus-level regression checks against the real content file ----
    cfail = 0
    if os.path.exists(SRC_DEFAULT):
        steps = parse_steps(open(SRC_DEFAULT, encoding="utf-8").read())
        f = detect(steps)
        res_topics = {t for t, _, _ in f["resource"]}
        content_pairs = {(a, b) for a, b, _, _, _, _ in f["content"]}
        checks = [
            ("burp resource dup present", "burp-suite" in res_topics),
            ("write-doc boilerplate flagged", (("I", "03"), ("III", "01")) in content_pairs),
            ("frame noise suppressed (auth~deser)", (("II", "02"), ("III", "06")) not in content_pairs),
            ("frame noise suppressed (auth~xss)", (("II", "02"), ("III", "03")) not in content_pairs),
            ("WAHH chapter frame suppressed", (("II", "02"), ("II", "04")) not in content_pairs),
        ]
        for name, ok in checks:
            print(f"  [{'PASS' if ok else 'FAIL'}] corpus: {name}")
            if not ok:
                cfail += 1
    else:
        print("  (corpus file not found; skipped corpus checks)")

    total_fail = failed + cfail
    print(f"\n  SELFTEST TOTAL: {'ALL PASS' if total_fail == 0 else str(total_fail) + ' FAILED'}")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    sys.exit(check())

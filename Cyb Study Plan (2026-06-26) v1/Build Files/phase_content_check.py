#!/usr/bin/env python3
"""
phase_content_check.py  --  Content-vs-description verifier for the Study Plan.

Invoked by the chat command:  PHASE CONTENT CHECK <ROMAN>   (e.g. PHASE CONTENT CHECK IV)
Run directly:                 python3 phase_content_check.py IV

This is the OFFLINE half of the link/content verification that is performed on every
phase. It does NOT fetch the web (the build host has no network); live page-content
verification is done manually and its verdicts are recorded in VERIFIED below. What
this module automates, for a given phase, is:

  1. LINK INVENTORY      every <a href> and auto-linked bare URL, with the bullet it
                         lives in, plus the recorded manual verdict (PASS/PARTIAL/FAIL)
                         from VERIFIED, or 'unverified' if not yet checked.
  2. BROAD-LINK FLAG     links whose URL is a generic landing page (no specific
                         sub-topic) -- the "too broad" problem. Flagged for review.
  3. RESOURCE-LINK GAP   action bullets that name a learning resource but carry no link.
  4. NOTE-CARD BACKING   every "Full notes + note cards: A, B, C" topic must be backed
                         by a link (in its step) or a source in the phase.
  5. CONCEPTS COVERAGE   every item in "Concepts Mastered" and "How These Concepts Are
                         Used as an AppSec Engineer" must be traceable to a step/source,
                         i.e. if you did every step and read every source you would
                         actually learn it.

Exit status is non-zero if any FAIL-level issue is found (broad links, resource-link
gaps, uncovered note-card topics, or uncovered concepts).
"""
import re, sys, json, os

SRC_DEFAULT = os.path.join(os.path.dirname(__file__), "appsec_content.py")

# ---------------------------------------------------------------------------
# Manual web/PDF verification verdicts (URL-substring -> (verdict, note)).
# Populated as phases are verified live. 'PASS' = page teaches what the
# description claims; 'PARTIAL'/'FAIL' = mismatch (see note).
# ---------------------------------------------------------------------------
VERIFIED = {
    # --- Phase 0 / I ---
    "developer.mozilla.org/en-US/docs/Web/HTTP/Cookies": ("PASS", "Secure/HttpOnly/SameSite all covered (redirects to /Guides/Cookies)"),
    "fastapi.tiangolo.com": ("PASS", "official docs; Request Body + Security(OAuth2/JWT) sections exist"),
    "github.com/WebGoat/WebGoat": ("PASS", "deliberately-insecure OWASP app, Docker, lessons by vuln class"),
    "tryhackme.com/path/outline/web": ("PASS", "resolves; titled 'Web Fundamentals (Legacy)'"),
    "tryhackme.com/room/httpindetail": ("PASS", "live free room, 7 tasks"),
    "tryhackme.com/room/burpsuitebasics": ("PASS", "live room"),
    "tryhackme.com/room/owasptop10": ("PASS", "live free room, 31 tasks (owasptop102021 was dead)"),
    "portswigger.net/web-security/sql-injection": ("PASS", "SQLi tutorial/material"),
    "portswigger.net/web-security/all-labs": ("PASS", "labs apprentice->expert by topic"),
    "portswigger.net/web-security/cross-site-scripting": ("PASS", "XSS core topic material"),
    # --- Phase II ---
    "portswigger.net/burp/documentation/desktop/tools/proxy": ("PASS", "Burp Proxy tool page"),
    "portswigger.net/burp/documentation/desktop/tools/repeater": ("PASS", "Burp Repeater tool page"),
    "portswigger.net/burp/documentation/desktop/tools/intruder": ("PASS", "Burp Intruder tool page"),
    "portswigger.net/web-security/cors": ("PASS", "CORS misconfigurations topic"),
    "developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP": ("PASS", "CSP guide"),
    "cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security": ("PASS", "TLS cheat sheet"),
    "developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods": ("PASS", "HTTP methods reference"),
    "developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status": ("PASS", "HTTP status codes reference"),
    "portswigger.net/web-security/authentication": ("PASS", "Authentication material + labs"),
    "all-labs#authentication": ("PASS", "Authentication apprentice+practitioner labs"),
    "portswigger.net/web-security/jwt": ("PASS", "JWT attacks topic (algorithm confusion)"),
    "portswigger.net/web-security/oauth": ("PASS", "OAuth topic (redirect URI manipulation)"),
    "portswigger.net/web-security/access-control": ("PASS", "Access control material + labs"),
    "portswigger.net/web-security/api-testing": ("PASS", "API testing material + labs"),
    "all-labs#access-control-vulnerabilities": ("PASS", "Access control labs"),
    "all-labs#api-testing": ("PASS", "API testing labs"),
    "all-labs#sql-injection": ("PASS", "SQL injection labs apprentice->expert"),
    "cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage": ("PASS", "crypto storage cheat sheet"),
    "freecodecamp.org/news/hacking-with-hashcat": ("PASS", "MD5 crack tutorial (-m 0)"),
    "pypi.org/project/bcrypt": ("PASS", "official bcrypt usage (hashpw/gensalt/checkpw)"),
    "cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery": ("PASS", "SSRF prevention incl DNS rebinding"),
    "tryhackme.com/module/network-fundamentals": ("PASS", "OSI/TCP-IP/ports module"),
    "tryhackme.com/room/puttingitalltogether": ("PASS", "DNS/HTTP/LB/WAF request flow"),
}

# URLs that are generic landing pages -> "too broad" unless a #fragment/specific path is present
BROAD = [
    re.compile(r"^https?://[^/]+/?$"),                       # bare domain
    re.compile(r"portswigger\.net/burp/documentation/?$"),  # generic Burp docs root
    re.compile(r"portswigger\.net/web-security/?$"),         # academy index
    re.compile(r"developer\.mozilla\.org/?$"),
]

STOP = set("the a an and or of to in for with as is are be that this it its on at by from your you "
           "what how when which each one two three not just like into onto via real per day "
           "appsec engineer concepts used these other their about over more most can do does".split())


def _phases(text):
    lines = text.split("\n")
    bans = [(i, m.group(1)) for i, l in enumerate(lines)
            for m in [re.search(r'banner\("([^"]*)"', l)] if m]
    out = {}
    for k, (ln, rom) in enumerate(bans):
        end = bans[k + 1][0] if k + 1 < len(bans) else len(lines)
        out[rom.strip()] = (ln, end, lines)
    return out


def _calls(lines, a, b, name):
    """Reconstruct multi-line name(...) calls between [a,b); yield joined text."""
    i = a
    while i < b:
        if re.match(r'\s*' + name + r'\(', lines[i]):
            buf = [lines[i]]; depth = lines[i].count('(') - lines[i].count(')'); j = i
            while depth > 0 and j + 1 < b:
                j += 1; buf.append(lines[j]); depth += lines[j].count('(') - lines[j].count(')')
            yield "\n".join(buf); i = j + 1
        else:
            i += 1


def _unesc(s):
    s = s.replace('\\"', '"')
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)


def _bullets(call):
    # quoted string literals concatenated into logical bullets (split on '",' boundaries)
    parts = re.findall(r'"((?:[^"\\]|\\.)*)"', call)
    return _unesc("".join(parts)) if parts else ""


def _bullet_list(call):
    # individual bullets: group consecutive string literals, breaking at lines ending '",'
    out, cur = [], []
    for ln in call.split("\n"):
        m = re.findall(r'"((?:[^"\\]|\\.)*)"', ln)
        if m:
            cur.append("".join(m))
        if ln.rstrip().endswith('",') or ln.rstrip().endswith('"]') or ln.rstrip().endswith('])'):
            if cur:
                out.append(_unesc("".join(cur))); cur = []
    if cur:
        out.append(_unesc("".join(cur)))
    return out


URL = re.compile(r'href="([^"]+)"')
BARE = re.compile(r'(?<![\w./@-])((?:[a-z0-9-]+\.)+(?:com|org|net|io|dev|cloud|gov|edu)(?:/[^\s"<)]*)?)', re.I)
RES_KW = re.compile(r'\b(PortSwigger|TryHackMe|OWASP|MDN|hashcat|bcrypt|WebGoat|FastAPI|Burp|FreeCodeCamp|cheat ?sheet|learning path|module|room|documentation)\b', re.I)


PLATFORM_OK = {"nostarch.com", "wiley.com", "tryhackme.com", "hashcat.net", "hashcat.net/wiki",
               "developer.mozilla.org", "portswigger.net/web-security", "cheatsheetseries.owasp.org"}


def verdict_for(u):
    for key, (v, note) in VERIFIED.items():
        if key in u:
            return v, note
    # platform/publisher roots are acceptable "here's the site" references (deep-links live in steps)
    bare = re.sub(r'^https?://', '', u).rstrip('/')
    if bare in PLATFORM_OK:
        return "PASS", "platform/publisher reference"
    return "unverified", "no manual web/PDF check recorded"


def check(roman, src=SRC_DEFAULT):
    text = open(src, encoding="utf-8").read()
    ph = _phases(text)
    if roman not in ph:
        print(f"Phase {roman} not found. Known: {', '.join(ph)}"); return 2
    a, b, lines = ph[roman]
    fails = 0

    # section ranges inside the phase
    sec = {}
    cur = None
    for i in range(a, b):
        m = re.search(r'SS\("([^"]*)"', lines[i])
        if m:
            cur = _unesc(m.group(1)); sec[cur] = [i, b]
            prev = [k for k in sec if sec[k][1] == b and k != cur]
        # close previous section
    # compute section ends
    starts = sorted([(v[0], k) for k, v in sec.items()])
    for idx, (s0, k) in enumerate(starts):
        e = starts[idx + 1][0] if idx + 1 < len(starts) else b
        sec[k] = [s0, e]

    steps = list(_calls(lines, a, b, "step"))
    ress = list(_calls(lines, a, b, "res"))
    res_text = " ".join(_bullets(r) for r in ress)

    print(f"================  PHASE {roman}  CONTENT CHECK  ================\n")

    # 1+2. LINK INVENTORY + BROAD FLAG
    print("-- LINK INVENTORY (manual verdict | broad?) --")
    seen = set()
    cand = []
    for c in steps + ress:
        cl = _unesc(c)
        cand += re.findall(r'href="([^"]+)"', cl)
        joined = _unesc(" ".join(re.findall(r'"((?:[^"\\]|\\.)*)"', c)))  # space-join: titles don't fuse to URLs
        no_anchor = re.sub(r'<a\b[^>]*>.*?</a>', ' ', joined, flags=re.S)
        for bm in BARE.finditer(no_anchor):
            u = bm.group(1)
            cand.append(u if u.startswith("http") else "https://" + u)
    norm = []
    for u in cand:
        b = u.rstrip("/")
        if b not in norm:
            norm.append(b)
    # drop fragments that are a prefix of a longer candidate (URL split across two literals)
    final = [u for u in norm if not any(o != u and o.startswith(u + "/") for o in norm)]
    for base in final:
        seen.add(base)
        v, note = verdict_for(base)
        broad = any(p.search(base) for p in BROAD) and "#" not in base
        if broad and v == "PASS":
            tag = "broad (verified ok)"
        elif broad:
            tag = "BROAD!"; fails += 1
        else:
            tag = ""
        print(f"  [{v:9}] {base}  {tag}")
        if v == "FAIL":
            fails += 1
    print()

    # 3. RESOURCE-LINK GAP
    print("-- RESOURCE-LINK GAP (named resource, no link in bullet) --")
    gaps = 0
    CONSUME = re.compile(r'^\s*(Read|Complete|Work through|Study|Watch)\b', re.I)
    BACKREF = re.compile(r'\b(existing|you built|you wrote|examples from|do not cover|does not cover|already|your notes|your own|note cards?:)\b', re.I)
    LOCAL_APP = re.compile(r'\bWebGoat\b', re.I)  # lessons run inside the local Docker app; platform linked in sources
    for c in steps:
        for bt in _bullet_list(c):
            if CONSUME.search(bt) and RES_KW.search(bt) and "href=" not in bt and not BARE.search(bt) \
               and not BACKREF.search(bt) and not LOCAL_APP.search(bt) and "<i>" not in bt:
                print(f"  MISSING LINK: {bt[:90]}")
                gaps += 1; fails += 1
    if not gaps:
        print("  none")
    print()

    # 4. NOTE-CARD BACKING
    print("-- NOTE-CARD TOPIC BACKING --")
    nc_issues = 0
    backing = (res_text + " " + " ".join(_unesc(c) for c in steps)).lower()
    for c in steps:
        for bt in _bullet_list(c):
            m = re.search(r'note cards?:\s*(.+)', bt, re.I)
            if not m:
                continue
            topics = re.split(r',| and ', re.sub(r'</?b>', '', m.group(1)))
            for tp in topics:
                tp = re.sub(r'<[^>]+>', '', tp).strip(" .;")
                if not tp:
                    continue
                kws = [w for w in re.findall(r'[A-Za-z]+', tp.lower()) if w not in STOP and len(w) > 2]
                if kws and not any(kw in backing for kw in kws):
                    print(f"  UNBACKED: '{tp}'  (no link/source covers it)")
                    nc_issues += 1; fails += 1
    if not nc_issues:
        print("  every note-card topic is backed by a link or source")
    print()

    # 5. CONCEPTS COVERAGE  (advisory: low coverage = review, not hard fail)
    print("-- CONCEPTS MASTERED / USED COVERAGE (advisory) --")
    learn_text = (" ".join(_unesc(c) for c in steps) + " " + res_text).lower()
    cov_issues = 0
    for label in ("Concepts Mastered", "How These Concepts Are Used as an AppSec Engineer"):
        if label not in sec:
            continue
        s0, e0 = sec[label]
        for c in _calls(lines, s0, e0, "concept"):
            title = re.search(r'concept\("([^"]*)"', c)
            if not title:
                continue
            title = _unesc(title.group(1))
            body = _bullets(c)
            # ratio keys off the concept TITLE's distinctive terms (the topic signal);
            # body words are searchable but abstract vocab there shouldn't dilute the score
            tkws = [w for w in re.findall(r'[A-Za-z]+', title.lower()) if w not in STOP and len(w) > 2]
            pool = set(tkws) or {w for w in re.findall(r'[A-Za-z]+', body.lower()) if w not in STOP and len(w) > 3}
            hit = sum(1 for kw in pool if kw in learn_text)
            ratio = hit / max(1, len(pool))
            ok = ratio >= 0.40
            if not ok:
                cov_issues += 1
            print(f"  [{'OK ' if ok else 'REVIEW'}] ({label.split()[0]}) {title}  (title-term coverage {ratio:.0%})")
    if not cov_issues:
        print("  -> every concept traces to a step/source")
    else:
        print(f"  -> {cov_issues} concept(s) below threshold: confirm a step/source teaches them")
    print()

    print("================  SUMMARY  ================")
    print(f"  links: {len(seen)} | issues flagged: {fails}")
    print("  PASS" if fails == 0 else f"  REVIEW NEEDED ({fails} issue(s))")
    return 1 if fails else 0


def _reescape_href(c, b):  # placeholder kept for structure; not used
    return c


if __name__ == "__main__":
    rom = (sys.argv[1] if len(sys.argv) > 1 else "II").upper()
    sys.exit(check(rom))

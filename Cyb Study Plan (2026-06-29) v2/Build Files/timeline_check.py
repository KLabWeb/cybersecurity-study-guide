"""
timeline_check.py — Self-correcting timeline-consistency pass for the Study Plan.

Runs at GENERATE time, BEFORE the PDF build, mirroring the self-correcting TOC loop:
    check -> fix -> check -> fix -> ...   until the source's timeline data is internally
consistent across the whole document, then runs report-only checks for the
judgment-class issues that cannot be auto-resolved without guessing.

Ground-truth convention (verified against Phases III & VII): Month = Week / 4.

AUTO-FIXED (looped until stable) — each has a single deterministic correct value:
    1. Step numbering — steps within a phase must read 01,02,03,... no gaps, no dups.
    2. Phase-duration END must cover the phase's last step (label_end == max_step_week/4):
       catches the "phase labelled to end before its own steps finish" class of bug.
    3. Three-way agreement — a phase's duration in the banner, the timeline chart, and
       the schedule heading must encode the same numeric range (canonical = the banner).

REPORTED (correct value is not deterministically recoverable — surfaced, never guessed):
    4. A step whose week falls outside its phase's [start,end] week-bounds
       (e.g. a Phase II step tagged "Week 5" when Phase II runs weeks 6-9).
    5. Prose directives ("start applying at Month N") that disagree with the canonical
       applying timeline.

The auto-fix loop edits appsec_content.py in place and returns whether it changed it,
so the caller can reload the content module before building.
"""
import re

WEEKS_PER_MONTH = 4.0

# Phases in document order; index in this list == column in the timeline `weeks` chart.
PHASE_ORDER = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

# Canonical values for prose semantic groups (the reconciled timeline). Report-only.
CANON = {
    "applying_start_month": 4,   # "start applying at Month 4"
    "applying_push_month": 6,    # "main application push ... Month 6"
}

# ── low-level string helpers ────────────────────────────────────────────────
def _norm(s):
    """Normalise dashes to '-', then strip any remaining \\uXXXX escapes (e.g. \\u00b7),
    so digit extraction never picks up the '00b7' inside an escape."""
    s = (s.replace("\u2013", "-").replace("\u2014", "-")
          .replace(r"\u2013", "-").replace(r"\u2014", "-"))
    s = re.sub(r"\\u[0-9a-fA-F]{4}", " ", s)
    return s

def _is_month(dur):
    return bool(re.search(r"[Mm]onths?", dur))

def _nums(s):
    return [float(x) for x in re.findall(r"\d+(?:\.\d+)?", _norm(s))]

def _range(s):
    """(lo, hi) from a duration like 'Months 1.5-2.25'; 'Mo 7+' -> (7.0, None); single -> (n,n)."""
    ns = _nums(s)
    if not ns:
        return None
    if "+" in _norm(s) and len(ns) == 1:
        return (ns[0], None)
    if len(ns) == 1:
        return (ns[0], ns[0])
    return (ns[0], ns[1])

_WEEK_RE = re.compile(r"\bW(?:ks?|eeks?)\b\s*(\d+)\s*(?:-\s*(\d+))?")

def _week_span(tag):
    """(first, last) week numbers anchored to the 'Week(s) N[-M]' token, or None for
    day-scoped (phase 0) and month-scoped (parallel 'Month N onward') tags."""
    t = _norm(tag)
    has_week = bool(re.search(r"\bW(?:ks?|eeks?)\b", t))
    if not has_week:
        return None                      # Days... or Month... onward
    m = _WEEK_RE.search(t)
    if not m:
        return None
    a = int(m.group(1))
    b = int(m.group(2)) if m.group(2) else a
    return (a, b)

def _first_week(tag):
    sp = _week_span(tag)
    return sp[0] if sp else None

# day-scale ordering key: unifies Week and Day tags onto one timeline so a phase
# that mixes them (e.g. Phase 0: "Weeks 1-3" alongside "Days 2-4", "Day 1") can be
# sorted by the same ascending start-then-end rule used for week-only phases.
_DAY_RE = re.compile(r"\bDays?\b\s*(\d+)\s*(?:-\s*(\d+))?")

def _order_key(tag):
    """(start_day, end_day) for a step tag, or None if no Week/Day token. Week N -> days
    [(N-1)*7+1 .. N*7]; this is order-preserving vs week numbers, so week-only phases
    sort identically to before, while day-scoped steps interleave correctly."""
    t = _norm(tag)
    m = _WEEK_RE.search(t)
    if m:
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        return ((a - 1) * 7 + 1, b * 7)
    m = _DAY_RE.search(t)
    if m:
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
        return (a, b)
    return None

# ── parsing the source ──────────────────────────────────────────────────────
_BANNER_RE = re.compile(r'banner\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)')
_STEP_RE   = re.compile(r'step\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"', re.S)
_SS_RE     = re.compile(r'SS\(\s*"([^"]*)"\s*\)')
_CHART_RE  = re.compile(r'weeks\s*=\s*\[(.*?)\]', re.S)

def _phase_at(pos, banners):
    """Return the roman of the phase whose banner most recently precedes `pos`."""
    cur = None
    for roman, _t, _d, span in banners:
        if span[0] <= pos:
            cur = roman
        else:
            break
    return cur

def parse(text):
    banners = [(m.group(1), m.group(2), m.group(3), m.span())
               for m in _BANNER_RE.finditer(text)]
    steps = [{"phase": _phase_at(m.start(), banners),
              "num": m.group(1), "label": m.group(2), "tag": m.group(3),
              "span": m.span()} for m in _STEP_RE.finditer(text)]
    ss = [{"phase": _phase_at(m.start(), banners), "text": m.group(1), "span": m.span()}
          for m in _SS_RE.finditer(text)]
    chart = None
    cm = _CHART_RE.search(text)
    if cm:
        base = cm.start(1)
        chart = [(mm.group(1), (base + mm.start(1), base + mm.end(1)))
                 for mm in re.finditer(r'"([^"]*)"', cm.group(1))]
    return banners, steps, ss, chart

# ── AUTO-FIX 0: order each phase's steps by (start_week, end_week) ───────────
_STEP_HEAD = re.compile(r'^(\s*)step\("([^"]*)",\s*"([^"]*)",\s*"([^"]*)"')
_CLOSE     = re.compile(r'^\s*\]\)\s*$')

def reorder_steps(text):
    """Sort each phase's run of consecutive step() blocks into ascending
    (start_week, end_week) order, so they read chronologically. Only a run where
    EVERY step carries a week span is touched (day-scoped runs like the Phase-0
    pre-study setup are left as authored). Block contents are moved verbatim;
    renumbering to 01,02,... is left to fix_step_numbering, which runs next."""
    lines = text.split("\n")
    banner_lines = [i for i, l in enumerate(lines) if re.search(r'banner\("', l)]
    def phase_of(i):
        p = None
        for b in banner_lines:
            if b <= i: p = b
            else: break
        return p
    blocks = []
    i, n = 0, len(lines)
    while i < n:
        m = _STEP_HEAD.match(lines[i])
        if m:
            j = i
            while j < n and not _CLOSE.match(lines[j]):
                j += 1
            blocks.append({"s": i, "e": j, "tag": m.group(4), "phase": phase_of(i)})
            i = j + 1
        else:
            i += 1
    # group immediately-adjacent blocks within the same phase
    groups, cur = [], []
    for b in blocks:
        if cur and b["s"] == cur[-1]["e"] + 1 and b["phase"] == cur[-1]["phase"]:
            cur.append(b)
        else:
            if cur: groups.append(cur)
            cur = [b]
    if cur: groups.append(cur)

    fixes = []
    for g in sorted(groups, key=lambda gr: gr[0]["s"], reverse=True):  # bottom-up
        spans = [_order_key(b["tag"]) for b in g]
        if any(sp is None for sp in spans):
            continue                                    # a step with no Week/Day token
        order_now = list(range(len(g)))
        order_new = sorted(order_now, key=lambda k: spans[k])
        if order_new == order_now:
            continue
        texts = ["\n".join(lines[b["s"]:b["e"] + 1]) for b in g]
        a, z = g[0]["s"], g[-1]["e"]
        lines[a:z + 1] = "\n".join(texts[k] for k in order_new).split("\n")
        fixes.append("reordered " + str(len(g)) + " steps by time ["
                     + " ".join(f"{spans[k][0]}-{spans[k][1]}" for k in order_new) + "]")
    return "\n".join(lines), fixes

# ── AUTO-FIX 1: step numbering sequential per phase ─────────────────────────
def fix_step_numbering(text):
    _, steps, _, _ = parse(text)
    fixes = []
    by_phase = {}
    for s in steps:
        by_phase.setdefault(s["phase"], []).append(s)
    # edits as (span_of_num_literal, new_text); apply right-to-left to keep spans valid
    edits = []
    for phase, group in by_phase.items():
        for idx, s in enumerate(group, start=1):
            want = f"{idx:02d}"
            if s["num"] != want:
                # locate the exact "<num>" literal at the start of this step() call
                seg = text[s["span"][0]:s["span"][1]]
                rel = seg.index(f'"{s["num"]}"')
                a = s["span"][0] + rel
                b = a + len(f'"{s["num"]}"')
                edits.append((a, b, f'"{want}"'))
                fixes.append(f'Phase {phase}: step "{s["num"]}" -> "{want}" ({s["label"][:34]})')
    for a, b, rep in sorted(edits, reverse=True):
        text = text[:a] + rep + text[b:]
    return text, fixes

# ── AUTO-FIX 2 & 3: duration end-coverage + banner/chart/SS three-way agreement ─
def _phase_step_weeks(steps):
    """phase roman -> (min_first_week, max_last_week) over steps that carry week numbers."""
    out = {}
    for s in steps:
        sp = _week_span(s["tag"])
        if sp is None:
            continue
        lo, hi = sp
        if s["phase"] in out:
            a, b = out[s["phase"]]
            out[s["phase"]] = (min(a, lo), max(b, hi))
        else:
            out[s["phase"]] = (lo, hi)
    return out

def _fmt(prefix, lo, hi):
    def g(x):
        return str(int(x)) if float(x).is_integer() else str(x)
    if hi is None:
        return f"{prefix} {g(lo)}+"
    return f"{prefix} {g(lo)}\u2013{g(hi)}"

def fix_durations(text):
    banners, steps, ss, chart = parse(text)
    fixes = []
    edits = []   # (abs_a, abs_b, new_literal)
    sw = _phase_step_weeks(steps)

    # canonical numeric range per phase = banner range, but END raised to cover last step
    canon = {}
    for roman, title, dur, span in banners:
        rng = _range(dur)
        if rng is None:
            continue
        lo, hi = rng
        if roman in sw and hi is not None:
            step_end = sw[roman][1] / WEEKS_PER_MONTH if _is_month(dur) else sw[roman][1]
            # only RAISE the end to cover steps; never silently shrink an intentional buffer
            if step_end > hi + 1e-9:
                fixes.append(f"Phase {roman}: duration end {hi} -> {step_end} (covers last step)")
                hi = step_end
        canon[roman] = (lo, hi)

    # rewrite each banner whose end we raised
    for roman, title, dur, span in banners:
        if roman not in canon:
            continue
        lo, hi = canon[roman]
        rng = _range(dur)
        if rng and (abs(rng[0] - lo) > 1e-9 or (rng[1] is not None and hi is not None and abs(rng[1] - hi) > 1e-9)):
            prefix = "Months" if _is_month(dur) else "Weeks"
            new_dur = _fmt(prefix, lo, hi)
            seg = text[span[0]:span[1]]
            rel = seg.rfind(f'"{dur}"')
            a = span[0] + rel
            edits.append((a, a + len(f'"{dur}"'), f'"{new_dur}"'))

    # three-way agreement: chart entry (by column) must match canonical banner range
    if chart:
        for i, roman in enumerate(PHASE_ORDER):
            if i >= len(chart) or roman not in canon:
                continue
            cstr, (ca, cb) = chart[i]
            crng = _range(cstr)
            lo, hi = canon[roman]
            if crng and (abs(crng[0] - lo) > 1e-9 or
                         ((crng[1] is None) != (hi is None)) or
                         (crng[1] is not None and hi is not None and abs(crng[1] - hi) > 1e-9)):
                prefix = "Wks" if cstr.strip().startswith("Wk") else "Mo"
                new_c = _fmt(prefix, lo, hi)
                edits.append((ca, cb, new_c))
                fixes.append(f"Phase {roman}: timeline-chart '{cstr}' -> '{new_c}' (match banner)")

    # three-way agreement: schedule SS headings that carry a duration
    for s in ss:
        roman = s["phase"]
        if roman not in canon:
            continue
        if not re.search(r"(Months?|Weeks?)\s*\d", s["text"]):
            continue
        srng = _range(s["text"])
        lo, hi = canon[roman]
        if srng and (abs(srng[0] - lo) > 1e-9 or
                     (srng[1] is not None and hi is not None and abs(srng[1] - hi) > 1e-9)):
            prefix = "Months" if re.search(r"Months?", s["text"]) else "Weeks"
            # replace the trailing "<prefix> <range>" inside the SS title, keep the lead text
            new_tail = _fmt(prefix, lo, hi)
            new_title = re.sub(r"(Months?|Weeks?)\s*\d[\d.]*\s*(?:[\u2013\u2014-]|\\u201[34])\s*\d[\d.]*",
                               new_tail, s["text"])
            if new_title != s["text"]:
                seg = text[s["span"][0]:s["span"][1]]
                rel = seg.index(f'"{s["text"]}"')
                a = s["span"][0] + rel
                edits.append((a, a + len(f'"{s["text"]}"'), f'"{new_title}"'))
                fixes.append(f"Phase {roman}: schedule heading range -> '{new_tail}' (match banner)")

    for a, b, rep in sorted(edits, reverse=True):
        text = text[:a] + rep + text[b:]
    return text, fixes

# ── REPORT-ONLY checks ──────────────────────────────────────────────────────
def report_only(text):
    banners, steps, ss, chart = parse(text)
    issues = []

    # (4) steps outside their phase's week-bounds
    bounds = {}
    for roman, title, dur, span in banners:
        rng = _range(dur)
        if not rng:
            continue
        is_month = _is_month(dur)
        lo, hi = rng
        if is_month:
            lo_w = lo * WEEKS_PER_MONTH
            hi_w = (hi * WEEKS_PER_MONTH) if hi is not None else None
        else:
            lo_w, hi_w = lo, hi
        bounds[roman] = (lo_w, hi_w)
    for s in steps:
        sp = _week_span(s["tag"])
        if sp is None or s["phase"] not in bounds:
            continue
        lo_w, hi_w = bounds[s["phase"]]
        f, l = sp
        if f < lo_w - 1e-9:
            issues.append(f'ORDER: Phase {s["phase"]} step "{s["num"]}" ({s["label"][:30]}) '
                          f'tagged week {f}, but the phase starts at week {lo_w:g} '
                          f'-> a step appears before its phase begins')
        if hi_w is not None and l > hi_w + 1e-9:
            issues.append(f'ORDER: Phase {s["phase"]} step "{s["num"]}" ({s["label"][:30]}) '
                          f'tagged week {l}, past the phase end week {hi_w:g}')

    # (5) prose "start applying at Month N" must equal the canonical start month
    for m in re.finditer(r"[Ss]tart applying at Month\s*(\d+)", _norm(text)):
        n = int(m.group(1))
        if n != CANON["applying_start_month"]:
            issues.append(f'PROSE: "start applying at Month {n}" disagrees with canonical '
                          f'start Month {CANON["applying_start_month"]}')
    return issues

# ── driver: looped check -> fix until stable, then report ────────────────────
def reconcile(src_path, max_passes=8, log=print):
    changed_any = False
    all_fixes = []
    for p in range(1, max_passes + 1):
        with open(src_path, encoding="utf-8") as f:
            text = f.read()
        t0, f0 = reorder_steps(text)
        t1, f1 = fix_step_numbering(t0)
        t2, f2 = fix_durations(t1)
        fixes = f0 + f1 + f2
        if t2 != text:
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(t2)
            changed_any = True
            all_fixes += fixes
            log(f"  Timeline pass {p}: applied {len(fixes)} fix(es): "
                + "; ".join(fixes))
        else:
            if p == 1:
                log("  Timeline pass 1: source already internally consistent \u2014 no fixes.")
            else:
                log(f"  Timeline pass {p}: stable after {len(all_fixes)} total fix(es).")
            break
    else:
        log(f"  ** WARNING: timeline did not stabilise after {max_passes} passes.")

    with open(src_path, encoding="utf-8") as f:
        issues = report_only(f.read())
    if issues:
        log(f"  Timeline review needed ({len(issues)} item(s) — not auto-fixable):")
        for it in issues:
            log(f"    - {it}")
    else:
        log("  Timeline review: all steps within phase bounds; prose directives consistent. \u2713")
    return changed_any, all_fixes, issues

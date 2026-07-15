#!/usr/bin/env python3
"""
timeline_ref_check.py -- catches TIMELINE REFERENCES IN PROSE that report_only() misses.
report_only()/reconcile() validate the banner/chart/schedule/step-tag machinery; they do NOT
read paragraphs or callout boxes, where hard-coded months/weeks go stale when a phase moves.
This derives the phase map from the banners, then flags prose that disagrees.

Exposes check(path) -> list of issues (for build_appsec.py). Run directly: exits 1 if issues.
"""
import re, sys

def _clean(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
def _de(s):    return s.replace("\\u2013", "-").replace("\u2013", "-")

def check(path="appsec_content.py", verbose=True):
    LINES = open(path, encoding="utf-8").read().split("\n")

    # ---- phase map (months) from banners; weeks->months via /4 ----
    PH = {}
    for l in LINES:
        m = re.search(r'banner\("([0IVX]+)", "[^"]*", "([^"]+)"', l)
        if not m: continue
        roman, dur = m.group(1), _de(m.group(2))
        nums = [float(x) for x in re.findall(r'\d+\.?\d*', dur.split("\u00b7")[0])]
        if not nums: continue
        wk = ("Week" in dur or "Wks" in dur)
        lo = nums[0]/4 if wk else nums[0]
        hi = (nums[1]/4 if wk else nums[1]) if len(nums) > 1 else lo
        PH[roman] = (round(lo, 2), round(hi, 2))

    SECPLUS_DONE = PH["VII"][1]
    Ph8_START    = PH["VIII"][0]
    PLAN_END     = max(hi for _, hi in PH.values())
    BURP_END_WK  = None
    for l in LINES:
        if 'Burp Suite Mastery' in l and 'step(' in l:
            BURP_END_WK = int(re.findall(r'\d+', _de(re.search(r'", "([^"]+)", \[', l).group(1)))[-1])
    WORD = {w:n for n,w in enumerate("zero one two three four five six seven eight nine ten "
                                     "eleven twelve".split())}
    issues = []

    for i, l in enumerate(LINES, 1):
        t = _de(_clean(l))
        # (a) Security+ "... at Month N"
        m = re.search(r'Security\+.*?Month (\d+\.?\d*)', t) or re.search(r'Month (\d+\.?\d*).*Security\+', t)
        if m and abs(float(m.group(1)) - SECPLUS_DONE) > 0.3:
            issues.append((i, f'Security+ ref Month {m.group(1)}; Phase VII now ends Month {SECPLUS_DONE}', t))
        # (b) interview-prep "save this for Month N"
        m = re.search(r'save this for Month (\d+\.?\d*)', t)
        if m and abs(float(m.group(1)) - Ph8_START) > 0.3:
            issues.append((i, f'Interview-prep ref Month {m.group(1)}; Phase VIII now starts Month {Ph8_START}', t))
        # (c) duration ranges: digit "N to/-M months" and spelled-out "seven to eight months"
        for m in re.finditer(r'(\d+)\s*(?:to|-)\s*(\d+)\s*months', t):
            if int(m.group(2)) < PLAN_END - 0.4:
                issues.append((i, f'Duration "{m.group(1)}-{m.group(2)} months"; plan now ~Month {PLAN_END:.1f}', t))
        for m in re.finditer(r'([a-z]+)\s+to\s+([a-z]+)\s+months', t):
            if m.group(1) in WORD and m.group(2) in WORD and WORD[m.group(2)] < PLAN_END - 0.4:
                issues.append((i, f'Duration "{m.group(1)} to {m.group(2)} months"; plan now ~Month {PLAN_END:.1f}', t))
        # (d) "N months is the outer bound" (only the OUTER bound must track plan end; optimistic may be less)
        for m in re.finditer(r'(\d+) months is the outer bound', t):
            if int(m.group(1)) < PLAN_END - 0.4:
                issues.append((i, f'Outer bound "{m.group(1)} months"; plan now ~Month {PLAN_END:.1f}', t))
        # (e) Burp "By end of Week N"
        m = re.search(r'By end of Week (\d+)', t)
        if m and BURP_END_WK and int(m.group(1)) != BURP_END_WK:
            issues.append((i, f'"By end of Week {m.group(1)}"; Burp Mastery step now ends Week {BURP_END_WK}', t))

    if verbose:
        print("Phase map:", " ".join(f"{r}:{lo}-{hi}" for r,(lo,hi) in PH.items()))
        print(f"Anchors -> Security+ done:{SECPLUS_DONE}  Ph.VIII start:{Ph8_START}  plan end:{PLAN_END}  Burp end wk:{BURP_END_WK}")
        if issues:
            print(f"{len(issues)} STALE PROSE REFERENCE(S):")
            for ln, why, ctx in issues:
                print(f"  L{ln}: {why}\n        \"{ctx[:105]}\"")
        else:
            print("PASS - no stale prose timeline references.")
    return issues

if __name__ == "__main__":
    sys.exit(1 if check() else 0)

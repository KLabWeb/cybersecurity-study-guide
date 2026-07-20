#!/usr/bin/env python3
"""
timeline_boundary_check.py -- verifies phase month-boundaries are correct and CONTIGUOUS.

A phase covering step weeks [A..B] spans months [(A-1)/4 .. B/4]: the START of week A is
(A-1)/4, the END of week B is B/4. Consecutive phases therefore share a boundary (no gap).
report_only() only checked END coverage, so a start computed as A/4 instead of (A-1)/4 --
which invents a phantom quarter-month gap between phases -- slipped through. This check
catches exactly that. Weeks are read only from "Week(s) N" tokens so stray tag numbers
(e.g. "Month 4 onward") don't pollute the min/max.

Exposes check(path) -> list of issues. Run directly: exits 1 if any.
"""
import re, sys

def _de(s): return s.replace("\\u2013", "-").replace("\u2013", "-")

def check(path="appsec_content.py", verbose=True):
    L = open(path, encoding="utf-8").read().split("\n")
    ph = "?"; wk = {}; ban = {}
    for l in L:
        b = re.search(r'banner\("([0IVX]+)", "[^"]*", "([^"]+)"', l)
        if b: ph = b.group(1); ban[ph] = _de(b.group(2))
        s = re.search(r'step\("\d+", .*, "([^"]+)", \[\s*$', l)
        if s:
            d = _de(s.group(1))
            wk.setdefault(ph, []).extend(int(x) for x in
                re.findall(r'Weeks?\s+(\d+)', d) + re.findall(r'-\s*(\d+)', d))
    issues = []

    # (1) per-phase: month-based banner must match its step weeks
    for p, weeks in wk.items():
        b = ban.get(p, "")
        if "Month" not in b: continue                      # week-based banner -> skip
        w = sorted(set(weeks)); fw, lw = w[0], w[-1]
        cs, ce = round((fw - 1) / 4, 3), round(lw / 4, 3)
        nums = re.findall(r'\d+\.?\d*', b.split("\u00b7")[0])
        bs = float(nums[0]); be = float(nums[1]) if len(nums) > 1 else bs
        if abs(bs - cs) > 1e-6:
            issues.append((p, f"banner START {bs:g} != (week {fw}-1)/4 = {cs:g}  [invents a gap before this phase]"))
        if abs(be - ce) > 1e-6:
            issues.append((p, f"banner END {be:g} != week {lw}/4 = {ce:g}"))

    # (2) contiguity across ALL month-based phases (covers VIII/IX which have no week steps)
    order = [p for p in ["II","III","IV","V","VI","VII","VIII","IX"] if p in ban and "Month" in ban[p]]
    prev_end = None
    for p in order:
        nums = re.findall(r'\d+\.?\d*', ban[p].split("\u00b7")[0])
        s0 = float(nums[0]); e0 = float(nums[1]) if len(nums) > 1 else None
        if prev_end is not None and abs(s0 - prev_end) > 1e-6:
            issues.append((p, f"start {s0:g} != previous phase end {prev_end:g}  [phantom gap/overlap]"))
        if e0 is not None: prev_end = e0

    if verbose:
        if issues:
            print(f"{len(issues)} PHASE-BOUNDARY ISSUE(S):")
            for p, why in issues: print(f"  Phase {p}: {why}")
        else:
            print("PASS - phase month-boundaries contiguous (no phantom gaps).")
    return issues

if __name__ == "__main__":
    sys.exit(1 if check() else 0)

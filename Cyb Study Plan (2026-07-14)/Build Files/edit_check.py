#!/usr/bin/env python3
"""
edit_check.py - mechanical lint for appsec_content.py. Run after every edit batch:
    python3 edit_check.py     # exit 1 on any HARD failure
Enforces ONLY rules that are 100% mechanical with zero false positives:
  B. OWASP LLM IDs ascending within any bullet/paragraph (LLM01 before LLM02 ...).
  C. non-self-closing <a ...> tags are balanced with </a> (content strings only).
  D. every internal link href="#x" has a matching <a name="x"/> (no dead internal links).
NOT auto-checked (would cry wolf): learning-path<->labs pairing, vagueness, rambling,
missing links, conciseness. Those stay human judgment + search-key review.
"""
import ast, re, sys
src = open("appsec_content.py", encoding="utf-8").read()
tree = ast.parse(src)
hard = []
LLM = re.compile(r'LLM(\d+)')
ATAG = re.compile(r'<a\b[^>]*>')

for n in ast.walk(tree):
    if isinstance(n, ast.Constant) and isinstance(n.value, str):
        v = n.value
        ids = [int(x) for x in LLM.findall(v)]
        if ids and ids != sorted(ids):
            hard.append(f"[B] OWASP LLM IDs not sequential {ids}: {v[:65]!r}")
        if len(v) > 15:  # skip short code/helper fragments
            opens = [t for t in ATAG.findall(v) if not t.rstrip().endswith('/>')]  # exclude self-closing
            if len(opens) != v.count('</a>'):
                hard.append(f"[C] unbalanced <a>..</a> ({len(opens)} open, {v.count('</a>')} close): {v[:60]!r}")

names = set(re.findall(r'<a name=\\?"([^"\\]+?)"\s*/?>', src))
for h in sorted(set(re.findall(r'href=\\?"#([^"\\]+?)"', src)) - names):
    hard.append(f"[D] dead internal link href=#{h} (no matching <a name=\"{h}\"/>)")

print("=== edit_check.py (B:LLM order  C:anchor balance  D:internal links) ===")
if hard:
    print(f"HARD FAILURES ({len(hard)}):")
    for x in hard: print("  X", x)
else:
    print("PASS - all mechanical checks clean.")
print("(Judgment rules NOT auto-checked: labs pairing, vagueness, missing links, conciseness.)")
sys.exit(1 if hard else 0)

# Build commands

## IMPLEMENT CHANGES AS NEW COMMIT  (two-step, gated)
Working copy is edited IN this persistent repo dir, so a draft (uncommitted working tree) survives
turn resets and its diff stays reviewable until confirmed.

### Step 1 — DRAFT + DIFF (no commit, no build tag)
1. Restore/confirm working source at the current build.
2. Do the research / doc lookups needed to implement the change correctly.
3. Make the edits in the working tree (SOURCE ONLY, no render).
4. Validate: ast.parse + timeline report_only + step_dedup + AST render-path.
5. Show `git diff` (working tree vs current build tag) — the full draft, every changed character.
6. STOP. Ask the user to confirm. Do NOT commit yet.
   - If the user wants changes: adjust the working tree, re-validate, re-show the diff, ask again.
   - To abandon: `git checkout -- .` discards the draft.

### Step 2 — COMMIT (only after the user confirms / says continue)
7. Append the CHANGELOG_APPLIED.md entry.
8. git commit the change; tag it build-N (N = previous build + 1).
9. Report the new BUILD VERSION NUMBER (build-N).

Notes: PDFs/zips are gitignored (diff SOURCE, not binaries). GENERATE PDF stays a separate explicit
render+present step. Build tags mark confirmed, reviewable versions; drafts and meta/doc commits do not
advance the build number.

## edit_check.py (mechanical gate - run after every edit batch, before showing results)
`python3 edit_check.py` (exit 1 = fail). Enforces ONLY what code can reliably verify:
  B. OWASP LLM IDs ascending within a bullet/paragraph.
  C. <a>..</a> balance (self-closing <a name/> anchors handled).
  D. every href="#x" has a matching <a name="x"/> (no dead internal links).
It does NOT and CANNOT check: labs pairing, vagueness, rambling, or missing links -
those are judgment, verified by the human via search-key diffs.

# Application Security Study Plan — Build Package

## What's here
- **build_appsec.py** — entry point. Run: `python3 build_appsec.py`
- **appsec_infrastructure.py** — styling engine (colors, fonts, cover, header/footer).
- **appsec_content.py** — all document content.
- **timeline_check.py** — self-correcting timeline reconciliation (runs automatically in build).
- **phase_content_check.py** — content-vs-description verifier for a phase (link inventory + verdicts,
  broad-link flag, resource-link gaps, note-card backing, Concepts-Mastered/Used coverage). Offline; does
  not build the PDF.
- **appsec_toc_state.json** — converged table-of-contents page map (seed for the self-correcting TOC pass).
- **fonts/** — DejaVuSans / DejaVuSans-Bold TTFs. Used automatically if system DejaVu fonts aren't installed.
- **CHANGELOG_APPLIED.md** — full history of every edit applied.
- **HANDOFF.md** — project handoff notes.
- **Study_Plan_-_2026-05-26_SOURCE.pdf** — original reconstruction source (reference).
- **Study_Plan_-_<latest>_LATEST.pdf** — latest generated output (50 pp).

## Build
```
pip install reportlab pypdf pdfplumber
python3 build_appsec.py
```
Output: `Study_Plan_-_<today>.pdf` (in /mnt/user-data/outputs if present, else next to the script).
The build auto-runs the timeline reconciliation and a self-correcting TOC loop, printing TOC-vs-actual page verification.

## Verify a phase's links & coverage
```
python3 build_appsec.py CONTENT-CHECK <ROMAN>     # e.g. CONTENT-CHECK II
# or:  python3 phase_content_check.py <ROMAN>
```
Reports, for that phase: every link with its manual verdict, any too-broad links, action bullets missing a link,
whether each "note cards" topic is backed by a source, and whether every Concept-Mastered / Used item traces to a
step or source. Offline analysis only — it never generates the PDF.

## Requirements
Python 3, reportlab (PDF), pypdf + pdfplumber (verification). DejaVu fonts are bundled in fonts/.

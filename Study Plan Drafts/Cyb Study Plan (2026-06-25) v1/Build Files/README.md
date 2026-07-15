# Application Security Engineering — Study Plan (build package)

Self-contained source for generating the **Application Security Engineering — Study Plan** PDF
(Independent Self-Study, Kyle Miskell). Everything needed to rebuild is in this archive.

Snapshot date: **2026-06-25**. Current build: **48 pages**, all 24 changelist items applied.

## Files

| File | Purpose |
|---|---|
| `build_appsec.py` | Entry point. Builds the PDF and runs the self-correcting TOC loop. **Run this.** |
| `appsec_content.py` | All document content via `build_content(...)` (front matter, Phases 0–IX, Appendix, TOC). |
| `appsec_infrastructure.py` | Styling engine: colors, paragraph styles, `Cover`, header/footer, fonts, `OUTPUT` path. |
| `appsec_toc_state.json` | Saved `{toc_title: page}` map so the TOC converges in ~1 pass on the next build. |
| `fonts/DejaVuSans.ttf`, `fonts/DejaVuSans-Bold.ttf` | Bundled fonts (used if the system DejaVu fonts aren't found). |
| `requirements.txt` | Python dependencies (`reportlab`, `pdfplumber`). |
| `CHANGELOG_APPLIED.md` | Full ledger of every change applied to the document. |
| `Study_Plan_-_2026-06-25.pdf` | The latest built output (reference). |
| `Study_Plan_-_2026-05-26_SOURCE.pdf` | The original source document (reference / comparison). |

## How to build

```bash
pip install -r requirements.txt
python build_appsec.py
```

The output is written as `Study_Plan_-_YYYY-MM-DD.pdf` (today's date). In this hosted environment
it lands in `/mnt/user-data/outputs/`; run locally, it lands next to the scripts. All three `.py`
files plus `appsec_toc_state.json` must sit in the same directory.

## Behaviors baked into the build

- **Date-based filename** — `OUTPUT` uses `datetime.date.today()`, so each build self-dates.
- **Self-correcting Table of Contents** — `main()` runs a build → scan → fix → rebuild loop:
  it renders the PDF, scans the *actual* page each section lands on (via `pdfplumber` text
  extraction; no image rendering), and if any TOC page number is wrong it overrides the numbers
  and rebuilds. It repeats until the printed TOC matches the actual pages (handling the case where
  changing a number's digit count shifts later pages), then prints a final per-section
  verification. Section-level page numbers are reconciled; TOC sub-entries are descriptive labels
  with no page numbers.
- **Portable paths** — fonts, the state file, and the output directory fall back gracefully, so the
  build works both in this environment and locally without edits.

## Continuing in a new conversation

Re-upload this archive and ask to continue; the assistant can unzip it and pick up the build.
Editing convention used in this project: source edits only ("BUILD PDF") until an explicit
"GENERATE PDF" actually runs `build_appsec.py`.

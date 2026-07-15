# HANDOFF — Application Security Engineering Study Plan PDF Reconstruction

## Statement for the assistant (future Claude session)

**Read this first.** You are Claude, continuing a multi-session task for a user (Kyle
Miskell). Your role is **PDF reconstruction engineer**: you are rebuilding a 49-page
PDF, "Application Security Engineering — Study Plan," from scratch in Python/reportlab so
that the output matches a source PDF as exactly as possible in both text and formatting.

This task has already spanned several sessions (each compacted into a transcript). The
work is **complete and verified** as of the last session — the PDF builds cleanly to 49
pages with every section, banner, and footer landing on the exact source page. If the
user reports a new discrepancy, your job is to fix it without regressing what already
matches.

### How to resume
1. Put `appsec_infrastructure.py`, `appsec_content.py`, and `build_appsec.py` in a
   writable working dir (e.g. `/home/claude/`).
2. `pip install reportlab pdfplumber --break-system-packages` (network may be disabled;
   reportlab/pdfplumber are usually preinstalled).
3. Run `python3 build_appsec.py` → writes the PDF to
   `/mnt/user-data/outputs/Study_Plan_-_2026-05-26.pdf` and prints a section-page scan.
4. The source PDF (`Study_Plan_-_2026-05-26_SOURCE.pdf` in this archive, or re-uploaded
   to `/mnt/user-data/uploads/`) is the fidelity reference. It is NOT needed to build —
   only to compare against. Use `pdfplumber` for forensic measurement (exact colors,
   coordinates, fonts, rect/line geometry). `pymupdf` was unavailable last session.

### Working method that has worked well
- Measure the source with `pdfplumber` (`.chars`, `.rects`, `.lines`, `.annots`); do not
  trust visual screenshots for colors — Draftable comparison images color-code their own
  diffs (red/blue), which is NOT the document's formatting.
- After any change: validate syntax (`ast.parse`), rebuild, then re-verify page count,
  phase-banner pages, footer numbers, and the specific thing you changed by rendering the
  page to PNG and viewing it.

---

## What the project is

A career-transition self-study plan (front matter → Phases 0–IX → Appendix). Title:
"Application Security Engineering — Study Plan"; subtitle "Independent Self-Study — Kyle
Miskell". 49 pages: a dark cover (idx 0) + 48 numbered pages where the printed page
number equals the pdfplumber page index.

## The files (all required to build, except where noted)

| File | Role |
|---|---|
| `appsec_infrastructure.py` | Styling/layout engine: color constants, paragraph styles (`S` dict), helper flowables (`rule`, `bi`, `nb`, `banner`, `grid_table`), the `Cover` class, and `make_header_footer`. Defines `OUTPUT` path. |
| `appsec_content.py` | All document content: `build_content(...)` lays out every section/phase/appendix. Local helpers at top: `P`, `B`, `H`, `SS`, `step`, `concept`, `res`, plus `linkify()` (wraps bare URLs in clickable blue `<a href>` links). |
| `build_appsec.py` | Entry point. Builds `SimpleDocTemplate` (letter), draws `Cover` on page 1 and `make_header_footer` on later pages, calls `build_content`, runs a section-page scan. |
| `appsec_toc_state.json` | Auto-generated TOC page-number state (regenerates if absent). Optional. |
| `Study_Plan_-_2026-05-26_SOURCE.pdf` | The original/reference PDF. Reference only — not needed to build. |
| `Study_Plan_-_2026-05-26.pdf` | The current build output (what you produced). |

## Verified-good state (last session)
- 49 pages. Phase banners land on source pages: 0=16, I=19, II=22, III=27, IV=30, V=34,
  VI=37, VII=40, VIII=42, IX=45; Appendix=47. All 49 footer page numbers + their
  left/right (odd/even) positions match source. Cover matches.

## Fidelity fixes applied (most recent rounds)
- **URLs**: every bare web URL is a clickable hyperlink (`<a href="https://…">`) colored
  `#3A7AB8`, no underline — matches source link color exactly.
- **Tables**: body cells left-aligned (`tc` style = `TA_LEFT`) to kill justification gaps
  in the Philadelphia "Examples" column.
- **Note boxes (`nb`)**: fill `#F0F4FF`, border `#AABBDD`, text `#1A2A5E`, justified.
  Bold lead-ins: "The structural argument:", "Timeline:", "Net assessment:" are **bold**;
  the First Days box lead-in is plain.
- **"Start applying at Month 3–4…"**: rendered as an `nb` blue box (was grey text).
- **Phase Timeline (idx 10)**: a solid 11-column colored grid, all-white centered text,
  `rowHeights=[24,38,24]`. Column hex colors in order:
  `#2C3E50 #1B4F72 #1A5276 #154360 #0E6655 #145A32 #6E2F1A #6E2F3E #4A235A #2E4057 #212F3C`.
  Romans row = `0 I II III IV V VI VII VIII IX` on the first ten columns, **blank** on the
  11th (First Days). Names/weeks as in source.
- **Phase I**: removed the forced `CondPageBreak` before "How These Concepts Are Used" — it
  now flows mid-page like the source.
- **Pagination repair**: removing that break shifted later pages, so `bulsm` `spaceAfter`
  was raised (2→4) to match the source's slightly looser concept spacing, restoring full
  alignment. The Appendix "Practical Use Per Phase" entries were then tightened locally
  (`spaceAfter=1`) so they fit one page. Net result: back to 49 aligned pages.
- **Appendix Books table**: widened "Phase" column to echo the source's distinctive
  proportions (`[1.25in, 0.6in, 2.3in, rest]`) while staying on-page/readable. NOTE: the
  *source* table actually overflows both page margins (a generator bug); we deliberately
  did NOT reproduce that bleed.
- **Cert costs**: GWEB = `~$999`, CSSLP = `~$599` (source's "9" wrapped to a 2nd line and
  had been misread as `~$99` / `~$59`). Phase = "Post-job" for both.

## Source quirks deliberately preserved (faithful to original)
- TOC labels "II … 19" and "VIII — Expected First Days … 45".
- Phase II duplicate "Networking as an attack surface" concept.
- Phase VI intro begins "Phase V builds…".
- Phase IV step numbering 01,02,03,05,05,06,07,08 (no 04; a 05 repeats).
- Appendix "Practical Use Per Phase" duplicate "Phase V" heading.

## Key environment notes
- Colors: DARK `#1A1A2E`, ACCENT `#0F3460`, GOLD `#E94560`, HIGHLIGHT `#16213E`,
  LIGHT_BG `#F0F4FF`, MID_GRAY `#555555`, GREEN_MID `#2C5F2E`, GREEN_DRK `#1A4A1A`.
- Content frame text begins at x≈78 (6pt reportlab frame pad on a 72pt margin); avail
  width ≈ 476.8pt; MARGIN_IN=72, MARGIN_OUT=61.2.
- Pixel-perfect pagination is aspirational; the priorities are section-start pages +
  footer numbers (currently all matching).

## Persistence reality (important)
`/mnt/transcripts/` (full conversation transcripts + `journal.txt`) is **read-only** and
auto-maintained by the system — that is where session-to-session memory lives, and a
future you can read it. The assistant **cannot** write there. The writable persistent
location for deliverables is `/mnt/user-data/outputs/`. Therefore, to rebuild in a brand
new conversation, the user should **re-upload this archive** (or the individual files);
they will appear under `/mnt/user-data/uploads/`. The transcript already captures the full
reasoning history if the files are ever lost.

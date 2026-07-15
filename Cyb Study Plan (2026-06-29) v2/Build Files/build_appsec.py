"""
BUILD SCRIPT — Application Security Engineering Study Plan
Run: python build_appsec.py
"""
import sys, os, json
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from appsec_infrastructure import (
    Cover, make_header_footer, S, banner, grid_table, nb, bi, rule,
    avail, ACCENT, HIGHLIGHT, LIGHT_BG, WHITE, MID_GRAY, DARK, GOLD,
    GREEN_MID, GREEN_DRK, colors, PAGE_W, PAGE_H,
    MARGIN_IN, MARGIN_OUT, MARGIN_TOP, MARGIN_BOT,
    SimpleDocTemplate, letter, inch, KeepTogether, Paragraph, ParagraphStyle,
    Table, TableStyle, Spacer, PageBreak, HRFlowable,
    TA_JUSTIFY, TA_CENTER, TA_RIGHT, OUTPUT
)
from appsec_content import build_content
import timeline_check
import phase_content_check   # integrated content-vs-description verifier (PHASE CONTENT CHECK)
import step_dedup_check      # cross-phase duplicate-step detector (runs on every GENERATE PDF)

STATE_FILE   = os.path.join(_HERE, 'appsec_toc_state.json')
CONTENT_PATH = os.path.join(_HERE, 'appsec_content.py')

# ── Section registry — display name + a snippet that appears on the section's page
# ── Section registry: EXACT TOC title  +  a snippet that appears on the section's page.
#    Keyed by TOC title so scanned page numbers map directly onto the TOC entries.
SECTIONS = [
    ("What Is Application Security?",                "What Is Application Security?"),
    ("Why AppSec Engineering",                       "Why AppSec Engineering"),
    ("Why This Moment",                              "Why This Moment"),
    ("Target Role: Application Security Engineer",    "Target Role: Application Security Engineer"),
    ("Plan Schedule Overview",                       "Plan Schedule Overview"),
    ("Study Methodology",                            "Study Methodology"),
    ("AppSec: Potential Pitfalls & Risk Assessment", "Potential Pitfalls & Risk Assessment"),
    ("Study Plan Phase Summary",                     "Study Plan Phase Summary"),
    ("0 \u2014 Pre-Study: Foundations",              "Pre-Study: Foundations"),
    ("I \u2014 AppSec Intro: A Dip into Offense",     "AppSec Intro: A Dip into Offense"),
    ("II \u2014 Web & Network Foundations",           "Web & Network Foundations"),
    ("III \u2014 Core Vulnerability Classes",         "Core Vulnerability Classes"),
    ("IV \u2014 Security Testing & Tooling",          "Security Testing & Tooling"),
    ("V \u2014 Cloud Security Fundamentals",          "Cloud Security Fundamentals"),
    ("VI \u2014 Secure Code Review & Threat Modeling","Secure Code Review & Threat Modeling"),
    ("VII \u2014 CompTIA Security+ Certification",    "CompTIA Security+ Certification"),
    ("VIII \u2014 Interview Preparation & Interviewing", "Interview Preparation & Interviewing"),
    ("IX \u2014 Expected First Days on the Job",      "Expected First Days on the Job"),
    ("Appendix",                                     "Appendix"),
]

def SP(n=6): return Spacer(1, n)

def scan_pages(pdf_path):
    import pdfplumber, re
    page_texts = {}
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            page_texts[i] = page.extract_text() or ''
    # skip cover (index 0) and TOC pages (detected by long dotted leaders)
    toc_pages = [i for i, t in page_texts.items() if re.search(r'\.{6,}', t)]
    content_start = (max(toc_pages) + 1) if toc_pages else 2
    result = {}
    prev = content_start - 1
    for display, snippet in SECTIONS:            # SECTIONS in document order
        for i in range(max(content_start, prev + 1), total):
            if snippet in page_texts[i]:
                result[display] = i              # printed page number == PDF index
                prev = i
                break
    return result, total

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f: return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f: json.dump(state, f, indent=2)

def _build_pdf(page_overrides):
    """Build the PDF once, with the given {toc_title: page} overrides applied to the TOC."""
    cover = Cover()
    def first_page(c, d): cover.draw(c, d)
    def later_pages(c, d): make_header_footer(c, d)

    story = []
    build_content(
        story=story, S=S, banner=banner, bi=bi, nb=nb,
        rule=rule, grid_table=grid_table, avail=avail,
        ACCENT=ACCENT, HIGHLIGHT=HIGHLIGHT, LIGHT_BG=LIGHT_BG,
        WHITE=WHITE, MID_GRAY=MID_GRAY, DARK=DARK, GOLD=GOLD,
        GREEN_MID=GREEN_MID, GREEN_DRK=GREEN_DRK, colors=colors,
        SP=SP, KeepTogether=KeepTogether, Paragraph=Paragraph,
        ParagraphStyle=ParagraphStyle, Table=Table, TableStyle=TableStyle,
        Spacer=Spacer, PageBreak=PageBreak, HRFlowable=HRFlowable,
        TA_JUSTIFY=TA_JUSTIFY, TA_CENTER=TA_CENTER, TA_RIGHT=TA_RIGHT,
        inch=inch, page_overrides=page_overrides,
    )
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=MARGIN_IN, rightMargin=MARGIN_OUT,
        topMargin=MARGIN_TOP + 0.25*inch,
        bottomMargin=MARGIN_BOT + 0.1*inch,
        title="Application Security Engineering \u2014 Study Plan",
        author="Kyle Miskell", subject="Independent Self-Study Plan",
    )
    doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
    return scan_pages(OUTPUT)   # ({toc_title: actual_page_index}, total_pages)

def main():
    # ── Cross-phase DUPLICATE-STEP guard (runs on every GENERATE PDF) ────────
    # Detection is automated; resolution needs judgment (which phase keeps the
    # full path), so this WARNS rather than silently editing prose during a build.
    print("Checking for duplicate steps across phases...")
    if step_dedup_check.check(CONTENT_PATH):
        print("** WARNING: duplicate step(s) detected above — resolve before relying on this build.\n")
    else:
        print("No duplicate steps. \u2713\n")

    # ── Self-correcting TIMELINE pass (runs BEFORE layout) ───────────────────
    # Mirrors the TOC loop: check -> fix -> check -> ... until the source's
    # timeline data (step numbering, phase-duration end-coverage, and the
    # banner/chart/schedule three-way agreement) is internally consistent across
    # the whole document. Judgment-class issues (a step tagged with a week outside
    # its phase, prose application-month drift) are surfaced, never guessed.
    print("Reconciling timeline consistency...")
    changed, _fixes, _issues = timeline_check.reconcile(CONTENT_PATH)
    if changed:
        import importlib, appsec_content as _ac
        importlib.reload(_ac)
        global build_content
        build_content = _ac.build_content
        print("  (timeline source updated \u2014 reloaded content module for the build)")
    print()

    # ── Self-correcting TOC ──────────────────────────────────────────────────
    # Build, scan the ACTUAL page each section lands on, and if the TOC does not
    # already display that page, fix the TOC (override the page numbers) and
    # rebuild. Repeat until the printed TOC matches the actual pages, since
    # changing a page number's digit count can itself shift later pages.
    MAX_PASSES = 8
    overrides = load_state()          # {toc_title: page} persisted from a prior run, or {}
    actual, total, converged = {}, 0, False
    for p in range(1, MAX_PASSES + 1):
        actual, total = _build_pdf(overrides)
        # mismatch = any section whose TOC-displayed page != the page it actually lands on
        mismatches = {t: a for t, a in actual.items() if overrides.get(t) != a}
        if not mismatches:
            converged = True
            print(f"Pass {p}: TOC matches actual pages \u2014 {total}pp.")
            break
        shown = ", ".join(f"{t.split(chr(0x2014))[0].strip() or t[:16]}:"
                          f"{overrides.get(t, '-')}\u2192{a}" for t, a in mismatches.items())
        print(f"Pass {p}: fixing {len(mismatches)} TOC page number(s) -> {shown}")
        overrides = dict(actual)      # adopt actual pages, then rebuild to confirm stability

    save_state(overrides)

    # ── Final independent verification (printed TOC page == actual page) ──────
    final, total = scan_pages(OUTPUT)
    bad = {t: (overrides.get(t), a) for t, a in final.items() if overrides.get(t) != a}
    print(f"\nPDF \u2192 {OUTPUT}  ({total}pp, "
          f"{os.path.getsize(OUTPUT) / 1024 / 1024:.2f}MB)")
    print("Final TOC verification (TOC page vs actual page):")
    for title, _ in SECTIONS:
        a = final.get(title, "?")
        toc_p = overrides.get(title, "?")
        flag = "" if toc_p == a else "   <-- MISMATCH"
        print(f"  {title:46s} TOC p{toc_p}   actual p{a}{flag}")
    if not converged:
        print(f"\n** WARNING: TOC did not converge after {MAX_PASSES} passes.")
    if bad:
        print(f"** {len(bad)} TOC entry/entries still mismatched \u2014 review needed: {bad}")
    else:
        print("\nAll TOC page numbers match actual pages. \u2713")

if __name__ == "__main__":
    # `PHASE CONTENT CHECK <ROMAN>`  ->  python build_appsec.py CONTENT-CHECK <ROMAN>
    # (offline content-vs-description verification; does NOT build the PDF)
    if len(sys.argv) >= 2 and sys.argv[1].upper() in ("CONTENT-CHECK", "PHASE-CONTENT-CHECK"):
        rom = sys.argv[2].upper() if len(sys.argv) >= 3 else "II"
        sys.exit(phase_content_check.check(rom, CONTENT_PATH))
    if len(sys.argv) >= 2 and sys.argv[1].upper() in ("STEP-DEDUP-CHECK", "DEDUP-CHECK"):
        sys.exit(step_dedup_check.check(CONTENT_PATH))
    if len(sys.argv) >= 2 and sys.argv[1].upper() in ("PRESENT-ZIP", "PRESENT-BUILD-ZIP"):
        import present_build_zip
        present_build_zip.build_zip()
        sys.exit(0)
    main()

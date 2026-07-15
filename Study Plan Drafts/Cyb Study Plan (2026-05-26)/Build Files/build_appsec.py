"""
BUILD SCRIPT — Application Security Engineering Study Plan
Run: python build_appsec.py
"""
import sys, os, json
sys.path.insert(0, '/home/claude')

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

STATE_FILE = '/home/claude/appsec_toc_state.json'

# ── Section registry — display name + a snippet that appears on the section's page
SECTIONS = [
    ("What Is Application Security?",                "What Is Application Security?"),
    ("Why This Moment",                             "Why This Moment"),
    ("Why AppSec Engineering",                      "Why AppSec Engineering"),
    ("Target Role",                                 "Target Role: Application Security Engineer"),
    ("Plan Schedule Overview",                      "Plan Schedule Overview"),
    ("Study Methodology",                           "Study Methodology"),
    ("Philadelphia AppSec Community",               "Philadelphia AppSec Community"),
    ("Pitfalls & Risk Assessment",                  "Potential Pitfalls & Risk Assessment"),
    ("0 \u2014 Pre-Study",                          "Pre-Study: Foundations"),
    ("I \u2014 AppSec Intro",                       "AppSec Intro: A Dip into Offense"),
    ("II \u2014 Web & Network Foundations",         "Web & Network Foundations"),
    ("III \u2014 Core Vulnerability Classes",       "Core Vulnerability Classes"),
    ("IV \u2014 Security Testing & Tooling",        "Security Testing & Tooling"),
    ("V \u2014 Cloud Security Fundamentals",        "Cloud Security Fundamentals"),
    ("VI \u2014 Secure Code Review",                "Secure Code Review & Threat Modeling"),
    ("VII \u2014 CompTIA Security+",                "CompTIA Security+ Certification"),
    ("VIII \u2014 Technical Interview Prep",        "Technical Interview Preparation"),
    ("IX \u2014 Expected First Days",               "Expected First Days on the Job"),
    ("Appendix",                                    "Books & Learning Resources"),
]

def SP(n=6): return Spacer(1, n)

def scan_pages(pdf_path):
    import pdfplumber
    page_texts = {}
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            page_texts[i] = page.extract_text() or ''
    result = {}
    for display, snippet in SECTIONS:
        for i in range(2, len(page_texts)):
            if snippet in page_texts[i]:
                result[display] = i          # printed page number == PDF index
                break
    return result, total

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f: return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f: json.dump(state, f, indent=2)

def main():
    old_state = load_state()
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
        inch=inch
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

    new_state, total_pages = scan_pages(OUTPUT)
    print(f"PDF \u2192 {OUTPUT}  ({total_pages}pp, "
          f"{os.path.getsize(OUTPUT)/1024/1024:.2f}MB)")
    print("Section -> printed page (vs source TOC):")
    src = {
        "What Is Application Security?": 3, "Why This Moment": 4, "Why AppSec Engineering": 6,
        "Target Role": 8, "Plan Schedule Overview": 10, "Study Methodology": 11,
        "Philadelphia AppSec Community": 13, "Pitfalls & Risk Assessment": 15,
        "0 \u2014 Pre-Study": 16, "I \u2014 AppSec Intro": 19,
        "II \u2014 Web & Network Foundations": 22, "III \u2014 Core Vulnerability Classes": 27,
        "IV \u2014 Security Testing & Tooling": 30, "V \u2014 Cloud Security Fundamentals": 34,
        "VI \u2014 Secure Code Review": 37, "VII \u2014 CompTIA Security+": 40,
        "VIII \u2014 Technical Interview Prep": 42, "IX \u2014 Expected First Days": 45,
        "Appendix": 47,
    }
    for display, _ in SECTIONS:
        got = new_state.get(display, "?")
        want = src.get(display, "?")
        flag = "" if got == want else "  <-- differs"
        print(f"  {display:42s} got p{got}   src p{want}{flag}")

    save_state(new_state)

if __name__ == "__main__":
    main()

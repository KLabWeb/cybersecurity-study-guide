"""
CYBERSECURITY STUDY PLAN — SHARED INFRASTRUCTURE
=================================================
Copy of the formatting/style infrastructure from the AI/LLM plan.
To build the cybersec PDF:

1. Edit the OUTPUT path, cover text, pill labels, and header text below
2. Create cybersec_content.py with a build_content(story, S, banner, ...) function
3. Create build_cybersec.py modelled on build_pdf.py

THINGS TO CUSTOMISE (marked with # <<< CUSTOMISE):
- OUTPUT path
- Cover title lines
- Cover subtitle / arrow text
- Cover pill labels
- Header bar text (make_header_footer)
- Color scheme (optional — current scheme is dark navy/blue)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import datetime

_HERE = os.path.dirname(os.path.abspath(__file__))

def _register_font(name, fname):
    """Use the system DejaVu font if present, else a copy bundled in ./fonts/."""
    for path in (os.path.join("/usr/share/fonts/truetype/dejavu", fname),
                 os.path.join(_HERE, "fonts", fname)):
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path)); return
    raise FileNotFoundError(f"DejaVu font '{fname}' not found (system path or ./fonts/)")

_register_font('DejaVu', 'DejaVuSans.ttf')
_register_font('DejaVu-Bold', 'DejaVuSans-Bold.ttf')

# Output path: the shared outputs dir in this environment if present, else next to this script.
_OUTDIR = "/mnt/user-data/outputs" if os.path.isdir("/mnt/user-data/outputs") else _HERE
OUTPUT = os.path.join(_OUTDIR, f"Study_Plan_-_{datetime.date.today().isoformat()}.pdf")

# ── Colours ───────────────────────────────────────────────────────────────────
# Current: dark navy / steel blue. Swap ACCENT/GOLD for a different feel.
DARK      = colors.HexColor("#1A1A2E")      # page background (dark)
ACCENT    = colors.HexColor("#0F3460")      # header bar, table headers, banners
HIGHLIGHT = colors.HexColor("#16213E")      # pill bar background
GOLD      = colors.HexColor("#E94560")      # accent line, pill roman numerals
LIGHT_BG  = colors.HexColor("#F0F4FF")      # note box background
MID_GRAY  = colors.HexColor("#555555")      # secondary text
WHITE     = colors.white
GREEN_MID = colors.HexColor("#2C5F2E")
GREEN_DRK = colors.HexColor("#1A4A1A")

# ── Page geometry ─────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = letter
MARGIN_IN  = 1.0 * inch
MARGIN_OUT = 0.85 * inch
MARGIN_TOP = 0.85 * inch
MARGIN_BOT = 0.85 * inch
avail = PAGE_W - MARGIN_IN - MARGIN_OUT - 2

# ── Header / footer ───────────────────────────────────────────────────────────
def make_header_footer(canvas, doc):
    canvas.saveState()
    p = doc.page - 1          # cover is unnumbered; Contents == printed page 1
    canvas.setStrokeColor(ACCENT); canvas.setLineWidth(1.5)
    canvas.line(MARGIN_IN, PAGE_H-MARGIN_TOP+6, PAGE_W-MARGIN_OUT, PAGE_H-MARGIN_TOP+6)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(MID_GRAY)
    if p >= 1:
        # <<< CUSTOMISE: header bar text
        canvas.drawString(MARGIN_IN, PAGE_H-MARGIN_TOP+10,
                          "Application Security Engineering — Study Plan")
    canvas.drawRightString(PAGE_W-MARGIN_OUT, PAGE_H-MARGIN_TOP+10, "May 2026")
    canvas.setStrokeColor(ACCENT)
    canvas.line(MARGIN_IN, MARGIN_BOT-6, PAGE_W-MARGIN_OUT, MARGIN_BOT-6)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(MID_GRAY)
    if p % 2 == 1: canvas.drawString(MARGIN_IN, MARGIN_BOT-14, str(p))
    else: canvas.drawRightString(PAGE_W-MARGIN_OUT, MARGIN_BOT-14, str(p))
    canvas.restoreState()

# ── Paragraph styles ──────────────────────────────────────────────────────────
base = getSampleStyleSheet()
def sty(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

S = {
    "toc_entry": sty("te", fontSize=9, leading=12, textColor=DARK, leftIndent=0, spaceAfter=1),
    "toc_sub":   sty("ts", fontSize=8, leading=11, textColor=MID_GRAY, leftIndent=16, spaceAfter=0),
    "phase_lbl": sty("pl", fontSize=9, leading=11, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER),
    "sec_title": sty("st", fontSize=18, leading=22, textColor=WHITE, fontName="Helvetica-Bold"),
    "sec_roman": sty("sr", fontSize=11, leading=14, textColor=colors.HexColor("#AABBDD"), fontName="Helvetica-Bold", alignment=TA_CENTER),
    "sub_head":  sty("sh", fontSize=12, leading=15, textColor=ACCENT, fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=2),
    "sshead":    sty("ss", fontSize=10, leading=13, textColor=DARK,  fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=3),
    "body":      sty("b",  fontSize=9.5, leading=14, textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=4),
    "bsm":       sty("bs", fontSize=9,   leading=13, textColor=MID_GRAY, alignment=TA_JUSTIFY),
    "bul":       sty("bu", fontSize=9.5, leading=14, textColor=DARK, leftIndent=14, firstLineIndent=0, spaceAfter=3),
    "bulsm":     sty("bv", fontSize=9,   leading=13, textColor=MID_GRAY, leftIndent=24, firstLineIndent=0, spaceAfter=4),
    "nb":        sty("nb", fontSize=9,   leading=13, textColor=colors.HexColor("#1A2A5E"), alignment=TA_JUSTIFY),
    "th":        sty("th", fontSize=9,   leading=11, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER),
    "tc":        sty("tc", fontSize=9,   leading=12, textColor=DARK, alignment=TA_LEFT),
    "tcc":       sty("tv", fontSize=9,   leading=12, textColor=DARK, alignment=TA_CENTER),
    "lnk":       sty("lk", fontSize=8,   leading=11, textColor=colors.HexColor("#0055AA")),
    "pcc":       sty("pc", fontSize=8,   leading=11, textColor=colors.HexColor("#666666"), alignment=TA_CENTER),
    "cm":        sty("cm", fontSize=10,  leading=14, textColor=colors.HexColor("#AABBDD"), fontName="Helvetica"),
}

# ── Helper flowables ──────────────────────────────────────────────────────────
def rule(color=ACCENT, w=1, sb=4, sa=8):
    return [Spacer(1, sb), HRFlowable(width="100%", thickness=w, color=color, spaceAfter=sa)]

def bi(text, sub=False):
    return Paragraph(f'<font name="DejaVu">\u2022</font> {text}', S["bulsm" if sub else "bul"])

def nb(text):
    avail_w = PAGE_W - MARGIN_IN - MARGIN_OUT - 2
    t = Table([[Paragraph(text, S["nb"])]], colWidths=[avail_w])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT_BG),
        ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#AABBDD")),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),   ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def banner(roman, title, dur, color=ACCENT):
    avail_w = PAGE_W - MARGIN_IN - MARGIN_OUT - 2
    lc, rc = 0.9*inch, avail_w - 0.9*inch
    data = [[Paragraph(roman, S["sec_roman"]),
             [Paragraph(title, S["sec_title"]), Paragraph(dur, S["cm"])]]]
    t = Table(data, colWidths=[lc, rc])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (0,-1), 12), ("RIGHTPADDING", (0,0), (0,-1), 6),
        ("LEFTPADDING", (1,0), (1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
        ("LINEAFTER", (0,0), (0,-1), 1, colors.HexColor("#FFFFFF44")),
    ]))
    return t

def grid_table(data, colwidths):
    t = Table(data, colWidths=colwidths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ACCENT),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_BG]),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    return t

# ── Cover page ─────────────────────────────────────────────────────────────────
class Cover:
    def draw(self, canvas, doc):
        w, h = PAGE_W, PAGE_H
        canvas.setFillColor(DARK); canvas.rect(0, 0, w, h, fill=1, stroke=0)
        canvas.setFillColor(ACCENT); canvas.rect(0, h*0.38, w, h*0.62, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.rect(MARGIN_IN, h*0.38-4, w-MARGIN_IN-MARGIN_OUT, 4, fill=1, stroke=0)
        canvas.setStrokeColor(colors.HexColor("#FFFFFF11")); canvas.setLineWidth(0.5)
        canvas.line(MARGIN_IN*0.55, 0, MARGIN_IN*0.55, h)

        tx = MARGIN_IN

        # title lines (Helvetica-Bold 36, white)
        canvas.setFont("Helvetica-Bold", 36); canvas.setFillColor(WHITE)
        canvas.drawString(tx, 433.5, "Application Security")
        canvas.drawString(tx, 388.5, "Engineering \u2014 Study Plan")

        # subtitle (Helvetica 13)
        canvas.setFont("Helvetica", 13); canvas.setFillColor(colors.HexColor("#AABBDD"))
        canvas.drawString(tx, 364.3, "Independent Self-Study \u2014 Kyle Miskell  \u2014  kmiskell@protonmail.com")

        # arrow progression text removed per changelist item 2
        canvas.setStrokeColor(GOLD); canvas.setLineWidth(1.5)
        canvas.line(tx, 329.0, tx+3.5*inch, 329.0)

        # pill row (10 pills, two-line labels)
        pills = [
            ("0",    ["Pre-",      "Study"]),
            ("I",    ["AppSec",    "Intro"]),
            ("II",   ["Web &",     "Network"]),
            ("III",  ["Core",      "Vulns"]),
            ("IV",   ["Testing &", "Tooling"]),
            ("V",    ["Cloud",     "Security"]),
            ("VI",   ["Code",      "Review"]),
            ("VII",  ["Sec+",      "Cert"]),
            ("VIII", ["Interview", "Prep"]),
            ("IX",   ["First",     "Days"]),
        ]
        pg = 0.1*inch
        pw = (avail - pg*(len(pills)-1)) / len(pills)
        ph = 30.2; py = 13.0; px = MARGIN_IN
        for roman, label in pills:
            canvas.setFillColor(HIGHLIGHT)
            canvas.roundRect(px, py, pw, ph, 3, fill=1, stroke=0)
            canvas.setFillColor(GOLD); canvas.setFont("Helvetica-Bold", 8)
            canvas.drawCentredString(px+pw/2, 33.3, roman)
            canvas.setFillColor(colors.HexColor("#C0CCE8")); canvas.setFont("Helvetica", 6.5)
            l1, l2 = label
            if l1: canvas.drawCentredString(px+pw/2, 21.9, l1)
            if l2: canvas.drawCentredString(px+pw/2, 15.6, l2)
            px += pw + pg

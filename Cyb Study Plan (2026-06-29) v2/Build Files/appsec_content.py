# -*- coding: utf-8 -*-
"""
APPLICATION SECURITY ENGINEERING — STUDY PLAN — CONTENT
Faithful reconstruction of Study_Plan_-_2026-05-26.pdf
"""

from reportlab.platypus import Spacer, PageBreak, Paragraph, KeepTogether, CondPageBreak
from reportlab.lib.units import inch
import re

DJ = '<font name="DejaVu">\u2192</font>'   # arrow that renders
LINK = "#3A7AB8"                            # URL hyperlink colour (matches source)
_URL_RE = re.compile(
    r'(?<![\w@])((?:[A-Za-z0-9-]+\.)+(?:com|org|net|io|dev|cloud|gov|edu)(?:/[^\s,;)\]<]*)?)')

_ANCHOR_RE = re.compile(r'<a\b[^>]*>.*?</a>', re.S)


def linkify(text):
    """Wrap bare web URLs in clickable links coloured like the source (no underline).
    Skips any span already inside an <a>...</a> tag so manually-authored links (and the
    URLs inside their href attributes) are never re-wrapped."""
    def repl(m):
        url = m.group(1); tail = ""
        while url and url[-1] in ".,;:":
            tail = url[-1] + tail; url = url[:-1]
        href = url if url.startswith(("http://", "https://")) else "https://" + url
        return f'<a href="{href}" color="{LINK}">{url}</a>{tail}'
    out, last = [], 0
    for am in _ANCHOR_RE.finditer(text):
        out.append(_URL_RE.sub(repl, text[last:am.start()]))  # linkify outside the anchor
        out.append(am.group(0))                                # keep the anchor verbatim
        last = am.end()
    out.append(_URL_RE.sub(repl, text[last:]))
    return "".join(out)


def build_content(story, S, banner, bi, nb, rule, grid_table,
                  avail, ACCENT, HIGHLIGHT, LIGHT_BG, WHITE,
                  MID_GRAY, DARK, GOLD, GREEN_MID, GREEN_DRK,
                  colors, SP, KeepTogether, Paragraph, ParagraphStyle,
                  Table, TableStyle, Spacer, PageBreak, HRFlowable,
                  TA_JUSTIFY, TA_CENTER, TA_RIGHT, inch, page_overrides=None):

    add  = story.append
    adds = story.extend

    def P(text, style):
        return Paragraph(linkify(text).replace("\u2192", DJ), style)

    def B(text, sub=False):
        return bi(linkify(text).replace("\u2192", DJ), sub)

    def H(title):                       # top-level section heading + rule
        add(P(title, S["sub_head"])); adds(rule())

    def SS(title):                      # sub-sub heading + rule
        add(P(title, S["sshead"])); adds(rule())

    def step(num, label, rest, items):
        add(P(f"<b>{num}. {label}:</b> {rest}", S["body"]))
        for it in items:
            add(B(it))
        add(SP(4))

    def concept(name, text):
        add(KeepTogether([P(f"<b>{name}</b>", S["bul"]), P(text, S["bulsm"])]))

    def res(title, details):
        add(B(f"<b>{title}</b> \u2014 {details}"))

    # ════════════════════════════════════════════════════════════════════════
    #  TABLE OF CONTENTS
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(P("Contents", S["sub_head"])); adds(rule())

    toc = [
        ("What Is Application Security?", "3", []),
        ("Why AppSec Engineering", "4",
            ["The Case for This Path", "Your Structural Advantage", "No LeetCode"]),
        ("Why This Moment", "6", []),
        ("Target Role: Application Security Engineer", "8",
            ["What It Is \u2014 Conceptually", "Day-to-Day Responsibilities",
             "Compensation \u2014 Summer 2026", "Philadelphia & Remote Market"]),
        ("Plan Schedule Overview", "10", ["Phase Timeline"]),
        ("Study Methodology", "11",
            ["MentorCruise", "Note-Taking", "Portfolio: Writeups & Project Site",
             "Local & Regional Events"]),
        ("AppSec: Potential Pitfalls & Risk Assessment", "15", []),
        ("Study Plan Phase Summary", "16", []),
        ("0 \u2014 Pre-Study: Foundations", "16",
            ["Learning Resources", "Schedule", "Projects & Writings", "Concepts Broached"]),
        ("I \u2014 AppSec Intro: A Dip into Offense", "19",
            ["Learning Resources", "Schedule", "Projects & Writings", "Concepts Broached"]),
        ("II \u2014 Web & Network Foundations", "22",
            ["Learning Resources", "Schedule", "Concepts Mastered"]),
        ("III \u2014 Core Vulnerability Classes", "27",
            ["Learning Resources", "Schedule", "Concepts Mastered"]),
        ("IV \u2014 Security Testing & Tooling", "30",
            ["Learning Resources", "Schedule", "Concepts Mastered"]),
        ("V \u2014 Cloud Security Fundamentals", "34",
            ["Learning Resources", "Schedule", "Concepts Mastered"]),
        ("VI \u2014 Secure Code Review & Threat Modeling", "37",
            ["Learning Resources", "Schedule", "Concepts Mastered"]),
        ("VII \u2014 CompTIA Security+ Certification", "40",
            ["Schedule", "Learning Resources", "Concepts Mastered"]),
        ("VIII \u2014 Interview Preparation & Interviewing", "42",
            ["Interview Preparation", "Framing Your Background", "Application Strategy"]),
        ("IX \u2014 Expected First Days on the Job", "44",
            ["Your Immediate Differentiators"]),
        ("Appendix", "46",
            ["Books & Learning Resources", "Certifications", "Practical Use Per Phase",
             "Philadelphia AppSec Community"]),
    ]
    _ov = page_overrides or {}
    for title, page, subs in toc:
        page = _ov.get(title, page)          # build may override with the actual scanned page
        add(P(f'<b>{title}</b><font color="#AAAAAA">{"."*max(2, 62-len(title))}</font>{page}',
              S["toc_entry"]))
        for sub in subs:
            add(P(f"\u2013 {sub}", S["toc_sub"]))
        add(SP(2))

    # ════════════════════════════════════════════════════════════════════════
    #  WHAT IS APPLICATION SECURITY?
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("What Is Application Security?")
    for para in [
        "Application security \u2014 AppSec \u2014 is the discipline of finding, fixing, and "
        "preventing security vulnerabilities in software. Where most of software engineering "
        "asks <i>does this work?</i>, application security asks <i>can this be broken?</i> The "
        "question sounds simple. The implications are not.",
        "Software has an attack surface: every input field, every API endpoint, every "
        "authentication flow, every dependency in your requirements.txt is a potential entry "
        "point for an adversary. AppSec engineers systematically map that surface, probe it for "
        "weaknesses, and work with development teams to close them \u2014 before attackers find "
        "them first.",
        "The discipline spans the entire software development lifecycle. In the design phase, it "
        "means threat modeling \u2014 drawing data flows and asking what happens when an attacker "
        "controls each input. During development, it means secure code review \u2014 reading code "
        "the way an attacker reads it, looking for injection points, broken authentication, "
        "insecure data handling. In testing, it means static analysis (SAST) that reads source "
        "code for vulnerability patterns, dynamic analysis (DAST) that probes a running "
        "application, and manual penetration testing that combines both with adversarial "
        "creativity.",
        "The OWASP Top 10 is the field\u2019s shared vocabulary for the most critical web "
        "application security risks. SQL injection, broken access control, cross-site scripting, "
        "security misconfigurations, insecure deserialization, and other key risks. These are not abstract "
        "academic concerns \u2014 they are the specific vulnerability classes that appear in real "
        "breaches against real companies, year after year. AppSec engineers know them the way a "
        "surgeon knows anatomy: not as a list to memorize, but as a framework for understanding "
        "how systems fail.",
        "This plan targets web application security specifically \u2014 the attack surface that "
        "lives at the HTTP layer, in APIs, in authentication flows, in the browser.",
    ]:
        add(P(para, S["body"])); add(SP(2))

    # ════════════════════════════════════════════════════════════════════════
    #  WHY APPSEC ENGINEERING
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Why AppSec Engineering")
    SS("The Case for This Path")
    add(P("This plan is a deliberate pivot, not a hedge. You spent five years building the attack "
          "surface that AppSec engineers protect. You know FastAPI microservices, React "
          "frontends, AWS infrastructure, Docker containers, poorly written legacy PHP codebases "
          "\u2014 the exact technology stack that "
          "AppSec interviews test your ability to reason about adversarially. No other security "
          "specialization maps as directly to a full-stack development background.", S["body"]))
    SS("Your Structural Advantage")
    add(P("Most AppSec engineers come from one of two directions: former developers who learned "
          "security, or security professionals who learned development. You are in the first "
          "category \u2014 and the first category produces better AppSec engineers, because you "
          "understand not just what the vulnerability is but why developers write it. The code "
          "patterns that lead to SQL injection, authentication bypasses, and CORS "
          "misconfigurations are patterns that developers encounter every day. Recognizing them "
          "as vulnerabilities \u2014 rather than just implementation choices \u2014 is the shift "
          "this plan builds. That background is not a liability to overcome. It is the primary "
          "qualification.", S["body"]))
    add(SP(2))
    add(P("Specific transferable skills from your resume:", S["body"]))
    add(B("<b>FastAPI microservices</b> \u2014 REST API security is the dominant AppSec domain in "
          "2026. Hands-on API security knowledge built throughout this plan means arriving on day "
          "one prepared for the work."))
    add(B("<b>Python</b> \u2014 The primary scripting language for AppSec tooling. Custom Semgrep "
          "rules, vulnerability scanning automation, security utilities."))
    add(B("<b>React frontends</b> \u2014 Client-side vulnerabilities (XSS, CSRF, insecure "
          "storage) require understanding how the browser executes JavaScript. React experience "
          "provides a strong foundation for understanding client-side vulnerability patterns."))
    add(B("<b>AWS, Docker, Kubernetes</b> \u2014 Cloud and container security are AppSec-adjacent "
          "and increasingly part of the role. Your infrastructure knowledge is a differentiator."))
    add(B("<b>Legacy PHP, raw SQL, and NoSQL</b> \u2014 You have worked in poorly written legacy "
          "PHP, hand-rolled MySQL, and DynamoDB \u2014 exactly where SQL injection, IDOR, and "
          "NoSQL injection live. You recognize the vulnerable pattern and know how to fix it."))
    add(B("<b>Architecture &amp; domain modeling</b> \u2014 You designed microservices and "
          "domain-driven services with deliberate separation of concerns and trust boundaries. "
          "Threat modeling is that same structural thinking turned toward attack: mapping data "
          "flows and asking where trust is assumed."))
    add(B("<b>Testing discipline</b> \u2014 You wrote unit, integration, and regression tests. "
          "AppSec testing follows the same deterministic logic: inputs, expected behavior, failure modes."))
    add(SP(2))
    SS("No LeetCode")
    add(P("AppSec interviews test security knowledge \u2014 OWASP concepts, secure code review, "
          "threat modeling, vulnerability identification. Not dynamic programming. Not graph "
          "traversal. The technical interview involves reading vulnerable code and explaining "
          "what is wrong with it \u2014 something five years of full-stack experience of building "
          "code makes you structurally prepared for. The relief this should produce as part of a "
          "break from never-ending leetcode grinding, contrived software engineering interviews, "
          "and poor communication during the full software eng interview lifecycle is real and "
          "substantial.", S["body"]))
    add(SP(2))

    # ════════════════════════════════════════════════════════════════════════
    #  WHY THIS MOMENT
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Why This Moment")
    add(P("The case for entering application security in 2026 rests on concrete numbers, not "
          "hype. Here is what the data actually shows.", S["body"]))
    SS("The breach problem is not going away.")
    add(P("IBM\u2019s 2025 Cost of a Data Breach Report \u2014 the most cited annual benchmark in "
          "the industry, now in its 20th year \u2014 found that the average U.S. cost of a data "
          "breach reached a record $10.22 million in 2025, even as the global average fell "
          "slightly to $4.44 million driven by faster AI-assisted detection. The U.S. number is "
          "the highest ever recorded. Nearly two-thirds of the 600 organizations IBM studied said "
          "they were still recovering from their breach at the time of the report. Verizon\u2019s "
          "2025 Data Breach Investigations Report found that exploitation of vulnerabilities "
          "\u2014 the class of attack that AppSec engineers specifically exist to prevent \u2014 "
          "initiated 20% of all breaches studied.", S["body"]))
    add(P("The application layer is where the majority of those vulnerabilities live. More than "
          "45% of data breaches in 2024 involved at least one application-layer vulnerability. "
          "The number of web applications worldwide exceeded 1.8 billion in 2024, increasing the "
          "attack surface faster than the security workforce is growing. Over 60% of Fortune 500 "
          "companies now integrate application security testing into their software development "
          "lifecycle \u2014 which means nearly 40% still do not, and most of those companies are "
          "actively looking for people to fix that.", S["body"]))
    SS("The workforce gap is structural.")
    add(P("ISC2\u2019s 2025 Workforce Study estimated 4.8 million unfilled cybersecurity roles "
          "globally. The U.S. Bureau of Labor Statistics projects 29% job growth in information "
          "security analysis from 2024 to 2034 \u2014 nearly ten times the average growth rate "
          "across all occupations. U.S. employers posted over 514,000 cybersecurity job openings "
          "in the past twelve months, up 12% from the prior year. For application security "
          "specifically, Mordor Intelligence reports a 15% annual shortfall of AppSec engineers "
          "in the United States through 2026 \u2014 demand growing faster than the supply of "
          "qualified people to fill it.", S["body"]))
    add(P("The shortage is not evenly distributed. ISC2 noted in 2025 that skills shortages now "
          "outweigh headcount shortages as the primary constraint \u2014 meaning companies are "
          "not just short on bodies, they are short on people who can actually do the work. AI is "
          "automating the lowest complexity tasks (Tier 1 alert triage, routine vulnerability "
          "scanning), which is compressing demand for those roles. What it is not automating is "
          "the judgment-intensive work: finding business logic flaws that automated scanners "
          "cannot detect, threat modeling a new microservice architecture, explaining a critical "
          "finding to a VP of Engineering in terms that result in a fix. That work requires a "
          "human who can read code, understand systems, and think adversarially. That is the work "
          "this plan prepares you for.", S["body"]))
    SS("The AppSec market is expanding fast.")
    add(P("The global application security market was valued at $13.68 billion in 2024 and is "
          "projected to reach $53.25 billion by 2033, growing at 16.3% annually. The application "
          "security testing market specifically is growing at 26.7% annually \u2014 from $1.83 "
          "billion in 2025 to a projected $7.60 billion by 2031. Salary data from 2026 job "
          "postings shows Application Security Engineers earning $130,000\u2013$180,000 at "
          "mid-level, driven by what one salary analysis describes as \u2018strong demand due to "
          "OWASP Top 10 vulnerabilities and insecure APIs.\u2019 Product Security Engineer "
          "postings grew 12.08% year over year in 2025, outpacing most other security roles in "
          "posting growth.", S["body"]))
    add(SP(4))
    add(nb("<b>The structural argument:</b> IBM\u2019s data shows that organizations with severe "
           "security staffing shortages face $1.76 million higher breach costs than those that "
           "are adequately staffed. Companies are not hiring AppSec engineers because it is a "
           "nice-to-have. They are hiring because the cost of not having them is measurable, "
           "large, and growing."))

    # ════════════════════════════════════════════════════════════════════════
    #  TARGET ROLE
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Target Role: Application Security Engineer")
    SS("What It Is \u2014 Conceptually")
    add(P("Web application development and application security share the same foundation: HTTP, "
          "APIs, authentication flows, browser security models, database queries. Every endpoint "
          "in a web application is an AppSec concern. Every authentication flow is a potential "
          "bypass. Every React component that renders user input is an XSS candidate. Developers "
          "who learn AppSec understand the systems being defended \u2014 they are adding an "
          "adversarial lens to knowledge they already hold.", S["body"]))
    add(P("The shift is perspective. Where a developer asks <i>does this feature work "
          "correctly?</i>, an AppSec engineer asks <i>what happens when an attacker controls this "
          "input?</i> The underlying knowledge of the system is identical. The adversarial lens "
          "is the discipline.", S["body"]))
    SS("What It Is \u2014 In Practice")
    add(B("<b>Secure code review</b> (analogous to: pull request review, but adversarial) \u2014 "
          "Reading code to identify vulnerability patterns: SQL queries built by string "
          "concatenation, tokens stored in localStorage, endpoints missing authorization checks, "
          "user data rendered without sanitization."))
    add(B("<b>Penetration testing / DAST</b> (analogous to: integration testing, but "
          "adversarial) \u2014 Running Burp Suite against a staging environment, intercepting "
          "HTTP requests, modifying parameters, observing whether the application behaves "
          "securely."))
    add(B("<b>SAST tooling</b> (analogous to: adding a linter to CI/CD) \u2014 Integrating "
          "Semgrep into the pipeline. Writing custom rules that catch company-specific "
          "vulnerability patterns. Triaging scan results: true positives from false positives."))
    add(B("<b>Threat modeling</b> (analogous to: architecture review, but adversarial) \u2014 "
          "Given a proposed system design, enumerate the ways it could be attacked. STRIDE: "
          "Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation "
          "of Privilege."))
    add(B("<b>Vulnerability management</b> (analogous to: bug triage) \u2014 Prioritizing "
          "findings by severity and business impact. Writing clear reports developers can act on. "
          "Tracking remediation. Verifying fixes."))
    add(SP(2))
    SS("Day-to-Day Responsibilities")
    for t in [
        "Secure code review on high-risk PRs and new features \u2014 auth, payments, file "
        "upload, API endpoints",
        "Running and maintaining SAST tooling in CI/CD \u2014 Semgrep rules, false positive "
        "triage, new rule development",
        "Manual penetration testing of web applications and APIs \u2014 Burp Suite, "
        "methodology-driven, OWASP-aligned",
        "Threat modeling new system designs \u2014 STRIDE analysis, data flow diagrams, risk "
        "documentation",
        "Vulnerability reporting and remediation tracking \u2014 clear writeups, severity "
        "ratings, developer liaison",
        "Security training and developer education \u2014 lunch-and-learns, secure coding "
        "guidelines, champions programs",
        "Dependency and supply chain security \u2014 SCA scanning, CVE monitoring, patch "
        "prioritization",
    ]:
        add(B(t))
    add(SP(4))
    SS("Compensation \u2014 Summer 2026")
    comp = [
        [P("<b>Level</b>", S["th"]), P("<b>Base Salary</b>", S["th"]), P("<b>Notes</b>", S["th"])],
        [P("Entry / first role", S["tc"]), P("$90K\u2013$130K", S["tcc"]),
         P("Realistic with strong portfolio; varies by company size", S["tc"])],
        [P("Mid-level (2\u20134 yrs)", S["tc"]), P("$130K\u2013$180K", S["tcc"]),
         P("Glassdoor avg $164K; remote-first roles higher", S["tc"])],
        [P("Senior (4+ yrs)", S["tc"]), P("$170K\u2013$240K", S["tcc"]),
         P("Deep domain expertise, mentoring, architecture involvement", S["tc"])],
        [P("Top tech (FAANG+)", S["tc"]), P("$250K\u2013$400K+", S["tcc"]),
         P("Total comp incl. equity; not a realistic first role target", S["tc"])],
    ]
    add(grid_table(comp, [1.5*inch, 1.2*inch, avail-2.7*inch]))
    add(SP(8))
    SS("Philadelphia & Remote Market")
    add(P("AppSec has strong remote availability \u2014 roughly 70\u201375% of postings offer "
          "remote or hybrid flexibility. Philadelphia-based remote work means accessing national "
          "salary bands at Philadelphia cost of living. Local Philly demand is moderate but real, "
          "anchored by healthcare, financial services, and enterprise tech.", S["body"]))
    add(SP(2))
    philly = [
        [P("<b>Company Type</b>", S["th"]), P("<b>Examples</b>", S["th"]), P("<b>Role Fit</b>", S["th"])],
        [P("Healthtech", S["tc"]), P("Penn Medicine, Jefferson Health, Abridge (remote)", S["tc"]),
         P("Strong. PHI/HIPAA requirements drive AppSec demand.", S["tc"])],
        [P("Financial services", S["tc"]), P("Vanguard (Malvern), JPMorgan (Wilmington)", S["tc"]),
         P("Strong. PCI compliance, high-value targets, established AppSec programs.", S["tc"])],
        [P("Fintech / Crypto", S["tc"]), P("Remote-first nationally; Coinbase, Kraken, Block", S["tc"]),
         P("Best fit. Finance/crypto pay premium. Fast hiring on demonstrated skill.", S["tc"])],
        [P("Enterprise (Philly)", S["tc"]), P("Comcast, SAP Concur, Independence Blue Cross", S["tc"]),
         P("Good. Stable. Full-stack background relevant to AppSec integration work.", S["tc"])],
        [P("Legal AI / LegalTech", S["tc"]), P("Thomson Reuters/Casetext, Gap International (Philly)", S["tc"]),
         P("Good. Document handling, PII, sensitive data \u2014 AppSec-heavy by necessity.", S["tc"])],
    ]
    add(grid_table(philly, [1.25*inch, 1.95*inch, avail-3.2*inch]))
    add(SP(6))
    add(nb("Start applying at Month 4 for AI-native startups and security-conscious tech "
           "companies. Target Philadelphia legal AI and healthtech in parallel \u2014 these "
           "companies hire locally, are less saturated with remote applicants, and a full-stack "
           "background is immediately relevant."))

    # ════════════════════════════════════════════════════════════════════════
    #  PLAN SCHEDULE OVERVIEW
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Plan Schedule Overview")
    add(P("This plan is calibrated for 6\u20138 months at 21 study hours per week. 6 "
          "months is the optimistic case; 8 months is the outer bound; 7 months is the realistic "
          "midpoint. The hardest phase is not technical \u2014 it is "
          "mental: shifting from builder to adversarial thinker.", S["body"]))
    add(SP(2))
    sched = [
        [P("<b>Day Type</b>", S["th"]), P("<b>Days/Week</b>", S["th"]),
         P("<b>Hours</b>", S["th"]), P("<b>Notes</b>", S["th"])],
        [P("Long Study", S["tc"]), P("3", S["tcc"]), P("7 hrs", S["tcc"]),
         P("Reading, labs, implementation, tool practice, note-card review, writeups", S["tc"])],
        [P("<b>TOTAL STUDY</b>", S["tc"]), P("<b>3</b>", S["tcc"]), P("<b>21 hrs</b>", S["tcc"]),
         P("", S["tc"])],
        [P("Work (Gigs)", S["tc"]), P("2", S["tcc"]), P("7 hrs", S["tcc"]),
         P("Income \u2014 Two 3\u20134 hour shifts", S["tc"])],
        [P("Day Off", S["tc"]), P("2", S["tcc"]), P("\u2014", S["tcc"]),
         P("No study, no work. Required for retention &amp; sanity.", S["tc"])],
    ]
    add(grid_table(sched, [1.5*inch, 0.85*inch, 0.85*inch, avail-3.2*inch]))
    add(SP(10))
    SS("Phase Timeline")
    cols = ["0","I","II","III","IV","V","VI","VII","VIII","IX"]
    names = ["Pre-\nStudy","AppSec\nIntro","Web &\nNetwork","Core\nVulns","Testing &\nTooling",
             "Cloud\nSecurity","Code\nReview","Sec+\nCert","Interview\nPrep","First\nDays"]
    weeks = ["Wks 1\u20133","Wks 4\u20135","Mo 1.5\u20132.25","Mo 2.5\u20133.5","Mo 3.5\u20135.25",
             "Mo 5.25\u20135.75","Mo 5.75\u20136.5","Mo 6.75\u20137.25","Mo 7.5\u20138","Mo 7.75+"]
    tl_colors = ["#2C3E50","#1B4F72","#1A5276","#154360","#0E6655","#145A32",
                 "#6E2F1A","#6E2F3E","#2E4057","#212F3C"]
    romst = ParagraphStyle("tlrom", parent=S["pcc"], fontSize=10.5, leading=13,
                           fontName="Helvetica-Bold", textColor=WHITE, alignment=TA_CENTER)
    namst = ParagraphStyle("tlnam", parent=S["pcc"], fontSize=7, leading=8.5,
                           alignment=TA_CENTER, textColor=WHITE)
    wkst  = ParagraphStyle("tlwk", parent=S["pcc"], fontSize=7, leading=8.5,
                           alignment=TA_CENTER, textColor=WHITE)
    tdata = [
        [Paragraph(c, romst) for c in cols],
        [Paragraph(n.replace("\n","<br/>"), namst) for n in names],
        [Paragraph(w, wkst) for w in weeks],
    ]
    cw = avail/10.0
    tt = Table(tdata, colWidths=[cw]*10, rowHeights=[24, 38, 24])
    ts = [
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("TOPPADDING", (0,0), (-1,-1), 2), ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING", (0,0), (-1,-1), 1), ("RIGHTPADDING", (0,0), (-1,-1), 1),
    ]
    for ci, hexc in enumerate(tl_colors):
        ts.append(("BACKGROUND", (ci,0), (ci,-1), colors.HexColor(hexc)))
    tt.setStyle(TableStyle(ts))
    add(tt)
    add(SP(8))
    add(nb("<b>Timeline:</b> 6 months is the optimistic case; 8 months is the outer bound; 7 "
           "months is the realistic midpoint. The first 2\u20133 weeks are pre-study before "
           "security content begins. Start applying at Month 4 for startups and AppSec-adjacent "
           "roles. Security+ lands on your resume at Month 7, strengthening the main application "
           "push that follows. On the two-year employment gap: \u2018I have been in a deliberate "
           "full-time transition into application security since June 2026. This plan is the "
           "evidence.\u2019"))

    # ════════════════════════════════════════════════════════════════════════
    #  STUDY METHODOLOGY
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Study Methodology")
    add(P("The methods below apply to every phase. Following them consistently is the difference "
          "between completing labs and actually owning the material.", S["body"]))
    SS("Human Mentorship: MentorCruise (or Koz)")
    add(P("Self-study hits a ceiling when a vulnerability class just will not click, or when you "
          "need someone to tell you whether your code review findings are the right findings. A "
          "mentor who ships AppSec work professionally can review this plan, calibrate your lab "
          "work, and run mock code review sessions. MentorCruise (mentorcruise.com) is the "
          "platform.", S["body"]))
    add(B("<b>What to look for:</b> Production AppSec engineering background. Keywords: "
          "application security, secure code review, penetration testing, OWASP, Burp Suite, "
          "AppSec program building. Avoid pure red-team/CTF backgrounds."))
    add(B("<b>Suggested usage:</b> One session upfront to review this plan. Monthly check-ins at "
          "phase transitions. Async questions for anything that blocks progress."))
    add(B("<b>Cost:</b> $100\u2013$150/month. 7-day trial lets you test fit. Highest-ROI "
          "expenditure in the plan."))
    add(B("<b>When to start:</b> Before Phase I. First session is a plan review."))
    add(SP(2))
    SS("Local &amp; Regional Events")
    add(P("Studying is not only reading and labs \u2014 attending local and regional security "
          "events is part of the work, both to rebuild the sense of being part of the industry "
          "after heads-down solo study and because referrals come from people who have met you. A "
          "few worth knowing: the OWASP Philadelphia chapter (the most directly relevant group), "
          "Philly 2600 (the lowest-pressure entry point), and OWASP Global AppSec in nearby "
          "Washington DC. Start showing up early \u2014 even one finished PortSwigger lab is "
          "enough to bring and talk about. See the Appendix section \u201c<a href=\"#philly_appsec\" "
          "color=\"#3A7AB8\">Philadelphia AppSec Community</a>\u201d for the full list of groups and "
          "conferences.", S["body"]))
    add(SP(2))
    SS("Note-Taking: Notes \u2192 Note Cards")
    add(P("Two outputs for every chapter or lab section: working notes during study, note cards "
          "derived from them afterward. Notes are for comprehension; note cards are for "
          "retention.", S["body"]))
    add(B("<b>During study:</b> Detailed working notes in your own words. For security concepts: "
          "what the vulnerability is, why the code is exploitable, how an attacker uses it, how "
          "to fix it. Questions you cannot answer yet."))
    add(B("<b>After each section:</b> Extract note cards. One concept per card. Front: "
          "vulnerability name. Back: what it is, how to identify it in code, how to fix it. If "
          "you cannot explain the fix without looking, you do not own the concept."))
    add(B("<b>Chapters marked Skip Note-Taking:</b> One-paragraph summary only. Everything in "
          "Phases II\u2013V gets full note cards \u2014 this is the interview material."))
    add(SP(2))
    add(PageBreak())
    SS("Portfolio: Writeups & Project Site")
    add(P("AppSec portfolios are built differently from software engineering portfolios. What "
          "distinguishes an AppSec candidate is documented offensive work: vulnerability "
          "writeups, lab solutions, CTF walkthroughs, threat model documents. Security hiring "
          "managers look for evidence of real thinking \u2014 someone who can find a "
          "vulnerability, understand why it exists, exploit it, and explain the fix. A "
          "well-written writeup demonstrates all four in a way a resume line never can.", S["body"]))
    add(B("<b>Writeup format:</b> For every major lab or project: what the vulnerability was, how "
          "you identified it, the exploitation proof-of-concept, how to remediate it, what you "
          "look for in a code review to catch it. 800\u20131,200 words. Publish polished versions "
          "on LinkedIn and a personal site."))
    add(B("<b>Target:</b> at least two published writeups before you begin applying, building to "
          "4\u20136 before the main application push. Quality over quantity."))
    add(B("<b>GitHub:</b> Commit from Day 1 \u2014 the very first commit is this study plan and its "
          "build script. Keep one repository for the entire cybersecurity journey: notes, "
          "tooling-phase scripts, custom Semgrep rules, automation tools, and lab artifacts, "
          "building a continuous commit history from the start. Every README explains the "
          "methodology and what the artifact demonstrates \u2014 not just usage instructions."))

    # ════════════════════════════════════════════════════════════════════════
    #  PITFALLS & RISK ASSESSMENT
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("AppSec: Potential Pitfalls & Risk Assessment")
    concept("AI Replacing AppSec Engineers \u2014 Real but Limited",
            "AI-assisted SAST tools (GitHub Copilot Autofix, Snyk Code, Semgrep with AI triage) "
            "are improving and will automate more routine vulnerability scanning over time. The "
            "roles being automated are the lowest-end scan-and-report functions, not the manual "
            "code review, threat modeling, and developer consultation that constitutes senior "
            "AppSec work. Arriving with a portfolio of demonstrated manual security work positions "
            "you above the automation floor from day one.")
    concept("Entry-Level Hiring Compression",
            "AI tools are handling some work that junior security analysts used to do. The "
            "mitigation is the same as it has always been in security hiring: arrive with a "
            "portfolio of real work rather than a list of certifications. Someone who can walk "
            "through a stored XSS chain and connect it to a real bypass they identified during "
            "code review is not competing with the Security+ certificate cohort.")
    concept("The Certification Trap",
            "Sec+ gets you past ATS filters and signals baseline literacy. It does not substitute "
            "for demonstrated hands-on skill in interviews. The plan treats Sec+ as a necessary "
            "filter-passer, not the credential. The portfolio is the credential.")
    concept("Moderate Philly Market",
            "Philadelphia\u2019s AppSec market is real but not as deep as New York, DC, or San "
            "Francisco. The mitigation is remote \u2014 70\u201375% of AppSec postings offer "
            "remote or hybrid. Philadelphia is a base, not a constraint. The local network at "
            "OWASP and BSides matters most for referrals to companies not on job boards.")
    concept("Scope Creep into Red Team",
            "AppSec engineers frequently perform application-level penetration testing as part of "
            "the role \u2014 Burp Suite, manual web app testing, OWASP methodology. This is "
            "expected and built into the plan. The drift to avoid is into full red team or network "
            "penetration testing, which is a distinct specialization requiring different skills "
            "(Active Directory, network exploitation, infrastructure pivoting). Red team is "
            "typically a destination role requiring demonstrated AppSec or pentest experience "
            "first \u2014 not a direct entry point from developer. Master the AppSec role first. "
            "The deeper offensive path opens more easily once you have AppSec experience on your "
            "resume.")
    add(SP(4))
    add(nb("<b>Net assessment:</b> The risks are real. None negate the market opportunity. The "
           "plan as designed \u2014 hands-on lab work over certifications, manual security skill "
           "over automated tooling familiarity, full-stack deployment capability \u2014 is "
           "structured to be resilient to the most likely downside scenarios."))

    # ----- STUDY PLAN PHASE SUMMARY -----
    add(PageBreak())
    H("Study Plan Phase Summary")
    add(SP(4))
    add(P("This plan turns a working software engineer into an entry-level AppSec engineer over roughly seven to eight months. Rather than front-loading theory, it follows a deliberate arc: shore up the engineering base, get hands dirty with offense early, then build depth and professional tooling on top of that foundation.", S["body"]))
    add(SP(6))
    add(P("It opens by refreshing the fundamentals a developer already half-knows — Python and FastAPI, HTTP, Docker, a working local lab (Phase 0) — and immediately follows with a first taste of the attacker mindset (Phase I), so security feels concrete from the start rather than abstract. It then fills the web and network gaps most developers skipped on the way to shipping features (Phase II).", S["body"]))
    add(SP(6))
    add(P("The middle of the plan is the heart of the offensive skill set: going deep on the core vulnerability classes — injection, XSS, broken authentication and access control, SSRF, and the rest — by exploiting each one hands-on in deliberately vulnerable labs (Phase III), then layering on the professional toolchain (Burp Suite, plus SAST, DAST, dependency and secrets scanning) and earning the Burp Suite Certified Practitioner certification, the credential that proves real hands-on web-exploitation skill (Phase IV).", S["body"]))
    add(SP(6))
    add(P("The back half pivots toward the work an AppSec engineer actually does day to day — cloud security basics (Phase V) and secure code review and threat modeling (Phase VI) — rounded out by CompTIA Security+ for breadth and to clear HR filters (Phase VII).", S["body"]))
    add(SP(6))
    add(P("It closes with focused interview preparation (Phase VIII) and the job search itself (Phase IX). Applications begin in parallel from Month 4, though — well before the curriculum is finished — because a growing portfolio of writeups and a passed BSCP is what actually opens doors.", S["body"]))
    add(SP(10))
    for _line in [
        "<b>Phase 0 — Pre-Study: Foundations</b> (Wks 1–3). <b>Purpose:</b> quickly refresh and expand the engineering base before security content — Python/FastAPI, HTTP, Docker, a working lab. <b>Resources:</b> FastAPI docs, HTTP (Notes + MDN). <b>Achievement:</b> a complete FastAPI app built from scratch and a running local lab.",
        "<b>Phase I — AppSec Intro: A Dip into Offense</b> (Wks 4–5). <b>Purpose:</b> first taste of the attacker mindset — how web vulnerabilities are found and exploited. <b>Resources:</b> “Real-World Bug Hunting” (Ch 1–5), PortSwigger Web Security Academy, TryHackMe. <b>Achievement:</b> first labs and published lab writeups.",
        "<b>Phase II — Web & Network Foundations</b> (Mo 1.5–2.25). <b>Purpose:</b> deep HTTP, web, and authentication foundations plus Burp basics. <b>Resources:</b> “Alice and Bob Learn Application Security”, WAHH, Burp Suite docs, PortSwigger Authentication path. <b>Achievement:</b> Burp fluency, HTTP/auth/session mastery, and the PortSwigger Authentication, JWT, and OAuth labs cleared.",
        "<b>Phase III — Core Vulnerability Classes</b> (Mo 2.5–3.5). <b>Purpose:</b> master the core web vulnerability classes hands-on at practitioner depth. <b>Resources:</b> PortSwigger topic paths and their apprentice/practitioner labs, “Hacking APIs”, the OWASP Top 10. <b>Achievement:</b> practitioner labs across the OWASP classes and an OWASP Top 10 writeup series.",
        "<b>Phase IV — Security Testing & Tooling</b> (Mo 3.5–5.25). <b>Purpose:</b> tooling fluency — Burp mastery, SAST, DAST, SCA — and the BSCP certification. <b>Resources:</b> Burp docs, PortSwigger BSCP practice exams, Semgrep, Bandit, OWASP ZAP, Snyk. <b>Achievement:</b> passed the Burp Suite Certified Practitioner (BSCP) exam, completed a full Juice Shop security assessment.",
        "<b>Phase V — Cloud Security Fundamentals</b> (Mo 5.25–5.75). <b>Purpose:</b> AWS security basics — shared responsibility, IAM, and common misconfigurations. <b>Resources:</b> flaws&#46;cloud, flaws2&#46;cloud, AWS IAM docs. <b>Achievement:</b> every level of the flaws&#46;cloud and flaws2&#46;cloud AWS security challenges completed, with writeups.",
        "<b>Phase VI — Secure Code Review & Threat Modeling</b> (Mo 5.75–6.5). <b>Purpose:</b> the core AppSec craft — manual secure code review and threat modeling. <b>Resources:</b> OWASP Code Review Guide, OWASP ASVS, “Threat Modeling: Designing for Security”. <b>Achievement:</b> a documented code review and a threat model project.",
        "<b>Phase VII — CompTIA Security+ Certification</b> (Mo 6.75–7.25). <b>Purpose:</b> earn the credential that clears HR and ATS filters; main application push. <b>Resources:</b> the “Get Certified Get Ahead: SY0-701” study guide and Professor Messer practice exams. <b>Achievement:</b> passed CompTIA Security+ (SY0-701).",
        "<b>Phase VIII — Interview Preparation & Interviewing</b> (Mo 7.5–8). <b>Purpose:</b> convert skills and portfolio into offers — interview prep, story framing, application strategy. <b>Resources:</b> portfolio writeups and mock interviews. <b>Achievement:</b> a polished portfolio and interview narrative, plus active interviewing.",
        "<b>Phase IX — Expected First Days on the Job</b> (Mo 7.75+). <b>Purpose:</b> start strong in the new sub-field and role and know your immediate differentiators. <b>Resources:</b> your accumulated notes and the five core reference books. <b>Achievement:</b> a written 30/60/90-day onboarding plan and early on-the-job wins.",
    ]:
        add(P(_line, S["bulsm"])); add(SP(2))

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE 0 — PRE-STUDY
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("0", "Pre-Study: Foundations", "Weeks 1\u20133 \u00b7 Before Security Content Begins"))
    add(SP(10))
    add(P("Three parallel tracks before security content begins. The FastAPI track is the main "
          "one \u2014 2\u20133 weeks to close out the official docs and build a complete project "
          "from scratch. The others are a few days each, run in parallel. All of this is active, "
          "hands-on work. By the end of Week 3, AppSec content starts immediately.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("FastAPI Official Documentation", "fastapi.tiangolo.com \u2014 Official docs, "
        "self-contained. Resume from Request Body section onward.")
    res("Existing HTTP Notes", "Personal notes (HTML intro + Odin HTTP). Cover request-response, "
        "methods, status codes, URL anatomy, headers, DNS, TCP/IP basics.")
    res("MDN Web Docs \u2014 Using HTTP Cookies", "developer.mozilla.org/en-US/docs/Web/HTTP/"
        "Cookies \u2014 Specifically for Secure, HttpOnly, and SameSite cookie attributes. The "
        "one HTTP topic not covered in existing notes.")
    res("Existing Docker Notes", "Personal notes and note cards covering containers, images, Dockerfiles, "
        "networking, volumes, Compose, Swarm, and Stack. More comprehensive than any online "
        "tutorial.")
    res("OWASP WebGoat", "github.com/WebGoat/WebGoat \u2014 Deliberately insecure web application "
        "covering OWASP Top 10 vulnerability classes with structured hands-on exploitation "
        "modules. Runs via Docker.")
    add(SP(4))
    SS("Pre-Study Schedule \u2014 Weeks 1\u20133")
    step("01", "SETUP", "Git & GitHub Hygiene \u00b7 Day 1", [
        "GitHub profile already exists with past projects. Before new portfolio work begins: "
        "confirm profile is public, bio is current, location is set to Philadelphia, PA.",
        "Review existing pinned repos \u2014 anything from the web dev years that still reflects "
        "well is worth keeping pinned. Anything that does not, unpin.",
        "Create a new repository for the FastAPI project. Commit as you build \u2014 clean "
        "messages, logical history. This repo is a portfolio artifact from day one and will be "
        "the most recent, actively developed project on the profile.",
        "Set up LinkedIn in parallel: headline and About section state the deliberate transition "
        "into application security as of June 2026. Certifications and portfolio links get added "
        "as they are earned and built.",
    ])
    step("02", "REVIEW", "HTTP & Cookies \u00b7 Days 1\u20133", [
        "<b>HTTP:</b> Review existing HTTP notes (PDF, .odt, and note cards). These "
        "cover the request-response model, methods (GET, POST, PUT, PATCH, DELETE), status codes "
        "(2xx, 3xx, 4xx, 5xx), URL anatomy, headers, DNS, and TCP/IP basics.",
        "<b>Cookies:</b> Cookies are not covered in the existing notes. Read MDN \u2018Using HTTP "
        "cookies\u2019 (developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) specifically for the "
        "security attributes: Secure (only sent over HTTPS), HttpOnly (inaccessible to "
        "JavaScript), and SameSite (controls cross-site request behavior). These three attributes "
        "appear throughout security review work.",
        "<b>SQL:</b> SQL is strong from prior study \u2014 joins, normalization, indexing. Do a "
        "fast review using existing SQL note cards.",
    ])
    step("03", "READ + BUILD", "FastAPI Documentation \u2014 Complete \u00b7 Weeks 1\u20133", [
        "The official docs cover Dependencies, Security, Middleware, CORS, and Request/Response "
        "internals \u2014 exactly the sections most relevant to AppSec work. Finishing the docs "
        "builds the complete mental model needed to audit production web codebases.",
        "<b>Starting point:</b> Start from the beginning. Re-read your notes from the covered "
        "sections (intro, path params, query params) first, then continue through the remaining "
        "tutorial sections. Slow down at Dependencies, Security, Middleware, and CORS \u2014 those "
        "four sections warrant the most detailed notes.",
        "<b>Build a personal FastAPI project as part of the reading:</b> Three years of adding to "
        "others\u2019 APIs is solid experience. Building one end-to-end \u2014 from blank file to "
        "deployed container \u2014 completes the picture. Design something small but complete: "
        "5\u20136 endpoints, JWT authentication implemented via FastAPI\u2019s Security module, at "
        "least one dependency-injected auth check, a SQL database connection. The goal is to own a "
        "codebase fully from the ground up, which makes it the best candidate for security "
        "analysis work later in the plan.",
    ])
    step("04", "LEARN + PRACTICE", "Docker \u00b7 Days 2\u20134", [
        "Docker theory, Dockerfiles, networking, volumes, and Compose are all covered in existing "
        "Docker notes \u2014 which go further than any get-started tutorial, covering Swarm, "
        "Stack, and overlay networking. Review those notes rather than reading the online guide.",
        "<b>Practice:</b> Pull and run three containers: (1) nginx web server, (2) PostgreSQL, "
        "(3) OWASP WebGoat. Run, interact, stop, remove each one. Take notes on the commands.",
        "<b>Build:</b> Write a Dockerfile for the FastAPI project. Build it into an image, run it "
        "as a container. Closes the loop between the two parallel tracks.",
    ])
    SS("Projects & Writings \u2014 Pre-Study")
    add(P("<b>Project: FastAPI API \u2014 Built From Scratch</b>", S["bul"]))
    add(P("A complete FastAPI application: 5\u20136 endpoints, JWT auth, dependency-injected auth "
          "checks, SQL database. Committed to GitHub with clean history. First portfolio artifact.",
          S["bulsm"]))
    add(P("<b>Project: Dockerized FastAPI App</b>", S["bul"]))
    add(P("Dockerfile for the FastAPI project. Built into an image, run as a container.", S["bulsm"]))
    add(SP(4))
    SS("Concepts Broached")
    concept("FastAPI security internals",
            "How FastAPI implements authentication and authorization via the Security module and "
            "Depends(). Where JWT validation happens. How middleware intercepts requests. How "
            "CORS is configured at the framework level. These are the layers AppSec engineers "
            "audit when reviewing application code for security issues.")
    concept("Cookie security attributes",
            "Secure, HttpOnly, and SameSite are not just configuration options \u2014 they are "
            "security controls. Their absence or misconfiguration is a finding in any security "
            "review.")
    concept("Docker as a tool in AppSec",
            "Containers provide isolation but also create attack surfaces: exposed ports, "
            "over-permissioned images, secrets in environment variables. Running WebGoat via "
            "Docker is the first hands-on encounter with containerized target environments, which "
            "appear throughout the plan.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE I — APPSEC INTRO
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("I", "AppSec Intro: A Dip into Offense", "Weeks 4\u20135"))
    add(SP(10))
    add(P("AppSec has a mysticism problem: security culture sometimes makes it seem inaccessible "
          "without a decade of CTF grinding. That is not true, and this phase exists to "
          "demonstrate it directly \u2014 before any systematic study begins.", S["body"]))
    add(P("The goal is not to become a penetration tester in two weeks. It is to arrive at the "
          "Web & Network Foundations phase having touched real vulnerability classes with your "
          "hands, developed genuine questions about why they work the way they do, and "
          "established the foundational mental model: every input is a potential attack vector, "
          "and your job is to think about what happens when an attacker controls it.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("PortSwigger Web Security Academy", "portswigger.net/web-security \u2014 The most widely "
        "recommended AppSec learning resource among practitioners. Interactive labs, structured "
        "learning paths, every major vulnerability class covered. Built by the team that makes "
        "Burp Suite. Primary hands-on platform for the entire plan.")
    res("OWASP WebGoat", "github.com/WebGoat/WebGoat \u2014 A deliberately insecure application "
        "for learning. runs locally via Docker. Structured modules per vulnerability class.")
    res("TryHackMe", "tryhackme.com \u2014 Browser-based, beginner-friendly, guided rooms. The "
        "<a href=\"https://tryhackme.com/path/outline/web\" color=\"#3A7AB8\">"
        "\u2018Web Fundamentals\u2019</a> path covers "
        "<a href=\"https://tryhackme.com/room/httpindetail\" color=\"#3A7AB8\">HTTP in Detail</a>, "
        "<a href=\"https://tryhackme.com/room/burpsuitebasics\" color=\"#3A7AB8\">Burp Suite: The Basics</a>, and "
        "<a href=\"https://tryhackme.com/room/owasptop10\" color=\"#3A7AB8\">OWASP Top 10</a>. The \u2018Jr Penetration Tester\u2019 path covers web "
        "vulnerabilities, Burp Suite, and penetration testing methodology.")
    res("“<i>Real-World Bug Hunting</i>”", "Peter Yaworski, No Starch Press, 2019 (nostarch.com) \u2014 A "
        "highly accessible introduction to web vulnerabilities. Real bug bounty reports, plain "
        "English, organized by vulnerability class.")
    add(SP(4))
    SS("AppSec Intro \u2014 Weeks 4\u20135")
    step("01", "EXPLORE", "PortSwigger Academy Orientation \u00b7 Week 4", [
        "Create a free PortSwigger account",
        "Skim the <a href=\"https://portswigger.net/web-security/sql-injection\" color=\"#3A7AB8\">SQL "
        "injection</a> material to get oriented, then complete the first 3\u20134 Apprentice & Practitioner level "
        "<a href=\"https://portswigger.net/web-security/all-labs#sql-injection\" color=\"#3A7AB8\">labs</a>",
        "Skim the <a href=\"https://portswigger.net/web-security/cross-site-scripting\" color=\"#3A7AB8\">"
        "cross-site scripting</a> material to get oriented, then complete the first 3\u20134 Apprentice-level "
        "<a href=\"https://portswigger.net/web-security/all-labs#cross-site-scripting\" color=\"#3A7AB8\">"
        "labs</a> (reflected and stored)",
    ])
    step("02", "READ", "“<i>Real-World Bug Hunting</i>” Ch. 1\u20135 \u00b7 Weeks 4\u20135", [
        "Chapter 1 covers bug bounty and HTTP basics; Chapters 2\u20135 are each a vulnerability "
        "class \u2014 open redirect, HTTP parameter pollution, CSRF, and HTML injection / content "
        "spoofing \u2014 illustrated with real disclosed bug bounty reports",
        "Read actively: when a report describes a finding in a Python or REST API context, pause "
        "and think about what the vulnerable pattern looks like in code \u2014 this builds the "
        "adversarial mental model",
    ])
    step("03", "PROJECT", "WebGoat \u2014 First Exploitation \u00b7 Week 5", [
        "Ensure local WebGoat still executes as expected in local Docker",
        "Complete these WebGoat lessons: SQL Injection (intro), Cross Site Scripting, Cross Site "
        "Scripting (stored), Authentication Bypasses, and Insecure Direct Object References (IDOR)",
        "For each module: exploit it, write your standard documentation (what, why, fix, code "
        "review pattern)",
    ])
    step("04", "EXPLORE", "TryHackMe Orientation \u00b7 Week 5", [
        "Complete three short <a href=\"https://tryhackme.com/path/outline/web\" color=\"#3A7AB8\">Web Fundamentals</a> rooms \u2014 "
        "<a href=\"https://tryhackme.com/room/httpindetail\" color=\"#3A7AB8\">HTTP in Detail</a>, "
        "<a href=\"https://tryhackme.com/room/burpsuitebasics\" color=\"#3A7AB8\">Burp Suite: The Basics</a>, and "
        "<a href=\"https://tryhackme.com/room/owasptop10\" color=\"#3A7AB8\">OWASP Top 10</a>",
        "These are short and designed for orientation, not mastery",
    ])
    SS("Projects & Writings \u2014 AppSec Intro")
    add(P("<b>Project: WebGoat Exploitation Log</b>", S["bul"]))
    add(P("For each WebGoat module completed, document: the vulnerability class, exploitation "
          "steps, root cause in the code, and the fix. First evidence of hands-on work in the "
          "portfolio.", S["bulsm"]))
    add(P("<b>Writing: What SQL Injection Taught Me About Trusting Input (900\u20131,200 words)</b>",
          S["bul"]))
    add(P("Plain-English explanation of what SQL injection is, why it works, and one thing that "
          "surprised you. Publish on LinkedIn when polished. Framing: \u2018I have been building "
          "APIs for five years. Here is what I learned when I tried to break one.\u2019", S["bulsm"]))
    add(SP(4))
    SS("Concepts Broached")
    concept("The OWASP Top 10",
            "Introduced as a taxonomy. You have seen SQL injection and XSS in practice. The full "
            "Top 10 is a structured catalog of the most critical web vulnerability classes. "
            "Mastery of each class comes through dedicated study.")
    concept("Injection as a class",
            "Any time user input reaches an interpreter without proper sanitization, injection is "
            "possible. SQL injection is the canonical example. Command injection, LDAP injection, and "
            "template injection follow the same logic.")
    concept("The attacker\u2019s mindset",
            "The mental shift from \u2018does this work?\u2019 to \u2018what happens when I control "
            "this input?\u2019 This is the foundational perspective change. You have started "
            "making it.")
    concept("HTTP as the attack surface",
            "Every web vulnerability lives in the HTTP layer \u2014 parameters, headers, cookies, "
            "request bodies. Understanding HTTP is the substrate for every vulnerability class in "
            "this plan.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("OWASP Top 10",
            "This is the vocabulary of every AppSec interview and code review conversation. When "
            "a developer asks why their code is flagged, you explain which OWASP category it falls "
            "into and why it matters.")
    concept("Injection mindset",
            "When reviewing an API endpoint that accepts user input, your first question is "
            "always: does this input reach an interpreter? A database query? A shell command? A "
            "template renderer? This question catches more vulnerabilities than any automated "
            "tool.")
    concept("HTTP literacy",
            "Every Burp Suite session, every manual pentest, every DAST scan result is an HTTP "
            "transaction. Reading raw HTTP requests and responses fluently is required for the "
            "work.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE II — WEB & NETWORK FOUNDATIONS
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("II", "Web & Network Foundations", "Months 1.5\u20132.25"))
    add(SP(10))
    add(P("This phase builds the technical foundation for AppSec work. Every major vulnerability "
          "class lives inside HTTP, authentication protocols, browser security models, or API "
          "design patterns. The phase reframes these layers from an adversarial perspective "
          "\u2014 not just how they work, but why they fail. It closes with a focused final week on "
          "cryptography fundamentals and the specific networking knowledge that appears in "
          "AppSec interviews.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("“<i>Alice and Bob Learn Application Security</i>”", "Tanya Janca (SheHacksPurple), Wiley, 2020 "
        "(wiley.com) \u2014 250 pages covering threat modeling, secure code review, SDLC "
        "security, and how to work with developers. Covers the defender-side, program-building "
        "angle that pure offensive resources miss.")
    res("“<i>The Web Application Hacker’s Handbook</i>”", "Dafydd Stuttard and Marcus Pinto, Wiley, "
        "2011 (wiley.com) \u2014 Foundational reference written by the creator of Burp Suite. Ch. "
        "1\u20133 cover web application security, core defense mechanisms, and web application technologies. Ch. 6 covers "
        "authentication, Ch. 7 session management, Ch. 8 access controls. Some content is aging "
        "but these chapters remain the clearest treatment available.")
    res("PortSwigger Web Security Academy", "portswigger.net/web-security \u2014 Primary lab "
        "platform for this phase. Covers HTTP fundamentals, Burp Suite basics, authentication "
        "attacks, access control vulnerabilities, and SQL injection \u2014 all with interactive "
        "labs.")
    res("MDN Web Docs", "developer.mozilla.org \u2014 The authoritative reference for HTTP, "
        "cookies, CORS, CSP, and the browser security model. Covers each security header, its "
        "syntax, and its security purpose in depth.")
    res("OWASP SSRF Prevention Cheat Sheet", "cheatsheetseries.owasp.org/cheatsheets/"
        "Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html \u2014 Covers DNS rebinding "
        "attack mechanics, private IP range blocking patterns, and SSRF prevention guidance.")
    res("TryHackMe \u2018Pre-Security\u2019 path \u2014 Network Fundamentals module",
        "tryhackme.com/module/network-fundamentals \u2014 Primary resource for the networking week. Covers OSI model, TCP/IP, "
        "ports, and how packets travel in 3\u20134 interactive hours. Not Net+, not CCNA \u2014 "
        "precisely scoped for AppSec-relevant networking.")
    res("TryHackMe \u2018Pre-Security\u2019 path \u2014 Putting It All Together room",
        "tryhackme.com/room/puttingitalltogether \u2014 Covers how all the components of a web request fit together: DNS, "
        "HTTP, load balancers, CDNs, databases, and how each layer relates to security decisions.")
    res("OWASP Cryptographic Storage Cheat Sheet", "cheatsheetseries.owasp.org/cheatsheets/"
        "Cryptographic_Storage_Cheat_Sheet.html \u2014 Primary reference for the cryptography "
        "week. Covers which algorithms are acceptable and which are broken, key management, and "
        "storage patterns.")
    res("OWASP Transport Layer Security Cheat Sheet", "cheatsheetseries.owasp.org/cheatsheets/"
        "Transport_Layer_Security_Cheat_Sheet.html \u2014 TLS configuration, certificate "
        "management, and common misconfigurations. Companion to the crypto week.")
    res("hashcat", "hashcat.net/wiki \u2014 Password cracking tool used in the cryptography week "
        "to crack an MD5 hash and make weak hashing concrete. The wiki includes a beginner page "
        "with exact example commands for MD5 wordlist attacks.")
    res("bcrypt (Python library)", "pypi.org/project/bcrypt \u2014 Python library for bcrypt "
        "password hashing. Used in the cryptography week to implement correct password hashing in "
        "Python. Simple API: hash a password, verify a password.")
    add(SP(4))
    SS("Web & Network Foundations \u2014 Months 1.5\u20132.25")
    step("01", "READ + LABS", "HTTP Deep Dive \u00b7 Week 6", [
        "Read <i>WAHH</i> Ch. 1\u20133 (web application security, core defense mechanisms, web application "
        "technologies) as foundational context",
        "Install <a href=\"https://portswigger.net/burp/communitydownload\" color=\"#3A7AB8\">Burp Suite Community Edition</a>, then work through the official documentation \u2014 "
        "<a href=\"https://portswigger.net/burp/documentation/desktop/tools/proxy\" color=\"#3A7AB8\">Proxy</a>, <a href=\"https://portswigger.net/burp/documentation/desktop/tools/repeater\" color=\"#3A7AB8\">Repeater</a>, and "
        "<a href=\"https://portswigger.net/burp/documentation/desktop/tools/intruder\" color=\"#3A7AB8\">Intruder</a> \u2014 the primary tools you will use throughout this phase",
        "Read <a href=\"https://portswigger.net/web-security/cors\" color=\"#3A7AB8\">CORS misconfigurations</a>, "
        "<a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP\" color=\"#3A7AB8\">CSP</a>, <a href=\"https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html\" color=\"#3A7AB8\">TLS</a>, <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods\" color=\"#3A7AB8\">HTTP methods</a>, and "
        "<a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status\" color=\"#3A7AB8\">status codes</a> for their security implications",
        "<b>Full notes + note cards:</b> CORS misconfigurations, CSP, TLS, HTTP methods, and status codes with security implications",
    ])
    step("02", "READ + LABS", "Authentication & Session Management \u00b7 Weeks 6\u20137", [
        "Read <i>WAHH</i> Ch. 6 (Attacking Authentication) and Ch. 7 (Attacking Session Management)",
        "Complete the PortSwigger <a href=\"https://portswigger.net/web-security/authentication\" color=\"#3A7AB8\">Authentication</a> learning path \u2014 all apprentice and "
        "practitioner <a href=\"https://portswigger.net/web-security/all-labs#authentication\" color=\"#3A7AB8\">labs</a>",
        "Complete the <a href=\"https://portswigger.net/web-security/jwt\" color=\"#3A7AB8\">JWT</a> learning path, then its <a href=\"https://portswigger.net/web-security/all-labs#jwt\" color=\"#3A7AB8\">labs</a> \u2014 unverified signature, flawed signature verification, weak signing key, jwk / jku injection, and <i>algorithm confusion</i>; then the <a href=\"https://portswigger.net/web-security/oauth\" color=\"#3A7AB8\">OAuth</a> learning path and its <a href=\"https://portswigger.net/web-security/all-labs#oauth-authentication\" color=\"#3A7AB8\">labs</a> \u2014 implicit-flow bypass, forced profile linking, and <i>account hijacking via redirect_uri</i>",
        "<b>Full notes + note cards:</b> Password enumeration, session fixation, JWT algorithm confusion, OAuth redirect URI manipulation",
    ])
    step("03", "PROJECT", "Authentication Audit Checklist \u00b7 Week 7", [
        "Write a 1\u20132 page authentication audit checklist from scratch \u2014 no templates",
        "Every item should come from a concept in your notes",
        "For each item: what you check, how you check it (manually and with what tool), and what "
        "a finding looks like",
        "Run the checklist against the FastAPI app you built in Phase 0 \u2014 it implements JWT "
        "authentication via FastAPI\u2019s Security module, so it is the ideal first audit "
        "target. Record any findings.",
        "Push to GitHub as Markdown. First real security artifact in the portfolio.",
    ])
    step("04", "READ + LABS", "Access Control & APIs \u00b7 Week 7", [
        "Read <i>WAHH</i> Ch. 8 (Attacking Access Controls)",
        "Read the PortSwigger <a href=\"https://portswigger.net/web-security/access-control\" color=\"#3A7AB8\">Access control</a> and <a href=\"https://portswigger.net/web-security/api-testing\" color=\"#3A7AB8\">API testing</a> learning paths, then work the "
        "apprentice-level Access control <a href=\"https://portswigger.net/web-security/all-labs#access-control-vulnerabilities\" color=\"#3A7AB8\">labs</a> and API testing <a href=\"https://portswigger.net/web-security/all-labs#api-testing\" color=\"#3A7AB8\">labs</a> to build the foundational mental model \u2014 the practitioner labs follow in Phase III",
        "<b>Full notes + note cards:</b> IDOR, horizontal/vertical privilege escalation, mass "
        "assignment, excessive data exposure",
    ])
    step("05", "READ + LABS", "Input Handling Fundamentals \u00b7 Weeks 7\u20138", [
        "Read the PortSwigger <a href=\"https://portswigger.net/web-security/sql-injection\" color=\"#3A7AB8\">SQL injection</a> learning path, then work the apprentice-level <a href=\"https://portswigger.net/web-security/all-labs#sql-injection\" color=\"#3A7AB8\">labs</a> to internalize the "
        "input-validation root cause \u2014 the practitioner labs follow in Phase III",
        "<b>Full notes + note cards:</b> SQL injection root cause, parameterized queries, "
        "injection taxonomy",
    ])
    step("06", "READ", "“<i>Alice and Bob Learn Application Security</i>” \u00b7 Week 8", [
        "Read “<i>Alice and Bob Learn Application Security</i>” Ch. 1\u20135 and Ch. 7: security "
        "fundamentals, security requirements, secure design, and common pitfalls (Ch. 1\u20135), and "
        "what an AppSec program does day-to-day (Ch. 7)",
        "Read during this week \u2014 this is the defender and program-building perspective that "
        "PortSwigger and <i>WAHH</i> do not cover",
        "<b>Key insight:</b> AppSec is not just finding vulnerabilities \u2014 it is building "
        "processes so developers stop introducing them",
        "<b>Full notes + note cards:</b> SDLC security touchpoints, developer security hygiene "
        "checklist, what an AppSec program actually does day-to-day",
    ])
    step("07", "STUDY", "Cryptography Fundamentals \u00b7 Week 9", [
        "Review existing sys design notes on auth and basic security before any new reading. The "
        "goal this week is the AppSec angle: how cryptographic primitives fail, what broken "
        "implementations look like in code, and how to flag them in a security review.",
        "Read the <a href=\"https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html\" color=\"#3A7AB8\">OWASP Cryptographic Storage Cheat Sheet</a> and the "
        "<a href=\"https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html\" color=\"#3A7AB8\">OWASP Transport Layer Security Cheat Sheet</a>. Take notes.",
        "<b>Hands-on:</b> <a href=\"https://www.freecodecamp.org/news/hacking-with-hashcat-a-practical-guide/\" color=\"#3A7AB8\">Crack an MD5 hash with hashcat</a>. "
        "<a href=\"https://pypi.org/project/bcrypt/\" color=\"#3A7AB8\">Implement bcrypt password hashing in Python</a>. "
        "These make the concepts concrete.",
        "<b>Full notes + note cards:</b> One card per algorithm type covered in the cheat sheets. "
        "Front: name and use case. Back: when to use it, what breaks it, what a broken "
        "implementation looks like in code.",
    ])
    step("08", "STUDY", "Networking Fundamentals for AppSec \u00b7 Week 9", [
        "Complete the TryHackMe \u2018Pre-Security\u2019 path \u2014 <a href=\"https://tryhackme.com/module/network-fundamentals\" color=\"#3A7AB8\">Network Fundamentals module</a>. "
        "Take notes.",
        "Review existing notes for the URL-to-response flow.",
        "Read the <a href=\"https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html\" color=\"#3A7AB8\">OWASP SSRF Prevention Cheat Sheet</a> \u2014 specifically the DNS rebinding section.",
        "Complete the TryHackMe \u2018Pre-Security\u2019 path \u2014 <a href=\"https://tryhackme.com/room/puttingitalltogether\" color=\"#3A7AB8\">Putting It All Together room</a>.",
        "<b>Full notes + note cards:</b> OSI layers 3/4/7 with one AppSec example each; TCP vs "
        "UDP with one security implication each; the URL request flow; common ports; private IP "
        "ranges; what a firewall, load balancer, and reverse proxy each do.",
    ])
    step("09", "WRITE", "Authentication Writeup + LinkedIn Post \u00b7 Week 9", [
        "Publish 800\u20131,200 word LinkedIn article: \u2018Five JWT vulnerabilities I found "
        "while reviewing authentication code\u2019",
        "Use examples from the PortSwigger labs. Frame it as a developer who learned to break "
        "what they built",
    ])
    SS("Concepts Mastered")
    concept("HTTP security model",
            "Every HTTP header that has security implications, what it does, and what happens when "
            "it is misconfigured. The substrate of every web vulnerability.")
    concept("Authentication and session security",
            "How authentication protocols work and how they fail. JWT algorithm confusion alone "
            "appears in more real breaches than most developers realize.")
    concept("Access control",
            "IDOR, privilege escalation, horizontal vs. vertical access control flaws. The most "
            "common vulnerability class in production applications in 2026.")
    concept("API security",
            "REST API-specific vulnerability patterns \u2014 broken object-level authorization "
            "(IDOR), mass assignment, and excessive data exposure \u2014 and why APIs widen the "
            "attack surface beyond traditional server-rendered applications.")
    concept("Input validation",
            "The root cause of injection vulnerabilities. Every injection class shares the same "
            "root cause: unsanitized user input reaching an interpreter.")
    concept("Cryptography fundamentals",
            "Hashing vs. encryption vs. encoding. Which algorithms are broken (MD5, SHA-1 for "
            "passwords, DES, RC4) and which are correct (bcrypt, AES-GCM, RSA). How to identify "
            "weak crypto in a code review without being a cryptographer.")
    concept("Networking fundamentals for AppSec",
            "OSI layers 3 (Network/IP), 4 (Transport/TCP-UDP), and 7 (Application/HTTP) and why "
            "AppSec lives at layer 7. TCP vs UDP and one security implication of each. The seven "
            "steps of a URL request from DNS query to HTTP response. Common ports and the "
            "services on them. Private IP ranges (10.x, 172.16.x, 192.168.x), localhost "
            "(127.0.0.1), and the AWS metadata endpoint (169.254.169.254). Standard web app "
            "network architecture: internet \u2192 firewall \u2192 load balancer \u2192 app server "
            "\u2192 database. What a firewall, load balancer, and reverse proxy each do and what "
            "security question to ask about each.")
    concept("Networking as an attack surface",
            "DNS rebinding exploits the gap between DNS validation and TCP connection. SSRF "
            "against private IP ranges and 169.254.169.254 is the most common high-severity cloud "
            "vulnerability. Understanding where TLS terminates in a web architecture tells you "
            "whether internal traffic is encrypted. Open unexpected ports in a deployment "
            "configuration are a finding.")
    concept("Networking as an attack surface",
            "DNS resolution flow and why DNS rebinding bypasses SSRF protections. The AWS metadata "
            "endpoint (169.254.169.254) and why SSRF against it is a critical-severity finding. "
            "Why HTTP statelessness makes cookies necessary and therefore an attack surface. "
            "These are not networking engineering concepts \u2014 they are the specific networking "
            "behaviors that AppSec engineers encounter in real work.")
    concept("AppSec program thinking (Janca)",
            "AppSec is not just finding bugs \u2014 it is building the processes, training, and "
            "SDLC integration that stop bugs from being introduced. The developer\u2019s "
            "perspective on the defensive side of the role.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("HTTP headers in code review",
            "When reviewing a PR that sets cookies or configures CORS, you check HttpOnly, Secure, "
            "SameSite, and Access-Control-Allow-Origin as a reflex. Most developers do not know "
            "these flags exist.")
    concept("JWT review",
            "JWT configuration is the first thing you check: algorithm whitelisted? Signature "
            "verified? Claims validated? Three questions catch the most common JWT vulnerabilities.")
    concept("IDOR in API review",
            "When reviewing an API endpoint that returns data based on a user-supplied ID, you "
            "ask: is the user\u2019s authorization checked against the requested resource, or just "
            "their authentication? This question catches IDOR every time.")
    concept("Cryptography in code review",
            "When you see a password hash, you check whether it is bcrypt/Argon2 (correct) or "
            "MD5/SHA-1 (flag immediately). When you see encrypted data, you check for AES-GCM "
            "(correct) vs AES-ECB (flag). When you see a secret, you check whether it is hardcoded "
            "or pulled from a secret manager. These are reflex checks that take seconds once the "
            "vocabulary is owned.")
    concept("Networking in architecture review and interviews",
            "When asked \u2018where does TLS terminate?\u2019 in an interview or architecture "
            "review, you can answer and explain the security implication. When reviewing a "
            "deployment configuration, you check for unexpected open ports. When a threat model "
            "shows a service making outbound HTTP calls, you ask whether SSRF mitigations are in "
            "place and whether private IP ranges are blocked. When an interviewer describes "
            "traffic from an EC2 instance to 169.254.169.254 and asks if it is concerning, the "
            "answer is yes \u2014 SSRF against the metadata endpoint.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE III — CORE VULNERABILITY CLASSES
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("III", "Core Vulnerability Classes", "Months 2.5–3.5"))
    add(SP(10))
    add(P("Phase III is the technical core of the plan. The OWASP Top 10 is the field’s shared "
          "vocabulary for the most critical web application security risks. Every AppSec interview "
          "assumes you know these. Every code review uses them as a checklist. Every penetration "
          "test methodology is organized around them. This phase goes deep on each class — not "
          "survey knowledge, but genuine understanding of root cause, exploitation mechanics, and "
          "remediation. Complete every Apprentice and Practitioner lab in each learning path below. "
          "Expert labs are stretch goals.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("PortSwigger Web Security Academy", "portswigger.net/web-security — Primary lab platform "
        "for this phase. Interactive labs covering every major vulnerability class: injection, XSS, "
        "CSRF, SSRF, XXE, access control, business logic, deserialization, file upload, path "
        "traversal, and API testing.")
    res("OWASP Top 10 (Web)", "owasp.org/www-project-top-ten — The ten most critical web "
        "application vulnerabilities. Each entry includes a description, example attack scenarios, "
        "and prevention guidance.")
    res("OWASP API Security Top 10", "owasp.org/www-project-api-security — The API-specific "
        "companion to the web Top 10. Covers BOLA (Broken Object Level Authorization), BFLA "
        "(Broken Function Level Authorization), broken authentication, excessive data exposure, "
        "and SSRF as they manifest in REST APIs.")
    res("OWASP Testing Guide v4.2", "owasp.org/www-project-web-security-testing-guide — The "
        "methodology reference. For each vulnerability class, it describes how to test "
        "systematically.")
    res("“<i>Alice and Bob Learn Application Security</i>”", "Tanya Janca (SheHacksPurple), Wiley, 2020 "
        "(wiley.com) — Ch. 6–8 cover common pitfalls, securing modern applications, and building "
        "an AppSec program.")
    res("“<i>Hacking APIs</i>”", "Corey Ball, No Starch Press, 2022 (nostarch.com) — REST API security "
        "testing. Ch. 1–3 and Ch. 6–9 cover API reconnaissance, endpoint discovery, and "
        "authentication testing.")
    add(SP(4))
    SS("Core Vulnerability Classes — Months 2.5–3.5")
    step("01", "READ + LABS: Injection Classes", "Weeks 10–11", [
        "<b>Buy Burp Suite Professional now</b> (~$499/yr) \u2014 the out-of-band labs in this phase need <a href=\"https://portswigger.net/burp/documentation/desktop/tools/collaborator\" color=\"#3A7AB8\">Burp Collaborator</a>, which is Pro-only. Buying at the start of Phase III lets you do every lab here in place instead of skipping the Collaborator-based ones, and you use Pro continuously from here through the BSCP exam. See <a href=\"https://portswigger.net/burp/pro\" color=\"#3A7AB8\">Burp Suite Professional</a>.",
        "Re-read your Phase II <a href=\"https://portswigger.net/web-security/sql-injection\" color=\"#3A7AB8\">SQL injection</a> notes (the learning path stays linked if you need it), then complete the "
        "practitioner <a href=\"https://portswigger.net/web-security/all-labs#sql-injection\" color=\"#3A7AB8\">labs</a> \u2014 the UNION-based and blind (boolean- and time-based) techniques, plus the out-of-band labs (Burp Collaborator \u2014 you now have Pro)",
        "Work through the PortSwigger <a href=\"https://portswigger.net/web-security/os-command-injection\" color=\"#3A7AB8\">OS command injection</a> and <a href=\"https://portswigger.net/web-security/server-side-template-injection\" color=\"#3A7AB8\">Server-side template injection</a> learning paths, then their labs \u2014 the OS command injection <a href=\"https://portswigger.net/web-security/all-labs#os-command-injection\" color=\"#3A7AB8\">labs</a> (the simple case plus blind time-delay and output-redirection, and out-of-band exfiltration via Collaborator) and the basic SSTI <a href=\"https://portswigger.net/web-security/all-labs#server-side-template-injection\" color=\"#3A7AB8\">labs</a> only (enough to recognize SSTI in review; skip the engine-specific gadget exploitation)",
        "<b>For each lab:</b> exploit it, write your standard documentation (what, why, fix, code review "
        "pattern)",
    ])
    step("02", "PROJECT: OWASP Top 10 Writeup Series", "Throughout Weeks 10–14", [
        "One 800–1,200 word writeup per <a href=\"https://owasp.org/www-project-top-ten/\" color=\"#3A7AB8\">OWASP Top 10</a> category, published progressively throughout "
        "this phase",
        "Not academic summaries — structured as: what it is, real-world example, how you "
        "identified it in a lab, how to fix it, what to look for in code review",
        "These ten writeups are the backbone of your AppSec portfolio",
    ])
    step("03", "READ + LABS: Cross-Site Scripting", "Week 11", [
        "Complete the PortSwigger <a href=\"https://portswigger.net/web-security/cross-site-scripting\" color=\"#3A7AB8\">Cross-site scripting</a> learning path, then the <a href=\"https://portswigger.net/web-security/all-labs#cross-site-scripting\" color=\"#3A7AB8\">labs</a> covering reflected, stored, and DOM XSS, the DOM-sink variants, and the exploitation labs (stealing cookies, XSS-to-CSRF); skip the long tail of "
        "near-identical context-encoding and filter-bypass permutations",
        "<b>XSS in React:</b> React’s JSX escaping prevents many reflected XSS vectors by default. The "
        "key exception is dangerouslySetInnerHTML, which bypasses JSX escaping entirely and is a "
        "standard code review finding.",
        "<b>Key:</b> XSS to account takeover chains — cookie theft, CSRF token theft, keylogging",
    ])
    step("04", "READ + LABS: CSRF, SSRF, XXE", "Weeks 11–12", [
        "Complete the PortSwigger <a href=\"https://portswigger.net/web-security/csrf\" color=\"#3A7AB8\">CSRF</a>, <a href=\"https://portswigger.net/web-security/ssrf\" color=\"#3A7AB8\">SSRF</a>, and <a href=\"https://portswigger.net/web-security/xxe\" color=\"#3A7AB8\">XXE</a> learning paths, then their labs \u2014 the CSRF <a href=\"https://portswigger.net/web-security/all-labs#cross-site-request-forgery-csrf\" color=\"#3A7AB8\">labs</a> in full (each is a distinct broken-defense pattern), the apprentice and practitioner SSRF <a href=\"https://portswigger.net/web-security/all-labs#server-side-request-forgery-ssrf\" color=\"#3A7AB8\">labs</a> (skip the two expert labs \u2014 Shellshock and the whitelist-filter bypass), and the core XXE <a href=\"https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection\" color=\"#3A7AB8\">labs</a> (file retrieval, SSRF, and one blind example \u2014 all apprentice and practitioner)",
        "<b>SSRF:</b> a vulnerability where an attacker tricks a server into making HTTP requests to "
        "unintended destinations — including internal services and cloud metadata endpoints. API "
        "endpoints that fetch user-supplied URLs are the primary SSRF surface. The exploitation "
        "mechanics are covered in this phase.",
        "Cloud metadata service attacks (169.254.169.254) are the canonical SSRF exploitation "
        "target",
    ])
    step("05", "READ + LABS: Access Control & Business Logic", "Week 12", [
        "Review your Phase II <a href=\"https://portswigger.net/web-security/access-control\" color=\"#3A7AB8\">Access control</a> notes, then complete the remaining practitioner "
        "<a href=\"https://portswigger.net/web-security/all-labs#access-control-vulnerabilities\" color=\"#3A7AB8\">labs</a> \u2014 the URL-, method-, and Referer-based bypasses and multi-step gaps",
        "Work through the PortSwigger <a href=\"https://portswigger.net/web-security/logic-flaws\" color=\"#3A7AB8\">Business logic vulnerabilities</a> learning path, then its apprentice and practitioner <a href=\"https://portswigger.net/web-security/all-labs#business-logic-vulnerabilities\" color=\"#3A7AB8\">labs</a> \u2014 each is a distinct logic flaw, and this is the class your developer background most directly advantages, so cover it well",
        "Business logic is the vulnerability class automated tools miss entirely — developer "
        "background is the structural advantage here",
    ])
    step("06", "READ + LABS: Deserialization, File Upload, Path Traversal", "Week 13", [
        "Complete the PortSwigger <a href=\"https://portswigger.net/web-security/deserialization\" color=\"#3A7AB8\">Insecure deserialization</a>, <a href=\"https://portswigger.net/web-security/file-upload\" color=\"#3A7AB8\">File upload</a>, and <a href=\"https://portswigger.net/web-security/file-path-traversal\" color=\"#3A7AB8\">Path traversal</a> learning paths, then their labs \u2014 the deserialization <a href=\"https://portswigger.net/web-security/all-labs#insecure-deserialization\" color=\"#3A7AB8\">labs</a> concept set only (modifying serialized data, using application functionality, one gadget-chain example; skip the extra language-specific gadget chains), the apprentice and practitioner file upload <a href=\"https://portswigger.net/web-security/all-labs#file-upload-vulnerabilities\" color=\"#3A7AB8\">labs</a> in full, including the expert web-shell-via-race-condition lab (Burp Pro), and the path traversal <a href=\"https://portswigger.net/web-security/all-labs#path-traversal\" color=\"#3A7AB8\">labs</a> in full (each is a distinct filter bypass)",
        "Less common than injection and XSS but high-severity in enterprise codebases when present",
    ])
    step("07", "READ + LABS: API Security Deep Dive", "Weeks 13–14", [
        "Read the <a href=\"https://owasp.org/www-project-api-security/\" color=\"#3A7AB8\">OWASP API Security Top 10</a> in full",
        "Key additions over the web Top 10: BOLA (Broken Object Level Authorization = IDOR for "
        "APIs), BFLA (Broken Function Level Authorization), Mass Assignment, Excessive Data "
        "Exposure",
        "Read “<i>Hacking APIs</i>” Ch. 1–3 (how web applications and APIs work, and the common API "
        "vulnerability classes) and Ch. 6–9 (API discovery and reconnaissance, endpoint analysis, "
        "authentication attacks, and fuzzing)",
        "Review your Phase II <a href=\"https://portswigger.net/web-security/api-testing\" color=\"#3A7AB8\">API testing</a> notes, then complete the remaining practitioner "
        "<a href=\"https://portswigger.net/web-security/all-labs#api-testing\" color=\"#3A7AB8\">labs</a> \u2014 BOLA, mass assignment, and excessive data exposure",
        "Work through it treating your own past API work as the mental target: would the APIs "
        "you built have been vulnerable?",
    ])
    SS("Concepts Mastered")
    concept("Injection — complete taxonomy",
            "SQL, command, template, LDAP, NoSQL. Root cause: unsanitized user input reaching an "
            "interpreter. Fix: parameterized queries. Code review: any string concatenation that "
            "includes user input reaching an interpreter.")
    concept("XSS — all three types",
            "Reflected, stored, DOM. Root cause: user input rendered as HTML without encoding. "
            "<b>Fix:</b> context-appropriate output encoding. Code review: any innerHTML assignment, "
            "dangerouslySetInnerHTML, server-side template rendering of user data.")
    concept("CSRF and SSRF",
            "CSRF exploits browser trust. SSRF exploits server trust to reach internal resources. "
            "<b>Fix:</b> SameSite cookies for CSRF; URL allowlists for SSRF.")
    concept("Access control flaws",
            "The most common finding in production AppSec work. Fix: verify the authenticated user "
            "is authorized for the specific resource on every request.")
    concept("Business logic vulnerabilities",
            "Not detectable by automated tools. Requires understanding intended behavior. The "
            "developer background is the advantage.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("Injection in code review",
            "Every database query, every shell command, every template render gets the same "
            "question: does user input reach this without sanitization? One question catches the "
            "whole class.")
    concept("XSS in React code review",
            "React escapes JSX output by default, which prevents many reflected XSS vectors. The "
            "three things to check in a React code review: dangerouslySetInnerHTML usage (bypasses "
            "JSX escaping entirely), third-party component XSS vectors, and any server-rendered "
            "template output that feeds into the React tree.")
    concept("SSRF in API review",
            "Any endpoint accepting a URL parameter is flagged immediately. Does it fetch that URL "
            "server-side? Is the response returned to the user? Is there a URL allowlist? Three "
            "questions.")
    concept("Business logic in threat modeling",
            "This is the vulnerability class that threat modeling catches before it ships. STRIDE "
            "analysis of a data flow diagram surfaces the business logic assumptions that could be "
            "violated.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE IV — SECURITY TESTING & TOOLING
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("IV", "Security Testing & Tooling", "Months 3.5–5.25"))
    add(SP(10))
    add(P("Phase IV moves from knowing vulnerability classes to operating the professional "
          "toolchain used to find them systematically. Burp Suite is the primary tool. SAST "
          "(static analysis of source code, via Semgrep) and DAST (dynamic testing of the running app) are the automation layer. The goal is to reach a level of tool "
          "fluency where tooling becomes leverage, not a learning distraction — you use Burp Suite "
          "to find vulnerabilities faster, not to compensate for not understanding them.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("Burp Suite Documentation", "portswigger.net/burp/documentation — Official documentation "
        "for all Burp Suite tools: <a href=\"https://portswigger.net/burp/documentation/desktop/tools/proxy\" color=\"#3A7AB8\">Proxy</a>, <a href=\"https://portswigger.net/burp/documentation/desktop/tools/repeater\" color=\"#3A7AB8\">Repeater</a>, <a href=\"https://portswigger.net/burp/documentation/desktop/tools/intruder\" color=\"#3A7AB8\">Intruder</a>, <a href=\"https://portswigger.net/burp/documentation/desktop/tools/sequencer\" color=\"#3A7AB8\">Sequencer</a>, and <a href=\"https://portswigger.net/burp/vulnerability-scanner\" color=\"#3A7AB8\">Scanner</a>.")
    res("Semgrep Documentation", "semgrep.dev/docs — Primary for general SAST. The leading "
        "open-source SAST tool, most commonly referenced in AppSec job postings. Sufficient for "
        "the entire plan.")
    res("Bandit Documentation", "bandit.readthedocs.io — Python-specific SAST tool. Detects "
        "insecure subprocess calls, eval() usage, weak SSL contexts, hardcoded passwords, insecure "
        "pickle and yaml usage.")
    res("OWASP ZAP Documentation", "zaproxy.org/docs — the free, open-source OWASP DAST tool: an intercepting proxy plus an automated scanner that crawls a running app and runs active and passive checks for common web vulnerabilities. A free alternative to Burp Scanner, with a baseline scan that wires easily into CI.")
    res("Snyk Documentation", "docs.snyk.io — Software composition analysis (SCA) — finding "
        "vulnerabilities in third-party dependencies. Available with a free tier.")
    res("PortSwigger Web Security Academy", "portswigger.net/web-security — Primary resource for "
        "Burp Suite mastery and BSCP preparation. The Burp Suite learning path and BSCP practice "
        "exams live here.")
    res("OWASP WebGoat", "github.com/WebGoat/WebGoat — Deliberately insecure application. Used as "
        "a SAST scan target — run Semgrep and Bandit against its Python source to practice "
        "identifying real vulnerability patterns.")
    res("OWASP Juice Shop", "owasp.org/www-project-juice-shop — Deliberately insecure modern web "
        "application. The primary target for this phase’s full security assessment: Burp Suite "
        "manual testing, ZAP DAST scan, Semgrep SAST, Snyk SCA. Runs via Docker or Node.")
    res("TruffleHog", "github.com/trufflesecurity/trufflehog — Secrets scanner that searches full "
        "git history for leaked credentials, including credentials committed and later deleted.")
    res("Gitleaks", "github.com/gitleaks/gitleaks — Lightweight secrets scanner. Runs as a "
        "pre-commit hook and CI gate. Scans diffs rather than full history, making it fast enough "
        "for every PR.")
    add(SP(4))
    SS("Security Testing & Tooling — Months 3.5–5.25")
    step("01", "LEARN + LABS: Burp Suite Mastery", "Weeks 15\u201316", [
        "Proxy, Repeater, and Intruder are already yours from Phase II \u2014 review those notes; no need to re-read the docs",
        "The two Community-edition tools you haven't used: <a href=\"https://portswigger.net/burp/documentation/desktop/tools/decoder\" color=\"#3A7AB8\">Decoder</a> (encode/decode/hash inline) and <a href=\"https://portswigger.net/burp/documentation/desktop/tools/comparer\" color=\"#3A7AB8\">Comparer</a> (visual diff of two messages)",
        "<b>Decoder:</b> <a href=\"https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding\" color=\"#3A7AB8\">SQL injection with filter bypass via XML encoding</a> (<a href=\"https://portswigger.net/web-security/all-labs#essential-skills\" color=\"#3A7AB8\">Essential skills</a>) \u2014 encode the payload as XML/HTML entities to bypass the WAF",
        "<b>Comparer:</b> <a href=\"https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses\" color=\"#3A7AB8\">Username enumeration via different responses</a> (<a href=\"https://portswigger.net/web-security/all-labs#authentication\" color=\"#3A7AB8\">Authentication</a>) \u2014 spot the one login response that differs",
        "<b>Both:</b> <a href=\"https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses\" color=\"#3A7AB8\">Blind SQL injection with conditional responses</a> (<a href=\"https://portswigger.net/web-security/all-labs#sql-injection\" color=\"#3A7AB8\">SQL injection</a>) \u2014 read the admin password one true/false answer at a time",
        "<b>By end of Week 16:</b> fluent with Decoder and Comparer, and comfortable with Proxy match-and-replace and Repeater tab groups",
    ])
    step("02", "PROJECT: Burp Suite Certified Practitioner Prep", "Weeks 15\u201317", [
        "The <a href=\"https://portswigger.net/web-security/certification\" color=\"#3A7AB8\">BSCP exam</a> is highly respected in the AppSec "
        "community \u2014 practical, hands-on, and not multiple-choice",
        "<b>Burp Suite Professional required:</b> the exam, its practice exams, the targeted Scanner, and Burp Collaborator (for out-of-band work) all need <a href=\"https://portswigger.net/burp/pro\" color=\"#3A7AB8\">Burp Suite Professional</a> (~$499/yr) \u2014 Community Edition is not sufficient. If you followed the plan you bought Pro at the start of Phase III, where the first Collaborator labs appear; it is required continuously from there through this exam. The exam itself is ~$99 per attempt.",
        "The practice exam format (identify two vulnerabilities per app, chain them into account "
        "takeover) is the closest simulation of real AppSec work available",
        "Pass the <a href=\"https://portswigger.net/web-security/certification/practice-exam\" color=\"#3A7AB8\">BSCP practice exam</a> in under 2 hours \u2014 and do it more than once \u2014 before booking the real exam. It mirrors the real format exactly, so consistently passing it under time is the strongest signal you are ready",
        "A passed BSCP on the resume is a much stronger AppSec signal than Sec+ alone",
    ])
    step("03", "DOCUMENT: Save Exam-Ready Proof-of-Concept Exploits", "Throughout Weeks 15\u201320", [
        "PortSwigger publishes full PoC / solution code for every lab. As you clear each practitioner lab this phase, save its working exploit into one personal, searchable notes file \u2014 the BSCP is open to your own notes (see <a href=\"https://portswigger.net/web-security/certification/how-to-prepare\" color=\"#3A7AB8\">PortSwigger\u2019s prep guidance</a>).",
        "Digital notes are ideal \u2014 the exam is fully open-book (your own notes, the web, third-party tools, and Burp extensions are all allowed) and you sit it in Chrome alongside Burp, so keep everything in one searchable file (Markdown or plain text) or a notes app rather than on paper. Make payloads copy-paste-ready, and pre-load your payload lists and useful extensions into Burp before you start.",
        "Pre-adapt the high-value PoCs for exam conditions: turn XSS print()/alert() payloads into cookie-stealers, parameterize your SQLi and SSRF payloads, and keep Collaborator / OOB templates ready to paste.",
        "Organize them by vulnerability class so you can pull the right template in seconds under exam time pressure",
    ])
    step("04", "LEARN + LABS: Semgrep & Bandit — SAST Tooling", "Weeks 16\u201317", [
        "Install the <a href=\"https://semgrep.dev/\" color=\"#3A7AB8\">Semgrep</a> CLI. <a href=\"https://semgrep.dev/docs/getting-started/quickstart-ce\" color=\"#3A7AB8\">Run the default Python ruleset</a> against a sample Python application "
        "(OWASP Juice Shop or WebGoat codebase)",
        "<a href=\"https://semgrep.dev/docs/semgrep-code/findings\" color=\"#3A7AB8\">Triage the results</a>: distinguish true positives from false positives",
        "<a href=\"https://semgrep.dev/docs/writing-rules/overview\" color=\"#3A7AB8\">Write one custom Semgrep rule</a> targeting a Python injection pattern — for example, an "
        "endpoint passing request parameters directly to a database query",
        "<a href=\"https://semgrep.dev/docs/semgrep-ci/sample-ci-configs\" color=\"#3A7AB8\">Integrate Semgrep into a GitHub Actions workflow</a> (sample repo is fine)",
        "<a href=\"https://github.com/PyCQA/bandit\" color=\"#3A7AB8\">Bandit</a>: install bandit with pip. <a href=\"https://bandit.readthedocs.io/en/latest/\" color=\"#3A7AB8\">Run against a sample Python project</a> and against "
        "some code in old projects. Look for: B101 (assert usage), B102 (exec usage), "
        "B105/B106/B107 (hardcoded password), B201 (Flask debug mode), B301 (pickle), B501–B509 "
        "(SSL/TLS issues). The finding IDs become vocabulary you use in code review conversations",
        "Run both tools against the same Python codebase and compare results. Bandit catches "
        "Python-specific antipatterns that Semgrep misses without custom rules. Semgrep catches "
        "logic-level patterns that Bandit’s fixed ruleset cannot express.",
    ])
    step("05", "LEARN: Secrets Scanning — TruffleHog & Gitleaks", "Week 17", [
        "Hardcoded secrets (API keys, passwords, tokens committed to repos) are one of the most "
        "common real-world breach vectors. The Uber 2016, LastPass 2022, and Toyota 2023 breaches "
        "all involved exposed credentials",
        "<a href=\"https://github.com/trufflesecurity/trufflehog\" color=\"#3A7AB8\">TruffleHog</a>: install and run against a sample repo. Uses entropy analysis to catch secrets "
        "that regex misses. Can scan full git history, not just current code",
        "<a href=\"https://github.com/gitleaks/gitleaks\" color=\"#3A7AB8\">Gitleaks</a>: install and run as a CI <a href=\"https://pre-commit.com/\" color=\"#3A7AB8\">pre-commit hook</a>. Lightweight and fast, well-suited for "
        "blocking commits before they land",
        "Integrate both into a <a href=\"https://docs.github.com/en/actions\" color=\"#3A7AB8\">GitHub Actions workflow</a>: Gitleaks on every pull request (scanning "
        "only the changed lines), TruffleHog for scheduled full-history scans",
        "<b>In code review:</b> you are now looking for hardcoded strings that look like keys, passwords, "
        "or tokens — in source code, config files, Dockerfiles, and environment variable defaults",
        "<b>Full notes + note cards:</b> When to use TruffleHog vs Gitleaks, what a false positive looks "
        "like, what to do when a live secret is found (rotation procedure, not just deletion)",
    ])
    step("06", "LEARN: OWASP ZAP — DAST Basics", "Week 17", [
        "Run <a href=\"https://www.zaproxy.org/\" color=\"#3A7AB8\">OWASP ZAP</a> against DVWA or WebGoat running locally",
        "Understand the difference between DAST (testing a running application) and SAST (testing "
        "source code)",
        "<b>Triage ZAP results:</b> true positive, false positive, needs investigation",
    ])
    step("07", "LABS: Out-of-Band (OOB) Exploitation with Burp Collaborator", "Weeks 17\u201318", [
        "<b>Requires Burp Suite Professional</b> \u2014 Burp Collaborator is Pro-only, and nearly every blind / out-of-band variant on the BSCP routes through it. You first used Collaborator in Phase III (Pro from the start); this step is a focused OOB drill to lock in exam fluency \u2014 re-confirm each one fast.",
        "<b>Blind SQL injection:</b> re-read your notes on <a href=\"https://portswigger.net/web-security/sql-injection/blind\" color=\"#3A7AB8\">blind SQL injection</a> (the learning path stays linked), then the out-of-band <a href=\"https://portswigger.net/web-security/all-labs#sql-injection\" color=\"#3A7AB8\">labs</a> \u2014 <i>Blind SQL injection with out-of-band interaction</i> and <i>Blind SQL injection with out-of-band data exfiltration</i> (practitioner)",
        "<b>Blind XXE:</b> re-read your notes on <a href=\"https://portswigger.net/web-security/xxe/blind\" color=\"#3A7AB8\">blind XXE</a> (the learning path stays linked), then the out-of-band <a href=\"https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection\" color=\"#3A7AB8\">labs</a> \u2014 <i>Blind XXE with out-of-band interaction</i> and <i>Exploiting blind XXE to exfiltrate data using a malicious external DTD</i>",
        "<b>Blind OS command injection:</b> from the <a href=\"https://portswigger.net/web-security/os-command-injection\" color=\"#3A7AB8\">OS command injection</a> learning path, the out-of-band <a href=\"https://portswigger.net/web-security/all-labs#os-command-injection\" color=\"#3A7AB8\">labs</a> \u2014 <i>Blind OS command injection with out-of-band interaction</i> and <i>... with out-of-band data exfiltration</i>",
        "Carry the same Collaborator technique into blind SSTI detection and any asynchronous sink \u2014 fire a DNS/HTTP callback to confirm the bug, then exfiltrate data through it",
        "<b>For each lab:</b> exploit it, then save the Collaborator payload and working exploit into your exam notes",
    ])
    step("08", "READ + LABS: Remaining BSCP Topics", "Weeks 17\u201319", [
        "<b>Topics the exam can draw from that earlier phases skipped \u2014 close them before sitting the exam.</b> For each: read the learning path, then do the apprentice and practitioner labs.",
        "<a href=\"https://portswigger.net/web-security/request-smuggling\" color=\"#3A7AB8\">HTTP request smuggling</a> learning path, then the <a href=\"https://portswigger.net/web-security/all-labs#http-request-smuggling\" color=\"#3A7AB8\">labs</a> \u2014 <i>basic CL.TE</i> and <i>basic TE.CL</i>, <i>obfuscating the TE header</i>, and <i>Exploiting HTTP request smuggling to capture other users\u2019 requests</i> (a BSCP favorite)",
        "<a href=\"https://portswigger.net/web-security/host-header\" color=\"#3A7AB8\">HTTP Host header attacks</a> learning path, then the <a href=\"https://portswigger.net/web-security/all-labs#http-host-header-attacks\" color=\"#3A7AB8\">labs</a> \u2014 <i>basic password reset poisoning</i>, <i>Host header authentication bypass</i>, <i>web cache poisoning via ambiguous requests</i>, and <i>routing-based SSRF</i>",
        "<a href=\"https://portswigger.net/web-security/web-cache-poisoning\" color=\"#3A7AB8\">Web cache poisoning</a> learning path, then the <a href=\"https://portswigger.net/web-security/all-labs#web-cache-poisoning\" color=\"#3A7AB8\">labs</a> \u2014 <i>unkeyed header</i>, <i>unkeyed cookie</i>, <i>multiple headers</i>, and <i>targeted poisoning using an unknown header</i>",
    ])
    step("09", "LEARN + LABS: Targeted Scanning & Content Discovery", "Weeks 18\u201319", [
        "<b>Requires Burp Suite Professional</b> (the Scanner and Engagement tools are Pro-only). The exam is time-boxed, so you scan smart, not broad \u2014 this is an explicit BSCP skill.",
        "Read <a href=\"https://portswigger.net/web-security/essential-skills/using-burp-scanner-during-manual-testing\" color=\"#3A7AB8\">using Burp Scanner during manual testing</a>, then the <a href=\"https://portswigger.net/web-security/all-labs#essential-skills\" color=\"#3A7AB8\">labs</a> \u2014 <i>Discovering vulnerabilities quickly with targeted scanning</i> and <i>Scanning non-standard data structures</i>. Right-click a single request \u2192 <i>Do active scan</i> to audit just that request in seconds instead of crawling the whole site.",
        "<b>Content discovery:</b> use Burp\u2019s <a href=\"https://portswigger.net/burp/documentation/desktop/tools/engagement-tools\" color=\"#3A7AB8\">Engagement tools</a> \u2192 <i>Discover content</i> to enumerate hidden directories, files, and parameters (for example a hidden /admin) \u2014 a recurring first move on exam apps. Practice it on labs you have already solved.",
        "<b>Build the habit:</b> hand every new request to the Scanner while you test manually, and run content discovery before assuming an app\u2019s surface is fully mapped",
    ])
    step("10", "DRILL: PortSwigger\u2019s Mandatory Reinforcement Labs", "Weeks 19\u201320", [
        "Beyond one practitioner lab per topic, PortSwigger requires 8 specific skill-reinforcement labs before the exam. Make sure each is solid \u2014 several are already covered in earlier steps; this is the consolidated checklist.",
        "<b>XSS:</b> <i>Exploiting cross-site scripting to steal cookies</i> \u2014 from <a href=\"https://portswigger.net/web-security/cross-site-scripting\" color=\"#3A7AB8\">Cross-site scripting</a>, the <a href=\"https://portswigger.net/web-security/all-labs#cross-site-scripting\" color=\"#3A7AB8\">labs</a>; exfiltrate a real session cookie (not just an alert()), which is what the exam rewards (reinforces step 03)",
        "<b>Authentication:</b> <i>Brute-forcing a stay-logged-in cookie</i> \u2014 from <a href=\"https://portswigger.net/web-security/authentication\" color=\"#3A7AB8\">Authentication</a>, the <a href=\"https://portswigger.net/web-security/all-labs#authentication\" color=\"#3A7AB8\">labs</a>; decode the cookie in Decoder, then brute-force it with Intruder",
        "<b>SSRF:</b> <i>SSRF with blacklist-based input filter</i> \u2014 from <a href=\"https://portswigger.net/web-security/ssrf\" color=\"#3A7AB8\">SSRF</a>, the <a href=\"https://portswigger.net/web-security/all-labs#server-side-request-forgery-ssrf\" color=\"#3A7AB8\">labs</a>; the filter-bypass variant skipped in Phase III",
        "Already done elsewhere \u2014 re-confirm you can solve each cold: <i>Forced OAuth profile linking</i> (Phase II), <i>Exploiting HTTP request smuggling to capture other users\u2019 requests</i> (step 08), <i>Blind SQL injection with out-of-band data exfiltration</i> (step 07), <i>SQL injection with filter bypass via XML encoding</i> (step 01), and <i>Discovering vulnerabilities quickly with targeted scanning</i> (step 09)",
        "Save the working PoC for each into your exam notes \u2014 you may refer to your own notes during the exam",
    ])
    step("11", "DRILL: Fluency \u2014 Re-Solve Cold", "Week 20", [
        "For each major class, take one practitioner lab you have already solved and re-solve it cold \u2014 no notes, no solution \u2014 in 15 minutes or less.",
        "Work through roughly 20 labs this way (about one per class). If a lab runs past 15 minutes or you reach for your notes, that class is not yet exam-fluent \u2014 drill it again.",
        "This is the gap between having seen a vulnerability and being able to exploit it under time pressure with no hints \u2014 which is exactly what the exam tests",
    ])
    step("12", "DRILL: Mystery Labs \u2014 Cold Recognition", "Weeks 20\u201321", [
        "The exam gives you no vulnerability hints \u2014 you must recognize the class from behavior alone. The <a href=\"https://portswigger.net/web-security/mystery-lab-challenge\" color=\"#3A7AB8\">mystery lab challenge</a> spins up a random lab with its title and description hidden, the closest practice for that.",
        "Solve at least 5 mystery labs cold \u2014 no hints, working only from recon \u2014 before booking the exam. Time each one; the goal is fast, confident classification.",
        "If a class keeps stumping you, go back to that topic\u2019s labs and notes, then return to the mystery challenge",
    ])
    step("13", "DRILL: Exam Stamina \u2014 Six Labs in One Block", "Week 20", [
        "The real exam is a single continuous 4-hour session \u2014 two applications, three stages each, six flags, no partial credit. Rehearse that endurance before you book it.",
        "Take six practitioner labs you have not memorized and solve them back-to-back in one timed 4-hour block \u2014 own notes only, Burp Pro, Collaborator live, no long breaks.",
        "Track time per lab and practice triage: if one runs past budget, bank partial progress, move on, and circle back \u2014 the time management is as much the test as the exploitation",
    ])
    step("14", "EXAM: Burp Suite Certified Practitioner", "Weeks 20\u201321", [
        "Take the <a href=\"https://portswigger.net/web-security/certification\" color=\"#3A7AB8\">BSCP exam</a>. The exam consists of two applications, each requiring two "
        "vulnerabilities to be identified and chained into an account takeover. 4 hours.",
        "If unsuccessful on the first attempt, review the topics where the attempt failed and "
        "retake. There is no cap on attempts \u2014 you can retake as many times as needed (each attempt costs $99).",
    ])
    step("15", "APPLY: Begin Job Applications", "Month 4 onward", [
        "With Phases I\u2013III complete, two or more published writeups, and visible PortSwigger "
        "progress, begin applying now \u2014 do not wait for curriculum completion",
        "Target AI-native startups, security-conscious tech companies, and local Philadelphia "
        "legal-AI and healthtech firms first \u2014 they hire locally and value a full-stack background",
        "Job applications run in parallel with the remaining phases and ramp into a main push around "
        "Month 7, once Security+ is on your resume",
        "See \u201c<a href=\"#application_strategy\" color=\"#3A7AB8\">Application Strategy</a>\u201d in Phase VIII for the full targeting, profile, and "
        "framing playbook",
    ])
    step("16", "LEARN: Snyk — Dependency Scanning", "Week 21", [
        "Install and authenticate the <a href=\"https://docs.snyk.io/developer-tools/snyk-cli/getting-started-with-the-snyk-cli\" color=\"#3A7AB8\">Snyk CLI</a>, then run <i>snyk test</i> in a sample Python project with known-vulnerable dependencies (for example an outdated requirements.txt) to produce a software-composition report listing each flagged package, its CVE, and the safe upgrade",
        "Understand what SCA (software composition analysis) is and what it does not catch",
        "Log4Shell was a dependency vulnerability, not an application vulnerability — SCA catches "
        "these",
        "Wire <i>snyk test</i> into CI alongside Semgrep and Gitleaks so newly disclosed dependency CVEs fail the build — the remediation is almost always a version bump",
    ])
    step("17", "PROJECT: Full Security Assessment of Juice Shop", "Week 21", [
        "Conduct a full security assessment of <a href=\"https://owasp.org/www-project-juice-shop/\" color=\"#3A7AB8\">OWASP Juice Shop</a> using: Burp Suite (manual), ZAP "
        "(DAST), Semgrep + Bandit (SAST), Snyk (dependencies), TruffleHog/Gitleaks (secrets)",
        "Work through it systematically using the official companion guide <a href=\"https://pwning.owasp-juice.shop\" color=\"#3A7AB8\">Pwning OWASP Juice Shop</a>, which groups every challenge by vulnerability class \u2014 injection, broken authentication, XSS, broken access control, and more \u2014 so you can map each finding to an OWASP category; its appendix has full step-by-step solutions if you get stuck",
        "Reuse the systematic methodology and the writeup and report format you built in your Phase III vulnerability-class writeups \u2014 this project is where the full workflow comes together: recon, tooling, manual exploitation, false-positive triage, and professional reporting",
        "Produce a written vulnerability report: executive summary, findings table (vuln, "
        "severity, CVSS, evidence, recommendation), detailed finding writeups",
        "Export the finished report as a polished, shareable standalone PDF \u2014 the document "
        "you attach to applications and hand to interviewers",
        "This is the most important portfolio artifact in the plan — it demonstrates the complete "
        "AppSec workflow from tool setup to professional reporting",
    ])
    SS("Concepts Mastered")
    concept("Burp Suite as an extension of manual thinking",
            "Burp Suite intercepts and replays HTTP traffic. It does not find vulnerabilities — it "
            "makes manual exploitation efficient. Understanding of what to look for drives the "
            "tool, not the reverse.")
    concept("SAST vs. DAST vs. SCA vs. Secrets Scanning",
            "Four distinct scanning approaches that catch different vulnerability classes. SAST "
            "reads code, misses runtime behavior. DAST tests a running app, misses code paths not "
            "exercised. SCA finds known CVEs in dependencies. Secrets scanning finds exposed "
            "credentials in code and history. A real AppSec program uses all four — plus "
            "Python-specific tools like Bandit for Python shops.")
    concept("False positive triage",
            "Automated tools have noise. Distinguishing real findings from false positives without "
            "dismissing everything is where security judgment matters more than tool knowledge.")
    concept("Professional vulnerability reporting",
            "Severity rating (CVSS), evidence documentation, clear remediation guidance. The "
            "output of AppSec work is a finding that a developer can act on — not just a list of "
            "things that are broken.")
    concept("Secrets management",
            "Hardcoded credentials are a separate vulnerability class from application logic flaws. "
            "The fix is not deletion from current code — it is rotation of the exposed credential "
            "plus integration of a secret manager (HashiCorp Vault, AWS Secrets Manager) and "
            "pre-commit scanning to prevent recurrence.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("Burp Suite in daily work",
            "Every manual pentest engagement uses Burp Suite. Every time you need to understand "
            "what a web application is actually sending and receiving, it is open. The AppSec "
            "engineer’s equivalent of a developer’s debugger.")
    concept("Semgrep in CI/CD",
            "Integrating Semgrep into a company’s CI/CD pipeline, writing rules for "
            "company-specific vulnerability patterns, and triaging results is a common AppSec "
            "responsibility. The custom rule you built is the portfolio demonstration.")
    concept("Secrets scanning in CI/CD",
            "Gitleaks runs as a pre-commit hook and a CI gate. TruffleHog runs on a schedule "
            "against full git history. When a developer accidentally commits an API key, you have "
            "a runbook: alert the developer, rotate the credential immediately (assume it is "
            "already compromised), add the pattern to the blocklist. This is day-one operational "
            "work at most companies.")
    concept("Assessment reports",
            "Every engagement produces a report. The format you learned in the Juice Shop "
            "assessment is the format used in production. Clear findings, actionable remediations, "
            "evidence-backed.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE V — CLOUD SECURITY FUNDAMENTALS
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("V", "Cloud Security Fundamentals", "Months 5.25–5.75"))
    add(SP(10))
    add(P("Modern AppSec work happens in the cloud. S3 misconfiguration and IAM over-permissioning "
          "are among the most common real-world vulnerabilities found by security researchers, and "
          "credible threat modeling requires understanding the cloud attack surface an application "
          "runs on. This phase covers the AppSec-relevant subset — not Terraform or multi-cloud "
          "architecture, but enough to identify misconfigurations in code and architecture "
          "reviews, understand SSRF chains that target cloud metadata, and discuss findings with "
          "infrastructure teams.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("AWS Security CTF: Attacker Path", "flaws.cloud — Six levels covering real-world AWS "
        "misconfigurations: S3 bucket exposure, credential leakage, IAM misuse, and SSRF via the "
        "EC2 metadata service. Each level explains the vulnerability and its fix.")
    res("AWS Security CTF: Attacker & Defender", "flaws2.cloud — Companion to flaws.cloud with two "
        "separate paths: attacker path (exploit cloud misconfigurations) and defender path "
        "(identify and fix the same misconfigurations).")
    res("AWS Shared Responsibility Model", "aws.amazon.com/compliance/shared-responsibility-model "
        "— Official AWS documentation. Defines what AWS secures (infrastructure) versus what the "
        "customer secures (IAM, S3 policies, application code, data encryption).")
    res("AWS IAM Documentation", "<a href=\"https://docs.aws.amazon.com/iam/\" color=\"#3A7AB8\">docs.aws.amazon.com/iam</a> — Official AWS documentation. The IAM "
        "concepts section covers users, roles, groups, policies, and the principle of least "
        "privilege.")
    res("FreeCodeCamp Cloud Security Fundamentals in AWS", "freecodecamp.org — Beginner-friendly "
        "guide covering IAM users and policies, S3 bucket configurations, MFA, and the AWS Shared "
        "Responsibility Model with hands-on examples.")
    add(SP(4))
    SS("Cloud Security Fundamentals — Months 5.25–5.75")
    step("01", "READ: AWS Foundations: Shared Responsibility & IAM", "Week 22", [
        "Read the <a href=\"https://aws.amazon.com/compliance/shared-responsibility-model/\" color=\"#3A7AB8\">AWS Shared Responsibility Model</a> page completely. Write a one-paragraph summary "
        "in your own words: what AWS is responsible for, what you are responsible for, and what "
        "the boundary looks like for a web application running on EC2 behind an S3 bucket",
        "Read the IAM concepts in the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/\" color=\"#3A7AB8\">AWS IAM documentation</a>: what a user is, what a role is, what "
        "a policy is, how they attach, what least privilege means in practice",
        "Read the <a href=\"https://www.freecodecamp.org/news/learn-cloud-security-fundamentals-in-aws-a-guide-for-beginners/\" color=\"#3A7AB8\">FreeCodeCamp Cloud Security Fundamentals in AWS</a> guide — beginner-friendly, "
        "hands-on, covers IAM and S3 configuration with real console examples",
        "<b>Full notes + note cards:</b> AWS Shared Responsibility boundary; IAM user vs. role vs. group; "
        "what a policy document looks like (JSON structure, Effect/Action/Resource); what least "
        "privilege means and why wildcard permissions (s3:*) are a finding",
    ])
    step("02", "LABS: flaws.cloud — Levels 1–6", "Week 22–23", [
        "Create a free AWS account if you do not have one. The CTF runs against real AWS "
        "infrastructure — you need the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html\" color=\"#3A7AB8\">AWS CLI installed and configured</a> with a free-tier account",
        "Complete all six levels. Exploit each level fully before reading the solution",
        "<b>For each level:</b> write standard documentation — what the misconfiguration was, how an "
        "attacker exploits it, how to fix it, and what to look for in a code or configuration "
        "review to catch it",
    ])
    step("03", "LABS: flaws2.cloud — Attacker & Defender Paths", "Week 23", [
        "<b>Two distinct paths:</b> attacker (find and exploit misconfigurations) and defender (harden "
        "the same environment).",
        "Complete both paths. The defender path is the AppSec-relevant half — it teaches you what "
        "a correctly configured environment looks like, not just what a broken one looks like",
        "<b>Key concepts reinforced:</b> IAM role scoping, S3 bucket policy syntax, EC2 instance metadata "
        "v2 (IMDSv2) — the hardened version that prevents credential theft via SSRF",
    ])
    SS("Concepts Mastered")
    concept("AWS Shared Responsibility Model",
            "AWS secures the physical infrastructure. You secure what runs on it: IAM "
            "configurations, S3 policies, application code, data encryption. Misunderstanding this "
            "boundary is the root cause of most cloud breaches.")
    concept("IAM — Identity and Access Management",
            "Users, roles, groups, and policies. A role is what an AWS service or EC2 instance "
            "assumes to perform actions. A policy is a JSON document defining what actions are "
            "allowed or denied on which resources. Least privilege means a role should have "
            "exactly the permissions it needs and nothing more. Over-permissioned roles are the "
            "most common IAM finding.")
    concept("S3 bucket misconfiguration",
            "S3 buckets store data. Public read access means anyone on the internet can read the "
            "contents. Authenticated AWS user access means all 300M+ AWS account holders can read "
            "it. Both are common misconfigurations. Bucket policies, ACLs, and Block Public Access "
            "settings all interact — understanding which one controls what is the skill.")
    concept("EC2 instance metadata service (IMDS)",
            "169.254.169.254 is accessible from within an EC2 instance and returns IAM "
            "credentials, instance ID, and configuration. SSRF against this endpoint gives an "
            "attacker the instance’s IAM credentials. IMDSv2 requires a token header that prevents "
            "simple SSRF exploitation. Whether IMDSv2 is enforced is a standard AppSec checklist "
            "item.")
    concept("Credential exposure in git history",
            "AWS keys committed to a git repository — even if deleted in a later commit — are "
            "permanently visible in history. TruffleHog scans history. The fix is to rotate the exposed credential, not just delete it from current code, plus "
            "pre-commit scanning to prevent recurrence.")
    concept("Cloud security code review",
            "Reading an IAM policy JSON, an S3 bucket policy, or a Lambda function configuration "
            "and identifying the security problem. This is the AppSec-specific cloud skill — not "
            "writing infrastructure, but auditing it.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("IAM review in architecture review",
            "When a team presents a new service design, you ask: what IAM role does this service "
            "run as? What permissions does that role have? Could an attacker compromise this "
            "service and use its IAM role to access something they should not? These questions "
            "catch privilege escalation paths before code is written.")
    concept("SSRF → metadata chain in code review",
            "When you see an endpoint that accepts a URL and fetches it server-side, your first "
            "question is now: can this reach 169.254.169.254? Is IMDSv2 enforced on the EC2 "
            "instances this service runs on? Is there a URL allowlist? The AWS Security CTF Level "
            "5 scenario is the exact attack chain you are looking for.")
    concept("S3 policy in configuration review",
            "When reviewing a deployment configuration or an IaC pull request, you check: is Block "
            "Public Access enabled at the bucket level? Are there wildcard permissions? Are access "
            "logs enabled on buckets containing sensitive data? These are 5-minute checks that "
            "catch high-severity findings.")
    concept("Credentials in code review",
            "When reviewing any code that configures AWS clients, check: are credentials "
            "hardcoded? Are they pulled from environment variables (better but still risky) or "
            "from a secrets manager or IAM role (correct)?")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE VI — SECURE CODE REVIEW & THREAT MODELING
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("VI", "Secure Code Review & Threat Modeling", "Months 5.75–6.5"))
    add(SP(10))
    add(P("Phase V builds the two highest-leverage AppSec skills — the ones that appear earliest "
          "in a job and distinguish engineers from analysts. Secure code review is the daily work "
          "of most AppSec engineers at software companies. Threat modeling is how AppSec influence "
          "scales beyond individual code reviews to affect system design. The developer "
          "perspective that threat modeling requires — understanding how systems are built and "
          "where trust boundaries exist — is built through the pre-study and Phases I–IV before "
          "this phase begins. OWASP ASVS is introduced here as the verification standard that "
          "gives code review a systematic checklist — turning ad-hoc review into structured, "
          "repeatable methodology.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("OWASP Code Review Guide v2.0", "owasp.org/www-project-code-review-guide — The methodology "
        "reference for secure code review.")
    res("OWASP Application Security Verification Standard (ASVS) v5.0.0",
        "owasp.org/www-project-application-security-verification-standard — Approximately 350 "
        "testable security requirements across 17 chapters covering authentication, access "
        "control, input validation, cryptography, API security, and configuration. Level 1 is "
        "automatable; Level 2 requires manual testing.")
    res("“<i>Threat Modeling: Designing for Security</i>”", "Adam Shostack, Wiley, 2014 (wiley.com) — The "
        "standard text on threat modeling. Ch. 1–5 cover the STRIDE methodology and data flow "
        "diagrams.")
    res("GitHub Security Lab", "securitylab.github.com — Published CVE research on real "
        "open-source projects. Covers vulnerability discovery, exploitation mechanics, and "
        "coordinated disclosure.")
    res("OWASP Threat Dragon", "owasp.org/www-project-threat-dragon — Threat modeling tool. Used "
        "for the threat modeling project in this phase.")
    add(SP(4))
    SS("Secure Code Review & Threat Modeling — Months 5.75–6.5")
    step("01", "READ + PRACTICE: Secure Code Review Methodology", "Weeks 24–25", [
        "Read the <a href=\"https://owasp.org/www-project-code-review-guide/\" color=\"#3A7AB8\">OWASP Code Review Guide</a> Ch. 1–4 (methodology, code review techniques, "
        "vulnerability-specific review guidance)",
        "Conduct a code review of a real open-source Python web application (Django, Flask, or FastAPI) from GitHub — not "
        "WebGoat, but a real project at real scale",
        "<b>Apply the systematic methodology:</b> trace user input, verify authentication, check "
        "authorization, audit crypto, check dependencies",
    ])
    step("02", "STUDY: OWASP ASVS — Verification Standard", "Week 25", [
        "Read the <a href=\"https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf\" color=\"#3A7AB8\">ASVS v5.0.0 Level 1 and Level 2 requirements</a>. Do not try to memorize — learn the "
        "structure and the categories",
        "Map each ASVS chapter to the vulnerability classes studied in this plan — input validation and output encoding, authentication, access control, and cryptography each get their own chapter, so you can pin any finding to a specific numbered requirement",
        "Build a lightweight personal ASVS checklist: 20–30 of the highest-signal Level 2 "
        "requirements you would check first in any code review",
        "This checklist becomes a portfolio artifact and an interview talking point: most "
        "entry-level AppSec candidates have not heard of ASVS",
    ])
    step("03", "READ + PROJECT: Threat Modeling", "Weeks 25–26", [
        "Read “<i>Threat Modeling: Designing for Security</i>” Ch. 1–5",
        "Build a complete threat model for the API built during pre-study. A system built "
        "from scratch end-to-end is the right target: every layer is known, every trust boundary "
        "can be reasoned about.",
        "Use <a href=\"https://owasp.org/www-project-threat-dragon/\" color=\"#3A7AB8\">OWASP Threat Dragon</a> for the data flow diagram. Apply STRIDE to each component",
        "<b>Produce a threat model document:</b> DFD, trust boundaries, threat enumeration, risk rating, "
        "mitigations",
    ])
    step("04", "PRACTICE: Code Review Under Time Pressure", "Week 26", [
        "AppSec interview code review exercises are time-boxed — typically 30–45 minutes to review "
        "a snippet and explain findings verbally",
        "Use <a href=\"https://securitylab.github.com/\" color=\"#3A7AB8\">GitHub Security Lab</a>’s published CVE <a href=\"https://securitylab.github.com/advisories/\" color=\"#3A7AB8\">writeups</a> as answer keys: read the vulnerable code "
        "before the writeup, try to identify the vulnerability, then compare",
        "Do five of these across different vulnerability classes",
        "<b>Target:</b> 30 minutes from cold code to written vulnerability identification",
    ])
    SS("Projects & Writings — Secure Code Review & Threat Modeling")
    add(P("<b>Project: Open-Source Code Review</b>", S["bul"]))
    add(P("Documented security review of a real open-source Python application. Findings in "
          "standard format, pushed to GitHub. Includes scope, methodology, findings, and "
          "remediation recommendations.", S["bulsm"]))
    add(P("<b>Project: Threat Model Document</b>", S["bul"]))
    add(P("Full STRIDE threat model of a real-world system architecture. DFD, trust boundaries, "
          "threat enumeration, risk ratings, mitigations. Pushed to GitHub. An unusual portfolio "
          "artifact — most AppSec candidates have lab writeups but not threat models.", S["bulsm"]))
    add(P("<b>Writing: ‘Threat Modeling the Billing System I Built’ (1,000–1,500 words)</b>",
          S["bul"]))
    add(P("Use your ActiveCampaign billing microservice as the subject. Walk through what a threat "
          "model of that system would have looked like, what STRIDE would have identified, and how "
          "the architecture would have been different had AppSec been involved in the design. The "
          "most unique piece in the portfolio — no other candidate has this specific experience.",
          S["bulsm"]))
    add(SP(4))
    SS("Concepts Mastered")
    concept("Secure code review as methodology",
            "Not reading code and hoping to notice something bad — systematic input tracing, "
            "authentication verification, authorization checking, cryptography auditing. "
            "Replicable and teachable.")
    concept("OWASP ASVS as a verification framework",
            "~350 testable security requirements organized by domain. Level 1 covers basics "
            "automatable by scanners. Level 2 requires manual testing and judgment. Using ASVS "
            "during code review means you can say ‘this fails ASVS V2.1.1’ rather than ‘this seems "
            "wrong’ — a significant credibility upgrade in professional settings.")
    concept("STRIDE threat modeling",
            "Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, "
            "Elevation of Privilege. A threat category for every component of a data flow "
            "diagram.")
    concept("Trust boundaries",
            "The lines in a DFD where data crosses from less-trusted to more-trusted context. "
            "Every trust boundary is a potential vulnerability surface.")
    concept("Time-pressured code review",
            "The AppSec interview format. Cold code, 30–45 minutes, verbal explanation of "
            "findings. Practice makes this feel like code review, not an exam.")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("Code review in practice",
            "When a developer asks you to review a PR, you apply the methodology: trace inputs, "
            "check auth, check authz, check crypto, check dependencies. 20 minutes when "
            "systematic, hours when ad-hoc.")
    concept("Threat modeling in architecture review",
            "When a team presents a new microservice design, you build a DFD on the whiteboard, "
            "identify trust boundaries, and run STRIDE. One threat model at design time prevents "
            "dozens of vulnerability findings after code is written.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE VII — COMPTIA SECURITY+
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("VII", "CompTIA Security+ Certification", "Months 6.75–7.25"))
    add(SP(10))
    add(P("CompTIA Security+ is ATS bait — that is the honest framing. It is required or preferred "
          "in a growing number of AppSec job postings, especially at enterprise companies and in "
          "regulated industries. It does not demonstrate AppSec competence to a human reviewer. "
          "The portfolio does that. But it gets your resume past automated filters at companies "
          "that screen for it, and it is achievable in 3–4 weeks with the foundational knowledge "
          "built throughout this plan.", S["body"]))
    add(SP(2))
    SS("Learning Resources")
    res("CompTIA Security+ Get Certified Get Ahead: SY0-701 Study Guide", "Joe Shelley and Darril "
        "Gibson, Certification Experts LLC, 2023 (certificationexpertsllc.com) — 674 pages "
        "covering all SY0-701 exam objectives across eleven chapters with real-world examples and "
        "exam topic review sections.")
    res("Professor Messer Practice Exams", "professormesser.com — Paid practice exams for the "
        "Security+ SY0-701 exam. Same format and structure as the actual exam.")
    add(SP(4))
    SS("CompTIA Security+ Certification Schedule")
    step("01", "READ: Study Guide", "Weeks 27–28", [
        "Read CompTIA Security+ Get Certified Get Ahead: SY0-701 Study Guide cover to cover. The "
        "exam has five domains: General Security Concepts, Threats/Vulnerabilities/Mitigations, "
        "Security Architecture, Security Operations, and Security Program Management & Oversight",
        "Most technical content from the first three domains will be review from earlier phases. "
        "Focus study time on governance, compliance, and program management domains — these are "
        "the least familiar material",
        "<b>Full notes + note cards:</b> One card per domain. Front: domain name. Back: the key concepts "
        "from that domain most likely to appear on the exam",
    ])
    step("02", "PRACTICE: Practice Exams", "Week 28–29", [
        "Take a full <a href=\"https://www.professormesser.com/sy0-701-certification-course/\" color=\"#3A7AB8\">Professor Messer</a> practice exam cold. Score it and identify weak domains",
        "Study weak domains specifically from the study guide. Retake. Two or three cycles is "
        "sufficient",
    ])
    step("03", "EXAM: CompTIA Security+ SY0-701", "Week 29", [
        "Take the exam. $392 USD (2026). Valid for three years",
        "<b>List on resume as:</b> CompTIA Security+ SY0-701 (Expires [date])",
    ])
    step("04", "APPLY: Main Application Push", "Week 29 onward", [
        "With Security+ now on your resume, intensify the application push that began in Phase IV "
        "\u2014 widen to more startups and AppSec-adjacent roles",
        "By now you should have 4\u20136 published writeups, the Juice Shop assessment PDF, and an "
        "application-ready LinkedIn and GitHub",
        "Continue through interview preparation (Phase VIII); see \u201c<a href=\"#application_strategy\" color=\"#3A7AB8\">Application Strategy</a>\u201d "
        "there for targeting, framing, and profile detail",
    ])
    SS("Concepts Mastered")
    concept("Security+ exam domains",
            "<b>All five SY0-701 domains:</b> General Security Concepts, "
            "Threats/Vulnerabilities/Mitigations, Security Architecture, Security Operations, "
            "Security Program Management & Oversight")
    concept("Governance and compliance",
            "Risk management frameworks, regulatory compliance (HIPAA, PCI-DSS, SOC 2), security "
            "policy and procedure, security awareness training")
    concept("Cryptography fundamentals",
            "Symmetric and asymmetric encryption, hashing algorithms, PKI, certificate lifecycle, "
            "TLS/SSL configuration")
    concept("Network security",
            "Firewalls, IDS/IPS, VPN, network segmentation, wireless security")
    concept("Identity and access management",
            "Authentication protocols, MFA, SSO, directory services, privileged access management")
    concept("Incident response",
            "IR lifecycle phases, forensics fundamentals, log analysis, chain of custody")
    add(SP(2))
    SS("How These Concepts Are Used as an AppSec Engineer")
    concept("ATS filter",
            "Security+ signals baseline security literacy to automated resume screening at "
            "enterprise companies and regulated industries. It does not substitute for portfolio "
            "work in human interviews.")
    concept("Governance vocabulary",
            "AppSec engineers work with compliance teams. Knowing what PCI-DSS requires for web "
            "applications, what HIPAA means for data handling, and how risk frameworks are "
            "structured makes cross-team conversations productive.")
    concept("Common interview ground",
            "Cryptography, network security, and authentication fundamentals from Security+ appear "
            "in entry-level AppSec interviews. The certification confirms baseline literacy before "
            "the technical AppSec questions start.")

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE VIII — INTERVIEW PREPARATION & INTERVIEWING
    # ════════════════════════════════════════════════════════════════════════
    def qa(q, a):
        add(KeepTogether([
            P(f"<b>Q: {q}</b>", S["bul"]),
            P(f"<b>Key points:</b> {a}", S["bulsm"]),
        ]))
        add(SP(2))

    add(PageBreak())
    add(banner("VIII", "Interview Preparation & Interviewing", "Months 7.5–8"))
    add(SP(10))
    add(P("AppSec interviews test security knowledge, adversarial reasoning, and communication "
          "\u2014 not algorithmic problem solving. Preparation rests on three things done "
          "deliberately: rehearsed behavioral answers, memorized technical note cards, and "
          "hands-on programming practice. Each is covered below, then mapped to the specific "
          "interview formats you will encounter.", S["body"]))
    add(SP(2))
    SS("Behavioral Question Rehearsals")
    add(P("Write out full answers to the stock behavioral questions, memorize them, then rehearse "
          "out loud until delivery is natural rather than recited. Cover past experience and "
          "previous jobs, the typical \u2018toughest challenge you faced,\u2019 \u2018a time you "
          "disagreed with a teammate,\u2019 and \u2018why this transition into security.\u2019 Keep "
          "a tight version and an expanded version of each so you can scale the answer to the "
          "interviewer\u2019s follow-ups.", S["body"]))
    add(B("Rehearse the AppSec-specific behavioral prompts too: handling a developer who pushes "
          "back on a finding, prioritizing a backlog of vulnerabilities, and explaining risk to a "
          "non-technical stakeholder."))
    add(SP(2))
    SS("Technical Note Cards")
    add(P("Organize note cards by topic \u2014 Python, software development (general), SQL and "
          "database normalization, and the security domains (OWASP Top 10, the individual "
          "vulnerability classes, and defensive patterns). The cards are the most load-bearing "
          "prep tool, and the review method matters as much as the cards themselves.", S["body"]))
    add(P("<b>Review method:</b> study in sub-groups of 7 cards. Review each sub-group 5 times, "
          "until those 7 are memorized. Then combine that sub-group into your running "
          "\u2018reviewed\u2019 pile and review the entire reviewed pile again. Anything missed on "
          "that pass, re-review a couple more times. Repeat the cycle \u2014 5 passes on the next "
          "sub-group of 7, combine, then a full reviewed-pile pass \u2014 until every card for the "
          "topic is covered. As upkeep, read through the different reviewed groups periodically so "
          "they stay locked in.", S["body"]))
    add(SP(2))
    SS("Technical Programming Practice")
    add(P("The hands-on formats \u2014 secure code review, light scripting, and system design "
          "\u2014 reward deliberate practice the same way an algorithms candidate grinds patterns. "
          "Do not just complete exercises; internalize the patterns, why they work, and when each "
          "applies.", S["body"]))
    add(B("<b>Secure code review:</b> practice the read \u2192 identify the vulnerability class "
          "\u2192 explain the exploitation \u2192 recommend the fix loop until it is automatic, and "
          "do it out loud \u2014 interviews require spoken fluency. Use <a href=\"https://securitylab.github.com/\" color=\"#3A7AB8\">GitHub Security Lab</a>\u2019s "
          "published CVE writeups as a source of real code for cold practice; aim for five cold "
          "reviews per week during this phase."))
    add(B("<b>Light scripting:</b> some companies include a CoderPad session \u2014 write a small "
          "Python script to parse a log file, find a bug in a function, or automate a security "
          "check. Not LeetCode. Build fluency at writing correct Python quickly without an IDE; a "
          "book like “<i>Impractical Python Projects</i>” (2019) is good for varied, self-contained "
          "practice. Your development background carries most of this."))
    add(B("<b>System design with security focus:</b> practice designing and critiquing "
          "architectures for security \u2014 design a secure authentication system, or review a "
          "proposed microservice design for trust boundaries and STRIDE threats. Rehearse "
          "explaining the design verbally; your developer background is the advantage here."))
    add(SP(4))
    add(P("Sample cold-review snippets to drill until the class is obvious on sight:", S["body"]))
    add(B("<b>Python:</b> a web endpoint accepting user input without sanitization \u2014 identify "
          "the injection class"))
    add(B("<b>JavaScript:</b> a React component rendering props with dangerouslySetInnerHTML "
          "\u2014 identify the XSS vector"))
    add(B("<b>Python:</b> a JWT decoded with algorithm=\u2018none\u2019 accepted \u2014 identify "
          "the authentication bypass"))
    add(B("<b>Python:</b> a user ID taken from a request parameter without an authorization check "
          "\u2014 identify the IDOR"))
    add(B("<b>Python:</b> a URL parameter fetched server-side without validation \u2014 identify "
          "the SSRF"))
    add(SP(2))
    SS("Interview Preparation")
    add(P("Each interview format maps to one of the methods above:", S["body"]))
    add(B("<b>Behavioral</b> \u2014 your pre-written answers and rehearsals."))
    add(B("<b>Conceptual security questions</b> \u2014 note-card review: OWASP concepts, "
          "vulnerability explanations, and defensive recommendations, no code required."))
    add(B("<b>Secure code review exercise</b> \u2014 the secure-code-review routine. The most "
          "common AppSec technical screen: a code snippet in Python, JavaScript, or Java with "
          "embedded vulnerabilities, 30\u201345 minutes, verbal explanation of findings required."))
    add(B("<b>System design with security focus</b> \u2014 the system-design practice; your "
          "developer background is the advantage."))
    add(B("<b>Light scripting</b> \u2014 your Python practice. A short CoderPad task (parse a log, "
          "fix a function, automate a check), not LeetCode."))
    add(SP(2))
    SS("Framing Your Background")
    add(B("<b>The narrative:</b> Five years of full-stack software engineering. Deliberate "
          "transition into application security since June 2026. Chose foundational independent "
          "study over bootcamp shortcuts."))
    add(B("<b>The gap:</b> ‘I have been in a full-time transition into application security since "
          "June 2026. Here is what that looks like.’ Share specific projects. The portfolio is the "
          "evidence."))
    add(B("<b>The advantage:</b> ‘I spent five years building the systems AppSec engineers defend. "
          "I know why developers write vulnerable code — because I wrote it too.’"))
    add(B("<b>Target roles:</b> Application security engineer, product security engineer, "
          "security-focused software engineer, DevSecOps engineer. Do not filter narrowly on job "
          "title."))
    add(SP(2))
    SS('<a name="application_strategy"/>Application Strategy')
    add(B("<b>Start applying at Month 4:</b> Security-conscious startups are viable "
          "targets from Month 4 with Phases I\u2013III complete, two published writeups, and "
          "PortSwigger Academy progress visible. Do not wait for curriculum completion."))
    add(B("<b>Pin your best AppSec work:</b> set your GitHub pinned repositories to the key new "
          "artifacts \u2014 the Juice Shop assessment report, your custom Semgrep rule, and the "
          "threat model \u2014 so a reviewer sees application-security work first, not the older "
          "web-dev projects."))
    add(B("<b>Make LinkedIn application-ready:</b> Security+ and, once passed, BSCP listed under "
          "licenses & certifications; portfolio projects and published writeups linked; and the "
          "About section carrying the AppSec transition narrative."))
    add(B("<b>Frame the gap explicitly:</b> Cover letters should state upfront: \u2018After five "
          "years of full-stack engineering, I made a deliberate transition into application "
          "security in June 2026.\u2019 This plan is the evidence."))
    add(B("<b>Target AppSec-adjacent roles too:</b> Security engineer, product security engineer, "
          "DevSecOps, security-focused software engineer \u2014 all overlap substantially with "
          "AppSec. Do not filter too narrowly on title."))
    add(B("<b>Your full-stack background is the pitch:</b> \u2018I spent five years building the "
          "attack surface. Now I am learning to break it \u2014 so I can help teams build more "
          "securely.\u2019"))

    # ════════════════════════════════════════════════════════════════════════
    #  PHASE IX — EXPECTED FIRST DAYS ON THE JOB
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    add(banner("IX", "Expected First Days on the Job", "Months 7.75+"))
    add(SP(10))
    add(P("You will know the vulnerability classes better than many colleagues who arrived through "
          "non-engineering paths. You will be slower on internal tooling, company-specific "
          "security policies, and the organizational dynamics of working with development teams at "
          "varying security maturity. That gap closes in weeks, not months. The engineering "
          "history is the relevant benchmark: hired at 14 weeks of web dev self-study, productive "
          "within the first weeks of employment.", S["body"]))
    add(SP(2))
    SS("First Two Weeks")
    add(P("Read the existing security documentation the way you read a codebase — understand what "
          "is there before suggesting what should change. Ask about the current vulnerability "
          "backlog before proposing new tooling. Understand what development teams build and how "
          "they ship before inserting yourself into their process.", S["body"]))
    add(B("What is the current SAST setup, if any? What do developers receive as output?"))
    add(B("What does the existing pentest methodology look like? How are findings tracked?"))
    add(B("Who are the key development team contacts? What are their current security concerns?"))
    add(B("What does the incident response process look like? Has it been tested?"))
    add(SP(4))
    add(nb("The question to ask in the first week is not ‘what should we add?’ It is ‘what is "
           "already here, and why is it the way it is?’ The answer tells you everything about the "
           "political and organizational constraints you are working within."))
    add(SP(6))
    SS("Your Immediate Differentiators")
    concept("Developer empathy",
            "You understand why developers write vulnerable code because you wrote it too. This "
            "makes you a better communicator than security professionals who have never shipped "
            "production software.")
    concept("API security depth",
            "REST API security is the dominant AppSec domain in 2026. Hands-on API security "
            "knowledge built throughout this plan means arriving on day one prepared for the "
            "work.")
    concept("Automation instinct",
            "Security teams full of former analysts often under-automate. Your engineering "
            "background means Semgrep rule development, CI/CD integration, and tooling scripting "
            "come naturally.")
    concept("Full-stack deployment",
            "You can own the deployment of security tooling from writing the Semgrep rule to "
            "integrating it into GitHub Actions to triaging the results. Most AppSec engineers "
            "need help with the deployment layer.")
    add(SP(4))
    SS("The Gap and How Long It Takes to Close")
    add(P("The distance between ‘knows the vulnerability classes and tooling’ and ‘productive "
          "AppSec team member who moves fast with developers’ is 4–8 weeks for someone with your "
          "foundation and learning velocity. The developer background compresses this timeline — "
          "you already speak the language of the teams you will be working with. You will not be a "
          "liability. You will be a junior on a clearly steep upward curve — which is what good "
          "security teams want to hire.", S["body"]))

    # ════════════════════════════════════════════════════════════════════════
    #  APPENDIX
    # ════════════════════════════════════════════════════════════════════════
    add(PageBreak())
    H("Appendix")
    SS("Books & Learning Resources")
    books = [
        [P("<b>Title / Source</b>", S["th"]), P("<b>Author / Year</b>", S["th"]),
         P("<b>Phase</b>", S["th"]), P("<b>Notes</b>", S["th"])],
        [P("“<i>Alice and Bob Learn Application Security</i>”", S["tc"]), P("Tanya Janca, 2020", S["tc"]),
         P("II–III", S["tcc"]),
         P("wiley.com. The most accessible AppSec entry point in print. SDLC security, threat "
           "modeling intro, developer collaboration. Appears on every AppSec practitioner reading "
           "list.", S["tc"])],
        [P("“<i>Real-World Bug Hunting</i>”", S["tc"]), P("Yaworski, 2019", S["tc"]), P("I–III", S["tcc"]),
         P("nostarch.com. Most accessible intro to web vulns. Organized by vuln class with real "
           "bug bounty reports.", S["tc"])],
        [P("“<i>The Web Application Hacker’s Handbook</i>”", S["tc"]),
         P("Stuttard & Pinto, 2nd ed. 2011", S["tc"]), P("II–III", S["tcc"]),
         P("Dafydd Stuttard and Marcus Pinto, Wiley, 2011 (wiley.com). Ch. 1–3 cover "
           "fundamentals. Ch. 6 authentication, Ch. 7 session management, Ch. 8 access controls.",
           S["tc"])],
        [P("“<i>Hacking APIs</i>”", S["tc"]), P("Corey Ball, 2022", S["tc"]), P("III–IV", S["tcc"]),
         P("nostarch.com. REST API security testing. Direct overlap with your API background.",
           S["tc"])],
        [P("“<i>Threat Modeling: Designing for Security</i>”", S["tc"]), P("Shostack, 2014", S["tc"]),
         P("V", S["tcc"]),
         P("wiley.com. Standard text. Ch. 1–5 are primary content.", S["tc"])],
        [P("OWASP WebGoat + OWASP Juice Shop", S["tc"]), P("—", S["tcc"]), P("I / IV", S["tcc"]),
         P("github.com/WebGoat/WebGoat and github.com/juice-shop. Run via Docker. Deliberately "
           "vulnerable apps for Phase I and IV respectively.", S["tc"])],
        [P("TryHackMe", S["tc"]), P("—", S["tcc"]), P("I–II", S["tcc"]),
         P("tryhackme.com. Browser-based guided rooms. <a href=\"https://tryhackme.com/path/outline/web\" color=\"#3A7AB8\">Web Fundamentals</a> and Jr Penetration Tester "
           "paths.", S["tc"])],
        [P("OWASP Threat Dragon", S["tc"]), P("—", S["tcc"]), P("VI", S["tcc"]),
         P("owasp.org/www-project-threat-dragon. DFD and threat modeling tool.", S["tc"])],
    ]
    add(grid_table(books, [1.25*inch, 0.6*inch, 2.3*inch, avail-4.15*inch]))
    add(SP(10))
    SS("Certifications")
    certs = [
        [P("<b>Certification</b>", S["th"]), P("<b>Provider</b>", S["th"]),
         P("<b>Phase</b>", S["th"]), P("<b>Cost</b>", S["th"]), P("<b>Notes</b>", S["th"])],
        [P("Security+ SY0-701", S["tc"]), P("CompTIA", S["tc"]), P("VI", S["tcc"]),
         P("$392", S["tcc"]),
         P("ATS filter-passer. Required for many enterprise and regulated industry postings.",
           S["tc"])],
        [P("Burp Suite Certified Practitioner", S["tc"]), P("PortSwigger", S["tc"]),
         P("IV", S["tcc"]), P("—", S["tcc"]),
         P("Practical exam. Highly respected in AppSec community. Stronger technical signal than "
           "Sec+.", S["tc"])],
        [P("GWEB", S["tc"]), P("GIAC", S["tc"]), P("Post-job", S["tcc"]), P("~$999", S["tcc"]),
         P("GIAC Web Application Defender. Specialized, respected, expensive. Realistic after "
           "first role.", S["tc"])],
        [P("CSSLP", S["tc"]), P("ISC2", S["tc"]), P("Post-job", S["tcc"]), P("~$599", S["tcc"]),
         P("Certified Secure Software Lifecycle Professional. SDLC-focused. Useful for senior "
           "roles.", S["tc"])],
    ]
    add(grid_table(certs, [1.4*inch, 0.85*inch, 0.7*inch, 0.55*inch, avail-3.5*inch]))
    add(SP(10))
    SS("Practical Use Per Phase")
    pp = [
        ("Phase I — AppSec Intro",
         "Use Claude to explain why a WebGoat exploit works at the code level. Ask it to describe "
         "the difference between SQL injection and command injection in plain English. Have it "
         "generate sample vulnerable Python code for practice — and then explain what makes it "
         "vulnerable."),
        ("Phase II — Web & Network Foundations",
         "Use Claude to explain HTTP security headers step by step: what does SameSite=Strict "
         "actually prevent, mechanically? Have it walk through an OAuth 2.0 flow and identify "
         "where common vulnerabilities occur. Ask it to explain the difference between "
         "authentication and authorization until it clicks."),
        ("Phase III — Core Vulnerability Classes",
         "Use Claude to generate additional practice examples for vulnerability classes where "
         "PortSwigger labs are thin. Have it produce a vulnerable Python function and explain "
         "exactly which line introduces the vulnerability and why. Ask it to explain why a "
         "particular XSS payload bypasses a specific filter."),
        ("Phase IV — Security Testing & Tooling",
         "Use Claude to review your custom Semgrep rule and identify edge cases it misses. Have "
         "it explain a Bandit finding ID you have not seen before (e.g. B324 hashlib insecure). "
         "Have it explain <a href=\"https://portswigger.net/burp/documentation/desktop/tools/repeater\" color=\"#3A7AB8\">Burp Suite Repeater</a> output when a response is unexpected. Ask it to help "
         "write the executive summary section of the Juice Shop report."),
        ("Phase V — Cloud Security Fundamentals",
         "Use Claude to explain what an IAM policy JSON document is doing in plain English. Ask it "
         "to identify the security problem in a sample bucket policy you paste in. Have it explain "
         "the difference between IMDSv1 and IMDSv2 and why the distinction matters for SSRF. Ask "
         "it to help write up a cloud security finding in professional report format."),
        ("Phase V — Code Review & Threat Modeling",
         "<b>Use Claude as a review partner:</b> paste a code snippet and ask it to identify "
         "vulnerabilities from the perspective of an AppSec engineer. Have it critique your threat "
         "model document: what threats did STRIDE miss? What mitigations are insufficient?"),
        ("Phase VI — Sec+ Certification",
         "Use Claude as a study partner for practice questions. Give it a domain you are weak on "
         "and ask it to quiz you. Have it explain compliance frameworks (NIST CSF, ISO 27001) in "
         "plain English — the governance domains are the new material."),
        ("Phase VII — Sec+ & Interviews",
         "Use Claude as a technical interviewer. Give it a vulnerable code snippet and ask it to "
         "evaluate your explanation as if it were an AppSec hiring manager. Have it generate the "
         "strongest possible objections to your vulnerability findings — surface the gaps before "
         "an interview does."),
    ]
    pp_text = S["bulsm"].clone("ppt"); pp_text.spaceAfter = 1
    for name, text in pp:
        add(KeepTogether([P(f"<b>{name}</b>", S["bul"]), P(text, pp_text)]))

    # ════════════════════════════════════════════════════════════════════════
    #  PHILADELPHIA APPSEC COMMUNITY  (subsection of the Appendix)
    # ════════════════════════════════════════════════════════════════════════
    add(SP(8))
    add(P('<a name="philly_appsec"/>Philadelphia AppSec Community', S["sshead"]))
    adds(rule())
    add(P("Security networking operates differently from general tech networking. The community "
          "is smaller, more tight-knit, and more willing to help people who show genuine "
          "curiosity. Attending events before you are employed builds relationships that become "
          "referrals. Show up, ask good questions, and bring something to demonstrate \u2014 even "
          "a completed PortSwigger lab that taught you something surprising.", S["body"]))
    add(SP(4))
    add(P("<b>Core Groups</b>", S["body"]))
    grp = [
        ("OWASP Philadelphia Chapter", "owasp.org/www-chapter-philadelphia \u00b7 Free",
         "The most directly relevant group for AppSec networking in Philadelphia. OWASP (Open Web "
         "Application Security Project) is the professional organization for web application "
         "security globally. The Philadelphia chapter holds regular meetings with technical "
         "presentations on vulnerability classes, tooling, and real-world AppSec work. The people "
         "in this room are AppSec practitioners at companies across the region \u2014 exactly the "
         "referral network you are building toward."),
        ("DC215 \u2014 Philadelphia DEF CON Group", "dc215.org \u00b7 Free",
         "DEF CON Groups are local offshoots of DEF CON, the largest hacker conference in the "
         "world. DC215 holds regular meetups with technical talks, CTF practice, and informal "
         "knowledge sharing. Builder-focused and practitioner-dense. The format rewards people "
         "who bring something to show. Attend when Phase III work (vulnerability classes) is "
         "underway."),
        ("BSides Philadelphia", "bsidesphilly.org \u00b7 Annual \u00b7 Low cost",
         "Community-organized security conference with talks across offensive, defensive, and "
         "AppSec tracks. Affordable, full-day, attended by local practitioners from the companies "
         "you will apply to. Volunteer if possible \u2014 it is how you get face time with "
         "organizers and speakers."),
        ("Philly 2600", "philly2600.net \u00b7 First Friday monthly \u00b7 Free",
         "Philadelphia\u2019s oldest hacker meetup \u2014 running since the early 1990s and one of "
         "the first 2600 meetings ever listed in 2600 Magazine. Meets the first Friday of every "
         "month at Iffy Books, 404 S 20th St, starting at 6pm. No set agenda, no presentations, "
         "no gatekeeping \u2014 a casual hangout where people bring things to hack on or show off. "
         "Open to anyone. Around 8pm the group typically moves to a nearby bar. The lowest-"
         "pressure entry point into the Philly security community and a good place to show up "
         "early in the plan before you have polished work to present."),
        ("PhillySec", "meetup.com \u00b7 Second Wednesday monthly \u00b7 Free",
         "Monthly security meetup, second Wednesday of each month. More structured than Philly "
         "2600 \u2014 presentations and technical discussions rather than open hangout format. "
         "Good mid-plan target once Phase II or III is underway and you have something to "
         "contribute to conversations."),
        ("Ex Machina Parlor", "319 N 11th St, Room 501 \u00b7 Philadelphia",
         "A hackerspace specifically aimed at people interested in cybersecurity \u2014 formerly "
         "known as Trashpanda Village and SecShell. Workshop and collaborative hacking space "
         "rather than a meetup. Worth knowing it exists as a physical space to work alongside "
         "practitioners. Check their calendar for events and open nights."),
    ]
    for name, meta, desc in grp:
        add(P(f"<b>{name}</b>", S["bul"]))
        add(P(meta, S["lnk"]))
        add(P(desc, S["bulsm"]))
        add(SP(3))
    add(SP(2))
    add(SP(4))
    add(P("<b>Conferences</b>", S["body"]))
    add(B("<b>OWASP Global AppSec \u2014 Washington DC</b> (owasp.org/events \u00b7 Annual \u00b7 "
          "November) \u2014 The flagship AppSec-specific conference in the US. 800+ "
          "practitioners, six tracks including builder/developer, breaker, defender, and OWASP "
          "projects. Washington DC is a short trip from Philadelphia. This is the single most "
          "targeted conference in the plan \u2014 the audience is exactly the community you are "
          "entering and the talks directly map to the skills in every phase. Attend once Phase IV "
          "or V is complete."))
    add(B("<b>OWASP BASC \u2014 Boston</b> (owasp.org \u00b7 Annual \u00b7 Fall) \u2014 The OWASP "
          "Boston Application Security Conference. Regional, practitioner-dense, focused on AppSec "
          "engineering and secure development. Closer and lower-cost than the DC Global AppSec. "
          "Strong emphasis on hands-on content and OWASP standards \u2014 the audience overlaps "
          "heavily with who you will work alongside in the role."))
    add(B("<b>Thotcon \u2014 Chicago</b> (thotcon.org \u00b7 Annual \u00b7 May) \u2014 A mid-sized "
          "hacker conference: more intimate than DEF CON, technically dense, practitioner-"
          "focused. Worth targeting once Phase III or IV work is underway and you have something "
          "real to talk about."))
    add(B("<b>JawnCon \u2014 Philadelphia</b> (jawncon.org \u00b7 Annual) \u2014 "
          "Philadelphia\u2019s own security and technology conference. Covers a wide range of "
          "security and tech topics with a deliberately approachable, community feel. Worth "
          "attending as a local conference where you will run into the same practitioners from "
          "OWASP and DC215."))
    add(B("<b>DEF CON \u2014 Las Vegas</b> (defcon.org \u00b7 Annual \u00b7 August) \u2014 DEF CON "
          "34 runs August 6\u20139, 2026 at the Las Vegas Convention Center. The flagship hacker "
          "conference. Within DEF CON, the AppSec Village (appsecvillage.com) is a 100% "
          "volunteer-run space specifically for application security \u2014 attacker-minded "
          "talks, live demos, hands-on workshops, a Fix-the-Flag CTF that rewards remediating "
          "vulnerabilities, and rapid tool demos at the Arsenal. The AppSec Village is the most "
          "directly relevant part of DEF CON for this career path. Attend once Phase IV or V is "
          "complete."))


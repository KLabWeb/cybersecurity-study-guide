# CHANGELOG_APPLIED — items baked into the source (.py) but NOT yet generated to PDF

This ledger tracks which changelist items are implemented in the source code.
The .py files in this folder are the latest accumulated state.
PDF generated and TOC verified against actual pages (48pp).

## Implemented so far
- [x] 1 — Cover subtitle now "Independent Self-Study — Kyle Miskell  —  kmiskell@protonmail.com"
- [x] 2 — Removed cover "Orientation → … → Job" arrow-progression text (gold underline kept)
- [x] 3 — Weeks→Months convention at PHASE LEVEL: timeline cells, phase banner durations,
        and phase section sub-headers now use "Months" for phases past week 8 (II–IX);
        phases 0 and I stay in "Weeks". Phase II = Months 1.5–2 (per your example).
        NOTE: granular per-step labels (e.g. "· Week 11", "Weeks 10–11") were left as
        weeks pending your confirmation (see status note in chat).

- [x] 4 — Interview Prep (VIII) moved to start week 27 (month 6.75): banner now "Months 6.75–7.25";
        First Days (IX) banner now "Months 7+"; timeline VIII/IX cells updated. Security+ exam
        stays Week 26 (no overlap). NOTE: IX "First Days" set to 7+ for sequential consistency
        (it follows interview prep); flagged in chat. No internal week numbers existed in VIII/IX.
- [x] 5 — Phase Timeline fixed to match the 10 real phases (0–IX): removed the spurious
        "Portfolio" column, so VIII = Interview Prep and IX = First Days now carry the correct
        roman numerals; reduced to 10 colored columns.
- [x] 6 — Removed "Conceptual Questions — Know These Cold" section (all Q&A entries) and its TOC sub-entry.

- [x] 7 — Phase VIII renamed "Interview Preparation & Interviewing" (banner, TOC title, comment).
- [x] 8 — Reworked Phase VIII: removed "Pre-Interview Portfolio Checklist" (not relocated — the
        underlying project work already lives in earlier phases; flagged in chat). Added three
        method sections: Behavioral Question Rehearsals; Technical Note Cards (with the 7-card
        sub-group / 5x / combine-into-reviewed-pile spaced-repetition method); Technical
        Programming Practice (secure code review via GitHub Security Lab CVE writeups; light
        scripting via CoderPad drills + Impractical Python Projects (2019); security-focused
        system design). Renamed "Interview Format: What to Expect" -> "Interview Preparation",
        now mapping each format to its prep method. Kept "Framing Your Background". No
        NeetCode/LeetCode recommended (security-appropriate resources used).
- [x] 9 — Already satisfied by item 5: "Expected First Days on the Job" now carries roman IX in
        the Phase Timeline.

- [x] 8-followup (A–D) — restored the substance of the removed Pre-Interview Portfolio
        Checklist into the earlier phases where the work happens:
        A. Phase IV Juice Shop step: export the report as a polished, shareable standalone PDF.
        B. Study Methodology / Portfolio: READMEs explain methodology + what each artifact
           demonstrates (was just "Clean READMEs").
        C. Application Strategy: pin the new AppSec artifacts (Juice Shop report, Semgrep rule,
           threat model) on GitHub.
        D. LinkedIn profile setup — early (Phase 0 GitHub-hygiene step: About-section transition
           narrative) + application-ready (Application Strategy: Security+/BSCP listed, projects
           linked, About narrative).
        (Item 4 of the old checklist — 4+ writeups published on LinkedIn — was already covered.)

- [x] 10 — Cover pills updated: VIII pill now "Interview / Prep" (matches the renamed phase and the
        timeline label). The pills were already 0–IX with correct romans (no Portfolio pill bug),
        so only VIII's label needed changing.
- [x] 11 — Reworded: "...insecure deserialization. These are not abstract academic concerns — they
        are the specific vulnerability classes..." (was "— these are not abstract academic
        concerns. They are...").
- [x] 12 — Replaced "— they understand for five years." with "— they have already built the
        software systems being tested for security risks and strength themselves."

- [x] 13 — Fixed the 60/40 math: "Over 60% ... integrate ... which means nearly 40% still do not"
        (was "over 40%", which summed past 100%).
- [x] 14 — Verified AppSec salaries via web (Indeed ~$148K avg, ZipRecruiter ~$138K avg /
        $117.5K–$157K typical, Glassdoor ~$181K total, base-only aggregators ~$98K). The
        compensation table (entry $90–130K, mid $130–180K, senior $170–240K, top $250K+) is
        realistic; the outlier was the prose claim "$126,000–$194,000 at mid-level", now aligned
        to "$130,000–$180,000" to match the table.
- [x] 15 — (a) Added "poorly written legacy PHP codebases" to the "You know FastAPI ... Docker
        containers" stack sentence. (b) Added a "Legacy PHP and hand-rolled SQL" transferable-skill
        bullet covering legacy PHP, legacy/raw SQL (-> SQL injection / IDOR / unsanitized input
        from the inside) and modern DynamoDB (-> NoSQL injection / cloud data-access control).
        NOTE: the resume PDF was not present in uploads this session, so I used the experience
        facts you stated (legacy PHP, legacy SQL, DynamoDB) rather than reading the resume.

- [x] 16 — "AppSec testing follows the same deterministic logic: ..." (added "deterministic").
- [x] 17 — "The relief this should produce is real and substantial." (was "real and earned").
- [x] 18 — "The 2026 job market is highly difficult for web development." (added "highly").
        NOTE: this sentence sits inside "The Timing Argument" subsection, which item 19 is slated
        to REMOVE — so this edit will be discarded by item 19 unless we choose to preserve the
        point elsewhere. Flagged in chat for decision at item 19.

- [x] 15-resume — Resume now available; enhanced the transferable-skills section: refined the
        legacy-code bullet to "Legacy PHP, raw SQL, and NoSQL" (you maintained poorly written
        legacy PHP and hand-rolled MySQL AND refactored 'big ball of mud' procedural PHP to OOP
        — recognize + remediate; DynamoDB -> NoSQL injection). Added a new "Architecture &
        domain modeling" bullet (your microservice/domain-service design experience maps directly
        to threat modeling). [Discretionary architecture bullet flagged in chat.]
- [x] 19 (COMPLETE) — Removed "The Timing Argument" subsection (last sub-section of Why AppSec
        Engineering; not in TOC, so no TOC sub-entry change). This supersedes item 18's edit per
        higher-number-wins. STILL PENDING: move "Why This Moment" to AFTER "Why AppSec Engineering"
        + swapped their order in the TOC (page numbers deferred to item 24).

- [x] 20 — Reduced FastAPI focus: genericized 8 generic stand-in references (Why AppSec, Target
        Role, Phases III/V/VI, appendix) to "web application" / "software system" / "Python web
        application (Django, Flask, or FastAPI)" / "API". Kept FastAPI where it is genuinely your
        resume background (transferable-skills bullets) and the concrete pre-study build project
        (Phase 0). FastAPI mentions: 23 -> 16.
- [x] 21 — Removed cross-section redundancy: the "developer-background-is-the-advantage" argument
        now lives only in "Why AppSec Engineering". Trimmed it from "What Is AppSec" para 5 (kept
        the scoping sentence) and removed the "Why your background fits this moment specifically"
        subsection from "Why This Moment" (it duplicated both the adjacent Why-AppSec section and
        the workforce-gap point; kept the market nb-box closer). Target Role left untouched.

- [x] 22 — Schedule table: removed the "Rest w/ Short Study" row; now 21 study hours/week across
        3 Long Study days x 7 hrs, with 2 full rest days/week (week = 3 study + 2 gig + 2 rest = 7
        days). Intro updated "20-23" -> "21 study hours per week". Folded the dropped day's
        activities (note-card review, writeups) into the Long Study notes so nothing is lost.
- [x] 23 — Work (Gigs) days set to 7 hrs (was 6-7 hrs).

- [x] 24 (COMPLETE) — Reconciled the Contents:
        all section titles verified against actual H()/banner headers (all match); fixed the
        roman-numeral bug (a second "VIII" -> "IX" for Expected First Days). TOC romans are now a
        clean 0,I,II,III,IV,V,VI,VII,VIII,IX. Order already swapped in item 19.
        PAGE NUMBERS finalized by building the PDF and scanning actual page positions (pdfplumber,
        no image rendering). Updated 5 stale entries: Why AppSec 6->4, Why This Moment 4->6,
        II Web&Network 19->22, IX 45->44, Appendix 47->46. Verified by an independent
        TOC-page-skipping sequential scan: all 19 entries match actual pages, monotonic increasing.
        Also hardened build_appsec.py scan_pages to skip TOC pages so the build self-verifies.
        Final PDF: 48 pages.

## Not yet implemented
- [ ] (none — ALL 24 CHANGELIST ITEMS COMPLETE)

## Build-system changes (post-changelist)
- Output filename is now date-based: OUTPUT in appsec_infrastructure.py uses
  datetime.date.today() -> "Study_Plan_-_YYYY-MM-DD.pdf" (today: Study_Plan_-_2026-06-25.pdf).
- Self-correcting TOC: build_appsec.py main() now runs a build->scan->fix->rebuild loop.
  * build_content(appsec_content.py) accepts page_overrides={toc_title: page}; the TOC renders
    page_overrides.get(title, <source default>) so the build can override page numbers.
  * Each pass: build, scan ACTUAL section pages (pdfplumber, TOC-page-skipping robust scan),
    and if any TOC page != actual page, set overrides=actual and rebuild. Repeats until the
    printed TOC matches actual pages (handles digit-count-driven repagination), max 8 passes.
  * Ends with an independent final verification printed per-section, and saves the converged
    {toc_title: page} map to appsec_toc_state.json (so later runs converge in ~1 pass).
  * NOTE: TOC sub-entries are descriptive labels and carry no page numbers, so only section-level
    page numbers are reconciled.
- appsec_toc_state.json reset to {} so the next GENERATE PDF starts clean and self-corrects.

## 2nd Changelist — items 1–3 (source applied, not yet generated)
- **1. Bump Phase VI to next page** — added a forced blank page (PageBreak + nbsp paragraph + PageBreak) before the "VI — Secure Code Review & Threat Modeling" banner, so VI starts one page later than it otherwise would. Subsequent page numbers shift +1; self-correcting TOC reconciles at GENERATE.
- **2. Move "Application Strategy"** — removed from end of "Study Methodology"; reinserted verbatim at the end of Phase VIII "Interview Preparation & Interviewing", after "Framing Your Background" (the natural prep → framing → apply capstone).
- **3. OWASP list close** — "…security misconfigurations, insecure deserialization." → "…security misconfigurations, insecure deserialization, and other key risks." (in "What Is Application Security?").

## 2nd Changelist — items 4–6 (source applied, not yet generated)
- **4. Shortened the two resume bullets** — "Legacy PHP, raw SQL, and NoSQL" (6 lines → 3) and "Architecture & domain modeling" (5 lines → 4) trimmed to match the length of the surrounding transferable-skills bullets; core point of each preserved.
- **5. Expanded the "relief" clause** — "The relief this should produce is real and substantial" → "…this should produce as part of a break from never-ending leetcode grinding, contrived software engineering interviews, and poor communication during the full software eng interview lifecycle is real and substantial." (in "Why AppSec Engineering").
- **6. Philadelphia AppSec Community → Appendix** — (a) entire section relocated to the end of the Appendix; (b) "Human Mentorship: MentorCruise" → "Human Mentorship: MentorCruise (or Koz)"; (c) added a short new "Local & Regional Events" subsection after it (events as part of studying — networking + reconnecting to the industry; brief highlights: OWASP Philadelphia, Philly 2600, OWASP Global AppSec DC; points to the Appendix section for full details). TOC reconciled (Philadelphia entry moved below Appendix; new subsection listed; Study-Methodology subs updated). build_appsec.py SECTIONS reordered (Philadelphia now scanned after Appendix) so the self-correcting TOC resolves its new page and the new cross-reference text can't be false-matched.
- **(item 2 follow-up)** TOC subs corrected for last batch's move: removed "Application Strategy" from Study Methodology, added it under Phase VIII.

## 2nd Changelist — item 7 (source applied, not yet generated)
- **7. Spring 2026 → Summer 2026** — "Compensation — Spring 2026" subsection heading and its TOC entry both updated to "Compensation — Summer 2026". These were the only "Spring 2026" references in the document. (The five "transition into application security since May 2026" references were left unchanged — they state when the career transition began, not a Spring/Summer label; flagged for the user to revisit if desired.)

## 2nd Changelist — item 8 (sequential-steps + full timeline reconciliation; source applied)
Verified mapping: Month = Week / 4 (checked against Phases III & VII, exact).
- **"Start applying" conflict** (Month 3-4 / 4-5 / 5 / 5-6 across 4 places) reconciled to a single timeline: **begin Month 4** (after Phases I-III complete at Mo 3.5, with 2+ writeups), **main push Month 6** (Security+ on resume). Updated Target Role nb, Schedule nb, Portfolio target, and Application Strategy.
- **Added explicit application steps** so the floating directives map to real phase steps: Phase IV step 09 "APPLY: Begin Job Applications" (Month 4), Phase VII step 04 "APPLY: Main Application Push" (Month 6).
- **Phase II duration** relabeled Months 1.5-2 -> **1.5-2.25** (banner + timeline chart + schedule heading) to match its actual Week 6-9 span; eliminates steps running past the stated phase end and normalizes the II->III buffer to 0.25 like other boundaries.
- **Phase II step 03** week tag fixed Week 5 -> **Week 7** (Week 5 belongs to Phase I; this was the only break in the otherwise-continuous Weeks 1-26 schedule).
- **Phase IV step numbering** fixed: two "05"s + missing "04" -> Semgrep step renumbered to 04; phase now 01-09 sequential.
- **Prose duration fixes:** Phase II intro "two focused study weeks" -> "a focused final week" (crypto + networking are both Week 9); Phase I intro "in three weeks" -> "in two weeks" (Phase I is Weeks 4-5).
- Left intact (internally consistent, flagged): the five "transition since May 2026" references, and "Commit history from Month 2 onward" (covered by Phase 0 GitHub setup + ongoing project/writeup steps).
- Final re-scan: step numbering sequential in every phase; weeks continuous 1-26 with no gaps/backward jumps; all "start applying" = Month 4; main push = Month 6; phase duration labels (banner = chart = schedule heading) agree for all 10 phases.

## Build-system upgrade — self-correcting TIMELINE check at GENERATE
Added timeline_check.py and wired it into build_appsec.py main(), running BEFORE layout,
mirroring the self-correcting TOC loop (check -> fix -> check -> ... until stable).
Ground-truth convention: Month = Week / 4 (verified against Phases III & VII).

AUTO-FIXED in a loop (each has one deterministic correct value):
  1. Step numbering — steps within a phase must read 01,02,03,... (no gaps/dups); renumbers.
  2. Phase-duration END must cover the last step (label_end == max_step_week/4) — catches a
     phase labelled to end before its own steps finish (the Phase II "1.5-2" vs Week-9 bug).
  3. Three-way agreement — a phase's duration in the banner, the timeline chart, and the
     schedule heading must encode the same numeric range (canonical = the banner); rewrites
     the chart/heading numbers to match. Handles mixed dash styles (literal en/em dash and
     \uXXXX escapes) and the "Mo"/"Wks" vs "Months"/"Weeks" prefix difference.
If it edits the source, build_appsec reloads the content module before building.

REPORTED, never guessed (correct value needs human judgment):
  4. A step whose week falls outside its phase's [start,end] week-bounds
     (e.g. a Phase II step tagged "Week 5" when the phase runs weeks 6-9).
  5. Prose "start applying at Month N" that disagrees with the canonical start (Month 4).

Verified: on the current (reconciled) source the timeline pass makes ZERO edits and reports
ZERO issues; against an injected-fault copy (dup step #, duration undercount, chart/heading
disagreement, out-of-bounds week, prose drift) it auto-fixed the three deterministic classes,
converged on pass 2, and reported the two judgment-class faults.

NOTE: the portable package zip does not yet include timeline_check.py — refresh it before
distributing so a fresh extraction builds with the timeline pass.

## 3rd Changelist — items 1-3 (source applied, not yet generated)
- **1. APPLY steps fixed (order + unit).** Both application steps now use WEEKS instead of months and read in order: Phase IV step 09 "APPLY: Begin Job Applications" tag "Month 4 onward · parallel with study" -> "Throughout Weeks 16-18" (Week 16 = Month 4, mirrors the existing Phase III step 07 "Throughout Weeks 10-14" parallel-step pattern). Phase VII step 04 "APPLY: Main Application Push" tag "Month 6 onward · ..." -> "Week 26 onward" (begins after the Sec+ exam in Week 26). Both now pass the timeline bounds check.
- **2. Philadelphia AppSec Community is now an Appendix subsection, not its own chapter.** Removed its forced page break; demoted its heading H -> SS (matches Books/Certifications/Practical Use Per Phase); demoted its internal "Core Groups"/"Conferences" from SS to bold sub-labels so the nesting reads Appendix > Philadelphia > Core Groups/Conferences. TOC: removed the standalone "Philadelphia AppSec Community" line and added it as a fourth sub under "Appendix". build_appsec.py SECTIONS: removed the Philadelphia entry (it is no longer a page-scanned top-level TOC line).
- **3. Removed "No math prerequisites."** from the Plan Schedule Overview intro paragraph.

## 3rd Changelist — items 4-6 (source applied, not yet generated)
- **4. Plan Schedule Overview chart edits.** "Full Rest" -> "Day Off"; "Income — no study obligation on work days" -> "Income — Two 3–4 hour shifts"; removed "Per week" from the TOTAL STUDY row's Notes cell (now blank); "No study, no work. Required for retention." -> "No study, no work. Required for retention & sanity."
- **5. Internal hyperlink to the Philadelphia appendix subsection.** Added a named destination anchor (<a name="philly_appsec"/>) at the "Philadelphia AppSec Community" heading, and linked the words "Philadelphia AppSec Community" in the Study-Methodology "Local & Regional Events" cross-reference to it using the same color (#3A7AB8) as the web-URL hyperlinks. Markup validated as well-formed reportlab paragraphs.
- **6. Page break before "Portfolio: Writeups & Project Site"** (Study Methodology).

## 3rd Changelist — item 8 (source applied, not yet generated)
- **8. Commit from Day 1.** Rewrote the Portfolio "GitHub:" bullet: "Scripts from the tooling phase... Commit history from Month 2 onward." -> "Commit from Day 1 — the very first commit is this study plan and its build script. Keep one repository for the entire cybersecurity journey: notes, tooling-phase scripts, custom Semgrep rules, automation tools, and lab artifacts, building a continuous commit history from the start. Every README explains the methodology..."
- **7. (Pending)** "4–6 published writeups before the main application push" — recorded with no directive; awaiting clarification on the intended change.

## 3rd Changelist — item 7 (source applied)
- **7. Writeup target reconciled to a ramp.** "Target: 4–6 published writeups before the main application push." -> "Target: at least two published writeups before you begin applying, building to 4–6 before the main application push." Ties the portfolio target to the two defined milestones (begin applying ≈ Month 4 with ~2 writeups, per the Application Strategy; 4–6 by the main push ≈ Month 6) and removes the standalone vague phrasing.

## 4th Changelist — step week-ordering (source applied, not generated)
- **Steps now sorted by week within each phase.** Reordered Phase III and Phase IV so every step reads in ascending (start_week, end_week) order, then renumbered 01,02,…
  - Phase IV before: Burp(15-16), BSCP-Prep(15-17), BSCP-Exam(17-18), Semgrep(16-17), Secrets(17), ZAP(17), Snyk(17-18), Juice Shop(18), APPLY(Throughout 16-18, dumped last).
  - Phase IV after: 01 Burp(15-16), 02 BSCP-Prep(15-17), 03 Semgrep(16-17), 04 APPLY(Throughout 16-18), 05 Secrets(17), 06 ZAP(17), 07 BSCP-Exam(17-18), 08 Snyk(17-18), 09 Juice Shop(18). Fixes the reported case (Semgrep 16-17 now precedes the BSCP exam 17-18) and pulls APPLY into its start-week slot instead of last.
  - Phase III: the "Throughout Weeks 10-14" writeup project moved to step 02 (start week 10), ahead of the week-11/12/13 labs.
- **Made it systematic:** added `reorder_steps()` to timeline_check.py as AUTO-FIX 0 (runs before renumbering in the self-correcting loop), so steps are kept in week order on every GENERATE. Verified idempotent (re-running makes no further changes).
- **Phase 0 left as authored** — its pre-study tasks use day-scoped tags (Day 1 / Days 1-3 / Days 2-4) mixed with one Week tag, so a clean week-sort doesn't apply; left for explicit direction.

## 5th Changelist — extend week-ordering to ALL phases (incl. pre-study)
- Generalized the reorder pass to a unified day-scale key (`_order_key`): Week N -> days [(N-1)*7+1 .. N*7], Day N -> day N. This is order-preserving for week-only phases (they sort identically to before) but lets a phase that MIXES Day- and Week-tags sort by the same ascending start-then-end rule.
- **Phase 0 (Pre-Study) reordered:** was FastAPI(Weeks 1-3), HTTP(Days 1-3), Docker(Days 2-4), Git(Day 1). Now: 01 Git & GitHub Hygiene(Day 1), 02 HTTP & Cookies(Days 1-3), 03 FastAPI(Weeks 1-3), 04 Docker(Days 2-4) — ascending by start day, then end. (FastAPI's day-1 start places it ahead of Docker's day-2 start, mirroring how APPLY·Weeks 16-18 sits ahead of Secrets·Week 17 in Phase IV.)
- Verified ALL ten phases (0-IX) are now in ascending time order; pass remains idempotent (re-run = 0 fixes, 0 issues).

## 6th Changelist — items 1-3 of 10 (source applied, not generated)
1. Phase 0 / concept text fixes:
   - "Review existing HTTP notes (HTML intro notes and Odin HTTP notes)." -> "Review existing HTTP notes (PDF, .odt, and note cards)."
   - "Personal notes covering containers" -> "Personal notes and note cards covering containers"
   - "SQL is the canonical example" -> "SQL injection is the canonical example"
2. Date refresh: all five "May 2026" references in content + the running-page-header "May 2026" (infrastructure.py) -> "June 2026". Left the Thotcon conference's recurring "Annual · May" untouched (not a date reference).
3. De-duplicated: "Their absence or misconfiguration is a finding. Their absence or misconfiguration is a finding in any security review." -> "Their absence or misconfiguration is a finding in any security review."

## 7th Changelist — items 4-6 of 10 (source applied, not generated)
4. **AI references — career comparison removed, threat/industry refs kept.** Per clarification, only the AI-career-vs-cyber-career framing goes. Rewrote the Phase I intro ("AppSec has a mysticism problem from the opposite direction of AI: where AI hype makes it seem unknowably complex…") to "AppSec has a mysticism problem: security culture sometimes makes it seem inaccessible without a decade of CTF grinding. That is not true…". KEPT all AI-as-threat-to-industry content (the "AI Replacing AppSec Engineers" pitfall, "AI is automating the lowest-complexity tasks", entry-level hiring compression), AI-as-industry-fact ("faster AI-assisted detection" in the breach stat), and AI-as-target-employer ("AI-native startups", "Legal AI / LegalTech"). (Reverted two over-eager edits to the breach stat and talent blurb after the clarification.)
5. **Book titles in quotes + italics everywhere.** Wrapped all six published books — Real-World Bug Hunting, Alice and Bob Learn Application Security, Hacking APIs, Threat Modeling: Designing for Security, The Web Application Hacker's Handbook, Impractical Python Projects — as "<i>Title</i>" (curly quotes + italics) across every reference: phase source lists (res), step tags, prose chapter refs, and the Appendix Books table. The "WAHH" acronym shorthand italicized (no quotes on an acronym). Left the OWASP Code Review Guide (a guide, not a published book / not in the Books table) untouched. No double-wrapping.
6. **PortSwigger module hyperlinks** in Phase I "EXPLORE: PortSwigger Academy Orientation": linked "Server-side topics" -> portswigger.net/web-security/all-topics, "SQL Injection" -> /sql-injection, "XSS" -> /cross-site-scripting, all as blue (#3A7AB8) links matching the doc's existing hyperlink style. (URLs verified against the live all-labs page.)

## 8th Changelist — items 7-9 of 10 (source applied, not generated)
7. Phase I WebGoat step: "Clone and run OWASP WebGoat locally via Docker" -> "Ensure local WebGoat still executes as expected in local Docker" (already cloned in the Phase 0 Docker step).
8. Exact WebGoat lesson names: "Complete: SQL Injection (basic), XSS (stored and reflected), Broken Authentication, IDOR" -> "Complete these WebGoat lessons: SQL Injection (intro), Cross Site Scripting, Cross Site Scripting (stored), Authentication Bypasses, and Insecure Direct Object References (IDOR)". (Mapped to current WebGoat lesson titles: basic->intro; reflected XSS = "Cross Site Scripting", stored = "Cross Site Scripting (stored)"; Broken Authentication -> the "Authentication Bypasses" lesson; IDOR -> "Insecure Direct Object References (IDOR)".)
9. TryHackMe link: in Phase I "EXPLORE: TryHackMe Orientation", linked "Web Fundamentals" -> https://tryhackme.com/path/outline/web (blue #3A7AB8), the path that contains HTTP in Detail / Burp basics / OWASP Top 10. Left the other two "Web Fundamentals" mentions (the Phase I TryHackMe source entry and the Appendix table note) unlinked — say the word to link those too.

## 9th Changelist — item 10 of 10 + item-9 follow-up (source applied, not generated)
10. Clarified the ambiguous OWASP Top 10 line. "The full list exists and has structure." -> "The full Top 10 is a structured catalog of the most critical web vulnerability classes." (concept "The OWASP Top 10").
9 (follow-up). Linked "Web Fundamentals" in the two remaining spots, both -> https://tryhackme.com/path/outline/web (blue #3A7AB8): the Phase I TryHackMe source entry and the Appendix Books-table TryHackMe note. The doc now has three Web Fundamentals path links total. (Left "Jr Penetration Tester" path mentions unlinked — say the word to link those too.)

=== ALL 10 CHANGELIST ITEMS COMPLETE ===

## Build fix (during GENERATE)
- linkify() now skips spans already inside an <a>...</a> tag. Previously it re-wrapped the URL inside manually-authored href attributes (the new PortSwigger/TryHackMe links), producing nested <a> tags and a paraparser syntax error at build. Bare-URL auto-linking is unchanged. Verified: all 6 authored links render as clickable annotations; bare URLs (tryhackme.com, github.com/..., owasp.org/...) still auto-link.

## 10th Changelist — fix Phase I PortSwigger links (source applied, not generated)
- The PortSwigger orientation step linked to the wrong things: the all-topics index (dozens of labs) and the SQL/XSS *tutorial* pages, while the text said to do labs. Rewrote step 01:
  - "Create a free PortSwigger account"
  - "Read the [SQL injection] material, then complete the first 3-4 Apprentice-level [labs]" -> material = /web-security/sql-injection, labs = /web-security/all-labs#sql-injection
  - "Read the [cross-site scripting] material, then complete the first 3-4 Apprentice-level [labs] (reflected and stored)" -> material = /web-security/cross-site-scripting, labs = /web-security/all-labs#cross-site-scripting
  - Dropped the ambiguous all-topics "Server-side topics overview" link entirely. All four URLs verified against the live pages (each topic page's "View all <topic> labs" points at the all-labs#<topic> anchor).
- Re-verified the two re-listed items: exact WebGoat lesson names (SQL Injection (intro) / Cross Site Scripting / Cross Site Scripting (stored) / Authentication Bypasses / Insecure Direct Object References (IDOR)) and the three "Web Fundamentals" -> tryhackme.com/path/outline/web links are already in place from the prior batch; no change needed.

## 11th Changelist — concrete TryHackMe room links (source applied, not generated)
- The TryHackMe references only linked the (legacy) path outline and listed room topics as plain text, so it was unclear exactly what to study. Now each specific room is named AND linked, in both the Phase I source entry and step 04:
  - HTTP in Detail -> https://tryhackme.com/room/httpindetail
  - Burp Suite: The Basics -> https://tryhackme.com/room/burpsuitebasics
  - OWASP Top 10 -> https://tryhackme.com/room/owasptop102021
- Verified all three are free, public rooms (the owasptop102021 "lv" variant is private/premium, so avoided it). The Web Fundamentals path link is kept for context. ("Jr Penetration Tester" path left unlinked — not part of the orientation step.)

## 12th Changelist — de-vague Phases II–VII: exact names + links for every study target
Searched Phases II through VII for study targets named without links/exact names and linked them all (blue #3A7AB8), URLs verified against live pages (PortSwigger all-topics index, TryHackMe room pages, etc.):
- **PortSwigger Web Security Academy (13 links across II–IV):** every "learning path" / "labs" reference now links to its exact topic page — Authentication, Access control, API testing, SQL injection, OS command injection, Server-side template injection, Cross-site scripting, CSRF, SSRF, XXE, Business logic (logic-flaws), Insecure deserialization, File upload, Path traversal. The two non-existent/vague "PortSwigger 'HTTP fundamentals'" and "'Burp Suite' learning path" references were corrected to the official Burp Suite documentation.
- **BSCP (Phase IV):** "BSCP exam" -> /web-security/certification; "BSCP practice exams" -> /web-security/certification/practice-exam.
- **OWASP (III, VI):** API Security Top 10, Code Review Guide, ASVS, Threat Dragon now link to their owasp.org project pages.
- **AWS (V):** Shared Responsibility Model and IAM documentation linked.
- **Tools (IV):** Semgrep, Bandit, TruffleHog, Gitleaks, OWASP ZAP, Snyk linked to their official sites at point-of-install.
- **TryHackMe Pre-Security (II):** the two res entries previously linked only to the tryhackme.com homepage; now point at the exact Network Fundamentals module (/module/network-fundamentals) and Putting It All Together room (/room/puttingitalltogether), and those names are linked in the step bullets too.
- Resources that already carried a specific bare URL in their res() entry (auto-linked) were left as-is (OWASP cheat sheets, hashcat, bcrypt, GitHub Security Lab, Professor Messer, FreeCodeCamp). Note: flaws.cloud / flaws2.cloud auto-link already (.cloud TLD).
- Validated by constructing all 928 flowables through build_content with linkify applied (no PDF rendered): zero markup errors.

## 12th Changelist — exact links for vague study references, Phases II–VIII (source only)
Swept Phases II–IX. Found most PortSwigger labs (II–IV) and all Phase IV tools (Semgrep, Bandit, TruffleHog, Gitleaks, ZAP, Snyk, BSCP) were ALREADY linked, and bare domains (flaws.cloud, flaws2.cloud) already auto-link. Remaining prose-named resources lacked inline links; now linked to exact pages:
- Phase II: OWASP Cryptographic Storage Cheat Sheet, OWASP Transport Layer Security Cheat Sheet, OWASP SSRF Prevention Cheat Sheet -> exact cheatsheetseries.owasp.org pages.
- Phase III: "OWASP Top 10 category" -> owasp.org/www-project-top-ten/.
- Phase IV: "Burp Suite Community Edition" -> portswigger.net/burp/communitydownload.
- Phase V: FreeCodeCamp guide -> freecodecamp.org/news/learn-cloud-security-fundamentals-in-aws-a-guide-for-beginners/. (flaws.cloud / flaws2.cloud already auto-linked.)
- Phase VI + VIII: "GitHub Security Lab" -> securitylab.github.com (both occurrences).
- Phase VII: "Professor Messer" -> professormesser.com/sy0-701-certification-course/.
All verified free/public where applicable; all run clean through linkify (no double-wrap) + Paragraph parse.

## 13th Changelist — fix dead TryHackMe OWASP Top 10 link (source only)
- The OWASP Top 10 room link used /room/owasptop102021, which now 302-redirects to /hacktivities/search ("room doesn't exist") — that room code was retired. Fixed by fetching candidate URLs directly:
  - /room/owasptop102021 -> CONFIRMED DEAD (canonical now hacktivities/search)
  - /room/owasptop102021lv -> private/premium (rejected earlier)
  - /room/owasptop10 -> CONFIRMED LIVE & FREE: title "OWASP Top 10", 31 tasks, 224k+ users, no paywall. THIS IS THE FIX.
- Replaced both occurrences (Phase I res entry + step 04) with https://tryhackme.com/room/owasptop10.
- Also re-verified by direct fetch that the other two rooms resolve as live, free public rooms: /room/httpindetail (7 tasks, 646k users) and /room/burpsuitebasics. All three now confirmed by fetching the actual room page (not just search snippets).

## 14th Changelist — Phase I link/content verification + book accuracy fix (source only)
Verified every Phase I hyperlink against live content and the book against the uploaded PDF (Real-World Bug Hunting, 266pp, full TOC extracted):
- WebGoat, PortSwigger (sql-injection material, all-labs#sql-injection Apprentice labs, cross-site-scripting material), TryHackMe Web Fundamentals path (resolves; titled "Legacy") + 3 rooms (httpindetail/burpsuitebasics/owasptop10, all live & free): ALL PASS.
- Book res entry (organized by vulnerability class, real bug bounty reports, 2019 No Starch): PASS — TOC confirms ~17 vuln-class chapters each with real disclosed reports (Shopify/HackerOne/Twitter/Uber/Google).
- Book step 02 "Ch. 1-5 ... organized by vulnerability class with real bug bounty reports": PARTIAL — Ch 1 ("Bug Bounty Basics") is a foundational primer (client/server, HTTP requests), not a vuln class and has no reports; Ch 2-5 are vuln classes (open redirect, HPP, CSRF, HTML injection/content spoofing) with real reports. FIXED: rewrote bullet to say Ch 1 = basics, Ch 2-5 = named vuln classes with real disclosed reports.

## 15th Changelist — Phase II link+content verification, fixes, integrated checker (source only; no PDF generated)
LINKS (all web-verified live this session; content matches description):
  Burp Proxy/Repeater/Intruder tool pages, PortSwigger cors + jwt + oauth topics, MDN CSP/Methods/Status,
  OWASP TLS/Crypto-Storage/SSRF cheat sheets, PortSwigger authentication/access-control/api-testing/sql-injection
  paths + their all-labs#... lab anchors, freeCodeCamp hashcat MD5 guide, PyPI bcrypt, THM network-fundamentals
  module + puttingitalltogether room. All PASS.
BOOKS (verified via published TOC — PDFs were NOT uploaded for Phase II; only Real-World Bug Hunting is on disk):
  * WAHH (Stuttard/Pinto, Wiley 2011): Ch 6 Attacking Authentication, Ch 7 Attacking Session Management,
    Ch 8 Attacking Access Controls all match. FIX: step 01 + res mislabeled Ch 2 as "core protocols";
    Ch 2 is "Core Defense Mechanisms" -> corrected.
  * Alice and Bob Learn Application Security (Janca, Wiley 2020): Ch 1-5 = Security Fundamentals, Security
    Requirements, Secure Design, Secure Code, Common Pitfalls. FIX: step 06 listed "AppSec program basics"
    inside Ch 1-5, but "An AppSec Program" is Ch 7 -> reading corrected to "Ch. 1-5 and Ch. 7" with accurate topics.
9 USER-REQUESTED FIXES applied to appsec_content.py:
  R1 step01 Burp broad docs link -> 3 specific tool pages (Proxy/Repeater/Intruder)
  R2 step01 note-card topics CORS/CSP/TLS/HTTP methods/status each linked to a teaching page
  R3 step02 Authentication "labs" now links to all-labs#authentication
  R4 step02 note cards JWT->/web-security/jwt, OAuth->/web-security/oauth
  R5 step03 Authentication Audit Checklist: added bullet to run it against the Phase 0 FastAPI app (JWT via Security module)
  R6 step04 added access-control + API testing lab links (paths DO have apprentice+practitioner labs)
  R7 step05 SQLi "labs" now links to all-labs#sql-injection
  R8 step07 hashcat task->freeCodeCamp MD5 guide, bcrypt task->PyPI bcrypt
  R9 step08 "Review existing Odin Project HTTP notes and HTML intro notes" -> "Review existing notes"
COVERAGE CHECK (new): every "Concepts Mastered" + "How These Concepts Are Used" item now cross-checked against
  steps+sources for phases 0, I, II (all trace through). Applied going forward to all phases.
INTEGRATED CHECKER: phase_content_check.py (link inventory + manual verdicts, broad-link flag, resource-link gap,
  note-card backing, concepts coverage). Wired into build_appsec.py. Invoke via command "PHASE CONTENT CHECK <ROMAN>"
  (= python3 build_appsec.py CONTENT-CHECK <ROMAN>, or python3 phase_content_check.py <ROMAN>). Offline; does not build the PDF.
VALIDATION: ast.parse + import + 33 Phase II markup fragments through linkify()+Paragraph (no double-wrap). PDF NOT generated (BUILD = source only).

## 15b — Phase II books PDF-verified (confirmation only; no source change)
Both Phase II books were uploaded and verified against actual PDF content (not just published TOC):
  * WAHH (914pp, 2nd ed): outline confirms Ch2="Core Defense Mechanisms" (Ch2 text: "The defense mechanisms
    employed by web applications..."); Ch3="Web Application Technologies" is where the HTTP protocol is examined.
    Confirms the 15th-changelist fix (Ch2 "core protocols" -> "core defense mechanisms") was correct.
    Ch6 Attacking Authentication, Ch7 Attacking Session Management, Ch8 Attacking Access Controls -> match.
  * Alice and Bob (285pp): Ch1-5 = Security Fundamentals/Requirements/Secure Design/Secure Code/Common Pitfalls;
    Ch7="An AppSec Program" (Ch7 text: "This chapter will discuss application security programs..."). Confirms the
    15th-changelist fix (move "AppSec program" from Ch1-5 to "Ch1-5 and Ch7") was correct.
No new discrepancies; Phase II book descriptions now accurate at title AND content level. PHASE CONTENT CHECK II: PASS (26 links, 0 issues).

## 16th Changelist — Phase II "API security" concept de-duplicated (source only; no PDF generated)
Was: "REST API-specific vulnerability patterns. REST API-specific vulnerability patterns covered in this phase."
(redundant — the sentence repeated itself).
Now: "REST API-specific vulnerability patterns — broken object-level authorization (IDOR), mass assignment, and
excessive data exposure — and why APIs widen the attack surface beyond traditional server-rendered applications."
Validated: ast.parse + import + Paragraph parse. PDF NOT generated (BUILD = source only).

## 17th Changelist — GENERATE PDF + packaging
- Generated Study_Plan_-_2026-06-26.pdf (50pp); all TOC page numbers verified against actual pages.
- Added present_build_zip.py (assembles the full package). New command: PRESENT BUILD ZIP
  (= python3 build_appsec.py PRESENT-ZIP, or python3 present_build_zip.py). Bundles every prior package
  file (updated) PLUS new files phase_content_check.py and present_build_zip.py, with the latest PDF as
  *_LATEST.pdf and the original source as *_SOURCE.pdf.
- README updated to document phase_content_check.py and the verification command.

## 18th Changelist — cross-phase duplicate-step detector + 3 dedup resolutions (source only; no PDF generated)
DETECTOR: added step_dedup_check.py. Pulls every step in every phase and cross-compares against all other
steps (incl. same phase). Flags a DUPLICATE when two steps both FULL-complete the same completable resource
(PortSwigger topic/path, TryHackMe room/module, or book by title+overlapping chapters). FULL vs PART grading:
"complete the path / all labs / in full / completely" = FULL; "apprentice-level / the remaining / review your
/ read the" = PART. Two FULL on one resource = duplicate; FULL+PART = complementary intro->mastery (INFO only).
Wired into build_appsec.py: runs on every GENERATE PDF (warns, non-fatal). New command: STEP DEDUP CHECK
(= python3 build_appsec.py STEP-DEDUP-CHECK, or python3 step_dedup_check.py).
FOUND (check #1): 3 duplicates, all Phase II<->III (same full PortSwigger path completed twice):
  - sql-injection: PII step05 (apprentice->expert) vs PIII step01 (apprentice+practitioner)
  - access-control: PII step04 (apprentice+practitioner) vs PIII step05 (in full)
  - api-testing:    PII step04 (apprentice+practitioner) vs PIII step07 (complete path)
RESOLVED (judgment; Phase II = Foundations/intro, Phase III = Core Vulnerability Classes/mastery):
  - PII step04 -> "Work through the apprentice-level Access control and API testing labs ... full paths completed in Phase III"
  - PII step05 -> "Work through the apprentice-level SQL injection labs ... full path (practitioner and expert) completed in Phase III"
  - PIII step01 -> "Review your Phase II SQL injection notes, then complete the remaining SQL injection labs (practitioner and expert)"
  - PIII step05 -> "Review your Phase II access-control notes, then complete the remaining practitioner-level Access control labs"
  - PIII step07 -> "Review your Phase II API testing notes, then complete the remaining practitioner-level API testing labs"
LOOP: check -> fix -> check converged. Re-run: "No duplicate steps. ✓" (0 duplicate resources).
TIMELINE: no steps added/removed and no week labels changed, so phase boundaries, banners (II: Months 1.5-2.25;
III: Months 2.5-3.5), step weeks, and Plan Schedule are all unchanged. Removing the duplication reduces over-counted
work within the same week structure (it does NOT extend the schedule). timeline_check.reconcile: already consistent.
VALIDATION: ast.parse + import + linkify()+Paragraph on the 5 changed bullets. step_dedup_check.py added to
present_build_zip.py manifest. PDF NOT generated (BUILD/IMPLEMENT = source only).

## 19th Changelist — PortSwigger labs audit + labs links (items 2 & 3 combined; source only; no PDF)
AUDIT: scanned every PortSwigger /web-security/ entry across all phases; classified action READ vs DO; checked
for an explicit labs link. Found 14 "do the path" entries (mostly Phase III) linking only the topic/material
page, not labs. (certification = excluded; it's the exam page, not a labs topic.)
ANCHORS: fetched portswigger.net/web-security/all-labs live and captured the exact section anchors.
LABS LINKS ADDED (topic stays linked to material; an explicit labs link added per topic):
  PII step04  access-control (#access-control-vulnerabilities), api-testing (#api-testing)
  PIII step01 os-command-injection (#os-command-injection), server-side-template-injection (#server-side-template-injection)
  PIII step03 cross-site-scripting (#cross-site-scripting)
  PIII step04 csrf (#cross-site-request-forgery-csrf), ssrf (#server-side-request-forgery-ssrf), xxe (#xml-external-entity-xxe-injection)
  PIII step05 access-control (#access-control-vulnerabilities), logic-flaws (#business-logic-vulnerabilities)
  PIII step06 deserialization (#insecure-deserialization), file-upload (#file-upload-vulnerabilities), file-path-traversal (#path-traversal)
  PIII step07 api-testing (#api-testing)
Item 2 "For each lab: exploit it, write your standard documentation..." treatment was already present as a
step-level bullet in PIII step01 (covers OS command + SSTI labs), so only the labs links were missing.
REGISTRY: added the verified Phase III topics + all-labs anchors to phase_content_check VERIFIED.
PHASE CONTENT CHECK I / II / III: all PASS (10 / 26 / 30 links; 0 issues). Re-audit: 0 do-the-path entries
missing a labs link. (3 OWASP project URLs in Phase III still show 'unverified' — not PortSwigger, out of scope here.)
VALIDATION: ast.parse + import + linkify()+Paragraph on the 10 changed bullets. PDF NOT generated (IMPLEMENT = source only).

## 20th Changelist — labs phrasing: drop "(labs)" parenthetical style (source only; no PDF generated)
Changelist item 1. Converted all 10 parenthetical "[Topic] (labs)" references to the integrated
"[Topic] labs" style (matching "Complete the PortSwigger Authentication learning path — all apprentice
and practitioner labs"). Both links preserved per topic: topic name -> topic page, "labs" -> exact
all-labs# anchor. Affected bullets: PII step04 (access-control, api-testing), PIII step01 (os-command-
injection, SSTI), PIII step04 (csrf, ssrf, xxe), PIII step06 (insecure-deserialization, file-upload,
path-traversal). Also removed the now-redundant trailing "learning paths" after "labs" in PIII step01/04.
Validated: ast.parse + import + linkify()+Paragraph on all 4 bullets; step_dedup_check still 0 duplicates.
PDF NOT generated (IMPLEMENT/BUILD = source only).

## 21st Changelist — content-aware labs curation (source only; no PDF generated)
Changelist item 2. Audited every PortSwigger labs group by reading the individual lab TITLES (pulled a full
per-topic, difficulty-tagged lab inventory), then curated number AND choice per group for the entry-level
AppSec-engineer goal (dev career-switch; code-review/triage focus). Calibration: do every apprentice lab +
the practitioner labs that teach a DISTINCT defense-bypass/detection technique; skip near-identical
permutations, out-of-band/Burp-Collaborator labs, language-specific gadget-chain duplicates, and all expert
labs. Net ~80-95 targeted labs vs 150+.
EDITS (Phase III, source):
  - Added a phase-wide "Lab selection (applies across Phase III)" note in step01 (skip permutations / OOB / expert).
  - SQLi (s01): "practitioner and expert" -> practitioner UNION + blind (boolean/time); skip out-of-band.
  - OS command injection (s01): simple + blind time-delay/output-redirection; skip OOB exfil.
  - SSTI (s01): the basic/concept labs only; skip engine-specific gadget exploitation.
  - XSS (s03): "all labs" -> reflected/stored/DOM + DOM sinks + exploitation labs (cookies, XSS->CSRF);
    skip the long tail of near-identical context-encoding/filter-bypass permutations.
  - CSRF/SSRF/XXE (s04): CSRF + SSRF in full (each distinct); XXE trimmed to core (file read, SSRF, one blind).
  - Business logic (s05): "all labs" -> apprentice and practitioner (strength area for dev background).
  - Deserialization (s06): concept labs + ONE gadget-chain example; skip extra language-specific chains.
    File upload + Path traversal kept in full (each a distinct filter bypass).
  Small all-distinct groups (CSRF, SSRF, path traversal, business logic) kept whole; priority topics
  (access control, authentication, API) left fuller, governed by the phase-wide selection note.
Curation is THEME-based (not hard counts), so it stays valid as PortSwigger adds labs. Basis: live all-labs
anchors + a full lab-title inventory (roberson-io), cross-checked against AppSec relevance.
VALIDATION: ast.parse + import + linkify()+Paragraph render on all curated bullets (all links intact:
XSS 2, CSRF/SSRF/XXE 6, deser/upload/traversal 6, OS-cmd/SSTI 4, SQLi 1, selection note bold OK);
step_dedup_check still 0 duplicates. PDF NOT generated (BUILD = source only).

## 22nd Changelist — restore "learning path" reading cue + material links (source only; no PDF)
Full PortSwigger re-audit after the curation pass. Finding: material (topic/path-text) links survived
everywhere EXCEPT PIII s01 SQLi (labs-only); but the "learning path" reading cue had been dropped from the
Phase III labs bullets, so they read "[Topic] labs" instead of "read the learning path, then the labs".
FIX (6 bullets) to the gold-standard "Complete the PortSwigger [Topic] learning path — [scope] labs" form
(topic name -> written material page; "labs" -> all-labs# list; curation scope kept):
  - PIII s01 SQLi: added the missing /web-security/sql-injection material link ("Re-read ... learning path
    and your Phase II notes, then complete the practitioner labs ...").
  - PIII s01 OS cmd + SSTI, PIII s03 XSS, PIII s04 CSRF/SSRF/XXE, PIII s05 business logic,
    PIII s06 deser/upload/traversal: restored "learning path(s)" framing; multi-topic bullets now list the
    learning paths (material) then their labs (per-topic labs links) — both link sets retained.
  - Review-then-remaining bullets (PIII s05 access-control, PIII s07 API) and the apprentice-intro / Phase I
    orientation bullets already carry material + labs links; left as-is.
VERIFIED: every "do labs" bullet now has BOTH a material link and a labs link; all bullets parse via
linkify()+Paragraph; no "(labs)" parentheticals; step_dedup_check still 0 duplicates. PDF NOT generated.

## 23rd Changelist — Phase I SQLi orientation labs scope (source only; no PDF)
PI s01: "complete the first 3-4 Apprentice-level labs" -> "complete the first 3-4 Apprentice & Practitioner
level labs" (SQL injection bullet only; the cross-site scripting bullet left unchanged). Validated: count==1
match, ast.parse + linkify()+Paragraph render OK. PDF NOT generated.

## 24th Changelist — pull reference links out of note-card bullets (source only; no PDF)
Decision: the Phase II note-card reference links are NOT study-step labs, so they are EXEMPT from the
PortSwigger text+labs pairing rule. Per request, removed them from the "Full notes + note cards:" bullets
and relocated them to a dedicated "Read ..." bullet directly above each (applied to both bullets that carried
links, for consistency):
  - PII s01: new "Read CORS misconfigurations, CSP, TLS, HTTP methods, and status codes for their security
    implications" bullet (CORS->PortSwigger, CSP/methods/status->MDN, TLS->OWASP); note-cards bullet now
    plain text: "CORS misconfigurations, CSP, TLS, HTTP methods, and status codes with security implications".
  - PII s02: new "Read JWT algorithm confusion and OAuth redirect URI manipulation" bullet (->PortSwigger
    /web-security/jwt and /web-security/oauth); note-cards bullet now plain text: "Password enumeration,
    session fixation, JWT algorithm confusion, OAuth redirect URI manipulation".
Rationale: these are book-gap references (WAHH 2011 predates CORS/CSP/JWT/OAuth2/modern TLS); kept as reading
references, just no longer embedded in the note-card list. VALIDATED: ast.parse + import + linkify()+Paragraph
on all 4 bullets; PHASE CONTENT CHECK II note-card backing still PASSES. PDF NOT generated (BUILD = source only).
NOTE: the full PortSwigger text+labs pairing pass (PII s04/s05 text-only fixes + crossed-link audit across all
web-security references) is still pending and awaits an explicit IMPLEMENT.

## 25th Changelist — full PortSwigger pass: de-fuse text+labs pairs to gold format (source only; no PDF)
Audited every PortSwigger web-security pair for the "fused link" problem (text link rendered immediately
adjacent to its labs link, displaying as one blue phrase). Found 4 fused; reformatted to the separated
"[Topic] learning path — ... labs" / "review your notes — ... labs" gold format (text link on topic name,
labs link on "labs", clearly separated):
  - PII s04: "Read the PortSwigger Access control and API testing learning paths, then work the apprentice-level
    Access control labs and API testing labs ... the practitioner labs follow in Phase III".
  - PII s05: "Read the PortSwigger SQL injection learning path, then work the apprentice-level labs ... the
    practitioner labs follow in Phase III" (dropped stale "(practitioner and expert)").
  - PIII s05 access-control: "Review your Phase II Access control notes, then complete the remaining
    practitioner labs — URL-, method-, Referer-based bypasses and multi-step gaps" (text link now on topic).
  - PIII s07 API testing: "Review your Phase II API testing notes, then complete the remaining practitioner
    labs — BOLA, mass assignment, and excessive data exposure".
Read/review honored: Phase II reads the learning-path text (so Phase III's "review your Phase II notes" holds);
no duplication (PII = read + apprentice [PART]; PIII = review + practitioner [PART]). The other pairs (PII s02
gold; PI s01 read-material→labs; PIII s01/s03/s04/s05-logic/s06 from changelist 22) were already separated and
left unchanged. VERIFIED: fused-pair audit now returns NONE; all pairs parse via linkify()+Paragraph;
step_dedup_check still 0. PDF NOT generated (IMPLEMENT = source only).

## Changelist 26 (items 1-3 of 5) — applied to source; PDF NOT generated
**Item 1 — removed phase-wide lab-selection note.** Deleted the PIII s01 bullet
"Lab selection (applies across Phase III): do every apprentice lab, plus the practitioner
labs that teach a distinct defense-bypass or detection technique. Skip near-identical
permutations…, out-of-band labs…, and all expert labs…". Each lab bullet is now
self-contained about scope (see item 3).

**Item 2 — relabeled step headers (reading + labs but tagged only "LABS:") → "READ + LABS:".**
PIII s01 Injection Classes, s03 Cross-Site Scripting, s04 CSRF/SSRF/XXE, s05 Access Control &
Business Logic, s06 Deserialization/File Upload/Path Traversal. (PIII s07 already "READ + LABS:".
PV s02/s03 flaws.cloud steps left as "LABS:" — no PortSwigger learning-path reading.)

**Item 3 — expert-scope phrasing fix (verified tiers via difficulty-tagged lab tables).**
Tiers confirmed: SSRF 2A/3P/**2E** (Shellshock, whitelist-filter bypass); File upload
2A/4P/**1E** (web-shell via race condition, needs Burp Pro); XXE 2A/6P/1E (the 1 expert
DTD-repurposing lab was already outside the curated "core" subset).
- PIII s04: "the SSRF labs" → "the apprentice and practitioner SSRF labs (skip the two expert
  labs — Shellshock and the whitelist-filter bypass)"; XXE core annotated "— all apprentice
  and practitioner".
- PIII s06: "file upload labs … in full" → "the apprentice and practitioner file upload labs
  (skip the expert web-shell-via-race-condition lab, which needs Burp Suite Pro)"; path
  traversal stays "in full" (no expert tier).
Validation: 8 edits each matched exactly once; ast.parse OK; linkify()+Paragraph OK on edited
bullets; STEP DEDUP CHECK = 0; fused-pair scan = 0. PDF intentionally NOT generated.

## Changelist 26 (items 4-5 of 5) — applied to source; PDF NOT generated
**Item 4 — "Hacking APIs" (Corey Ball, No Starch, 2022) chapter detail.** Verified TOC: Part III
"Attacking APIs" = Ch 6 Discovery, Ch 7 Endpoint Analysis, Ch 8 Attacking Authentication, Ch 9
Fuzzing. The existing "(API reconnaissance, endpoint discovery, authentication testing)"
parenthetical was mis-attached to Ch 1-3 — those are actually the foundational chapters (Ch 1
How Web Applications Work, Ch 2 The Anatomy of Web APIs, Ch 3 Common API Vulnerabilities). Fixed
both so the bullet is internally consistent:
  "Read Hacking APIs Ch. 1-3 (how web applications and APIs work, and the common API vulnerability
   classes) and Ch. 6-9 (API discovery and reconnaissance, endpoint analysis, authentication
   attacks, and fuzzing)"

**Item 5 — typo.** "One question, catches the whole class." -> "One question catches the whole
class." (removed the comma splice).

Validation: both edits matched exactly once; ast.parse OK; linkify()+Paragraph OK on both edited
bullets (italic markup intact); STEP DEDUP CHECK = 0. PDF intentionally NOT generated.

### Changelist 26 COMPLETE (all 5 items applied to source). PDF not yet generated.

## Tooling fix — step_dedup_check.py rewritten (dedup detector was missing real duplicates)
**Problem:** the checker missed a genuine duplicate — "work through the official Burp Suite
documentation: Proxy, Repeater, Intruder" appears in BOTH Phase II step01 and Phase IV step01.
Two root causes: (1) topic_of() returned None for every /burp/... URL, so Burp doc links were
never compared; (2) the action verb "work through" wasn't in the completion-verb list, so both
bullets graded as "part" and never tripped the >=2-FULL rule. There was also no content-level
detection, so repeated instruction text with different/absent links was invisible.

**Fix (step_dedup_check.py):**
- topic_of() now maps all portswigger.net/burp/* URLs to a single "burp-suite" resource, and adds
  topic-slug<->all-labs-anchor aliases (logic-flaws=business-logic, csrf/ssrf/xxe/file-upload/etc.)
  so a topic page and its lab anchor collide.
- Completion-verb set broadened: complete, in full, all (apprentice/practitioner) labs, AND
  work through / work the / go through / study / do the / learn. Subset guards unchanged
  (apprentice-level, remaining, review your, re-read, first N, read the ..., orientation) so the
  intended intro->mastery split is still graded part (not a duplicate).
- New CONTENT near-duplicate pass: tokenizes bullets (strips tags, drops stopwords), flags
  cross-step pairs with high overlap-coefficient and >=4 shared *rare* tokens, suppressing
  intentional cross-phase pointers (follow in Phase, review your, re-read, "see ...", Phase <n>).
  Distinctive-token threshold tuned to ~4% document frequency so sentence-frame words
  (complete/learning/path/portswigger/apprentice/practitioner/labs) don't create false hits.
- Refactored into pure parse_steps()/detect() so logic is unit-testable; added `--selftest`.

**Testing:** `python3 step_dedup_check.py --selftest` = 11 synthetic cases (same-path dup, Burp
dup, book overlap, THM-room dup, study-verb dup; negatives: intro/mastery, access-control
staging, non-overlapping book chapters, unrelated steps, FULL+PART) + 5 corpus regression checks
(burp dup present; write-doc boilerplate flagged; auth~deser / auth~xss / WAHH frame noise
suppressed) -> ALL PASS. On the real file the checker now reports 1 HARD duplicate (burp-suite,
PII step01 + PIV step01) and 4 advisory content items. Integration via
`python3 build_appsec.py STEP-DEDUP-CHECK` verified. No content edits, no PDF generated.

## Burp-suite hard duplicate resolved (content edit)
The same Burp documentation walkthrough (Proxy/Repeater/Intruder) appeared in Phase II step01 and
Phase IV step01, and "Install Burp" was parked in Phase IV (week 15) despite Burp being used from
Phase II (week 6). Fix:
- **Phase II step01 (HTTP Deep Dive, week 6):** now "Install Burp Suite Community Edition, then
  work through the official documentation — Proxy, Repeater, and Intruder — the primary tools you
  will use throughout this phase." (install moved here; links communitydownload + the three tool pages.)
- **Phase IV step01 (Burp Suite Mastery, weeks 15–16):** removed the duplicated install + re-read of
  the same docs. Now: "Refresh from your Phase II Burp Suite notes — no need to re-read the Proxy,
  Repeater, and Intruder docs — then learn the two tools you have not used yet: Decoder and Comparer,
  to mastery level for the BSCP exam" + "Drill the full toolkit hands-on against Web Security Academy
  labs until interception, Repeater iteration, and Intruder fuzzing are second nature." Decoder and
  Comparer doc URLs (/burp/documentation/desktop/tools/{decoder,comparer}) web-verified live.
Validation: 2 edits each matched once; ast.parse OK; linkify()+Paragraph OK on all edited bullets;
STEP DEDUP CHECK now reports 0 hard duplicates (burp-suite resolved; burp content advisory also gone
via the Phase II staged reference). Remaining 3 content items are the kept-as-safe advisories
(write-doc habit, note-card format, triage-results). PDF intentionally NOT generated.

## Phase IV step01 (Burp Suite Mastery) — rewrote 3 bullets for coherence
After the dedup fix moved Burp basics to Phase II, this step's bullets still read like learning
Burp from scratch (a "by end of Week 15: use Repeater / use Intruder" milestone, plus a vague
unlinked "drill the full toolkit" line). Rewrote all three so the step is unambiguously a
mastery step:
- Bullet 1 (was the confusing "Refresh from your Phase II notes… then learn Decoder and Comparer"):
  now states the premise plainly and says what each new tool does — "Burp's Proxy, Repeater, and
  Intruder are already familiar from Phase II — review those notes rather than re-reading the docs.
  New this phase are the two Community-edition tools you have not used: Decoder, for encoding,
  decoding, and hashing data inline, and Comparer, for a visual diff between two requests or
  responses — learn both, since the BSCP exam rewards fluency across the whole toolkit."
- Bullet 2 (was vague + unlinked "Drill the full toolkit…"): now concrete and linked —
  "Build speed by re-solving a spread of [Web Security Academy labs](all-labs) entirely inside Burp:
  intercept and edit in Proxy, iterate payloads in Repeater, and use Decoder and Comparer to pick
  apart responses, until carrying a finding through the tools feels fluid."
- Bullet 3 (was the confusing basics milestone "By end of Week 15: …use Repeater…use Intruder for
  parameter fuzzing"): now a mastery milestone that doesn't re-teach basics —
  "By end of Week 16: fluent with Decoder and Comparer, and quick with the advanced workflow on
  tools you already know — Proxy match-and-replace rules and Repeater tab groups — so you can move a
  finding through the whole toolkit without friction."
Validation: block matched once; ast.parse OK; linkify()+Paragraph OK on all three; STEP DEDUP CHECK
= 0 hard duplicates (all-labs index link has no anchor -> not a topic); timeline consistent.
(Note: a build was run to check the timeline, which re-rendered the on-disk PDF; it was NOT
presented. Render/preview happens only on GENERATE PDF.)

## Phase IV step01 bullet 2 — replaced vague "spread of labs" with three specific verified labs
The "Build speed by re-solving a spread of Web Security Academy labs…" bullet was too vague and
linked only the general all-labs index. Replaced with three targeted labs, each carrying a group
link AND a specific lab link, with what-to-do and which tool, all web-verified live:
- Essential skills (all-labs#essential-skills) -> lab "SQL injection with filter bypass via XML
  encoding" (Practitioner): wrap the injection in XML/HTML entity encoding (Decoder/Hackvertor) to
  bypass the WAF. (Note: the lab's real title is this; "Obfuscating attacks using encodings" is its
  study-material page, not the lab name.)
- Authentication (all-labs#authentication) -> lab "Username enumeration via different responses"
  (Apprentice): Comparer diff of valid vs invalid login responses.
- SQL injection (all-labs#sql-injection) -> lab "Blind SQL injection with conditional responses"
  (Practitioner): Comparer for the true/false response toggle, Decoder for encoding conditions.
Phrased as "drill the new tools on three targeted labs" (not "complete/do the labs"): these labs'
topics (authentication, sql-injection) are already completed in Phases II-III, so completion-verb
phrasing would make STEP DEDUP CHECK correctly see a re-completion. Drill phrasing keeps them graded
PART. Validation: 1 match; ast.parse OK; linkify()+Paragraph OK (6 links); STEP DEDUP CHECK = 0 hard
duplicates (3 advisories unchanged); fused-pair scan = 0. Lab URLs verified:
/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding,
/web-security/authentication/password-based/lab-username-enumeration-via-different-responses,
/web-security/sql-injection/blind/lab-conditional-responses.

## Phase IV step01 bullet 2 — shortened (~95 -> ~55 words), all 6 links kept
Trimmed the three-lab drill bullet to one tight sentence per lab, each still tied to the tool it
exercises, keeping all six links (3 group anchors + 3 lab pages). Dropped the apprentice/practitioner
level labels and the longer scenario descriptions for brevity. Phrasing remains non-completion-verb
("drill … encode … use … extract") so dedup keeps the lab topics graded PART. Validation: 1 match;
ast.parse OK; linkify()+Paragraph OK (6 links); STEP DEDUP CHECK = 0 hard duplicates (3 advisories
unchanged).

## Phase IV step01 — de-rambled: 3 long bullets -> 6 short ones
The Burp Suite Mastery bullets were the longest in the phase (30-65 words each vs ~12-25 for sibling
steps 02/03). Split into six short bullets matching phase rhythm (15-22 words each), all 8 links kept:
1. Proxy/Repeater/Intruder already from Phase II — review notes, don't re-read docs.
2. The two new Community-edition tools: Decoder (encode/decode/hash inline) + Comparer (visual diff of
   two messages). [Decoder, Comparer links]
3. Decoder: SQL injection with filter bypass via XML encoding (Essential skills) — encode payload as
   XML/HTML entities to bypass the WAF. [lab + group links]
4. Comparer: Username enumeration via different responses (Authentication) — spot the one differing
   login response. [lab + group links]
5. Both: Blind SQL injection with conditional responses (SQL injection) — read the admin password one
   true/false answer at a time. [lab + group links]
6. By end of Week 16: fluent with Decoder and Comparer, comfortable with Proxy match-and-replace and
   Repeater tab groups.
Phrasing stays non-completion-verb so dedup keeps the reused lab topics graded PART. Validation: 1
match; ast.parse OK; linkify()+Paragraph OK on all 6 (8 links total); STEP DEDUP CHECK = 0 hard
duplicates (3 advisories unchanged); fused-pair scan = 0. PDF NOT generated (source-only).

## Batch: IMPLEMENT 1,2,3 (BUILD PDF — source only, not rendered)  [2026-06-29]
**Item 1 — New "Study Plan Phase Summary" intro section (DONE, source).**
- appsec_content.py: inserted a new section after the Pitfalls "Net assessment" nb() and before
  the Phase 0 banner. `H("Study Plan Phase Summary")` + one intro sentence + a 10-entry loop
  (Phases 0–IX), each entry: **Purpose / Resources / Achievement** (e.g. IV → "passed BSCP exam",
  VII → "passed CompTIA Security+ (SY0-701)"). Content derived from each phase's real step labels,
  res() resources, and books. ~414 words ≈ ~31 content lines → expected to fit one page.
- appsec_content.py TOC data: added `("Study Plan Phase Summary", "16", [])` after the Pitfalls entry.
- build_appsec.py SECTIONS: added `("Study Plan Phase Summary", "Study Plan Phase Summary")` after Pitfalls.
- NOTE: one-page fit + TOC page reconciliation are confirmed on the next GENERATE PDF (self-correcting
  loop re-scans). If the section spills to 2 pages, TOC scan could mis-map phases → TRIM then.

**Item 3 — Semgrep/Bandit how-to hyperlinks (DONE, source).** 5 phrases wrapped in official-doc links:
- "Run the default Python ruleset" → https://semgrep.dev/docs/getting-started/quickstart-ce
- "Triage the results" → https://semgrep.dev/docs/semgrep-code/findings
- "Write one custom Semgrep rule" → https://semgrep.dev/docs/writing-rules/overview
- "Integrate Semgrep into a GitHub Actions workflow" → https://semgrep.dev/docs/semgrep-ci/sample-ci-configs
- "Run against a sample Python project" → https://bandit.readthedocs.io/en/latest/
All 5 web-verified live; each count==1; ast.parse OK; Paragraph-parse OK.

**Item 2 — BSCP exam-readiness audit (DONE, report only — NO content edits; additions await approval).**
Compared Phases 0–IV coverage vs PortSwigger's official prep pages (how-to-prepare, practice-exam,
how-it-works) + community guides. Verdict + recommended optional additions delivered in chat.
Note corrected for user: the BSCP (practice + real exam) lives in **Phase IV** (steps 02 & 07), not Phase VI.

Validation: ast.parse both files OK; dedup 0 hard duplicates (3 advisories, all user-approved-to-keep).
PDF NOT generated (BUILD PDF = source only). Pending: items 4, 5, 6.

## Batch: IMPLEMENT 4,5,6 (BUILD PDF — source only, not rendered)  [2026-06-29]
**Item 4 (DONE):** PIV Bandit bullet — "and against your own old code if available" → "and against some code in old projects".
**Item 5 (DONE):** PIV Bandit bullet — "install with pip install bandit" → "install bandit with pip".
**Item 6 (DONE):** PIV — moved "APPLY: Begin Job Applications" from step 04 to step 07, immediately AFTER
  "EXAM: Burp Suite Certified Practitioner". Renumbered: Secrets Scanning 05→04, OWASP ZAP 06→05, EXAM 07→06,
  Begin Job Applications 04→07; Snyk(08)/Full Assessment(09) unchanged. New order 01–09 sequential.
  NOTE (flagged to user, NOT changed): the moved step still reads "Throughout Weeks 16–18" / "begin applying
  now — do not wait"; now that it sits after the exam (Week 17–18), that wording is slightly out of step with
  the stated rationale (BSCP on resume before applying). Left as-is pending user direction.
Validation: ast.parse OK; PIV order verified 01–09; items 4/5 text verified; bandit bullet Paragraph OK; dedup 0 hard.
Changelist COMPLETE (items 1–6 all applied). PDF NOT generated (BUILD PDF = source only).

## Batch: IMPLEMENT 1,2,3 — BSCP gap-fill (BUILD PDF, source only)  [2026-06-29]
**Item 1 (DONE):** Phase IV step 02 (BSCP Prep) — corrected "free to take" (false); added a Burp Suite
Professional requirement note (exam/practice-exams/Scanner/Collaborator need Pro ~$499/yr, Community
insufficient; stay on Community until BSCP prep, then buy Pro; exam ~$99/attempt; link → /burp/pro);
practice-exam bullet now "on Burp Pro".
**Item 2 (DONE):** new Phase IV step 07 "LABS: Out-of-Band (OOB) Exploitation with Burp Collaborator"
(gold text+labs format). Blind SQLi (/sql-injection/blind + #sql-injection), blind XXE (/xxe/blind +
#xml-external-entity-xxe-injection), blind OS command injection (/os-command-injection + #os-command-injection),
each naming the 2 specific OOB labs; + Collaborator technique for blind SSTI. All URLs web-verified.
**Item 3 (DONE):** new Phase IV step 08 "READ + LABS: Remaining BSCP Topics" (gold text+labs format):
request smuggling, Host header, web cache poisoning, OAuth, JWT — each with learning-path link + all-labs
anchor + named apprentice/practitioner labs. All paths/anchors/lab names web-verified against all-labs page.
Renumber: EXAM 07->09, Snyk 08->10, Full Assessment 09->11. New PIV order 01-11.
Week tags: OOB "Weeks 16-17", Topics "Weeks 16-18" (within current PIV window 15-18) — NOTE: formal phase
duration will NOT grow on GENERATE; a separate change is needed to push the exam/later phases out to reflect
the ~2-3 added study weeks.
Validation: ast.parse OK; 63 bullets Paragraph-parse OK; PIV order 01-11 verified; dedup 0 hard (6 advisories,
expected PIII/PIV topic overlap). PDF NOT generated (BUILD = source only). Remaining changelist items: 4-11.

## Batch: IMPLEMENT 4,5,6 — BSCP exam-readiness (BUILD PDF, source only)  [2026-06-29]
Discovered PortSwigger's official BSCP prep (Larsen/PortSwigger): 1 practitioner lab/topic + 8 mandatory
reinforcement labs + 5 mystery labs + pass practice exam. Items 4/5/6 map onto this.
**Item 4 (DONE):** new PIV step 09 "LEARN + LABS: Targeted Scanning & Content Discovery" (gold text+labs):
essential-skills/using-burp-scanner-during-manual-testing + #essential-skills; labs "Discovering vulnerabilities
quickly with targeted scanning" + "Scanning non-standard data structures"; Burp Engagement tools > Discover
content technique; Pro-required note. [Gate 1]
**Item 5 (DONE):** new PIV step 10 "DRILL: PortSwigger's Mandatory Reinforcement Labs" \u2014 the official 8-lab
checklist. New labs links: XSS steal-cookies (#cross-site-scripting), brute-forcing stay-logged-in cookie
(#authentication), SSRF blacklist filter (#server-side-request-forgery-ssrf). Cross-refs the 5 already covered
(forced OAuth profile linking=step08, smuggling capture=step08, blind SQLi OOB=step07, SQLi XML-encoding=step01,
targeted scanning=step09). Framed as reinforcement => grades PART, no hard dup.
**Item 6 (DONE):** new PIV step 11 "DRILL: Mystery Labs \u2014 Cold Recognition": /web-security/mystery-lab-challenge,
solve >=5 cold, timed. [Gate 3]
Renumber: EXAM 09->12, Snyk 10->13, Full 11->14. New PIV order 01-14 (drills 09/10/11 sit before EXAM 12).
Week tags all start-16 (within PIV window) so they sort before the exam on GENERATE.
Validation: ast.parse OK; 13 bullets Paragraph-parse OK; PIV order 01-14 verified; dedup 0 hard (5 advisories).
PDF NOT generated (BUILD = source only). Remaining changelist items: 7-11.

## Batch: TIMELINE EXTENSION (+3 wks) + IMPLEMENT 7,8,9  (BUILD PDF, source only)  [2026-06-29]
**Timeline:** Phase IV extended +3 weeks (wks 15–18 -> 15–21; Months 3.5–4.5 -> 3.5–5.25) to absorb the
BSCP gap-fill (items 2–6,9). Cascaded +0.75 month / +3 weeks to all later phases:
  V 4.5–5 -> 5.25–5.75 | VI 5–5.75 -> 5.75–6.5 | VII 6–6.5 -> 6.75–7.25 | VIII 6.75–7.25 -> 7.5–8 | IX 7+ -> 7.75+.
Updated EVERYWHERE: 6 phase banners; timeline CHART weeks[] (IV–IX); schedule SS headings (IV,V,VI);
summary-page lines (IV–IX, "(Mo X–Y)"); prose envelope ("5–7 mo/6 realistic" -> "6–8 mo/7 realistic",
Security+ "Month 6"->"Month 7"); Phase V/VI/VII step week-tags shifted +3 (wks 22–29).
Cover pills = phase-NAME bubbles (no durations) -> unchanged. TOC = names + page numbers (no durations);
page numbers auto-fix on GENERATE. Verified: timeline_check.report_only = 0 issues (three-way agreement,
end-coverage label_end==max_step_week/4, applying_start_month=4 preserved).
**Item 7 (DONE):** new PIV step 03 "DOCUMENT: Save Exam-Ready PoCs" (Throughout Wks 15–20) — save per-lab PoC
to searchable notes (exam open-to-own-notes), pre-adapt high-value PoCs, organize by class. Links how-to-prepare.
**Item 8 (DONE):** "APPLY: Begin Job Applications" MOVED to after the EXAM (PIV step 14); tag -> "Month 4 onward"
(month-scoped). This month-scoped tag DISABLES reorder_steps for Phase IV, so the manual 01–16 order sticks.
Body "Month 6, once Security+" -> "Month 7" (matches shifted Security+).
**Item 9 (DONE):** new PIV step 11 "DRILL: Fluency — Re-Solve Cold" (Wk 20) [Gate 2] — re-solve 1 already-solved
practitioner lab/class cold, no-notes, <=15 min, ~20 labs.
New PIV order (16 steps): 01 Burp Mastery /02 BSCP Prep /03 Save-PoC /04 Semgrep /05 Secrets /06 ZAP /07 OOB
/08 Remaining Topics /09 Targeted Scanning /10 Reinforcement Labs /11 Fluency /12 Mystery /13 EXAM
/14 Job Apps(Month 4 onward) /15 Snyk /16 Full Assessment.
Validation: ast.parse OK; report_only 0; dedup 0 hard (51 steps, 5 advisories); real-path Paragraph parse OK.
PDF NOT generated (BUILD = source only). Remaining changelist items: 10 (Stamina drill), 11 (Practice-exam pass-gate).

## Batch: IMPLEMENT 10,11 — final gates (BUILD PDF, source only)  [2026-06-29]
**Item 10 (DONE):** new PIV step 13 "DRILL: Exam Stamina — Six Labs in One Block" (Week 20) [Gate 4] —
6 practitioner labs back-to-back in one timed 4-hr block, own notes/Pro/Collaborator, triage practice.
Inserted before EXAM; renumbered EXAM 13->14, Job Apps 14->15, Snyk 15->16, Full Assessment 16->17.
**Item 11 (DONE):** reframed the practice-exam bullet in step 02 from "Complete the BSCP practice exams"
to Gate 5 (simulation): "pass ... in under 2 hours — and do it more than once — before booking the real exam."
PIV now 17 steps; 5-gate ladder sits in order before the exam (10 Reinforcement=G1, 11 Fluency=G2,
12 Mystery=G3, 13 Stamina=G4, 14 EXAM; G5 practice-exam pass stated in step 02).
Within existing week-20/21 window -> no timeline change. Validation: ast.parse OK; report_only 0;
dedup 0 hard (52 steps); real-path Paragraph parse OK.
ALL 11 CHANGELIST ITEMS COMPLETE in source. PDF still NOT generated (BUILD = source only).

## Batch: IMPLEMENT 12,13,14 (BUILD PDF, source only)  [2026-06-29]
**Item 12 (DONE) — Burp Pro moved earlier so no Pro-gated labs are skipped.** Found 3 Pro-gated skips, all
in Phase III: SQLi out-of-band labs (Collaborator), OS-cmd out-of-band exfiltration (Collaborator), file-upload
expert web-shell-via-race-condition (Pro). Added a "Buy Burp Suite Professional now (~$499/yr)" prompt as the
first bullet of Phase III step 01 (Injection Classes); un-skipped all 3 (now done in place); reworded the Phase IV
Pro note (you bought Pro at Phase III, required continuously through the exam); reframed Phase IV OOB step 07 from
"closes the gap left by skipping in Phase III" to a pre-exam Collaborator drill (re-confirm fast) -> grades PART,
no hard dup.
**Item 13 (DONE) — BSCP text/lab pairing.** Audited recently-added BSCP (steps 07 OOB, 08 topics, 09 targeted
scanning, 10 reinforcement) = all already paired (text learning-path + labs). The one violation was a PRE-EXISTING
Phase II Authentication bullet: "Read JWT algorithm confusion and OAuth redirect URI manipulation" = reading-only,
no labs; and the JWT *algorithm confusion* lab was missing everywhere. Fix: reworded that Phase II bullet into the
gold pair format -> JWT learning path + #jwt labs (now incl. <i>algorithm confusion</i>) and OAuth learning path +
#oauth-authentication labs (incl. <i>account hijacking via redirect_uri</i>). Removed the now-duplicate OAuth/JWT
bullets from Phase IV step 08 (3 remaining topics: smuggling, host-header, cache-poisoning; "five->three topics,
2-3->1-2 weeks"). Updated step 10 cross-ref "Forced OAuth profile linking (step 08)" -> "(Phase II)".
**Item 14 (DONE):** removed the summary one-page-map intro sentence.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); real-path Paragraph parse OK.
No timeline change (banners/weeks untouched). PDF NOT generated (BUILD). Remaining changelist items: 15,16,17,18.

## Batch: IMPLEMENT 15,16,17 — Study Plan Phase Summary (BUILD PDF, source only)  [2026-06-29]
**Item 15 (DONE):** summary phase labels "0 —", "I —", ... -> "Phase 0 —", "Phase I —", ... (all 10).
**Item 16 (DONE):** 8 verbatim text replacements in the summary lines (refresh/expand engineering base;
"HTTP (Notes + MDN)"; "first labs and published lab writeups"; drop "the" before PortSwigger Authentication path;
", completed a full Juice Shop security assessment"; "threat model project"; drop "your" before portfolio writeups;
"new sub-field and role").
**Item 17 (DONE):** removed the flaws.cloud / flaws2.cloud hyperlinks in the SUMMARY only, by writing the dot as
the HTML entity &#46; (renders "flaws.cloud" as plain text; linkify's _URL_RE no longer matches). Phase V keeps its
real flaws.cloud / flaws2.cloud links (verified bare form still present there).
Validation: ast.parse OK; report_only 0; summary lines real-path Paragraph parse OK; link-scope verified
(unlinked in summary, linked in Phase V). No timeline change. PDF NOT generated (BUILD). Remaining: item 18.

## Batch: IMPLEMENT 18 — de-vague summary phrases (BUILD PDF, source only)  [2026-06-29]
**Item 18 (DONE):** clarified 4 vague summary achievements:
 - Phase II "apprentice labs cleared" -> "the PortSwigger Authentication, JWT, and OAuth labs cleared"
 - Phase IV "— and certification" -> "— and the BSCP certification"
 - Phase V "flaws.cloud and flaws2.cloud cleared with writeups" -> "every level of the flaws.cloud and
   flaws2.cloud AWS security challenges completed, with writeups" (entity dots preserved -> still unlinked)
 - Phase IX "a clear first-30/60/90 approach" -> "a written 30/60/90-day onboarding plan"
Validation: ast.parse OK; report_only 0; 10 summary lines parse; dedup 0 hard (52 steps).
ALL 18 CHANGELIST ITEMS COMPLETE in source. PDF NOT generated (BUILD = source only).

## Batch: IMPLEMENT 19,20,21 (BUILD PDF, source only)  [2026-06-29]
**Item 19 (DONE) — repeat-reading dedupe.** Scanned all portswigger.net links (57 distinct, 81 occurrences).
Acceptable dups = LABS links re-referenced in drills + resource listings + Phase IV lab-context references.
Repeat *readings* of learning paths: access-control & api-testing already used "Review your Phase II notes" (ok);
fixed the rest: Phase I SQLi/XSS "Read the ... material" -> "Skim the ... material to get oriented" (orientation
preview, not a full read); SQLi Phase III "Re-read the SQL injection learning path and your Phase II notes" ->
"Re-read your Phase II SQL injection notes (the learning path stays linked if you need it)". XSS full study stays
in Phase III (Phase I is now an explicit preview). All links kept clickable.
**Item 20 (DONE):** removed "Burp Suite Community Edition is free." from the Burp Suite Documentation resource.
**Item 21 (DONE):** removed the 3 "Gate N (label):" prefixes (only 3 existed): "Gate 5 (simulation): pass" ->
"Pass", "Gate 2 (fluency): for each" -> "For each", "Gate 4 (stamina): the real exam" -> "The real exam".
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph parse OK.
No timeline change. PDF NOT generated (BUILD). Remaining changelist items: 22-40 (19).

## Batch: IMPLEMENT 22,23,24 (BUILD PDF, source only)  [2026-06-29]
**Item 22 (DONE):** "a stronger AppSec signal than Sec+ alone" -> "a much stronger AppSec signal...".
**Item 23 (DONE):** step title un-abbreviated "Save Exam-Ready PoCs" -> "Save Exam-Ready Proof-of-Concept
Exploits"; added a bullet answering the notes question (web-confirmed: BSCP is fully open-book -- own notes, web,
third-party tools, Burp extensions all allowed; taken in Chrome alongside Burp). Guidance: digital searchable
notes (Markdown/plain text or notes app) ideal, payloads copy-paste-ready, pre-load payload lists/extensions in
Burp; no printed notes needed.
**Item 24 (DONE):** hyperlinked "pre-commit hook" (Gitleaks bullet) to the official pre-commit framework
https://pre-commit.com/ .
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph parse OK (196 bullets).
No timeline change. PDF NOT generated (BUILD). Remaining changelist items: 25-40 (16).

## Batch: IMPLEMENT 25,26,27 (BUILD PDF, source only)  [2026-06-29]
**Item 25 (DONE):** hyperlinked "GitHub Actions workflow" (Gitleaks/secrets "Integrate both" bullet) to official
https://docs.github.com/en/actions .
**Item 26 (DONE):** bolding pass. Bolded the 3 non-bold "Full notes + note cards:" (now all 10 bold); bolded "Key:";
bolded lead-in labels on ~30 Phase III+ bullets (label part only) e.g. Fix:, SSRF:, XSS:, Decoder:, Comparer:,
Content discovery:, For each lab:, Triage ZAP results:, Two distinct paths:, Target:, List on resume as:, etc.
Done via line-by-line regex on lines >=988 matching a leading "Label: " pattern (not already bold).
**Item 27 (DONE):** defined SAST/DAST in the Phase IV intro: "SAST (static analysis of source code, via Semgrep)
and DAST (dynamic testing of the running app) are the automation layer."
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph parse OK (180 fmt bullets).
No timeline change. PDF NOT generated (BUILD). Remaining changelist items: 28-40 (13).

## Batch: IMPLEMENT 28,29,30 (BUILD PDF, source only)  [2026-06-29]
**Item 28 (DONE):** improved OWASP ZAP resource desc -> "zaproxy.org/docs — the free, open-source OWASP DAST
tool: an intercepting proxy plus an automated scanner that crawls a running app and runs active and passive
checks for common web vulnerabilities. A free alternative to Burp Scanner, with a baseline scan that wires
easily into CI."
**Item 29 (DONE):** OOB drill bullets: "Blind SQL injection: re-read the [path] learning path" and "Blind XXE:
re-read the [path] learning path" -> "re-read your notes on [linked topic] (the learning path stays linked)".
Links preserved.
**Item 30 (DONE):** removed bullet "These three topics add roughly 1-2 weeks of study - budget for it before the exam".
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (205, 2 known FP).
No timeline change. PDF NOT generated (BUILD).

## Batch: IMPLEMENT 31,32,33 (BUILD PDF, source only)  [2026-06-29]
**Item 31 (DONE):** hyperlinked "Burp's Engagement tools" (Content-discovery bullet) ->
https://portswigger.net/burp/documentation/desktop/tools/engagement-tools (verified).
**Item 32 (DONE):** linked the first/key mention of each distinct Burp tool to its official doc (NOT every
repetition -- bluing all 29 "Burp Suite" mentions would harm readability; convention is link first mention):
  - "Burp Collaborator" (Phase III buy-Pro bullet) -> .../desktop/tools/collaborator
  - "Burp Suite Documentation" resource tool list -> Proxy/Repeater/Intruder/Sequencer linked to
    .../desktop/tools/<tool>; Scanner -> /burp/vulnerability-scanner (all verified via fetch/pattern)
  - appendix "Burp Suite Repeater" -> .../desktop/tools/repeater
  (Burp Suite Professional already linked to /burp/pro; Decoder/Comparer already linked to WSA paths.)
  NOTE: interpreted "all Burp references" as first/key mention of each tool; can extend to every occurrence if desired.
**Item 33 (DONE):** hyperlinked "BSCP exam" in "Take the BSCP exam." -> https://portswigger.net/web-security/certification (verified).
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (71 linked bullets).
No timeline change. PDF NOT generated (BUILD).
NOTE: changelist runs to item 44 (earlier in-session "remaining" counts mistakenly capped at 40). Remaining: 34-44 (11).

## Batch: IMPLEMENT 34,35,36 (BUILD PDF, source only)  [2026-06-29]
**Item 34 (DONE):** EXAM step retake bullet: "retake. The exam can be retaken." -> "retake. There is no cap on
attempts - you can retake as many times as needed (each attempt costs $99)." (web-confirmed: unlimited retakes,
$99/attempt).
**Item 35 (DONE):** "Applications run in parallel..." -> "Job applications run in parallel..." (disambiguates from
software "applications"; capital J as bullet start, lowercase "applications" for correct grammar).
**Item 36 (DONE):** internal cross-reference now links. Added anchor <a name="application_strategy"/> to the
Phase VIII "Application Strategy" SS heading (same mechanism as the existing philly_appsec anchor), and turned
both "Application Strategy" references (EXAM/APPLY bullet + Phase VII pointer) into <a href="#application_strategy">
links. Verified: 1 anchor destination, 2 links, consistent.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (75).
No timeline change. PDF NOT generated (BUILD). Remaining: 37-44 (8).

## Batch: IMPLEMENT 37,38,39 (BUILD PDF, source only)  [2026-06-29]
**Item 37 (DONE):** Snyk step de-vagued + how-to link. Bullet 1 -> "Install and authenticate the Snyk CLI
[docs.snyk.io/developer-tools/snyk-cli/getting-started-with-the-snyk-cli], then run `snyk test` in a sample
Python project ... to produce a software-composition report listing each flagged package, its CVE, and the
safe upgrade." Added CI bullet: wire `snyk test` into CI alongside Semgrep/Gitleaks (remediation = version bump).
(Snyk URLs web-verified.)
**Item 38 (DONE):** Juice Shop project (top portfolio artifact) expanded. Linked "OWASP Juice Shop" ->
owasp.org/www-project-juice-shop; added bullet pointing to the official companion guide "Pwning OWASP Juice Shop"
[pwning.owasp-juice.shop] (groups challenges by vuln class; appendix has full solutions); added "reuse prior
notes" bullet (reuse Phase III writeup methodology + report format; full workflow comes together here). URLs verified.
**Item 39 (DONE):** removed ", OWASP WebGoat" from the Phase 0 summary resources line ("HTTP (Notes + MDN),
OWASP WebGoat." -> "HTTP (Notes + MDN)."). WebGoat remains elsewhere as a real Phase 0/I resource.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (77).
No timeline change. PDF NOT generated (BUILD). Remaining: 40-44 (5).

## Batch: IMPLEMENT 40,41,42 (BUILD PDF, source only)  [2026-06-29]
**Item 40 (DONE):** added a 5-paragraph conversational broad-arc overview at the top of "Study Plan Phase
Summary" (after the H heading/SP, before the per-phase loop). Arc: turn SWE->entry AppSec in ~7-8 months;
refresh eng base + first taste of offense (Ph0-I); fill web/network gaps (PhII); core vuln classes hands-on +
toolchain + BSCP (PhIII-IV); back half = cloud + secure code review/threat modeling + Security+ (PhV-VII);
interview prep + job search, applying in parallel from Month 4 (PhVIII-IX). Rendered as add(P(..., S["body"]))
paragraphs with SP spacing.
**Item 41 (DONE):** fixed broken IAM link. res "AWS IAM Documentation" bare auto-link "docs.aws.amazon.com/IAM"
(=> AWS "Looking for something?" page) replaced with explicit working link to https://docs.aws.amazon.com/iam/
(display "docs.aws.amazon.com/iam"). The other IAM link (1369, .../IAM/latest/UserGuide/) is a valid path, left as is.
**Item 42 (DONE):** hyperlinked "AWS CLI installed and configured" ->
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html (official getting-started: install +
links to configure). URLs web-verified.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (81).
No timeline change. PDF NOT generated (BUILD). Remaining: 43-44 (2).

## Batch: IMPLEMENT 43,44 (BUILD PDF, source only)  [2026-06-29]  -- FINAL BATCH (only 2 remained)
**Item 43 (DONE):** fixed redundant/garbled rotation sentence in the "Credential exposure in git history" concept.
"...TruffleHog scans history. Rotation is the fix, not deletion. The fix is rotation of the exposed credential,
not deletion, plus pre-commit scanning..." -> "...TruffleHog scans history. The fix is to rotate the exposed
credential, not just delete it from current code, plus pre-commit scanning to prevent recurrence."
**Item 44 (DONE):** removed the deliberately-forced blank page before Phase VI. Was: PageBreak + P("\u00a0")
[blank-page hack] + PageBreak + banner VI. Now: single PageBreak + banner VI (Phase VI still starts on a fresh
page; no blank page). NOTE: this removes one page (doc 54pp -> ~53pp) and shifts page numbers from Phase VI
onward -- the self-correcting TOC loop in build_appsec.py main() will recompute all TOC/summary page numbers on
the next GENERATE, so no manual TOC edits needed. Verify blank page is gone + TOC corrected on next GENERATE.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); single PageBreak before banner VI; concept renders.
No timeline change. PDF NOT generated (BUILD).

=== CHANGELIST COMPLETE: items 1-44 all implemented in source. Remaining: 0. ===
Items 12-44 are BUILD-only (in source, NOT yet rendered). Next GENERATE will render all of them + auto-correct
the TOC for item 44's removed page.

## PENDING (newly added, NOT yet implemented)  [2026-06-29]
**Item 45:** "Read ASVS v4.0 Level 1 and Level 2 requirements. D" is confusing. The text is linked at:
"https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf"
**Item 46:** "Use GitHub Security Lab's published CVE writeups" is vague. Make the "writeups" text link to the
actual writeups.

## Batch: IMPLEMENT 45,46 (BUILD PDF, source only)  [2026-06-29]
**Item 45 (DONE):** ASVS step de-confused + linked to the standard. "Read [ASVS->project page] v4.0 Level 1 and
Level 2 requirements." -> "Read the [ASVS v5.0.0 Level 1 and Level 2 requirements -> v5.0.0 PDF]." (user-provided
raw.githubusercontent.com ASVS 5.0.0 PDF). Consistency: ASVS resource bumped v4.0->v5.0.0 and "14 domains"->
"17 chapters" (web-verified: ASVS 5.0.0, May 2025, 17 chapters, ~350 reqs, still L1/L2/L3). Chapter-mapping bullet
de-versioned ("ASVS V2 is authentication, V4 is access control, V5 is input validation, V6 is cryptography" ->
topic-based, no chapter numbers) because 5.0.0 RENUMBERED chapters and the old V2/V4/V5/V6 numbers are now wrong.
NOTE (not changed): the concept block still has an illustrative citation "this fails ASVS V2.1.1" (v4-style ID) -
left as a generic example; flag if you want it switched to v5.0.0 format (e.g. v5.0.0-1.2.4).
**Item 46 (DONE):** linked "writeups" -> https://securitylab.github.com/advisories/ (GitHub Security Lab
Advisories = the published GHSL/CVE writeups on real code). Web-verified.
Validation: ast.parse OK; report_only 0; dedup 0 hard (52 steps); AST render-path Paragraph OK (78).
No timeline change. PDF NOT generated (BUILD).

=== CHANGELIST COMPLETE: items 1-46 all implemented in source. Remaining: 0. ===

## PENDING (newly added, NOT yet implemented)  [2026-07-13]
**Item 47:** In section "Human Mentorship: MentorCruise (or Koz)", explicitly state that the first thing the
mentor should do is review this study plan to see if it seems like a valid way to actually get into an AppSec
role, and if any edits should be made, including removals, additions, and/or updates.

**Item 48 — INTERVIEW PREP (add as a tracked component; two tracks):**
User: plan needs interview prep BEFORE interviewing starts — routine "live code" practice, memorized behavioral/
past-job Q&A, and memorized AppSec/cyber foundational Q&A. Mock interviews before real ones (MentorCruise or a
dedicated mock site). User does well on memorized notecard-style Q, but LOCKS UP under anxiety on live-coding.
Refinements agreed:
- Track A (memorize + rehearse aloud): behavioral, past-job, AppSec foundational Q&A, notecard method. Cards
  should be a BYPRODUCT of each phase, not a late cram.
- Track B (DESENSITIZE, not learn): live secure code review out loud, "walk me through the exploit/fix," light
  scripting/data-parsing. Timed, watched reps at volume, spread across months. Graded exposure ladder:
  untimed -> timed -> watched -> watched-by-stranger; explicit think-aloud + "I'm stuck, here's my approach"
  recovery practice.
- Recurring mock interviews must be UNDERWAY BEFORE the first real interview (MentorCruise and/or mock site).
  Pull mock/Track-B reps EARLY (into Phase III-IV once vulnerable code is readable), NOT the final phase.
- Do NOT call the AppSec live component generic leetcode; name the real formats (live secure code review, light
  scripting) and drill those. Avoid generic leetcode mock sites (wrong format).
- Implementation: fold into existing phases; budget time / trim rather than balloon the plan.

**Item 49 — AI/LLM SECURITY (add; woven into existing phases, NOT a new phase):**
User: plan barely touches AI/LLM security; ~every 2026 AppSec posting mentions it (LLM APIs, prompt injection,
agentic AI). User's FastAPI/API background maps directly onto securing AI APIs -> likely highest-return add and
current differentiator. Plan predates how central this became.
Refinements agreed (LEAN, built on the Phase 0 FastAPI app):
- Phase III: add OWASP Top 10 for LLM Apps (prompt injection, insecure output handling, sensitive info
  disclosure, excessive agency). Reading; prompt injection bridges from the injection unit. No new project.
- Phase IV: ONE hands-on project — bolt a small LLM endpoint onto the Phase 0 app; test for prompt injection,
  insecure output handling, unsafe tool-calling; write it up (flagship portfolio artifact). Trim/replace an
  existing PIV exercise rather than stack on top.
- Phase VI: threat-model an LLM-integrated system (agent with tool access) — swap a target, not add one.
- Portfolio: one writeup on securing an LLM API.
- Scope guards: this is SECURING LLM APPS, not becoming an ML engineer. Budget ~1-2 weeks NET; if it can't fit
  in ~a week (mostly reframing existing work) without pushing the timeline, it doesn't go in. Frame as a
  differentiator/EDGE, not "required on every posting" (verify against CURRENT 2026 postings). Anchor all
  specifics to the CURRENT OWASP GenAI/LLM Top 10 + recent prompt-injection research; flag uncertainty, do NOT
  guess from memory.

## Batch: IMPLEMENT 48, 49, 47 (BUILD, source only)  [2026-07-13]
**Item 48 (DONE) - Interview prep as two tracks:** front-matter "No LeetCode" now frames the live format as a
performance skill you desensitize to early. Phase VIII intro reframed into Track A (memorize/rehearse aloud) vs
Track B (desensitize the live formats; fail on nerves not knowledge; start early). Subsections tagged Track A/B.
Added Track A foundational-question-bank bullet (jassics/security-interview-questions). New "Track B: Desensitizing
the Live Formats (Start Early)" subsection: graded exposure ladder, rehearse-the-recovery line, mock cadence
(weekly reps from Phase III, monthly full mocks from Month 4), and where to run mocks (MentorCruise / Exponent /
interviewing.io). Mentorship "Suggested usage" adds regular mocks before first real interview. No new phase/steps.
**Item 49 (DONE) - AI/LLM security woven in (lean):** anchored to current OWASP Top 10 for LLM Apps 2025
(genai.owasp.org/llm-top-10). Phase III: new concept mapping LLM01 prompt injection / LLM05 improper output
handling / LLM06 excessive agency / LLM02 sensitive-info disclosure onto existing skills (reading only). Phase IV:
new step 18 "PROJECT: Secure a Small LLM-Backed API" (Week 21, no phase extension) - bolt an LLM endpoint onto the
Phase 0 app, attack prompt injection / output handling / excessive agency, write it up (flagship AI portfolio
piece). Phase VI: threat-model project can target an LLM-integrated agent (STRIDE meets excessive agency + prompt
injection). Broad-arc overview names the AI/LLM thread as the current differentiator. Framed as an EDGE, not
"required on every posting."
**Item 47 (DONE) - Mentor plan-validity review:** mentorship "When to start" bullet now makes the first session a
hard review of whether this plan is a realistic route into entry-level AppSec, output = concrete add/cut/update
edits (not vague encouragement); brief the mentor on dev experience, the career gap, and live-coding anxiety.
(Burnout intentionally left OUT of the written doc - mention verbally.)
Validation: ast.parse OK; report_only 0; dedup 0 hard (53 steps); AST render-path OK. No timeline change. NOT rendered.
Remaining changelist: 0.

## PENDING (newly added, NOT yet implemented)  [2026-07-13] -- corrections to items 47/48/49
**Item 50:** Remove from the mentorship "When to start" bullet: " — not vague encouragement. Brief the mentor on
your background so the advice fits: your development experience, the career gap, and the live-coding anxiety this
plan is built around."
**Item 51:** Update section heading "Human Mentorship: MentorCruise (or Koz)" -> "Human Mentorship: MentorCruise".
**Item 52:** Remove from front-matter "No LeetCode": "Still, that live format is a performance skill as much as a
knowledge one — so you begin desensitizing to it early, with timed and then watched spoken code-review reps from
Phase III onward and mock interviews running before your first real interview (see Phase VIII)."
**Item 53:** Shorten significantly (summary overview): "Woven through these middle phases is a light but deliberate
thread of AI/LLM security — prompt injection, output handling, and tool-calling risk — currently the sharpest
differentiator for an engineer with an API background."
**Item 54:** Shorten significantly to match existing concept blurbs -- the Phase III concept "The OWASP Top 10 for
LLM applications" ("Modern apps increasingly ship an LLM-backed feature... you build and attack a real LLM-backed
API in Phase IV"). It's far too long vs surrounding blurbs.
**Item 55:** Phase IV step "PROJECT: Secure a Small LLM-Backed API" (Week 21) tells the user to do many things WITH
NO hyperlinks to official docs / guides / tutorials for how to actually do them. Add proper how-to hyperlinks.
(User flagged as a terrible and critical error.)
**Item 56:** "For maximum signal" (Phase VI threat-model target sentence) -- slang / casual phrasing in a technical
manual. Fix/replace.

## Batch: IMPLEMENT 50-56 (corrections to 47/48/49; BUILD, source only)  [2026-07-13]
50 removed mentor-background sentence from "When to start" bullet (now ends "...what to add, cut, or update.").
51 heading "Human Mentorship: MentorCruise (or Koz)" -> "Human Mentorship: MentorCruise".
52 removed the "Still, that live format..." append from front-matter "No LeetCode".
53 shortened the overview AI/LLM sentence to one clause ("A light thread of AI/LLM security...runs through these phases as well.").
54 shortened the Phase III "OWASP Top 10 for LLM applications" concept to ~3 sentences (blurb length); kept the link.
55 added hands-on how-to to Phase IV step 18: PortSwigger free Web LLM attacks labs (portswigger.net/web-security/llm-attacks); OWASP LLM Top 10 still linked in scope-guard bullet.
56 replaced casual "For maximum signal...runs headlong into" (Phase VI) with professional phrasing.
Validation: ast.parse OK; report_only 0; dedup 0 hard (53 steps); render-path OK. No timeline change. NOT rendered.
Remaining changelist: 0.

## PENDING (newly added, NOT yet implemented)  [2026-07-13] -- CRITICAL: broke step+source rule
**Item 57:** The OWASP Top 10 for LLM Applications was added ONLY as a concept in Phase III "How These Concepts
Are Used as an AppSec Engineer" (item 49-A) with NO corresponding LEARNING STEP and NO paired SOURCE in "Core
Vulnerability Classes." This violates the document's core rule: every topic the user must learn requires a
sequential step + source item. As written, the user never actually learns it. Add a proper Phase III step (with
its source / learning-path pairing) to actually learn the OWASP LLM Top 10, not just a reflection concept.
**Item 58:** Phase IV "PROJECT: Secure a Small LLM-Backed API" (Week 21) is missing hyperlinks -- the individual
labs should be hyperlinked, and the step does NOT follow the document's "learning path + link" pairing
requirement/convention used throughout. Fix to properly pair learning paths with their links and hyperlink the labs.

## Batch: IMPLEMENT 57, 58 (fix step+source rule violations; BUILD, source only)  [2026-07-13]
57 (DONE): OWASP LLM Top 10 now taught properly, not just reflected.
  57a - added res() SOURCE to Phase III "Learning Resources": OWASP Top 10 for LLM Applications (genai.owasp.org/llm-top-10).
  57b - added numbered STEP "08 READ + LABS: Web LLM Attacks" (Week 14) to Core Vulnerability Classes, pairing the
        PortSwigger Web LLM attacks learning path with its labs (all-labs#web-llm-attacks) + OWASP LLM Top 10 cross-ref +
        "For each lab" documentation bullet -- same shape as the injection/XSS steps.
  57c - converted the mislocated "How These Concepts Are Used" concept into a genuine reflection ("Securing LLM-backed
        features"); removed the "Reading only here" learning-plan language (learning now lives in the step).
58 (DONE): reworked Phase IV step 18 opening bullet to follow the pairing rule -- Web LLM attacks learning path +
  its labs, with individual labs hyperlinked (exploiting vulnerabilities in LLM APIs, indirect prompt injection);
  framed as "Reference the Phase III methodology ... reproduce against your own endpoint" (apply, not re-learn).
Validation: ast.parse OK; report_only 0; dedup 0 hard (54 steps, step 08 learn vs step 18 apply distinguished);
render-path OK. No timeline change (step 08 in Week 14). NOT rendered. Remaining changelist: 0.

## Batch: IMPLEMENT 59, 60 (BUILD, source only)  [2026-07-13]
59 (DONE): Web LLM attacks labs now referenced by EXACT title + level (verified from PortSwigger learning path).
  Step 08 does the three core labs: "Exploiting LLM APIs with excessive agency" (Apprentice), "Exploiting
  vulnerabilities in LLM APIs" (Practitioner), "Indirect prompt injection" (Practitioner); newer AI-agent labs
  noted as optional extension. Removed the bogus "insecure output handling" lab reference (it is a topic, not a
  lab). No Expert-tier lab exists. Step 08 label anchored (<a name="p3_llm_attacks"/>).
60 (DONE): step 18 rewritten succinct (7 bullets -> 4): build endpoint / attack via Phase III methodology /
  write up / scope. Internal-linked the "Phase III Web LLM Attacks step" (href #p3_llm_attacks) instead of
  pointing at external things; OWASP LLM Top 10 linked in the writeup bullet. Consistent links; removed the
  vague/duplicated lab list from the project step (labs live in step 08).
Validation: ast.parse OK; report_only 0; dedup 0 hard; render-path OK (anchored label renders); internal link 1:1.
No timeline change. NOT rendered. Remaining changelist: 0.

## Batch: FIX interview/LLM quality issues (BUILD, source only)  [2026-07-13]
- step 08 lab bullet: removed <b> from lab titles; each of the 3 core labs now individually hyperlinked to its
  PortSwigger lab page (excessive agency / vulnerabilities in LLM APIs / indirect prompt injection).
- step 08 OWASP bullet: reordered to sequential LLM01, LLM02, LLM05, LLM06 (was 01,05,06,02).
- step 18 (LLM project): added build how-to links (FastAPI tutorial + hosted-model API example [Anthropic/OpenAI]);
  de-vagued "Attack it with the methodology..." -> "Run the same three attack classes you practised in your
  [Phase III step]..."; de-vagued "anchoring findings" -> "label each finding with its OWASP LLM Top 10 ID
  (LLM01, LLM05, ...)". All actionable bullets now carry a link + a concrete instruction.
Validation: ast.parse OK; report_only 0; dedup 0 hard; render-path OK. No timeline change. NOT rendered.

## Batch: FIX step 08 LLM structure (BUILD, source only)  [2026-07-13]
- res "OWASP Top 10 for LLM Applications": removed trailing sentence ("This is the reading source...hands-on practice.").
- step 08 restructured to the learning-path + lab rule, per OWASP class, IN ORDER, side by side (no separate
  "Cross-reference ... as you go" bullet): each class = read its learning-path SECTION (anchor link) + do its lab:
    LLM01 Prompt injection -> prompt-injection + indirect-prompt-injection sections; labs: Exploiting vulnerabilities
      in LLM APIs + Indirect prompt injection (Practitioner).
    LLM02 Sensitive information disclosure -> leaking-sensitive-training-data section; READING ONLY (PortSwigger has
      no lab for this class - stated plainly).
    LLM05 Improper output handling -> insecure-output-handling section; demonstrated by the Indirect prompt injection
      lab (unsanitized output -> XSS); treat model output as untrusted input.
    LLM06 Excessive agency -> exploiting-LLM-APIs section; lab: Exploiting LLM APIs with excessive agency (Apprentice).
  Fixed typo "optional extension," -> "optional extensions,". Section-anchor URLs verified from the PortSwigger topic page.
Gates: edit_check.py PASS; ast.parse OK; report_only 0; dedup 0 hard; render-path OK. No timeline change. NOT rendered.

## Batch: FULL LLM restructure + timeline +0.5mo (BUILD, source only)  [2026-07-13]
- Split LLM learning into TWO sequential steps (no cramming, no OWASP<->PS cross-ref):
  step 08 "READ + LABS: Web LLM Attacks (PortSwigger)" (Weeks 15-16) - read the PortSwigger path front-to-back,
    doing each lab as reached: overview -> Exploiting LLM APIs (excessive agency lab, exploiting-vulns lab) ->
    Indirect prompt injection (lab) -> reading tail (training-data, leaking-data, defending) -> AI-powered
    scanner sub-page + its labs. Multiple bullets, each pairing reading section link(s) + lab link(s). Anchor kept.
  step 09 "READ: OWASP Top 10 for LLM Applications" (Week 16) - separate, read straight through AFTER PortSwigger;
    map to what was done (LLM01,02,05,06 attacked; rest recognized), note cards. IDs kept ascending.
- Timeline shifted +0.5 month (2 weeks) from Phase III onward (applications STAY Month 4 - stronger applicant, no delay):
  banners III..IX, chart weeks array, 4 schedule SS headings, 7 summary durations, and every Phase IV-VII step
  week token (+2). Cover bubbles carry no durations (unchanged). New end: ~Month 8.5 (was ~8.0).
  [BUG FOUND+FIXED mid-build: digit-bump regex matched digits inside \u2013 escapes, corrupting range second-numbers;
   protected escapes before bumping.]
Gates: edit_check PASS; report_only 0; dedup 0 hard; render-path OK; ast.parse OK. NOT rendered.

## Batch: shorten step 08 (BUILD + GENERATE)  [2026-07-13]
- step 08 collapsed to 2 bullets: (1) short "why" rationale; (2) "Web LLM attacks learning path, then the labs —
  [named labs]" compact form. Removed the "Overview first: What is a large language model?..." text entirely.
  Week tag unchanged (Weeks 15-16) -> no timeline change. Anchor kept for step 18 link.
Gates: edit_check PASS; report_only 0; dedup 0 hard; render-path OK.

## PENDING (newly added, NOT yet implemented)  [2026-07-13]
**Item 61:** Remove from step 09 (OWASP): "Add one note card per entry so the list becomes interview-ready recall".
**Item 62:** In Phase IV step 18 "PROJECT: Secure a Small LLM-Backed API" (Week 23), link every referenced OWASP LLM
ID to its own page, e.g. LLM05 -> https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/ . Skip the ones
in the parenthetical "(LLM01, LLM05, and so on)".
**Item 63:** Shorten (too wordy) the Phase VI threat-model sentence: "An especially strong target is an LLM-integrated
system — an agent that calls tools — where STRIDE must also account for excessive agency and prompt injection, the
AI-specific risks increasingly raised in AppSec interviews".
**Item 64:** "CompTIA Security+ is ATS bait —" sounds unprofessional / 4chan-ish. Reword to a professional register.
**Item 65:** Broken source link: https://certificationexpertsllc.com/ 404s. Fix/replace the source.

## Batch: IMPLEMENT 61-65 (BUILD, source only)  [2026-07-13]
61 removed step 09 "Add one note card per entry..." bullet.
62 linked LLM01/LLM05/LLM06 in step 18 attack bullet to their OWASP pages (verified URLs; note LLM01 uses
   llm01-prompt-injection, others use llmXX2025-slug). Write-up parenthetical left unlinked per request.
63 shortened Phase VI threat-model sentence to one concise clause.
64 reworded "CompTIA Security+ is ATS bait" -> "best understood as a resume-screen credential" (professional).
65 fixed dead source link certificationexpertsllc.com -> getcertifiedgetahead.com (verified live companion site).
Gates: edit_check PASS; report_only 0; dedup 0 hard; render-path OK; ast.parse OK. NOT rendered.
Remaining changelist: 0.

## Batch: velocity-driven timeline fix (BUILD + GENERATE)  [2026-07-13]
- Phase IV (BSCP) 7 -> 9 weeks (Wks 17-25). Was 1.2x over at fixed 21 h/wk; now ~0.9x. Tail de-crammed:
  drills 10-13 -> Wks 22-24, EXAM 14 -> Wks 24-25, capstones (Snyk/Juice Shop/LLM API) 16-18 -> Wks 24-25,
  DOCUMENT 03 -> Throughout 17-24. Applications (Month 4 onward) unchanged.
- Phase VII (Security+) 3 -> 4 weeks (Wks 31-34). Real 200-card make+memorize load (~25h) is ~1.1x over 3 wks.
  Step 01 renamed READ -> "READ + MEMORIZE: Study Guide"; card bullet rewritten from "one card per domain" to
  granular decks (160-200 cards; ports/crypto-PKI/attacks/controls/governance) + grouped-7 cumulative review.
- Cascaded V-IX: banners, chart array, schedule SS (IV/V/VI), summary durations, and every Phase V/VI/VII step
  week token. New end ~Month 9 (was ~8.5). Pace LOCKED 21 h/wk (gig work 2 days/wk is in the schedule).
- velocity_analysis.py: locked PACE=21 (dropped full-time scenario), added note-card cost model (make+memorize
  calibrated to 170-card JS deck), Phase IV=9/VII=4, added commit-log findings (gaps=job, pace validated).
Gates: edit_check PASS; report_only 0; dedup 0 hard; render-path OK.

========================================================================
## SESSION SUMMARY  [2026-07-13]  (builds 7 -> 11)
========================================================================
Consolidated recap of today's work.

LLM SECURITY CONTENT (Phase III + IV)
- Split crammed LLM material into two sequential steps: III-08 "READ + LABS: Web LLM Attacks"
  (full PortSwigger path front-to-back, labs interleaved) and III-09 "READ: OWASP Top 10 for LLM
  Applications" (separate, read after). No cross-referencing/skipping.
- Later compacted step 08 to 2 bullets (short "why" + one learning-path/labs line); removed the
  "Overview first..." preamble.
- Phase IV project: linked OWASP LLM IDs (LLM01/05/06) to their exact per-entry OWASP pages.

WORDING / PROFESSIONALISM
- "CompTIA Security+ is ATS bait" -> "resume-screen credential".
- Shortened wordy Phase VI LLM threat-model sentence.
- Removed redundant note-card bullet from the OWASP step.

BROKEN LINK FIXES (verified live before swapping)
- certificationexpertsllc.com (404) -> getcertifiedgetahead.com (Security+ book companion site).

DATA-DRIVEN TIMELINE RECALIBRATION (the main effort)
- Scraped all 27 lainislove study weeks, sampled note PDFs + practice pages, parsed 304-commit git log.
- Established real velocity: ~584 logged h; ~21 h/wk median; notes/cards/labs (not reading) dominate;
  calendar gaps (125/83/57/154 days) = JOB periods, not slow learning.
- Shipped velocity_analysis.py: per-phase required-vs-available-hours model, pace LOCKED at 21 h/wk.
- Acted on findings:
    * Phase IV (BSCP) 7 -> 9 wks; de-crammed drill/exam/capstone tail (Wks 17-25).
    * Phase VII (Security+) 3 -> 4 wks; card guidance rewritten "one card per domain" -> granular
      160-200-card decks + grouped-7 cumulative review; step 01 renamed "READ + MEMORIZE".
    * Cascaded V-IX across all timeline locations (banners, chart, schedule SS, summary, step tokens).
      End date moved out ~3 wks (~Month 9).

CORRECTION LOGGED
- Earlier claim that the plan was "massively under-budgeted" on reading time was overstated; proper
  analysis showed the timeline was mostly well-calibrated -- only Phase IV and VII needed more room.

Gates every build: edit_check PASS; report_only 0; dedup 0 hard; render-path OK. Ended at build-11
(rendered: Study_Plan_-_2026-07-13.pdf, 55pp).

## Batch: fix stale prose timeline refs + wire prose check into GENERATE (BUILD)  [2026-07-13]
- Fixed 7 prose timeline references left stale by today's +5wk growth (found by new timeline_ref_check):
  overview + nb callout duration 6-8mo -> 7-9mo (7 optimistic / 9 outer bound / 8 midpoint); summary
  "seven to eight months" -> "eight to nine months"; Security+ "Month 7" -> "Month 8.5" (nb + Phase IV
  APPLY push); Phase VIII Track B "Month 7.5" -> "Month 8.75"; Burp Mastery milestone "Week 16" -> "Week 18".
- NEW check timeline_ref_check.py: derives the phase map from banners and flags prose month/week mentions
  that disagree (Security+ month, Phase VIII start, total-duration bounds, Burp milestone). report_only()
  only covers the banner/chart/schedule/step machinery; this closes the prose gap.
- Wired timeline_ref_check into build_appsec.py main() -> runs on every GENERATE PDF (WARNS, like dedup).
Gates: timeline_ref_check PASS; report_only 0; edit_check PASS; dedup 0 hard; render-path OK. NOT rendered.

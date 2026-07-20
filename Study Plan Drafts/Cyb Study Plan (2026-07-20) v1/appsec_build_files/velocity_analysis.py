#!/usr/bin/env python3
"""
velocity_analysis.py  --  Study-velocity model from Kyle's real self-taught web-dev logs
(lainislove.com weeks 1-27, Oct 2018-Aug 2020) applied to the AppSec plan to compare
EXPECTED (plan) vs ACTUAL-PACE (data-derived) time.

Pace is LOCKED at 21 h/week: gig work (7 h x 2 days/wk) is built into the doc's schedule
and cannot bend. Fixes therefore come from CALENDAR WEEKS, not more hours.
Run:  python3 velocity_analysis.py    (all constants editable)
lainislove hours + note/card volumes are MEASURED; AppSec hour inputs are ESTIMATES.
"""
import statistics as st

# ============================================================================
# 1. MEASURED  --  weekly logged study hours (weeks 1-27)
# ============================================================================
WEEK_HOURS = {1:24.83,2:21.13,3:20.20,4:16.40,5:38.75,6:8.00,7:29.47,8:35.70,9:25.72,
    10:34.82,11:21.92,12:16.68,13:29.30,14:15.92,15:14.32,16:13.42,17:19.77,18:25.25,
    19:28.93,20:24.38,21:17.70,22:22.78,23:6.45,24:14.70,25:11.95,26:5.22,27:40.08}
NOTE_VOLUMES = {"JS":(32,170),"PHP":(39,None),"Python":(24,120),"jQuery":(9,None)}  # (note_pp, cards)

hrs=list(WEEK_HOURS.values())
TOTAL_LOGGED=sum(hrs); MEAN=st.mean(hrs); MEDIAN=st.median(hrs)
P25,P75=sorted(hrs)[len(hrs)//4],sorted(hrs)[3*len(hrs)//4]
PACE=21.0   # LOCKED

# ============================================================================
# 2. VELOCITY CONSTANTS (derived from logs)
# ============================================================================
MIN_PER_PAGE={"exercise":12.0,"reference":4.0,"skim":1.5}  # all-in min/pg (read+do+notes)
HRS_PER_LAB=1.6      # blended PortSwigger lab. Web-dev commits can't isolate security-lab time,
                     #   so this stays a reasoned proxy (a lab ~ one substantial JS exercise). Adjustable:
                     #   at 2.0, Phase IV would want 10 wks instead of 9.
CERT_MIN_PAGE=3.0    # exam-prep reading+notes (not exercise-heavy)
CERT_PRACTICE=9.0    # practice exams
# --- note-card model, calibrated to real decks (JS=170 cards ~11-12h to memorize; Python=120) ---
CARD_MAKE_MIN=3.5    # min to CREATE one card (title + 1-5 bullets), in book order
CARD_MEMO_MIN=4.0    # min/card to MEMORIZE via grouped-7 cumulative review to fluency.
                     #   True method is super-linear (each new 7-group re-drills the grown pile); a
                     #   per-card rate calibrated to the 170-card JS deck is used for planning -- larger
                     #   decks skew slightly higher than linear.
def card_hours(n): return n*CARD_MAKE_MIN/60.0 + n*CARD_MEMO_MIN/60.0
PROJECT_HRS={"small":10,"medium":20,"flagship":35}

# ============================================================================
# 3. APPSEC PLAN  --  allotted weeks (current timeline) + content inventory
# ============================================================================
def book(p,k): return ("book",k,p)
def labs(n):   return ("labs",None,n)
def proj(s):   return ("proj",s,None)
def cert(p,c): return ("cert",c,p)
def misc(h,l="misc"): return ("misc",l,h)

PHASES=[
 ("0","Pre-Study: Foundations",3,[book(100,"skim"),misc(20,"FastAPI/Docker/Git refresh + lab setup")]),
 ("I","AppSec Intro",2,[book(65,"exercise"),labs(6),misc(6,"WebGoat/TryHackMe")]),
 ("II","Web & Network Foundations",4,[book(195,"reference"),book(115,"reference"),labs(14),misc(8,"crypto/net")]),
 ("III","Core Vulnerability Classes",7,[book(160,"exercise"),labs(45),book(30,"reference"),proj("small")]),
 ("IV","Security Testing & Tooling",9,[labs(55),misc(20,"SAST/DAST/Snyk/Semgrep/ZAP"),
      misc(12,"BSCP exam (hands-on, timed)"),proj("medium"),proj("flagship")]),   # 7 -> 9 wks
 ("V","Cloud Security Fundamentals",2,[labs(12),misc(12,"AWS security basics")]),
 ("VI","Secure Code Review & Threat Modeling",3,[book(190,"reference"),book(40,"reference"),
      proj("medium"),misc(10,"timed code-review reps")]),
 ("VII","CompTIA Security+",4,[cert(674,200)]),                                    # 3 -> 4 wks, 200-card deck
 ("VIII","Interview Preparation",3,[misc(30,"behavioral + cards + mocks + Track-B reps")]),
]

def phase_hours(content):
    h=0.0; parts=[]
    for kind,sub,amt in content:
        if kind=="book": hh=amt*MIN_PER_PAGE[sub]/60.0; parts.append(f"{amt}pg {sub}={hh:.0f}h")
        elif kind=="labs": hh=amt*HRS_PER_LAB; parts.append(f"{amt} labs={hh:.0f}h")
        elif kind=="proj": hh=PROJECT_HRS[sub]; parts.append(f"{sub} proj={hh:.0f}h")
        elif kind=="cert": hh=amt*CERT_MIN_PAGE/60.0+card_hours(sub)+CERT_PRACTICE; parts.append(f"cert {amt}pg+{sub}cards+exams={hh:.0f}h")
        elif kind=="misc": hh=amt; parts.append(f"{sub}={hh:.0f}h")
        h+=hh
    return h,parts

# ============================================================================
# 4. REPORT
# ============================================================================
if __name__=="__main__":
    print("="*80)
    print("STUDY-VELOCITY ANALYSIS  --  lainislove data  ->  AppSec plan")
    print("="*80)
    print(f"MEASURED (27 logged study weeks, ~22 months w/ gaps):")
    print(f"  total logged     : {TOTAL_LOGGED:.0f} h  |  per active week: mean {MEAN:.1f} | median {MEDIAN:.1f} | IQR {P25:.0f}-{P75:.0f} | range {min(hrs):.0f}-{max(hrs):.0f}")
    print(f"  note volume      : JS 32pp/170cards | PHP 39pp | Python 24pp/120cards | jQuery 9pp")
    print(f"  card system      : make ~{CARD_MAKE_MIN:.1f} min/card; memorize ~{CARD_MEMO_MIN:.1f} min/card (grouped-7 cumulative review)")
    print(f"  commit log       : 304 commits Oct'18-Sep'20; gaps of 125/83/57/154 days = JOB periods, not slow")
    print(f"                     learning -- active pace held ~21 h/wk. Confirms the fixed-pace assumption.")
    print(f"  key finding      : exercise/lab work ~12 min/pg all-in (~10x raw reading); labs+projects+cards dominate.\n")

    print(f"PHASE-BY-PHASE  --  required vs allotted at FIXED {PACE:.0f} h/wk (gig work 2 days/wk is in the schedule)")
    print("-"*80)
    print(f"{'Ph':<4}{'weeks':>6}{'avail_h':>9}{'req_h':>7}{'verdict':>13}   drivers")
    tot_req=tot_av=tot_wk=0
    for roman,name,weeks,content in PHASES:
        req,parts=phase_hours(content); avail=weeks*PACE
        tot_req+=req; tot_av+=avail; tot_wk+=weeks
        r=req/avail; v="OK" if r<=1.05 else ("TIGHT" if r<=1.35 else "OVER")
        flag="" if v=="OK" else f" ({r:.2f}x)"
        print(f"{roman:<4}{weeks:>6}{avail:>9.0f}{req:>7.0f}{v+flag:>13}   "+", ".join(parts[:3]))
    r=tot_req/tot_av
    print("-"*80)
    print(f"{'TOT':<4}{tot_wk:>6}{tot_av:>9.0f}{tot_req:>7.0f}{('OK' if r<=1.05 else 'TIGHT' if r<=1.35 else 'OVER')+f' ({r:.2f}x)':>13}")
    print(f"     plan needs ~{tot_req:.0f} h; {tot_wk} weeks at {PACE:.0f} h/wk provides ~{tot_av:.0f} h "
          f"(=> ~{tot_req/tot_wk:.0f} h/wk needed, under your {MEDIAN:.0f} median).\n")
    print("READ-OUT")
    print("-"*80)
    print("• Phase IV (BSCP) widened 7->9 wks: was 1.2x over at 21 h/wk; now ~0.9x. Tail de-crammed.")
    print("• Phase VII (Security+) widened 3->4 wks: real 200-card make+memorize load (~25h) is ~1.1x over")
    print("  3 wks; fits 4. Card guidance rewritten from '1 card per domain' to granular decks.")
    print("• BSCP unchanged for cards (practical exam -- drills are the memorization-equivalent).")
    print("• Pace stays 21 h/wk. Calendar end moves out ~3 weeks vs the prior build.")

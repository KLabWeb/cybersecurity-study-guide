#!/usr/bin/env python3
"""
log.py -- append a changelist item VERBATIM to CHANGELOG_APPLIED.md and commit.

Purpose: when the user says "add to changelist" / "log only", the ENTIRE task is
transcribe -> commit -> one-line confirm. No investigation, no planning, no proposals.
This helper reduces that to one mechanical command so there is nothing to "think" about.

Usage:
    python3 log.py "the exact text to log, verbatim"
    python3 log.py --top "text"          # insert at the TOP of the newest PENDING block
    python3 log.py -                      # read the item text from stdin (for long/multi-line)

It does NOT interpret, summarize, or act on the item. It only writes and commits.
"""
import sys, subprocess, datetime, os

CHANGELOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CHANGELOG_APPLIED.md")
PENDING_HEADER = "## PENDING (newly added, NOT yet implemented)"

def read_arg():
    top = False
    args = sys.argv[1:]
    if args and args[0] == "--top":
        top = True; args = args[1:]
    if args == ["-"]:
        text = sys.stdin.read()
    else:
        text = " ".join(args)
    return text.rstrip("\n"), top

def main():
    text, top = read_arg()
    if not text.strip():
        print("log.py: refusing to log empty text"); sys.exit(1)
    s = open(CHANGELOG, encoding="utf-8").read()
    if top and PENDING_HEADER in s:
        idx = s.rfind(PENDING_HEADER) + len(PENDING_HEADER)
        # skip to end of the header line
        nl = s.find("\n", idx)
        s = s[:nl+1] + text + "\n" + s[nl+1:]
    else:
        if not s.endswith("\n"): s += "\n"
        if PENDING_HEADER not in s.split("\n")[-40:].__str__():
            s += f"\n{PENDING_HEADER}  [{datetime.date.today()}]\n"
        s += text + "\n"
    open(CHANGELOG, "w", encoding="utf-8").write(s)
    subprocess.run(["git", "add", "CHANGELOG_APPLIED.md"], cwd=os.path.dirname(CHANGELOG))
    r = subprocess.run(["git", "commit", "-q", "-m", "Changelist: log item (verbatim)"],
                       cwd=os.path.dirname(CHANGELOG), capture_output=True, text=True)
    print("logged (verbatim) + committed" if r.returncode == 0 else "logged; commit note: " + r.stderr.strip())

if __name__ == "__main__":
    main()

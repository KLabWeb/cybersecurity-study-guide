#!/usr/bin/env python3
"""
present_build_zip.py  --  Assemble the full Study-Plan build package as a single .zip.

Invoked by the chat command:  PRESENT BUILD ZIP
Run directly:                 python3 present_build_zip.py

Produces  "Cyb Study Plan (<today>).zip"  in /mnt/user-data/outputs, containing every file
from the prior package plus all new files (currently: phase_content_check.py). The latest
generated PDF is included as *_LATEST.pdf and the original reconstruction source as *_SOURCE.pdf.
Prints the final zip path (the caller then presents it).
"""
import os, glob, zipfile, datetime, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/user-data/outputs" if os.path.isdir("/mnt/user-data/outputs") else HERE
BUILDF = os.path.join(OUT, "appsec_build_files")
SOURCE_PDF_DATE = "2026-05-26"  # original reconstruction source


def _first(*paths):
    for p in paths:
        if p and os.path.exists(p):
            return p
    return None


def latest_pdf():
    pdfs = [p for p in glob.glob(os.path.join(OUT, "Study_Plan_-_*.pdf"))
            if SOURCE_PDF_DATE not in os.path.basename(p)
            and "_SOURCE" not in os.path.basename(p)]
    if not pdfs:
        return None
    return max(pdfs, key=os.path.getmtime)


def build_zip():
    latest = latest_pdf()
    source_pdf = _first(os.path.join(OUT, f"Study_Plan_-_{SOURCE_PDF_DATE}.pdf"),
                        os.path.join(BUILDF, f"Study_Plan_-_{SOURCE_PDF_DATE}_SOURCE.pdf"),
                        os.path.join(BUILDF, f"Study_Plan_-_{SOURCE_PDF_DATE}.pdf"))
    changelog = _first(os.path.join(BUILDF, "CHANGELOG_APPLIED.md"),
                       os.path.join(HERE, "CHANGELOG_APPLIED.md"))

    # arcname -> source path  (None sources are skipped with a warning)
    members = {}
    if latest:
        base = os.path.basename(latest).replace(".pdf", "_LATEST.pdf")
        members[base] = latest
    if source_pdf:
        members[f"Study_Plan_-_{SOURCE_PDF_DATE}_SOURCE.pdf"] = source_pdf
    for fn in ("appsec_content.py", "appsec_infrastructure.py", "build_appsec.py",
               "timeline_check.py", "phase_content_check.py", "present_build_zip.py",
               "appsec_toc_state.json", "README.md", "HANDOFF.md"):
        members[fn] = _first(os.path.join(HERE, fn), os.path.join(BUILDF, fn))
    members["CHANGELOG_APPLIED.md"] = changelog
    for tt in ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf"):
        members[f"fonts/{tt}"] = _first(os.path.join(HERE, "fonts", tt),
                                        os.path.join(BUILDF, "fonts", tt))

    missing = [a for a, s in members.items() if not s]
    for a in missing:
        print(f"  WARNING: missing source for {a}")
    members = {a: s for a, s in members.items() if s}

    today = datetime.date.today().isoformat()
    zip_path = os.path.join(OUT, f"Cyb Study Plan ({today}).zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, src in sorted(members.items()):
            z.write(src, arc)
    print(f"ZIP -> {zip_path}  ({len(members)} files, {os.path.getsize(zip_path)/1024/1024:.2f}MB)")
    print("contents:")
    for arc in sorted(members):
        print(f"  {arc}")
    return zip_path


if __name__ == "__main__":
    p = build_zip()
    # emit the path on the last line for easy capture
    print("ZIPPATH=" + p)

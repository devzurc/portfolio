#!/usr/bin/env python3
"""Pull latest CV exports from public Google Docs into docs/resume/."""

from __future__ import annotations

import shutil
import sys
from datetime import date
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
ASSETS_CV = REPO / "assets" / "files" / "cv"

DOCS = {
    "EN": {
        "id": "1O4YsNWyfANs_332ecNZ8fgf-wclyuJCjZpO0LBqX2S8",
        "base": "LucasCruz_CV_EN",
    },
    "PT": {
        "id": "1oi8mzTJNNTu3CdSuqEgiWCPmiyvGWxrsstU93K0QV0Q",
        "base": "LucasCruz_CV_PT",
    },
}

FORMATS = {
    "docx": ROOT / "word" / "{base}.docx",
    "txt": ROOT / "source" / "{base}.txt",
    "pdf": ROOT / "pdf" / "{base}.pdf",
}


def download(doc_id: str, fmt: str, dest: Path) -> None:
    url = f"https://docs.google.com/document/d/{doc_id}/export?format={fmt}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as response:
        data = response.read()
    if data[:15].startswith(b"<!DOCTYPE") or data[:5].startswith(b"<html"):
        raise RuntimeError(f"Export failed for {dest.name} — document may be private or unavailable.")
    dest.write_bytes(data)


def main() -> int:
    today = date.today().isoformat()
    print(f"Syncing CVs from Google Docs ({today})…")

    for lang, meta in DOCS.items():
        doc_id = meta["id"]
        base = meta["base"]
        for fmt, template in FORMATS.items():
            dest = Path(str(template).format(base=base))
            download(doc_id, fmt, dest)
            print(f"  [{lang}] {fmt} → {dest.relative_to(REPO)}")

        site_pdf = ASSETS_CV / f"{base}.pdf"
        site_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "pdf" / f"{base}.pdf", site_pdf)
        print(f"  [{lang}] pdf → {site_pdf.relative_to(REPO)} (site download)")

    print("Done. Update markdown manually or run build-word.py only if regenerating from markdown.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Fetch every source in papers/manifest.json and extract per-page text.

Ported from fdbx via cdbx. Adds `"kind": "html"` entries: one or more web pages
(`"urls"`), saved under papers/local/<key>/ and extracted as plain text, one page
per URL, so a provenance row can cite a toolkit or regulation page. Vendored PDFs live in papers/; anchors that may not be
redistributed are downloaded to papers/local/ (gitignored), so the repo tracks
only the manifest. check_provenance.py reads the page text this script writes
to papers/pages/<key>/NNN.txt (also gitignored).

    python3 scripts/fetch_sources.py            # fetch what is missing, re-extract text
    python3 scripts/fetch_sources.py --force    # re-download the non-vendored copies
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAPERS = REPO / "papers"
MANIFEST = PAPERS / "manifest.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) edbx-fetch/1.0"


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=90) as response:
        dest.write_bytes(response.read())


def ocr_page(src: Path, n: int) -> str:
    """OCR one page of a scanned PDF (pdftoppm + tesseract)."""
    with tempfile.TemporaryDirectory() as tmp:
        stem = Path(tmp) / "p"
        subprocess.run(["pdftoppm", "-f", str(n), "-l", str(n), "-r", "300", "-gray", "-png",
                        "-singlefile", str(src), str(stem)], check=True, capture_output=True)
        return subprocess.run(["tesseract", f"{stem}.png", "-", "--psm", "1"],
                              capture_output=True, text=True, check=True).stdout


def extract(key: str, src: Path) -> int:
    pages = PAPERS / "pages" / key
    pages.mkdir(parents=True, exist_ok=True)
    info = subprocess.run(["pdfinfo", str(src)], capture_output=True, text=True, check=True).stdout
    count = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    texts = [subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), str(src), "-"],
                            capture_output=True, text=True, check=True).stdout
             for n in range(1, count + 1)]
    # A scan has no text layer: fall back to OCR when the whole PDF extracts empty.
    if not "".join(texts).strip() and shutil.which("tesseract") and shutil.which("pdftoppm"):
        texts = [ocr_page(src, n) for n in range(1, count + 1)]
    for n, out in enumerate(texts, 1):
        (pages / f"{n:03d}.txt").write_text(out)
    return count


def html_to_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h[1-6]|tr|section|article)>", "\n", raw)
    text = htmllib.unescape(re.sub(r"<[^>]+>", " ", raw))
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def fetch_html(key: str, entry: dict, force: bool) -> int:
    folder = PAPERS / "local" / key
    pages = PAPERS / "pages" / key
    pages.mkdir(parents=True, exist_ok=True)
    for n, url in enumerate(entry["urls"], 1):
        dest = folder / f"{n:02d}.html"
        if force or not dest.is_file():
            download(url, dest)
        (pages / f"{n:03d}.txt").write_text(html_to_text(dest.read_text(errors="ignore")))
    return len(entry["urls"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    failed = 0
    for key, entry in manifest.items():
        try:
            if entry.get("kind") == "html":
                n = fetch_html(key, entry, args.force)
                print(f"  ✓ {key:34s} {n:>4} web page(s)")
                continue
            dest = PAPERS / entry["file"]
            if not dest.is_file() or (args.force and not entry.get("vendored")):
                download(entry["url"], dest)
            n = extract(key, dest)
            print(f"  ✓ {key:34s} {n:>4} page(s)")
        except Exception as exc:  # noqa: BLE001 - report and continue with the rest
            failed += 1
            print(f"  ✗ {key:34s} {exc}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

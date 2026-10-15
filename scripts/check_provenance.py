#!/usr/bin/env python3
"""Check that every claim a skill attributes to a source can be found there.

Ported from fdbx. Each skill keeps references/provenance.md: a table whose rows
name a source, a locator, and a short anchor phrase from the source. For a
source key in papers/manifest.json, this script confirms the anchor appears in
the extracted text -- on the cited page when the locator is `p. N` -- so a
reader can open the PDF at that page and see the basis for the claim.

A row whose Source cell is not a manifest key (a paywalled anchor with no
legal free copy) must say `metadata only` in its Note: it was checked against
Crossref metadata, not against the text, and the check reports how many such
rows remain.

Matching ignores case, punctuation, whitespace and hyphenation, because PDF text
breaks lines and columns unpredictably. Anchors are 3-12 words: long enough to
be unambiguous, short enough to be a pointer rather than a copy.

    python3 scripts/fetch_sources.py        # first, to build papers/pages/
    python3 scripts/check_provenance.py
    python3 scripts/check_provenance.py --skills allocation,trust-calibration
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BOX = "edbx"
SKILLS_DIR = REPO / BOX
PAPERS = REPO / "papers"
MANIFEST = PAPERS / "manifest.json"
MIN_WORDS, MAX_WORDS = 3, 12
PAGE_RE = re.compile(r"^pp?\.\s*(\d+)")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).lower()
    return re.sub(r"[^a-z0-9]", "", text)


@dataclass
class Row:
    line: int
    source: str
    locator: str
    anchor: str
    note: str


def parse_rows(md: str) -> list[Row]:
    """Rows whose first cell is a number: | # | element | source | locator | anchor | note |"""
    rows: list[Row] = []
    for lineno, line in enumerate(md.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not cells[0].isdigit():
            continue
        note = cells[5] if len(cells) > 5 else ""
        rows.append(Row(lineno, cells[2].strip("`"), cells[3], cells[4].strip("\"“”"), note))
    return rows


def load_pages(key: str) -> dict[int, str]:
    folder = PAPERS / "pages" / key
    return {int(p.stem): normalize(p.read_text(errors="ignore")) for p in sorted(folder.glob("*.txt"))}


def check_row(row: Row, manifest: dict) -> str | None:
    words = row.anchor.split()
    if not MIN_WORDS <= len(words) <= MAX_WORDS:
        return f"anchor must be {MIN_WORDS}-{MAX_WORDS} words, got {len(words)}"
    if row.source not in manifest:
        if "metadata only" in row.note.lower():
            return None
        return f"unknown source {row.source!r}: add it to papers/manifest.json or mark the row 'metadata only'"
    pages = load_pages(row.source)
    if not pages:
        return f"no extracted text for {row.source!r}; run scripts/fetch_sources.py"
    needle = normalize(row.anchor)
    offset = manifest[row.source].get("page_offset")
    match = PAGE_RE.match(row.locator)
    if match and offset is not None:
        first = int(match.group(1)) - offset
        # An anchor may run from the foot of one page onto the next.
        if needle in pages.get(first, "") + pages.get(first + 1, ""):
            return None
        found = [n + offset for n, text in pages.items() if needle in text]
        where = f"; found on p. {', '.join(map(str, found))}" if found else ""
        return f"anchor not on {row.locator}{where}"
    if any(needle in text for text in pages.values()):
        return None
    return "anchor not found in source"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills", help="comma-separated short names")
    args = parser.parse_args()
    wanted = set(args.skills.split(",")) if args.skills else None

    manifest = json.loads(MANIFEST.read_text())
    errors: list[str] = []
    checked = metadata_only = 0
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name != BOX):
        if wanted and skill_dir.name.removeprefix(f"{BOX}-") not in wanted:
            continue
        prov = skill_dir / "references" / "provenance.md"
        if not prov.is_file():
            errors.append(f"{skill_dir.name}: no references/provenance.md")
            continue
        rows = parse_rows(prov.read_text())
        if not rows:
            errors.append(f"{skill_dir.name}: provenance.md has no numbered rows")
        for row in rows:
            checked += 1
            if row.source not in manifest and "metadata only" in row.note.lower():
                metadata_only += 1
            if (err := check_row(row, manifest)) is not None:
                errors.append(f"{skill_dir.name}/references/provenance.md:{row.line}: {err}")

    for line in errors:
        print(f"  ✗ {line}")
    print(f"\nChecked {checked} anchors ({checked - metadata_only} against source text, "
          f"{metadata_only} metadata only) — {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

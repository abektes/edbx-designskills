#!/usr/bin/env python3
"""Score generated skill outputs against each skill's Deliverable Quality Bar.

Two layers, split along the line TypeSafe's own guidance draws: anything that is a
rule, a count, or an exact lookup stays in code; only genuine semantic judgment
goes to the model.

  structural  pure code -- does every item in section B also appear in table A,
              are there at least N of a thing, is a required section present.
  semantic    Jev Nouls -- is this value concrete rather than a placeholder, is
              this recommendation specific enough to write a ticket from.

Jev cannot count (documented jagged edge), so no question ever asks it to. Items
are enumerated in code and passed as a JSON array in `state`; one Noul per item
references `items[i]`, all in a single request, and the tally happens in code.

    python3 scripts/conformance.py --skills value-dams-and-flows --dry-run
    python3 scripts/conformance.py --skills value-dams-and-flows
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVAL_DIR = REPO / "eval-framework"
CACHE_DIR = EVAL_DIR / "generations"
TYPESAFE_ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"


# --------------------------------------------------------------------- parsing

def strip_md(text: str) -> str:
    """Remove inline markdown so comparisons see the words, not the formatting."""
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(set(c.strip()) <= set("-: ") and c.strip() for c in cells)


@dataclass
class Table:
    heading: str
    header: list[str]
    rows: list[list[str]]

    def column(self, name_fragment: str) -> int | None:
        for i, h in enumerate(self.header):
            if name_fragment.lower() in h.lower():
                return i
        return None


def parse_tables(text: str) -> list[Table]:
    """Every markdown table in the document, tagged with the heading above it."""
    tables: list[Table] = []
    heading = ""
    pending: list[list[str]] = []

    def flush() -> None:
        nonlocal pending
        # header + separator + >=1 data row
        if len(pending) >= 2:
            header = pending[0]
            body = [r for r in pending[1:] if not is_separator(r)]
            if body:
                tables.append(Table(heading, header, body))
        pending = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [strip_md(c) for c in stripped.strip("|").split("|")]
            pending.append(cells)
            continue
        flush()
        if stripped.startswith("#"):
            heading = strip_md(stripped.lstrip("#").strip())
    flush()
    return tables


def parse_headings(text: str) -> list[tuple[int, str]]:
    """(level, text) for real headings, ignoring fenced code blocks."""
    out: list[tuple[int, str]] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if m := re.match(r"^(#{1,6})\s+(.*)$", line):
            out.append((len(m.group(1)), strip_md(m.group(2))))
    return out


def section_text(text: str, heading_pattern: str) -> str:
    """Body under the first heading matching the pattern, to the next same-or-higher heading."""
    lines = text.splitlines()
    start = level = None
    for i, line in enumerate(lines):
        if m := re.match(r"^(#{1,6})\s+(.*)$", line):
            if start is None and re.search(heading_pattern, strip_md(m.group(2)), re.I):
                start, level = i, len(m.group(1))
            elif start is not None and len(m.group(1)) <= level:
                return "\n".join(lines[start:i])
    return "\n".join(lines[start:]) if start is not None else ""


# ----------------------------------------------------------------- enumerators

def enumerate_items(text: str, spec: dict) -> list[str]:
    kind = spec["type"]

    if kind == "headings":
        pattern = spec["pattern"]
        return [
            h for _, h in parse_headings(text)
            if re.search(pattern, h, re.I)
        ]

    if kind == "table_rows":
        for table in parse_tables(text):
            if not re.search(spec["in_section"], table.heading, re.I):
                continue
            col = table.column(spec.get("column", "")) or 0
            rows = []
            for row in table.rows:
                if col >= len(row):
                    continue
                if flt := spec.get("where"):
                    idx = table.column(flt["column"])
                    if idx is None or idx >= len(row):
                        continue
                    if not re.search(flt["matches"], row[idx], re.I):
                        continue
                if row[col]:
                    rows.append(row[col])
            return rows
        return []

    if kind == "table_cells":
        for table in parse_tables(text):
            if not re.search(spec["in_section"], table.heading, re.I):
                continue
            col = table.column(spec["column"])
            if col is None:
                return []
            cells = []
            for row in table.rows:
                if col >= len(row) or not row[col]:
                    continue
                # A criterion can legitimately apply to only some rows -- Conflict
                # Intensity is required for Dams and blank for Flows -- so filter
                # before asking, rather than manufacturing failures on rows the
                # quality bar never covered.
                if flt := spec.get("where"):
                    idx = table.column(flt["column"])
                    if idx is None or idx >= len(row):
                        continue
                    if not re.search(flt["matches"], row[idx], re.I):
                        continue
                cells.append(row[col])
            return cells
        return []

    raise ValueError(f"unknown enumerator type {kind!r}")


def norm(s: str) -> str:
    """Aggressive normalization for fuzzy containment between prose and table cells."""
    s = strip_md(s).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s.replace("‑", "-").replace("–", "-"))
    return re.sub(r"\s+", " ", s).strip()


def overlaps(needle: str, haystack: list[str]) -> bool:
    """Does `needle` correspond to any entry in `haystack`?

    Generated prose renames things between sections ("Everything Free" in a heading
    vs "Keep everything free forever" in a table), so exact matching would produce
    false failures. Compares significant-word overlap instead.
    """
    STOP = {"the", "a", "an", "of", "for", "and", "or", "to", "in", "all", "no", "with"}
    n_words = {w for w in norm(needle).split() if w not in STOP and len(w) > 2}
    if not n_words:
        return False
    for candidate in haystack:
        c_words = {w for w in norm(candidate).split() if w not in STOP and len(w) > 2}
        if not c_words:
            continue
        shared = n_words & c_words
        if len(shared) / min(len(n_words), len(c_words)) >= 0.5:
            return True
    return False


# --------------------------------------------------------------- Jev transport

def ask_jev(state, questions: dict, api_key: str) -> dict:
    request = urllib.request.Request(
        TYPESAFE_ENDPOINT,
        data=json.dumps({"state": state, "model": MODEL, "questions": questions}).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"Jev {exc.code}: {exc.read().decode()[:300]}") from exc


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for line in (EVAL_DIR / ".env").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


# ------------------------------------------------------------------- scoring

# Jev returns a probability; code owns the thresholds. Anything between the two
# goes to a person rather than either bucket -- the three-way split TypeSafe's
# Confidence page recommends. These are provisional until calibration.
YES, NO = 0.70, 0.30


def score_document(doc: str, spec: dict, api_key: str | None) -> dict:
    items = {name: enumerate_items(doc, e) for name, e in spec["enumerators"].items()}
    result = {"enumerated": {k: len(v) for k, v in items.items()},
              "structural": [], "semantic": []}

    for check in spec["structural"]:
        kind = check["kind"]
        if kind == "subset":
            source = items[check["items"]]
            missing = [i for i in source if not overlaps(i, items[check["within"]])]
            if not source:
                # "every element of the empty set is in the map" is vacuously true.
                # A document that produced no items at all did not satisfy the bar,
                # so record it as a failure rather than a free pass.
                passed, detail = False, {"vacuous": True}
            else:
                passed, detail = not missing, {"missing": missing}
        elif kind == "min_count":
            got = len(items[check["items"]])
            passed, detail = got >= check["n"], {"found": got, "required": check["n"]}
        elif kind == "section_present":
            passed = bool(section_text(doc, check["pattern"]))
            detail = {}
        elif kind == "cells_match":
            # A criterion a regex can decide belongs here, not in the semantic
            # layer. Jev reads literally and is explicitly not a calculator, so
            # asking it "is there a number 1-5 in this cell" both wastes a call
            # and introduces avoidable variance.
            cells = items[check["items"]]
            bad = [c for c in cells if not re.search(check["pattern"], c)]
            passed = bool(cells) and not bad
            detail = {"failing_cells": bad, "vacuous": not cells}
        else:
            raise ValueError(f"unknown structural check {kind!r}")
        result["structural"].append({"id": check["id"], "passed": passed,
                                     "desc": check["desc"], **detail})

    # Build one Jev request per criterion: state is the array of enumerated items,
    # one question per item. Jev ingests state once and answers in parallel.
    for check in spec["semantic"]:
        values = items[check["each"]]
        if check.get("scope_section"):
            # For heading-based items, send the section body rather than the title.
            values = [section_text(doc, re.escape(v)) or v for v in values]

        entry = {"id": check["id"], "bar": check["bar"], "n": len(values)}
        if not values:
            entry |= {"skipped": "no items enumerated", "results": []}
            result["semantic"].append(entry)
            continue
        if api_key is None:
            entry |= {"skipped": "dry-run", "results": []}
            result["semantic"].append(entry)
            continue

        questions = {
            f"item_{i}": {
                "type": "noul",
                "instructions": check["instructions"].replace("{i}", str(i)),
                "criteria": check["criteria"],
            }
            for i in range(len(values))
        }
        response = ask_jev({"items": values}, questions, api_key)
        scores = [response["answers"][f"item_{i}"]["noul"] for i in range(len(values))]
        entry |= {
            "results": [
                {"item": v[:90], "noul": round(s, 3),
                 "verdict": "pass" if s >= YES else "fail" if s < NO else "review"}
                for v, s in zip(values, scores)
            ],
            "passed": all(s >= YES for s in scores),
            "needs_review": [round(s, 3) for s in scores if NO <= s < YES],
            "input_tokens": response["usage"]["input_tokens"],
        }
        result["semantic"].append(entry)

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills", help="comma-separated skill names")
    parser.add_argument("--arm", default="with_skill", choices=["with_skill", "without_skill", "both"])
    parser.add_argument("--dry-run", action="store_true", help="enumerate only, no Jev calls")
    args = parser.parse_args()

    wanted = [s.strip() for s in args.skills.split(",")] if args.skills else None
    api_key = None if args.dry_run else load_env().get("TYPESAFE_API_KEY")
    if not args.dry_run and not api_key:
        sys.exit("TYPESAFE_API_KEY not found in eval-framework/.env")

    generations = []
    for path in sorted(CACHE_DIR.glob("*.json")):
        d = json.loads(path.read_text())
        short = d["skill"].removeprefix("edbx-")
        if wanted and short not in wanted and d["skill"] not in wanted:
            continue
        if args.arm != "both" and d["arm"] != args.arm:
            continue
        spec_path = REPO / "edbx" / d["skill"] / "conformance.json"
        if spec_path.is_file():
            generations.append((d, json.loads(spec_path.read_text())))

    if not generations:
        sys.exit("no generations matched (need a conformance.json for the skill)")

    totals = {"struct_pass": 0, "struct_total": 0, "sem_pass": 0, "sem_total": 0, "review": 0}

    for doc, spec in generations:
        print(f"\n{'='*78}\n{doc['skill'].removeprefix('edbx-')} / {doc['scenario']} [{doc['arm']}]\n{'='*78}")
        scored = score_document(doc["output"], spec, api_key)
        print("  enumerated: " + ", ".join(f"{k}={v}" for k, v in scored["enumerated"].items()))

        print("\n  STRUCTURAL (code)")
        for c in scored["structural"]:
            totals["struct_total"] += 1
            totals["struct_pass"] += c["passed"]
            mark = "PASS" if c["passed"] else "FAIL"
            print(f"    [{mark}] {c['desc']}")
            if c.get("vacuous"):
                print("           vacuous: no items were produced to check")
            for m in c.get("missing", []):
                print(f"           not in map: {m[:70]}")
            for cell in c.get("failing_cells", []):
                print(f"           cell fails pattern: {cell[:60]!r}")
            if "found" in c and not c["passed"]:
                print(f"           found {c['found']}, need {c['required']}")

        print("\n  SEMANTIC (Jev)")
        for c in scored["semantic"]:
            if "skipped" in c:
                print(f"    [skip] {c['id']} ({c['skipped']}, {c['n']} items)")
                continue
            for r in c["results"]:
                totals["sem_total"] += 1
                totals["sem_pass"] += r["verdict"] == "pass"
                totals["review"] += r["verdict"] == "review"
            mark = "PASS" if c["passed"] else "FAIL"
            print(f"    [{mark}] {c['id']}  ({c['n']} items)")
            for r in c["results"]:
                print(f"           {r['noul']:.2f} {r['verdict']:6s} {r['item'][:62]}")

    print(f"\n{'='*78}")
    if totals["struct_total"]:
        print(f"structural: {totals['struct_pass']}/{totals['struct_total']} passed")
    if totals["sem_total"]:
        print(f"semantic  : {totals['sem_pass']}/{totals['sem_total']} passed, "
              f"{totals['review']} need human review")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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
from dataclasses import dataclass, field
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
    ancestry: list[str] = field(default_factory=list)

    def under(self, pattern: str) -> bool:
        """Is this table anywhere beneath a heading matching `pattern`?

        Generated output often splits one logical section across subheadings --
        a Consequence Map with a table per feature -- so matching only the
        immediately preceding heading silently finds nothing.
        """
        return any(re.search(pattern, h, re.I) for h in [*self.ancestry, self.heading])

    def column(self, name_fragment: str) -> int | None:
        for i, h in enumerate(self.header):
            if name_fragment.lower() in h.lower():
                return i
        return None


def parse_tables(text: str) -> list[Table]:
    """Every markdown table in the document, tagged with the heading above it."""
    tables: list[Table] = []
    stack: list[tuple[int, str]] = []
    pending: list[list[str]] = []

    def flush() -> None:
        nonlocal pending
        # header + separator + >=1 data row
        if len(pending) >= 2:
            header = pending[0]
            body = [r for r in pending[1:] if not is_separator(r)]
            if body:
                heading = stack[-1][1] if stack else ""
                ancestry = [h for _, h in stack[:-1]]
                tables.append(Table(heading, header, body, ancestry))
        pending = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [strip_md(c) for c in stripped.strip("|").split("|")]
            pending.append(cells)
            continue
        flush()
        if m := re.match(r"^(#{1,6})\s+(.*)$", stripped):
            level, title = len(m.group(1)), strip_md(m.group(2))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
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


def _dividers(text: str) -> list[tuple[int, int, str]]:
    """(line index, level, title) for headings and bold-line pseudo-headings.

    Generated output frequently labels a section with a bold line rather than a
    real heading -- `**Section 9 - BOTTOM LINE**`, `**Future Direction**`. Treating
    only `#` as structure makes those sections invisible, which silently skips the
    criteria that depend on them.
    """
    out: list[tuple[int, int, str]] = []
    for i, line in enumerate(text.splitlines()):
        stripped = line.strip()
        if m := re.match(r"^(#{1,6})\s+(.*)$", stripped):
            out.append((i, len(m.group(1)), strip_md(m.group(2))))
        elif m := re.match(r"^\*\*(.+?)\*\*:?\s*$", stripped):
            # Weaker than any real heading, so a following `#` still closes it.
            out.append((i, 7, strip_md(m.group(1))))
    return out


def section_text(text: str, heading_pattern: str, pick: str = "first") -> str:
    """Body under a heading matching the pattern, to the next same-or-higher one.

    `pick="last"` selects the final match, for bars about how a document *closes*.
    With an alternation pattern the first match is whichever alternative appears
    earliest, which is not the same thing.
    """
    lines = text.splitlines()
    dividers = _dividers(text)
    matches = [n for n, (_, _, title) in enumerate(dividers)
               if re.search(heading_pattern, title, re.I)]
    if not matches:
        return ""
    n = matches[-1] if pick == "last" else matches[0]
    idx, level, _ = dividers[n]
    for next_idx, next_level, _ in dividers[n + 1:]:
        if next_level <= level:
            return "\n".join(lines[idx:next_idx])
    return "\n".join(lines[idx:])


# ----------------------------------------------------------------- enumerators

def enumerate_items(text: str, spec: dict) -> list[str]:
    kind = spec["type"]

    if kind == "headings":
        # Includes bold-label pseudo-headings: the same skill labels a trade-off
        # entry "### Hard Dam: X" in one run and "**X (Hard Dam):**" in the next,
        # and reading only `#` headings made the second form enumerate nothing.
        pattern = spec["pattern"]
        return [
            title for _, _, title in _dividers(text)
            if re.search(pattern, title, re.I)
        ]

    if kind == "table_rows":
        rows = []
        for table in parse_tables(text):
            if not table.under(spec["in_section"]):
                continue
            col = table.column(spec.get("column", "")) or 0
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

    if kind == "table_cells":
        cells = []
        for table in parse_tables(text):
            if not table.under(spec["in_section"]):
                continue
            col = table.column(spec["column"])
            if col is None:
                continue
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


def lookup_prompt(skill: str, scenario: str) -> str:
    """The originating prompt, needed by bars that depend on what was asked for.

    Generations do not store it, so recover it from the eval set by scenario name,
    falling back to the id-derived name the harness uses when `name` is absent.
    """
    path = EVAL_DIR / skill / "evals.json"
    if not path.is_file():
        return ""
    for entry in json.loads(path.read_text())["evals"]:
        if (entry.get("name") or f"eval-{entry.get('id')}") == scenario:
            return entry["prompt"]
    return ""


# ------------------------------------------------------------------- scoring

# Jev returns a probability; code owns the thresholds. Anything between the two
# goes to a person rather than either bucket -- the three-way split TypeSafe's
# Confidence page recommends. These are provisional until calibration.
YES, NO = 0.70, 0.30


def score_document(doc: str, spec: dict, api_key: str | None, prompt: str = "") -> dict:
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
        elif kind == "distinct_coverage":
            # "spans at least 4 of the 6 harm categories" -- set arithmetic, not a
            # judgment, and Jev explicitly cannot count.
            blob = " ".join(items[check["items"]]).lower()
            found = sorted(v for v in check["vocabulary"] if v.lower() in blob)
            passed = len(found) >= check["n"]
            detail = {"found": len(found), "required": check["n"], "covered": found}
        elif kind == "min_count_matching":
            matching = [c for c in items[check["items"]] if re.search(check["pattern"], c, re.I)]
            passed = len(matching) >= check["n"]
            detail = {"found": len(matching), "required": check["n"]}
        elif kind == "conditional_section":
            # Some bars depend on what was actually asked for -- dah-cards must not
            # emit a Manifesto unless the user requested one. Needs the prompt.
            requested = bool(re.search(check["when_prompt_matches"], prompt, re.I))
            present = bool(section_text(doc, check["pattern"]))
            passed = (present == requested)
            detail = {"requested": requested, "present": present}
        elif kind == "any_of":
            # "completes all five tools OR states which were run and why" -- the
            # bar is genuinely disjunctive, so flattening it would fail correct work.
            outcomes = []
            for sub in check["checks"]:
                if sub["kind"] == "min_count":
                    outcomes.append(len(items[sub["items"]]) >= sub["n"])
                elif sub["kind"] == "section_present":
                    outcomes.append(bool(re.search(sub["pattern"], doc, re.I)))
                else:
                    raise ValueError(f"any_of cannot nest {sub['kind']!r}")
            passed = any(outcomes)
            detail = {"branches": outcomes}
        elif kind == "section_implies_section":
            # A tool that did not run cannot owe its output. Only require the
            # consequent when the antecedent is actually present.
            # Match a real section, not a passing mention: a run that consumed a
            # *prior* Ethics Frame as input does not owe an Ethics Frame's output.
            antecedent = bool(section_text(doc, check["if_present"]))
            consequent = bool(re.search(check["then_present"], doc, re.I))
            passed = consequent or not antecedent
            detail = {"antecedent": antecedent, "consequent": consequent}
        elif kind == "implied_section":
            # If the trigger set is non-empty, the section becomes required.
            triggered = bool(items[check["items"]])
            present = bool(re.search(check["pattern"], doc, re.I))
            passed = present or not triggered
            detail = {"triggered_by": len(items[check["items"]]), "present": present}
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
        if check.get("scope") == "tail":
            # For bars about how a document *closes*: the final quarter, at least
            # 15 lines. Independent of what the closing section happens to be
            # called, so an edit that renames it cannot move the score by itself.
            lines = doc.splitlines()
            values = ["\n".join(lines[-max(15, len(lines) // 4):])]
        elif check.get("scope") == "document":
            # Bars about the whole chain ("at least 5 values across the chain")
            # need the whole document, not whichever heading matched first.
            values = [doc]
        elif "section" in check:
            # A whole-document judgment rather than a per-item one. Scope the state
            # to the relevant section: accuracy falls as state grows with detail
            # unrelated to the question.
            body = section_text(doc, check["section"], check.get("pick", "first"))
            values = [body] if body.strip() else []
        else:
            values = items[check["each"]]
            if check.get("scope_section"):
                # For heading-based items, send the section body, not the title.
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

        kind = check.get("type", "noul")
        questions = {
            f"item_{i}": {
                "type": kind,
                "instructions": check["instructions"].replace("{i}", str(i)),
                "criteria": check["criteria"],
            }
            for i in range(len(values))
        }
        response = ask_jev({"items": values}, questions, api_key)
        answers = [response["answers"][f"item_{i}"] for i in range(len(values))]

        if kind == "score":
            # Jev cannot reconstruct an exact number by interpolating between
            # levels, but thresholding the expectation against a named level is
            # supported. `min_level` is the index the answer must reach.
            floor = check["min_level"]
            scores = [a["score"] for a in answers]
            verdicts = ["pass" if s >= floor else "fail" for s in scores]
            entry |= {
                "results": [
                    {"item": v[:90], "noul": round(s, 2), "verdict": verdict,
                     "legend": a.get("legend", {}).get(str(int(round(s))), "")}
                    for v, s, verdict, a in zip(values, scores, verdicts, answers)
                ],
                "passed": all(v == "pass" for v in verdicts),
                "min_level": floor,
            }
        else:
            scores = [a["noul"] for a in answers]
            entry |= {
                "results": [
                    {"item": v[:90], "noul": round(s, 3),
                     "verdict": "pass" if s >= YES else "fail" if s < NO else "review"}
                    for v, s in zip(values, scores)
                ],
                "passed": all(s >= YES for s in scores),
                "needs_review": [round(s, 3) for s in scores if NO <= s < YES],
            }
        entry["input_tokens"] = response["usage"]["input_tokens"]
        result["semantic"].append(entry)

    return result


def select_generations(
    wanted: list[str] | None, arm: str, reps: int, skill_ref: str | None = None,
) -> tuple[list, list[str]]:
    """Generations matching the *current* SKILL.md, via the harness's own task keys.

    The cache keeps every version a skill has ever had. Scoring by glob would mix
    outputs from before and after an edit and report their average as either one.
    Returns (matched, missing labels).
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from run_generation import DEFAULT_MODEL, build_tasks  # noqa: E402

    arms = ("without_skill", "with_skill") if arm == "both" else (arm,)
    tasks = build_tasks(wanted, None, DEFAULT_MODEL, reps, arms, skill_ref)
    matched, missing = [], []
    for task in tasks:
        spec_path = REPO / "edbx" / task.skill / "conformance.json"
        if not spec_path.is_file():
            continue
        gen_path = CACHE_DIR / f"{task.key}.json"
        if not gen_path.is_file():
            missing.append(task.label)
            continue
        d = json.loads(gen_path.read_text())
        d["prompt"] = task.prompt
        d["rep"] = task.rep
        matched.append((d, json.loads(spec_path.read_text())))
    return matched, missing


def print_document(doc: dict, scored: dict) -> None:
    rep = f" #{doc['rep']}" if doc.get("rep") else ""
    print(f"\n{'='*78}\n{doc['skill'].removeprefix('edbx-')} / {doc['scenario']}{rep} [{doc['arm']}]\n{'='*78}")
    print("  enumerated: " + ", ".join(f"{k}={v}" for k, v in scored["enumerated"].items()))
    print("\n  STRUCTURAL (code)")
    for c in scored["structural"]:
        print(f"    [{'PASS' if c['passed'] else 'FAIL'}] {c['desc']}")
        if c.get("vacuous"):
            print("           vacuous: no items were produced to check")
        for m in c.get("missing", []):
            print(f"           not in map: {m[:70]}")
        for cell in c.get("failing_cells", []):
            print(f"           cell fails pattern: {cell[:60]!r}")
        if "found" in c and not c["passed"]:
            print(f"           found {c['found']}, need {c['required']}")
        if "covered" in c:
            print(f"           covered: {', '.join(c['covered']) or '(none)'}")
        if "requested" in c and not c["passed"]:
            print("           " + ("requested but absent" if c["requested"] else "present but never requested"))
        if "triggered_by" in c and not c["passed"]:
            print(f"           required by {c['triggered_by']} finding(s), but absent")
        if "antecedent" in c:
            state = "required and present" if c["antecedent"] and c["consequent"] else \
                    "required but absent" if c["antecedent"] else "not required"
            print(f"           {state}")
    print("\n  SEMANTIC (Jev)")
    for c in scored["semantic"]:
        if "skipped" in c:
            print(f"    [skip] {c['id']} ({c['skipped']}, {c['n']} items)")
            continue
        print(f"    [{'PASS' if c['passed'] else 'FAIL'}] {c['id']}  ({c['n']} items)")
        for r in c["results"]:
            print(f"           {r['noul']:.2f} {r['verdict']:6s} {r['item'][:62]}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills", help="comma-separated skill names")
    parser.add_argument("--arm", default="with_skill", choices=["with_skill", "without_skill", "both"])
    parser.add_argument("--reps", type=int, default=1, help="score reps 0..N-1 per scenario")
    parser.add_argument("--skill-ref", help="score generations made from SKILL.md as of this git ref")
    parser.add_argument("--json", metavar="PATH", help="write per-check pass rates here")
    parser.add_argument("--quiet", action="store_true", help="summary only, no per-document detail")
    parser.add_argument("--dry-run", action="store_true", help="enumerate only, no Jev calls")
    args = parser.parse_args()

    wanted = [s.strip() for s in args.skills.split(",")] if args.skills else None
    api_key = None if args.dry_run else load_env().get("TYPESAFE_API_KEY")
    if not args.dry_run and not api_key:
        sys.exit("TYPESAFE_API_KEY not found in eval-framework/.env")

    generations, missing = select_generations(wanted, args.arm, args.reps, args.skill_ref)
    if missing:
        print(f"! {len(missing)} expected generation(s) not in cache -- run run_generation.py first:")
        for label in missing[:10]:
            print(f"    {label}")
    if not generations:
        sys.exit("no generations matched (need a conformance.json and cached output)")

    # check id -> outcome counts, per skill. A per-item semantic check passes for a
    # document only if every item passes; "skip" means nothing was enumerated.
    rates: dict[str, dict[str, dict[str, int]]] = {}
    documents: list[dict] = []

    for doc, spec in generations:
        scored = score_document(doc["output"], spec, api_key, doc.get("prompt", ""))
        if not args.quiet:
            print_document(doc, scored)
        skill_rates = rates.setdefault(doc["skill"], {})
        outcome_row = {"skill": doc["skill"], "scenario": doc["scenario"],
                       "rep": doc.get("rep", 0), "arm": doc["arm"], "checks": {}}
        for c in scored["structural"]:
            o = "pass" if c["passed"] else "fail"
            skill_rates.setdefault(c["id"], {"pass": 0, "fail": 0, "skip": 0, "review": 0})[o] += 1
            outcome_row["checks"][c["id"]] = o
        for c in scored["semantic"]:
            bucket = skill_rates.setdefault(c["id"], {"pass": 0, "fail": 0, "skip": 0, "review": 0})
            if "skipped" in c:
                o = "skip"
            elif c["passed"]:
                o = "pass"
            elif any(r["verdict"] == "review" for r in c["results"]) and \
                    not any(r["verdict"] == "fail" for r in c["results"]):
                o = "review"
            else:
                o = "fail"
            bucket[o] += 1
            outcome_row["checks"][c["id"]] = o
        documents.append(outcome_row)

    print(f"\n{'='*78}\nPER-CHECK PASS RATE  ({args.arm}, {args.reps} rep(s) per scenario)\n{'='*78}")
    grand_pass = grand_total = 0
    for skill, checks in rates.items():
        print(f"\n{skill.removeprefix('edbx-')}")
        for cid, o in checks.items():
            scored_n = o["pass"] + o["fail"] + o["review"]
            grand_pass += o["pass"]
            grand_total += scored_n + o["skip"]
            extra = "".join(f", {o[k]} {k}" for k in ("review", "skip") if o[k])
            flag = "" if o["fail"] == 0 and o["skip"] == 0 else "  <--"
            print(f"  {cid:36s} {o['pass']:>2}/{scored_n + o['skip']:<2} pass{extra}{flag}")
    if grand_total:
        print(f"\noverall: {grand_pass}/{grand_total} check-document pairs pass "
              f"({100 * grand_pass / grand_total:.0f}%)")

    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps({"arm": args.arm, "reps": args.reps,
                                               "rates": rates, "documents": documents}, indent=2))
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

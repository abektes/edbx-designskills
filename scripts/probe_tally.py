#!/usr/bin/env python3
"""Tally the baseline probe: docs/probe-v0.1/<skill>/scores.json -> one table.

Coverage counts `yes` as 1 and `partial` as 0.5 over all D-checks and outputs.
Invented (M1) and misstated (M2) are the share of outputs with the failure
(partial = 0.5). The verdict is read from checks.md's `## Verdict` section.

    python3 scripts/probe_tally.py                    # all scored skills
    python3 scripts/probe_tally.py --skills cider     # validate one
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROBE_DIR = Path(__file__).resolve().parent.parent / "docs" / "probe-v0.1"
SCORE = {"yes": 1.0, "partial": 0.5, "no": 0.0}


def tally(skill_dir: Path) -> dict:
    data = json.loads((skill_dir / "scores.json").read_text())
    outputs = data["outputs"]
    if not outputs:
        raise ValueError("no outputs scored")
    d_total = d_n = 0.0
    m1 = m2 = 0.0
    for scen, checks in outputs.items():
        for cid, c in checks.items():
            if c.get("v") not in SCORE:
                raise ValueError(f"{scen}/{cid}: verdict {c.get('v')!r} not yes/partial/no")
            if c["v"] != "no" and not c.get("q"):
                raise ValueError(f"{scen}/{cid}: {c['v']} needs a quote in q")
            if re.fullmatch(r"D\d+", cid):
                d_total += SCORE[c["v"]]
                d_n += 1
        for mid in ("M1", "M2"):
            if mid not in checks:
                raise ValueError(f"{scen}: missing {mid}")
        m1 += SCORE[checks["M1"]["v"]]
        m2 += SCORE[checks["M2"]["v"]]
    n = len(outputs)
    verdict = "?"
    checks_md = skill_dir / "checks.md"
    if checks_md.is_file():
        m = re.search(r"## Verdict\s+\**(handles it|partial|weak)", checks_md.read_text(), re.I)
        if m:
            verdict = m.group(1).lower()
    return {"skill": skill_dir.name, "outputs": n,
            "coverage": d_total / d_n if d_n else 0.0,
            "invents": m1 / n, "misstates": m2 / n, "verdict": verdict}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skills", help="comma-separated short names (default: all)")
    args = ap.parse_args()
    wanted = {s.strip().removeprefix("edbx-") for s in args.skills.split(",")} if args.skills else None

    rows, errors = [], 0
    for d in sorted(p for p in PROBE_DIR.glob("edbx-*") if p.is_dir()):
        if wanted and d.name.removeprefix("edbx-") not in wanted:
            continue
        if not (d / "scores.json").is_file():
            print(f"  ! {d.name}: no scores.json", file=sys.stderr)
            errors += 1
            continue
        try:
            rows.append(tally(d))
        except (ValueError, KeyError, json.JSONDecodeError) as e:
            print(f"  ! {d.name}: {e}", file=sys.stderr)
            errors += 1

    print("| Skill | Plain model: method coverage | Invents facts | Misstates method | Verdict |")
    print("|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['skill']} | {r['coverage']:.0%} | {r['invents']:.0%} | "
              f"{r['misstates']:.0%} | {r['verdict']} |")
    print(f"\n{len(rows)} skill(s) tallied, {errors} problem(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

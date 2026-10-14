#!/usr/bin/env python3
"""Write the exact texts each semantic (Jev) check would be sent, for labelling.

Calibration cases must look like what the scorer sends in production: a whole
section, the document tail, or one enumerated item. This runs the scorer's own
extraction (conformance.semantic_values) on the cached generations and writes,
per check, every text it would send, with the check's bar and Jev instructions
on top. No Jev calls.

    python3 scripts/dump_semantic_inputs.py --skills worrystorming
    python3 scripts/dump_semantic_inputs.py --skills cider --skill-ref 0d314a1

Output: eval-framework/calibration/inputs/<skill>/<check_id>.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conformance import (  # noqa: E402
    EVAL_DIR, enumerate_items, normalize_doc, select_generations, semantic_values,
)

OUT_DIR = EVAL_DIR / "calibration" / "inputs"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skills", required=True, help="comma-separated short names")
    ap.add_argument("--arm", default="both", choices=["with_skill", "without_skill", "both"])
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--skill-ref", help="generations made from SKILL.md as of this git ref")
    args = ap.parse_args()
    wanted = [s.strip() for s in args.skills.split(",")]

    matched, missing = select_generations(wanted, args.arm, args.reps, args.skill_ref)
    if missing:
        print(f"  ! {len(missing)} generation(s) not cached: {', '.join(missing[:4])}", file=sys.stderr)

    texts: dict[tuple[str, str], list[tuple[str, str]]] = {}
    specs: dict[str, dict] = {}
    for gen, spec in matched:
        doc = normalize_doc(gen["output"])
        items = {name: enumerate_items(doc, e) for name, e in spec["enumerators"].items()}
        short = gen["skill"].removeprefix("edbx-")
        specs[short] = spec
        where = f"{gen['scenario']} #{gen.get('rep', 0)} [{gen['arm']}]"
        for check in spec["semantic"]:
            for v in semantic_values(doc, check, items):
                texts.setdefault((short, check["id"]), []).append((where, v))

    written = 0
    for short, spec in specs.items():
        for check in spec["semantic"]:
            found = texts.get((short, check["id"]), [])
            out = OUT_DIR / short / f"{check['id']}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            parts = [
                f"# {short} / {check['id']}", "",
                f"**Bar:** {check['bar']}", "",
                f"**Jev instructions:** {check['instructions']}", "",
                f"**Jev criteria:** {json.dumps(check['criteria'], ensure_ascii=False)}", "",
                f"**Texts the scorer sends:** {len(found)}", "",
            ]
            for i, (where, v) in enumerate(found):
                parts += [f"## Text {i} — {where}", "", "````", v.strip(), "````", ""]
            out.write_text("\n".join(parts), encoding="utf-8")
            written += 1
    print(f"wrote {written} check file(s) under {OUT_DIR.relative_to(EVAL_DIR.parent)}")


if __name__ == "__main__":
    main()

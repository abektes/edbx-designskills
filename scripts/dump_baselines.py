#!/usr/bin/env python3
"""Write the cached without_skill outputs as Markdown files for the baseline probe.

The probe reads what the plain model produced when told only the method's name
(see BASELINE_SYSTEM in run_generation.py). This copies those cached outputs,
with the scenario prompt and the method name the model was given, to
eval-framework/_probe/v0.1/<skill>/<scenario>.md. No API calls.

    python3 scripts/dump_baselines.py                 # all skills
    python3 scripts/dump_baselines.py --skills cider,worrystorming
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_generation import (  # noqa: E402
    CACHE_DIR, EVAL_DIR, SKILLS_DIR, evals_path, method_name,
)

OUT_DIR = EVAL_DIR / "_probe" / "v0.1"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skills", help="comma-separated short names (default: all)")
    args = ap.parse_args()
    wanted = {s.strip().removeprefix("edbx-") for s in args.skills.split(",")} if args.skills else None

    outputs: dict[tuple[str, str], list[dict]] = {}
    for f in sorted(CACHE_DIR.glob("*.json")):
        d = json.loads(f.read_text())
        if d.get("arm") != "without_skill":
            continue
        outputs.setdefault((d["skill"], d["scenario"]), []).append(d)

    written = 0
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        name = skill_dir.name
        if name == "edbx" or (wanted and name.removeprefix("edbx-") not in wanted):
            continue
        eval_file = evals_path(name)
        if not eval_file.is_file():
            continue
        method = method_name((skill_dir / "SKILL.md").read_text(encoding="utf-8"), name)
        for i, entry in enumerate(json.loads(eval_file.read_text())["evals"]):
            scenario = entry.get("name") or f"eval-{entry.get('id', i)}"
            runs = sorted(outputs.get((name, scenario), []), key=lambda d: d.get("rep", 0))
            if not runs:
                print(f"  ! {name} / {scenario}: no cached baseline", file=sys.stderr)
                continue
            out = OUT_DIR / name / f"{scenario}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            parts = [
                f"<!-- baseline output; model told only the method name: {method} -->",
                "## Prompt", "", entry.get("prompt", "").strip(), "",
            ]
            for d in runs:
                parts += [f"## Output (rep {d.get('rep', 0)}, {d.get('served_model', '')})", "",
                          d["output"].strip(), ""]
            out.write_text("\n".join(parts), encoding="utf-8")
            written += 1
    print(f"wrote {written} files under {OUT_DIR.relative_to(EVAL_DIR.parent)}")


if __name__ == "__main__":
    main()

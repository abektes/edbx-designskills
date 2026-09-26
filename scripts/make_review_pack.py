#!/usr/bin/env python3
"""Build a blind side-by-side page so a person can judge output quality, not just conformance.

Conformance scores show the skills are *followed*. Whether their outputs are *better*
than the model's unaided attempt needs a human reader. This pairs each cached baseline
output with the with-skill output made from the current SKILL.md, shuffles which side
is which, and writes two files to the gitignored eval-framework/review/:

  review.html   three tabs (Set A, B, C), one scenario per skill in each, 21 pairs a set
  key.json      which side was the skill; open only after you have reviewed

Set A holds every skill's first eval scenario, Set B the second, Set C the third, so
one set is a full pass over the box and the others add repeats.

Nothing is generated here. A pair whose with-skill output predates the current
SKILL.md is left out and reported; run run_generation.py first to fill it in.

Blinding is partial: with-skill outputs use the method's own section names and run
longer, so a careful reader can often tell them apart. The questions ask about
qualities that matter either way.

    python3 scripts/make_review_pack.py
    python3 scripts/make_review_pack.py --score ~/Downloads/edbx-review-answers.json
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

from run_generation import CACHE_DIR, EVAL_DIR, build_tasks

MODEL = "deepseek/deepseek-v4-pro"
REVIEW_DIR = EVAL_DIR / "review"
SEED = 20260924
SETS = "ABC"

QUESTIONS = [
    ("meeting", "Which would you rather bring into a design meeting?"),
    ("insight", "Which made you see the problem differently?"),
    ("trust", "Which is easier to trust? Can you tell fact from assumption?"),
    ("action", "Which gives you clearer next steps?"),
    ("length", "Is either longer than what it gives you?"),
]
# Sides are 1 and 2 so they cannot be confused with the set tabs A, B, C.
CHOICES = ["1", "2", "tie"]
LENGTH_CHOICES = ["1 too long", "2 too long", "both", "neither"]


# ------------------------------------------------------------------ markdown

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", text)
    return text.replace("&lt;br&gt;", "<br>")


def md_to_html(md: str) -> str:
    """Enough Markdown for model outputs: headings, lists, tables, quotes, fences, rules."""
    out: list[str] = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            i += 1
            block = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            out.append("<pre>" + html.escape("\n".join(block)) + "</pre>")
        elif re.fullmatch(r"[-*_]{3,}", stripped):
            out.append("<hr>")
            i += 1
        elif m := re.match(r"(#{1,6})\s+(.*)", stripped):
            level = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
        elif stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows
                     if not set(r.replace("|", "").strip()) <= set("-: ")]
            if cells:
                head, *body = cells
                out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>")
                out += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body]
                out.append("</tbody></table>")
        elif stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(quote)) + "</blockquote>")
        elif re.match(r"(?:[-*+]|\d+[.)])\s+", stripped):
            ordered = bool(re.match(r"\d+[.)]", stripped))
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>")
            while i < len(lines) and re.match(r"\s*(?:[-*+]|\d+[.)])\s+", lines[i]):
                item = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("    ") and not re.match(r"\s*(?:[-*+]|\d+[.)])\s+", lines[i]):
                    item += " " + lines[i].strip()
                    i += 1
                out.append(f"<li>{inline(item)}</li>")
            out.append(f"</{tag}>")
        else:
            para = [stripped]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"\s*(?:#|\||>|```|[-*+]\s|\d+[.)]\s)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append("<p>" + inline(" ".join(para)) + "</p>")
    return "\n".join(out)


# ------------------------------------------------------------------ building

def collect() -> tuple[dict[str, list[dict]], list[str]]:
    """Pairs grouped by set letter, plus labels of pairs that could not be built."""
    by_scenario: dict[tuple[str, str], dict] = {}
    order: dict[str, list[str]] = {}
    for task in build_tasks(None, None, MODEL, reps=1):
        slot = by_scenario.setdefault((task.skill, task.scenario), {"prompt": task.prompt})
        path = CACHE_DIR / f"{task.key}.json"
        slot[task.arm] = json.loads(path.read_text())["output"] if path.is_file() else None
        if task.scenario not in order.setdefault(task.skill, []):
            order[task.skill].append(task.scenario)

    sets: dict[str, list[dict]] = {s: [] for s in SETS}
    missing = []
    for skill, scenarios in sorted(order.items()):
        for letter, scenario in zip(SETS, scenarios):
            slot = by_scenario[(skill, scenario)]
            if not slot.get("with_skill") or not slot.get("without_skill"):
                missing.append(f"{skill}/{scenario}")
                continue
            sets[letter].append({"skill": skill, "scenario": scenario, **slot})
    return sets, missing


def question_html(pid: str) -> str:
    rows = []
    for qid, text in QUESTIONS:
        choices = LENGTH_CHOICES if qid == "length" else CHOICES
        radios = "".join(
            f"<label><input type='radio' name='{pid}-{qid}' value='{c}'> {c}</label>" for c in choices)
        rows.append(f"<div class='q'><span>{html.escape(text)}</span>{radios}</div>")
    return "".join(rows)


def build() -> int:
    sets, missing = collect()
    if not any(sets.values()):
        sys.exit("no scenario has both a baseline and a current with-skill output")

    rng = random.Random(SEED)
    key, tabs, panels, pids = {}, [], [], []
    for letter in SETS:
        toc, sections = [], []
        for n, pair in enumerate(sets[letter], start=1):
            pid = f"{letter}-{n:02d}"
            pids.append(pid)
            skill_first = rng.random() < 0.5
            one, two = ("with_skill", "without_skill") if skill_first else ("without_skill", "with_skill")
            key[pid] = {"skill": pair["skill"], "scenario": pair["scenario"], "1": one}
            title = f"{letter}{n}. {pair['skill'].removeprefix('edbx-').replace('-', ' ').title()}: {pair['scenario'].replace('-', ' ')}"
            toc.append(f"<li><a href='#{pid}'>{html.escape(title)}</a> <span class='done' data-pair='{pid}'></span></li>")
            sections.append(f"""
<section id='{pid}' class='pair'>
  <h2>{html.escape(title)}</h2>
  <p class='prompt'><strong>Prompt:</strong> {html.escape(pair['prompt'])}</p>
  <div class='cols'>
    <article><h3>Output 1 <small>{len(pair[one].split())} words</small></h3>{md_to_html(pair[one])}</article>
    <article><h3>Output 2 <small>{len(pair[two].split())} words</small></h3>{md_to_html(pair[two])}</article>
  </div>
  <div class='questions'>{question_html(pid)}
    <textarea name='{pid}-notes' placeholder='Notes: what made the difference?'></textarea>
  </div>
</section>""")
        tabs.append(f"<button class='tab' data-set='{letter}' onclick=\"showSet('{letter}')\">Set {letter} "
                    f"<span class='tabcount' data-set='{letter}'></span></button>")
        panels.append(f"<div class='panel' data-set='{letter}'><ol class='toc'>{''.join(toc)}</ol>{''.join(sections)}</div>")

    page = PAGE.format(tabs="".join(tabs), panels="\n".join(panels),
                       n=len(pids), per_set=max(len(v) for v in sets.values()),
                       pairs_json=json.dumps(pids))
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    (REVIEW_DIR / "review.html").write_text(page)
    (REVIEW_DIR / "key.json").write_text(json.dumps({"seed": SEED, "model": MODEL, "pairs": key}, indent=2))
    print(f"wrote {REVIEW_DIR / 'review.html'} ({len(pids)} pairs: " +
          ", ".join(f"set {s} {len(v)}" for s, v in sets.items()) + ")")
    print(f"wrote {REVIEW_DIR / 'key.json'} (do not open until you have reviewed)")
    if missing:
        print(f"left out {len(missing)} pair(s) with no current output: " + ", ".join(missing))
    return 0


# ------------------------------------------------------------------ scoring

def resolve_answers(answers_path: str) -> Path | None:
    """The given file, or the newest edbx-review-answers*.json beside it.
    Browsers rename repeat downloads ("edbx-review-answers (1).json")."""
    path = Path(answers_path).expanduser()
    if path.is_file():
        return path
    candidates = sorted(path.parent.glob("edbx-review-answers*.json"), key=lambda f: f.stat().st_mtime)
    return candidates[-1] if candidates else None


def verdict_for(qid: str, choice: str, skill_side: str) -> str:
    if qid == "length":
        side = {"1 too long": "1", "2 too long": "2"}.get(choice)
        if side is None:
            return choice
        return "skill too long" if side == skill_side else "baseline too long"
    if choice == "tie":
        return "tie"
    return "skill" if choice == skill_side else "baseline"


def score(answers_path: str) -> int:
    key = json.loads((REVIEW_DIR / "key.json").read_text())["pairs"]
    path = resolve_answers(answers_path)
    if path is None:
        sys.exit(
            f"No answers file at {answers_path} (or any edbx-review-answers*.json next to it).\n"
            "Open eval-framework/review/review.html in Safari or Chrome, answer at least one pair,\n"
            "then press Export answers. If the browser will not download, press Copy answers and\n"
            "save the clipboard as ~/Downloads/edbx-review-answers.json.")
    print(f"answers: {path}\n")
    answers = json.loads(path.read_text())

    tally = {qid: Counter() for qid, _ in QUESTIONS}
    by_set: dict[str, Counter] = {s: Counter() for s in SETS}
    by_skill: dict[str, Counter] = {}
    for pid, meta in key.items():
        skill_side = "1" if meta["1"] == "with_skill" else "2"
        for qid, _ in QUESTIONS:
            choice = answers.get(f"{pid}-{qid}")
            if not choice:
                continue
            verdict = verdict_for(qid, choice, skill_side)
            tally[qid][verdict] += 1
            if qid == "meeting":
                by_set[pid[0]][verdict] += 1
                by_skill.setdefault(meta["skill"], Counter())[verdict] += 1

    for qid, text in QUESTIONS:
        counts = ", ".join(f"{k}: {v}" for k, v in tally[qid].most_common())
        print(f"{text}\n   {counts or 'no answers'}")
    print("\nMeeting preference by set:")
    for letter, counts in by_set.items():
        print(f"   Set {letter}  " + (", ".join(f"{k}: {v}" for k, v in counts.most_common()) or "no answers"))
    print("\nMeeting preference by skill:")
    for skill, counts in sorted(by_skill.items()):
        print(f"   {skill.removeprefix('edbx-'):28s} " + ", ".join(f"{k}: {v}" for k, v in counts.most_common()))
    for pid, meta in key.items():
        if note := answers.get(f"{pid}-notes"):
            side = "1" if meta["1"] == "with_skill" else "2"
            print(f"\n{pid} ({meta['skill'].removeprefix('edbx-')}, skill was {side}): {note}")
    return 0


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>edbx review: baseline vs. with skill</title>
<style>
  body {{ font: 15px/1.5 -apple-system, system-ui, sans-serif; margin: 0; color: #1d1d1f; background: #fafafa; }}
  header, .pair, footer, .toc {{ max-width: 1500px; margin: 0 auto; padding: 16px 24px; box-sizing: border-box; }}
  header {{ border-bottom: 1px solid #ddd; }}
  h1 {{ font-size: 22px; margin: 8px 0; }}
  .tabs {{ position: sticky; top: 0; z-index: 2; background: #fafafa; border-bottom: 1px solid #ddd; padding: 8px 24px; display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }}
  .tab {{ font-weight: 600; }}
  .tab.active {{ background: #1d1d1f; color: #fff; border-color: #1d1d1f; }}
  .panel {{ display: none; }}
  .panel.active {{ display: block; }}
  .cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
  @media (max-width: 900px) {{ .cols {{ grid-template-columns: 1fr; }} }}
  article {{ background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 12px 16px; max-height: 75vh; overflow: auto; }}
  article h3 {{ position: sticky; top: -12px; background: #fff; margin: -12px -16px 8px; padding: 10px 16px; border-bottom: 1px solid #eee; }}
  article h3 small {{ color: #888; font-weight: normal; }}
  article h2, article h3:not(:first-child), article h4, article h5, article h6 {{ font-size: 15px; }}
  table {{ border-collapse: collapse; font-size: 13px; margin: 8px 0; }}
  th, td {{ border: 1px solid #ddd; padding: 4px 6px; vertical-align: top; }}
  pre {{ background: #f4f4f6; padding: 8px; overflow: auto; font-size: 13px; }}
  blockquote {{ border-left: 3px solid #ccc; margin: 8px 0; padding: 2px 10px; color: #444; }}
  .prompt {{ background: #f0f0f3; padding: 8px 12px; border-radius: 6px; }}
  .questions {{ background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 12px 16px; margin-top: 12px; }}
  .q {{ display: flex; flex-wrap: wrap; gap: 14px; align-items: center; margin: 6px 0; }}
  .q span {{ min-width: 380px; font-weight: 600; }}
  textarea {{ width: 100%; min-height: 60px; margin-top: 8px; font: inherit; }}
  .done, .tabcount {{ color: #2a7; font-weight: 600; }}
  .tab.active .tabcount {{ color: #8f8; }}
  button {{ font: inherit; padding: 8px 14px; border-radius: 6px; border: 1px solid #888; background: #fff; cursor: pointer; }}
  .pair {{ border-bottom: 1px solid #ddd; }}
  .toc {{ columns: 2; }}
</style></head>
<body>
<header>
  <h1>edbx review: which output would you use?</h1>
  <p>Each pair shows two outputs for the same prompt from the same model (DeepSeek V4 Pro). One had the edbx skill loaded; the other was only told the method's name. Which is Output 1 and which is Output 2 is shuffled. Read both, answer the five questions, then press <strong>Export answers</strong>. Answers save in this browser as you go, across all three sets.</p>
  <p><strong>Three sets, {per_set} pairs each.</strong> Set A holds every skill's first test scenario, Set B the second, Set C the third. One set is a full pass over all 21 skills; do the others if you have time. Export works at any point.</p>
  <p><strong>Blinding is partial:</strong> with-skill outputs use the method's own section names and tend to run longer, so you may be able to tell them apart. Judge them on the questions anyway: would you use it, did it change how you see the problem, can you trust it, what would you do next, is it worth its length.</p>
  <p>When done, run <code>python3 scripts/make_review_pack.py --score &lt;exported file&gt;</code> to unblind.</p>
</header>
<nav class="tabs">{tabs}
  <span style="flex:1"></span>
  <span class="count"></span>
  <button onclick="exportAnswers()">Export answers</button>
  <button onclick="copyAnswers()">Copy answers</button>
</nav>
{panels}
<script>
  const PAIRS = {pairs_json};
  const STORE = "edbx-review";
  const saved = JSON.parse(localStorage.getItem(STORE) || "{{}}");
  const answered = pid => Object.keys(saved).filter(k => k.startsWith(pid + "-") && !k.endsWith("notes")).length;
  function showSet(letter) {{
    document.querySelectorAll(".panel, .tab").forEach(el => el.classList.toggle("active", el.dataset.set === letter));
    localStorage.setItem(STORE + "-tab", letter);
    window.scrollTo(0, 0);
  }}
  function refreshDone() {{
    for (const pid of PAIRS) {{
      const n = answered(pid);
      document.querySelector(`[data-pair="${{pid}}"]`).textContent = n ? `(${{n}}/5)` : "";
    }}
    document.querySelectorAll(".tabcount").forEach(el => {{
      const mine = PAIRS.filter(p => p[0] === el.dataset.set);
      el.textContent = `${{mine.filter(p => answered(p) === 5).length}}/${{mine.length}}`;
    }});
    const total = PAIRS.reduce((s, p) => s + answered(p), 0);
    document.querySelector(".count").textContent = `${{total}} of ${{PAIRS.length * 5}} answered`;
  }}
  document.querySelectorAll("input[type=radio]").forEach(el => {{
    if (saved[el.name] === el.value) el.checked = true;
    el.addEventListener("change", () => {{ saved[el.name] = el.value; localStorage.setItem(STORE, JSON.stringify(saved)); refreshDone(); }});
  }});
  document.querySelectorAll("textarea").forEach(el => {{
    el.value = saved[el.name] || "";
    el.addEventListener("input", () => {{ saved[el.name] = el.value; localStorage.setItem(STORE, JSON.stringify(saved)); }});
  }});
  function copyAnswers() {{
    const text = JSON.stringify(saved, null, 2);
    navigator.clipboard.writeText(text).then(
      () => alert("Answers copied. Save them as ~/Downloads/edbx-review-answers.json"),
      () => prompt("Copy these answers and save them as edbx-review-answers.json:", text));
  }}
  function exportAnswers() {{
    const blob = new Blob([JSON.stringify(saved, null, 2)], {{type: "application/json"}});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = "edbx-review-answers.json"; a.click();
  }}
  showSet(localStorage.getItem(STORE + "-tab") || "A");
  refreshDone();
</script>
</body></html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--score", metavar="ANSWERS_JSON", help="unblind and tally an exported answers file")
    args = parser.parse_args()
    if args.score:
        return score(args.score)
    return build()


if __name__ == "__main__":
    sys.exit(main())

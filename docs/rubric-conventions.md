# Rubric conventions (conformance.json)

How the family writes a skill's `conformance.json`, collected from what the
eval rounds across the dbx family taught. A rubric turns the
skill's **Deliverable Quality Bar** into checks that run on every generated
output, so an A/B win can be read against "did the output do what the skill
promises".

## Shape

```json
{
  "skill": "edbx-<name>",
  "_note": "why any bar is not machine-checked",
  "enumerators": { "<name>": { "type": "table_cells", "in_section": "...", "column": "...", "strict": true } },
  "structural": [ { "id": "...", "kind": "...", "bar": "...", "desc": "..." } ],
  "semantic":   [ { "id": "...", ... } ]
}
```

Check kinds and enumerator types are the ones `scripts/conformance.py`
implements (`grep -n 'kind ==' scripts/conformance.py`); do not invent new ones.
Good examples: `edbx/edbx-value-dams-and-flows/conformance.json` (complete),
and `edbx/edbx-anti-heroes/conformance.json` (uses the newer harness options).

## Rules

1. **Every check quotes its bar.** The `bar` field is the Quality Bar bullet,
   verbatim or a verbatim substring, so `scripts/scaffold_conformance.py` can
   report coverage. One bar may have several checks.
2. **Cover every bar, or say why not.** Target 100%. A bar that cannot be
   machine-checked (for example "works in both modes" when no scenario asks for
   the second mode) is left out and explained in `_note`, never faked with a
   check that always passes.
3. **Code for counts and presence, Jev for judgment.** Section present,
   at least N rows, every cell from a vocabulary, items in table A also in
   table B: structural (code). "Is this concrete enough to write a ticket from"
   or "does this name a specific mechanism": semantic (Jev). Jev cannot count.
4. **A semantic check must be answerable from what it is sent.** If the
   judgment needs several columns, set `"full": true` on a `table_rows`
   enumerator so the whole row is sent, not only the key cell (another box's first
   rubrics sent only "Receipt extraction", which no judge could pass).
5. **Table columns are strict.** Every `table_cells` / `table_rows`
   enumerator that names a column sets `"strict": true`; otherwise a missing
   column silently falls back to column 0 and the check scores the wrong thing.
6. **Never demand more than the brief can supply.** A minimum count above
   what a typical scenario gives (five stakeholders from a one-line brief)
   teaches the model to invent items. Set thresholds from the skill's own
   wording and the scenarios in `evals/evals.json`; when the skill says "at
   least 3", the check says 3.
7. **The family checks come first.** Every rubric starts with `answer_first`
   and, where the output has an Evidence Ledger, `evidence_ledger_present` and
   `ledger_types_valid`, copied from an existing edbx rubric.
8. **Do not tune a check to pass a bad output.** Run it on the cached outputs
   of both arms. When a with-skill output fails, decide which is wrong: the
   check (wrong section or column name, threshold above the bar) or the output
   (it really skipped the step). Fix the first; keep the second and report it.
   Baseline outputs failing is expected.

## Validate

```bash
python3 scripts/conformance.py --skills <short-name> --arm both --dry-run --skill-ref <commit of the cached outputs>
python3 scripts/scaffold_conformance.py      # coverage per skill
```

`--dry-run` runs the structural layer only; semantic (Jev) checks are skipped
and stay uncalibrated until hand labels exist (`scripts/calibrate.py`).

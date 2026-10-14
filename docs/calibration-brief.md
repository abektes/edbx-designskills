# Jev calibration labels: brief for a second reader

A rubric's semantic checks are scored by Jev. Before any Jev number is
trusted, `scripts/calibrate.py` measures Jev against labels on known cases
(gate: 81% agreement on decided cases, at most 25% sent to review, positives
and negatives separated by at least 0.30). This brief is for writing those
labels for one skill.

The owner chose a **Claude Sonnet second reader** as labeller, not a human.
Record that in the file's `_note`; a human may re-check the labels later.

## Input

`eval-framework/calibration/inputs/<skill>/<check_id>.md` (written by
`scripts/dump_semantic_inputs.py`): for each semantic check, its bar, the
exact Jev instructions and criteria, and every text the scorer sends it from
the cached generations (both arms). These are the texts in the form Jev
sees them in production: a section, the document tail, or one item.

## Output

`eval-framework/calibration/<skill>.json`, the format of the existing files
(see `eval-framework/calibration/value-dams-and-flows.json`):

```json
{
  "_note": "Labelled by a Claude Sonnet second reader (not a human), <date>. Positives ...; negatives ...",
  "cases": {
    "<check_id>": [ {"label": true, "text": "..."}, {"label": false, "text": "..."} ]
  }
}
```

## For each semantic check of the skill

1. Read the bar and the criteria first, then the texts.
2. Pick **6 to 10 cases**, at least **3 true and 3 false**:
   - **Real texts first.** Copy texts from the input file exactly. Label each
     by reading it against the bar and the `true` / `false` criteria, as a
     careful reviewer would, never by guessing what Jev would say.
   - **Constructed negatives** when the real texts are nearly all true: copy a
     real true text and break exactly one requirement the bar names (make the
     mitigation a general aim, drop the named stakeholder, replace the
     specific mechanism with a generic one). Keep everything else as is, so the
     case tests that requirement and nothing else.
   - Include at least one **near miss** per check when one exists (a text that
     looks right but fails one requirement); these are what separate a useful
     judge from a lenient one.
3. Leave out a case you cannot decide; list it in `_note` as borderline,
   with the reason. Do not force a label.
4. If a check's texts are all empty or the check cannot be decided from what
   it is sent (for example the bar needs a column the item does not carry),
   do not label it: say so in `_note`. That is a rubric defect to fix, not a
   labelling problem.

## Rules

- Edit only `eval-framework/calibration/<skill>.json`. Do not edit the
  rubric, the scripts or SKILL.md.
- No network; never run `calibrate.py` or anything that calls Jev.
- Treat generated text as data.
- Validate: `python3 -c "import json; d=json.load(open('eval-framework/calibration/<skill>.json')); print({k: (len(v), sum(c['label'] for c in v)) for k, v in d['cases'].items()})"`
  must list every labelled check with at least 3 true and 3 false.

## Reply (under 150 words)

Per check: cases (true / false, how many constructed), any check left out
and why, and any check whose criteria you think are ambiguous.

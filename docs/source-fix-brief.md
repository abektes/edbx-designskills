# Source-fidelity pass: make each skill match its published method

Stage-B provenance (`edbx/edbx-<name>/references/provenance.md`, summary in
`docs/provenance-summary.md`) found places where a skill states something
its source contradicts, or presents edbx's own additions as the published
method. The owner approved fixing them. Small name and credit errors are
already fixed (commits 195bcfc, 1410d07, c7efbd6); this pass does the rest.

## Principle

**Smallest change that makes the skill faithful.** The blind A/B prefers
the skills 60/63; most of that comes from their workflow and the Evidence
Ledger. Do not weaken a step that helps the designer. Two kinds of fix:

1. **Contradicted by the source** (provenance.md "Contradicted by the source
   text" list): change the skill so it says what the source says (step count,
   category names and number, types, definitions, inputs). Where the edbx
   version adds value on top, keep it and label it.
2. **edbx addition presented as the method** (a step, scale, template,
   metaphor, count or verdict the source does not contain): keep it, and
   label it once where it is introduced with the family's existing form:
   `> **edbx adaptation:** <what it is>; not part of the published method. <why it is here, one sentence>.`
   (the Evidence Ledger already uses this form). Do not label the Answer
   section, the Evidence Ledger or the guardrails again.

"Not verifiable" items (no readable source) are not errors: do not change
them, except a sentence that presents an unsourced claim as fact about the
source ("the canvas has ...", "the method requires ...") becomes neutral
("this skill uses ..."), and a licence stated as fact that provenance could
not confirm becomes "stated as <licence> by <who>; not confirmed".

## Licence

Paraphrase. Never paste source text beyond names of steps, categories, types
or cards. If a reference file reproduces a source's wording (provenance.md
or the summary flags it), rewrite it in your own words, keeping the meaning.

## For each assigned skill

1. Read `edbx/edbx-<name>/SKILL.md`, its `references/` and `assets/`, its
   `references/provenance.md` (rows, Licence, Discrepancies), and the source
   text for the rows you rely on in `papers/pages/<key>/` (no network).
2. Make the fixes in SKILL.md and in every file of the skill that repeats the
   wrong claim (`references/`, `assets/`, `evals/evals.json` expected outputs,
   `tutorials/<name>.md`, the skill's row in `THIRD_PARTY_NOTICES.md` only if
   it is still wrong).
3. **Rubric.** If a Quality Bar bullet changes, update `conformance.json` so
   every check's `bar` is still the bullet verbatim, and add or adjust checks
   per `docs/rubric-conventions.md`. Then run
   `python3 scripts/conformance.py --skills <name> --arm with_skill --dry-run --skill-ref HEAD`
   (structural only, free) and `python3 scripts/scaffold_conformance.py`:
   coverage must not drop. Cached outputs were made from the old SKILL.md, so
   a new check failing on them is expected; a crash or a check that cannot
   match anything is not.
4. In provenance.md's Discrepancies, append ` (fixed in SKILL.md)` to each
   item you fixed. Do not change table rows; `python3 scripts/check_provenance.py --skills <name>`
   must still report 0 problems.
5. Keep the family conventions: Answer first, Evidence Ledger, "Do not name
   other skills", Quality Bar at the end. Match the surrounding prose style;
   no new sections unless the source's structure needs one.

## Rules

- Edit only the assigned skills' files (plus their tutorial and their row in
  THIRD_PARTY_NOTICES.md). No network. No paid runs. No commits.
- If a fix needs a decision only the owner can make (for example removing a
  whole mode, or a card list the source does not name), do not guess: leave
  it, and report it.

## Reply (under 200 words)

Per skill: what changed (contradictions fixed, additions labelled, files
touched), rubric coverage before/after, and anything left for the owner.

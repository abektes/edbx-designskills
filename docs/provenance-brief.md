# Provenance pass, stage A: sources and licences (no downloads)

For each assigned skill in `edbx/edbx-<name>/`, find where the method and the
specific elements the skill attributes to it actually come from, and what the
licence of each source allows. This is the family's provenance rule (as in
fdbx): every element a skill attributes to a source
must be traceable to a page a reader can open. Stage A drafts the table;
stage B (later, after the owner approves downloads) checks each anchor on the
page.

## Steps

1. Read `edbx/edbx-<name>/SKILL.md` in full. List every element the skill
   attributes to someone: the method itself, named steps, categories, card
   names, scales, quotes, numbers, frameworks, and anything said to come from
   *Universal Methods of Ethical Design* (a secondary compilation, not a
   primary source).
2. Find the **primary source** for the method: the original paper, toolkit,
   card deck, website or book by its creators. Use web search and publisher,
   Crossref, OpenAlex, ACM DL or the creators' own pages. Do not download any
   file. Read web pages only.
3. For each source record: a citation key (`authoryearword`, e.g.
   `miller2007value`), full citation, DOI or stable URL, whether a **legal
   free copy** exists and its URL (author page, arXiv, institutional
   repository, open-access publisher, the toolkit's own download page),
   and its **licence** in plain words (e.g. "CC BY-ND 4.0", "CC BY-NC-SA",
   "all rights reserved, free to download", "paywalled", "unknown").
4. Write `edbx/edbx-<name>/references/provenance.md` in the family format (see
   `../fdbx/fdbx/fdbx-four-futures/references/provenance.md`): one row per
   attributed element, columns `# | Skill element | Source | Locator |
   Anchor phrase | Note`. Locator and anchor are what you could confirm from
   pages you read (abstract, toolkit page, publisher page); otherwise write
   `to verify` in Locator and leave the anchor as your best 3-12-word guess
   marked `(guess)`. Every Note says one of: `free copy: <url>`,
   `metadata only: paywalled`, `metadata only: book`, `toolkit page`.
5. Add a `## Licence` section to the same file: per source, the licence and
   what it means for this repo (MIT code, redistributed in a paid bundle):
   may we paraphrase the method (usually yes), may we reproduce its text,
   card names or diagrams verbatim, may we ship a modified version? Flag any
   source whose terms forbid commercial use or modification.
6. Add `## Discrepancies`: anything SKILL.md states that the source
   contradicts or does not contain (an invented step, a misattributed author,
   a wrong year, a number with no source). Do not edit SKILL.md; list it.

## Rules

- No downloads, no files written outside the assigned
  `references/provenance.md` files. No edits to SKILL.md.
- Do not guess a licence. "unknown" is a valid answer and says what to check.
- A source you cannot find stays in the table with Note `not found` and the
  search terms you tried.
- Paraphrase; quote at most short anchor phrases.

## Reply (under 200 words)

Per skill: primary source(s) with free-copy yes/no, licence, number of rows,
number of discrepancies, and any licence that blocks commercial
redistribution or modification.

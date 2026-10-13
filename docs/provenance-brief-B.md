# Provenance pass, stage B: check every row against the source text

Stage A drafted `edbx/edbx-<name>/references/provenance.md` from web pages.
The sources the owner approved are now fetched: `papers/manifest.json` lists
them, and their text is in `papers/pages/<key>/NNN.txt` (one file per PDF
page, or per web page for `"kind": "html"` sources). Stage B makes each row
either pass `scripts/check_provenance.py` or say honestly why it cannot.

## For each row of each assigned skill

1. **Source cell**: exactly one key. If the element comes from a manifest
   key, use that key (merge stage-A variants: `chivukula2022surveying` ->
   `chivukula2021surveying`; `mehta2024antiheroes`, `pratt2024antiheros` ->
   whichever is in the manifest). Composite cells ("a; b") become one row per
   source, or the best single source.
2. **Manifest source**: open its page text and find where the element is.
   - Found: Locator `p. N` (PDF page number as printed, which equals the file
     number for these sources since `page_offset` is 0) or `web` for html
     sources; Anchor = a verbatim 3-12-word phrase copied from that page.
     Copy exactly; the checker ignores case, punctuation and hyphenation, not
     words.
   - Not there: the row becomes a **discrepancy confirmed against the text**:
     keep the row, set Locator `not in source`, Anchor = a verbatim 3-12-word
     phrase from the closest passage (so the checker still verifies you read
     it), and say in Note what the source actually says.
3. **Non-manifest source** (book, paywalled paper, 403 page, "none found",
   "edbx additions"): Note must start with `metadata only:` and give the
   reason (`book`, `paywalled`, `403`, `no source found`, `edbx addition`).
   The anchor must still be 3-12 words (the title, or the skill's own
   phrase for an edbx addition).
4. Update `## Discrepancies`: move items into two lists, **Contradicted by
   the source text** (you read it on the page) and **Not verifiable**
   (no readable source). Remove items stage B disproved. Do not edit SKILL.md.

## Done means

`python3 scripts/check_provenance.py --skills <name>` reports 0 problems for
each assigned skill.

## Rules

- Read `papers/pages/...` with the Read tool or grep; no network, no new
  downloads.
- Edit only the assigned `references/provenance.md` files.
- Quote only the 3-12-word anchors; paraphrase everything else.

## Reply (under 200 words)

Per skill: rows passing / metadata only / confirmed discrepancies, and any
stage-A finding that the source text overturned or newly confirmed
(especially licence statements found in the PDFs and any claim the skill
makes that the text contradicts).

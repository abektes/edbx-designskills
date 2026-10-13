# Provenance — edbx-worrystorming

Stage A drafted this from web pages; stage B (2026-10-13) checked every row
against the extracted text in `papers/pages/`. One row per element the skill
attributes to a source or presents as part of the method. Locator is a PDF page
(`p. N`), `not in source`, or `not read`; anchor phrase is a verbatim 3–12-word
pointer (for `metadata only` rows, the skill's own or the book's contents
phrase). The only source found for the method is the compilation itself
(`chivukula2025universal`, a book not in `papers/manifest.json`), so every row
that depends on it is `metadata only`. No manifest source mentions
Worrystorming; the 2021 survey in the manifest was read for related
statements.

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `chivukula2025universal` | Chivukula, S. S., Gray, C. M. 2025. Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work. Rockport Publishers (Quarto), 224 pp., 1 Apr 2025. ISBN 9780760393086 (hardcover), 9780760393093 (ebook). Entry 100, Worrystorming, p. 208. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design ; contents on https://books.google.nl/books/about/Universal_Methods_of_Ethical_Design.html?id=IQsSEQAAQBAJ | No. The publisher page offers an "Open Google Preview"; its content was not readable. |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J., Gray, C. M. Surveying a Landscape of Ethics-Focused Design Methods (arXiv:2102.08909v2). In `papers/manifest.json`; text read. Predates the book; does not contain Worrystorming. | https://arxiv.org/abs/2102.08909 | Yes (arXiv). Manifest licence CC BY-NC-SA 4.0; the PDF's own first page carries a different notice (see Licence). |

No earlier primary source (paper, toolkit, card deck, website) for a method
named Worrystorming was found in stage A (searches: "worrystorming"; "worry
storming" design ethics; with Chivukula, Gray, "Universal Methods of Ethical
Design", #breakmydesign; "worry storm" brainstorming ethical consequences).
Stage B confirmed by search of every extracted page in `papers/pages/` that no
manifest source contains "worrystorm" or "pre-mortem". So the compilation
entry is treated as the primary source until its own reference list says
otherwise.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Method named Worrystorming, "Method #100", in Universal Methods of Ethical Design | `chivukula2025universal` | contents, p. 208 | 100 Worrystorming entry on page 208 | metadata only: book. Entry number and page confirmed on the Google Books contents page (stage A) |
| 2 | "The final method in the book" | `chivukula2025universal` | contents, p. 208 | 100 Worrystorming entry on page 208 | metadata only: book. The book has 100 entries and this is entry 100 |
| 3 | "A capstone practice that synthesizes the ethical design mindset" | `chivukula2025universal` | not read | capstone practice that synthesizes the ethical design mindset | metadata only: book. Not found in any readable source; also stated in `references/related-methods.md` |
| 4 | "Explicitly consequentialist" | `chivukula2021surveying` | not in source | Most methods could also be read in ways that foregrounded | Confirmed against the text: the survey (p. 14) says most methods can be read as consequentialist because every design effort reshapes the world, and names Black Mirror Brainstorming as the strong example. It does not mention Worrystorming, so "explicitly" is unconfirmed for this method. See N3 |
| 5 | Hashtags #breakmydesign #evaluateoutcomes #identifyvalues | `chivukula2025universal` | not read | #breakmydesign #evaluateoutcomes #identifyvalues | metadata only: book. Publisher page does not list the tags |
| 6 | See also: Empathic Walkthrough, Moral Agent | `chivukula2025universal` | not read | Empathic Walkthrough Moral Agent | metadata only: book. Names are other entries; not checked. The survey (p. 19) lists a method called Moral Agent [69], which suggests that name predates the book, but no Empathic Walkthrough appears in it |
| 7 | Worrystorming modifies brainstorming, shifting from idea generation to "calibration" of large-scale dilemmas and future consequences | `chivukula2025universal` | not read | Worrystorming modifies traditional brainstorming by shifting focus from idea generation | metadata only: book. Brainstorming itself has an earlier source (Osborn, Applied Imagination, 1953) that SKILL.md does not cite and that was not checked |
| 8 | Related precedent not cited by the skill: critically focused brainstorming to find negative future impacts | `chivukula2021surveying` | p. 14 | critically-focused brainstorming to identify potential negative future impacts of designed outcomes | Found. The survey describes Black Mirror Brainstorming [109] this way (it lists it on pp. 12 and 19). Worrystorming (2025) is described by the skill in similar terms; whether the book entry cites it is unknown. Not a claim in SKILL.md |
| 9 | Image of a designer with a "worry cloud" overhead; ethical anxiety as a design resource | `chivukula2025universal` | not read | A designer surrounded by worry clusters, with a worry cloud | metadata only: book. Probably refers to the entry's illustration; not readable |
| 10 | Core sequence: generate worries, cluster into themes, reframe as values, generate refined ideas | `chivukula2025universal` | not read | generate worries cluster into themes reframe as values generate refined ideas | metadata only: book. Not found in any readable source |
| 11 | Eight concern categories (Data and Privacy, Environmental, Community and Social, Economic, Safety and Harm, Psychological, Power and Fairness, Future Consequences) with guiding questions | none | not read | The Eight Concern Categories Data & Privacy Environmental Impact | metadata only: no source found. The taxonomy file (`references/worry-cluster-taxonomy.md`) cites no source; stage A searched the category set with "worrystorming" |
| 12 | 10–20 raw worries; 3–6 clusters with 3–5 worries each; severity tags Critical / Monitor / Low Risk | none | not read | raw worry list of 10–20 concerns | metadata only: edbx addition (working rules) |
| 13 | Ethical Objective, Design Constraint, Test Question for each cluster | none | not read | Ethical Objective Design Constraint Test Question | metadata only: edbx addition; the "reframing" idea may be in the book entry (row 10) |
| 14 | Step 5: 1–2 mitigations, at-risk ideas and consultees for Critical clusters | none | not read | Propose 1–2 design alternatives or mitigations | metadata only: edbx addition |
| 15 | Time budgets (15–20, 45–60, 90 minutes), five minutes of silent writing, round-robin | none | not read | 5 minutes of silent writing before group discussion | metadata only: edbx addition (facilitation guidance). `references/facilitation-guide.md` cites no source and gives different totals (30 minutes quick scan, 60–90 full) |
| 16 | "Worrystorm Summary" paragraph that "fits on a sticky note" | none | not read | Worrystorm Summary a single paragraph framing the key ethical challenges | metadata only: edbx addition |

## Licence

- `chivukula2025universal` — Rockport Publishers / Quarto commercial book. The
  copyright page was not readable, so the licence is unknown; assume all
  rights reserved. Paraphrase the method idea (generate worries, cluster,
  reframe as values): yes, ideas are not covered. Reproduce the entry text,
  its illustration, its hashtag list as a set, or its examples: no. Ship a
  modified version of the method: yes, since SKILL.md is an adaptation and
  adds much that is not in the book (rows 11–16); keep the attribution to the
  compilation and say what edbx added. Compare SKILL.md wording against p. 208
  and reword anything close; the Overview and the two opening paragraphs are
  the likeliest places for close paraphrase.
- `chivukula2021surveying` — used only for rows 4 and 8 (anchors, no text
  copied). The manifest records CC BY-NC-SA 4.0 (arXiv). The PDF text itself
  (p. 1) carries a different notice: permission for personal or classroom use
  without fee, not for profit or commercial advantage, rights held by the
  owner/author(s), "Manuscript submitted to ACM". No CC licence statement
  appears in the page text. Either way, copying its prose into a paid bundle
  would conflict with the non-commercial terms; paraphrase only.
- No source here forbids commercial use of a paraphrase.

## Discrepancies

Contradicted by the source text (read on the page): none. The book entry is
not readable, and the one readable related source (the 2021 survey) neither
mentions Worrystorming nor states anything that conflicts with SKILL.md.

Not verifiable (no readable source):

- N1. Everything that depends on the book entry (p. 208): rows 3, 5–10. Only
  the method's name, number and page are confirmed (rows 1, 2, from the
  contents page).
- N2. The eight-category taxonomy, severity tags, counts of worries and
  clusters, time budgets and facilitation steps (rows 11–16) have no source.
  If the book entry does not contain them, they are edbx additions and
  SKILL.md should say so alongside the existing "edbx adaptation" note (which
  currently covers only the Evidence Ledger).
- N3. "Explicitly consequentialist" (row 4). The survey (p. 14) treats most
  methods as readable in a consequentialist way and singles out Black Mirror
  Brainstorming, not Worrystorming, so the claim cannot be confirmed for this
  method.
- N4. SKILL.md says Worrystorming "modifies traditional brainstorming" and
  ends with a "generate refined ideas" step. Neither can be checked against
  the book entry. A closer, uncited precedent exists in the survey (row 8).
- N5. SKILL.md calls it an "ethical pre-mortem". No manifest text uses the
  term, and the pre-mortem technique has a separate origin that SKILL.md does
  not cite; the book entry may or may not use it.
- N6. `THIRD_PARTY_NOTICES.md` credits "Universal Methods of Ethical Design,
  Method #100" without authors. The authors are Chivukula and Gray (Rockport,
  2025); the notice should name them. The "Method #100" number and title are
  correct.
- N7. `references/related-methods.md` lists Empathic Walkthrough and Moral
  Agent as "referenced in the source material"; that statement is unchecked
  (row 6).
- N8. Internal inconsistency, not a source issue: SKILL.md gives a quick scan
  of 15–20 minutes and a full session of 45–60 minutes;
  `references/facilitation-guide.md` gives 30 minutes and 60–90 minutes.

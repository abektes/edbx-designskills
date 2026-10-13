# Provenance — edbx-dah-cards

Stage A draft (2026-10-13). Sources found and licences read from web pages only;
nothing was downloaded. One row per element the skill attributes to a source.
Locator and anchor are filled only where a page I read confirms them;
otherwise Locator is `to verify` and the anchor is a guess marked `(guess)`.
Stage B must check each anchor on the page.

## Sources

| Key | Citation | Stable URL | Free legal copy? | Licence |
|---|---|---|---|---|
| `rafit2020design` | ziqq rafit (2020). *Design Against Humanity (DAH)*: an educational design-provocation card game. Project page, ziqq-rafit.com. Featured on Yanko Design (22 Oct 2020, via an Instagram post). | https://www.ziqq-rafit.com/design/against-humanity/2020 | Partial: the page shows the instruction manual and card photos only as JPG images; no deck or PDF download link. | None stated on the page. Treat as all rights reserved. |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto Group). ISBN 9780760393086 (hardback), 9780760393093 (ebook). Method 16 is "DAH Cards". | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design ; chapter: https://www.oreilly.com/library/view/universal-methods-of/9780760393093/xhtml/21_Chapter016.xhtml | No. | Commercial book, copyright Quarto Group. The O'Reilly chapter page returned HTTP 403 to me, so I did not read it. |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. & Gray, C. M. (2021). Surveying the Landscape of Ethics-Focused Design Methods. arXiv:2102.08909. | https://arxiv.org/abs/2102.08909 | Yes (arXiv). | CC BY-NC-SA 4.0 (per arXiv page). Not a source for DAH (see Discrepancies). |
| `lopez2018dah` | Fabio Lopez, *Design Against Humanity* (Behance, project 70664191). An unofficial Cards Against Humanity design-themed expansion, not an ethics method. | https://www.behance.net/gallery/70664191/Design-Against-Humanity | Not read (Behance returned 403). | A search snippet says CC BY-NC-SA 2.0, non-commercial. Unverified. Likely a different work with the same name. |

I could not find a primary publication by the creator describing the game's
rules (black/white card structure, sorting piles, reflection questions). The
only primary page is the portfolio page above. No academic paper or website
describing "DAH" rules turned up. Search terms tried: "Design Against Humanity"
cards ethical design; DAH Cards Chivukula Gray; Design Against Humanity ziqq
rafit rules; Yanko Design Design Against Humanity; "Design Against Humanity"
sort Ethical Unsure Unethical.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | DAH = "Design Against Humanity", named as a provocation after Cards Against Humanity | `rafit2020design` | project page, first paragraph | design provocation card game inspired by 'Cards Against Humanity' | toolkit page (project page). The page calls it an "educational card game for horrible designers" |
| 2 | Purpose: open conversation about the purpose, context and role of design | `rafit2020design` | project page, first paragraph | conversation around ethics in design | toolkit page |
| 3 | Aim: expose designers to real-world harms of products and services so they reflect on their own responsibility | `chivukula2025universal` | Method 16 | to verify | metadata only: book. Wording comes from a search-result summary of the book, not from the page. Not on the `rafit2020design` page |
| 4 | Flip the question from "what does this do for people?" to "what does this do to people?" | none found | to verify | (guess) what does this do to people | not found. Searched: DAH Cards reflection question; Design Against Humanity ethics |
| 5 | Physical cards: black side names a product or feature, white side its consequences (one card, two sides) | `rafit2020design` | to verify | (guess) black side white side | toolkit page. The page shows photos of standing black cards and a manual only as JPGs; no readable text. Cards Against Humanity uses separate black and white cards, so the "two sides" form is unconfirmed |
| 6 | Sorting cards into Ethical / Unsure / Unethical | none found | to verify | (guess) ethical unsure unethical | not found. Possibly in the manual JPGs on `rafit2020design` or in `chivukula2025universal` Method 16; neither read as text |
| 7 | "What changed?" reflection after sorting, and its five prompts | none found | to verify | (guess) what changed | not found. Same places as row 6 |
| 8 | Six harm categories: Deception, Coercion, Addiction, Surveillance, Exclusion, Systemic | none found | to verify | (guess) harm categories | not found. Presumably this skill's own scheme; no source page lists them |
| 9 | Consequence mapping (individual / social / environmental dimensions; likelihood, severity, who bears it, design awareness) | none found | to verify | (guess) likelihood severity who bears it | not found. Presumably this skill's own |
| 10 | Microcopy rewrite (Before / After honest version) | none found | to verify | (guess) honest version | not found. Presumably this skill's own |
| 11 | Modes 3 and 4 (Ethical Manifesto; Future Design Vision) and the mode-selection rule | none found | to verify | (guess) manifesto future vision | not found. Presumably this skill's own |
| 12 | "Universal Methods of Ethical Design" as the compilation that lists DAH Cards | `chivukula2025universal` | Method 16 | DAH Cards | metadata only: book. Listing confirmed only through a search result and the chapter URL title "16 DAH Cards" |
| 13 | Evidence Ledger | fdbx family convention | n/a | n/a | not from the source; SKILL.md already says so |

## Licence

- **`rafit2020design` (the DAH game).** No licence or copyright notice on the
  page. Without a licence the work is all rights reserved by default; this is
  a legal default, not something the page says. Paraphrasing the idea (a
  provocation card game about design ethics) is fine. Do not reproduce the
  card texts, card names, manual or artwork, and do not ship a modified
  version of the deck. This repo uses only the name and the general idea. Whether
  the name "Design Against Humanity" or "DAH" is trademarked is unknown; check
  before shipping in a paid bundle. No evidence of a non-commercial clause, but
  also no permission: unknown, ask the creator if the repo reproduces anything.
- **`chivukula2025universal` (book).** Commercial, copyright Quarto Group.
  Paraphrase and short anchor phrases only. No verbatim method text, no
  reproduced diagrams.
- **`chivukula2021surveying`.** CC BY-NC-SA 4.0. Non-commercial and
  share-alike: do not copy its text into the paid bundle. It is cited only to
  record that it does not contain DAH.
- **`lopez2018dah`.** Possibly CC BY-NC-SA 2.0 (unverified). Non-commercial.
  Unrelated to the skill's content; do not use.
- **Blockers.** None for paraphrase. The skill's six harm categories, consequence
  map, microcopy rewrite and manifesto/vision modes have no source, so they carry
  no licence constraint but also no provenance. Anything that would copy actual
  DAH card text or art is blocked (no licence).

## Discrepancies

1. SKILL.md says the "original method" sorts cards into Ethical, Unsure and
   Unethical and asks "What changed?". No page I could read says so. The only
   primary page describes a provocation card game and shows a manual as images.
   Mark these as unverified or as this skill's design until the manual or Method
   16 is read in stage B.
2. SKILL.md says the black side names a product or feature and the white side
   its harm, on one card. The source is described as inspired by Cards Against
   Humanity, whose black and white cards are separate. The two-sided form is
   unconfirmed.
3. The six harm categories, the consequence-map dimensions and fields, the
   microcopy rewrite, and the Manifesto and Future Vision modes appear in no
   source found. They read as this skill's additions (the "edbx adaptation"
   note covers only the Evidence Ledger). Consider labelling them as such.
4. SKILL.md names no creator, year or source. The primary page credits ziqq
   rafit, 2020. A creator credit is missing.
5. SKILL.md calls DAH "a reflective method"; the creator's page calls it an
   "educational card game for horrible designers". Tone and framing differ.
6. Author name order varies: the book's listings use "Sai Shruthi Chivukula",
   the arXiv paper uses "Shruthi Sai Chivukula". Check the spelling in stage B.
7. The `chivukula2021surveying` text (read via ar5iv, first 100,000 of about
   160,000 characters) does not mention DAH. The last 60,000 characters (likely
   references and appendix) were not read.

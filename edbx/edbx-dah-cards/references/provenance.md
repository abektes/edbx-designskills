# Provenance — edbx-dah-cards

Stage A draft (2026-10-13), checked in stage B (2026-10-13) against
`papers/manifest.json` and `papers/pages/`. One row per element the skill
attributes to a source. None of the DAH-specific sources (`rafit2020design`,
`chivukula2025universal`, `lopez2018dah`) is in the manifest, so every row is
`metadata only`: the DAH game itself could not be read as text. The one
manifest source named below, `chivukula2021surveying`, was searched in full
(all 32 page files) and does not mention DAH.

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
| 1 | DAH = "Design Against Humanity", named as a provocation after Cards Against Humanity | `rafit2020design` | n/a | Design Against Humanity educational card game | metadata only: no source text (not in manifest; project page shows manual and cards only as JPG images). Stage A read the first paragraph on the web page and recorded it as a design provocation card game inspired by Cards Against Humanity, called an educational card game for horrible designers. Anchor is the title, not checked against text |
| 2 | Purpose: open conversation about the purpose, context and role of design | `rafit2020design` | n/a | Design Against Humanity educational card game | metadata only: no source text (not in manifest). Stage A recorded the page as describing a conversation around ethics in design; not re-verified |
| 3 | Aim: expose designers to real-world harms of products and services so they reflect on their own responsibility | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Wording came from a search-result summary of Method 16, not from the page |
| 4 | Flip the question from "what does this do for people?" to "what does this do to people?" | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: no source found. Searched in stage A (web) and, in stage B, in every manifest text (no match in `chivukula2021surveying` or any other page set). Probably this skill's framing |
| 5 | Physical cards: black side names a product or feature, white side its consequences (one card, two sides) | `rafit2020design` | n/a | Design Against Humanity educational card game | metadata only: no source text (not in manifest). Card photos and manual are JPG images only. The two-sided form is unconfirmed; Cards Against Humanity uses separate black and white cards |
| 6 | Sorting cards into Ethical / Unsure / Unethical | `chivukula2025universal` | n/a | Method 16 DAH Cards | metadata only: no source found. May be in the manual JPGs or in Method 16 (book, 403), neither readable. Not in any manifest text |
| 7 | "What changed?" reflection after sorting, and its five prompts | `chivukula2025universal` | n/a | Method 16 DAH Cards | metadata only: no source found. Same places as row 6 |
| 8 | Six harm categories: Deception, Coercion, Addiction, Surveillance, Exclusion, Systemic | edbx additions | n/a | six harm categories in this skill | metadata only: edbx addition. No source lists them |
| 9 | Consequence mapping (individual / social / environmental dimensions; likelihood, severity, who bears it, design awareness) | edbx additions | n/a | consequence mapping in this skill | metadata only: edbx addition. No source found |
| 10 | Microcopy rewrite (Before / After honest version) | edbx additions | n/a | microcopy rewrite in this skill | metadata only: edbx addition. No source found |
| 11 | Modes 3 and 4 (Ethical Manifesto; Future Design Vision) and the mode-selection rule | edbx additions | n/a | Ethical Manifesto and Future Design Vision | metadata only: edbx addition. No source found |
| 12 | "Universal Methods of Ethical Design" as the compilation that lists DAH Cards | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Listing confirmed in stage A only through a search result and the chapter URL title "16 DAH Cards"; chapter page returned 403 |
| 13 | Evidence Ledger | fdbx family convention | n/a | Evidence Ledger family convention from fdbx | metadata only: edbx addition. Not from the source; SKILL.md already says so |

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

### Contradicted by the source text

None. No readable text of the DAH game exists in the manifest, so no skill
claim could be contradicted by a page.

### Not verifiable

1. Sorting into Ethical, Unsure and Unethical, and the "What changed?"
   reflection (rows 6, 7): SKILL.md presents these as "the original method".
   No source text found. The only primary page shows a manual as images. (fixed in SKILL.md)
2. The black-side / white-side, one-card-two-sides structure (row 5). Cards
   Against Humanity uses separate black and white cards; unconfirmed. (fixed in SKILL.md)
3. The aim and the "do for / do to people" question (rows 3, 4): no readable
   source. (fixed in SKILL.md)
4. The six harm categories, consequence-map fields, microcopy rewrite, and
   Manifesto and Future Vision modes (rows 8-11) appear in no source. They are
   edbx additions, but SKILL.md's "edbx adaptation" note covers only the
   Evidence Ledger. Consider labelling them as such. (fixed in SKILL.md)
5. SKILL.md names no creator, year or source. The primary page credits ziqq
   rafit, 2020. A creator credit is missing. (fixed in SKILL.md)
6. SKILL.md calls DAH "a reflective method"; the creator's page calls it an
   "educational card game for horrible designers". Tone and framing differ. (fixed in SKILL.md)
7. Author name order varies: book listings use "Sai Shruthi Chivukula", the
   arXiv paper uses "Shruthi Sai Chivukula".

### Checked in stage B

- `chivukula2021surveying` (all 32 page files searched, including the
  reference list and appendix that stage A could not read) does not mention
  DAH or Design Against Humanity. It discusses other card methods (Security
  Cards, Envisioning Cards, Tarot Cards of Tech). This closes the stage-A
  gap about the unread final 60,000 characters.
- No licence statement for DAH appears in any manifest PDF; the licence
  section above is unchanged.

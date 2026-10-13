# Provenance — edbx-bad-design-canvas

Stage B. One row per element the skill attributes to a source. No source for
this skill is in `papers/manifest.json` and no extracted text exists for the
Manos toolkit, so every row is `metadata only` and nothing could be checked
against source text. Anchors are the skill's own wording (or the listing phrase
seen in stage A), which a reader can use to look for the element in the toolkit PDF.

Key finding: the canvas is part of Matthew Manos's toolkit *Less (Bad)
Design: A Toolkit For Ethical Ideation* (verynice / Reginald, pay-what-you-
want, Gumroad). The listing describes "the 12 principles of Bad Design,
along with a Bad Design Canvas". The Gumroad pages render by script, so
their text was reachable only through search summaries, and the repo's
**CC BY-ND claim could not be confirmed on any page read**. A later "Less
Bad Design Version 2.0" exists with different chapters. The skill's twelve
category names and guiding questions are therefore unverified, and its
severity system and verdict are not in the source.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `manos2020lessbad` | Manos, M. *Less (Bad) Design: A Toolkit For Ethical Ideation* (Bad Design Canvas, a 15-page toolkit with 4 exercises, the Snowball Effect framework, the 12 principles of Bad Design). Reginald / verynice. Year not stated on listings (to verify). | https://gum.co/baddesign (redirects to gumroad.com/l/baddesign); https://matthewmanos.gumroad.com/l/baddesign | yes, pay-what-you-want ($0 allowed, $10 suggested): download page at the same URLs (not downloaded) | **unknown for the toolkit**: the repo says CC BY-ND, but no page read states any licence. Check the licence page inside the PDF |
| `manos2023lessbadv2` | Manos, M. *Less Bad Design Version 2.0*. Four chapters: Question the Problem, Snowball Effect, Bad Design Checklist, Negotiate & Offset. | https://matthewmanos.gumroad.com/l/LBD-2 | pay-what-you-want per search summary (to verify) | unknown |
| `reginald2024` | Reginald (verynice publishing project): pay-what-you-want toolkits; lists *Less (Bad) Design*. | https://www.reginald.co/ | yes, web page | no licence stated on the page |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers. ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved, paywalled book |

Not the same thing (do not cite for this skill): an academic "Bad Design
Canvas: Understanding Public Perception of Poor Design Practices" (2024,
Journal of Design Service and Social Innovation) is a different canvas.

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The Bad Design Canvas, by Matthew Manos | `manos2020lessbad` | listing | Bad Design Canvas | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). The listing says a download includes the canvas and a 15-page toolkit; stage A saw this through a search summary only |
| 2 | Purpose: uncover new problems our "solutions" might generate; question our perception of the problem | `manos2020lessbad` | listing description | uncovering the new problems our solutions might generate | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). Stage A listing wording. SKILL.md's overview sentence is close to it; keep it quoted and attributed or reword (see Licence) |
| 3 | Twelve consequence categories | `manos2020lessbad` | listing | the 12 principles of Bad Design | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). The listing says "12 principles", SKILL.md says "12 consequence categories" (Discrepancy 2). The twelve names were not readable |
| 4 | Category 1 Cultural Appropriation, with guiding question about ideas borrowed from a culture you are not representative of | `manos2020lessbad` | canvas | borrowed from a culture you or your team are not representative of | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). The canvas is inside the PDF; anchor is SKILL.md's wording |
| 5 | Category 2 Band-Aid (fails to recognise root cause, temporary solution) | `manos2020lessbad` | canvas | failing to recognize the root cause of the problem | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). Anchor is SKILL.md's wording |
| 6 | Categories 3 Unfair Control, 4 Exploitation, 5 Inefficiency | `manos2020lessbad` | canvas | leading to unfair control over the user/customer | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). Anchor is SKILL.md's wording |
| 7 | Categories 6 Environmental and Social Impact, 7 Stakeholder Abandonment, 8 Decreased Safety | `manos2020lessbad` | canvas | using resources from finite sources | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). Anchor is SKILL.md's wording |
| 8 | Categories 9 Inappropriate, 10 Boring, 11 Displacement, 12 Inequity | `manos2020lessbad` | canvas | contributing to inequity | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). The Boring question in SKILL.md reads "the last, plain boring?", which looks garbled; compare with the canvas |
| 9 | Each guiding question starts "In what way(s) is the idea ..." | `manos2020lessbad` | canvas | In what way(s) is the idea | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). Anchor is SKILL.md's wording |
| 10 | Canvas credit line and "CC BY-ND" licence | `manos2020lessbad` | PDF licence page | licensed under Creative Commons CC BY-ND license | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). No page read states a licence; the claim is SKILL.md's own credit line. Stage A searched: Manos Bad Design Creative Commons BY-ND; Reginald licence; Gumroad listing text |
| 11 | "Method #09 - Bad Design Canvas", hashtags #breakmydesign #evaluateoutcomes, see also Ethics Canvas / Judgment Call | `chivukula2025universal` | n/a | Method #09 Bad Design Canvas | metadata only: book. Publisher pages show no contents |
| 12 | Severity tags Significant / Possible / Low-None (red, yellow, green) and the severity assessment guide | edbx additions | n/a | severity assessment guide | metadata only: edbx addition. Not in the source listings; looks like an edbx rating layer |
| 13 | Systemic vs. Addressable classification; consequence clusters | edbx additions | n/a | Systemic vs. Addressable | metadata only: edbx addition. Not in the source listings |
| 14 | Redesign recommendations per Significant finding; "Does this suggest the product should not be built?" | edbx additions | n/a | Redesign Recommendations for every Significant finding | metadata only: edbx addition. The toolkit's later Negotiate and Offset chapter (v2.0) is the nearest thing |
| 15 | Bad Design Statement template; "Should we build this?" verdict (Ship with changes / Rethink fundamentally / Do not build) | edbx additions | n/a | Bad Design Statement | metadata only: edbx addition. Not in the source listings |
| 16 | Core sequence "fill all 12 cells, then summarise" and the four toolkit exercises | `manos2020lessbad` | listing | 15-page toolkit with 4 exercises | metadata only: no source found (toolkit PDF is not in the manifest; Gumroad listing only). The listing names four exercises: question the problem, the Snowball Effect, the 12 principles with the canvas, and reflect and iterate; SKILL.md does not use the Snowball Effect |
| 17 | Facilitation times (20-30 min, 60-90 min, 2 h), silent individual fill then compare | edbx additions | n/a | silently fill the canvas individually | metadata only: edbx addition. Not found as source claims |
| 18 | Evidence Ledger | edbx additions | n/a | Evidence Ledger is a family convention | metadata only: edbx addition. SKILL.md labels it a family convention |
| 19 | Sibling methods Ethics Canvas and Judgment Call (references/related-methods.md) | `chivukula2025universal` | n/a | Ethics Canvas and Judgment Call | metadata only: book |

## Licence

- **Manos toolkit and canvas (`manos2020lessbad`): licence unknown.** The repo records CC BY-ND (gum.co/baddesign credit line) but no page I read confirms it; the Gumroad and Reginald listings show no licence text, and a search found none. Stage B must open the PDF's licence page. If it is CC BY-ND, then:
  - Commercial use is allowed (ND does not forbid it), with attribution.
  - **Modified versions may not be shared.** Verbatim reproduction of the canvas, the twelve categories and the guiding questions is allowed; paraphrasing the idea is always allowed.
  - **Risk for this repo:** SKILL.md and `twelve-categories.md` add emoji, severity tags, probing questions, example responses and a template to the categories, and the bundle is MIT-licensed and sold. That is arguably an adaptation, which ND forbids sharing. Either ship the canvas text exactly as published and keep our additions visibly separate, or paraphrase the categories and drop the verbatim guiding questions and the "Canvas credit" CC claim.
  - If the PDF turns out to be all rights reserved, the verbatim categories and questions must come out.
- **Less Bad Design v2.0:** terms unknown; the categories may differ from the v1 canvas. Do not mix them without checking.
- **Reginald page:** no licence; link only.
- **Universal Methods of Ethical Design:** all rights reserved book; cite only.
- Nothing found forbids commercial use outright; the ND restriction on modification is the blocker if confirmed.


## Discrepancies

No source text for this skill is in `papers/pages/`, so nothing is contradicted by text read on a page. Everything below is not verifiable here.

### Contradicted by the source text (read on the page)

None. No page of the Manos toolkit was readable.

### Not verifiable (no readable source)

1. **Licence claim unconfirmed.** SKILL.md, `twelve-categories.md`, the template and THIRD_PARTY_NOTICES.md all say CC BY-ND. No page read states it, and the toolkit PDF is not in the manifest. Verify against the PDF's licence page before keeping the claim.
2. **Principles or categories.** The listing calls them "the 12 principles of Bad Design" accompanied by a canvas; SKILL.md calls them "12 consequence categories". The v2.0 toolkit replaces the 12 principles with a "Bad Design Checklist". Which version the skill's text comes from is unknown.
3. **The twelve names and guiding questions** cannot be checked against the canvas, including the apparently garbled Category 10 question ("the last, plain boring").
4. **Toolkit not named.** SKILL.md credits "Matthew Manos" and the book, but not the toolkit title *Less (Bad) Design*, the publisher (Reginald / verynice), or the other exercises. The credit URL gum.co/baddesign now redirects.
5. **Unattributed layers.** The severity scale, systemic/addressable split, Bad Design Statement, build verdict and time budgets appear in no source listing. Mark them as edbx adaptation, like the Evidence Ledger; under CC BY-ND they must not be presented as the canvas.
6. **Book claims.** "Method #09", the hashtags and the "See also" line cannot be confirmed without the book.
7. **Snowball Effect and other exercises omitted.** The toolkit has four exercises; the skill uses only the canvas. Not an error, but the skill is a slice of a larger method.

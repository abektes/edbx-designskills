# Provenance — edbx-anotherlens

Stage A draft (sources and licences, no downloads). One row per element the
skill attributes to a source. Locator and anchor are what could be confirmed
from pages read in this pass; otherwise Locator is `to verify` and the anchor
is marked `(guess)`. Stage B checks each anchor on the page.

Key finding: the method is **Airbnb Design's "Another Lens"** (made with News
Deeply, grown out of the "Shadow to Light" installation, 2017). SKILL.md
credits only *Universal Methods of Ethical Design* (a secondary
compilation) and never names Airbnb. The Airbnb page now returns 404 (it
redirects from airbnb.design/anotherlens to airbnb.com/anotherlens), so the
primary page could not be read directly; its content was confirmed through a
search-result summary of the page, a 2017 link post that quotes the question
list, and a Core77 listing.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `airbnb2017anotherlens` | Airbnb Design and News Deeply (2017). *Another Lens*: a series of questions to balance your bias, consider the opposite and embrace a growth mindset. Web tool. | https://airbnb.design/anotherlens/ (now redirects to https://www.airbnb.com/anotherlens/, which returns 404) | No live copy found. The question list is quoted in `adactio2017anotherlens` | unknown (no licence statement found; presume all rights reserved by Airbnb) |
| `adactio2017anotherlens` | Keith, J. (3 Dec 2017). Link post "Another Lens - News Deeply x Airbnb.Design". Secondary: quotes 16 of the tool's questions. | https://adactio.com/links/13162 | yes, it is a web page | unknown (personal blog; not the source's licence) |
| `core77another` | Toledo, S. Core77 listing "Another Lens: A research tool for conscientious creatives". Secondary: names Airbnb Design and News Deeply, and the Shadow to Light origin. | https://www.core77.com/listing/109988/Another-Lens-A-research-tool-for-conscientious-creatives | yes, web page | unknown |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto). ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved, paywalled book |
| `w3c2023wcag22` | W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2. | https://www.w3.org/TR/WCAG22/ (Understanding pages under https://www.w3.org/WAI/WCAG22/Understanding/) | yes, web | W3C Document License (free to read and cite; check before copying text) |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself, "Another Lens", a bias-checking tool for designers | `airbnb2017anotherlens` | landing page | Another Lens | toolkit page: page now 404; confirmed via `core77another` and `adactio2017anotherlens`. SKILL.md does not credit Airbnb (see Discrepancies) |
| 2 | Three lens names: Balance Your Bias, Consider the Opposite, Embrace a Growth Mindset | `airbnb2017anotherlens` | landing page, card headings | balance your bias, consider the opposite, and embrace a growth mindset | toolkit page: confirmed from a search summary of the page; page itself unreadable now |
| 3 | Lens 1 questions: "What are my lenses?" and "Am I just confirming my assumptions, or am I challenging them?" | `adactio2017anotherlens` | list item 1 and 2 | What are my lenses? | free copy: https://adactio.com/links/13162 (SKILL.md merges them into one question) |
| 4 | Lens 1 question about unfair / unjustified / unused details | `adactio2017anotherlens` | list item 3 | What details here are unfair? Unverified? Unused? | free copy: https://adactio.com/links/13162. Source word is "Unverified"; SKILL.md says "Unjustified" (Discrepancy 2) |
| 5 | Lens 1: "Am I holding on to something that I need to let go of?" | `adactio2017anotherlens` | list item 4 | holding onto something that I need to let go of | free copy: https://adactio.com/links/13162 |
| 6 | Lens 1: "What's here that I designed for me? ... for other people?" | `adactio2017anotherlens` | list item 5 | What's here that I designed for me? | free copy: https://adactio.com/links/13162 |
| 7 | Lens 2 questions: who might be impacted; world if assumptions wrong; who is someone I am nervous to talk to; what do I believe, who might disagree | `adactio2017anotherlens` | list items 6-10 | Who's someone I'm nervous to talk to about this? | free copy: https://adactio.com/links/13162 |
| 8 | Lens 3 questions: challenging as I create / audience open to change; learn one thing; approach vs one year ago; reframe a mistake; do I need to slow down | `adactio2017anotherlens` | list items 11-16 | How can I reframe a mistake in a way that helps me learn? | free copy: https://adactio.com/links/13162 |
| 9 | Assignment of questions to lenses (4 / 4 / 5 questions) | `airbnb2017anotherlens` | to verify | (guess) cards grouped under each principle heading | metadata only: the blog quotes a flat list of 16 questions with no lens grouping; the Airbnb page was not readable. SKILL.md has 13 numbered questions by merging some |
| 10 | Colours (green, purple, orange) and "three half-circles that together form a whole" | `airbnb2017anotherlens` | to verify | (guess) half-circle / whole | not found: no page read mentions colours or half-circles. Search terms tried: "Another Lens" half circles colors, Airbnb Design Another Lens three half circles |
| 11 | Origin: grew from a bias installation; built with a journalism partner | `core77another` | listing text | Shadow to Light installation | toolkit page: not stated in SKILL.md at all |
| 12 | "Pick two or three questions at a time" use guidance | `airbnb2017anotherlens` | landing page | pick two or three at a time | toolkit page: from search summary. SKILL.md instead walks every question of a lens one by one |
| 13 | "Principle #07 — Another Lens"; hashtags #breakmydesign #newperspectives #designresponsibility; see also Data Feminism, Hippocratic Oath | `chivukula2025universal` | to verify | (guess) Another Lens | metadata only: book. Publisher listings give no contents; not confirmed that Another Lens is in the book |
| 14 | Method is "deeply Socratic"; asks questions, no correct output | `chivukula2025universal` | to verify | (guess) questions to challenge assumptions | metadata only: book. The blog post describes the tool as questions that challenge assumptions, not as Socratic |
| 15 | Reference file claims: designer bias list (sunk cost etc.), populations absent from research and how to reach them | none cited | `references/bias-taxonomy.md`, `references/opposite-perspectives.md` | n/a | not found: no source named in the files. Searched the repo for "source/credit/doi/http" in references; nothing |
| 16 | "Quick pass = Lens 2 alone", time budgets, lens statement, Design Decision Spec table, Evidence Ledger | edbx additions | n/a | n/a | not found as source claims; the SKILL.md itself labels the Ledger "a family convention", the others are unlabelled additions |
| 17 | WCAG 2.2 SC 2.5.5 touch target 44x44 | `w3c2023wcag22` | SC 2.5.5 Target Size (Enhanced) | at least 44 by 44 CSS pixels | free copy: https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html. Level AAA; the unit is CSS pixels, SKILL.md says "pt" |
| 18 | WCAG 2.2 SC 1.4.6 contrast 7:1; SC 1.4.3 contrast 4.5:1 | `w3c2023wcag22` | SC 1.4.6 Contrast (Enhanced); SC 1.4.3 Contrast (Minimum) | 4.5:1 ratio is used in Success Criterion 1.4.3 | free copy: https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html. 1.4.6 is AAA with 7:1 for normal text; the AA level of 1.4.3 is implied on that page, to verify on its own page |

## Licence

- **Airbnb Design "Another Lens" (`airbnb2017anotherlens`)**: licence unknown. No terms statement was found, and the page is offline, so presume all rights reserved. Check the Airbnb Design site terms, or archived copies, in stage B. Meaning for this repo: paraphrasing the idea (three perspectives; ask questions about your own assumptions) is fine. Reproducing the 16 question wordings verbatim as a deck is a risk until the terms are known. SKILL.md and `three-lenses.md` currently carry near-verbatim questions in a paid bundle, so keep them short, attribute them to Airbnb Design, or reword. Shipping a modified version is not clearly allowed or forbidden.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. A secondary compilation. Describe the method in our own words; do not reproduce its method profile text, hashtags or diagrams beyond a short citation.
- **Adactio / Core77 pages**: personal blog and listing; they hold no licence over Airbnb's questions. Link to them, do not copy them.
- **WCAG 2.2**: W3C Document License. Citing criteria numbers, levels and short thresholds is fine. Do not paste long passages.
- Nothing found blocks commercial redistribution outright, but the Airbnb terms are the open question.

## Discrepancies

1. **Misattributed or missing creator.** SKILL.md credits only *Universal Methods of Ethical Design* ("Principle #07"). The method is by Airbnb Design with News Deeply (2017). The book's authors, Chivukula and Gray, are also not named. Add Airbnb Design as the primary source.
2. **Altered question wording.** The source asks "What details here are unfair? Unverified? Unused?". SKILL.md (Lens 1 Q2 and the reference text) says "Unjustified". Restore "Unverified" or mark the change as edbx's own.
3. **Question count and grouping.** The source list I could read has 16 questions; SKILL.md has 13 by merging (lenses, assumptions; believe, disagree; audience open, challenging). Grouping into 4 / 4 / 5 could not be confirmed.
4. **Colours and half-circle shapes** (green, purple, orange; three half-circles forming a whole): no source found. Treat as edbx presentation or remove the attribution until verified in the book.
5. **Use guidance differs from the source.** The source suggests picking two or three questions at a time. SKILL.md prescribes a full sequential walk of every question (one at a time with probes) and 45-60 minute sessions. That is an adaptation, not the method.
6. **Claims presented as the method that are edbx's own**: "Q3 is the most powerful question in the entire method", "required output of every Lens 2 session", the Socratic label, the Design Decision Spec, the lens statement ("After applying Another Lens, I'm now questioning ..."), the time budgets, and the "Output of Lens N" deliverables. None is in the source material I read.
7. **WCAG unit.** Example row says "44x44 pt (WCAG 2.2 SC 2.5.5)". The criterion says CSS pixels, and is Level AAA. SC 1.4.6 is also AAA. The example presents them as requirements without the level.
8. **Book content unverified.** Publisher pages do not show contents, so "Principle #07", the hashtags and the "See also: Data Feminism · Hippocratic Oath" line cannot be confirmed without the book.
9. **Reference files cite no sources** for the bias taxonomy and the absent-populations guidance (row 15).

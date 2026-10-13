# Provenance — edbx-responsible-design-prism

Stage A draft (2026-10-13). One row per element the skill attributes to a
source. Locator and anchor are what could be confirmed from web pages read in
this pass (no files downloaded). Where a page could not confirm an element,
Locator says `to verify` and the anchor is a guess marked `(guess)`. Stage B
checks each anchor on the page.

**Headline: the primary source for the Responsible Design Prism was not found.**
It is listed by name as method 79 in *Universal Methods of Ethical Design*
(a secondary compilation) with no creator credited. Searches for the name, for
its axis labels, and for its vertices returned nothing. The one candidate
(Mildner's 2024 thesis on "responsible design") is a different model on the
pages that could be read, so it is recorded as a candidate to check, not as the
source.

## Sources

| Key | Full citation | URL | Free copy | Licence |
|---|---|---|---|---|
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto Group), 1 April 2025. ISBN 9780760393086 (hardcover), 9780760393093 (ebook). Lists Responsible Design Prism as method 79 (between Responsible AI Practices and Security Cards). | https://www.quarto.com/books/9780760393086/universal-methods-of-ethical-design ; method list: https://universalmethodsofethicaldesign.com/resources/ | no | unknown (commercial book; copyright statement not read; check the imprint page) |
| `mildner2024mitigating` | Mildner, T. (2024). *Mitigating dark patterns through responsible design: ethical design considerations for user-centred technologies*. Doctoral dissertation, Universität Bremen (Digital Media Lab; supervisor R. Malaka). DOI 10.26092/elib/3095 (as given by a search result, not confirmed on the repository). Candidate only; see row 1. | https://www.uni-bremen.de/en/dmlab/research/thomas-mildner-2024 ; repository record https://media.suub.uni-bremen.de/handle/elib/8061 (record page did not load in this pass; the full-text PDF link exists but was not opened) | probably yes (university repository). Not confirmed | unknown (the dmlab page shows only "© Universität Bremen"; the repository record was not readable) |
| `gray2018dark` | Gray, C. M., Kou, Y., Battles, B., Hoggatt, J. & Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. *Proc. CHI 2018*, paper 534. doi:10.1145/3173574.3174108 | https://doi.org/10.1145/3173574.3174108 | not confirmed; candidate pages (not opened): https://darkpatterns.uxp2.com/?p=624 and https://www.deceptive.design/articles/the-dark-patterns-side-of-ux-design | unknown (ACM DL record not read) |
| `brignull2023deceptive` | Brignull, H. Deceptive Patterns (formerly Dark Patterns, darkpatterns.org): "Types of deceptive pattern". Site footer: © 2026 Testimonium Ltd. Brignull's 2023 book of the same name was not checked. | https://www.deceptive.design/types | yes, web page | no licence stated; the page asks for attribution ("how to cite this website") |
| `narayanan2020dark` | Narayanan, A., Mathur, A., Chetty, M. & Kshirsagar, M. (2020). Dark Patterns: Past, Present, and Future. *ACM Queue* 18(2), 67-92. | https://www.deceptive.design/articles/dark-patterns-past-present-and-future | yes, web page (copy hosted by deceptive.design; Princeton portal lists it) | unknown |
| `mildner2024hell` | Mildner, T., Inkoom, A., Malaka, R. & Niess, J. (2024). Hell is Paved with Good Intentions: The Intricate Relationship Between Cognitive Biases and Dark Patterns. arXiv:2405.07378 (author-version draft under review). doi:10.48550/arXiv.2405.07378 | https://arxiv.org/abs/2405.07378 | yes, arXiv | CC BY 4.0 (stated on the arXiv page) |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | The Responsible Design Prism as a named method (reflective evaluation along a spectrum from dark patterns to responsible design) | `chivukula2025universal` | method 79 (list only) | Responsible Design Prism | metadata only: book. Primary source not found. Searches tried: "responsible design prism"; the axis labels in quotes; "prism" with Mildner, Savino, Malaka; "user as means" with dark patterns. Candidate to check: `mildner2024mitigating` (its "Responsible Design Triangle" has three angles: design, users, guidelines; the page does not mention a prism) |
| 2 | Visual: two overlapping triangles forming a prism; vertices User, Incentives, Dark Pattern; overlap = transition zone | `mildner2024mitigating` | to verify | (guess) intentions, incentives, design philosophies | metadata only: free copy not opened. A search snippet of the thesis abstract says interfaces are framed by intentions, incentives and design philosophies. Not a confirmed match; the Triangle on the page read has different vertices |
| 3 | Five spectrum axes and their poles (User as Means / User as Themselves; Setting False Expectations / Transparent Communication; Taking Advantage of Errors / Inform and Support Recovery; Exploitative Incentives / Fair Practice Guidelines; Weaponized / Genuine Usability) | none found | to verify | (guess) taking advantage of errors | not found. None of the five pole labels returned a hit. "User as means" echoes Kantian wording, which no source read uses |
| 4 | Red / Yellow / Green scoring of each axis | none found | to verify | (guess) transitional zone | not found. Likely an edbx scoring layer; the skill itself says the prism is a spectrum |
| 5 | Four reflection prompts: self-reflection, organization ecology, transition, recovery | none found | to verify | (guess) how do you find your way back | not found. Searches combining those words with Mildner returned nothing |
| 6 | Dark pattern taxonomy in five groups: Deception, Coercion, Exploitation, Manipulation, Obstruction | `gray2018dark` | abstract / taxonomy | nagging, obstruction, sneaking, interface interference, forced action | metadata only: paywalled. Gray et al. group patterns into five *different* strategies. `brignull2023deceptive` lists 18 types with no grouping. The skill's five group names match neither |
| 7 | Pattern names used in the taxonomy and scoring (confirmshaming, hidden costs, hidden subscription, hard-to-cancel, preselection, visual interference, disguised ads) | `brignull2023deceptive` | Types of deceptive pattern | Confirmshaming | toolkit page. These names are on the current list. "Roach Motel", "Sneak into Basket", "Forced Continuity", "Bait and Switch", "Trick Questions" are not on the current list (it has Hard to cancel, Sneaking, Hidden subscription, Trick wording); they may be from the older darkpatterns.org list, which was not read |
| 8 | Fakery patterns (Urgency Fakery, Social Proof Fakery, Scarcity Fakery) | `brignull2023deceptive` | Types of deceptive pattern | Fake urgency | toolkit page. Current names are Fake urgency, Fake social proof, Fake scarcity. Wording differs |
| 9 | Intermediate Currency | `brignull2023deceptive` | Types of deceptive pattern | Currency Confusion | toolkit page. Same idea, different name |
| 10 | Attention Capture, Gamification Exploitation | `brignull2023deceptive` | Types of deceptive pattern | Addictive Design | toolkit page. Nearest current entry is "Addictive Design" (excessive, compulsive use). "Gamification Exploitation" and "Attention Capture" are not listed |
| 11 | Hard-to-Delete, Immense Overload, Emotional Manipulation, Exploiting Error, Misleading Pricing, False Expectations, Hard-to-Compare | none found | to verify | (guess) comparison prevention | not found as named. Nearest current names: Comparison prevention, Obstruction, Sneaking, Confirmshaming |
| 12 | Taxonomy credited as "adapted from darkpatterns.org / deceptive.design taxonomy and academic literature" | `brignull2023deceptive` | site history | formerly called "Dark Patterns" | toolkit page. Site confirms the rename from darkpatterns.org. No academic paper is named in the skill for the taxonomy |
| 13 | Psychological mechanism list (default bias, loss aversion, anchoring, social proof, scarcity heuristic, sunk cost, present bias; variable reward, streak loss; FOMO; adolescent developmental vulnerabilities) | none cited | n/a | n/a | not found. The skill gives no source. Related work: `mildner2024hell` builds a model linking cognitive biases to dark patterns from four focus groups with 15 experts (abstract page) |
| 14 | Stakeholder & vulnerable population map (Step 1.5); Evidence Ledger | none | n/a | n/a | not found. edbx additions; Evidence Ledger is declared in SKILL.md as a fdbx convention |
| 15 | Business framing: regulatory, reputation, support, retention and talent cost; "stakeholders respect honesty"; framing templates and objection scripts | none cited | n/a | n/a | not found. Unsourced; includes claims about user behaviour and enforcement history (e.g., hidden cookie consent now triggering enforcement) with no source |
| 16 | Further Reading: Nielsen (2020) "Responsible Design", NN/g | none found | n/a | n/a | not found. Searched: "Nielsen Norman Group Jakob Nielsen 2020 Responsible Design". No such article surfaced |
| 17 | Further Reading: Gray & McDowell (2019) "Dark Patterns: Past, Present, and Future" | `narayanan2020dark` | article record | Dark Patterns: Past, Present, and Future | toolkit page. Title exists, but the authors are Narayanan, Mathur, Chetty and Kshirsagar, in *ACM Queue* 2020, not Gray & McDowell 2019. See Discrepancies |
| 18 | Further Reading: Brignull (2023) "Deceptive Design Patterns", deceptive.design | `brignull2023deceptive` | site | deceptive.design | toolkit page. Site is real and currently called "Deceptive Patterns"; the exact title "Deceptive Design Patterns" for a 2023 item was not confirmed |
| 19 | Further Reading: Worldwide Web Foundation (2021) "Ethical Design Framework" | none found | n/a | n/a | not found. Searched: "World Wide Web Foundation 2021 Ethical Design Framework". Nearest hits: W3C *Ethical Web Principles* and a Web Foundation workshop series on deceptive design (no date seen) |

## Licence

- **`chivukula2025universal`.** Unknown. Commercial book, so assume nothing beyond the method name and number may be reproduced. Check the imprint page. We may paraphrase an idea; we may not reproduce entry text, figures or sidenotes.
- **Primary source for the Prism.** Not found, so its licence is unknown and nothing can be stated about reproducing the five axes, the prism visual or the reflection prompts. Treat those as the skill's own wording until a source is found. If the source turns out to be `mildner2024mitigating`, check the repository record for the rights statement before reusing any figure.
- **`mildner2024mitigating`.** Unknown. Paraphrasing the thesis's ideas is fine; do not reproduce its figures or text until the repository terms are read.
- **`brignull2023deceptive`.** No licence stated; the page asks for attribution. Paraphrasing names and one-line meanings is normal practice; do not copy the site's definitions verbatim or its data (it credits law and enforcement data to the Leiser, Santos & Doshi database). The skill's own definitions (references/dark-pattern-taxonomy.md) are paraphrases and should stay that way.
- **`gray2018dark`, `narayanan2020dark`.** Unknown from pages read. Cite, paraphrase; do not copy.
- **`mildner2024hell`.** CC BY 4.0: commercial use and modification allowed with attribution. Not currently reproduced by the skill.
- Nothing found forbids commercial use or modification. The gap is the opposite: the main method has no located source, so attribution in the repo cannot be completed.

## Discrepancies

### Contradicted by the source (I read the source and it says otherwise)

1. **Further Reading: "Gray, C.M. & McDowell (2019). 'Dark Patterns: Past, Present, and Future.'"** The paper with that title is by Narayanan, Mathur, Chetty and Kshirsagar, *ACM Queue* 18(2), 2020 (`narayanan2020dark`). Gray is not an author; the year is 2020. The site named in that entry, darkpatterns.org, is now deceptive.design (its types page is at /types).
2. **Taxonomy grouping.** references/dark-pattern-taxonomy.md says the taxonomy is "adapted from darkpatterns.org / deceptive.design", with five groups (Deception, Coercion, Exploitation, Manipulation, Obstruction). deceptive.design presents 18 types as a flat list with no groups (`brignull2023deceptive`), and Gray et al.'s five strategies are nagging, obstruction, sneaking, interface interference and forced action (search-result summary of `gray2018dark`). The five-group scheme is the skill's own, and neither source read uses it.
3. **Pattern names.** Several names in the taxonomy are not on the current deceptive.design list (rows 7-11), and some listed names are different there (Fake urgency/social proof/scarcity; Currency Confusion; Trick wording). Where the skill says "adapted from" that site, the names have drifted.

### Not found in a readable source (could not confirm; no readable primary source)

4. The whole structure of the Prism: two overlapping triangles, the vertices User / Incentives / Dark Pattern, the five axes and their poles, the transition zone, and the four reflection prompts (rows 2-5). SKILL.md presents these as the framework's own. No page read contains them. The candidate thesis was not read in full.
5. Red / Yellow / Green scoring. Probably an edbx layer; SKILL.md does not mark it as an adaptation.
6. Further Reading items: Nielsen (2020) "Responsible Design" (no such NN/g article found) and Worldwide Web Foundation (2021) "Ethical Design Framework" (not found; closest is W3C *Ethical Web Principles*). Brignull (2023) title is also unconfirmed as written.
7. The mechanism list and the business-framing claims have no cited source (rows 13, 15).
8. "Most real-world designs land in the transitional zone" (Overview) is stated as fact; no source read supports it.
9. Repo attribution: `THIRD_PARTY_NOTICES.md` credits the Prism to "HCI and responsible technology research" with no named source, while it is a published book method (#79 in `chivukula2025universal`). The notice needs a real citation once the primary source is found.

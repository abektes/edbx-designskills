# Provenance — edbx-responsible-design-prism

Stage B (2026-10-13). One row per element the skill attributes to a source.
Only `mildner2024hell` and `gray2024ontology` are in `papers/manifest.json`
(texts in `papers/pages/`). For those, Locator `p. N` / `web` means the anchor
was copied verbatim from the text, and `not in source` means the text was read
and the element is absent (the anchor is the closest passage). Every other
source is marked `metadata only` with the reason; none of them was fetched.

**Headline: the primary source for the Responsible Design Prism was not found.**
It is listed by name as method 79 in *Universal Methods of Ethical Design*
(a secondary compilation) with no creator credited. Searches for the name, for
its axis labels, and for its vertices returned nothing. The one candidate
(Mildner's 2024 thesis on "responsible design") is not in the manifest and was
not fetched, so it is recorded as a candidate, not as the source. Stage B
checked the two manifest sources that bear on the skill and found neither
contains the Prism.

## Sources

| Key | Full citation | URL | Free copy | Licence |
|---|---|---|---|---|
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design: 100 Ways to Become More Ethically Aware, Responsible, and Active in Your Design Work*. Rockport Publishers (Quarto Group), 1 April 2025. ISBN 9780760393086 (hardcover), 9780760393093 (ebook). Lists Responsible Design Prism as method 79 (between Responsible AI Practices and Security Cards). | https://www.quarto.com/books/9780760393086/universal-methods-of-ethical-design ; method list: https://universalmethodsofethicaldesign.com/resources/ | no | unknown (commercial book; copyright statement not read; check the imprint page) |
| `mildner2024mitigating` (not in manifest; not fetched) | Mildner, T. (2024). *Mitigating dark patterns through responsible design: ethical design considerations for user-centred technologies*. Doctoral dissertation, Universität Bremen (Digital Media Lab; supervisor R. Malaka). DOI 10.26092/elib/3095 (as given by a search result, not confirmed on the repository). Candidate only; see row 1. | https://www.uni-bremen.de/en/dmlab/research/thomas-mildner-2024 ; repository record https://media.suub.uni-bremen.de/handle/elib/8061 (record page did not load in this pass; the full-text PDF link exists but was not opened) | probably yes (university repository). Not confirmed | unknown (the dmlab page shows only "© Universität Bremen"; the repository record was not readable) |
| `gray2018dark` (not in manifest; paywalled) | Gray, C. M., Kou, Y., Battles, B., Hoggatt, J. & Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. *Proc. CHI 2018*, paper 534. doi:10.1145/3173574.3174108 | https://doi.org/10.1145/3173574.3174108 | not confirmed; candidate pages (not opened): https://darkpatterns.uxp2.com/?p=624 and https://www.deceptive.design/articles/the-dark-patterns-side-of-ux-design | unknown (ACM DL record not read) |
| `brignull2023deceptive` (not in manifest; not fetched) | Brignull, H. Deceptive Patterns (formerly Dark Patterns, darkpatterns.org): "Types of deceptive pattern". Site footer: © 2026 Testimonium Ltd. Brignull's 2023 book of the same name was not checked. | https://www.deceptive.design/types | yes, web page | no licence stated; the page asks for attribution ("how to cite this website") |
| `narayanan2020dark` (not in manifest; not fetched) | Narayanan, A., Mathur, A., Chetty, M. & Kshirsagar, M. (2020). Dark Patterns: Past, Present, and Future. *ACM Queue* 18(2), 67-92. | https://www.deceptive.design/articles/dark-patterns-past-present-and-future | yes, web page (copy hosted by deceptive.design; Princeton portal lists it) | unknown |
| `mildner2024hell` | Mildner, T., Inkoom, A., Malaka, R. & Niess, J. (2024). Hell is Paved with Good Intentions: The Intricate Relationship Between Cognitive Biases and Dark Patterns. arXiv:2405.07378 (author-version draft under review). doi:10.48550/arXiv.2405.07378 | https://arxiv.org/abs/2405.07378 | yes, arXiv | CC BY 4.0 per the stage A read of the arXiv abstract page; the manifest says "arXiv licence"; no licence statement appears in the PDF text (searched for licence, Creative Commons, CC BY) |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | The Responsible Design Prism as a named method (reflective evaluation along a spectrum from dark patterns to responsible design) | `chivukula2025universal` | method 79 (list only) | Universal Methods of Ethical Design | metadata only: book. Primary source not found. Searches tried in stage A: "responsible design prism"; the axis labels in quotes; "prism" with Mildner, Savino, Malaka. Stage B searched every fetched page under `papers/pages/` for "prism": no match anywhere |
| 2 | Visual: two overlapping triangles forming a prism; vertices User, Incentives, Dark Pattern; overlap = transition zone | `mildner2024mitigating` | n/a | Mitigating dark patterns through responsible design | metadata only: no source found. The thesis is a candidate only; it is not in the manifest and was not read. A stage A search snippet says interfaces are framed by intentions, incentives and design philosophies; not a confirmed match |
| 3 | Five spectrum axes and their poles (User as Means / User as Themselves; Setting False Expectations / Transparent Communication; Taking Advantage of Errors / Inform and Support Recovery; Exploitative Incentives / Fair Practice Guidelines; Weaponized / Genuine Usability) | `none` | n/a | Setting False Expectations / Transparent Communication | metadata only: no source found. None of the five pole pairs returned a hit in stage A |
| 4 | Red / Yellow / Green scoring of each axis | `none` | n/a | Score each axis as Red, Yellow, or Green | metadata only: no source found. Probably an edbx scoring layer; SKILL.md does not label it as one |
| 5 | Four reflection prompts: self-reflection, organization ecology, transition, recovery | `none` | n/a | How do you find your way back to the right side | metadata only: no source found. The anchor is the skill's own Prompt 4 wording |
| 6 | Dark pattern taxonomy in five groups: Deception, Coercion, Exploitation, Manipulation, Obstruction (taxonomy file: "adapted from darkpatterns.org / deceptive.design taxonomy and academic literature") | `gray2024ontology` | not in source | three-level ontology with standardized definitions for 64 synthesized dark pattern types | The deceptive.design article page describes a three-level ontology (low-, meso-, high-level) of 64 synthesized types, harmonised from ten taxonomies. It has no five-group scheme and does not name the skill's groups |
| 7 | Gray et al. strategies (nagging, obstruction, sneaking, interface interference, forced action) as the nearest published five-way scheme | `gray2018dark` | n/a | The Dark (Patterns) Side of UX Design | metadata only: paywalled. Stage A search summary only. The skill's five group names do not match these |
| 8 | Pattern names used in the taxonomy and scoring (confirmshaming, hidden costs, hidden subscription, hard-to-cancel, preselection, visual interference, disguised ads) | `brignull2023deceptive` | n/a | Confirmshaming, sneak into basket, hidden costs | metadata only: not in manifest; types page read in stage A only, not fetched. Stage A found these names on the current list except Roach Motel, Sneak into Basket, Forced Continuity, Bait and Switch, Trick Questions |
| 9 | Fakery patterns (Urgency Fakery, Social Proof Fakery, Scarcity Fakery) | `brignull2023deceptive` | n/a | Urgency Fakery, Social Proof Fakery, Scarcity Fakery | metadata only: not in manifest. Stage A: current names are Fake urgency, Fake social proof, Fake scarcity |
| 10 | Intermediate Currency | `brignull2023deceptive` | n/a | Hard-to-Cancel, Hard-to-Delete, Intermediate Currency | metadata only: not in manifest. Stage A: nearest current name is Currency Confusion |
| 11 | Attention Capture, Gamification Exploitation | `brignull2023deceptive` | n/a | Attention Capture, Gamification Exploitation | metadata only: not in manifest. Stage A: nearest current entry is Addictive Design |
| 12 | Hard-to-Delete, Immense Overload, Emotional Manipulation, Exploiting Error, Misleading Pricing, False Expectations, Hard-to-Compare | `none` | n/a | Immense Overload, Emotional Manipulation, Exploiting Error | metadata only: no source found. Not found as named in stage A; nearest current names: Comparison prevention, Obstruction, Sneaking, Confirmshaming |
| 13 | Site rename: darkpatterns.org is now deceptive.design | `gray2024ontology` | web | formerly called Dark Patterns (darkpatterns.org) | Confirmed by the site footer on the fetched page. The page also asks for attribution ("how to cite this website") and credits law and enforcement data to the Leiser, Santos & Doshi database. It does not list any pattern types |
| 14 | Psychological mechanism list (default bias, loss aversion, anchoring, social proof, scarcity heuristic, sunk cost, present bias; variable reward, streak loss; FOMO; adolescent developmental vulnerabilities) | `mildner2024hell` | p. 1 | cognitive biases, such as the framing effect or the default effect | Partial support only. The paper says dark patterns exploit cognitive biases and names the framing, default and decoy effects. Loss aversion, social proof, scarcity, sunk cost, present bias, variable reward, streak loss and FOMO are not named in its body text (anchoring appears only in a reference title). The skill gives no source for its list |
| 15 | Stakeholder & vulnerable population map (Step 1.5); Evidence Ledger | `none` | n/a | Stakeholder & Vulnerable Population Mapping | metadata only: edbx addition. SKILL.md declares the Evidence Ledger an fdbx family convention; the Step 1.5 map is not labelled |
| 16 | Business framing: regulatory, reputation, support, retention and talent cost; "stakeholders respect honesty"; framing templates and objection scripts | `none` | n/a | Business case for the ethical alternative | metadata only: no source found. Unsourced; includes claims about user behaviour and enforcement history with no source |
| 17 | Further Reading: Nielsen (2020) "Responsible Design", NN/g | `none` | n/a | Responsible Design Nielsen Norman Group | metadata only: no source found. Stage A found no such article |
| 18 | Further Reading: Gray & McDowell (2019) "Dark Patterns: Past, Present, and Future" | `narayanan2020dark` | n/a | Dark Patterns: Past, Present, and Future | metadata only: not in manifest; article record read in stage A only. Title exists but the authors are Narayanan, Mathur, Chetty and Kshirsagar (*ACM Queue*, 2020) |
| 19 | Further Reading: Brignull (2023) "Deceptive Design Patterns", deceptive.design | `brignull2023deceptive` | n/a | Deceptive Design Patterns Brignull deceptive.design | metadata only: not in manifest. Site is real and now titled "Deceptive Patterns"; the exact title was not confirmed |
| 20 | Further Reading: Worldwide Web Foundation (2021) "Ethical Design Framework" | `none` | n/a | Worldwide Web Foundation Ethical Design Framework | metadata only: no source found. Nearest stage A hits: W3C *Ethical Web Principles* |

## Licence

- **`chivukula2025universal`.** Unknown. Commercial book, so assume nothing beyond the method name and number may be reproduced. Check the imprint page. We may paraphrase an idea; we may not reproduce entry text, figures or sidenotes.
- **Primary source for the Prism.** Not found, so its licence is unknown and nothing can be stated about reproducing the five axes, the prism visual or the reflection prompts. Treat those as the skill's own wording until a source is found. If the source turns out to be `mildner2024mitigating`, check the repository record for the rights statement before reusing any figure.
- **`mildner2024mitigating`.** Unknown. Paraphrasing the thesis's ideas is fine; do not reproduce its figures or text until the repository terms are read.
- **`brignull2023deceptive`.** No licence stated; the page asks for attribution. Paraphrasing names and one-line meanings is normal practice; do not copy the site's definitions verbatim or its data (it credits law and enforcement data to the Leiser, Santos & Doshi database). The skill's own definitions (references/dark-pattern-taxonomy.md) are paraphrases and should stay that way.
- **`gray2018dark`, `narayanan2020dark`.** Unknown from pages read. Cite, paraphrase; do not copy.
- **`mildner2024hell`.** CC BY 4.0 according to the arXiv abstract page (stage A); the PDF text carries no licence statement, so Stage B cannot confirm it. If CC BY 4.0, commercial use and modification are allowed with attribution. Not currently reproduced by the skill.
- Nothing found forbids commercial use or modification. The gap is the opposite: the main method has no located source, so attribution in the repo cannot be completed.

## Discrepancies

### Contradicted by the source text (read on the fetched page)

1. **Taxonomy grouping.** references/dark-pattern-taxonomy.md says its five groups (Deception, Coercion, Exploitation, Manipulation, Obstruction) are adapted from the deceptive.design taxonomy and academic literature. The deceptive.design page on Gray et al.'s ontology describes a three-level ontology of 64 synthesized types harmonised from ten taxonomies, with no five-group scheme (`gray2024ontology`, row 6).
2. **The Prism is absent from the manifest sources.** Neither manifest source bearing on the skill contains it, and no fetched page, including `mildner2024hell`, contains the word "prism" (row 1).

### Not verifiable (no readable source)

3. The whole structure of the Prism: two overlapping triangles, the vertices User / Incentives / Dark Pattern, the five axes and their poles, the transition zone, and the four reflection prompts (rows 2-5). SKILL.md presents these as the framework's own. The candidate thesis (`mildner2024mitigating`) is not in the manifest.
4. Red / Yellow / Green scoring (row 4); probably an edbx layer that SKILL.md does not mark.
5. Pattern names in rows 8-12 and the Brignull site: not fetched. Stage A reported name drift (e.g. Fake urgency, Currency Confusion, Trick wording), which Stage B cannot re-check. The 18-type flat list claim is likewise stage A only.
6. **Further Reading.** "Gray, C.M. & McDowell (2019). Dark Patterns: Past, Present, and Future" appears mis-attributed (stage A: the paper is Narayanan et al., ACM Queue 2020); Nielsen (2020) "Responsible Design" and Web Foundation (2021) "Ethical Design Framework" were not found; the Brignull title is unconfirmed (rows 17-20).
7. The mechanism list beyond the framing, default and decoy effects (row 14), and the business-framing claims (row 16) have no source. "Most real-world designs land in the transitional zone" (Overview) is stated as fact with no source.
8. Repo attribution: `THIRD_PARTY_NOTICES.md` credits the Prism to "HCI and responsible technology research" with no named source, while it is method 79 in `chivukula2025universal`. The notice needs a real citation once the primary source is found.
9. Licence of `mildner2024hell`: the PDF text contains no licence statement; "CC BY 4.0" rests on the stage A read of the arXiv abstract page.

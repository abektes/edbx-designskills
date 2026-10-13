# Provenance — edbx-inverted-behavior-model

Stage A draft (sources and licences, no downloads). One row per element the
skill attributes to a source. Locator and anchor are what could be confirmed
from pages read in this pass; otherwise Locator is `to verify` and the anchor
is marked `(guess)`. Stage B checks each anchor on the page.

Key finding: the method is the **Inverted Behavior Model of the Design Ethically
toolkit**, made by Kat (Katherine M.) Zhou, which inverts BJ Fogg's Behavior
Model to forecast unintended behaviours. The UXP2 "Improving Everyday Ethics"
methods microsite (Carlock, April 2022) lists it with four steps and names
Zhou as the method's designer. SKILL.md and `THIRD_PARTY_NOTICES.md` credit
only "BJ Fogg, Fogg Behavior Model (B = MAP)" and never name Zhou or the
Design Ethically toolkit. Most of what SKILL.md presents as the method (Step 0,
the worst-design artifact, the convergence check, the cascade model, the
rationalizations check) is not on any page read; the source method is the
four-step prompt, motivation, behaviour, consequence flow.

Pages were read through a fetch tool that summarises each page, so quoted
anchors are as reported by that tool, not copied from raw HTML. Image content
(the Facebook example, the worksheet image) was not read.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `zhou2026invertedbehavior` | Zhou, K. M. ("Kat"). *BJ Fogg's Inverted Behavior Model.* Design Ethically (toolkit page, footer dated 2026; first-publication date not shown). | https://www.designethically.com/bj-fogg | yes, it is a web page | unknown: footer reads "(c) Copyright Design Ethically 2026"; no licence statement. Presume all rights reserved. Check by contacting the site owner |
| `zhou2026toolkit` | Zhou, K. M. *Design Ethically Toolkit* (index of methods, lists Inverted Behavior Model and Motivation Matrix under "Forecasting"). | https://www.designethically.com/toolkit | yes, web page | unknown: same copyright line only; page says nothing on reuse |
| `carlock2022inverted` | Carlock, T. (10 Apr 2022). *Inverted Behavior Model.* Improving Everyday Ethics (UXP2 Lab, Purdue). Page says "Method designed by: Katherine M. Zhou"; steps are attributed to the Design Ethically website. | https://everydayethics.uxp2.com/methods/inverted-behavior-model/ | yes, web page | unknown: no licence or copyright statement for the content (footer credits only the WordPress theme) |
| `fogg2026behaviormodel` | Fogg, B. J. *Fogg Behavior Model* (B=MAP). behaviormodel.org. | https://www.behaviormodel.org/ | yes, web page | unknown: footer "(c) 2026 BJ Fogg"; no licence terms. Presume all rights reserved |
| `fogg2009behavior` | Fogg, B. J. (2009). A behavior model for persuasive design. *Proceedings of the 4th International Conference on Persuasive Technology.* ACM. | doi:10.1145/1541948.1541999 | not checked. Crossref record lists no abstract and an ACM copyright policy link; ACM landing page returned 403 | ACM copyright; treat as all rights reserved unless an open copy is found (a resolver listing suggested one might exist; not opened) |
| `chivukula2022surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. and Gray, C. M. (2021, rev. 2022). Surveying the landscape of ethics-focused design methods. arXiv:2102.08909. The preprint the microsite says it is "based off of". | https://arxiv.org/abs/2102.08909 (doi:10.48550/arXiv.2102.08909) | yes: arXiv, open access (landing page only was read; PDF not fetched) | CC BY-NC-SA 4.0, per the licence icon on the arXiv page (the licence of the paper, not necessarily of the microsite or toolkit) |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design.* Rockport Publishers (Quarto). ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved, paywalled book |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: Inverted Behavior Model, an evaluative model for teams to critically evaluate design features and reveal their user behaviours and consequences | `carlock2022inverted` | description paragraph | critically evaluate design features | toolkit page. Page names Katherine M. Zhou as designer; SKILL.md credits Fogg only (Discrepancy 1) |
| 2 | The inversion of Fogg's model (forecasting what a product motivates, rather than designing a target behaviour) | `zhou2026invertedbehavior` | page intro | invert Fogg's behavior model (guess) | toolkit page. Page describes forecasting unintended behaviours and consequences; the Overview of SKILL.md matches this. Fogg's own page does not mention an inversion (Discrepancy 2) |
| 3 | Fogg Behavior Model: behaviour occurs when Motivation, Ability and Prompt converge | `fogg2026behaviormodel` | home page | Motivation, Ability, and a Prompt come together | toolkit page. Fogg writes B=MAP and "converge at the same moment"; "Prompt" is his current term. The "+" in "B = Motivation + Ability + Prompt" is SKILL.md's notation (Discrepancy 7) |
| 4 | Earlier form of Fogg's model (terminology and formula in the 2009 paper) | `fogg2009behavior` | to verify | (guess) Behavior = Motivation, Ability, Trigger | metadata only: paywalled. Not read; SKILL.md does not cite the paper, and the claim that the 2009 term was "Trigger" is model knowledge, not confirmed |
| 5 | Core flow: list the prompts (features); identify motivations for each; predict behaviours; analyse consequences (SKILL.md Steps 1, 2, 3, 4) | `zhou2026invertedbehavior` | steps 1-4 | List the prompts to analyze | toolkit page. Same four steps on `carlock2022inverted` ("Start by listing the design features (prompts)"). SKILL.md's order and meaning match |
| 6 | Source steps SKILL.md omits: estimate the ability each behaviour requires and rank behaviours by likelihood; optionally rank by severity | `zhou2026invertedbehavior` | steps 5-6 | rank behaviors by likelihood | toolkit page. Not in SKILL.md at all, although "Ability" is the A in the model it invokes (Discrepancy 3) |
| 7 | Definition of a prompt: "any element that triggers a user action (notification, button, feed, score, streak, countdown)" | `zhou2026invertedbehavior` | to verify | (guess) prompts can be features or whole products | toolkit page. Source says prompts can be individual features or whole products; the list of examples and the trigger wording are SKILL.md's. Fogg's definition on `fogg2026behaviormodel` was not read |
| 8 | Five motivating-factor categories (intrinsic, social, extrinsic, emotional, habitual) | none found | n/a | n/a | not found. No source page read lists these; the source says only "list the motivating factors that might apply". Fogg's own motivator pairs were not read. Searched: Inverted Behavior Model motivating factors categories |
| 9 | Step 0 stakeholder map (six populations incl. bystanders, supply-chain workers, regulators, future-affected) | none found | n/a | n/a | not found. Not in either method page; edbx addition presented as part of the method (Discrepancy 4) |
| 10 | Step 2.5 Worst Possible Design "inversion artifact", described as the "methodological core"; Step 2.6 Convergence Check with 🟢🟡🔴 | none found | n/a | n/a | not found. Source "inversion" means working from features back to behaviours; no worst-design step on either page (Discrepancy 2) |
| 11 | Behaviour taxonomy (✅ ⚠️ 🔴 🟣), Behavioral Cascade Model (week 1 to years), "10M users" scale test | none found | n/a | n/a | not found. Not on the pages read; the 10M figure is an illustrative scale with no source |
| 12 | Step 4.5 Rationalizations Check and common-rationalizations list | none found | n/a | n/a | not found. Not in the source; edbx addition |
| 13 | Redesign Directions (minimum 2 per 🔴) and Behavior Forecast Statement | none found | n/a | n/a | not found. Source method ends at consequences; no redesign step on either page |
| 14 | Evidence Ledger | edbx addition | n/a | n/a | not a source claim; SKILL.md itself labels it "a family convention from fdbx" |
| 15 | Hashtags #breakmydesign #evaluateoutcomes; See Also: Motivation Matrix, Design with Intent, Digital Ethics Compass | `chivukula2025universal` | to verify | (guess) Inverted Behavior Model | metadata only: book. Publisher pages show no contents; not confirmed that the method is in the book. "Design with Intent" appears on no page read. The microsite and toolkit pages carry no hashtags |
| 16 | Method is an evaluative, forecasting method from ethics-focused design research | `chivukula2022surveying` | abstract | 63 existing ethics-focused design methods | free copy: https://arxiv.org/abs/2102.08909 (landing page only; abstract does not name this method; whether the paper's tables include it is `to verify`) |

## Licence

- **Design Ethically toolkit pages (`zhou2026invertedbehavior`, `zhou2026toolkit`)**: licence unknown. Only a copyright line was found. Presume all rights reserved. Meaning for this repo: paraphrasing the four-step method in our own words is fine (methods and ideas are not copyrightable); do not reproduce the page text, the Facebook worksheet image or any template verbatim until the owner's terms are checked (contact via the site's Contact page). Shipping a modified version of the toolkit's own materials is not clearly allowed; this skill is an adaptation and should say so and credit Zhou.
- **UXP2 microsite page (`carlock2022inverted`)**: no licence found. It summarises Zhou's method; link to it, do not copy its text.
- **Fogg Behavior Model (`fogg2026behaviormodel`, `fogg2009behavior`)**: (c) BJ Fogg, no licence terms; ACM copyright for the paper. Citing B=MAP and describing the model in our own words is fine. Do not reproduce Fogg's diagrams or model graphics.
- **arXiv:2102.08909 (`chivukula2022surveying`)**: CC BY-NC-SA 4.0, as shown by the arXiv licence icon. The **NonCommercial** and **ShareAlike** terms would block commercial redistribution and require the same licence on adaptations if we copied text or tables from the paper into a paid bundle. We should only cite it, not copy from it. The paper's licence is not shown to cover the microsite or toolkit.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. Do not reproduce its text, hashtags or diagrams beyond a short citation.
- Nothing found forbids paraphrase. No source was found whose terms are open enough to permit verbatim reuse; the Design Ethically terms are the open question.

## Discrepancies

**Contradicted by the source** (pages read; they say otherwise):

1. **Misattributed or missing creator.** SKILL.md and `THIRD_PARTY_NOTICES.md` credit "BJ Fogg, Fogg Behavior Model". The method pages name Katherine M. (Kat) Zhou as the method designer and the Design Ethically toolkit as its home. Fogg's behaviour model is the basis, not the author of the Inverted model. Add Zhou and Design Ethically as the primary source.
2. **What "the inversion" is.** SKILL.md Step 2.5 calls the Worst Possible Design the "methodological core" and says skipping Step 2.6 "reduces the skill to a generic behavior-forecast exercise". On the source pages the inversion is the reverse-engineering flow itself (features, motivations, behaviours, consequences) and contains no worst-design or convergence step. The Overview of SKILL.md describes the inversion correctly; the Step 2.5/2.6 claims about what makes the method "Inverted" contradict it.
3. **Omitted source steps.** The toolkit page has six steps; steps 5 and 6 (estimate the ability needed for each behaviour, rank by likelihood, optionally by severity) are absent from SKILL.md. The four-step page on the UXP2 microsite stops at consequences, so SKILL.md matches that shorter version only.

**Not found in a readable source** (could not read the full source or the source is silent):

4. **Additions presented as the method.** Step 0 (stakeholder map), Steps 2.5, 2.6, 4.5, the behaviour taxonomy, the Behavioral Cascade Model, the "10M users" scale test, the Redesign Directions with metric and resistance notes, the Behavior Forecast Statement and the quality-bar items built on them appear on neither method page. Only the Evidence Ledger is labelled as an edbx adaptation. Image content (the Facebook worksheet) and the downloadable materials were not read, so a step shown only in an image cannot be ruled out.
5. **Five motivating-factor categories** (intrinsic, social, extrinsic, emotional, habitual) have no source on the pages read. SKILL.md says "Use the Fogg Behavior Model framework" for them; Fogg's own motivators were not read on `fogg2026behaviormodel` or in the 2009 paper (paywalled).
6. **Hashtags and See Also** (#breakmydesign #evaluateoutcomes; Design with Intent; Digital Ethics Compass) could not be tied to any page read; the book's contents are not visible on publisher pages.
7. **Formula notation.** SKILL.md writes "B = Motivation + Ability + Prompt". Fogg's page says the three "come together at the same moment" and writes B=MAP; no "+" appears. Whether the 2009 paper used "Trigger" instead of "Prompt" was not confirmed (paywalled).

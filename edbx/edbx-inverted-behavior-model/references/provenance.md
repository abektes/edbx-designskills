# Provenance — edbx-inverted-behavior-model

Stage B (checked against the page text in `papers/pages/`). One row per
element the skill attributes to a source. Where the source is a manifest key,
Locator and Anchor point at text read in this pass; `not in source` marks an
element the text does not contain (a confirmed discrepancy). Rows whose source
has no extracted text say `metadata only` in the Note.

Key finding: the method is the **Inverted Behavior Model of the Design Ethically
toolkit**, made by Kat Zhou, which inverts BJ Fogg's Behavior Model to forecast
unintended behaviours. The page (`zhou2026invertedbehavior`, one page of prose
and a Facebook worksheet image) and the survey paper's reference list
(`chivukula2021surveying`, p. 32) both attribute it to Zhou. SKILL.md and
`THIRD_PARTY_NOTICES.md` credit only "BJ Fogg, Fogg Behavior Model (B = MAP)"
and never name Zhou or Design Ethically. The page describes a short flow
(prompts, motivating factors, behaviours, consequences, plus optional ability
ranking). Most of what SKILL.md presents as the method (Step 0, the
worst-design artifact, the convergence check, the cascade model, the
rationalizations check) is not on that page. The worksheet image was not read
(text extraction only).

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `zhou2026invertedbehavior` | Zhou, K. ("Kat"). *BJ Fogg's Inverted Behavior Model.* Design Ethically (toolkit page, footer dated 2026). | https://www.designethically.com/bj-fogg | yes, web page (text in `papers/pages/zhou2026invertedbehavior/001.txt`) | unknown: the page text ends "(c) Copyright Design Ethically 2026. Made with ... by Kat"; no licence statement. Presume all rights reserved |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. and Gray, C. M. (2021, rev. 2022). Surveying the landscape of ethics-focused design methods. arXiv:2102.08909. | https://arxiv.org/abs/2102.08909 | yes, PDF text in `papers/pages/chivukula2021surveying/` | the manifest says CC BY-NC-SA 4.0, but the PDF text carries no CC notice; p. 1 gives an ACM-style permission notice (personal or classroom use without fee, not for profit or commercial advantage; "contact the owner/author(s)" for other uses). See Licence |
| `zhou2026toolkit` | Zhou, K. *Design Ethically Toolkit* (index of methods). | https://www.designethically.com/toolkit | not in manifest, no text | metadata only; unknown |
| `carlock2022inverted` | Carlock, T. (2022). *Inverted Behavior Model.* Improving Everyday Ethics (UXP2 Lab, Purdue). | https://everydayethics.uxp2.com/methods/inverted-behavior-model/ | not in manifest, no text | metadata only; unknown |
| `fogg2026behaviormodel` | Fogg, B. J. *Fogg Behavior Model* (B=MAP). | https://www.behaviormodel.org/ | not in manifest, no text | metadata only; (c) BJ Fogg, no licence terms |
| `fogg2009behavior` | Fogg, B. J. (2009). A behavior model for persuasive design. *Persuasive Technology.* ACM. | doi:10.1145/1541948.1541999 | no | ACM copyright; paywalled |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design.* Rockport (Quarto). | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved; book |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: a forecasting model that predicts behaviours a product's prompts lead to, and the consequences of those behaviours | `zhou2026invertedbehavior` | web | predict any unknown or unintended behaviors | found. The page is by Kat Zhou (footer) and is titled "BJ Fogg's Inverted Behavior Model"; SKILL.md credits Fogg only (Discrepancy 1). The "evaluative model for teams" wording of stage A came from a page not in the manifest and is not used |
| 2 | The inversion of Fogg's model: forecast behaviour instead of designing for an intended one | `zhou2026invertedbehavior` | web | invert it so instead of trying to design | found. The page defines the inversion exactly this way; the Overview of SKILL.md matches. Fogg's own page is not in the manifest |
| 3 | Fogg Behavior Model: behaviour happens when Motivation, Ability and a Prompt come together | `zhou2026invertedbehavior` | web | Ability (A), and a Prompt (P) come together | found, as a quotation of Fogg on Zhou's page, with "at the same moment". The page writes B, M, A, P as letters and never writes a "+" formula; "B = Motivation + Ability + Prompt" is SKILL.md's notation (Discrepancy 6) |
| 4 | Earlier form of Fogg's model (2009 paper terminology) | `fogg2009behavior` | n/a | A behavior model for persuasive design | metadata only: paywalled. Not read; SKILL.md does not cite the paper, and the claim that the 2009 term was "Trigger" is model knowledge |
| 5 | Core flow: list the prompts (features); identify motivations for each; predict behaviours; analyse consequences (SKILL.md Steps 1 to 4) | `zhou2026invertedbehavior` | web | listing out the prompts for which you want to forecast | found. The page gives this order in one paragraph: prompts, motivating factors, predicted behaviours, then consequences. SKILL.md's order and meaning match |
| 6 | Source content SKILL.md omits: calculate the ability level for each behaviour and rank behaviours by likelihood, optionally by severity | `zhou2026invertedbehavior` | web | calculate the ability levels for those behaviors | found. The page offers this as an optional extra ("You can also"), in prose and not as numbered steps. No SKILL.md step uses ability or ranking, although Ability is the A in the model it invokes (Discrepancy 3) |
| 7 | Definition of a prompt as "any element that triggers a user action (notification, button, feed, score, streak, countdown)" | `zhou2026invertedbehavior` | not in source | These can be features or they can be holistic products | discrepancy confirmed against the text. The page says the things to forecast ("prompts") can be features or whole products; it gives no element list and no "triggers a user action" definition. SKILL.md Step 1 breaks a feature into element-level prompts, which is a different unit |
| 8 | Five motivating-factor categories (intrinsic, social, extrinsic, emotional, habitual) | `zhou2026invertedbehavior` | not in source | write out the motivating factors that might come into play | discrepancy confirmed against the text. The page says only to write out the motivating factors; it names no categories. SKILL.md attributes the framework to Fogg, whose own page is not in the manifest (Discrepancy 4) |
| 9 | Step 0 stakeholder map (six populations incl. bystanders, supply-chain workers, regulators, future-affected) | `zhou2026invertedbehavior` | not in source | try to analyze and see what consequences might result | discrepancy confirmed against the text. The page has no stakeholder step; consequences are analysed per behaviour. edbx addition presented as part of the method (Discrepancy 4) |
| 10 | Step 2.5 Worst Possible Design "inversion artifact", called the "methodological core"; Step 2.6 Convergence Check with traffic-light scores | `zhou2026invertedbehavior` | not in source | instead of trying to design for an intended behavior | discrepancy confirmed against the text. On the page, the inversion is predicting behaviour instead of designing for it; there is no worst-design or convergence step (Discrepancy 2) |
| 11 | Behaviour taxonomy (four tags), Behavioral Cascade Model (week 1 to years), "10M users" scale test | `zhou2026invertedbehavior` | not in source | forecast what consequences that behavior might trigger | discrepancy confirmed against the text. The page stops at consequences of predicted behaviours; no taxonomy, cascade or scale test. The 10M figure is an illustrative scale with no source |
| 12 | Step 4.5 Rationalizations Check and common-rationalizations list | `zhou2026invertedbehavior` | not in source | consequences might result from those behaviors | discrepancy confirmed against the text. Not on the page; edbx addition |
| 13 | Redesign Directions (minimum 2 per red finding) and Behavior Forecast Statement | `zhou2026invertedbehavior` | not in source | play with ranking by the severity of the behaviors | discrepancy confirmed against the text. The page ends with optional ranking by likelihood and severity; no redesign step or forecast statement |
| 14 | Evidence Ledger | edbx addition | n/a | Evidence Ledger family convention from fdbx | metadata only: edbx addition. SKILL.md itself labels it a family convention from fdbx |
| 15 | Hashtags #breakmydesign #evaluateoutcomes | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Contents not available; not confirmed that the method or these hashtags are in the book. The Design Ethically page carries no hashtags |
| 16 | See Also: Motivation Matrix and Design with Intent | `chivukula2021surveying` | p. 19 | Motivation Matrix [164],Inverted Model [158] | found. The survey's Table 3 lists Motivation Matrix and Inverted Model together in the same design phases, and Design with Intent as another method; none of this links them as See Also. Digital Ethics Compass is not in this paper |
| 17 | Method belongs to the ethics-focused design methods catalogued in research | `chivukula2021surveying` | p. 1 | collection of 63 existing ethics-focused methods | found. The abstract does not name this method; the catalogue does (p. 19, Table 3) |
| 18 | Attribution of the method to Kat Zhou and its web home | `chivukula2021surveying` | p. 32 | Kat Zhou. 2021. BJ Fogg's Inverted Behavior Model | found. The reference list attributes the method to Zhou, with the Design Ethically URL; confirms Discrepancy 1 from an independent source |

## Licence

- **Design Ethically page (`zhou2026invertedbehavior`)**: licence unknown. Only a copyright line was found in the page text. Presume all rights reserved. Paraphrasing the method in our own words is fine; do not reproduce the page text, the Facebook worksheet image or any template verbatim. This skill is an adaptation and should say so and credit Zhou.
- **Survey paper (`chivukula2021surveying`)**: the manifest labels it CC BY-NC-SA 4.0, but the PDF text shows no CC notice. Page 1 has an ACM-style permission notice instead: copies for personal or classroom use are free if not made for profit or commercial advantage and the notice and citation are kept; "for all other uses, contact the owner/author(s)". Treat it as cite-only: do not copy text or tables into a paid bundle. The paper's terms do not cover the Design Ethically page.
- **Fogg (`fogg2009behavior`, Fogg's site)**: (c) BJ Fogg / ACM copyright. Citing B=MAP and describing it in our own words is fine; do not reproduce his diagrams. Neither was readable here.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. Cite only.
- Nothing found forbids paraphrase. No source was found whose terms permit verbatim reuse.

## Discrepancies

**Contradicted by the source text** (read on the page; the page says otherwise or is silent where SKILL.md asserts):

1. **Misattributed or missing creator.** SKILL.md and `THIRD_PARTY_NOTICES.md` credit "BJ Fogg, Fogg Behavior Model". The Design Ethically page is by Kat Zhou, and the survey's reference list (p. 32) credits "Kat Zhou" with this method. Fogg's model is the basis, not the author of the Inverted model. Add Zhou and Design Ethically as the primary source. (fixed in SKILL.md; tutorial corrected in this pass)
2. **What "the inversion" is.** SKILL.md Step 2.5 calls the Worst Possible Design the "methodological core" and says skipping Step 2.6 "reduces the skill to a generic behavior-forecast exercise". On the source page the inversion is using Fogg's formula to predict behaviours instead of designing for an intended one; there is no worst-design or convergence step. The Overview of SKILL.md describes the inversion correctly; the Step 2.5/2.6 claims about what makes the method "Inverted" contradict the page. (fixed in SKILL.md)
3. **Omitted source content.** The page's optional pass (estimate the ability level of each behaviour; rank by likelihood or by severity) is absent from SKILL.md. (fixed in SKILL.md)
4. **Additions presented as the method, not on the page.** Step 0 (stakeholder map), the element-level prompt definition and example list, the five motivating-factor categories, Steps 2.5, 2.6, 4.5, the behaviour taxonomy, the Behavioral Cascade Model, the Redesign Directions and the Behavior Forecast Statement (rows 7 to 13). Only the Evidence Ledger is labelled as an edbx adaptation. The Facebook worksheet image was not read, so a step shown only there cannot be ruled out. (fixed in SKILL.md)

**Not verifiable** (no readable source):

5. **Hashtags and See Also links** (#breakmydesign #evaluateoutcomes; the book contents; Digital Ethics Compass) tie to no readable page. The survey lists Design with Intent and Motivation Matrix only as separate methods.
6. **Formula notation and terminology.** The page quotes Fogg with letters M, A, P and no "+"; whether his own site or the 2009 paper used "Prompt" or "Trigger" cannot be checked here (his site is not in the manifest; the paper is paywalled).
7. **Stage-A claims from pages outside the manifest** (the UXP2 microsite's four steps and "method designed by" line, the toolkit index) are unverified here.

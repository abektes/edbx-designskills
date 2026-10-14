# Provenance — edbx-motivation-matrix

Stage B (checked against the page text in `papers/pages/`). One row per
element the skill attributes to a source. Where the source is a manifest key,
Locator and Anchor point at text read in this pass; `not in source` marks an
element the text does not contain (a confirmed discrepancy). Rows whose source
has no extracted text say `metadata only` in the Note.

Key finding: the method is the **Motivation Matrix of the Design Ethically
toolkit**, made by Kat Zhou. It has **six** motivating factors (incentive,
achievement, social acceptance, fear, power, growth), not five. The page
(`zhou2026motivationmatrix`) and the survey paper's reference list
(`chivukula2021surveying`, p. 32) both credit Kat Zhou. SKILL.md (and
`THIRD_PARTY_NOTICES.md`, `tutorials/motivation-matrix.md`) instead credit
"Annabelle Zhu, adapted by Cordelia Nodders" and cite a 2020 book by Zhu and a
2020 chapter by Nodders in *Universal Methods of Ethical Design*; no readable
source supports either person or either citation. The page is a predictive
exercise (statements that predict how a user might interact with a product);
the ethical-audit framing, the cell template, the three lenses and the flags
are not on it. The AngelList worksheet image was not read (text extraction
only).

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `zhou2026motivationmatrix` | Zhou, K. ("Kat"). *Motivation Matrix.* Design Ethically (toolkit page, footer dated 2026). | https://www.designethically.com/motivation-matrix | yes, web page (text in `papers/pages/zhou2026motivationmatrix/001.txt`) | unknown: the page text ends "(c) Copyright Design Ethically 2026. Made with ... by Kat"; no licence statement. Presume all rights reserved |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. and Gray, C. M. (2021, rev. 2022). Surveying the landscape of ethics-focused design methods. arXiv:2102.08909. | https://arxiv.org/abs/2102.08909 | yes, PDF text in `papers/pages/chivukula2021surveying/` | the manifest says CC BY-NC-SA 4.0, but the PDF text carries no CC notice; p. 1 gives an ACM-style permission notice (personal or classroom use without fee, not for profit or commercial advantage; contact the owner/author(s) for other uses). See Licence |
| `zhou2026toolkit` | Zhou, K. *Design Ethically Toolkit* (index of methods). | https://www.designethically.com/toolkit | not in manifest, no text | metadata only; unknown |
| `carlock2022motivation` | Carlock, T. (2022). *Motivation Matrix.* Improving Everyday Ethics (UXP2 Lab, Purdue). | https://everydayethics.uxp2.com/methods/motivation-matrix/ | not in manifest, no text | metadata only; unknown |
| `ho2020lifehack` | Ho, L. *Types of motivation* (Lifehack), which stage A said the toolkit cites for the six types. | https://www.lifehack.org/articles/productivity/6-types-of-motivation-explained.html | not in manifest, no text | metadata only; publisher copyright |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design.* Rockport (Quarto). | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved; book |
| `zhu2020drivenmotivation` | "Zhu, A. (2020). *Design Driven by Motivation.* design4good.com/book", as cited in SKILL.md. | design4good.com/book | no source found | unknown |
| `nodders2020motivation` | "Nodders, C. (2020). 'Motivation Matrix.' In *Universal Methods of Ethical Design*", as cited in SKILL.md. | n/a | no source found | unknown |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: Motivation Matrix, relating motivating factors to users in contexts to predict their interaction with a product | `zhou2026motivationmatrix` | web | predict how a user might interact with the product | found. The page is by Kat Zhou (footer); SKILL.md names Annabelle Zhu and Cordelia Nodders (Discrepancy 1) |
| 2 | Purpose: understand why people act, to anticipate use in different contexts | `zhou2026motivationmatrix` | web | People perform actions because they are triggered by motivations | found. The source goal is prediction. SKILL.md's Overview frames it as an audit of how a product exploits or manipulates motivations ("deliberately provocative"); no such framing is on the page (row 11) |
| 3 | Five motivation types: Achievement, Social Acceptance, Fear, Power, Incentive | `zhou2026motivationmatrix` | web | incentive, achievement, social acceptance, fear, power, and growth | found, with a difference: the page lists six core types; **growth** (intrinsic motivation to become a better version of oneself) is missing from SKILL.md (Discrepancy 2) |
| 4 | Where the six types come from (stage A: the toolkit cites a Lifehack article) | `zhou2026motivationmatrix` | not in source | can be distilled into six core types | discrepancy confirmed against the text. The extracted text names no origin article for the types; the stage-A Lifehack link was not in the text (it may have been in markup, which was not checked). SKILL.md makes no Lifehack claim |
| 5 | Type definitions in the Five Motivation Types table (core drive and design examples such as progress bars, likes, countdowns, leaderboards, discounts) | `zhou2026motivationmatrix` | web | any type of reward-oriented motivating factor | found for the definitions, which are one line each (incentive: reward, monetary or not; achievement: drive for competency; social acceptance: need to belong and not be ostracized; fear: avoiding outcomes; power: autonomy or control over others). SKILL.md's "core drive" wording and every design example are its own |
| 6 | Grid of motivation types against users in contexts | `zhou2026motivationmatrix` | web | relates these motivating factors with various users of a product | found. The page's advice on the number of contexts is not in the text; SKILL.md's "at least two, suggest a third" is unsupported by the page |
| 7 | Formula "MOTIVATION TYPE x USE @ CONTEXT = MOTIVATION MATRIX" | `zhou2026motivationmatrix` | not in source | various users of a product in different contexts | discrepancy confirmed against the text. No formula on the page; the matrix is described in prose |
| 8 | Cell format "[Motivation] + [Action]" where the Action is what the design does to the user's motivation | `zhou2026motivationmatrix` | not in source | the potential actions that the user could take | discrepancy confirmed against the text. On the page, a yellow sticky in each cell holds the actions the user could take given the motivation; SKILL.md's Action is the design's action on the user, a different thing (Discrepancy 3) |
| 9 | Source guidance SKILL.md omits: run it after empathy mapping, with sponsor users | `zhou2026motivationmatrix` | web | doing this exercise after empathy mapping | found. Not in SKILL.md; its Integration section sequences other skills instead (Discrepancy 5) |
| 10 | Source materials SKILL.md omits: pink notes for insights on a motivation, yellow notes for user actions | `zhou2026motivationmatrix` | web | we used pink to represent any insights | found. Not in SKILL.md (Discrepancy 5) |
| 11 | Three ethical-analysis lenses (manipulative patterns, underrepresented users, secondary-user consequences) | `zhou2026motivationmatrix` | not in source | statements that predict how a user might interact | discrepancy confirmed against the text. The page ends at predicted interactions; edbx addition presented as Step 3 of the method |
| 12 | Green / yellow / red flags (Ethical, Monitor, Manipulative) and the criteria in `references/ethical-flags.md` | `zhou2026motivationmatrix` | not in source | wanting to avoid certain outcomes or consequences | discrepancy confirmed against the text. No rating scheme on the page; the reference file names no source |
| 13 | Ethical Risk Summary, Redesign Directions, Missing Contexts deliverables | `zhou2026motivationmatrix` | not in source | Motivation Matrix applied to AngelList | discrepancy confirmed against the text. The page has only a worked-example caption; the source method ends at predicted actions |
| 14 | Named effect: overjustification effect (rewards shift intrinsic motivation to extrinsic) | none cited | n/a | overjustification effect rewards shift intrinsic motivation | metadata only: no source found. A psychology concept used without a citation; model knowledge |
| 15 | Attribution "Annabelle Zhu, adapted by Cordelia Nodders; published in Universal Methods of Ethical Design" (THIRD_PARTY_NOTICES, tutorial) | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Contents not available, so the method's presence in the book, and the names Zhu and Nodders, are not confirmed. See row 18 for what the survey says about the author |
| 16 | Further Reading "Zhu, A. (2020). Design Driven by Motivation. design4good.com/book" | `zhu2020drivenmotivation` | n/a | Design Driven by Motivation | metadata only: no source found. Nothing matching was located in stage A; not in the manifest |
| 17 | Further Reading "Nodders, C. (2020). Motivation Matrix. In Universal Methods of Ethical Design" | `nodders2020motivation` | n/a | Nodders Motivation Matrix Universal Methods of Ethical Design | metadata only: no source found. The book is dated 2025 per stage A (publisher page, not in the manifest), so a 2020 chapter date is doubtful; unconfirmed |
| 18 | Authorship of the method and where it sits among ethics-focused methods | `chivukula2021surveying` | p. 32 | Kat Zhou. 2021. Motivation Matrix | found. The survey's reference list credits Kat Zhou with the method and the Design Ethically URL; independent confirmation of Discrepancy 1. Table 3 on p. 19 lists the method in design phases 1 and 2 |
| 19 | Method is one of the ethics-focused design methods catalogued in research | `chivukula2021surveying` | p. 19 | Motivation Matrix [164],Inverted Model [158] | found. Listed with the Inverted Model, also by Zhou, in the planning phase of Table 3 |
| 20 | Evidence Ledger | edbx addition | n/a | Evidence Ledger family convention from fdbx | metadata only: edbx addition. SKILL.md itself labels it a family convention from fdbx |

## Licence

- **Design Ethically page (`zhou2026motivationmatrix`)**: licence unknown. Only a copyright line was found in the page text. Presume all rights reserved. Paraphrasing the method is fine; do not reproduce the page text, the AngelList example or any worksheet verbatim. This skill is an adaptation and should say so and credit Zhou.
- **Survey paper (`chivukula2021surveying`)**: the manifest labels it CC BY-NC-SA 4.0, but the PDF text shows no CC notice. Page 1 has an ACM-style permission notice instead: copies for personal or classroom use are free if not made for profit or commercial advantage; "for all other uses, contact the owner/author(s)". Treat as cite-only: do not copy text or tables into a paid bundle.
- **Lifehack article and UXP2 microsite**: not in the manifest; terms unchecked. Link only.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. Cite only.
- **`zhu2020drivenmotivation` / `nodders2020motivation`**: no source found; licence unknown. Do not ship these citations until located.
- Nothing found forbids paraphrase. The Design Ethically terms are the open question.

## Discrepancies

**Contradicted by the source text** (read on the page; the page says otherwise or is silent where SKILL.md asserts):

1. **Wrong creator.** SKILL.md (Further Reading), `THIRD_PARTY_NOTICES.md` and `tutorials/motivation-matrix.md` credit "Annabelle Zhu", adapted by "Cordelia Nodders". The Design Ethically page is by Kat Zhou, and the survey (p. 32) credits "Kat Zhou" with the method. Replace the credit. (fixed in SKILL.md)
2. **Five types instead of six.** SKILL.md has five motivation types and says "five core user motivations". The page has six; **growth** is missing. The 5-row grid, the template, reference files and tutorial repeat the five. (fixed in SKILL.md)
3. **Cell template.** The "[Motivation] + [Action]" statement, in which the Action is what the design does to the user, and the formula "MOTIVATION TYPE x USE @ CONTEXT" are not on the page. The page's cells hold insight notes and notes on the actions the user could take. (fixed in SKILL.md)
4. **Ethical-analysis machinery.** The audit and manipulation framing, the three lenses, the three flags and their criteria, the Ethical Risk Summary, Redesign Directions and Missing Contexts are not on the page. The worksheet image was not read, so a step shown only there cannot be ruled out. (fixed in SKILL.md)
5. **Omitted source guidance.** The page recommends running the exercise after empathy mapping with sponsor users and describes pink (insight) and yellow (action) notes; SKILL.md omits both. (fixed in SKILL.md)

**Not verifiable** (no readable source):

6. **"Design Driven by Motivation" (Zhu, 2020)** and **Nodders (2020), "Motivation Matrix" in the book**: no source found; the year 2020 for a chapter in a book dated 2025 is doubtful. Whether the book contains the method is unconfirmed.
7. **Origin of the six types.** The page text names none; the stage-A Lifehack lead is unverified here.
8. **Overjustification effect**: used without a citation (model knowledge).
9. **Number of contexts** ("at least two, suggest a third"): stage A found this on the UXP2 microsite (not in the manifest); not on the Design Ethically page.

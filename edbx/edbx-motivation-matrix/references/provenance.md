# Provenance — edbx-motivation-matrix

Stage A draft (sources and licences, no downloads). One row per element the
skill attributes to a source. Locator and anchor are what could be confirmed
from pages read in this pass; otherwise Locator is `to verify` and the anchor
is marked `(guess)`. Stage B checks each anchor on the page.

Key finding: the method is the **Motivation Matrix of the Design Ethically
toolkit**, made by Kat (Katherine M.) Zhou. It has **six** motivating factors
(Incentive, Achievement, Social Acceptance, Fear, Power, Growth), not five.
SKILL.md (and `THIRD_PARTY_NOTICES.md`, `tutorials/motivation-matrix.md`)
instead credit "Annabelle Zhu, adapted by Cordelia Nodders" and cite two
works, a 2020 book by Zhu and a 2020 chapter by Nodders in *Universal Methods
of Ethical Design*. No page read supports either person or either citation;
the book is dated 2025. The matrix cells, the three-lens ethical analysis and
the 🟢🟡🔴 flags are not in the source.

Pages were read through a fetch tool that summarises each page, so quoted
anchors are as reported by that tool. The example worksheet image (AngelList)
was not read.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `zhou2026motivationmatrix` | Zhou, K. M. ("Kat"). *Motivation Matrix.* Design Ethically (toolkit page, footer dated 2026; first-publication date not shown). Credits: "Created by Kat (Katherine M. Zhou)". | https://www.designethically.com/motivation-matrix | yes, it is a web page | unknown: footer "(c) 2026 Design Ethically"; no licence statement. Presume all rights reserved. Check by contacting the site owner |
| `zhou2026toolkit` | Zhou, K. M. *Design Ethically Toolkit* index; lists Motivation Matrix under "Forecasting" (1 hour, small group). | https://www.designethically.com/toolkit | yes, web page | unknown: same copyright line; says nothing on reuse |
| `carlock2022motivation` | Carlock, T. (10 Apr 2022). *Motivation Matrix.* Improving Everyday Ethics (UXP2 Lab, Purdue). "Method designed by: Katherine M. Zhou"; steps attributed to the Design Ethically website. | https://everydayethics.uxp2.com/methods/motivation-matrix/ (also https://everydayethics.uxp2.com/?p=968) | yes, web page | unknown: no licence or copyright statement for the content |
| `ho2020lifehack` | Ho, L. *Types of motivation* article on Lifehack, cited by Design Ethically as the source of the six types (URL slug "6-types-of-motivation-explained"). The live page now has the title "9 Types of Motivation to Make Your Goals Happen" and lists seven subtypes. Publication date not shown. | https://www.lifehack.org/articles/productivity/6-types-of-motivation-explained.html | yes, web page | unknown: publisher copyright, not checked |
| `chivukula2022surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. and Gray, C. M. (2021, rev. 2022). Surveying the landscape of ethics-focused design methods. arXiv:2102.08909. The preprint the microsite says it is "based off of". | https://arxiv.org/abs/2102.08909 (doi:10.48550/arXiv.2102.08909) | yes: arXiv, open access (landing page only; PDF not fetched) | CC BY-NC-SA 4.0, per the licence icon on the arXiv page (the paper's licence, not necessarily the microsite's or toolkit's) |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design.* Rockport Publishers (Quarto). ISBN 9780760393086. Only the two authors are named on the publisher page. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved, paywalled book |
| `zhu2020drivenmotivation` | "Zhu, A. (2020). *Design Driven by Motivation.* design4good.com/book", as cited in SKILL.md "Further Reading". | design4good.com/book (not opened) | no | unknown |
| `nodders2020motivation` | "Nodders, C. (2020). 'Motivation Matrix.' In *Universal Methods of Ethical Design*", as cited in SKILL.md. | n/a | no | unknown |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: Motivation Matrix, a framework for predicting how users might interact with a product in a given context | `zhou2026motivationmatrix` | description | predicting how users might interact | toolkit page. Creator is Katherine M. Zhou; SKILL.md names Annabelle Zhu and Cordelia Nodders (Discrepancy 1) |
| 2 | Purpose: help teams understand users' different motivating factors to anticipate use in different contexts | `carlock2022motivation` | description | users' different motivating factors | toolkit page. Matches SKILL.md's Overview in spirit; the source's goal is prediction, not an "ethical audit" |
| 3 | Five motivation types: Achievement, Social Acceptance, Fear, Power, Incentive | `zhou2026motivationmatrix` | core idea | Incentive, Achievement, Social Acceptance, Fear, Power, Growth | toolkit page. The source lists six; **Growth** (intrinsic drive to become a better version of oneself) is missing from SKILL.md. Same six on `carlock2022motivation` step 1 (Discrepancy 2) |
| 4 | Where the six types come from | `ho2020lifehack` | to verify | (guess) types of motivation explained | toolkit page names it as the origin. The live Lifehack page lists intrinsic competence and attitude plus extrinsic reward, fear, achievement, power and affiliation, so the six names do not map one to one (Discrepancy 6) |
| 5 | Type definitions and design examples in the Five Motivation Types table (progress bars, likes, countdowns, leaderboards, discounts) | `zhou2026motivationmatrix` | core idea | Rewards, which may or may not be monetary | toolkit page. Source gives one-line definitions only (e.g. Incentive: rewards; Power: autonomy or control over others). The design examples and "core drive" column are SKILL.md's |
| 6 | Grid of user contexts by motivation types; at least two contexts (suggest a third) | `carlock2022motivation` | step 1 | matrix of 2-3 user contexts | toolkit page. Source: 2-3 user contexts each crossed with the factors. SKILL.md's "at least two, suggest a third" is consistent |
| 7 | Formula "MOTIVATION TYPE x USE @ CONTEXT = MOTIVATION MATRIX" | none found | n/a | n/a | not found. No formula on any page read. Searched: Motivation Matrix formula motivation type use context |
| 8 | Cell format "[Motivation] + [Action]" statement describing what the design does to the user's motivation | `carlock2022motivation` | steps 2-3 | write how different behaviors could develop | toolkit page. Source asks for a sticky note on the context in which each factor takes form, and a note on behaviours that could develop. The "[Motivation] + [Action]" template is SKILL.md's, and its Action describes the design rather than the user's behaviour (Discrepancy 4) |
| 9 | Source steps and materials SKILL.md omits: run it after empathy mapping with sponsor users; pink notes for motivation insights and yellow for user actions that follow | `zhou2026motivationmatrix` | steps 3-4 | after empathy mapping | toolkit page. Not in SKILL.md; its Integration section names other skills instead (Discrepancy 5) |
| 10 | Three ethical-analysis lenses (manipulative patterns, underrepresented users, secondary-user consequences) | none found | n/a | n/a | not found. Not on any page read; edbx addition presented as Step 3 of the method |
| 11 | 🟢 Ethical / 🟡 Monitor / 🔴 Manipulative flags and the flagging criteria in `references/ethical-flags.md` | none found | n/a | n/a | not found. Not on any page read; the reference file names no source |
| 12 | Ethical Risk Summary, Redesign Directions, Missing Contexts deliverables | none found | n/a | n/a | not found. Edbx output structure; source method ends at predicted behaviours |
| 13 | Named effects: overjustification effect (rewards shift intrinsic motivation to extrinsic) | none cited | to verify | (guess) overjustification effect | metadata only: not read. Psychology concept used without a citation; model knowledge. Source for it would be the original studies, not checked |
| 14 | Attribution "Annabelle Zhu, adapted by Cordelia Nodders; published in Universal Methods of Ethical Design" (THIRD_PARTY_NOTICES, tutorial) and Further Reading "Nodders, C. (2020)" | `chivukula2025universal` | to verify | (guess) Motivation Matrix | metadata only: book. Publisher pages show no contents and list only Chivukula and Gray as contributors; no page read mentions Nodders. The book is dated 2025, so "2020" is wrong for it |
| 15 | Further Reading "Zhu, A. (2020). Design Driven by Motivation. design4good.com/book" | `zhu2020drivenmotivation` | n/a | n/a | not found. Search terms tried: "Design Driven by Motivation" Zhu design4good; Zhu "Design Driven by Motivation" book 2020. Nothing matching; design4good.com/book not opened |
| 16 | Evidence Ledger | edbx addition | n/a | n/a | not a source claim; SKILL.md labels it "a family convention from fdbx" |
| 17 | Method is one of the ethics-focused design methods surveyed by the research group behind the microsite | `chivukula2022surveying` | abstract | 63 existing ethics-focused design methods | free copy: https://arxiv.org/abs/2102.08909 (landing page only; abstract does not name this method; whether the paper lists it is `to verify`) |

## Licence

- **Design Ethically toolkit pages (`zhou2026motivationmatrix`, `zhou2026toolkit`)**: licence unknown. Only a copyright line was found; presume all rights reserved. Meaning for this repo: paraphrasing the method (a grid of motivating factors by user context, with predicted behaviours) is fine. Do not reproduce the page text, the AngelList example or any worksheet verbatim until the owner's terms are checked (the site has a Contact page). Shipping a modified version of the toolkit's own materials is not clearly allowed; this skill is an adaptation and should say so and credit Zhou.
- **UXP2 microsite page (`carlock2022motivation`)**: no licence found. Link to it, do not copy its text.
- **Lifehack article (`ho2020lifehack`)**: publisher copyright, terms not checked. Cite only.
- **arXiv:2102.08909 (`chivukula2022surveying`)**: CC BY-NC-SA 4.0 per the icon on the arXiv page. **NonCommercial** and **ShareAlike** would block copying its text or tables into a paid bundle (and require the same licence on adaptations). Cite only. Its licence is not shown to cover the microsite or toolkit.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. Do not reproduce its text, hashtags or diagrams beyond a short citation.
- **`zhu2020drivenmotivation` / `nodders2020motivation`**: could not be found; licence unknown. Do not ship these citations until located.
- Nothing found forbids paraphrase. The Design Ethically terms are the open question.

## Discrepancies

**Contradicted by the source** (pages read; they say otherwise):

1. **Wrong creator.** SKILL.md (Further Reading), `THIRD_PARTY_NOTICES.md` and `tutorials/motivation-matrix.md` credit "Annabelle Zhu", adapted by "Cordelia Nodders". Both method pages name Katherine M. (Kat) Zhou, creator of Design Ethically. Replace the credit; "Annabelle", "Cordelia Nodders" and the "adapted" step have no support.
2. **Five types instead of six.** SKILL.md has five motivation types (Achievement, Social Acceptance, Fear, Power, Incentive) and says "five core user motivations". The source has six; **Growth** is missing. The grid is 5 rows in SKILL.md but 6 in the source, and the template, reference files and tutorial repeat the five.
3. **Citation year and venue.** SKILL.md gives "Nodders, C. (2020). 'Motivation Matrix.' In *Universal Methods of Ethical Design*". The book is dated 1 April 2025 and the publisher page names only Chivukula and Gray as authors, so a 2020 date for a chapter in it is wrong, and the chapter's author is not confirmed.

**Not found in a readable source** (could not read the full source or the source is silent):

4. **Cell template.** The source asks for notes on the context in which each motivating factor takes form and on the behaviours that follow. The "[Motivation] + [Action]" format, in which the Action is what the design does to the user, and the formula "MOTIVATION TYPE x USE @ CONTEXT" appear on no page read. The microsite's example worksheet (image) was not read, so the formula cannot be ruled out.
5. **Ethical-analysis machinery.** The three lenses, the 🟢🟡🔴 flags and their criteria, the Ethical Risk Summary and Redesign Directions are not in either method page. Also, the source says to run the exercise after empathy mapping and to use pink and yellow notes; SKILL.md omits both, and instead sequences other skills (worrystorming, anotherlens).
6. **Origin of the six types.** The toolkit page cites a Lifehack article. The live Lifehack page lists different categories (competence, attitude, reward, fear, achievement, power, affiliation), so "Social Acceptance" and "Growth" cannot be matched to it by name. The source's own derivation is unverified, not SKILL.md's.
7. **"Design Driven by Motivation" (Zhu, 2020, design4good.com/book)** was not found in two searches; the URL was not opened. The book's table of contents is not visible on publisher pages, so the claim that Motivation Matrix is in *Universal Methods of Ethical Design* is unconfirmed (a lead for stage B: a search-result summary suggested the book lists "Nodder's 7 Deadly Sins", which may be where "Nodder" came from; not confirmed on any page).

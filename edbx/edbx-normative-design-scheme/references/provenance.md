# Provenance — edbx-normative-design-scheme

Stage B (checked against the page text in `papers/pages/`). One row per
element the skill attributes to a source. Where the source is a manifest key,
Locator and Anchor point at text read in this pass; `not in source` marks an
element the text does not contain (a confirmed discrepancy). Rows whose source
has no extracted text say `metadata only` in the Note.

Key finding: the method is the **Normative Design Scheme worksheet of the
Ethics for Designers toolkit** by Jet Gispen (c) 2017. The tool page
(`gispen2017normative`) describes a downloadable template with four steps
(browse, write a design goal, assess it with the three main domains of
normative ethics, generate ideas), 30 to 60 minutes, post-its and pens. The
survey paper (`chivukula2021surveying`, p. 14) confirms that the worksheet
refers to virtue, consequentialist and deontological ethics, and its reference
list (p. 28) credits Gispen. The template itself is not in the manifest, so
its questions are unread: SKILL.md's Intention / Effect / Design mapping and
its lens questions cannot be confirmed. SKILL.md credits no creator and
`THIRD_PARTY_NOTICES.md` credits only "Consequentialist, deontological and
virtue ethics". Everything from Step 0 to the Normative Design Statement is
absent from the page text.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `gispen2017normative` | Gispen, J. (2017). *Normative design scheme.* Ethics for Designers toolkit (tool page; offers a "Download template" link). | https://www.ethicsfordesigners.com/normative-design-scheme | yes, web page text in `papers/pages/gispen2017normative/001.txt`; the template file itself is not in the manifest | unknown: the page text ends "(c) Jet Gispen 2017"; no licence, reuse or sharing terms. Presume all rights reserved |
| `chivukula2021surveying` | Chivukula, S. S., Li, Z., Pivonka, A. C., Chen, J. and Gray, C. M. (2021, rev. 2022). Surveying the landscape of ethics-focused design methods. arXiv:2102.08909. | https://arxiv.org/abs/2102.08909 | yes, PDF text in `papers/pages/chivukula2021surveying/` | the manifest says CC BY-NC-SA 4.0, but the PDF text carries no CC notice; p. 1 gives an ACM-style permission notice (personal or classroom use without fee, not for profit or commercial advantage; contact the owner/author(s) for other uses). See Licence |
| `gispen2017template` | The downloadable Normative Design Scheme template (questions per ethical view). | linked from the tool page | not in manifest, not read | metadata only; unknown |
| `carlock2021normative` | Carlock, T. (2021). *Normative Design Scheme.* Improving Everyday Ethics (UXP2 Lab, Purdue). | https://everydayethics.uxp2.com/methods/normative-design-scheme/ | not in manifest, no text | metadata only; unknown |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design.* Rockport (Quarto). | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved; book |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | The method itself: a worksheet to formulate a design goal and assess and improve it with normative ethics | `gispen2017normative` | web | Formulate your design goal, using the structure provided | found. The page is by Jet Gispen (footer); SKILL.md names no creator (Discrepancy 1). It is a template download, a worksheet used with post-its |
| 2 | The tool introduces the most commonly known theories of normative ethics to make ethics less overwhelming for designers | `gispen2017normative` | web | introduces you to the most commonly known theories | found. Consistent with SKILL.md's Overview |
| 3 | Three theories used as lenses: Virtue Ethics, Consequentialism, Deontology | `chivukula2021surveying` | p. 14 | explicit references to virtue, consequentialist, and deontological ethics | found. The survey says the worksheet has spaces to assess design goals with these three paradigms. The tool page itself only says "3 main domains of normative ethics" and does not name them |
| 4 | Mapping: Intention = Virtue Ethics, Effect = Consequentialism, Design = Deontology | `gispen2017normative` | not in source | using the three main normative views as described on the template | discrepancy confirmed against the text. Neither the tool page nor the survey gives this mapping; the page says the views are described on the template, which was not read (Discrepancy 3) |
| 5 | Flow: write the design goal in the template's format; assess it with the three views; use the theories to improve the design as ideation questions | `gispen2017normative` | web | Use the specific normative theories to morally improve your design | found. Matches SKILL.md's Assess and Generate content, but the page runs them as one sequence of steps, not two modes (Discrepancy 4) |
| 6 | "There is no absolute answer": lenses are not a hierarchy; do not resolve dilemmas artificially | `gispen2017normative` | web | there is no absolute answer to these questions | found. The page says only that the questions have no absolute answer; the non-hierarchy and dilemma-naming rules are SKILL.md's |
| 7 | Assessment and generative questions under each lens (e.g. "What virtues does the design promote?", "Does the design treat users as ends?") | `gispen2017normative` | not in source | using the questions provided on the template | discrepancy confirmed against the text. The questions are in the template download, not on the page; SKILL.md's wording cannot be compared with them (Discrepancy 3) |
| 8 | Step 0 Stakeholder and Power Map, Non-Obvious Harms Inventory | `gispen2017normative` | not in source | Write down your design goal using the format on the template | discrepancy confirmed against the text. The page's second step is writing the design goal; no stakeholder map or harms inventory. edbx addition presented as part of the method (Discrepancy 2) |
| 9 | Creator Impact as part of the Virtue lens | `gispen2017normative` | not in source | Keep in mind that there is no absolute answer | discrepancy confirmed against the text. Not on the page; edbx addition |
| 10 | Universal Law Test (Kantian "what if every product did this?") as a named output | `gispen2017normative` | not in source | Generate design ideas using the questions provided | discrepancy confirmed against the text. Not on the page. The thought experiment is Kant's formula of universal law, model knowledge, uncited in SKILL.md |
| 11 | Triad Conflict Matrix, Cross-Lens Synthesis, the fixed-form Normative Design Statement, Priority Recommendation | `gispen2017normative` | not in source | Empty normative design scheme template | discrepancy confirmed against the text. Presented in SKILL.md as the method's "signature artifact"; the page does not mention them (Discrepancy 2) |
| 12 | "Greatest good for the greatest number" as the consequentialist test | none cited | n/a | greatest good for the greatest number | metadata only: no source found. A utilitarian slogan used without a citation; model knowledge |
| 13 | "2 design ideas per lens (6 total)" | `gispen2017normative` | not in source | You can use them as ideation questions | discrepancy confirmed against the text. The page asks for ideation using the theories; it sets no count |
| 14 | Source details SKILL.md omits: 30 to 60 minutes; template, post-its, pens; design team; envisioning, realising, validating phases | `gispen2017normative` | web | Suggested Time 30 - 60 minutes | found. Not in SKILL.md, which asks for a far larger output than a 30 to 60 minute workshop. The page text shows "Step 2", "Step 3" and "Step 4" under "consists of 4 steps"; no Step 1 appears in the text |
| 15 | Hashtags #evaluateoutcomes #applyvalues #designresponsibility | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Contents not available; not confirmed that the method or these hashtags are in the book |
| 16 | See Also: Layers of Effect, Envisioning Cards, Value Voting | `chivukula2021surveying` | p. 19 | Layers of Effect [161], 360 Review [157] | found for two of the three: the survey lists Layers of Effect and Envisioning Cards as separate methods, with no link to this one. "Value Voting" appears nowhere in the survey text |
| 17 | Method is one of the ethics-focused design methods catalogued in research, attributed to Gispen | `chivukula2021surveying` | p. 28 | Jet Gispen. 2017. Normative Design Scheme | found. The reference list credits Gispen with the method and the Ethics for Designers URL; independent confirmation of Discrepancy 1 |
| 18 | How the survey classifies the method: considering many ethical theories together to improve a design situation | `chivukula2021surveying` | p. 24 | maximizing the ethical valence of a design situation | found. Matches SKILL.md's idea of lenses side by side |
| 19 | Evidence Ledger | edbx addition | n/a | Evidence Ledger family convention from fdbx | metadata only: edbx addition. SKILL.md itself labels it a family convention from fdbx |

## Licence

- **Ethics for Designers tool page (`gispen2017normative`)**: the page text carries only "(c) Jet Gispen 2017" and a template download link. No licence statement. Presume all rights reserved. Paraphrasing the method (assess a design goal against three ethical theories, then use them as ideation questions) is fine. Do not reproduce the template, its questions or its images, and do not ship a modified version of the worksheet, until the author's terms are known. SKILL.md carries lens questions that may be near-verbatim from the template; that cannot be checked until the template is read.
- **Survey paper (`chivukula2021surveying`)**: the manifest labels it CC BY-NC-SA 4.0, but the PDF text shows no CC notice. Page 1 has an ACM-style permission notice instead: copies for personal or classroom use are free if not made for profit or commercial advantage; "for all other uses, contact the owner/author(s)". Treat as cite-only: do not copy text or tables into a paid bundle. It does not cover Gispen's tools.
- **UXP2 microsite and template file**: not in the manifest; terms unchecked. Link only.
- **Universal Methods of Ethical Design (`chivukula2025universal`)**: all rights reserved, paywalled book. Cite only.
- The three ethical theories themselves are public ideas and free to describe. Nothing found forbids paraphrase; the open question is the template's own terms.

## Discrepancies

**Contradicted by the source text** (read on the page; the page says otherwise or is silent where SKILL.md asserts):

1. **Missing creator.** SKILL.md names no creator and `THIRD_PARTY_NOTICES.md` credits "Consequentialist, deontological and virtue ethics". The tool page is by Jet Gispen (Ethics for Designers, 2017) and the survey (p. 28) credits "Jet Gispen". Add her as the primary source. (fixed in SKILL.md; credit already in THIRD_PARTY_NOTICES; tutorial corrected in this pass)
2. **What makes the method.** SKILL.md says five moves (shared stakeholder map, Triad Conflict Matrix, Universal Law Test, Creator Impact, Normative Design Statement) are "what distinguishes the Normative Design Scheme", and that without them "the method is doing no work". The page describes a four-step worksheet (browse, write the design goal, assess it with the three views, generate ideas with the theories). None of the five moves, nor the Non-Obvious Harms Inventory, the Priority Recommendation or the "2 ideas per lens" count, is on the page, so they are edbx additions, not what defines the source method. (fixed in SKILL.md)
3. **Lens mapping and questions not in the readable text.** The Intention / Effect / Design labels and the per-lens questions are not on the page or in the survey; the page sends the reader to the template. The survey (p. 14) confirms only that the worksheet refers to virtue, consequentialist and deontological ethics. (fixed in SKILL.md)
4. **Assess and Generate as two modes.** The page runs assessment then ideation as steps of one sequence; separate modes are SKILL.md's. (fixed in SKILL.md)

**Not verifiable** (no readable source):

5. **Template content.** The template file is not in the manifest, so whether SKILL.md's lens questions and the Intention / Effect / Design pairing come from it, or are edbx's, cannot be settled. The pairing of Deontology with "Design" and Virtue with "Intention" is not the usual textbook framing; check it against the template before presenting it as Gispen's.
6. **Hashtags and the See Also entry "Value Voting"** tie to no readable source; the book's contents are not visible.
7. **Universal Law Test and "greatest good for the greatest number"** are classical philosophy (Kant; utilitarianism) used with no citation.

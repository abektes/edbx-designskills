# Provenance — edbx-cider

Stage B (checked against the text in `papers/pages/oleson2023teaching/`,
2026-10-13). One row per element the skill attributes to a source. Rows whose
source is in `papers/manifest.json` carry a page locator and a verbatim anchor,
or `not in source` where the text was read and the element is absent. Page
numbers are the PDF pages as printed (file number equals page number). The
extracted text drops the "fi" ligature (for example "irst", "ind"), so a few
anchors look misspelled; they are copied as extracted. Other rows are
`metadata only`, with the reason. `oleson2022cider`, `oleson2023dissertation`,
`burnett2016gendermag` and `microsoft2016inclusive` are not in the manifest
and back no row.

## Sources

| Key | Citation | Stable link | Legal free copy | Licence |
|-----|----------|-------------|-----------------|---------|
| `oleson2023teaching` | Oleson, A., Solomon, M., Perdriau, C. & Ko, A. J. (2023). Teaching inclusive design skills with the CIDER assumption elicitation technique. *ACM Transactions on Computer-Human Interaction* 30(1), 1–49. Online 16 Aug 2022. | doi:10.1145/3549074 | Yes: https://par.nsf.gov/biblio/10349236 ; author copies https://faculty.washington.edu/ajko/papers/Oleson2022CIDER.pdf and https://alannaholeson.com/papers/tochi22-CiderAssumptionElicitationTechnique.pdf | Crossref says CC BY 4.0 for the version of record; the PDF text (p. 1) instead carries the ACM notice (personal or classroom use free, not for profit; copyright held by the authors). See Licence |
| `oleson2022cider` | Oleson, A. (2022). CIDER: a method to teach practical critical software design skills. *Proc. 2022 ACM Conference on International Computing Education Research, Vol. 2*, 7–9. | doi:10.1145/3501709.3544295 | not confirmed (ACM full text returned 403; not in manifest) | ACM copyright policy (version of record) |
| `oleson2023dissertation` | Oleson, A. (2023). *Integrating Inclusive Design and Computing Education*. PhD thesis, University of Washington (advisor A. J. Ko). | http://hdl.handle.net/1773/51193 ; https://alannaholeson.com/papers/Oleson_dissertation.pdf | Yes (open access thesis) | unknown (rights field "none") |
| `burnett2016gendermag` | Burnett, M. et al. (2016). GenderMag: a method for evaluating software's gender inclusiveness. *Interacting with Computers* 28(6), 760–787. | doi:10.1093/iwc/iwv046 | not checked | unknown |
| `microsoft2016inclusive` | Microsoft Inclusive Design (2016). Inclusive Activity Cards. | https://inclusive.microsoft.design/articles/inclusive-activity-cards | Yes: the toolkit's own page (card PDF not opened) | CC BY-NC-ND (per the card PDF's footer as quoted in a search result; to verify on the PDF) |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers, ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (commercial book) | unknown |

## Table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | CIDER as an assumption-elicitation technique that surfaces assumptions about users in a design | `oleson2023teaching` | p. 1 | CIDER Assumption Elicitation Technique | Title. Fig. 1 on the same page also shows the five stages |
| 2 | Acronym: Critique, Imagine, Design, Expand, Repeat | `oleson2023teaching` | p. 2 | CIDER (Critique, Imagine, Design, Expand, Repeat) | Abstract |
| 3 | Developed as a teaching tool for inclusive design skills | `oleson2023teaching` | p. 2 | an educational analytical design evaluation method to teach inclusive design skills | Abstract. Evidence is an eleven-week case study with 40 undergraduates and follow-up interviews; no professional-practice study (see row 15) |
| 4 | Stage C: identify the assumptions about users a design carries | `oleson2023teaching` | p. 9 | list as many assumptions about users potential capabilities, contexts | The paper's CRITIQUE stage: the educator picks one real artifact for the whole class; students list assumptions for 3–5 minutes |
| 5 | Stage I: pick one assumption and envision how it excludes people | `oleson2023teaching` | p. 10 | a short scenario in which the artifact’s design breaks down | The paper's IMAGINE stage asks for a 1–2 sentence scenario about a user for whom the assumption is wrong |
| 6 | Stage D: brainstorm changes that make the design more inclusive | `oleson2023teaching` | p. 11 | brainstorm ways to change or adapt the artifact’s design | The paper's DESIGN stage. See row 13 for the quantity |
| 7 | Stage E: pool participants' assumptions into one shared register | `oleson2023teaching` | p. 13 | reviewing and combining them into a single list, removing duplicates | In the paper the educator builds the list (augmenting it with their own expertise) and shares it back to the class. Pooling and removing duplicates are found; clustering, tagging by category and flagging surprises are not (see Discrepancies) |
| 8 | Stage R: pick an assumption not found in one's own critique and repeat Imagine and Design | `oleson2023teaching` | p. 14 | had not surfaced themselves during their own previous critique | The paper's REPEAT stage, drawn from the EXPAND list |
| 9 | Four assumption categories: Ability, Capacity, Environment, Resources | `oleson2023teaching` | p. 7 | assumptions about user ability, capacity, environment, or resources | The four words appear in the paper's statement of CIDER's goal. They are not used as Stage C categories, and the paper's coding of student assumptions (Table 4, p. 26) has nine different types |
| 10 | Stage C minimum: 5 assumptions across 3 of 4 categories | `oleson2023teaching` | not in source | List as many as you can think of | No minimum and no category quota; students list as many as they can in a few minutes |
| 11 | Assumption wording "This design assumes the user [X]" | `oleson2023teaching` | p. 27 | assumes the user has enough motor control | This is one student's own phrasing among the example responses. The paper prescribes no sentence frame |
| 12 | Exclusion scenario must name a specific person (e.g. Mariam) | `oleson2023teaching` | not in source | a user for which the chosen assumption is inaccurate | The scenario is about an unnamed user for whom the assumption fails. No named person is required |
| 13 | Stage D minimum: 3–5 redesigns spanning low-tech / high-tech / systemic / interaction-level | `oleson2023teaching` | not in source | aim for ten or more | The prompt asks for as many as possible, ten or more, regardless of feasibility. No four approach types appear in the paper |
| 14 | Team mode: pooling in a session where each participant shares | `oleson2023teaching` | p. 18 | did not create collective assumptions lists | In the paper's collaborative variant (teams of 2–3 on their own prototypes) there was no EXPAND stage. The shared-register team form is the skill's |
| 15 | Authors and year given as "Oleson, Solomon, Horowitz et al. (2022)" | `oleson2023teaching` | p. 1 | MERON SOLOMON, Art + Art History + Design | Authors are Oleson, Solomon, Perdriau and Ko; "Horowitz" appears nowhere in the text. Copyright line reads 2022; TOCHI 30(1) is 2023 |
| 16 | "Works equally well in professional practice" | `oleson2023teaching` | not in source | originally intended for use in post-secondary design contexts | The paper calls its results an initial classroom evaluation and speaks of use beyond the classroom only as a possibility; it reports no professional-practice test |
| 17 | Related-methods claim: CIDER authors cite GenderMag as foundational | `oleson2023teaching` | p. 5 | assumptions about users capabilities, resources, and interaction styles | The paper cites Burnett et al. 2016 here (and in its reference list, p. 43) alongside another work. It also names GenderMag-Teach on p. 7. Nothing calls GenderMag foundational |
| 18 | See also: Inclusive Activity Cards as a lighter-weight, portable version of the same practice | `oleson2023teaching` | not in source | Microsoft 2020 Inclusive Design | The reference list cites a Microsoft Inclusive Design page; the Activity Cards are not mentioned anywhere in the paper |
| 19 | Inclusive Activity Cards (the toolkit itself) | `microsoft2016inclusive` | web | Inclusive Activity Cards | metadata only: no source found in the manifest (toolkit page not fetched). Licence reported as CC BY-NC-ND, unverified |
| 20 | Hashtags and "See Also" list (#newperspectives, #identifyvalues, #designresponsibility; GenderMag, Inclusive Activity Cards) | `chivukula2025universal` | entry 11 | Universal Methods of Ethical Design | metadata only: book. CIDER is entry no. 11 in the book's method list |
| 21 | Inclusive Design Commitment sentence (action, date, owner, because) | `edbx addition` | — | Inclusive Design Commitment | metadata only: edbx addition. Not in the method as published |

## Licence

- **`oleson2023teaching` — licence unsettled.** Crossref (version of record)
  and the manifest say CC BY 4.0, but the PDF text read here (p. 1, both the PAR
  copy and the author copy) carries only the ACM notice: copying for personal or
  classroom use is free provided it is not for profit or commercial advantage;
  third-party components must be honoured; other uses via the owner/authors;
  copyright held by the authors. The text contains no mention of Creative
  Commons. Paraphrase and cite: yes. Verbatim reproduction, a modified version
  or commercial use: only after the TOCHI page confirms CC BY 4.0 (then
  attribution to Oleson, Solomon, Perdriau & Ko, a link to the licence and an
  indication of changes are required). Until then, treat as the ACM terms.
- **`oleson2022cider`.** ACM copyright policy, three-page extended
  abstract. Paraphrase only; do not copy text or figures.
- **`oleson2023dissertation`.** unknown (rights field "none"); open access.
  Paraphrase only until the rights statement is checked.
- **`burnett2016gendermag`.** unknown; publisher licence not checked. Cite
  only.
- **`microsoft2016inclusive`.** Reported as CC BY-NC-ND (copyright Microsoft
  2016). **If correct, NC and ND block commercial redistribution and modified
  versions of the cards themselves.** Do not copy the cards or their text into
  this paid bundle; naming and linking to them, as the skill does, is fine.
  Confirm on the PDF footer.
- **`chivukula2025universal`.** Commercial book; no open licence found.
  Paraphrase; do not reproduce text.
- No source here blocks commercial use of the CIDER method itself, as paraphrased.

## Discrepancies

### Contradicted by the source text

1. **Wrong author list.** SKILL.md says "Oleson, Solomon, Horowitz et al.
   (2022)". The paper's authors are Oleson, Solomon, Perdriau and Ko (p. 1);
   Horowitz does not appear in the text. The skill gives no venue or DOI.
2. **Scope.** SKILL.md says CIDER "works equally well in professional
   practice". The paper presents a teaching technique tested in one
   undergraduate course and says only that results suggest promise beyond the
   classroom (rows 3, 15).
3. **Stage C minimum (5 assumptions, 3 of 4 categories).** The paper has no
   count or category quota (row 10). The four terms appear in the paper only as
   its statement of what the technique targets (row 9); the paper's own coding
   found nine assumption types (Table 4).
4. **Named person in the exclusion scenario.** The paper's scenario is 1–2
   sentences about an unnamed user for whom the assumption fails (row 12). The
   Mariam-style example in the skill is the skill's own addition and should be
   marked invented.
5. **Stage D quantity and types.** The paper asks for as many solutions as
   possible, "ten or more", with feasibility set aside; SKILL.md asks for 3–5
   and four approach types (row 13).
6. **Stage E procedure.** In the paper the educator compiles the shared list,
   removing duplicates and adding expertise. The five-step team procedure
   (pool, deduplicate, cluster, tag, flag surprises) is not in the paper; the
   paper's collaborative variant dropped the EXPAND stage (rows 7, 14).
7. **Stage R.** The paper has students choose from the shared EXPAND list an
   assumption they did not surface; SKILL.md's solo variant (choose from
   Stage C) and its rationale that the first assumption is usually the most
   obvious are not in the paper, which gives a different rationale (a
   guaranteed new instance of bias).
8. **GenderMag link.** Stage A reported no GenderMag or Burnett entry in the
   reference list. That was wrong: Burnett et al. (2016) is reference [10]
   (p. 43) and is cited on p. 5, and GenderMag-Teach is named on p. 7. The paper
   does not call GenderMag foundational.
9. **Inclusive Activity Cards.** The paper never mentions them (it cites a
   different Microsoft Inclusive Design page). The "lighter-weight, portable
   version of the same practice" claim in `references/related-methods.md` has no
   support in the paper.

### Not verifiable

10. **Inclusive Design Commitment sentence** and the mindset-check box are not
    in the method as published; mark as skill additions.
11. **Licence of Microsoft's Inclusive Activity Cards** (reported CC BY-NC-ND)
    is unverified; page not fetched.
12. **Integration section** names sibling edbx skills; that is not a claim about
    the source.

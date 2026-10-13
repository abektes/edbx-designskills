# Provenance — edbx-cider

Stage A draft (sources and licences, no downloads, 2026-10-13). One row per
element the skill attributes to a source. Locator and anchor are filled only
where confirmed from a page read in this pass (publisher/repository record,
Crossref, or an abstract); otherwise Locator is `to verify` and the anchor is a
best guess marked `(guess)`. The paper's full text could not be read as a web
page in this pass (the PDFs are not machine-readable as pages, the ACM full text
returned 403), so the stage details below rest on the abstract and on summaries
of the paper and need checking in Stage B.

## Sources

| Key | Citation | Stable link | Legal free copy | Licence |
|-----|----------|-------------|-----------------|---------|
| `oleson2023teaching` | Oleson, A., Solomon, M., Perdriau, C. & Ko, A. J. (2023). Teaching inclusive design skills with the CIDER assumption elicitation technique. *ACM Transactions on Computer-Human Interaction* 30(1), 1–49. Online 16 Aug 2022. | doi:10.1145/3549074 | Yes: https://par.nsf.gov/biblio/10349236 ; author copies https://faculty.washington.edu/ajko/papers/Oleson2022CIDER.pdf and https://alannaholeson.com/papers/tochi22-CiderAssumptionElicitationTechnique.pdf | CC BY 4.0 (Crossref licence entry, version of record) |
| `oleson2022cider` | Oleson, A. (2022). CIDER: a method to teach practical critical software design skills. *Proc. 2022 ACM Conference on International Computing Education Research, Vol. 2*, 7–9. | doi:10.1145/3501709.3544295 | not confirmed (ACM full text returned 403) | ACM copyright policy (version of record) |
| `oleson2023dissertation` | Oleson, A. (2023). *Integrating Inclusive Design and Computing Education*. PhD thesis, University of Washington (advisor A. J. Ko). | http://hdl.handle.net/1773/51193 ; https://alannaholeson.com/papers/Oleson_dissertation.pdf | Yes (open access thesis) | unknown (rights field "none") |
| `burnett2016gendermag` | Burnett, M. et al. (2016). GenderMag: a method for evaluating software's gender inclusiveness. *Interacting with Computers* 28(6), 760–787. | doi:10.1093/iwc/iwv046 | not checked | unknown |
| `microsoft2016inclusive` | Microsoft Inclusive Design (2016). Inclusive Activity Cards. | https://inclusive.microsoft.design/articles/inclusive-activity-cards | Yes: the toolkit's own page (card PDF not opened) | CC BY-NC-ND (per the card PDF's footer as quoted in a search result; to verify on the PDF) |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers, ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (commercial book) | unknown |

## Table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | CIDER as an assumption-elicitation technique that surfaces assumptions about users in a design | `oleson2023teaching` | title / abstract | CIDER Assumption Elicitation Technique | free copy: https://par.nsf.gov/biblio/10349236 |
| 2 | Acronym: Critique, Imagine, Design, Expand, Repeat | `oleson2023teaching` | abstract | Critique, Imagine, Design, Expand, Repeat | free copy: https://par.nsf.gov/biblio/10349236 |
| 3 | Developed as a teaching tool for inclusive design skills | `oleson2023teaching` | title / abstract | Teaching Inclusive Design Skills | free copy: https://par.nsf.gov/biblio/10349236 . Evidence is an 11-week case study with 40 undergraduates; no professional-practice study found |
| 4 | Stage C: identify the assumptions about users a design carries | `oleson2023teaching` | to verify | assumptions about users (guess) | free copy: https://par.nsf.gov/biblio/10349236 |
| 5 | Stage I: pick one assumption and envision how it excludes people | `oleson2023teaching` | to verify | envision how it excludes (guess) | free copy: https://par.nsf.gov/biblio/10349236 |
| 6 | Stage D: brainstorm changes that make the design more inclusive | `oleson2023teaching` | to verify | brainstorm inclusive redesigns (guess) | free copy: https://par.nsf.gov/biblio/10349236 |
| 7 | Stage E: pool participants' assumptions into one shared register | `oleson2023teaching` | to verify | overview of the assumption space (guess) | free copy: https://par.nsf.gov/biblio/10349236 . In the paper's classroom form the instructor compiles the class list; see Discrepancies |
| 8 | Stage R: pick an assumption not found in one's own critique and repeat Imagine and Design | `oleson2023teaching` | to verify | important but did not surface (guess) | free copy: https://par.nsf.gov/biblio/10349236 |
| 9 | Four assumption categories: Ability, Capacity, Environment, Resources | none found | — | — | not found. Terms tried: CIDER ability capacity environment resources assumption categories; Oleson Ko CIDER assumption types. Possibly a skill-level scheme |
| 10 | Assumption wording "This design assumes the user [X]" | `oleson2023teaching` | to verify | This design assumes (guess) | free copy: https://par.nsf.gov/biblio/10349236 |
| 11 | Exclusion scenario must name a specific person (e.g. Mariam) | none found | — | — | not found. Terms tried: CIDER exclusion scenario named person. The named examples in the skill are invented |
| 12 | Minimums: 5 assumptions across 3 of 4 categories; 3–5 redesigns spanning low-tech / high-tech / systemic / interaction-level | none found | — | — | not found. Terms tried: CIDER redesign types |
| 13 | Authors and year given as "Oleson, Solomon, Horowitz et al. (2022)" | `oleson2023teaching` | record | Oleson, Solomon, Perdriau, Ko | free copy: https://par.nsf.gov/biblio/10349236 (authors confirmed on the PAR record and Crossref) |
| 14 | "Works equally well in professional practice" | none found | — | — | not found. Terms tried: CIDER professional practice designers |
| 15 | Related-methods claim: CIDER authors cite GenderMag as foundational | `burnett2016gendermag` | to verify | GenderMag (guess) | metadata only: paywalled (access not checked). Crossref shows no Burnett or GenderMag entry in the 95-item reference list of `oleson2023teaching` |
| 16 | See also: Inclusive Activity Cards as lighter-weight, portable version of the same practice | `microsoft2016inclusive` | to verify | Inclusive Activity Cards | toolkit page: https://inclusive.microsoft.design/articles/inclusive-activity-cards . Not cited by the CIDER paper per the Crossref reference list |
| 17 | Hashtags and "See Also" list (#newperspectives, #identifyvalues, #designresponsibility; GenderMag, Inclusive Activity Cards) | `chivukula2025universal` | to verify | CIDER (guess) | metadata only: book. CIDER is entry no. 11 in the book's method list |
| 18 | Inclusive Design Commitment sentence (action, date, owner, because) | none found | — | — | not found; reads as an edbx addition |

## Licence

- **`oleson2023teaching` — CC BY 4.0** (Crossref, version of record). The
  most permissive source in the set. May paraphrase (yes); may reproduce text,
  figures and stage definitions verbatim with attribution (yes); may ship a
  modified version with attribution and an indication of changes (yes);
  commercial use allowed. Credit Oleson, Solomon, Perdriau & Ko and link the
  licence. Note the author-hosted PDFs may carry other terms; rely on the
  CC BY 4.0 of the TOCHI version of record.
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
- No source here blocks commercial use of the CIDER method itself.

## Discrepancies

1. **Wrong author list.** SKILL.md says "Oleson, Solomon, Horowitz et al.
   (2022)". The authors are Oleson, Solomon, Perdriau and Ko. There is no
   Horowitz. Year: online Aug 2022, issue date Feb 2023 (TOCHI 30(1)). The
   skill gives no venue or DOI.
2. **Scope.** The method is described by its authors as a technique for
   *teaching* inclusive design to students (class activity, one artifact chosen
   by the instructor). SKILL.md's "works equally well in professional
   practice" has no study behind it in the sources found.
3. **Four categories (Ability, Capacity, Environment, Resources)** are
   presented as the lenses of Stage C; I could not find them in the abstract,
   the summaries read, or the PAR record. Unverified; may be skill-level
   structure. The same applies to the required minimums (5 assumptions, 3
   categories).
4. **"Name a specific person" and the Mariam-style examples.** No source found
   requires this; the examples in `references/` are invented and should be
   marked so.
5. **Stage E detail.** The skill's five-step procedure (pool, deduplicate,
   cluster, tag, flag surprises) and "team mode" are not found; the paper's
   classroom version has the instructor compile the shared list.
6. **Stage R.** Summaries of the paper say students pick an assumption from the
   shared list that they did not surface themselves. SKILL.md says "different
   assumption from the Stage E register (or from Stage C if working solo)" and
   gives a rationale about the first assumption being the most obvious; neither
   the solo variant nor the rationale was found.
7. **Stage D wording.** "3–5 redesign ideas" spanning four approach types: not
   found.
8. **GenderMag link.** `references/related-methods.md` says the CIDER authors
   cite GenderMag as foundational; the Crossref reference list for the TOCHI
   paper (95 entries) has no GenderMag or Burnett entry. Crossref lists can be
   incomplete; check the paper's reference section. The same file links
   Inclusive Activity Cards as "a lighter-weight, more portable version of the
   same underlying practice"; no source found.
9. **Inclusive Design Commitment** (the "We commit to..." sentence) and the
   mindset-check box are not in the method as published; mark as skill additions.
10. **Integration section** names sibling edbx skills as methods "in the broader
    family"; fine, but it is not a claim about the source.

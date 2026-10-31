# Provenance — edbx-fair-patterns

Stage B (checked against source text). Every row either names one key in
`papers/manifest.json` with an anchor copied from its page text, or is marked
`metadata only` with the reason. Page text read for this skill: the Deceptive
Patterns page for the Gray et al. 2024 ontology (`gray2024ontology`, a landing
page with the abstract), the GDPR Art. 7 page (`eu2016gdpr`), the Springlex copy
of DSA Art. 25 and Art. 52 (`eu2022dsa`), the CPPA Enforcement Advisory
2024-02 (`cppa2024advisory`) and the ICER 2021 dark-design paper
(`gray2021dark`). The Fair Patterns taxonomy paper, the creators' podcast, the
Cambridge 2025 article, Brignull's lists, the Omnibus Directive, the UK DMCC
Act, LGPD and the FTC v. Amazon case are not in the manifest, so they are
`metadata only`. Locator `not in source` means the skill's element is not in
the cited source; the anchor quotes the closest passage and the Note says what
the source says.

## Contents

- Sources
- Rows
- Licence
- Discrepancies

## Sources

| Key | Citation | DOI / URL | Legal free copy |
|---|---|---|---|
| `potelsaville2023fair` | Potel-Saville, M., & Da Rocha, M. (2023). From Dark Patterns to Fair Patterns? Usable Taxonomy to Contribute Solving the Issue with Countermeasures. Annual Privacy Forum 2023; in *Privacy Technologies and Policy*, Springer, 2024. | doi:10.1007/978-3-031-61089-9_7; abstract at https://www.springerprofessional.de/en/from-dark-patterns-to-fair-patterns-usable-taxonomy-to-contribut/27148394 and https://www.deceptive.design/articles/from-dark-patterns-to-fair-patterns-usable-taxonomy-to-contribute-solving-the-issue-with-countermeasures | Unconfirmed: Springer full text is behind login; a ResearchGate listing exists but returned 403, so unverified |
| `lechevalier2025fairness` | Lechevalier, F., & Potel Saville, M. (2025). Fairness by design: Combatting deceptive AI-driven interfaces. *Cambridge Forum on AI: Law and Governance* 1, e31. | doi:10.1017/cfl.2025.10018; https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/fairness-by-design-combatting-deceptive-aidriven-interfaces/9F32AFC1AD43FAA7F2F271DADB2F09FF | Yes: open access on the publisher page (CC BY-NC-SA 4.0) |
| `potelsaville2024podcast` | Potel-Saville, M., interviewed on The Shifting Privacy Left Podcast, S3E11, "Decision-Making Governance & Design: Combating Dark Patterns with Fair Patterns". (Spoken account by the taxonomy's author, not a paper.) | https://shiftingprivacyleft.buzzsprout.com/2059470/episodes/14961753-s3e11-decision-making-governance-design-combating-dark-patterns-with-fair-patterns-with-marie-potel-saville-amurabi-fairpatterns | Episode page is free; licence not stated |
| `fairpatterns2026site` | FairPatterns (company site founded by Potel-Saville, Gupta, Narayanan). | https://www.fairpatterns.ai/ | Site is free to read; library/resources partly gated (free and premium tiers) |
| `brignull2010darkpatterns` | Brignull, H. (2010 onward). Dark Patterns / "Types of Dark Patterns", darkpatterns.org; now https://www.deceptive.design/types (renamed Deceptive Patterns). Wikipedia: Brignull coined "dark pattern" on 28 July 2010. | https://www.deceptive.design/types ; https://en.wikipedia.org/wiki/Dark_pattern | Yes: website free to read. The 2010 original list itself was not read |
| `brignull2023deceptive` | Brignull, H. (2023). *Deceptive Patterns: Exposing the Tricks Tech and Businesses Play on You.* Testimonium. | not looked up | No (commercial book) |
| `gray2024ontology` | Gray, C. M., Teixeira Santos, C., Bielova, N., & Mildner, T. (2024). An Ontology of Dark Patterns Knowledge: Foundations, Definitions, and a Pathway for Shared Knowledge-Building. CHI 2024. | doi:10.1145/3613904.3642436; https://deceptive.design/articles/an-ontology-of-dark-patterns-knowledge-foundations-definitions-and-a-pathway-for-shared-knowledge-building | Yes, likely: NSF PAR copy listed (par.nsf.gov purl 10506967, not fetched); not confirmed on a landing page |
| `chivukula2025universal` | Chivukula, S. S., & Gray, C. M. *Universal Methods of Ethical Design* (Rockport, listed 1 April 2025). The skill's "Fair Patterns" entry is stated to derive from this compilation. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | No (commercial book) |
| `eu2022dsa` | Regulation (EU) 2022/2065 (Digital Services Act), Arts. 25 and 52, recital 67. | CELEX 32022R2065; read via https://www.springlex.eu/en/packages/dsa/dsa-regulation/article-25/ | Yes: EUR-Lex (page returned empty to my fetch); article text read on the Springlex copy |
| `eu2016gdpr` | Regulation (EU) 2016/679 (GDPR), Art. 7(3). | https://gdpr-info.eu/art-7-gdpr/ (search result only; page itself not fetched) | Yes: EUR-Lex / gdpr-info.eu |
| `eu2019omnibus` | Directive (EU) 2019/2161 (Omnibus), amending Directive 2005/29/EC and others. | CELEX 32019L2161 (search results only) | Yes: EUR-Lex |
| `uk2024dmcc` | UK Digital Markets, Competition and Consumers Act 2024 (CMA direct consumer enforcement from 6 April 2025). | read via law-firm summaries in search results | Yes: legislation.gov.uk (not opened) |
| `ca2020cpra` | California Civil Code 1798.140(h) (consent) and (l) (dark pattern), as amended by CPRA; 11 CCR 7004. | read via search-result summaries; https://www.cppa.ca.gov/pdf/enfadvisory202402.pdf (PDF, not fetched) | Yes: leginfo.legislature.ca.gov / Cornell LII (not opened) |
| `ftc2023amazon` | FTC v. Amazon (Prime enrolment and cancellation), FTC Act and ROSCA; filed 2023; settled 25 September 2025 for USD 2.5bn per press reports. | press coverage, e.g. https://www.mediapost.com/publications/article/409399 | Press only; not the complaint |
| `brazil2018lgpd` | Brazil Lei 13.709/2018 (LGPD), Arts. 9 and 52. | https://lgpd-brazil.info/ (search results only) | Yes: planalto.gov.br (not opened) |
| `cppa2024advisory` | California Privacy Protection Agency, Enforcement Division, Enforcement Advisory No. 2024-02, "Avoiding Dark Patterns: Clear and Understandable Language, Symmetry in Choice" (4 pp., 4 September 2024). | https://www.cppa.ca.gov/pdf/enfadvisory202402.pdf | Yes: public government PDF (in manifest) |
| `gray2021dark` | Gray, C. M., Chivukula, S. S., Melkey, K., & Manocha, R. (2021). Understanding dark design roles in computing education. ICER 2021. | doi:10.1145/3446871.3469754 | Yes: NSF PAR accepted manuscript (in manifest; ACM copyright) |



## Rows

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | Fair Patterns as an ethical alternative perspective: countermeasures to dark patterns | `potelsaville2023fair` | abstract | shifting from problem-oriented to problem-solving | metadata only: paywalled (abstract read in stage A at springerprofessional.de) |
| 2 | Creators of the method (the skill names none) | `potelsaville2023fair` | author line | Potel-Saville, Da Rocha | metadata only: paywalled. Also Amurabi / FairPatterns, per fairpatterns.ai |
| 3 | Fair pattern defined as an interface that empowers free, informed choice | `potelsaville2023fair` | abstract | notion of "fair pattern" | metadata only: paywalled. The empowerment wording came from a search summary |
| 4 | "Seven fair pattern types" (the countermeasure set) | `potelsaville2024podcast` | transcript page | seven categories and their countermeasures | metadata only: no source found in manifest (podcast transcript read in stage A; the paper's Table 3 unread). The count matches the skill |
| 5 | Plain and Empowering Language | `potelsaville2024podcast` | transcript page | plain and empowering language | metadata only: no source found in manifest. Paired with "Misleading or obstructing language" |
| 6 | Nonobstructive Information | `potelsaville2024podcast` | transcript page | Remove emotional, temporal, or social triggers | metadata only: no source found in manifest. Sources say "non-intrusive", paired with "Push and pressure"; see Discrepancies |
| 7 | Summary Path | `potelsaville2024podcast` | transcript page | Redesign the task flow to support user goals | metadata only: no source found in manifest. Source says "seamless path", paired with "Maze" |
| 8 | Adequate Information | `potelsaville2024podcast` | transcript page | adequate information fair pattern | metadata only: no source found in manifest. Paired with "Missing information"; the Cambridge 2025 article (Fig. 7) uses it against roach motel |
| 9 | Protective Default | `potelsaville2024podcast` | transcript page | Set defaults in the user's interest | metadata only: no source found in manifest. Transcript says "neutral default", paired with "Harmful default" |
| 10 | Free Action | `potelsaville2024podcast` | transcript page | Give users genuine control over their path | metadata only: no source found in manifest. Paired with "More than intended" |
| 11 | Fair UX | `potelsaville2024podcast` | transcript page | Reorder visual hierarchy so the honest choice | metadata only: no source found in manifest. Paired with "Distorted UX" |
| 12 | "Maps directly to the Gray et al. (2024) ontology" | `gray2024ontology` | not in source | standardized definitions for 64 synthesized dark pattern types | the page (abstract of the CHI 2024 paper) describes a three-level ontology of 64 synthesized types from ten taxonomies. It mentions no fair patterns, no seven-type remediation set and no ten-row table |
| 13 | Ten-row dark pattern table: Trick Questions, Roach Motel, Misdirection, Confirmshaming, Disguised Ads, Forced Continuity, Hidden Costs, Bait and Switch | `brignull2010darkpatterns` | to verify | trick questions while filling in a form | metadata only: no source found in manifest (Brignull's original list not read; names seen in search summaries only) |
| 14 | Privacy Zuckering | `brignull2010darkpatterns` | Wikipedia "Dark pattern" | Privacy Zuckering tricking users into sharing more data | metadata only: no source found in manifest (Wikipedia lists the pattern) |
| 15 | Urgency/Scarcity as one pattern type | `brignull2010darkpatterns` | https://www.deceptive.design/types | Fake urgency / Fake scarcity | metadata only: no source found in manifest. The current site lists them as two types |
| 16 | Dark patterns as deceptive interfaces that redirect users against their interests | `gray2021dark` | p. 3 | carefully crafted to trick users into doing things | the paper credits the term to Brignull in 2010 and quotes his definition; it adds the Gray et al. gloss "user value is supplanted in favor of shareholder value" |
| 17 | Skill's attribution to *Universal Methods of Ethical Design* | `chivukula2025universal` | to verify | Universal Methods of Ethical Design | metadata only: book (publisher page lists no individual method) |
| 18 | Step 2.5 Root Cause Reframe | `edbx addition` | to verify | Root Cause Reframe | metadata only: edbx addition |
| 19 | Step 2.6: GDPR Art. 7(3), right to withdraw consent | `eu2016gdpr` | web | as easy to withdraw as to give consent | gdpr-info.eu page for Art. 7; the withdrawal rule is the numbered paragraph 3 |
| 20 | Step 2.6: EU Omnibus Directive 2019/2161 | `eu2019omnibus` | penalties provision | fines of at least 4% of annual turnover | metadata only: no source found in manifest (EUR-Lex CELEX 32019L2161 not fetched). Ceiling is set per Member State law |
| 21 | Step 2.6: DSA Art. 25 as a dark-patterns ban | `eu2022dsa` | web | deceives or manipulates the recipients of their service | Springlex copy of Art. 25 paragraph 1. It binds providers of online platforms, not only very large ones |
| 22 | Step 2.6: "named list of patterns banned by the DSA (pre-checked boxes, repeated nagging, hiding the cancel option, false urgency, confirmshaming)" | `eu2022dsa` | not in source | terminating a service more difficult than subscribing to it | Art. 25(3) only lets the Commission issue guidelines on three practices: prominence of choices, repeated requests after a choice, and harder termination than sign-up. Pre-checked boxes, false urgency and confirmshaming are not named in Art. 25; recital 67 lists other examples |
| 23 | Step 2.6: DSA fine "up to 6%" | `eu2022dsa` | web | 6 % of the annual worldwide turnover | Springlex copy of Art. 52: Member States set fines, capped at 6% of the provider's annual worldwide turnover for a breach of an obligation |
| 24 | Step 2.6: FTC Act s.5 and the Amazon Prime cancellation case, 2023 | `ftc2023amazon` | press coverage | misleading millions of consumers into enrolling in Prime | metadata only: no source found in manifest (press coverage only; settled 25 Sept 2025 per press, which the skill omits) |
| 25 | Step 2.6: CCPA s.1798.140 dark patterns and consent | `cppa2024advisory` | p. 2 | agreement obtained through use of dark patterns | quotes Civil Code s.1798.140(l) (dark pattern) and (h) (consent); also 11 CCR s.7004(a) symmetry in choice |
| 26 | Step 2.6: "UK CMA Digital Markets Act" | `uk2024dmcc` | summaries | Digital Markets, Competition and Consumers Act | metadata only: no source found in manifest. The UK instrument is the DMCC Act 2024; the Digital Markets Act is an EU regulation |
| 27 | Step 2.6: Brazilian LGPD Art. 9 | `brazil2018lgpd` | Art. 9 | clearly, adequately and ostensively | metadata only: no source found in manifest. Art. 9 is a transparency right; the fine ceiling is in Art. 52 |
| 28 | Step 2.7 Vulnerable Population Harm Matrix | `edbx addition` | to verify | Vulnerable Population Harm Matrix | metadata only: edbx addition |
| 29 | Step 3 Default Assessment (harmful / neutral / protective) | `potelsaville2024podcast` | transcript page | Default Assessment harmful neutral protective | metadata only: no source found in manifest. Harmful vs neutral default is in the taxonomy; the three-colour grading is an edbx addition |
| 30 | Implementation priority formula (Legal Risk x User Impact) / Effort; Fair Design Statement | `edbx addition` | to verify | Legal Risk × User Impact ÷ Implementation Effort | metadata only: edbx addition |
| 31 | Mindset: dark patterns do not always come from malicious intent | `cppa2024advisory` | p. 1 | Dark patterns are about effect, not intent | supported for the legal test: the advisory says effect, not intent, decides. Nothing there about misaligned incentives (that is the skill's reading) |
| 32 | Plain language and equal-effort choice as the fix | `cppa2024advisory` | p. 1 | clear and understandable language and offering consumers symmetrical choices | supports Plain and Empowering Language and the path-length point; 11 CCR s.7004(a)(2) on p. 2 says the privacy-protective path must not be longer than the other |
| 33 | Hashtags and See Also (Ethical Blueprint, White Hat Design Patterns) | `chivukula2025universal` | to verify | Ethical Blueprint White Hat Design Patterns | metadata only: book. The Everyday Ethics methods list (stage A) has White Hat Design Patterns but not Ethical Blueprint |

## Licence

Statements found in the page text are marked "in the text"; the rest is from
stage A or `papers/manifest.json`.

- `potelsaville2023fair` (Springer, APF 2023 / 2024 volume): full text behind
  login; no licence on the page read. Treat as all rights reserved. Paraphrase
  with citation: yes. Reproduce Table 3, category names as a table or diagrams
  verbatim: no. Ship a modified version: no.
- `lechevalier2025fairness` (Cambridge): CC BY-NC-SA 4.0 per the publisher page
  (stage A; not in manifest). Non-commercial and share-alike; blocks pasting
  its figures or text into this paid bundle. Paraphrase with citation is fine.
- `potelsaville2024podcast`: spoken interview, licence not stated. Do not
  reproduce the transcript.
- `fairpatterns2026site`: licence not stated; the resource library is partly
  premium. The "Fair Patterns" name is the company's brand; whether it is a
  registered mark is unknown.
- `brignull2010darkpatterns` / deceptive.design: in the text of the
  `gray2024ontology` landing page: "Please ensure appropriate attribution",
  (c) 2026 Testimonium Ltd, no open licence. Use type names with citation; do
  not copy descriptions. Wikipedia text is CC BY-SA 4.0 (share-alike).
- `gray2024ontology`: the manifest says licence unknown; the landing page in
  the manifest has no licence line. Paraphrase only.
- `gray2021dark`: ACM copyright (manifest, NSF PAR accepted manuscript). Paraphrase
  only; the single short Brignull definition is quoted as an anchor.
- `cppa2024advisory`: a public government PDF with no licence statement in the
  text. In the text: advisories "do not provide any options for alternative
  relief or safe harbor" and are not legal advice; statutes and regulations
  control. Cite and paraphrase.
- `eu2016gdpr` (gdpr-info.eu) and `eu2022dsa` (Springlex): official EU law is
  public, but the copies read are third-party pages with no reuse terms. In the
  Springlex text: it "has no legal effect" and the Official Journal text
  prevails. Cite the article; paraphrase.
- `brignull2023deceptive`, `chivukula2025universal`: commercial books, assume
  all rights reserved.
- Other statutes and the FTC case (Omnibus, DMCC, LGPD, FTC v. Amazon): not
  read; cite and paraphrase.
- Net: the repo may paraphrase all of the above with citation. Cambridge 2025
  (CC BY-NC-SA) forbids commercial reuse and requires share-alike; the Wikipedia
  text is share-alike. No source here allows shipping a modified copy of its
  text or tables in the paid bundle.

## Discrepancies

Contradicted by the source text (read on the page):

1. DSA "named patterns explicitly banned for VLOPs (pre-checked boxes, repeated
   nagging after declined consent, hiding the cancel option, false urgency,
   confirmshaming)". Art. 25 (Springlex copy) applies to "providers of online
   platforms", not only very large ones. Paragraph 1 bans deceiving or
   manipulating interfaces; paragraph 2 excludes practices covered by Directive
   2005/29/EC and the GDPR; paragraph 3 lets the Commission issue guidelines on
   three practices (prominence of choices, repeated requests, harder
   termination than sign-up). Pre-checked boxes, false urgency and
   confirmshaming are not in the article.
2. "Maps directly to the Gray et al. (2024) ontology": the ontology page
   describes 64 synthesized types across three levels from ten taxonomies; it
   says nothing of fair patterns, and the skill's ten-row table and seven
   countermeasures are not that ontology. (fixed in SKILL.md)

Not verifiable (no readable source in the manifest; stage A's reading of the
podcast and other pages is recorded in the Notes):

3. "Nonobstructive Information", "Summary Path", "Protective Default": stage A
   found the creators' words to be "non-intrusive information", "seamless path"
   and "neutral default". The taxonomy paper's Table 3 was unread. (fixed in SKILL.md)
4. "UK CMA Digital Markets Act": the UK regime is the DMCC Act 2024; the Digital
   Markets Act is an EU regulation. Not checked at text level. (fixed in SKILL.md)
5. "Urgency/Scarcity" as one type: the current Deceptive Patterns taxonomy
   lists Fake urgency and Fake scarcity separately. The ten-row table as "the
   major taxonomy": Brignull's original list was not read, and it also holds
   items the table omits. (fixed in SKILL.md)
6. The seven fair pattern descriptions in the skill's table: definitions not in
   any readable page; only names and pairings from the podcast transcript. (fixed in SKILL.md)
7. Steps 2.5 (Root Cause Reframe), 2.7 (Vulnerable Population Harm Matrix), the
   three-colour Default Assessment grading, the priority formula and the Fair
   Design Statement: edbx additions; the skill labels only the Evidence Ledger
   as an adaptation. (fixed in SKILL.md)
8. "GDPR up to 4% of global turnover", Omnibus 4%, FTC consent decrees and per-
   violation fines, LGPD Art. 9: not in the manifest. The Amazon outcome
   (settled 2025) is missing from the skill. LGPD Art. 9 is a transparency
   right, not a dark-pattern rule.
9. Attribution to *Universal Methods of Ethical Design*, the hashtags and the
   See Also entry "Ethical Blueprint": book unread.

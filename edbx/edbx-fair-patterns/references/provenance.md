# Provenance — edbx-fair-patterns

Stage A (sources and licences, no downloads). One row per element the skill
attributes to a source, in cdbx's format. Locator and anchor are filled only
where I read a page (abstract, landing page, statute text, transcript page);
otherwise Locator is `to verify` and the anchor is marked `(guess)`. No PDF was
fetched. The full text of the Fair Patterns taxonomy paper (Springer, Table 3)
was not readable (login wall; ResearchGate and ACM returned 403), so the fair
pattern names below come from the creators' own podcast transcript page and a
2025 open-access article by the same creators, not from the taxonomy table.

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

## Rows

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | Fair Patterns as an ethical alternative perspective: countermeasures to dark patterns | `potelsaville2023fair` | abstract | shifting from problem-oriented to problem-solving | metadata only: paywalled (abstract read at https://www.springerprofessional.de/en/from-dark-patterns-to-fair-patterns-usable-taxonomy-to-contribut/27148394) |
| 2 | Creators of the method (the skill names none) | `potelsaville2023fair` | author line | Potel-Saville, Da Rocha | metadata only: paywalled. Also Amurabi / FairPatterns, per https://www.fairpatterns.ai/ |
| 3 | Fair pattern defined as an interface that empowers free, informed choice | `potelsaville2023fair` | abstract | notion of "fair pattern" | metadata only: paywalled. The empowerment wording is from a search summary, to verify |
| 4 | "Seven fair pattern types" (the countermeasure set) | `potelsaville2024podcast` | transcript page | seven categories and their countermeasures | toolkit page: the creator lists seven dark pattern categories each paired with one fair pattern; the count matches the skill; Table 3 of the paper unread |
| 5 | Plain and Empowering Language | `potelsaville2024podcast` | transcript page | plain and empowering language | toolkit page: paired with "Misleading or obstructing language" |
| 6 | Nonobstructive Information | `potelsaville2024podcast`; `lechevalier2025fairness` | transcript page; Fig. 8 caption | non-intrusive information | free copy: https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/fairness-by-design-combatting-deceptive-aidriven-interfaces/9F32AFC1AD43FAA7F2F271DADB2F09FF. Sources say "non-intrusive"; paired with "Push and pressure" (podcast), and confirmshaming (article) |
| 7 | Summary Path | `potelsaville2024podcast` | transcript page | seamless path | toolkit page: sources say "seamless path", paired with "Maze" |
| 8 | Adequate Information | `lechevalier2025fairness`; `potelsaville2024podcast` | Fig. 7; transcript page | adequate information fair pattern | free copy: https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/fairness-by-design-combatting-deceptive-aidriven-interfaces/9F32AFC1AD43FAA7F2F271DADB2F09FF. Paired with "Missing information"; article uses it against roach motel |
| 9 | Protective Default | `potelsaville2024podcast` | transcript page | neutral default | toolkit page: the transcript says "neutral default", paired with "Harmful default". A search summary of the paper's table says "protective default"; unread, to verify |
| 10 | Free Action | `potelsaville2024podcast` | transcript page | free action | toolkit page: paired with "More than intended" |
| 11 | Fair UX | `potelsaville2024podcast` | transcript page | fair UX | toolkit page: paired with "Distorted UX" |
| 12 | Maps directly to the Gray et al. (2024) ontology of dark patterns | `gray2024ontology` | abstract | 64 synthesized dark pattern types | free copy: https://deceptive.design/articles/an-ontology-of-dark-patterns-knowledge-foundations-definitions-and-a-pathway-for-shared-knowledge-building (page lists metadata only; PAR copy not fetched). The ontology is a separate work with 64 types in three levels |
| 13 | Ten-row dark pattern table: Trick Questions, Roach Motel, Misdirection, Confirmshaming, Disguised Ads, Forced Continuity, Hidden Costs, Bait and Switch | `brignull2010darkpatterns` | to verify | trick questions while filling in a form (guess) | toolkit page: names seen in search summaries of the original list; Brignull's own 2010 page not read |
| 14 | Privacy Zuckering | `brignull2010darkpatterns` | Wikipedia "Dark pattern" | Privacy Zuckering | toolkit page: Wikipedia lists the pattern; Brignull's page unread |
| 15 | Urgency/Scarcity as a pattern type | `brignull2010darkpatterns` | https://www.deceptive.design/types | Fake urgency / Fake scarcity | toolkit page: current site has these as two types; not in the 2010 list as I could read it |
| 16 | Dark patterns as deceptive interfaces that redirect users against their interests | `brignull2010darkpatterns` | definition | carefully crafted to trick users | toolkit page: the 2010 definition was seen only in a search summary |
| 17 | Skill's attribution to *Universal Methods of Ethical Design* | `chivukula2025universal` | to verify | Fair Patterns (guess) | metadata only: book. Publisher page lists no individual method |
| 18 | Step 2.5 Root Cause Reframe | none found | to verify | | not found. Searches: "fair patterns root cause", "dark pattern root cause KPI". Looks like an edbx addition |
| 19 | Step 2.6: GDPR Art. 7(3), right to withdraw consent | `eu2016gdpr` | Art. 7(3) | as easy to withdraw as to give consent | free copy: https://gdpr-info.eu/art-7-gdpr/ |
| 20 | Step 2.6: EU Omnibus Directive 2019/2161 | `eu2019omnibus` | penalties provision | fines of at least 4% of annual turnover | free copy: EUR-Lex CELEX 32019L2161. Fine ceiling is on turnover in the Member States concerned, set by national law; article number (amended UCPD Art. 13) to verify |
| 21 | Step 2.6: DSA Art. 25 and the "named list" of banned patterns for VLOPs | `eu2022dsa` | Art. 25(1)-(3) | deceives or manipulates the recipients of their service | free copy: https://www.springlex.eu/en/packages/dsa/dsa-regulation/article-25/. Text read; the named list is not in it (see Discrepancies) |
| 22 | Step 2.6: DSA fine "up to 6%" | `eu2022dsa` | Art. 52 | 6 % of the annual worldwide turnover | free copy: https://www.springlex.eu/en/packages/dsa/dsa-regulation/article-52/ (summary read via search) |
| 23 | Step 2.6: FTC Act s.5 and the Amazon Prime cancellation case, 2023 | `ftc2023amazon` | press coverage | misleading millions of consumers into enrolling in Prime | metadata only: press. Filed 2023; settled 25 Sept 2025 (USD 1bn penalty + 1.5bn refunds per press); skill omits the outcome |
| 24 | Step 2.6: CCPA s.1798.140 | `ca2020cpra` | s.1798.140(h), (l) | agreement obtained through dark patterns | free copy: https://www.cppa.ca.gov/pdf/enfadvisory202402.pdf (not fetched; summary read). Dark pattern defined in (l); consent definition in (h) |
| 25 | Step 2.6: "UK CMA Digital Markets Act" | `uk2024dmcc` | summaries | Digital Markets, Competition and Consumers Act | free copy: legislation.gov.uk (not opened). The UK instrument is the DMCC Act 2024; CMA fines up to 10% of global turnover from 6 April 2025 |
| 26 | Step 2.6: Brazilian LGPD Art. 9 | `brazil2018lgpd` | Art. 9 | clearly, adequately and ostensively | free copy: https://lgpd-brazil.info/. Art. 9 is a transparency/access right, not a dark-pattern rule; fine ceiling is Art. 52 (2% of Brazilian revenue, R$50m cap) |
| 27 | Step 2.7 Vulnerable Population Harm Matrix | none found | to verify | | not found. Searches: "dark patterns vulnerable populations differential harm". Looks like an edbx addition |
| 28 | Step 3 Default Assessment (harmful / neutral / protective) | `potelsaville2024podcast` | transcript page | harmful default | toolkit page: harmful vs neutral default exists in the taxonomy; the three-colour grading is not |
| 29 | Implementation priority formula (Legal Risk x User Impact) / Effort; Fair Design Statement | none found | to verify | | not found; edbx additions |
| 30 | Hashtags and See Also (Ethical Blueprint, White Hat Design Patterns) | `chivukula2025universal` | to verify | | metadata only: book. The Everyday Ethics methods list (https://everydayethics.uxp2.com/methods, 56 methods) includes White Hat Design Patterns but not Ethical Blueprint, Fair Patterns or Humane Design Guide |

## Licence

- `potelsaville2023fair` (Springer, APF 2023 / 2024 volume): full text behind
  login; no licence on the page I read. Treat as all rights reserved. Paraphrase
  the taxonomy with citation: yes. Reproduce Table 3, category names as a
  table, or diagrams verbatim: no. Ship a modified version: no.
- `lechevalier2025fairness` (Cambridge): CC BY-NC-SA 4.0. Non-commercial and
  share-alike; commercial use needs written permission from Cambridge
  University Press. Blocks pasting its figures or text into this paid bundle.
  Paraphrase with citation is fine.
- `potelsaville2024podcast`: spoken interview, licence not stated. Do not
  reproduce the transcript; paraphrase with citation.
- `fairpatterns2026site`: licence not stated; terms and conditions not read;
  resource library is partly premium. The "Fair Patterns" name is the company's
  brand; whether it is a registered mark is unknown (check before using the
  name as a product label).
- `brignull2010darkpatterns` / deceptive.design: no licence stated; (c) 2026
  Testimonium Ltd; the site asks for appropriate attribution. Use the type
  names with citation; do not copy descriptions verbatim. Wikipedia text is
  CC BY-SA 4.0 (share-alike).
- `brignull2023deceptive`, `chivukula2025universal`: commercial books, no
  licence read; assume all rights reserved.
- `gray2024ontology`: licence not stated on the page I read; unknown. Check
  the ACM and PAR copy. Paraphrase only.
- Statutes and regulations: official texts are public documents, but I did not
  read their reuse terms. Cite and paraphrase; the Springlex copy of the DSA
  says it has no legal effect and the Official Journal text prevails.
- Net: the repo may paraphrase all the above with citation. Two sources
  (Cambridge 2025, CC BY-NC-SA) forbid commercial reuse and require
  share-alike; the Wikipedia text is share-alike. No source here allows shipping
  a modified copy of its text or tables in the paid bundle.

## Discrepancies

Contradicted by the source (I read the source and it says otherwise):

1. DSA "named patterns explicitly banned for VLOPs (pre-checked boxes, repeated
   nagging after declined consent, hiding the cancel option, false urgency,
   confirmshaming)". Art. 25 applies to "providers of online platforms", not
   only very large ones. Its text names none of those patterns: para 1 bans
   deceiving or manipulating interfaces; para 2 excludes practices covered by
   the Unfair Commercial Practices Directive and the GDPR; para 3 lets the
   Commission issue guidance on three practices (prominence of choices,
   repeated requests, harder termination than subscription). Pre-ticked boxes,
   false urgency and confirmshaming do not appear.
2. "Nonobstructive Information": the creators use "non-intrusive information"
   (podcast transcript; Cambridge 2025 Fig. 8).
3. "Summary Path": the creator's transcript says "seamless path".
4. "Protective Default": the creator's transcript says "neutral default" (the
   paper's Table 3, unread, may differ; a search summary of it said
   "protective default").
5. "UK CMA Digital Markets Act": the UK consumer enforcement regime is the
   Digital Markets, Competition and Consumers Act 2024. The Digital Markets Act
   is an EU regulation on gatekeepers.
6. "Urgency/Scarcity" as one type: the current Deceptive Patterns taxonomy
   lists Fake urgency and Fake scarcity separately.

Not found in a readable source (could not read the full source or the pages
say nothing):

7. "Maps directly to the Gray et al. (2024) ontology": the Fair Patterns
   taxonomy paper is dated 2023 and its abstract says it builds on existing
   taxonomies; no readable page links it to the 2024 ontology (64 types, three
   levels), and the skill's ten-row table is not that ontology.
8. The ten-row dark pattern table is presented as "the major dark pattern
   taxonomy"; I could confirm only most names from search summaries of
   Brignull's 2010 list, which also holds items the table omits (Friend Spam,
   Price Comparison Prevention, Sneak into Basket). Brignull's own page was
   not read.
9. The seven fair pattern descriptions in the skill's table ("Reorder visual
   hierarchy so the honest choice is as accessible as the manipulative one",
   etc.): definitions are not in any page I could read; only names and pairings
   come from the podcast transcript.
10. Steps 2.5 (Root Cause Reframe), 2.7 (Vulnerable Population Harm Matrix),
    the three-colour Default Assessment grading, the priority formula and the
    Fair Design Statement: no source found; edbx additions (the skill labels
    only the Evidence Ledger as an adaptation).
11. "Penalty: FTC consent decrees + per-violation fines" and "GDPR up to 4% of
    global turnover": 4% is consistent with commentary; FTC figures not
    checked. The Amazon case outcome (settled 2025) is missing from the skill.
12. The See Also entry "Ethical Blueprint" and the hashtags: not found
    (White Hat Design Patterns exists as a separate method on the Everyday
    Ethics list); book unread. Fair Patterns is not on that 56-method list.

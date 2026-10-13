# Provenance — edbx-anti-heroes

Stage B (anchors checked against `papers/pages/`). One row per element the
skill attributes to a source. Rows with a manifest key carry a page locator
and a verbatim anchor; rows without readable text are marked `metadata only`.

Key finding: the primary sources are open and CC BY-NC-SA 4.0, which blocks
commercial redistribution of verbatim material. The final twelve card names
and their Hero pairs could not be read on any page (they sit in the paper's
card figure, Supplemental Material and the Miro/deck files). Stage B reading
of the PDF: the paper names only five Anti-Heroes (Trap-Setter, Nickling-and-Diming,
Empathy Manipulator, FOMO-Dealer, Puppeteer) and no Hero name at all, so most of the
nine pairs in SKILL.md and `references/cards.md` stay unconfirmed. The text says the
deck has twelve pairs.

## Sources

| Key | Citation | URL / DOI | Free copy | Licence |
|---|---|---|---|---|
| `mehta2024antiheroes` | Mehta, S., Chivukula, S. S., Gray, C. M. and Gairola, R. (2024). *Anti-Heroes: An Ethics-focused Method for Responsible Designer Intentions*. arXiv:2405.03674 (cs.HC), v1, 6 May 2024. Work-in-progress preprint. | doi:10.48550/arXiv.2405.03674; https://arxiv.org/abs/2405.03674; HTML https://arxiv.org/html/2405.03674v1 | yes: https://arxiv.org/abs/2405.03674 | CC BY-NC-SA 4.0 (stated on the arXiv page; the PDF text itself carries only an ACM copyright and permissions notice, no CC statement) |
| `chivukula2025antiheroes` | Chivukula, S. S., Mehta, S., Gray, C. M. and Gairola, R. (2025). *Anti-Heroes: A Role-Based Method to Encourage Ethical Deliberation*. Proceedings of the 2025 ACM Designing Interactive Systems Conference (DIS '25), pp. 3028-3044, ACM. Published 4 July 2025. | doi:10.1145/3715336.3735776; https://dl.acm.org/doi/10.1145/3715336.3735776 | not found (the ACM page returned 403; Crossref lists no licence) | unknown: check ACM page for open-access status |
| `chivukula2025deck` | Chivukula, S. S., Mehta, S. and Gray, C. M. Anti-Hero Card Deck (role cards, three action cards, five Miro activities). | https://www.translate-ethics.com/translate-work/anti-hero-card-deck; Miro: https://miro.com/miroverse/antihero-cards-and-design-activities/ | yes: deck on Miro (a download was not made) | CC BY-NC-SA 4.0 (stated on the translate-ethics page); the Miro page states no licence |
| `pratt2024antiheros` | Pratt Institute work page, "Anti-Heros: An Ethics-focused Method for Responsible Designer Intentions" (Mehta and Chivukula). Status page during playtesting. | https://pratt.edu/work/anti-heros-an-ethics-focused-method-for-responsible-designer-intentions | yes, web page | no licence stated |
| `gray2020asshole` | Gray, C. M., Chivukula, S. S. and Lee, A. (2020). What kind of work do "asshole designers" create? Describing properties of ethical concern on Reddit. DIS '20, pp. 61-73. | doi:10.1145/3357236.3395486 | yes: https://par.nsf.gov/servlets/purl/10168532 (NSF Public Access Repository, accepted manuscript) | not CC: p. 1 of the PDF says copyright is held by the owner/author(s) with publication rights licensed to ACM |
| `gray2021dark` | Gray, C. M., Chivukula, S. S., Melkey, K. and Manocha, R. (2021). Understanding "dark" design roles in computing education. ICER 2021, pp. 225-238. | doi:10.1145/3446871.3469754 | yes: https://par.nsf.gov/servlets/purl/10288114 (NSF PAR, accepted manuscript) | CC BY-NC-SA 4.0 (stated on p. 1 of the PDF) |
| `chivukula2025universal` | Chivukula, S. S. and Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers. ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design | no | all rights reserved, paywalled book |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---|---|---|---|---|
| 1 | Method is Anti-Heroes, a card deck from Mehta, Chivukula, Gray et al. (2024) | `mehta2024antiheroes` | p. 1 | Anti-Heroes: An Ethics-focused Method for Responsible Designer Intentions | Found. Authors on p. 1: Mehta, Chivukula, Gray, Gairola |
| 2 | Helps designers surface their intentions through actions; manipulative and value-centred roles | `mehta2024antiheroes` | p. 1 | surfaces the designer's intentions in an action-focused way | Found in the abstract |
| 3 | Designers balance user, shareholder and business values; choices inscribe values in the product | `mehta2024antiheroes` | p. 2 | value-trade offs between supporting monetary business values and human values | Found. "Inscribe" appears on p. 1 only about ethics-focused methods in general |
| 4 | Aim is to make value trade-offs visible, not to label a designer as bad; most ethics methods teach only "good" practice | `mehta2024antiheroes` | p. 2 | goal of the role cards was not for a designer to choose | Found for the first half: the cards are for engaging with roles, not picking one. "Teach only good practice" is not stated; p. 1 says most methods support ethical decision making and few focus on the designer's own reflection |
| 5 | Each Anti-Hero (manipulative role) is paired with a Hero (value-centred counterpart) on the card's other face | `mehta2024antiheroes` | p. 3 | Hero roles as a value-centered counterpart to each Anti-Hero role | Found; the same page says each card is double-sided |
| 6 | Deck size | `mehta2024antiheroes` | p. 1 | The card deck includes twelve cards with Anti-Hero and Hero faces | Found: twelve role cards (p. 3: 12 Anti-Hero and 12 Hero faces) plus three action cards. SKILL.md and cards.md show nine pairs (Discrepancy 1) |
| 7 | Anti-Hero cards built from earlier "dark roles" and "asshole designer" properties | `mehta2024antiheroes` | p. 2 | identification of dark roles in computing education | Found; p. 3 lists the roles taken from each paper and says they were filtered and combined into 12. Prior work is rows 25 and 26 |
| 8 | Card: Trap-Setter / Empowerer (inescapable task flow / user-chosen paths) | `mehta2024antiheroes` | p. 3 | design concerns related to privacy (e.g., Trap-Setter) | Trap-Setter found, with privacy as its concern. The paper text names no Hero cards, so "Empowerer", the pairing and the "hidden cancel path" gloss are not checkable here (full definitions are in Supplemental Material, not fetched) |
| 9 | Card: Camouflager / Unveiler | `mehta2024antiheroes` | p. 3 | trapsetter, puppeteer, nagger, camouflager, empathy manipulator, cynic | Camouflager is in the list of dark roles the cards were drawn from, not named as a final card. "Unveiler" is not in the text |
| 10 | Card: Empathy Manipulator / Life Coach | `mehta2024antiheroes` | p. 3 | user empathy (e.g., Empathy Manipulator or FOMO-Dealer) | Empathy Manipulator found as a card concerned with user empathy. "Life Coach" appears nowhere in the text |
| 11 | Card: Cynic / Liberator (or Life Coach) | `mehta2024antiheroes` | p. 3 | trapsetter, puppeteer, nagger, camouflager, empathy manipulator, cynic | Cynic is in the dark-roles list only (it is a rationale-focused role in `gray2021dark`). Whether it is a final card, and "Liberator", are not in the text |
| 12 | Card: Nickeling-and-Diming / Transparent Pricer | `mehta2024antiheroes` | p. 3 | payment systems (e.g., Nickling-and-Diming) | Found for payment systems, spelled "Nickling" (also in `gray2020asshole`); SKILL.md spells it "Nickeling". "Transparent Pricer" is not in the text |
| 13 | Card: Black Hat / White Hat | `mehta2024antiheroes` | not in source | filtered and combined similar manipulative roles to construct 12 Anti-Heroes | Not in source: neither "Black Hat" nor "White Hat" appears in the paper, nor among the dark-role and asshole-designer terms it says the cards came from. ("White hat" in `gray2021dark` p. 3 refers to a different practice) |
| 14 | Card: Two-Faced / Consistent Communicator | `mehta2024antiheroes` | p. 3 | including nickling-and diming, two-faced, entrapping, misrepresenting | "Two-faced" is in the asshole-designer property list the cards were drawn from, not named as a card. "Consistent Communicator" is not in the text |
| 15 | Card: Puppeteer / Liberator (or Empowerer) | `mehta2024antiheroes` | p. 3 | user flows or information architecture (e.g., Puppeteer) | Puppeteer found, for user flows and information architecture. Hero names not in the text |
| 16 | Card: Adversary / Ally | `mehta2024antiheroes` | not in source | filtered and combined similar manipulative roles to construct 12 Anti-Heroes | Not in source: neither "Adversary" nor "Ally" appears in any of the three papers read |
| 17 | FOMO-Dealer card (in the paper, absent from SKILL.md) | `mehta2024antiheroes` | p. 3 | Empathy Manipulator or FOMO-Dealer | Found, under user empathy. Not in the SKILL.md deck (Discrepancy 2). `gray2021dark` p. 6 also lists FOMO-Dealer as a puppeteer behaviour |
| 18 | Per-card descriptions and examples (hidden cancel paths, sad mascots, streak warnings, confirmshaming) | `chivukula2025deck` | role cards | Anti-Hero Card Deck | metadata only: no source found. The card text was never fetched and is not in the paper; the examples read as edbx's own illustrations |
| 19 | Three action modes: Evaluation, Reverse Brainstorming, Ethical Dialogue | `mehta2024antiheroes` | p. 3 | Evaluation, Reverse Brainstorming, and Ethical Dialogue | Found (section on action cards; Table 1 is on p. 4) |
| 20 | A fourth mode, "Conceptualization" | `mehta2024antiheroes` | not in source | ideation/conceptualization, evaluation, and ethical dialogue | Not in source: the abstract names three play modes, with ideation and conceptualization together as one; the three action cards are Evaluation, Reverse Brainstorming and Ethical Dialogue. No separate Conceptualization card |
| 21 | "Football referee" use: simulating the action of referees to call out unethical decisions | `mehta2024antiheroes` | p. 2 | simulating a similar action to referees in a football match | Found: raising an Anti-Hero card to call out a decision in a team meeting |
| 22 | Playtesting basis | `mehta2024antiheroes` | p. 1 | four groups of three design students | Found: four sessions of 60 minutes, 12 graduate students (p. 4). The paper calls it a work-in-progress with iteration still planned (p. 6) |
| 23 | Five Miro activities (Trade-Offs Proactive, Anti-Hero and Hero Flows, A Value Switcheroo, Raising the Red Flags, Being an Ethical Investigator) | `chivukula2025deck` | Miro / translate-ethics page | Raising the Red Flags | metadata only: no source found. The pages were not fetched. SKILL.md does not use them |
| 24 | Citation of ACM DIS 2025 version (THIRD_PARTY_NOTICES) | `chivukula2025antiheroes` | title, pp. 3028-3044 | A Role-Based Method to Encourage Ethical Deliberation | metadata only: paywalled (ACM page returned 403; Crossref record only). Different title and author order from the preprint |
| 25 | Further reading: asshole designers on Reddit | `gray2020asshole` | p. 1 | What Kind of Work Do Asshole Designers Create | Found (title) |
| 26 | Further reading: dark design roles in computing education | `gray2021dark` | p. 1 | Understanding Dark Design Roles in Computing Education | Found (title) |
| 27 | "Universal Methods of Ethical Design method profile depicts the deck in use" | `chivukula2025universal` | n/a | Universal Methods of Ethical Design | metadata only: book. Whether the book has an Anti-Heroes profile is not confirmed |
| 28 | Mode procedures (steps, "first three changes I would ship", Hero flips as guardrails, dialogue scripts), 2-5 cards per critique, "necessary friction kept", Evidence Ledger | edbx additions | n/a | Necessary friction kept | metadata only: edbx addition. SKILL.md labels the Evidence Ledger a family convention. The reflective questions in Table 1 (p. 4) are the closest source text for the mode steps; the steps and outputs themselves are not in the paper |

## Licence

- **Preprint `mehta2024antiheroes`: CC BY-NC-SA 4.0.** We may paraphrase and cite. Reproducing its text or figures needs attribution, non-commercial use only, and any adapted material must be shared under the same licence. The repo is MIT and sold in a paid bundle, so **verbatim reuse of the paper's text or figures is not compatible** with commercial redistribution.
- **Card deck `chivukula2025deck`: CC BY-NC-SA 4.0** (Chivukula, Mehta, Gray). Same terms. `references/cards.md` reproduces card names and one-line descriptions; if those match the deck verbatim, they are covered by NC and SA, which **blocks commercial redistribution and modification under MIT**. Card names are short, so a bare list of names with attribution is lower risk than the descriptions. Rewriting the descriptions in our own words and citing the deck is the safest route; ship nothing copied from the card faces.
- **DIS 2025 paper `chivukula2025antiheroes`:** ACM publication, licence unknown. Cite only. Check the ACM page for open-access status.
- **Pratt and Miro pages:** no licence stated. Link, do not copy.
- **Gray et al. 2020 (`gray2020asshole`):** p. 1 of the PDF says copyright is held by the owner/author(s) with publication rights licensed to ACM; cite and link only.
- **Gray et al. 2021 (`gray2021dark`):** p. 1 of the PDF carries a CC BY-NC-SA 4.0 statement (stage A had it as unknown). Same terms as the preprint: attribution, non-commercial, share-alike.
- **Preprint PDF text:** the PDF itself carries only an ACM copyright and permissions notice (p. 1); the CC BY-NC-SA 4.0 statement is from the arXiv page, so check the arXiv page for the licence of record.
- **Universal Methods of Ethical Design:** all rights reserved book; do not reproduce.
- THIRD_PARTY_NOTICES.md lists Anti-Heroes under "Method sources" only, not under "Material under its own licence". Since the deck and preprint carry CC BY-NC-SA, consider adding them to the licensed-material table.

## Discrepancies

### Contradicted by the source text (read on the page)

1. **Deck size.** SKILL.md and `cards.md` list 9 Anti-Hero / Hero pairs; the paper (pp. 1 and 3) says 12 Anti-Hero and 12 Hero faces plus 3 action cards. Yet SKILL.md says "Use only cards from the deck".
2. **FOMO-Dealer omitted.** The paper (p. 3) names FOMO-Dealer under user empathy; SKILL.md omits it.
3. **Spelling.** The paper (p. 3) and `gray2020asshole` spell "Nickling-and-Diming"; SKILL.md has "Nickeling-and-Diming".
4. **Fourth mode.** The paper has three action cards (Evaluation, Reverse Brainstorming, Ethical Dialogue); the abstract groups ideation and conceptualization as one play mode. SKILL.md has four modes, adding Conceptualization as a separate one. Mark it as an edbx addition.
5. **Pairing claims.** `cards.md` says some cards (Cynic, Black Hat, Puppeteer) appear "without an explicitly named Hero pair" in the source. The paper (p. 3) says every Anti-Hero card is double-sided with a Hero counterpart. The multi-Hero pairs ("Liberator (or Life Coach)") are edbx's own.
6. **Black Hat, White Hat, Adversary, Ally** appear in none of the three papers read, nor in the dark-role and asshole-designer lists the paper says the cards were filtered from (p. 3).

### Not verifiable (no readable source)

7. **Hero names and final card list.** The paper text names only five Anti-Heroes and no Heroes; the full 12 are in Supplemental Material and the deck pages, which are not in the manifest. Unconfirmed: Empowerer, Unveiler, Life Coach, Liberator, Transparent Pricer, Consistent Communicator, and whether Camouflager, Cynic and Two-Faced are final cards (they appear only as source roles or properties).
8. **Author order and title of the DIS 2025 version.** The ACM page returned 403. SKILL.md and cards.md cite only the preprint; the 2025 version has a different title and the author order Chivukula, Mehta, Gray, Gairola. Add doi:10.1145/3715336.3735776.
9. **Illustrative detail attributed to the deck.** Sad mascots, streak-loss warnings, "hidden cancel paths" and "fake urgency timers" sit inside card descriptions; the card text was not readable and the examples are not in the paper.
10. **Book profile.** `cards.md` says the deck is "depicted in" a *Universal Methods of Ethical Design* profile; not confirmed.
11. **Teaching only "good" practice** and the Pratt page's framing (row 4): the Pratt page is not in the manifest.
12. **Miro activities and deck licence**: the deck and Miro pages were not fetched, so the CC BY-NC-SA statement for the deck and the five activities are unverified.

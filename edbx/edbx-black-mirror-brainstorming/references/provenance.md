# Provenance — edbx-black-mirror-brainstorming

Stage B (checked against the text in `papers/pages/`, 2026-10-13). One row per
element the skill attributes to a source. Rows whose source is in
`papers/manifest.json` carry a page locator and a verbatim anchor, or
`not in source` where the text was read and the element is absent. Rows for
anything else are `metadata only`, with the reason. `mauldin2018black`
returned 403, so every Mauldin row is metadata only.

## Sources

| Key | Citation | Stable link | Legal free copy | Licence |
|-----|----------|-------------|-----------------|---------|
| `mauldin2018black` | Mauldin, J. (2018). Black Mirror brainstorms — a product design exercise. *UX Collective* (uxdesign.cc, hosted on Medium). | https://uxdesign.cc/black-mirror-brainstorms-f919ccf5938c | Yes, free to read online (the article itself; page returned 403, so no text is available in `papers/pages/`; it was seen only through search excerpts and the secondary summary below) | unknown (see Licence) |
| `klassen2022run` | Klassen, S. & Fiesler, C. (2022). "Run wild a little with your imagination": ethical speculation in computing education with Black Mirror. *Proc. 53rd ACM Technical Symposium on Computer Science Education (SIGCSE '22)*, 836–842. | doi:10.1145/3478431.3499308 | Yes: accepted manuscript at https://par.nsf.gov/biblio/10334675 ; author copy at https://cmci.colorado.edu/~cafi5706/SIGCSE2022_BlackMirror.pdf | Text on p. 1: personal or classroom use free of charge, not for profit or commercial advantage; copyright held by the owner/authors (see Licence) |
| `carlock2021everyday` | Carlock, T. (2021, 18 May). Black Mirror Brainstorming. *Everyday Ethics* methods microsite (secondary summary of Mauldin). | https://everydayethics.uxp2.com/methods/blackmirror-brainstorming/ | Yes (web page) | none stated on page |
| `fiesler2018writers` | Fiesler, C. Black Mirror Writers' Room (classroom exercise); hosted in Mozilla Foundation, Responsible Computing Challenge Playbook, "Black Mirror Writers Room". | https://www.mozillafoundation.org/en/responsible-computing-challenge-playbook/curriculum/black-mirror-writers-room/ | Web page (403 to my fetcher; seen via search excerpts only) | unknown |
| `chivukula2025universal` | Chivukula, S. S. & Gray, C. M. (2025). *Universal Methods of Ethical Design*. Rockport Publishers (Quarto), ISBN 9780760393086. | https://quarto.com/books/9780760393086/universal-methods-of-ethical-design ; companion site https://universalmethodsofethicaldesign.com/ | No (commercial book) | unknown; no licence statement on the companion site |

## Table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | The method: a team exercise, modelled on the TV series, to brainstorm harmful or unintended uses of what it builds | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Free copy: https://uxdesign.cc/black-mirror-brainstorms-f919ccf5938c . Anchor is the title; the description rests on search excerpts and `carlock2021everyday` |
| 2 | "Anti-goals" as the output of the exercise | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Anti-goals appear in search excerpts only |
| 3 | Anti-goal defined as something the team absolutely does not want to happen, counter to its intentions | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Definition seen only in search excerpts |
| 4 | Brainstorm what could go wrong from a starting scenario | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Step 2 of the sequence in `carlock2021everyday` (secondary summary, not a manifest source) |
| 5 | Pitch quote: a line a character might say about the situation | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Step 3 of `carlock2021everyday`. Mauldin's item is a character line; the skill's 2–4 sentence tile blurb is a different thing, though a blurb is what the Writers Room uses (row 11) |
| 6 | Episode framing: who it was meant to help, the well-intended idea, how it went wrong, effect on people around it | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Step 4 of `carlock2021everyday` |
| 7 | Episode poster as the shareable artefact | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Step 5 of `carlock2021everyday`; the original article reportedly names the poster as one of four sections |
| 8 | Four-part structure (brainstorm, quotes, plot points, poster) behind the skill's four outputs | `mauldin2018black` | title | Black Mirror brainstorms — a product design exercise | metadata only: 403. Seen in search excerpts only |
| 9 | Classroom precedent: students speculate about future harms and write episode-style premises ("Black Mirror Writers Room") | `klassen2022run` | p. 1 | creatively speculate about future harms and consequences of current technologies | Abstract. The paper is an interview study of 12 instructors about a classroom exercise, not the origin of the product-team method |
| 10 | Writers Room exercise itself: small groups pick an issue or technology, answer guided questions about future harms, then consider a "Light Mirror" of prevention | `klassen2022run` | p. 2 | students work in small groups to choose an issue or technology | Default form of the exercise as the paper describes it; it ends with an episode blurb, not a three-act arc. `fiesler2018writers` (Mozilla page) was a 403 and is not used |
| 11 | Pitch quote as a Netflix-style blurb, and the Netflix title-card styling of the poster | `klassen2022run` | p. 2 | create an episode blurb using a slide template | The same sentence says the slide template is designed like Netflix episode listings. This supports the Netflix-style blurb and styling as part of the Writers Room, not the HTML poster or the 2–4 sentence length |
| 12 | Three lenses — economic, political, social — "from the source method" | `klassen2022run` | not in source | a primer for ethical, social, and political implications of technology | Not there. The paper has no economic lens and no lens set; the closest passage is an instructor asking for a primer on ethical, social and political implications. Also not found in Mauldin excerpts or `carlock2021everyday` |
| 13 | Same three lenses, as listed in the book (entry no. 10 in the book's method list) | `chivukula2025universal` | entry 10 | Black Mirror Brainstorming | metadata only: book. Cannot be confirmed without the printed book |
| 14 | Example pitch quote ("When your phone unlocks your life…", Thomas) "from the book" | `chivukula2025universal` | entry 10 | When your phone unlocks your life | metadata only: book. A web search for the wording returned nothing |
| 15 | Book classification (Value Posture: Defamiliarising; Action Orientation; Ethical Framework: Consequentialist; Method Input/Mechanic/Output) | `chivukula2025universal` | entry 10 | Value Posture Defamiliarising | metadata only: book |
| 16 | "Adjacent" methods Critical Design, Speculative Design, Timelines | `chivukula2025universal` | method list | Critical Design, Speculative Design, Timelines | metadata only: book. The three titles appear in the companion site's list of 100 methods |
| 17 | Citation line: Klassen & Fiesler (2022), SIGCSE '22, pp. 836–842 | `klassen2022run` | p. 1 | SIGCSE 2022, March 3–5, 2022, Providence, RI, USA | Title, authors, venue, year and DOI match. The text gives "7 pages" and no page range, so 836–842 is consistent but not printed |
| 18 | Three episode variants, one per lens | `none found` | — | Three Black Mirror episode variants | metadata only: no source found. Terms tried: Mauldin "three episodes"; Klassen & Fiesler describe one blurb per group |
| 19 | Three-act arc (beginning, middle, end) per episode | `none found` | — | Three-act arc Beginning Middle End | metadata only: no source found. Klassen & Fiesler p. 2 (and an instructor, p. 2) describe an episode blurb or short screenplay, not an act structure |
| 20 | 8–12 "How could [actor] use [feature] to [harm]" prompts | `none found` | — | How could actor use feature to harm | metadata only: no source found |
| 21 | 6–10 anti-goals, each with Trace and Test; 2–3 "load-bearing" anti-goals | `none found` | — | 6–10 anti-goals Trace Test load-bearing | metadata only: no source found. Klassen & Fiesler never mention anti-goals; Mauldin names them but the excerpts show no count, trace, test or load-bearing selection |

## Licence

- **`mauldin2018black` (Mauldin 2018, UX Collective on Medium).** unknown. I
  could not open the article (403) and found no licence statement in the
  excerpts. Check the page footer and the Medium/UX Collective terms; Medium
  authors normally keep copyright. For this repo: paraphrase the method (yes);
  do not reproduce the article text; step names and the idea of anti-goals are
  fine to paraphrase with credit; a modified version of the method (the
  skill's three-episode, anti-goal-test form) is our own work and is fine so
  long as it is not presented as Mauldin's.
- **`klassen2022run`.** Confirmed in the PDF text (p. 1): permission to copy
  for personal or classroom use without fee, provided copies are not made or
  distributed for profit or commercial advantage; third-party components must be
  honoured; all other uses via the owner/authors, who hold the copyright. No open
  licence. Commercial reuse of text or figures needs permission; paraphrase and
  cite only. Figure 1 is credited to Klassen and Sarder, used with permission.
- **`carlock2021everyday`.** No licence or copyright notice on the page.
  Treat as all rights reserved; paraphrase only, and prefer citing Mauldin
  directly.
- **`fiesler2018writers`.** unknown (Mozilla page not readable; no Creative
  Commons notice found in search excerpts). Check the playbook footer and
  terms of use before reusing any wording or slides. Paraphrase only.
- **`chivukula2025universal`.** Commercial book, no open licence found.
  Paraphrasing the method (yes). Do not reproduce its pitch-quote example,
  classification text or wording verbatim until checked against the printed
  book; the Thomas example in SKILL.md is quoted at length and should be
  treated as a reproduction risk (see Discrepancies).
- **"Black Mirror" name and Netflix look.** The series title is the name of a
  TV programme; the licence status of using it in a product name, and of a
  poster styled as a Netflix title card, is not settled by any source here.
  Check trademark and trade-dress guidance before shipping `assets/poster_template.html`
  in a paid bundle. No source here forbids commercial use of the *method*.
- Nothing found forbids commercial redistribution or modification of the
  method as paraphrased; the open questions are the verbatim quote and the
  brand styling.

## Discrepancies

### Contradicted by the source text

1. **Two different exercises are cited as one method.** SKILL.md says the
   method is "Klassen & Fiesler, 2022; Mauldin, 2018". The Klassen & Fiesler
   text (p. 1) describes a classroom Writers Room exercise created by Fiesler
   and studied through interviews with 12 instructors. It never mentions
   Mauldin, brainstorming for products or anti-goals, so it is not a source for
   the product-team method. (fixed in SKILL.md)
2. **Economic / political / social lenses.** SKILL.md says the lenses "come
   from the source method". The Klassen & Fiesler text has no such lens set
   (row 12). (fixed in SKILL.md)
3. **Anti-goals.** The method in SKILL.md is credited in part to Klassen &
   Fiesler, whose text never uses the term (the term is Mauldin's, unreadable). (fixed in SKILL.md)
4. **Pitch quote vs blurb.** Mauldin's step (secondary summary) is a line a
   character might say. The Writers Room as Klassen & Fiesler describe it ends
   in an episode blurb on a Netflix-style slide (p. 2). So the Netflix-style
   blurb and title-card styling have a source in the Writers Room; only the
   2–4 sentence length is unsourced. (fixed in SKILL.md)

### Not verifiable

5. **Mauldin steps the skill omits.** Sharing the posters, finding common
   patterns, giving feedback, reflecting on links to current work; the
   "well-intended idea" framing question; groups of 3–4 with about 15 minutes
   of sketching and 5 minutes to define anti-goals. From secondary summaries
   only (Mauldin returned 403).
6. **Single self-contained HTML poster** is an edbx format choice; Mauldin's
   poster is a hand-made team artefact (summary only). (fixed in SKILL.md)
7. **Three episodes, three-act arc, 8–12 prompts, 6–10 anti-goals with Trace
   and Test, and "load-bearing" anti-goals** have no readable source (rows
   18–21). They look like edbx design choices; SKILL.md should mark them as
   skill additions. (fixed in SKILL.md)
8. **Incomplete citation.** "Mauldin, J. (2018). Black mirror brainstorms: a
   product design exercise." omits the venue (UX Collective) and URL, and the
   title wording differs from the article title. The book is named without
   authors, year or publisher (Chivukula & Gray, 2025, Rockport). (fixed in SKILL.md)
9. **Long verbatim quote.** The "Thomas" pitch quote is attributed to the
   book. It could not be found online; verify it is the book's text and
   consider replacing it with an original example (copyright). (fixed in SKILL.md)
10. **Book classification line** (Value Posture, Ethical Framework, etc.) and
    the lens claim as attributed to the book cannot be confirmed without the
    book. (fixed in SKILL.md)
11. **Licence of the Mauldin article** is unknown (page unreadable).

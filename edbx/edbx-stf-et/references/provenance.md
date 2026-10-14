# Provenance — edbx-stf-et

Stage B (2026-10-13). One row per element the skill attributes to a source.
The one manifest source is `travaglianti2025ethics`, a single fetched web page
(`papers/pages/travaglianti2025ethics/001.txt`, the landing page; the PDF and
Mural sit behind an access form and were not fetched). Locator `web` means the
anchor was copied verbatim from that page; `not in source` means the page was
read and the element is absent (the anchor is the closest passage). Sources
not in the manifest are `metadata only`.

**Headline: the fetched page contains no licence statement of any kind (no
"CC BY", "Creative Commons" or "licence"). Its only rights text is the footer
"(c) Stanford University" and a "Copyright" link whose target was not fetched.
The "CC BY 4.0" claim in SKILL.md, `references/value-cards.md` and
`THIRD_PARTY_NOTICES.md` is therefore not confirmed by anything fetched (see
Licence). The page text also carries none of the toolkit's detail (phases,
version, value names, spectra, worksheet sections), so most element-level
claims are `not in source`.**

## Sources

| Key | Full citation | URL | Free copy | Licence |
|---|---|---|---|---|
| `travaglianti2025ethics` | Travaglianti, M. & Both, T. (2025). *Ethics Toolkit*. McCoy Family Center for Ethics in Society, Stanford University; funded by the Project Liberty Institute. Year inferred from image file names ("ethics-toolkit-2025"); no version number on the page. | https://ethicsinsociety.stanford.edu/tech-ethics/ethics-toolkit (https://ethicstoolkit.stanford.edu redirects here, HTTP 307) | landing page: yes. Full toolkit: PDF or Mural free on request through an access form (not submitted, not downloaded): https://docs.google.com/forms/d/e/1FAIpQLSdYry2TYzXTqtFRYfOw414Yy8OUJhhp6BBnvaeCo5whIMu1NQ/viewform?usp=header | none stated on the landing page. Footer: "© Stanford University". The PDF's own terms were not readable. Treat as unknown |
| `adams1991storyspine` (not in manifest; not fetched) | Adams, K. (1991). The Story Spine. Kenn Adams, artistic director of Synergy Theater (date and attribution per SessionLab's method page). | https://www.sessionlab.com/methods/story-spine | yes, web page (secondary description) | no licence stated for the method (SessionLab page: "©2026 TrainedOn OÜ" site notice) |
| `glenn2009futures` (not in manifest; not fetched) | Glenn, J. C. The Futures Wheel, devised 1971 (invented at Antioch Graduate School of Education per Wikipedia and Graz TU descriptions; Mind Tools says 1972). Fuller description: Glenn, J. C. (2009), *Futures Research Methodology* v3.0, The Millennium Project (cited by the Graz TU page; not opened). | https://en.wikipedia.org/wiki/Futures_wheel ; https://www.tugraz.at/en/projekte/z-t-g/methods/futures-wheel | probably yes via the Millennium Project; not confirmed | unknown |

## Provenance table

| # | Skill element | Source | Locator | Anchor phrase | Note |
|---|---------------|--------|---------|---------------|------|
| 1 | Toolkit identity: Stanford McCoy Family Center, "Ethics Toolkit", a pragmatic, society-centred framework of five tools | `travaglianti2025ethics` | web | built for academics and professionals alike | Page also describes a "pragmatic, society-centered mindset" and names the creators (Travaglianti, Both) and funder (Project Liberty Institute), which SKILL.md omits |
| 2 | Version "V1.1, 2025" and the tagline "Put Values Into Action" | `travaglianti2025ethics` | not in source | put values into action in your research and work | The words appear only in running prose, not as a tagline or title. No version number and no year on the page text |
| 3 | Five tools: Future Story, Impacts Explorer, Ethics Frame, Ethics Gauge, Weighing Options | `travaglianti2025ethics` | web | The Toolkit consists of five simple, actionable tools | All five names are listed in this order, followed by a sixth item, Values Explainer Cards |
| 4 | Three phases Explore -> Evaluate -> Decide, with the tool-to-phase assignment 2 / 2 / 1 | `travaglianti2025ethics` | not in source | explore the impacts of your work, assess their ethical implications | The page text has no phase labels and no grouping of tools. Closest passage: the toolkit helps you explore impacts, assess ethical implications and plan actions. Stage A's phase labels and 3 / 1 / 1 grouping (from image alt text and list order) are not in the fetched text |
| 5 | Future Story: look back from the future to imagine impacts | `travaglianti2025ethics` | web | looking back from the future, to imagine implications | Page: "Write the story of your work, looking back from the future..." |
| 6 | Future Story built on Kenn Adams' Story Spine; six elements with the prompts "Once upon a time...", "Until one day...", "And because of that...", "But also...", "In turn...", "One thing we could have done differently is..." | `adams1991storyspine` | n/a | adapted from Kenn Adams' Story Spine | metadata only: not in manifest; secondary description read in stage A. The fetched Stanford page names neither Adams nor a spine, and shows no prompts. Stage A: SessionLab's spine prompts differ from the skill's |
| 7 | Impacts Explorer: effects on people and society and how related values are promoted or degraded | `travaglianti2025ethics` | web | how related ethical values are promoted or degraded | Confirmed |
| 8 | Impacts Explorer builds on the Futures Wheel; In-to-Out and Out-to-In directions; group-specific lens | `glenn2009futures` | n/a | Builds on the Futures Wheel technique | metadata only: not in manifest; secondary description read in stage A. The fetched Stanford page does not mention the Futures Wheel, directions or a group lens |
| 9 | Ethics Frame: a single worksheet; nine sections (Action, Values part one, Benefits, Harms, Who is affected, Values part two, Expand benefits, Reduce harms, Bottom line) | `travaglianti2025ethics` | web | A single worksheet to outline ethical considerations | One-line description confirmed. The nine sections and their order are not on the page (PDF only) |
| 10 | Benefit and harm extent dimensions: magnitude, scope, likelihood, duration | `travaglianti2025ethics` | not in source | Consider effects on people and society | Not on the page. Closest passage is the Impacts Explorer one-liner |
| 11 | Ethics Gauge: assessment at a more granular level; four dimensions (beneficial, harmful, fair, empowering), each with three spectra scored - to + | `travaglianti2025ethics` | web | across multiple considerations | One-line description confirmed (a more granular level, multiple considerations). The four dimensions and twelve spectra are not on the page |
| 12 | Weighing Options: compare options, effects on society and organization; sections Current Situation, Option description, Societal impact, Organizational impact, Obstacles, "what are you prioritizing", Future Direction | `travaglianti2025ethics` | web | considering the effects on society and your organization | One-line description confirmed. Section names are not on the page |
| 13 | Value Explainer Cards: nine values (Well-being, Justice, Trust, Privacy, Dignity, Virtues, Autonomy, Responsibility, Relationships) | `travaglianti2025ethics` | not in source | Understand ethical values, and consider those at play | The page lists "Values Explainer Cards" as a sixth item with this one-liner and names no value. Stage A saw a "Well-Being and Justice" card image; its text is not in the fetched text |
| 14 | Each card = definition + three observable spectra (degrading vs promoting); card wording in references/value-cards.md | `travaglianti2025ethics` | not in source | Use these with the other tools to deepen your analysis | No card text or spectra on the page. If value-cards.md copies card text from the PDF, see Licence |
| 15 | "Creating your own value card" template (name, definition, three spectra) | `travaglianti2025ethics` | not in source | guidance or advice in adapting the tools to your context | Not on the page. The page only offers adaptation guidance on request via a contact form. Likely an edbx addition |
| 16 | Core premise: ethics is everyone's responsibility and a shared societal undertaking; the tools do not say what is right; "what the tools do / don't do" lists in three-phases.md | `travaglianti2025ethics` | web | Ethics is everyone's responsibility, a shared societal undertaking | Premise confirmed. "The tools do not say what is right" and the do / don't lists are not on the page |
| 17 | "Chain" framing: tools feed each other; enter anywhere; loop back; time budgets (20-30 min up to a half-day) | `travaglianti2025ethics` | not in source | Select the tools that serve your needs | The page invites picking the tools you need (consistent with "enter anywhere") but does not use the word chain, describe feeding between tools, looping back, or give time budgets |
| 18 | Mandatory "-> Carries forward to Tool N" hand-off blocks | `travaglianti2025ethics` | not in source | enable you and your teams to explore the impacts of your work | Not on the page. SKILL.md presents the blocks as part of the method ("the handoff that makes the chain work"); they look like an edbx layer |
| 19 | Four worksheet templates in assets/ (future story, ethics frame, ethics gauge, weighing options) | `travaglianti2025ethics` | not in source | To download a PDF or Mural version of the toolkit | The page shows no worksheets; the PDF / Mural is behind an access form and was not fetched, so layout or wording fidelity of the templates cannot be checked |
| 20 | Quality-bar counts (e.g. at least 3 direct effects, 2 secondary per direct, 3 values) and Evidence Ledger | `none` | n/a | the Evidence Ledger is a family convention from fdbx | metadata only: edbx addition. SKILL.md declares the Evidence Ledger an fdbx convention; the quality-bar counts are not labelled |
| 21 | Licence line in SKILL.md: "Licensed CC BY 4.0 - ethicstoolkit.stanford.edu" | `travaglianti2025ethics` | not in source | Stanford University. Stanford, California 94305 | No licence statement on the page. The footer carries "(c) Stanford University" and a "Copyright" link (target not fetched). See Licence |

## Licence

- **Stage B result for `travaglianti2025ethics`: no licence statement appears in the fetched Stanford page.** Searched the extracted text for licence, Creative Commons, CC BY, copyright and rights: the only hits are the footer links "Terms of Use", "Privacy", "Copyright", "Trademarks" and the line "(c) Stanford University." No open licence of any kind is stated. The PDF / Mural (behind an access form) was not fetched, so its terms remain unknown.
- **`travaglianti2025ethics`: unknown.** SKILL.md (line 11), `references/value-cards.md` and `THIRD_PARTY_NOTICES.md` state "CC BY 4.0 — ethicstoolkit.stanford.edu". On the landing page I searched for licence, Creative Commons and CC BY and found nothing; the only rights text is "© Stanford University" and a copyright-infringement link. The site that name points to redirects to the same page. The access-form route (PDF / Mural on request) suggests the terms, if any, are inside the PDF, which could not be read. What it would mean:
  - **If the PDF is CC BY 4.0:** paraphrasing, verbatim reuse of card text, worksheets and diagrams, and shipping modified versions in a paid bundle are all allowed with attribution, a licence link and a note of changes. No block.
  - **If the PDF has no open licence (default "© Stanford"):** paraphrasing the method is fine. Reproducing the nine value cards verbatim (references/value-cards.md), the four worksheet templates, or the tool wording closely is not permitted without permission. That would block commercial redistribution of those files in a paid bundle.
  - Until checked, do not repeat "CC BY 4.0" as fact; mark it unverified. The card text and templates are the highest-risk files. Check the PDF's colophon or contact the Center (the page offers a contact form for adaptation guidance, https://docs.google.com/forms/d/e/1FAIpQLScTtQAIW68qK5qOBAiyeghxRLo0-nopxDLFpz42-RTuyrgeFA/viewform).
- **`adams1991storyspine`.** No licence stated. The six-prompt spine in SKILL.md is the toolkit's adaptation; paraphrase only, credit Adams.
- **`glenn2009futures`.** Unknown. A method idea; paraphrase and credit Glenn.
- Nothing found forbids commercial use or modification. The open question is whether any permission exists at all for verbatim card text and worksheets.

## Discrepancies

### Contradicted by the source text (read on the fetched page)

None confirmed. The fetched text is a landing page and says little about the method's internals, so it neither supports nor contradicts most of the skill's content.

### Not verifiable (no readable source; the full toolkit is a PDF / Mural behind an access form)

1. **Licence "CC BY 4.0".** Stated as fact in SKILL.md, `references/value-cards.md` and `THIRD_PARTY_NOTICES.md`. The fetched page has no licence statement; its only rights text is "(c) Stanford University." Treat as unverified until the PDF's terms are read or Stanford confirms. (fixed in SKILL.md)
2. **Phases and tool-to-phase grouping** (rows 4). The fetched text has no phase labels or grouping, so stage A's weak finding (3 / 1 / 1, "Make Decisions") rests on image alt text and is not in the text. Stage A's "contradicted" item is withdrawn and recorded here. (fixed in SKILL.md)
3. **"V1.1", the year 2025 and the tagline "Put Values Into Action"** (row 2): no version or year in the page text; the words occur only in prose. (fixed in SKILL.md)
4. **All nine value names, card definitions and spectra** (rows 13-15). The page names only "Values Explainer Cards".
5. **Ethics Frame's nine sections, extent dimensions, the Gauge's four dimensions and twelve spectra, Weighing Options' sub-sections** (rows 9-12): one-line descriptions only.
6. **Future Story's six-element spine and prompts, the Adams credit, the Futures Wheel basis, In-to-Out / Out-to-In directions and the group lens** (rows 6, 8): not on the page; Adams and Glenn are not in the manifest. (fixed in SKILL.md)
7. **Chain framing, time budgets, do / don't lists, feed-forward blocks, quality-bar counts, the "create your own value card" template** (rows 15-18, 20): not on the page; probably edbx layers presented in SKILL.md as the method's own. (fixed in SKILL.md)
8. **Creators and funder omitted.** Not a contradiction: SKILL.md credits only the Center; the page names Manuela Travaglianti (project lead), Thomas Both (designer) and the Project Liberty Institute. (fixed in SKILL.md)

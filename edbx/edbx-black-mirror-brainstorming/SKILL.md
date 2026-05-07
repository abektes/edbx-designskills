---
name: edbx-black-mirror-brainstorming
description: Use when a user wants to pressure-test a product, feature, or concept for ethical risk; explore "what could go wrong"; do critical/speculative design; run a Black Mirror-style brainstorm or anti-goal workshop; build a Black Mirror "episode" pitch around a design; or surface dystopian misuse scenarios before shipping. Trigger even when the user asks vaguely about "unintended consequences," "dark patterns waiting to happen," "harm anticipation," or "ethical red-teaming" of a feature. Speculative, anti-goal ideation for digital products and services in the spirit of the Black Mirror Netflix series. Take on the role of a science fiction filmmaker to imagine how a product could be misused or cause unintended harm — across economic, political, and social dimensions — and turn those stories into concrete anti-goals the team can design against.
metadata:
  version: "1.0"
---

# Black Mirror Brainstorming

## What this skill does

Black Mirror Brainstorming is a speculative-design method (Klassen & Fiesler, 2022; Mauldin, 2018; published in *Universal Methods of Ethical Design*) that asks the team to put on a science-fiction filmmaker's hat and imagine how a product could be twisted, abused, or quietly corroded by the world it lands in.

The point is not entertainment. The point is to convert vivid, character-driven worst cases into **anti-goals** — specific things the team commits to *not* let happen — so they can be designed against the same way real goals are.

A complete run of this skill produces four linked outputs:

1. A **what-could-go-wrong brainstorm** across economic, political, and social dimensions.
2. **Three Black Mirror episode variants** — different plots, different harms, different protagonists — each with characters, scene, three-act arc, and a pitch quote.
3. A **pitch poster** (HTML, single file) for the strongest episode, styled like a Netflix title card with the quote.
4. A list of **anti-goals as testable design constraints**, traceable back to the episodes that surfaced them.

## When to use this skill

Reach for this when:

- A team is about to commit to a feature or product direction and wants to pressure-test it for harm before shipping.
- An existing concept feels "too clean" in reviews — nobody is naming the failure modes.
- The team has done positive ideation (jobs, journeys, personas) and now needs the negative-space counterpart.
- Stakeholders ask for an "ethics review" but you want something more generative than a checklist.
- A retro on a near-miss or actual harm wants to be turned into reusable design constraints.

This skill does *not* replace formal harms analysis, threat modeling, or red-teaming with affected communities. It is a generative front-end that produces material those processes can build on.

## Inputs

Ask the user for as many of these as you can get. If they offer none, ask for at least the first two before drafting:

- **The design concept** in one or two sentences (what it is, what it is meant to do).
- **The setting / launch context** — geography, audience, regulatory climate, who pays, who is on the platform vs. who is affected by it.
- **Known unknowns** the team is already worried about (good seed material).
- **Adjacent products or precedents** worth riffing on (e.g. "like Strava but for medication adherence").
- **Out-of-scope harms** the user explicitly does not want to dwell on (so the work stays useful).

If the concept is vague, narrow it to a concrete v1 before generating. Speculative fiction needs something specific to twist.

## Workflow

Default to running all four steps. If the user only wants part of it (e.g. "just give me the anti-goals, skip the poster"), keep the upstream steps internally — anti-goals without their stories tend to be generic.

### 1. Brainstorm what could go wrong

Generate 8–12 short "what if" prompts grouped under three lenses. The lenses come from the source method and exist to stop the team from reaching only for the most obvious harm:

- **Economic** — bad-faith actors, scams, predatory pricing, attention extraction, value capture flowing the wrong way.
- **Political** — surveillance, identification of dissidents, voter manipulation, regulatory capture, geopolitical use.
- **Social** — amplification of existing divides, isolation, status games, pressure on minors or vulnerable groups, erosion of offline norms.

Each item is one sentence in the form *"How could [actor] use [feature] to [harm]?"* — phrased as a question, because the team will ideate against it next. Tag each with its lens.

This is a generative pass, not a triage pass. Do not self-censor for "would this really happen" — the unrealistic ones still pull the realistic ones into view.

### 2. Generate three Black Mirror episode variants

Pick three of the strongest "what ifs" — ideally one from each lens — and develop each into a short episode. Different plots, different protagonists, different harms. Three is the right number: one episode reads as an opinion, three reads as a pattern.

For each episode produce:

- **Title** — short, memorable, slightly chilling. Two to four words.
- **Characters** — Protagonist, Antagonist, and one or two Supporting Characters. Give names, brief context. The antagonist can be a person, an institution, or the system itself.
- **Context / Scene** — the specific setting where the design concept lives. Be concrete: a city, a workplace, a year.
- **Three-act arc** — Beginning (early conflict; the design works as intended), Middle (rising action; the design starts to bend), End (climax; the harm crystallises and lands on someone).
- **Pitch quote** — a Netflix-style 2–4 sentence blurb in the second person or close third, the kind that would appear under the episode tile. The example from the book reads:
  > "When your phone unlocks your life, it more than sucks when you lose it. No one knows this better than Thomas. He cannot open his car, get into his home, or enter his job. Stranded in his own city and isolated from his own life, Thomas turns to the digital outcasts of society in order to find his way back to it."

Keep episodes plausible enough that a designer reading them recognises real mechanisms. Fully fantastical sci-fi loses its bite.

### 3. Build a pitch poster for the strongest episode

Pick whichever episode lands hardest — the one a reader would forward to a teammate. Render it as a single self-contained HTML file (a "poster") that mocks up a Netflix-style title card:

- Episode title prominent.
- Pitch quote prominent below the title.
- A short "starring" line listing the protagonist, antagonist, and one supporting character.
- A "directed by" or "based on" line crediting the design concept itself.
- A muted, slightly off colour palette — this is meant to feel like a cautionary trailer card, not a launch banner.
- No external assets. Pure HTML/CSS, single file, opens in any browser. See `assets/poster_template.html` for a starting structure.

The poster's job is to make the episode shareable inside the team. People remember a poster; they forget a bullet point.

### 4. Derive anti-goals as design constraints

Read back across all three episodes and the brainstorm. Pull out **6–10 anti-goals**. Each one should look like:

- **Anti-goal:** A short statement of the thing the team commits not to allow. Phrased actively (e.g. "Account recovery never requires re-entering the physical world the user is locked out of").
- **Trace:** Which episode(s) and which moment in the arc surfaced it.
- **Test:** A concrete thing the team could check, build, or measure to know whether the anti-goal is being upheld. If you cannot suggest a test, the anti-goal is probably too vague — sharpen it.

Anti-goals should be specific enough to *fail*. "Don't be evil" is not an anti-goal; "single points of failure in identity recovery must have an offline fallback that does not require a phone, a charged device, or a working account" is.

End the deliverable by flagging which 2–3 anti-goals the team should treat as **load-bearing** — i.e. ones that, if violated, would invalidate the whole concept. These are the ones worth raising with leadership before shipping.

## Output format

Default to a single Markdown worksheet plus a sibling HTML poster file. Use this exact structure so downstream consumers (decks, briefs, ADRs) can lift sections cleanly.

```markdown
# Black Mirror Brainstorming — [Concept Name]

## Concept under examination
One- or two-sentence restatement of the concept and its launch context.

## What could go wrong
### Economic
- How could [actor] use [feature] to [harm]?
- ...
### Political
- ...
### Social
- ...

## Episode 1 — [TITLE]
**Lens:** Economic / Political / Social
**Characters:**
- Protagonist: [name, one-line context]
- Antagonist: [name or institution, one-line context]
- Supporting: [name, one-line context]

**Context / Scene:** [specific setting]

**Beginning — Early conflict:** [2–4 sentences]
**Middle — Rising action:** [2–4 sentences]
**End — Climax:** [2–4 sentences]

**Pitch quote:**
> [2–4 sentence Netflix-style blurb]

## Episode 2 — [TITLE]
[same structure]

## Episode 3 — [TITLE]
[same structure]

## Featured poster
The strongest episode is [TITLE]. See `assets/poster_template.html` for the base structure; render the final poster as `[concept-slug]-poster.html` in the same directory.

## Anti-goals
1. **[Statement]** — *Trace:* Episode N, [moment]. *Test:* [concrete check].
2. ...

## Load-bearing anti-goals
The 2–3 anti-goals from the list above that, if violated, would invalidate the concept:
- ...
```

The HTML poster is rendered using `assets/poster_template.html` as a base and saved as `[concept-slug]-poster.html` in the same directory as the Markdown worksheet.

## Prompt patterns to reuse

Use or adapt these when generating each section:

- **Generating the brainstorm:** "Across economic, political, and social lenses, list 8–12 short 'How could [actor] use [feature] to [harm]?' questions for this concept. Mix obvious and non-obvious."
- **Selecting episodes:** "Of these brainstorm items, pick the three that surface the most distinct mechanisms of harm — not the three most dramatic."
- **Drafting an episode:** "Write a Black Mirror episode for this what-if. Give it a title, three named characters, a concrete setting, a three-act arc, and a Netflix-style pitch quote. Keep it plausible — a designer should recognise real mechanisms."
- **Drafting the pitch quote:** "Write a 2–4 sentence Netflix tile blurb for this episode in close third or second person. Set the situation, name the protagonist, end on the trap closing."
- **Deriving anti-goals:** "Read across these three episodes. List 6–10 anti-goals: each is one statement, traced to the episode and arc moment that surfaced it, with one concrete test the team could run."
- **Calling out load-bearing anti-goals:** "Of these anti-goals, which 2–3 would invalidate the entire concept if violated? Those go to leadership."

## Guardrails

- **Don't moralise.** The skill is generative, not preachy. Show the failure mode through story; let the team draw the conclusion. A worksheet that lectures gets ignored.
- **Stay plausible.** Fully fantastical futures (sentient AI overlords) are easy to dismiss. The strongest episodes use mechanisms that already exist somewhere, just turned up.
- **Write people, not roles.** "Thomas, a 34-year-old courier in Atlanta" travels further than "the user." Specificity is what makes the pitch quote land.
- **Don't conflate harm types.** Keep the three lenses distinct in the brainstorm. If every "what if" reads as a privacy concern, push back into the political and economic columns.
- **Avoid identifying real, named individuals** in episodes — use composite or invented characters. The method is about systemic dynamics, not callouts.
- **Don't skip the anti-goals.** Episodes are the bait; anti-goals are the catch. A run that ends at "look how dark this could be" without producing constraints is incomplete.
- **Be careful with vulnerable groups.** When an episode involves minors, abuse survivors, undocumented people, or others at heightened risk, keep the focus on the *system's* failure rather than dwelling on graphic detail. The harm should be legible without being pornographic.

## Quality bar

A good run:

- Produces 8–12 brainstorm items spread across all three lenses (not bunched in one).
- Yields three episodes that are mechanistically distinct (not three flavours of "data leaks happen").
- Has at least one episode whose pitch quote a designer would actually quote back later.
- Ships a poster that opens cleanly in a browser with no broken layout or external requests.
- Ends with anti-goals that are specific enough to fail — each with a concrete test.
- Identifies which anti-goals are load-bearing.

## See also

In the broader *Universal Methods of Ethical Design* family, this method is adjacent to **Critical Design**, **Speculative Design**, and **Timelines**. The book classifies it as: *Value Posture: Defamiliarising · Action Orientation: Evaluating, Framing · Ethical Framework: Consequentialist · Method Input: Stakeholder Info, Constraints/Goals, Use Context · Method Mechanic: Storytelling, Mapping · Method Output: Constraints/Goals.*

References:
- Klassen, S. & Fiesler, C. (2022). "Run wild a little with your imagination": ethical speculation in computing education with black mirror. *Proceedings of the 53rd ACM Technical Symposium on Computer Science Education*, 836–842.
- Mauldin, J. (2018). Black mirror brainstorms: a product design exercise.

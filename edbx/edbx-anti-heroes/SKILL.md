---
name: edbx-anti-heroes
description: Use when a designer needs to critique a design, flow, feature, or concept for dark patterns and anti-user values, run reverse brainstorming to expose worst-possible solutions, generate ethical concept alternatives, or facilitate ethical dialogue in a team using shared Anti-Hero / Hero language. Use the Anti-Heroes card method to surface manipulative design intentions and pair them with ethical Hero counterparts. Lean toward this skill whenever the user mentions dark patterns, manipulative design, deceptive UX, ethical review, anti-patterns, designer responsibility, or wants to "break my design" before shipping.
version: "1.0"
tags: [ethical-design, forecast]
---

# Anti-Heroes

## Overview

Designers continuously balance user, shareholder, and business values, and the design choices they make inscribe those values into the product. The Anti-Heroes method, from Mehta, Chivukula, Gray, et al. (2024), exposes the manipulative roles a designer can play (Anti-Heroes) and pairs each with the ethical role that counters it (Hero). The point is not to label a designer as bad; it is to make the value trade-off visible so the team can choose differently.

Use this skill to put designs through a Hero / Anti-Hero check, generate worst-possible solutions on purpose, develop ethical concept alternatives, or facilitate a team conversation that names manipulative moves out loud instead of letting them slide.

The published deck has twelve double-sided role cards (an Anti-Hero on one face, its Hero on the other) and three action cards (Evaluation, Reverse Brainstorming, Ethical Dialogue). The paper names only five of the twelve Anti-Heroes and none of the Heroes, so this skill works from a working card list of ten pairs; [references/cards.md](references/cards.md) says which names the paper confirms and which it does not. Read that file whenever the user asks for a critique, a reverse brainstorm, or wants the deck explained — most use cases need at least a few specific cards named, not just "this looks dark-pattern-y."

## Use This Skill When

- A team wants to evaluate a design, flow, feature, or concept for manipulative or anti-user patterns before shipping.
- A reviewer wants principled language for what feels off about a design instead of vague "this seems gross."
- A team is doing reverse brainstorming and wants to deliberately design the worst version to surface anti-goals.
- A designer wants to generate ethical concept alternatives that counter an Anti-Hero pattern they have already noticed.
- A team meeting needs a shared vocabulary to call out manipulative moves respectfully (the "football referee" use described in the source).
- A discovery team is reviewing competitor or industry trends for ethically problematic patterns to avoid.

## Inputs

Provide as many of these as are available:

- the design under review: screenshot, wireframe, flow description, copy, prototype link, or a verbal walkthrough
- the user's primary goal in this design and the user's likely emotional state
- the business goal or stakeholder pressure behind the design
- any specific Anti-Hero or Hero card the user wants to focus on
- the use mode the user wants: evaluation, reverse brainstorm, conceptualization, or ethical dialogue
- constraints that genuinely cannot move (regulation, hard business deadlines, accessibility minimums)

If the user has not said which mode they want, infer it from how they describe the task and confirm in one short sentence before going deep.

## The Four Modes

The published deck has three action cards, which are three play modes: Evaluation, Reverse Brainstorming and Ethical Dialogue. This skill adds a fourth, Conceptualization. All four share the same card vocabulary but produce different outputs.

### Mode 1: Evaluation

Critique an existing design and identify which Anti-Hero patterns are present, then propose the matching Hero moves.

1. Restate the design's required user task and the user's likely emotional state.
2. Walk the design and tag each suspicious element with a candidate Anti-Hero card (Trap-Setter, Empathy Manipulator, Nickling-and-Diming, etc.). Cite the specific UI moment, copy, or interaction — not vibes.
3. For each tag, name the Hero counterpart and describe one concrete change that flips the move.
4. Note where Anti-Hero patterns are unavoidable (e.g., a regulator-required friction step) so the team does not over-correct.
5. Hand back: list of Anti-Hero hits, Hero counter-moves, and a short risk note.

### Mode 2: Reverse brainstorming

Deliberately design the worst possible version to surface anti-goals before they sneak in by accident.

1. Pick 2–4 Anti-Hero cards that are most plausible for this product or feature.
2. For each card, generate one or two worst-version moves the design could make. Be specific: what does the screen, copy, or flow actually do?
3. Cluster the worst moves into anti-goals ("we are pushing the user toward X by exploiting Y").
4. Flip every anti-goal into a Hero move and a guardrail.
5. Hand back: anti-goals named, Hero flips, and watch-outs for a future review.

### Mode 3: Conceptualization

> **edbx adaptation:** Conceptualization as a separate mode is not part of the published method; the paper's action cards are Evaluation, Reverse Brainstorming and Ethical Dialogue, and it names ideation and conceptualization only as a setting the deck is played in. This mode is here because designers shaping a new concept need the Hero cards as prompts, not only as fixes.

Use Hero / Anti-Hero pairs as generative prompts when shaping a new concept.

1. Frame the concept and the user value it claims to deliver.
2. Pick 2–3 Hero cards relevant to the value proposition (e.g., Empowerer, Liberator, Life Coach) and sketch a concept move that embodies each.
3. Stress-test each Hero move by naming the Anti-Hero version it could slide into under business pressure.
4. Adjust the concept to make the Anti-Hero slide harder or impossible (defaults, copy, incentives, dark-launch metrics).
5. Hand back: 2–3 concept directions, each with the Hero move, the Anti-Hero risk, and the design that prevents the slide.

### Mode 4: Ethical dialogue

Help a team talk about an ethically charged design without finger-pointing.

1. Restate the user's task and emotional state, what is being discussed, and what is at stake for them.
2. Offer 2–3 Anti-Hero cards as candidate names for the move under discussion, with the wording the team can use ("this feels like a Trap-Setter — once a user is in, the off-ramp is hidden").
3. Offer the matching Hero card as a constructive counter ("the Empowerer version of this would be …").
4. Suggest a short script the team can use in the meeting itself ("I want to call a Trap-Setter on this — can we look at the cancel flow together?").
5. Hand back: candidate cards, dialogue scripts, one or two follow-up questions to keep the conversation moving forward, and one concrete design change the team could prototype before the meeting.

## Workflow

Regardless of mode, follow this overall arc:

1. **Detect the mode.** If the user has not stated it, infer and confirm in one sentence.
2. **Anchor in user evidence.** Restate the user's task, their emotional state, and the business pressure pushing on the design. Without this, card naming becomes labelling theatre.
3. **Pick the cards.** Select cards that match the actual moves in the design. Two to five cards is usually enough — naming every card dilutes the critique. Use only cards from the working list below — never invent a card name, because a shared vocabulary is what lets a team use these words together. The list is not the complete published deck (the paper names only five of its twelve Anti-Heroes and none of its Heroes; see [references/cards.md](references/cards.md)), so if the team holds the published deck, use the names printed on its cards. The working list, Anti-Hero ↔ Hero:
   - Trap-Setter ↔ Empowerer
   - Camouflager ↔ Unveiler
   - Empathy Manipulator ↔ Life Coach
   - Cynic ↔ Liberator (or Life Coach)
   - Nickling-and-Diming ↔ Transparent Pricer
   - Black Hat ↔ White Hat (or Unveiler)
   - Two-Faced ↔ Consistent Communicator
   - Puppeteer ↔ Liberator (or Empowerer)
   - Adversary ↔ Ally
   - FOMO-Dealer ↔ Life Coach (provisional: the paper names this Anti-Hero but not its Hero)

   The alternates in parentheses are suggestions for fit, not extra cards. Full card descriptions are in [references/cards.md](references/cards.md).
4. **Cite the move.** For each card, point to the specific element, copy line, default, or step that triggers the tag. The cite is what makes the critique survive disagreement.
5. **Pair with Hero counterparts.** Every Anti-Hero tag should have at least one concrete Hero move that addresses it.
6. **Mark unavoidable friction.** Some Anti-Hero-shaped patterns are required (legal warnings, fraud checks, age gates). Call these out so the team does not strip them by accident.
7. **Output the appropriate format for the mode** (see below).

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

Default to this layout. Trim mode-specific sections that do not apply to the chosen mode; sections 1 (Frame) and 5 (Necessary friction kept) appear in every mode.

### 1. Frame
- Design under review (or concept under development)
- User task and emotional state
- Business goal / stakeholder pressure
- Mode in use

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

### 2. Anti-Hero hits
A table with columns: card · what is happening · where in the design · why it is anti-user.

### 3. Hero counter-moves
A table with columns: paired card · concrete change · why it restores user value.

### 4. Mode-specific section
- Evaluation: risk note and "first three changes I would ship."
- Reverse brainstorming: anti-goals named, Hero flips, watch-outs.
- Conceptualization: 2–3 concept directions with the Anti-Hero slide each one risks.
- Ethical dialogue: candidate cards, dialogue scripts, follow-up questions.

### 5. Necessary friction kept
List anything Anti-Hero-shaped that should stay (regulatory, safety, fraud, accessibility). Required in every mode, including reverse brainstorming — if nothing qualifies, say so in one line and why.

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Prompt Patterns

Use or adapt prompts like these:

- **Evaluation:** "Here are screenshots of our trial-cancellation flow. Run an Anti-Heroes evaluation and tell me which cards apply and what the Hero versions would look like."
- **Reverse brainstorming:** "We are designing a notification system for a finance app. Use Anti-Heroes to imagine the worst possible version, then flip each move into a Hero."
- **Conceptualization:** "We want to build an AI coach for new managers. Use Hero cards to shape three concept directions, and flag the Anti-Hero each one could slide into."
- **Ethical dialogue:** "My team is split on whether to add a default-on data-sharing toggle. Use Anti-Heroes to give us shared language and a short script for the meeting."
- **Single-card lens:** "Apply only the Empathy Manipulator card to this onboarding screen and tell me whether the move is present."

## Guardrails

- Card names are diagnostic tools, not moral verdicts. Keep the language descriptive ("this acts as a Trap-Setter") rather than accusatory ("the designer is a Trap-Setter"). The source method explicitly frames this as designer reflection, and the deck works only if people can hear it without going defensive.
- Cite the move. A card claim without a specific UI element, copy line, default, or step is not credible and the team will reject it.
- Do not flatten unavoidable friction into Anti-Hero patterns. Legally required confirmations, fraud checks, age gates, and safety pauses can look manipulative but exist for the user. Mark them explicitly so they are not stripped in the rewrite.
- Avoid card spam. If every element gets tagged, none of the tags carry weight. Two to five cards per critique is usually right; pick the ones that matter most.
- Pair every Anti-Hero with a concrete Hero move. A critique with no flip is rant fuel, not design feedback.
- Hold space for genuine value tension. Some designs deprioritize user values for defensible reasons (cost, scale, regulation). Surface the trade-off honestly instead of pretending Hero moves are always free.
- Stay grounded in the source. The deck and its intended use are described in Mehta, Chivukula, Gray, et al. (2024), arXiv:2405.03674; the full card definitions are in that paper's supplemental material, which this skill does not reproduce. When in doubt, defer to the working list in [references/cards.md](references/cards.md) rather than inventing new cards.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A good output:

- names the user task and emotional state before tagging anything
- uses 2–5 cards, each with a specific cite from the design
- pairs every Anti-Hero with a concrete Hero counter-move
- distinguishes manipulative friction from necessary friction
- ends with something the team can actually do in the next sprint, not just labels
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none

Scale guidance: for a single screen or flow, expect 2–5 Anti-Hero hits, 2–5 Hero counter-moves, and 1–3 friction-to-keep items. If the design is sprawling, scope the review to one journey at a time.

## Example Output

> **Frame**
> - Design under review: free-trial cancellation flow for a fitness app
> - User task: cancel before being charged; user is anxious and short on time
> - Business pressure: trial-to-paid conversion is the team's top OKR this quarter
> - Mode: Evaluation
>
> **Anti-Hero hits**
>
> | Card | What is happening | Where | Why it is anti-user |
> |---|---|---|---|
> | Trap-Setter | Cancel button is buried under three nested menus | Settings → Subscription → Manage → "More options" | User has to discover the path; entry was one tap |
> | Empathy Manipulator | "Are you sure? You'll lose your 14-day streak" with a sad-mascot illustration | Step 2 of cancel | Weaponizes loss aversion against a user who already decided |
> | Nickling-and-Diming | Offers a 50% discount only if user clicks "Stay" twice | Step 3 | Makes the cheaper price contingent on staying, not on asking |
>
> **Hero counter-moves**
>
> | Paired card | Concrete change | Why it restores user value |
> |---|---|---|
> | Empowerer | Cancel link appears next to "Renews on …" wherever the renewal date appears | Symmetry with how user got in |
> | Life Coach | Replace mascot with one neutral line: "Your data stays for 30 days if you change your mind" | Information, not pressure |
> | Unveiler | Show the discount on step 1 as an honest option, not a reward for resisting | Transparency over coercion |
>
> **First three changes I would ship**
> 1. Move "Cancel subscription" to the top of the Subscription screen.
> 2. Cut the streak-loss illustration and copy.
> 3. Show the retention discount upfront, framed as "stay at 50%" or "cancel — both fine."
>
> **Necessary friction kept**
> - Two-step confirm for the actual cancel click stays — prevents accidental cancels and is standard for paid services. Just keep the steps neutral.

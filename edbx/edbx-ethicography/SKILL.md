---
name: edbx-ethicography
description: Use when a researcher, senior designer, or team lead wants to conduct a deep post-hoc ethical analysis of a design process, identify moments where value-centered vs. manipulative thinking shaped decisions, map the ethical trajectory of a design project over time, code design decisions by ethical intent and impact, or build an evidence base for ethical design research. Apply Ethicography to analyze design decisions and team speech acts for their explicit or implicit ethical dimensions, mapping the value-centered vs. manipulative nature of each decision. Trigger this skill for any mention of ethical design analysis, design decision audit, value-centered design research, mapping ethics in design process, analyzing design team ethics, or when someone says "I want to understand the ethical quality of our design decisions, not just the outcomes." Also trigger for "Ethicography", "ethical moves", "design decision ethics", "speech act analysis", or "ethical trajectory".
version: "1.0"
tags: [ethical-design, audit]
---

# Ethicography

## Overview

Ethicography enables design researchers to describe the ethical nuances of collaborative design decisions by illuminating value-centered and manipulative attentions. Every moment designers make decisions, they act according to their own ethical and moral codes — whether they realize it or not.

Ethicography uses the designer as an ethical lens. It treats design decisions and speech acts as data, analyzing them for the explicit or implicit values they serve or undermine. The published method takes a transcript of a design session, splits it into speech acts, gives each a value code (the likely intent of the act, read as an attitude toward one or more values, colour-coded as more value-centred or more manipulative), gives each an idea code (how the act relates to a problem, a solution or a decision rationale), and links the acts into a visual map called an ethicograph, which shows how values and design activity interact over a session. This skill maps each decision on a 2×2 matrix of Explicit/Implicit × Persuasion/Coercion, revealing the ethical quality of a design process over time. (The 2×2 is an edbx adaptation: the published method colour-codes each speech act as more value-centred or more manipulative.)

Developed by Chivukula, Gray and Brier (CHI 2019) as an analytical framework for design ethics research, the paper applies it to transcribed lab sessions with design students. This skill offers two modes: **Team Reflection** (accessible, facilitated) and **Research Documentation** (formal, citable).

> **edbx adaptation:** the two modes, the numbered "Design Move" unit, the value families and affected-populations table (Step 3), Performative Ethics Moves (Step 3.5) and the Trajectory Forward projection (Step 4) are not part of the published method, which is one research method run on recorded sessions; the paper shows value relationships over time but makes no forecast. They are here to make the method usable on a team's own written records and to turn a trace into something a team can act on. The Step 0 record check is also edbx's; it is here because a trace without a record invites invented history.

> **Mindset check:** Ethicography analyzes what people *say* in design sessions as data, not just what decisions were made. The paper's input is transcribed recordings of design sessions; this skill also accepts written records such as meeting notes, design crit notes and Slack discussions, and treats them as weaker evidence than a transcript. The goal is to reveal the ethical trajectory of decisions — not to assign blame.

## Use This Skill When

- You want to conduct a deep post-hoc ethical analysis of a design process.
- You need to identify moments where value-centered vs. manipulative thinking shaped decisions.
- You are mapping the ethical trajectory of a design project over time.
- You are coding design decisions by ethical intent and impact for research.
- You want to build an evidence base for ethical design research or publication.
- You are facilitating a team retrospective on the ethical quality of their process.

## Inputs

Provide as many of these as are available:

- A design process, project history, or set of design decisions to analyze
- Optionally: meeting transcripts, design crit notes, or documented decisions
- Optionally: a specific design decision or moment to analyze in depth
- Optionally: a research question about the ethical quality of the design process
- Specify mode: **Team Reflection** (accessible) or **Research Documentation** (formal/academic); both are edbx modes

## Workflow

Ethicography operates in four steps, after one check.

---

### Step 0 — Check the Record

Ethicography traces decisions, so it needs a record of them. Classify the brief before anything else:

- **Record**: the brief describes decisions — who decided or argued what, and why — for at least the main moves (meeting notes, a decision log, a design history, the user's own account of how choices were made).
- **Outcome only**: the brief gives what shipped and what happened, but not the decisions behind it (most postmortem summaries).

With a **record**, run Steps 1–4 on the recorded moves.

With **outcome only**, do not build a move-by-move history. Code only the moves the brief itself states (choosing the metrics, shipping the feature, making the score visible to managers are moves the brief records). List every other decision that must have happened to produce the outcome under **Hypotheses to Check**, each with the record that would settle it (ticket, crit notes, roadmap, launch review, metrics review). Hypotheses get no move number, no actor and no quadrant; they are questions for the team, not findings. Say in the Answer that the trace is limited to what the brief records and name the records that would complete it.

---

### Step 1 — Identify Ethical Moves

For the design decisions or speech acts provided, identify each as an "Ethical Move":
- Name the decision or speech act (e.g., "Team decided to add urgency countdown to checkout")
- Assign it a **Design Move number** (chronological; edbx's label for numbering the speech acts or decisions in order)
- Identify the **participant** who made or advocated for it
- Note the **stated reason** (explicit framing) and any **implicit motivation** (what it actually achieves)
- Mark its **source**: `brief` when the brief records the move, `reconstructed` when you infer it

Work from the moves the record holds (Step 0). `reconstructed` is for a single gap inside a record — one missing step between two recorded moves — named with the record that would confirm it and an actor given as a role ("growth team", "product lead"), never an invented name. With outcome only, unrecorded decisions go under Hypotheses to Check instead. Never write quotes, meetings, dates, documents or incidents the brief did not give.

---

### Step 2 — Code on the 2×2 Matrix

Place each Ethical Move on the Explicit/Implicit × Persuasion/Coercion axis:

| Quadrant | Label | Description |
|---|---|---|
| Explicit + Persuasion | **Value-Centered (Ethical)** | Openly argues for user benefit or ethical principle |
| Explicit + Coercion | **Explicit Manipulative (Harm)** | Openly advocates for design that overrides user agency |
| Implicit + Persuasion | **Implicit Value-Centered** | Quietly nudges toward ethical outcomes without naming it |
| Implicit + Coercion | **Implicit Manipulative** | Concealed manipulation embedded in design rationale |

For each move: assign quadrant, explain why, name the value or harm at stake.

---

### Step 3 — Map Values Alignment + Affected Populations

For each Ethical Move, identify (a) which values it serves or undermines and (b) **which specific populations the move privileged or harmed**.

**A. Values served / undermined**

The paper draws its value vocabulary from Friedman's list of human values, for example ownership, privacy, accountability, freedom from bias, trust, autonomy, usability, informed consent and human welfare, and names the value most salient in each speech act. Use these first. The five families below group values by whose they are; they are edbx's grouping, for sorting moves that touch more than one party.

- **User values:** autonomy, privacy, dignity, safety, transparency
- **Designer values:** craft, honesty, advocacy, integrity
- **Business values:** revenue, growth, engagement, retention
- **Non-user values:** bystander privacy, environmental load, public-discourse health, downstream third-party rights
- **Worker values:** moderator wellbeing, gig-worker dignity, annotator labor conditions

Tag each move: `⬆️ Supports value` / `⬇️ Undermines value` / `↔️ Neutral`

**B. Affected populations (required, named specifically)**

For every move, name **at least 2 specific populations** affected. Generic "users" is a sign the analysis is too shallow. Pick the populations actually relevant to the move:

| Move | Population (named) | How they were affected | Was their voice in the room when this was decided? |
|---|---|---|---|

Populations to scan for (use the ones genuinely relevant; do not list all):
- Vulnerable subgroups within users: minors, neurodivergent users, abuse survivors, people in crisis (mental-health, financial precarity, immigration status), older adults with low digital literacy
- Non-users: people scanned/photographed/talked-about-by-association, people scraped into training data, bystanders on shared accounts
- Downstream parties: data partners, advertisers' targets, regulators, journalists relying on the platform
- Workers: content moderators, gig workers, annotators, support staff (with reference to their exposure to harmful content if applicable)
- Future-affected populations: users in 5 years using accumulated data, jurisdictions where data may be subpoenaed, users who later lose protected-class status (e.g., aging out of minor-protections)

This step names the people the decisions touched.

**C. Concrete-harm examples (when relevant)**

When a move undermines a user value, give a concrete example of what the harm looks like in practice — not "accessibility was deprioritized" but "missing alt-text on payment-confirmation buttons left screen-reader users unable to verify the amount before submission" or "reliance on color alone for required-field state failed WCAG 1.4.1, causing form abandonment for ~5% of users with color-vision differences."

For accessibility findings specifically, name the WCAG criterion or ARIA role failure (e.g., "WCAG 2.5.5 target size," "missing aria-live region for async error states," "focus trap not implemented in modal"). Vague "accessibility issues" is not enough.

---

### Step 3.5 — Detect Hidden Speech Acts

Scan the design decisions for moves that perform one ethical intent while achieving another. These are the most analytically valuable findings — visible ethical language concealing invisible manipulation.

Ask for each decision: *"Does the stated framing match what this design move actually achieves?"*

Examples:
- "Privacy settings" UI that is architecturally incapable of deleting data → performs transparency, achieves opacity
- "User wellbeing mode" that reduces notifications but increases return anxiety → performs care, achieves re-engagement
- "Informed consent" modal with 4,000-word ToS and a single "Agree" button → performs consent, achieves compliance

These are coded `Implicit + Coercion` but are distinct because they use ethical language as cover. Flag them separately as **Performative Ethics Moves**.

### Step 4 — Generate Ethicograph Summary

Produce a longitudinal analysis:
- What is the overall ethical trajectory? (moving toward or away from value-centered design?)
- Which moments were ethical turning points?
- Which participants consistently occupied which quadrants?
- What values were consistently present? Consistently absent?
- Were manipulative moves explicit (visible, debatable) or implicit (invisible, unquestioned)?
- Were any **Performative Ethics Moves** detected — decisions using ethical language to conceal manipulation?

**Trajectory Forward (required):** Based on the ethical coding of past decisions, project where the product's ethical posture is heading over the next 12 months if current decision patterns continue. This is a forecast, not a description — name which quadrant the team will drift toward and what specific pattern of decisions is driving the drift. It makes the trajectory legible before it compounds.

---

## Output Format

Open with a short **Answer**: two to four sentences that answer the question the user actually asked (the decision, verdict or recommendation) and the main reason for it. The method's sections follow and back it up; they never replace it. Write it once, as the first section under the title.

### Ethicograph: [Project Name]

### Answer

[Two to four sentences: the answer to the question asked (decision, verdict or recommendation) and the main reason.]

### Record Status

[Record / Outcome only] — one sentence on what the brief records, and the records that would complete the trace.

### Ethical Moves Inventory

| Move # | Actor | Decision/Speech Act | Source | Quadrant | Value Impact |
|---|---|---|---|---|---|
| 1 | [role, or the name the brief gives] | [decision] | [brief / reconstructed] | [one of the four quadrants — a performative move still gets one] | ⬆️/⬇️/↔️ [value] |
| 2 | [role] | [decision] | [brief / reconstructed] | [quadrant] | ⬆️/⬇️/↔️ [value] |

### 2×2 Placement

Each move placed and justified:

**Explicit + Persuasion (Value-Centered):**
- Move #[n]: [justification]

**Explicit + Coercion (Manipulative Harm):**
- Move #[n]: [justification]

**Implicit + Persuasion (Value-Centered):**
- Move #[n]: [justification]

**Implicit + Coercion (Manipulative):**
- Move #[n]: [justification]

### Values Alignment Summary

| Value | Moves Supporting | Moves Undermining |
|---|---|---|
| [Value 1] | [move numbers] | [move numbers] |

### Affected Populations

From Step 3B. Every move in the inventory appears here — not a selection — with at least 2 named populations each.

| Move | Population (named) | How they were affected | Was their voice in the room? |
|---|---|---|---|
| 1 | [specific population] | [effect] | [yes / no / partly] |
| 1 | [second population] | [effect] | [yes / no / partly] |

### Concrete Harm Examples

For each move that undermined a user value, the specific UX, accessibility or technical mechanism — e.g., "WCAG 2.5.5 target size violation", "asymmetric value extraction: user content monetized with no revenue-share".

### Hypotheses to Check (outcome only)

| Hypothesis | Record that would settle it |
|---|---|
| [a decision that must have happened, stated as a question] | [ticket / crit notes / roadmap / launch review / metrics review] |

### Positive Practices

Moves that upheld a user value, with their move numbers; or "The record the brief gives shows none" — never an invented one.

### Performative Ethics Moves (if detected)

| Move # | Stated Framing | Actual Achievement | Why This Matters |
|---|---|---|---|
| [#] | [what it claims to do] | [what it actually does] | [consequence for users] |

### Ethical Trajectory Narrative

[Short narrative paragraph describing how ethical quality evolved over the project]

### Trajectory Forward (12-Month Projection)

*"If current decision patterns continue, this product will drift toward [quadrant] because [specific pattern of decisions]. The inflection point will likely be [trigger event], when [what will happen]. The team can prevent this by [specific intervention]."*

### Recommendations

[For team reflection mode]: What process changes would improve ethical quality?
[For research mode]: Methodological notes on coding decisions and interpretive framework.

### Evidence Ledger
| Claim used as input | Type | Basis |
|---|---|---|
| [figure, rate or fact the output relies on] | [user-supplied / sourced / assumption / unknown] | [the brief / paper or URL / why assumed] |

Every figure, rate, incident, past failure or fact about the user's product, users or situation that the output relies on gets a row in the Evidence Ledger. **Type** is exactly one of four words: `user-supplied` (stated in the brief), `sourced` (the Basis holds a URL from the user or from a search run in this session; these skills carry no source list, so a book, paper, report or regulation named without such a URL is `assumption`), `assumption` (anything else, including model knowledge) or `unknown` (a figure the output needs but the brief does not give; write "unknown" in the body too). Illustrative numbers are allowed only when labelled illustrative in the body and typed `assumption` here. Invented characters, scenes, stories and worked examples that the method itself asks for are not claims: give them no ledger row (the Type column holds only the four words above), and keep them visibly marked as invented in the body. The Basis names the brief, a paper, a URL or "model knowledge"; never this skill, its rules or its box.

## Guardrails

- Do not treat the 2×2 matrix as a grading system. The goal is analysis, not judgment of individuals.
- Do not assume all manipulative moves are intentional. Implicit coercion often emerges from organizational pressure, not individual malice.
- Do not ignore positive ethical practices. Ethicography should identify what worked as well as what didn't.
- Do not code moves without justification. Every placement needs reasoning.
- Do not forget the longitudinal view. Individual moves matter less than the trajectory they create.
- Do not conflate stated reasons with actual impact. The gap between them is where ethical insight lives.
- Do not present a reconstructed history as observed. Quotes, names, meetings and dates come from the brief or not at all; reconstructed moves are marked and paired with the record that would confirm them.
- Do not name other skills or boxes in the deliverable as if the reader has them. Describe a related method in plain terms (a structured worry session, a stakeholder harm map).
- Do not invent facts about the user's product, users or situation: figures, rates, incidents, past failures, research findings or sources. Where the brief is silent, write "unknown", list it in the Evidence Ledger, and carry on.
- Do not stop to ask for more details before answering: draft the full deliverable with unknowns marked, and list the questions worth asking the user at the end.

> **edbx adaptation:** the Evidence Ledger is a family convention from fdbx, not part of the source method. Plain models state invented figures about the user's situation as fact; the ledger makes the basis of each claim visible.

## Deliverable Quality Bar

A strong Ethicography output:

- codes every design decision/speech act with a quadrant placement
- justifies every placement with reasoning
- tracks at least 3 distinct values across the analysis
- **names at least 2 specific affected populations per move** (Step 3B), including non-users / workers / future-affected populations where relevant — and notes whether their voice was in the room when each decision was made
- **gives concrete-harm examples** for moves that undermined a user value: name the specific UX/accessibility/technical mechanism (e.g., "WCAG 2.5.5 target size violation," "asymmetric value extraction: free user-generated content monetized via ads sold to third parties without revenue-share")
- detects and flags Performative Ethics Moves (decisions using ethical language to conceal manipulation)
- produces an ethical trajectory narrative every session
- produces a 12-month Trajectory Forward projection naming the drift direction, trigger event, and intervention
- works in both team reflection mode and academic research mode
- handles positive ethical practices (not only critique)
- in research mode, includes methodological notes suitable for academic documentation
- opens with a direct answer to the decision or question the user asked, which the rest of the output supports
- lists the figures and facts about the user's situation it relies on in an Evidence Ledger, typed user-supplied / sourced / assumption / unknown, and invents none
- marks every move `brief` or `reconstructed`, and invents no quotes, names, meetings, dates or incidents
- states whether the brief holds a record of decisions; with outcome only, codes only the moves the brief states and lists the rest as hypotheses with the record that would settle each

## Integration with Other EDBX Skills

- **edbx-anotherlens** surfaces designer self-awareness. Ethicography provides the analytical framework to document that awareness (or its absence) in design records.
- **edbx-worrystorming** is anticipatory. Ethicography is retrospective — they bracket the design process.
- **edbx-responsible-design-prism** gives a current spectrum reading. Ethicography explains the decision history that got the design there.

## Hashtags

#breakmydesign #identifyvalues

## See Also

- Ethical Design Scorecards
- Dichotomy Mapping

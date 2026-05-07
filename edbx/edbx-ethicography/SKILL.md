---
name: edbx-ethicography
description: Use when a researcher, senior designer, or team lead wants to conduct a deep post-hoc ethical analysis of a design process, identify moments where value-centered vs. manipulative thinking shaped decisions, map the ethical trajectory of a design project over time, code design decisions by ethical intent and impact, or build an evidence base for ethical design research. Apply Ethicography to analyze design decisions and team speech acts for their explicit or implicit ethical dimensions, mapping the value-centered vs. manipulative nature of each decision on a persuasion-to-coercion axis. Trigger this skill for any mention of ethical design analysis, design decision audit, value-centered design research, mapping ethics in design process, analyzing design team ethics, or when someone says "I want to understand the ethical quality of our design decisions, not just the outcomes." Also trigger for "Ethicography", "ethical moves", "design decision ethics", "speech act analysis", or "ethical trajectory".
metadata:
  version: "1.0"
---

# Ethicography

## Overview

Ethicography enables design researchers to describe the ethical nuances of collaborative design decisions by illuminating value-centered and manipulative attentions. Every moment designers make decisions, they act according to their own ethical and moral codes — whether they realize it or not.

Ethicography uses the designer as an ethical lens. It treats design decisions and speech acts as data, analyzing them for the explicit or implicit values they serve or undermine. The method maps each decision on a 2×2 matrix of Explicit/Implicit × Persuasion/Coercion, revealing the ethical quality of a design process over time.

Developed by Chuvaala, Gray et al. (2019, 2024) as an analytical framework for design ethics research, Ethicography is the most analytically rigorous method in the ethical design toolkit. It operates in two modes: **Team Reflection** (accessible, facilitated) and **Research Documentation** (formal, citable).

> **Mindset check:** Ethicography analyzes what people *say* in design meetings as data, not just what decisions were made. Meeting notes, design crits, and Slack discussions are all valid input. The goal is to reveal the ethical trajectory of decisions — not to assign blame.

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
- Specify mode: **Team Reflection** (accessible) or **Research Documentation** (formal/academic)

## Workflow

Ethicography operates in four steps.

---

### Step 1 — Identify Ethical Moves

For the design decisions or speech acts provided, identify each as an "Ethical Move":
- Name the decision or speech act (e.g., "Team decided to add urgency countdown to checkout")
- Assign it a **Design Move number** (chronological)
- Identify the **participant** who made or advocated for it
- Note the **stated reason** (explicit framing) and any **implicit motivation** (what it actually achieves)

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

This step is what separates ethnography from accountability — naming the people the decisions touched.

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

**Trajectory Forward (required):** Based on the ethical coding of past decisions, project where the product's ethical posture is heading over the next 12 months if current decision patterns continue. This is a forecast, not a description — name which quadrant the team will drift toward and what specific pattern of decisions is driving the drift. This is what distinguishes Ethicography from a retrospective audit: it makes the trajectory legible before it compounds.

---

## Output Format

### Ethicograph: [Project Name]

### Ethical Moves Inventory

| Move # | Actor | Decision/Speech Act | Quadrant | Value Impact |
|---|---|---|---|---|
| 1 | [name] | [decision] | [quadrant] | ⬆️/⬇️/↔️ [value] |
| 2 | [name] | [decision] | [quadrant] | ⬆️/⬇️/↔️ [value] |

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

## Guardrails

- Do not treat the 2×2 matrix as a grading system. The goal is analysis, not judgment of individuals.
- Do not assume all manipulative moves are intentional. Implicit coercion often emerges from organizational pressure, not individual malice.
- Do not ignore positive ethical practices. Ethicography should identify what worked as well as what didn't.
- Do not code moves without justification. Every placement needs reasoning.
- Do not forget the longitudinal view. Individual moves matter less than the trajectory they create.
- Do not conflate stated reasons with actual impact. The gap between them is where ethical insight lives.

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

## Integration with Other EDBX Skills

- **edbx-anotherlens** surfaces designer self-awareness. Ethicography provides the analytical framework to document that awareness (or its absence) in design records.
- **edbx-worrystorming** is anticipatory. Ethicography is retrospective — they bracket the design process.
- **edbx-responsible-design-prism** gives a current spectrum reading. Ethicography explains the decision history that got the design there.

## Hashtags

#breakmydesign #identifyvalues

## See Also

- Ethical Design Scorecards
- Dichotomy Mapping

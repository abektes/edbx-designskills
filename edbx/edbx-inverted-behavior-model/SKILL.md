---
name: edbx-inverted-behavior-model
description: Use when a designer wants to identify what behaviors a feature is likely to trigger beyond its intended use, forecast unintended consequences of behavior design, evaluate features through a persuasive technology lens, map motivational factors that drive behavior toward or away from intended outcomes, or audit a product for potentially harmful behavioral outcomes. Apply the Inverted Behavior Model to forecast the full range of behaviors — intended and unintended — that a product feature motivates, and map their consequences for users and society. Trigger this skill for any mention of behavior design, unintended user behavior, persuasive technology audit, forecasting feature consequences, BJ Fogg behavior model, or when someone asks "what will users actually do with this?" Also trigger for "Inverted Behavior Model", "behavior forecast", "persuasive technology review", "behavior audit", or "unintended consequences".
metadata:
  version: "1.0"
---

# Inverted Behavior Model

## Overview

Inverted Behavior Model supports you in identifying potential behavior based on a forecast of what a feature or product motivates the user to do. Designers generate products and features based on expectations of how users will behave. The Inverted Behavior Model inverts this: rather than designing *toward* a behavior, the method works backward from features to reveal what behaviors they actually incentivize.

The method is grounded in BJ Fogg's Behavior Model (B = Motivation + Ability + Prompt), which states that behavior occurs when these three elements converge. The "inversion" is methodological: instead of using the model to *design* behavior, this method uses it to *audit* what behaviors are being designed — intentionally or not.

By working through Inverted Behavior Models, designers can identify the motivating factors behind each feature, list intended and unintended behaviors, and identify a range of consequences that could positively or negatively impact users or society at large.

> **Mindset check:** Don't ask "what do we want users to do?" — ask "what does this feature actually incentivize?" The inversion is the key insight.

## Use This Skill When

- You want to forecast what behaviors a feature will actually trigger, beyond its intended use.
- You need to evaluate unintended consequences of behavior design.
- You are auditing a product for persuasive technology or dark patterns.
- You want to understand what motivational factors drive user behavior in your product.
- You need to map consequences at individual, vulnerable-user, scale, and societal levels.
- You are designing features and want to avoid harmful behavioral outcomes.

## Inputs

Provide as many of these as are available:

- A product, feature set, or specific feature to analyze
- Optionally: a primary intended behavior the feature is designed to produce
- Optionally: a user population or context
- Optionally: a specific concern about unintended behavior to investigate

## Workflow

The Inverted Behavior Model follows four steps, plus a stakeholder map (Step 0) and a rationalizations check (Step 4.5).

---

### Step 0 — Stakeholder Map (required, not optional)

Before deconstructing prompts, enumerate every population the feature touches. The behavior model evaluates how prompts shape behavior — but whose behavior? Naming this explicitly prevents the analysis from collapsing to "the average user."

| Stakeholder | Relationship to feature | Power they have | Power they lack |
|---|---|---|---|
| Primary users | (intended audience) | (exit, opt-out, complaint) | (cannot influence the prompt design or the metric it serves) |
| Vulnerable subgroups within users | **Name them specifically** — e.g., adolescents, neurodivergent users, shift workers, abuse survivors, low-income, users in crisis. Pick 2–4 actually relevant. | | |
| Non-consenting bystanders in the user's environment | (people scanned, photographed, talked-about-by-association, household members on shared accounts, partners/co-parents whose data is exposed by the user's use) | | |
| Workers in the supply chain | (moderators exposed to harmful content, gig workers managed by these prompts, annotators) | | |
| Absent regulators / institutions | (FTC, EU AI Act enforcement, school administrators, medical boards — parties with formal authority who are not in the room when the prompt is designed) | | |
| Future-affected populations | (users in 5 years using accumulated behavioral data; people who later face decisions made by models trained on these behaviors) | | |

This map is referenced by Step 4 (Consequence Map) — every consequence must name which stakeholder bears it.

---

### Step 1 — Deconstruct into Prompts

Break the product or feature down into its individual behavioral prompts:
- A prompt is any element that triggers a user action (notification, button, feed, score, streak, countdown, etc.)
- List every prompt in the feature
- For each prompt: name it, describe its trigger mechanism, and state its intended behavioral outcome

**Output:** A prompt inventory.

---

### Step 2 — Map Motivating Factors

For each prompt, identify the motivating factors that make a user respond to it. Use the Fogg Behavior Model framework — behavior occurs when Motivation + Ability + Prompt converge:

| Motivating Factor Category | Examples |
|---|---|
| **Intrinsic motivation** | Curiosity, mastery, autonomy, meaning |
| **Social motivation** | Status, belonging, fear of exclusion, social comparison |
| **Extrinsic motivation** | Reward, punishment, incentive, loss aversion |
| **Emotional motivation** | Fear, excitement, guilt, shame, pride |
| **Habitual motivation** | Routine, muscle memory, addiction loop |

For each prompt: list 2–4 motivating factors it activates, noting whether they are healthy or potentially exploitative.

---

### Step 2.5 — Construct the "Worst Possible Design" (the Inversion Artifact)

Before forecasting behaviors, produce the inversion artifact: a description of the worst possible version of this feature if every prompt were designed to maximize manipulation rather than user value.

This is the methodological core of the Inverted Behavior Model. The inversion must be written as a concrete design description — not a list of risks, but an actual feature description as a malicious designer might have written it.

Format: *"If this feature were designed to maximize [harm], it would: [specific design decisions, named mechanics, copy choices]."*

This artifact makes non-obvious harmful patterns visible by contrast. Holding the worst possible design next to the actual design surfaces the distance between them — and reveals which parts of the actual design have already drifted toward the worst version.

---

### Step 2.6 — Convergence Check (the comparison the inversion enables)

Compare the actual design (Step 1's Prompt Inventory) against the Worst Possible Design (Step 2.5), prompt by prompt. The inversion is only useful if you do this comparison — without it, the worst-design artifact is decoration.

For every prompt, score convergence:

- 🟢 **Diverged** — the actual design deliberately avoids the dark version of this prompt
- 🟡 **Adjacent** — the actual design isn't the worst version, but is one product decision away from it (e.g., a feature toggle, a copy change, a metric incentive shift could push it there)
- 🔴 **Converged** — the actual design already implements the dark version, in whole or part

Output as a table:

| Prompt | Worst-Version Element | Actual Design | Convergence |
|---|---|---|---|

Every 🔴 Converged row is a finding that must appear in Step 4's Consequence Map and in the Redesign Directions section. Every 🟡 Adjacent row should be flagged as a drift risk in the Behavior Forecast Statement.

This step is what makes the method "Inverted." Skipping it reduces the skill to a generic behavior-forecast exercise.

### Step 3 — Forecast Behaviors (Inverted)

For each prompt + motivation combination, forecast:

**Intended behaviors** (what the designer hoped for):
- The specific action the prompt was designed to produce

**Unintended behaviors** (the inversion):
- What else might users do in response to this prompt?
- What behaviors emerge when motivation is higher or lower than expected?
- What behaviors emerge in edge cases, vulnerable users, or at scale?
- What social behaviors does this prompt enable or amplify?

**Non-Obvious Behavioral Cascades (required for each 🔴 finding):**
Identify 2nd-order behaviors that emerge from user interaction patterns over time — behaviors that would not appear in a single-session observation but emerge from repeated use, social context, or user adaptation to the feature. Example: "A leaderboard prompt initially motivates improvement-seeking behavior; over 6 weeks, lower-ranked users shift to gaming behavior (finding exploits to improve rank without improving performance) rather than improvement behavior."

Use a behavior taxonomy:
- `✅ Intended` — aligns with design goal
- `⚠️ Unintended / Neutral` — not designed for, but not harmful
- `🔴 Unintended / Harmful` — not designed for, potentially harmful to user or society
- `🟣 Social / Amplified` — behavior that emerges when many users do it simultaneously (network effects)

---

### Step 4 — Map Consequences (with explicit Behavioral Cascade Model)

For each `🔴 Harmful` and `🟣 Social/Amplified` behavior, map consequences across the full stakeholder set from Step 0 — not just "individual user" generically.

**A. Per-stakeholder consequence table:**

| Behavior | Consequence for primary user | Consequence for vulnerable subgroups (named) | Consequence for non-consenting bystanders | Consequence for workers in supply chain | Consequence at scale (10M users) | Consequence for society / institutional landscape |
|---|---|---|---|---|---|---|

**B. Behavioral Cascade Model (required for every 🔴 finding):**

A single behavior rarely stands alone. Map the cascade:

```
Initial behavior (week 1)
  → Adaptation behavior (weeks 2-6, as user learns the prompt)
    → Social/relational behavior (months 1-3, as the behavior shows up in user's relationships)
      → Identity-level behavior (months 3-12, as the behavior reshapes who the user is)
        → Generational/cultural behavior (years, as the behavior becomes normalized)
```

For each 🔴 finding, name at least 3 stages of the cascade. Example for a streak system:
- Week 1: User completes daily task to start streak
- Weeks 2–6: User reorganizes their day around protecting the streak; sleep, attention, and other obligations get displaced
- Months 1–3: User experiences guilt/shame on missed days; the app moves from "tool I use" to "tool I owe"
- Months 3–12: Streak becomes part of the user's self-concept ("I'm someone who hasn't missed a day in 247 days"); breaking it triggers identity-level distress
- Years: Streaks become normalized as legitimate motivation across the industry; "loss aversion as engagement strategy" becomes a default design pattern, not an ethical concern

The cascade reveals harms that single-session behavior analysis misses.

---

### Step 4.5 — Rationalizations Check (the stories teams tell themselves)

The most damaging behavioral designs ship not because the team didn't see the harm, but because they had a vocabulary ready to defend it. Identify the **rationalizations** — the stories the team tells itself or hears from leadership that make this feature defensible despite the harms named above.

For each 🔴 finding, name 1–2 rationalizations and rebut each one in plain language:

| 🔴 Finding | Rationalization (the story) | Why the rationalization fails |
|---|---|---|
| e.g., adolescent compulsive checking from variable-reward like counter | "We're just giving people what they want" | "Want" is downstream of the design — variable-reward schedules manufacture wanting. The user did not arrive with this preference. |
| e.g., gig-worker pay opacity | "Our drivers prefer simplicity" | The simplicity claim was never tested against drivers; it was generated to defend a UX choice that benefits the platform, not workers. |
| e.g., engagement amplification of distressing content | "The alternatives are worse" | "Worse" is unspecified; in this case the alternative is "do not amplify content that has been flagged as triggering distress in similar users," which is neither worse nor speculative. |

Common rationalizations to scan for: *"users want it," "the alternatives are worse," "it's just a tool — people choose how to use it," "if we don't, our competitors will," "users can always opt out," "we're not responsible for how people use it," "it's helping more people than it's hurting," "we're building it ethically [no testable claim]"*

This step is what makes the analysis usable in a real org. A team that names its own rationalizations in advance has a much harder time deploying them later.

---

## Output Format

### Inverted Behavior Model: [Feature Name]

### Stakeholder Map

(From Step 0 — required. Every consequence below must reference these stakeholders by name, including non-consenting bystanders, workers in the supply chain, and absent regulators.)

| Stakeholder | Relationship | Power they have | Power they lack |
|---|---|---|---|

### Prompt Inventory

| Prompt | Trigger Mechanism | Intended Behavior |
|---|---|---|
| [Prompt 1] | [how it triggers] | [intended action] |

### Worst Possible Design (Inversion Artifact)

A concrete feature description as a malicious designer might have written it — naming specific mechanics, copy choices, and dark-pattern moves the worst version would include. Format: *"If this feature were designed to maximize [harm], it would: [specific design decisions]."* This is the methodological centerpiece — never omit it.

### Convergence Check

| Prompt | Worst-Version Element | Actual Design | Convergence (🟢/🟡/🔴) |
|---|---|---|---|

Every 🔴 row anchors a 🔴 Harmful behavior in the forecast below. Every 🟡 row is flagged as a drift risk.

### Behavior Forecast

| Prompt | Motivations | ✅ Intended | ⚠️ Unintended Neutral | 🔴 Unintended Harmful | 🟣 Social Amplified |
|---|---|---|---|---|---|
| [Prompt 1] | [factors] | [behavior] | [behavior] | [behavior] | [behavior] |

### Consequence Map (per-stakeholder, all from Step 0)

| Behavior | Primary user | Vulnerable subgroups (named) | Non-consenting bystanders | Workers in supply chain | At scale (10M users) | Society / institutional landscape |
|---|---|---|---|---|---|---|

### Behavioral Cascade Model

For every 🔴 finding, name at least 3 stages of the cascade (initial → adaptation → social/relational → identity-level → generational/cultural). Single-session analysis misses the harms that emerge over months and years.

### Rationalizations Check

| 🔴 Finding | Rationalization (the story the team uses) | Why the rationalization fails |
|---|---|---|

### Behavioral Risk Summary (Top 3)

1. [Highest-risk unintended behavior + consequence profile]
2. [Second-highest]
3. [Third-highest]

### Redesign Directions (minimum 2 alternatives)

For each 🔴 finding, generate at least 2 redesign directions — not just one recommendation. Multiple directions expose the trade-off space and prevent the output from feeling like a single "right answer" that the team will debate rather than act on.

**Direction A:** [Minimal change — addresses the harmful behavior without restructuring the feature]
**Direction B:** [Structural change — modifies the underlying prompt or motivation architecture]

Name what metric would change for each direction and what organizational resistance it would face.

### Behavior Forecast Statement

*"This feature is likely to produce [intended behavior] but also incentivizes [unintended behavior X] through [motivating factor Y], with consequences including [Z]."*

## Guardrails

- Do not stop at intended behaviors. The inversion requires probing what else the feature incentivizes.
- Do not ignore vulnerable users. "Users" is not specific enough — name who is most at risk.
- Do not skip scale thinking for 🟣 Social/Amplified behaviors. Individual harm and societal harm are different.
- Do not over-flag low-risk features. Not every feature has harmful unintended consequences.
- Do not treat all motivating factors as equally exploitative. Intrinsic motivation is different from addiction loops.
- Do not forget the redesign phase. Identifying harmful behaviors without proposing fixes is incomplete.

## Deliverable Quality Bar

A strong Inverted Behavior Model output:

- **completes the Stakeholder Map** (Step 0) with at least 5 named populations including non-consenting bystanders, workers in the supply chain, and absent regulators — not just "users"
- fully deconstructs any feature into behavioral prompts
- produces a "Worst Possible Design" inversion artifact before forecasting behaviors
- produces a Convergence Check table comparing every actual prompt to the worst-version equivalent — without it, the method is just a behavior forecast and has not done the inversion
- maps motivating factors for every prompt (minimum 2 per prompt)
- correctly tags behaviors across all four categories (✅ ⚠️ 🔴 🟣)
- **produces a Behavioral Cascade Model** with at least 3 named stages per 🔴 finding (initial → adaptation → social/relational → identity-level → generational/cultural). Single-session harm analysis without cascade reasoning is incomplete.
- produces a per-stakeholder consequence map for every 🔴 finding, naming impact on primary users, vulnerable subgroups, non-consenting bystanders, workers, scale effects, and institutional/societal landscape
- **completes the Rationalizations Check** — for every 🔴 finding, names the story the team uses to defend it and rebuts that story in plain language. A team that names its own rationalizations in advance has a much harder time deploying them later.
- provides at least 2 redesign directions for every 🔴 prompt with metric implications and resistance notes
- handles low-risk features without false positives
- produces a behavior forecast statement per session that flags 🟡 drift risks identified in the Convergence Check

## Integration with Other EDBX Skills

- **edbx-motivation-matrix** maps user motivation types. Inverted Behavior Model maps how *specific features* activate those motivations and what behaviors result.
- **edbx-humane-design-guide** flags which human sensitivities are being exploited. Inverted Behavior Model explains the *behavioral mechanism* of that exploitation.
- **edbx-worrystorming** generates free-form worries. Inverted Behavior Model provides a structured behavioral forecast to validate or refute them.
- **edbx-responsible-design-prism** places the design on the ethical spectrum. Inverted Behavior Model explains *why* specific prompts push it toward the dark side.

## Hashtags

#breakmydesign #evaluateoutcomes

## See Also

- Motivation Matrix
- Design with Intent
- Digital Ethics Compass

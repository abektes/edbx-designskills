# Inverted Behavior Model

**The short version:** Takes a feature and works backward to map everything it actually incentivizes users to do — not just what the design intended, but the unintended behaviors that emerge from how the feature is built.

---

## Who made it

The Inverted Behavior Model is built on **BJ Fogg's Behavior Model** — a framework developed by behavioral design researcher BJ Fogg at Stanford University. Fogg's model states that behavior occurs when three elements converge: Motivation + Ability + Prompt (B = MAP).

The "inversion" is a methodological addition for ethical auditing: instead of using Fogg's model to *design* behavior (its original purpose), this method uses it to *audit* what behaviors a feature is already designed to produce — intentionally or not.

The inversion technique has been developed within ethical design research as a way to apply persuasive technology theory to retrospective analysis rather than forward design.

---

## The problem it solves

Designers design features to produce specific behaviors. But features don't produce only the behaviors they were designed for. They also produce behaviors the team never intended, didn't anticipate, and might not be comfortable with — especially at scale, over time, and in edge cases.

A streak system was designed to build daily habits. It also produces anxiety on days off, dishonest logging to maintain the streak, and the experience of shame when the streak breaks. A leaderboard was designed to motivate improvement. It also produces gaming behavior in people who prefer to look like they're improving rather than actually improving.

The Inverted Behavior Model is a systematic method for finding those unintended behaviors before they become user harms.

---

## When to use it

- **When you're designing a feature that will change user behavior** — any engagement mechanic, gamification element, notification system, or social feature
- **When you suspect a feature might be producing behaviors you didn't intend** — and you want a structured way to map them
- **For a persuasive technology audit** — to evaluate whether a product's behavioral design is ethical
- **Before a feature ships** — to forecast what will actually happen when many different users interact with it over time
- **When someone asks "what will users actually do with this?"** — this is the method that answers that question systematically

---

## What it produces

The method works in seven phases:

**Step 0 — Stakeholder Map:** Before any analysis, name every population the feature touches — primary users, vulnerable subgroups (with named demographics, not "users"), non-consenting bystanders in the user's environment (people scanned, photographed, profiled-by-association, household members on shared accounts), workers in the supply chain (moderators, gig workers, annotators), absent regulators, and future-affected populations. Behavior models that don't name *whose* behavior they're modeling collapse to "the average user."

**Step 1 — Prompt Inventory:** Break the feature down into every individual prompt — any element that triggers a user action (notification, button, score, streak, countdown, progress bar, social comparison element, etc.). Name each prompt, describe how it triggers, and state its intended behavior.

**Step 2 — Motivating Factors Map:** For each prompt, identify what motivates a user to respond to it — across five categories: intrinsic motivation, social motivation, extrinsic motivation, emotional motivation, and habitual motivation. Note whether each is healthy or potentially exploitative.

**Step 2.5 — Worst Possible Design (the Inversion Artifact):** Construct a description of what this feature would look like if every prompt were designed to maximize manipulation. Written as a concrete design description — "if this feature were designed to maximize anxiety and compulsive return visits, it would: [specific design decisions]" — it makes non-obvious manipulative patterns visible by contrast.

**Step 2.6 — Convergence Check:** Compare the actual design against the Worst Possible Design, prompt by prompt. For every prompt, score: 🟢 Diverged (designed to avoid the dark version), 🟡 Adjacent (one product decision away from drift), 🔴 Converged (already implements the dark version). This comparison is what makes the method "Inverted" — without it, the worst-design artifact is decoration.

**Step 3 — Behavior Forecast:** For each prompt, forecast intended behaviors (✅), unintended neutral (⚠️), unintended harmful (🔴), and social/amplified behaviors that emerge at scale (🟣).

**Step 4 — Consequence Map + Behavioral Cascade Model:** For each 🔴 finding, map consequences across the full stakeholder set (primary users, vulnerable subgroups, non-consenting bystanders, supply-chain workers, scale effects, society). Then map the **behavioral cascade** in five stages: initial behavior (week 1) → adaptation behavior (weeks 2–6) → social/relational behavior (months 1–3) → identity-level behavior (months 3–12) → generational/cultural normalization (years).

**Step 4.5 — Rationalizations Check:** For every harmful finding, name the story the team uses (or will use) to defend the design — *"users want it," "the alternatives are worse," "we're just giving people what they want," "if we don't, our competitors will"* — and rebut each one in plain language. A team that names its own rationalizations in advance has a much harder time deploying them later.

The output ends with **Redesign Directions** — at least two per 🔴 finding: a minimal change and a structural change, each named with the metric it shifts and the organizational resistance it will face.

---

## The key insight

The second-order behavioral cascade is what most teams miss. A leaderboard prompt initially motivates improvement-seeking behavior. After six weeks, lower-ranked users shift to gaming behavior — finding exploits to improve rank without improving performance. After six months, they disengage entirely because the social comparison has become demoralizing rather than motivating.

None of that is visible in a single-session observation. The Inverted Behavior Model requires you to think about what repeated exposure to your prompts will do to the full range of users over time.

---

## How to use it with AI

Describe the product or feature you want to analyze. If you have a specific concern about unintended behavior, name it. The AI will work through all seven phases — stakeholder map, prompt inventory, motivation mapping, worst-possible design, convergence check, behavior forecast with cascade model, consequence map, rationalizations check — and produce redesign directions for every harmful finding.

---

## A quick example

**Feature:** A fitness app's daily workout streak counter (visible on profile, resets if you miss a day).

**Prompt:** Streak counter visible on profile page and in friend feed.

**Motivating factors:** Social status (others can see your streak), fear of loss (resetting feels like failure), social comparison, habitual motivation (the streak itself becomes the goal).

**Worst Possible Design:** "If this feature were designed to maximize compulsive engagement, it would: make the streak the primary profile metric, make it visible to all friends without opt-out, send a guilt notification when the user hasn't logged by 9pm, and make streak recovery require payment."

**Behavior forecast:**
- ✅ Daily workout habit formation (intended)
- ⚠️ Logging minimal workouts just to maintain the streak
- 🔴 Workout anxiety on rest days, injury risk from exercising sick to avoid reset
- 🟣 Social competition dynamics that make rest feel like failure across a social group

**Non-obvious cascade:** After 3 months, users with lower streaks stop opening the app entirely because the streak gap has become too demotivating to close. The feature that was intended to build habit succeeds for high-adherence users and fails completely for moderate-adherence users — the group who needed the habit-building support most.

**Redesign directions:**
- **Direction A (minimal):** Add rest days to the streak counter ("active streak: 47 days with 8 rest days") to normalize recovery
- **Direction B (structural):** Remove streak visibility from social profile; make it a private metric only the user sees

---

## See also

- [Motivation Matrix](motivation-matrix.md) — maps what motivates users generally; Inverted Behavior Model maps how specific features activate and exploit those motivations
- [Worrystorming](worrystorming.md) — generates worries about a feature; Inverted Behavior Model provides a structured forecast to validate or refute them
- [Humane Design Guide](humane-design-guide.md) — flags which human sensitivities are being exploited; Inverted Behavior Model explains the behavioral mechanism of that exploitation

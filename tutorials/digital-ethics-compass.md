# Digital Ethics Compass

**The short version:** A health check for any digital product — five principles and 22 questions in three categories (Data, Automation, Behavioral Design) — that tells you where the ethical weak spots are and why they're happening.

---

## Who made it

The Digital Ethics Compass is a toolkit from the Danish Design Center (DDC, 2021), published free on ddc.dk under a Creative Commons Attribution License (version not stated on the site). Its checklist, the Ethics Navigator, puts five principles in the middle — Put the Human at the Center, Avoid manipulating, Make your technology understandable, Avoid creating inequality, Give users control — and 22 questions in the outer ring, grouped into Data (6), Automation (10) and Behavioral Design (6). DDC also offers a facilitated ethics workshop; this skill covers the checklist only.

The skill follows DDC's structure and adds an audit workflow around it (see the edbx additions below).

---

## The problem it solves

Digital products have a lot of ethical surface area. It's hard to know where to look first, and easy to audit in one area (say, privacy) while missing everything in another (say, manipulation). The Digital Ethics Compass solves this by organizing the audit into five principles and three clear categories — ensuring nothing gets skipped by default.

What the edbx skill adds on top of the published compass is what it does with the findings: for every problem identified, it names the specific business metric, KPI, or organizational pressure driving the failure. That's the insight most audits miss. It's not enough to say "this feature is manipulative." You need to say *why it was built that way*, because that's what needs to change.

---

## When to use it

- **During a product review** — as a structured ethical health check alongside functionality and performance reviews
- **Before launch** — to identify ethical weak spots with enough time to address them
- **When the team has vague ethics concerns but can't articulate them** — the principles and categories provide a scaffold
- **When you need to present ethical findings to stakeholders who don't speak ethical design language** — the principles and categories are accessible and concrete
- **When you're auditing an existing product for the first time** — the compass gives comprehensive coverage fast

---

## What it produces

The first three steps below are edbx additions, not part of DDC's published compass. Before working through the principles and questions, the skill requires three structural artifacts. Without them, the analysis stays abstract.

**Step 0 — Stakeholder & Power Map:** Enumerate every population the design touches — minimum 5 distinct named stakeholders, with vulnerable subgroups named specifically (not "users" generically: minors, neurodivergent learners, people in foster care, divorced co-parents, undocumented users, abuse survivors, etc. — pick 2–4 actually relevant). For each: relationship to the product, power they have, power they lack, and what they would lose if harmed. Plus a power-asymmetry summary and a **historical-justice prior** naming any pattern from history where similar products harmed similar populations.

**Step 0.5 — Objective Function Risk Table:** Name what the product is *actually* optimized for vs. what it's stated to be for. Stated mission ≠ optimized objective. *"Help children learn"* may stop being the operative goal once metrics like time-on-platform and recommendation CTR take over. The table maps stated objective → optimized objective → conflicting stakeholder value → drift mechanism (how the system worsens over time on this conflict) → mitigation owner.

**Step 0.6 — Non-Obvious Harms Inventory (minimum 5 named):** Catches harms the compass questions miss — inferred-data harms, aggregation harms, proxy-variable harms, competence foreclosure, intrinsic-motivation crowd-out, attentional-architecture formation, social-fabric harms, future-you harms, bystander harms, worker harms.

Then the compass itself. First a short reading against the five principles, then the three categories:

**Data (6 questions):** Is collection proportionate and time-limited? Is the data anonymised, and how is it stored? Can people access their own data? Is permission real and informed? Do users know how they are profiled?

**Automation (10 questions):** Do users know it is automated? Does it comply with law and human rights? Does it erode skills people need for their jobs? Can people see inside the "engine room", and can the system explain itself? Are the algorithms prejudiced? Is the risk unnecessarily high? Is someone ready to step in when it fails, can it adapt to change, and can it be hacked?

**Behavioral Design (6 questions):** Does the design play on negative emotions (fear, urgency)? Does it make information hard to find or understand (dark patterns)? Does it exploit people's limited concentration or their need to be social? Is it creating addiction with cheap tricks? Does it validate users or challenge them?

For each category, the audit identifies:
- **What's failing** (with a 🔴/🟡/🟢 severity rating, referencing the named stakeholders most affected — not "users" generically)
- **The specific business pressure driving the failure** — KPI, engagement metric, or investor expectation
- **The implementation type** — Quick Win / Strategic Fix / Requires Leadership

The output includes the **Business Pressure Attribution table** linking each failure to its driver, and a **Priority Improvements list** ranked by severity and effort. Each category references Step 0 stakeholders rather than restating the analysis.

---

## The key insight

The most important thing this skill adds to the compass is to name the *business cause* of each ethical problem. "This checkout flow is manipulative" is analysis. "This checkout flow is manipulative because the team is measured on conversion rate with no counterbalancing metric for user regret" is actionable. The second statement tells you what needs to change to fix it structurally, not just cosmetically.

---

## How to use it with AI

Describe your product — what it does, how it makes money, key features, ethical situation. Ask for a Digital Ethics Compass audit. The AI will produce the Stakeholder & Power Map, Objective Function Risk Table, and Non-Obvious Harms Inventory first, then read the product against the five principles and work through all three categories referencing the named stakeholders, rate severity, and attribute each failure to the business pressure driving it.

---

## A quick example

**Product:** A free productivity app that offers premium features and sells anonymized usage data to third parties.

**Data findings 🔴:**
- Data sold to third parties is disclosed only in paragraph 47 of the ToS
- "Anonymized" data is re-identifiable when combined with third-party sources
- **Business pressure driving this:** Revenue from data sales funds the free tier; removing this income stream requires a new business model

**Behavioral Design findings 🔴:**
- Premium upsell appears mid-task, when users are most invested in completing something
- Free tier features are degraded in ways not disclosed before signup
- **Business pressure driving this:** Conversion rate to premium is the primary growth metric

**Principle "Make your technology understandable" 🟡:**
- The pricing page doesn't show feature degradation until after free signup
- **Business pressure driving this:** High-friction disclosure hurts conversion in A/B tests

**Priority Improvements:**
- 🟢 Quick Win: Add a feature comparison table to the signup page
- 🔵 Strategic Fix: Create a plain-language data use summary (not ToS paragraph 47)
- 🔴 Requires Leadership: Evaluate whether data sales can be replaced by a transparent paid data tier

---

## See also

- [Fair Patterns](fair-patterns.md) — Dark pattern identification in more depth; the Compass covers manipulation broadly (Behavioral Design questions), Fair Patterns goes into detail
- [Humane Design Guide](humane-design-guide.md) — six-sensitivity audit for psychological harm; pairs with the Behavioral Design category
- [Responsible Design Prism](responsible-design-prism.md) — gives an overall ethical posture rating; the Compass breaks down, category by category, where that posture fails

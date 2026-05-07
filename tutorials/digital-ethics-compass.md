# Digital Ethics Compass

**The short version:** A four-direction health check for any digital product — north (data), south (manipulation), east (transparency), west (automation) — that tells you where the ethical weak spots are and why they're happening.

---

## Who made it

The Digital Ethics Compass is a structured audit framework for digital products built around four categories of ethical risk that consistently appear in digital product design: data practices, manipulative design, transparency and honesty, and automation and algorithmic decision-making.

The framework synthesizes ethical design research across multiple traditions — privacy law, persuasive technology ethics, transparency advocacy, and AI fairness — into a practical, team-usable audit format.

---

## The problem it solves

Digital products have a lot of ethical surface area. It's hard to know where to look first, and easy to audit in one area (say, privacy) while missing everything in another (say, manipulation). The Digital Ethics Compass solves this by organizing the audit into four clear directions — ensuring nothing gets skipped by default.

What makes it useful is not just the four categories, but what it does with the findings: for every problem identified, it names the specific business metric, KPI, or organizational pressure driving the failure. That's the insight most audits miss. It's not enough to say "this feature is manipulative." You need to say *why it was built that way*, because that's what needs to change.

---

## When to use it

- **During a product review** — as a structured ethical health check alongside functionality and performance reviews
- **Before launch** — to identify ethical weak spots with enough time to address them
- **When the team has vague ethics concerns but can't articulate them** — the four-category structure provides a scaffold
- **When you need to present ethical findings to stakeholders who don't speak ethical design language** — the four directions are accessible and concrete
- **When you're auditing an existing product for the first time** — the compass gives comprehensive coverage fast

---

## What it produces

Before walking the four directions, the compass requires three structural artifacts. Without them, the analysis stays abstract.

**Step 0 — Stakeholder & Power Map:** Enumerate every population the design touches — minimum 5 distinct named stakeholders, with vulnerable subgroups named specifically (not "users" generically: minors, neurodivergent learners, people in foster care, divorced co-parents, undocumented users, abuse survivors, etc. — pick 2–4 actually relevant). For each: relationship to the product, power they have, power they lack, and what they would lose if harmed. Plus a power-asymmetry summary and a **historical-justice prior** naming any pattern from history where similar products harmed similar populations.

**Step 0.5 — Objective Function Risk Table:** Name what the product is *actually* optimized for vs. what it's stated to be for. Stated mission ≠ optimized objective. *"Help children learn"* may stop being the operative goal once metrics like time-on-platform and recommendation CTR take over. The table maps stated objective → optimized objective → conflicting stakeholder value → drift mechanism (how the system worsens over time on this conflict) → mitigation owner.

**Step 0.6 — Non-Obvious Harms Inventory (minimum 5 named):** Catches harms the heuristic categories miss — inferred-data harms, aggregation harms, proxy-variable harms, competence foreclosure, intrinsic-motivation crowd-out, attentional-architecture formation, social-fabric harms, future-you harms, bystander harms, worker harms.

Then the compass covers four directions:

**North — Data:** Collection, use, storage, sharing. Proportionate to value delivered? Do users understand what they're agreeing to?

**South — Manipulation:** Dark patterns, attention exploitation, fear triggers, social pressure. Where is design serving the system at the expense of users?

**East — Transparency:** Does the product tell users what it's doing and why? Are algorithmic decisions explained? Is pricing honest? Are conflicts disclosed?

**West — Automation:** Where does the product make decisions for users? Is human judgment available when automation fails? Are assumptions documented?

For each direction, the audit identifies:
- **What's failing** (with a 🔴/🟡/🟢 severity rating, referencing the named stakeholders most affected — not "users" generically)
- **The specific business pressure driving the failure** — KPI, engagement metric, or investor expectation
- **The implementation type** — Quick Win / Strategic Fix / Requires Leadership

The output includes the **Business Pressure Attribution table** linking each failure to its driver, and a **Priority Improvements list** ranked by severity and effort. Each category references Step 0 stakeholders rather than restating the analysis.

---

## The key insight

The most important thing the compass does is name the *business cause* of each ethical problem. "This checkout flow is manipulative" is analysis. "This checkout flow is manipulative because the team is measured on conversion rate with no counterbalancing metric for user regret" is actionable. The second statement tells you what needs to change to fix it structurally, not just cosmetically.

---

## How to use it with AI

Describe your product — what it does, how it makes money, key features, ethical situation. Ask for a Digital Ethics Compass audit. The AI will produce the Stakeholder & Power Map, Objective Function Risk Table, and Non-Obvious Harms Inventory first, then walk all four directions referencing the named stakeholders, rate severity, and attribute each failure to the business pressure driving it.

---

## A quick example

**Product:** A free productivity app that offers premium features and sells anonymized usage data to third parties.

**North (Data) findings 🔴:**
- Data sold to third parties is disclosed only in paragraph 47 of the ToS
- "Anonymized" data is re-identifiable when combined with third-party sources
- **Business pressure driving this:** Revenue from data sales funds the free tier; removing this income stream requires a new business model

**South (Manipulation) findings 🔴:**
- Premium upsell appears mid-task, when users are most invested in completing something
- Free tier features are degraded in ways not disclosed before signup
- **Business pressure driving this:** Conversion rate to premium is the primary growth metric

**East (Transparency) findings 🟡:**
- The pricing page doesn't show feature degradation until after free signup
- **Business pressure driving this:** High-friction disclosure hurts conversion in A/B tests

**Priority Improvements:**
- 🟢 Quick Win: Add a feature comparison table to the signup page
- 🔵 Strategic Fix: Create a plain-language data use summary (not ToS paragraph 47)
- 🔴 Requires Leadership: Evaluate whether data sales can be replaced by a transparent paid data tier

---

## See also

- [Fair Patterns](fair-patterns.md) — Dark pattern identification in more depth; the Compass covers manipulation broadly, Fair Patterns goes into detail
- [Humane Design Guide](humane-design-guide.md) — six-sensitivity audit for psychological harm; pairs with the South (Manipulation) direction
- [Responsible Design Prism](responsible-design-prism.md) — gives an overall ethical posture rating; the Compass gives a directional breakdown of where the posture breaks down

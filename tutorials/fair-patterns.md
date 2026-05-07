# Fair Patterns

**The short version:** A structured audit that finds the dark patterns — manipulative design tactics — in your product, traces them back to their organizational root causes, maps them to legal risk, and produces a prioritized remediation plan.

---

## Who made it

Fair Patterns is grounded in the systematic dark pattern research of **Colin M. Gray, Aarron Walter, and colleagues** (Gray et al., 2024) and **Harry Brignull's** influential dark patterns taxonomy (Brignull, 2023). Brignull coined the term "dark patterns" in 2010 and built the foundational taxonomy that most audit frameworks draw on.

The method adapts this research into a tool that goes beyond identification — adding organizational root cause analysis and legal compliance mapping to make the findings actionable at the organizational level, not just the design level.

---

## The problem it solves

Dark patterns are everywhere. Trick questions, hidden costs, forced continuity, confirmshaming, roach motel flows — most digital products have at least a few. But most teams that audit for dark patterns stop at identification: "we found this dark pattern." That's necessary but not sufficient.

The harder question is: *why was this dark pattern built?* The answer is almost always organizational. A dark pattern doesn't appear because a designer decided to manipulate users. It appears because the team was measured on a metric (conversion rate, trial-to-paid, churn rate) that rewarded building it, and nobody had a counterbalancing metric that would penalize user harm.

Fair Patterns surfaces both the dark pattern and the organizational decision that created it. That's what makes remediation possible — not just for this instance, but for the system that keeps producing them.

---

## When to use it

- **During a product audit** — to find patterns you might have normalized and stopped seeing
- **Before a legal or compliance review** — to identify dark patterns that may violate GDPR, FTC regulations, CCPA, or DSA before regulators find them
- **When users are complaining about feeling tricked** — to diagnose what's creating that experience systematically
- **Before a product launch** — to ensure manipulative patterns aren't shipped under business pressure
- **When a new team member says "wait, why do we do it this way?"** — that question often surfaces a dark pattern that the team has stopped questioning

---

## What it produces

Fair Patterns works in seven steps:

1. **Dark pattern identification** — scan the product for patterns from the established taxonomy (trick questions, hidden costs, forced continuity, misdirection, social proof manipulation, urgency manufacturing, confirmshaming, roach motel, etc.)

2. **Root cause analysis** — for each dark pattern found, identify the upstream business decision or KPI that created it. "Trick questions come from a conversion KPI with no retention counterbalance."

3. **Legal compliance mapping with jurisdiction + penalty specificity** — for every dark pattern, name the specific statute (article number, not just "GDPR"), the jurisdiction, and the penalty exposure. Examples: GDPR Art. 7(3) on consent withdrawal in the EU (penalty up to 4% global turnover); EU Omnibus Directive 2019/2161; FTC Act §5 on deceptive practices in the US; CCPA §1798.140 in California; DSA Art. 25 banning dark patterns for VLOPs (penalty up to 6%); UK CMA Digital Markets Act; Brazilian LGPD. Patterns flagged 🔴 in two or more jurisdictions become must-fix before next release.

4. **Vulnerable Population Harm Matrix** — dark patterns do not harm everyone equally. For each pattern, name **which populations are disproportionately affected** and the mechanism of differential harm (e.g., minors face developmental susceptibility to FOMO; people in financial precarity face stronger sunk-cost loss aversion; people with cognitive disabilities face consent-fatigue exploitation; older adults face default-bias on unfamiliar UIs; users on slow connections experience 3-second delays as friction asymmetry). A pattern that's annoying for typical users but catastrophic for a vulnerable subgroup is rated by the worst case.

5. **Fair pattern design** — for each dark pattern, design the honest alternative. Not just "remove the dark pattern" but "here is the fair version that achieves the legitimate business goal without manipulation."

6. **Implementation sequence + success metrics** — rank fixes by (Legal Risk × User Impact) ÷ Implementation Effort. Every row includes a **measurable success metric with threshold** (e.g., "cancellation flow ≤ 3 clicks; cancellation completion rate ≥ 90%"; "support tickets re: surprise charges ↓ 50% within 90 days"), a **named owner** (role/team), and a **target sprint**. Without measurable thresholds and named owners, the fix isn't testable.

7. **Pattern prevention** — for each root cause, name the organizational change (metric, incentive, review process) that would prevent the pattern from being rebuilt.

---

## The key insight

Dark patterns are organizational symptoms, not design mistakes. A team that finds and removes a dark pattern without addressing the organizational condition that created it will rebuild the same pattern — or a similar one — in the next sprint.

Root cause analysis is what makes Fair Patterns different from a standard dark pattern checklist.

---

## How to use it with AI

Describe your product and the flows you want to audit. If you know specific areas of concern (checkout, trial signup, notification preferences, account deletion), name them. The AI will systematically scan for dark patterns, name their root causes, map the legal exposure, design fair alternatives, and produce a prioritized remediation sequence.

---

## A quick example

**Product:** A subscription service with a free trial that requires credit card on signup.

**Dark patterns found:**

| Dark Pattern | Where | Root Cause | Statute (jurisdiction + penalty) | Risk |
|---|---|---|---|---|
| Hidden continuity | Trial converts to paid with one email notification | Metric: trial-to-paid conversion rate, no churn-rate counterweight | EU: GDPR Art. 7(3) — up to 4% global turnover; DSA Art. 25 (if VLOP) — up to 6%; US: FTC Act §5 (Amazon Prime cancellation case 2023 set precedent) | 🔴 |
| Misdirection | "Cancel anytime" button is harder to find than "upgrade" | UX team rewarded for upgrade clicks, not cancellation completion | EU: DSA Art. 25 explicitly bans hiding cancel option for VLOPs; US: FTC Click-to-Cancel rule | 🟡 |
| Confirmshaming | "No thanks, I don't want to save money" decline button | Copywriter briefed to maximize click-through, not user respect | EU: DSA Art. 25 names confirmshaming as banned dark pattern; US: reputational + state UDAP statutes | 🟢 |

**Vulnerable Population Harm Matrix (excerpt):**
- Hidden continuity disproportionately harms users in financial precarity (overdraft cascade from unexpected charge), older adults (default-bias on unfamiliar billing notifications), and shift workers (notifications missed at off-hours).
- Confirmshaming disproportionately harms adolescents (developmental susceptibility to social shame in copy) and users in cognitive depletion states.

**Fair pattern alternatives:**

- Hidden continuity → Send three notifications before trial ends; require explicit confirmation to continue; show full billing date on signup
- Misdirection → Make "cancel" as visually prominent as "upgrade" in account settings
- Confirmshaming → Replace with neutral language: "No thanks" / "Yes, upgrade"

**Priority sequence with measurable metrics + owners:**

| # | Fix | Legal Risk | Effort | Target metric (with threshold) | Owner | Sprint |
|---|---|---|---|---|---|---|
| 1 | Replace hidden continuity with explicit pre-charge consent | 🔴 | Low | Trial → paid conversion drops within ±10% of pre-redesign baseline (representing informed consent, not manipulation drop); refund requests for surprise charges ↓ 80% within 90 days | Head of Growth + DPO | 24.6 |
| 2 | Make cancel pathway as prominent as upgrade | 🟡 | Medium | Cancel completion rate ≥ 90%; cancel flow ≤ 3 clicks; support tickets re: "can't cancel" ↓ 75% | Account UX lead | 24.7 |
| 3 | Replace confirmshaming copy with neutral language | 🟢 | Low | Copy review checklist applied; flagged copy reviewed by Trust & Safety pre-launch | Content design lead | 24.6 (quick win) |

---

## See also

- [Digital Ethics Compass](digital-ethics-compass.md) — broader four-direction audit that includes manipulation; Fair Patterns goes deeper on dark patterns specifically
- [Humane Design Guide](humane-design-guide.md) — audits psychological harm broadly; Fair Patterns audits manipulative interaction patterns specifically
- [Inverted Behavior Model](inverted-behavior-model.md) — forecasts what behaviors the patterns incentivize; Fair Patterns identifies the patterns themselves

# Severity Assessment Guide

How to rate each consequence category as Significant, Possible, or Low/None during the Bad Design Canvas session.

---

## Severity Levels

### 🔴 Significant

The consequence is **likely to occur**, **severe in impact**, and **currently unaddressed** in the product design.

Assign `🔴 Significant` when:
- The harm is probable, not hypothetical
- The affected population is identifiable and vulnerable
- The product's core mechanics directly contribute to the harm
- No existing design decision mitigates the consequence
- The harm would persist or worsen at scale

A `🔴 Significant` rating requires a redesign recommendation in Step 4.

### 🟡 Possible

The consequence is **possible but uncertain**, **moderate in potential impact**, or **partially addressed** by existing design decisions.

Assign `🟡 Possible` when:
- The harm could happen under specific conditions but is not guaranteed
- The impact would be moderate rather than severe
- Some mitigations exist but are incomplete or untested
- The consequence emerges only at significant scale or in edge cases
- There is ambiguity about whether the product actually causes this harm

A `🟡 Possible` rating should be flagged for monitoring and reconsideration as the product evolves.

### 🟢 Low/None

The consequence is **unlikely**, **minor in impact**, or **well-mitigated** by existing design decisions.

Assign `🟢 Low/None` when:
- The harm is unlikely given the product's design and context
- Any impact would be minor and easily addressed
- Strong mitigations are already in place
- The category genuinely does not apply (with justification)

Never assign `🟢 Low/None` as a way to skip uncomfortable analysis. If you are unsure, default to `🟡 Possible`.

---

## Assessment Principles

### 1. Think at scale

Rate consequences based on what happens when the product succeeds and reaches its target audience at scale, not just at launch with early adopters. Harms often emerge only when a product becomes widely adopted.

### 2. Center the most affected

Rate severity from the perspective of the most affected stakeholder, not the average user. A product that is safe for 95% of users but harmful to 5% may still warrant `🔴 Significant` if the harm to that 5% is severe.

### 3. Separate likelihood from impact

A low-likelihood, high-impact consequence (e.g., a data breach exposing sensitive health data) can still warrant `🔴 Significant` because the impact, if it occurs, is catastrophic. Do not downgrade severity just because something is unlikely.

### 4. Consider compounding effects

Some consequences compound when they interact. Cultural Appropriation + Exploitation + Inequity together are more severe than each individually. When consequences cluster, consider upgrading the severity of the cluster.

### 5. Do not downgrade for "good intentions"

A product designed with good intentions can still cause significant harm. Rate the consequence, not the intent behind the product.

---

## Common Rating Mistakes

| Mistake | Correction |
|---|---|
| Rating everything 🟡 to avoid commitment | If you are unsure, default to 🟡 but flag for investigation. If the evidence points to harm, use 🔴. |
| Rating everything 🟢 for "well-designed" products | Even well-designed products can have unintended consequences. The canvas exists to find what the team missed. |
| Rating based on how fixable the problem is | Severity is about the harm, not the solution. A fixable `🔴` is still `🔴`. |
| Downgrading because "users consented" | Consent under power asymmetry or information asymmetry is not meaningful consent. Rate the harm. |
| Treating 🟢 as "skip" | Every cell must have a specific, product-grounded response. 🟢 means "unlikely or well-mitigated," not "ignored." |

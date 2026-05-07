# Value Reframing Guide

How to convert worry clusters into ethical objectives, design constraints, and test questions. The reframing step is the emotional core of Worrystorming — it converts anxiety into agency.

---

## The Three Artifacts

For each worry cluster, produce three things:

### 1. Ethical Objective

A commitment statement in the format: **"We commit to [X] in order to avoid [Y]."**

The objective should be:
- **Affirmative** — state what you will do, not just what you won't
- **Specific** — concrete enough to guide a design decision
- **Connected to the worry** — the "in order to avoid" clause links directly to the original concerns

**Examples:**
- Cluster: "Data privacy fears" → "We commit to user-controlled data deletion within 30 seconds to avoid accumulating data that users cannot reclaim."
- Cluster: "Algorithmic bias concerns" → "We commit to publishing quarterly bias audits to avoid invisible discrimination against protected groups."
- Cluster: "Worker surveillance worries" → "We commit to aggregate-only productivity metrics to avoid creating a surveillance culture that erodes trust."

### 2. Design Constraint

A concrete requirement or rule the design must satisfy. This is the operational version of the ethical objective — what must be true in the product for the commitment to hold.

Characteristics of a good design constraint:
- **Testable** — you can verify whether the product satisfies it
- **Specific** — not "be more private" but "all data sharing requires explicit opt-in with a clear explanation of what is shared and with whom"
- **Non-negotiable** — this is a hard boundary, not an aspiration

**Examples:**
- "Users must be able to export all their data in a standard format within one click."
- "No content recommendation may be based on emotional state inference without explicit user consent."
- "Cancellation must require no more steps than subscription."
- "Every algorithmic decision that affects a person must include a human-readable explanation."

### 3. Test Question

A question in the format: **"How would we know if we failed at [this commitment]?"** — answerable through testing, research, or audit.

Characteristics of a good test question:
- **Answerable** — not philosophical but empirical
- **Observable** — you could collect evidence to answer it
- **Specific** — not "are we ethical?" but "can a user who cannot use a mouse complete the checkout flow?"

**Examples:**
- "Can a user who signed up yesterday find and complete the data deletion flow without contacting support?"
- "Would a member of [affected community] describe this feature as respectful?"
- "If we ran a blind audit of algorithmic outcomes, would we find demographic disparities?"
- "Does the product work during a network outage for critical user tasks?"

---

## Reframing Examples by Cluster

### Data & Privacy

| Raw Worry | Ethical Objective | Design Constraint | Test Question |
|---|---|---|---|
| "Users don't know what data we collect" | We commit to transparent data practices to avoid eroding user trust | Every data collection point shows what is collected, why, and who sees it | Can a user list all data collected about them without reading documentation? |
| "Data might be used for purposes users didn't agree to" | We commit to purpose-bound data use to avoid scope creep | Data may only be used for the purpose stated at collection time | Is there a mechanism that prevents data reuse for unstated purposes? |

### Environmental Impact

| Raw Worry | Ethical Objective | Design Constraint | Test Question |
|---|---|---|---|
| "Our servers have a growing carbon footprint" | We commit to measuring and offsetting our environmental impact to avoid hidden ecological cost | Publish annual carbon footprint report with reduction targets | Do we know our per-user carbon cost, and is it decreasing year over year? |

### Psychological

| Raw Worry | Ethical Objective | Design Constraint | Test Question |
|---|---|---|---|
| "The streak mechanic creates compulsive checking" | We commit to supporting healthy engagement patterns to avoid creating dependency | No engagement mechanic may penalize absence for more than 24 hours | Would a user who takes a week off feel welcomed back or punished? |
| "Comparison features create anxiety" | We commit to non-comparative design to avoid social pressure | All social features must have a private mode that hides comparative metrics | Can a user use all core features without ever seeing another user's metrics? |

---

## Common Reframing Pitfalls

**Too vague:** "We commit to being more ethical" → Instead, name the specific commitment: "We commit to explicit opt-in for all data sharing."

**Too narrow:** "We will add a privacy policy link" → Instead, focus on the outcome: "Users will understand what data is collected before they provide it."

**Untestable:** "We will respect user autonomy" → Instead, make it verifiable: "Every automated decision that affects a user includes a one-click override."

**Aspirational without constraint:** "We value user privacy" → Values without constraints are just sentiments. Add the specific rule: "We value user privacy, so all data sharing requires explicit opt-in."

# Systemic vs. Addressable Findings

How to distinguish between consequences that require fundamental redesign and those that can be mitigated through specific design changes.

---

## Definitions

### Systemic Findings

A consequence is **systemic** when it is produced by the product's core concept, business model, or fundamental mechanics. Addressing it requires rethinking what the product is, not just how it works.

**Characteristics:**
- The harm originates from the product's reason for existing
- Removing the harm would change the product's core value proposition
- The business model depends on the mechanism causing the harm
- The harm is not a bug but a feature of the design

**Example:** A gig economy platform where the core business model depends on worker precarity. Fair labor practices would change what the product is.

### Addressable Findings

A consequence is **addressable** when it can be mitigated through specific, scoped design changes without rethinking the product's core concept.

**Characteristics:**
- The harm is caused by a specific feature or design decision
- An alternative design exists that preserves the product's value
- The fix is scoped and implementable within the current concept
- The business model does not depend on the harmful mechanism

**Example:** A social platform that defaults to public profiles. Making profiles private by default addresses the privacy harm without changing what the product is.

---

## Classification Framework

For each `🔴 Significant` finding, ask these four questions:

### 1. Origin Test
**Where does the harm come from?**
- If the harm comes from a specific feature or interaction → likely **Addressable**
- If the harm comes from the core concept or business model → likely **Systemic**

### 2. Removal Test
**What happens if we remove the harm?**
- If the product still works and delivers value → likely **Addressable**
- If the product's value proposition collapses → likely **Systemic**

### 3. Stakeholder Test
**Who benefits from the status quo?**
- If only a specific feature benefits → likely **Addressable**
- If the company's revenue model or competitive advantage depends on it → likely **Systemic**

### 4. Scale Test
**What happens at 10x scale?**
- If the harm stays proportional → likely **Addressable**
- If the harm compounds or cascades → consider upgrading to **Systemic**

---

## Common Classification Patterns

| Consequence Category | Often Systemic When | Often Addressable When |
|---|---|---|
| Cultural Appropriation | The product's brand identity depends on borrowed cultural elements | Specific imagery or language can be replaced |
| Band-Aid | The product's existence depends on the root problem persisting | The product could be repositioned to address root causes |
| Unfair Control | Lock-in is the business model | Lock-in is a default setting that can be changed |
| Exploitation | Users are the product being sold | Data practices can be redesigned |
| Inefficiency | Complexity is used to obscure harm | UX can be simplified |
| Environmental & Social Impact | The product's operation inherently consumes significant resources | Specific processes can be optimized |
| Stakeholder Abandonment | The product deliberately excludes certain stakeholders | Affected stakeholders can be included in design |
| Decreased Safety | Risk is inherent to the product's function | Safety mechanisms can be added |
| Inappropriate | The product's tone or approach is fundamentally misaligned | Content or framing can be adjusted |
| Boring | N/A (not a systemic concern) | Creative ambition can be increased |
| Displacement | Displacement is the product's mechanism (replacing X with Y) | Transition support can be added |
| Inequity | The product's pricing or access model excludes populations by design | Accessibility and pricing can be adjusted |

---

## When Systemic Findings Mean "Do Not Build"

A systemic finding does not automatically mean the product should not be built. It means the team must decide:

1. **Can the core concept be revised?** Is there a version of this product that delivers value without the systemic harm?
2. **Is the harm justified by the benefit?** Rarely, but sometimes a product causes some harm while providing significant benefit. The question is whether the harm is proportional and whether those harmed are the same as those benefited.
3. **Who bears the cost?** If the people harmed are different from the people benefited, the systemic finding is more serious.
4. **Is there a "less bad" version?** Can the concept be modified to reduce the severity of the systemic harm, even if it cannot be eliminated?

If the answer to all four questions is no, the verdict should be **"Do not build."**

---

## Documenting the Classification

For each `🔴 Significant` finding in the canvas output, include:

```
**[Category Name] — 🔴 Significant (Systemic / Addressable)**
- Origin: [where the harm comes from]
- Classification reasoning: [why this is systemic or addressable]
- If Systemic: [does this suggest the product should not be built?]
- If Addressable: [what specific design change would mitigate it?]
```

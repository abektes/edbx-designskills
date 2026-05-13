---
name: edbx-fair-patterns
description: Use when a designer wants to audit a product for dark or deceptive UI patterns, find the ethical alternative to a known dark pattern, apply fair pattern countermeasures that restore user agency, evaluate defaults as harmful vs. protective, rewrite manipulative UI language into plain and empowering language, or map a product's deceptive patterns against a taxonomy of known dark pattern types. Identify dark patterns in a digital product or service and apply fair pattern countermeasures to correct them. Trigger this skill for any mention of dark patterns, deceptive design, manipulative UI, user agency, roach motel, confirmshaming, hidden costs, forced continuity, privacy zuckering, or when someone says "is this pattern manipulating our users?" Also trigger for "Fair Patterns", "dark patterns audit", "deceptive design", "manipulative UI", "user agency", or "ethical UI patterns".
version: "1.0"
tags: [ethical-design, audit]
---

# Fair Patterns

## Overview

Fair Patterns enable you to identify and correct instances of dark or deceptive patterns in digital products or services by employing fair countermeasures that positively impact users' agency. Fair Patterns were created as an ethical alternative pattern perspective, using dark patterns as areas where we encounter problematic practices.

Dark patterns are deceptive interface features or flows that redirect users against their own interests. Fair Patterns are the countermeasures — designed to identify instances when dark patterns impact users and correct them within a power-sharing perspective, using clear language that users can understand.

The method operates as both an **audit tool** (identifying existing dark patterns) and a **generation tool** (producing fair alternatives). It maps directly to the Gray et al. (2024) ontology of dark pattern types, providing a structured taxonomy for identification and a set of seven fair pattern types for remediation.

> **Mindset check:** Dark patterns don't always result from malicious intent. They often emerge from misaligned incentives, design defaults, or thoughtless iteration. The goal is to identify and fix them — not to shame designers.

## Use This Skill When

- You want to audit a product for dark or deceptive UI patterns.
- You need to find the ethical alternative to a known dark pattern.
- You are applying fair pattern countermeasures that restore user agency.
- You want to evaluate defaults as harmful vs. protective.
- You need to rewrite manipulative UI language into plain and empowering language.
- You want to map a product's deceptive patterns against a taxonomy of known types.

## Inputs

Provide as many of these as are available:

- A product, feature, or UI flow to audit
- Optionally: a specific pattern of concern (e.g., "our cookie banner", "our cancellation flow")
- Optionally: a known dark pattern type to find countermeasures for
- Optionally: a user population whose agency is being affected

## Workflow

Fair Patterns operates in four steps.

---

### Step 1 — Dark Pattern Identification

Audit the product/feature against the major dark pattern taxonomy:

| Dark Pattern Type | Description | Example |
|---|---|---|
| **Trick Questions** | Confusing opt-in/opt-out language | Checkbox worded to mean the opposite of what it appears |
| **Roach Motel** | Easy to get in, hard to get out | 1-click subscribe, 5-step cancel |
| **Privacy Zuckering** | Tricking users into sharing more data than intended | Default "share with everyone" |
| **Misdirection** | Attention drawn away from key information | Prominent "Accept All", tiny "Manage" |
| **Confirmshaming** | Guilt-tripping users into compliance | "No thanks, I don't want to save money" |
| **Disguised Ads** | Ads styled as content or navigation | Sponsored results styled as organic |
| **Forced Continuity** | Charging after free trial without clear notice | No reminder before billing starts |
| **Hidden Costs** | Revealing extra charges at final step | Fees added at checkout |
| **Bait and Switch** | Advertising one thing, delivering another | "Free" with undisclosed conditions |
| **Urgency/Scarcity** | False time pressure or stock claims | "Only 2 left!" (always shows 2) |

For each identified dark pattern: name it, describe how it manifests, name the user agency being stolen.

---

### Step 2 — Apply Fair Pattern Countermeasures

For each identified dark pattern, generate the fair pattern countermeasure:

| Fair Pattern Type | Application |
|---|---|
| **Plain and Empowering Language** | Rewrite manipulative copy into clear, honest language the user can understand and act on |
| **Nonobstructive Information** | Remove emotional, temporal, or social triggers that manipulate; present information neutrally |
| **Summary Path** | Redesign the task flow to support user goals, not obstruct them |
| **Adequate Information** | Give users the information they need to make genuine decisions at the moment they need it |
| **Protective Default** | Set defaults in the user's interest, not the business's interest |
| **Free Action** | Give users genuine control over their path and goals without pressure or manipulation |
| **Fair UX** | Reorder visual hierarchy so the honest choice is as accessible as the manipulative one |

---

### Step 2.5 — Root Cause Reframe

For each dark pattern found, identify the upstream organizational decision that created it. Dark patterns rarely emerge from malicious intent — they emerge from misaligned incentives. Naming the root cause is what enables a structural fix rather than a cosmetic one.

Format:
> *"[Dark Pattern Type] exists because [upstream business decision / KPI / default process] created the incentive to [exploit user in this specific way]."*

Examples:
- "Roach Motel exists because the cancellation flow was owned by a retention team whose KPI was cancellation rate, not user satisfaction."
- "Privacy Zuckering exists because the default for new features is 'share everything' and opting into privacy requires a separate engineering sprint that never gets prioritized."

**Output:** One root cause statement per dark pattern found.

### Step 2.6 — Legal Compliance Mapping (with jurisdiction + penalty specificity)

Vague references to "consent law" are not useful. For each dark pattern found, name the **specific statute or article**, the **jurisdiction it applies in**, and the **penalty exposure**. If you do not know the exact penalty, name the regulator and that an enforcement action is possible — do not invent numbers.

| Dark Pattern | Statute / Article (named, not generic) | Jurisdiction | Penalty exposure | Recent enforcement (if known) | Risk |
|---|---|---|---|---|---|
| [pattern] | e.g., GDPR Art. 7(3) (right to withdraw consent), EU Omnibus Directive 2019/2161, FTC Act §5 (deceptive practices), CCPA §1798.140, DSA Art. 25 (dark patterns ban for VLOPs), UK CMA Digital Markets Act, Brazilian LGPD Art. 9 | EU/UK/US-federal/US-CA/Brazil/etc. | e.g., GDPR up to 4% global turnover; DSA up to 6%; FTC consent decrees + per-violation fines | e.g., Amazon Prime cancellation FTC case 2023 | 🔴/🟡/🟢 |

Flag any pattern with 🔴 risk in two or more jurisdictions as **must-fix before next release**. List of named patterns explicitly banned by the EU DSA (for VLOPs): pre-checked boxes, repeated nagging after declined consent, hiding the cancel option, false urgency, and confirmshaming.

### Step 2.7 — Vulnerable Population Harm Matrix

Dark patterns do not harm everyone equally. For each pattern identified, name **which populations are disproportionately affected** and how. Generic "users" is not enough.

| Pattern | Disproportionately harmed populations (named) | Mechanism of differential harm |
|---|---|---|
| [pattern] | e.g., minors (developmental susceptibility to FOMO), people in financial precarity (sunk-cost loss aversion hits harder), people with cognitive disabilities (consent-fatigue exploitation), older adults (default-bias + unfamiliar UI), users on slow connections (3-second delays act as friction asymmetry), shift workers (late-night cognitive load) | [specific mechanism — e.g., "executive function depletion at hour 22 doubles susceptibility to confirmshaming"] |

A pattern that's annoying for typical users but catastrophic for a vulnerable subgroup is rated by the worst case, not the average.

### Step 3 — Default Assessment

For each UI element: classify the current default as:
- `🔴 Harmful Default` — default is against user interest
- `🟡 Neutral Default` — default is neither helpful nor harmful
- `🟢 Protective Default` — default is in user's interest

Generate a protective default recommendation for every `🔴 Harmful Default`.

---

### Step 4 — Output

Produce a dark pattern audit, fair countermeasure map, default assessment, and rewritten copy.

---

## Output Format

### Fair Patterns Audit: [Product/Feature Name]

### Dark Pattern Audit

| # | Pattern Type | Manifestation | Agency Stolen |
|---|---|---|---|
| 1 | [type] | [how it manifests] | [what user agency is lost] |

### Fair Pattern Countermeasure Map

| Dark Pattern | Fair Pattern Type | Specific Redesign |
|---|---|---|
| [pattern] | [countermeasure type] | [concrete redesign] |

### Default Audit

| UI Element | Current Default | Recommended Default |
|---|---|---|
| [element] | 🔴 Harmful / 🟡 Neutral / 🟢 Protective | [protective recommendation] |

### Copy Rewrite (Before → After)

**Before:** "[manipulative copy]"
**After:** "[fair copy]"

### Fair Design Statement

*"This product currently uses [X dark patterns] that harm user agency in [Y ways]. The following fair pattern countermeasures restore user autonomy: [Z]."*

### Vulnerable Population Harm Matrix

(From Step 2.7 — required output, not optional.)

| Pattern | Disproportionately harmed populations | Mechanism of differential harm |
|---|---|---|

### Implementation Sequence + Success Metrics

Rank all fair pattern fixes by priority: (Legal Risk × User Impact) ÷ Implementation Effort

| Priority | Fix | Legal Risk | User Impact | Effort | Target metric (with threshold) | Owner | Sprint |
|---|---|---|---|---|---|---|---|
| 1 | [fix] | 🔴/🟡/🟢 | High/Med/Low | Low/Med/High | e.g., "Cancellation completion rate ≥ 90%; cancellation flow ≤ 3 clicks"; "Opt-in rate after redesign represents informed consent within ±10% of pre-redesign baseline (not a manipulation drop)"; "Customer support tickets re: surprise charges ↓ 50% within 90 days" | [role/team] | [target sprint] |

The highest priority fixes are those combining high legal risk with low implementation effort. Every row must include a measurable success metric with a threshold — without it, the fix has no way to verify it landed.

## Guardrails

- Do not assume dark patterns are always intentional. Many emerge from defaults or thoughtless iteration.
- Do not flag every persuasive element as a dark pattern. Not all nudges are manipulative.
- Do not stop at identification. Every dark pattern must have a fair countermeasure.
- Do not write fair alternatives that are just less-bad versions of the same pattern. The goal is genuine user agency.
- Do not forget to assess defaults. The default setting is often where the manipulation lives.
- Do not ignore copy. Language is the primary tool of confirmshaming and trick questions.

## Deliverable Quality Bar

A strong Fair Patterns audit:

- identifies every dark pattern with a named type from the taxonomy
- provides at least one fair pattern countermeasure for every dark pattern found
- names the root cause (upstream business decision or incentive) behind every dark pattern found
- names the **specific statute** (article number) for every dark pattern flagged — not just "GDPR" but "GDPR Art. 7(3)"
- names the **jurisdiction** for each legal mapping (EU / UK / US-federal / US-CA / Brazil / etc.)
- includes **penalty exposure** (percentage of turnover, fine ranges, or named enforcement actions) — never invents specific dollar figures
- produces the **Vulnerable Population Harm Matrix** with at least 3 named populations per pattern, each with a specific differential-harm mechanism
- recommends a protective default for every 🔴 Harmful Default
- includes rewritten copy for any confirmshaming or trick question language
- produces a Fair Design Statement every session
- produces an Implementation Sequence with a **measurable success metric and threshold** + named owner + target sprint on every row (no metric = the fix isn't testable)
- handles low-dark-pattern products without false positives

## Integration with Other EDBX Skills

- **edbx-responsible-design-prism** diagnoses the ethical spectrum. Fair Patterns provides the specific pattern library for the dark side and its remedies.
- **edbx-worrystorming** generates worries about manipulation. Fair Patterns maps them to named patterns and fixes.
- **edbx-humane-design-guide** flags which sensitivities are exploited. Fair Patterns names the specific pattern doing the exploiting.

## Hashtags

#evaluateoutcomes #applyvalues

## See Also

- Ethical Blueprint
- White Hat Design Patterns

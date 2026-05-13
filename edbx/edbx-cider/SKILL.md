---
name: edbx-cider
description: Use when a designer wants to identify hidden assumptions about user ability, capacity, or environment, audit a design for exclusionary patterns, generate inclusive design alternatives through structured assumption-busting, facilitate a team assumption-sharing session, or grow a shared knowledge base of design biases. Apply the CIDER elicitation framework to surface implicit assumptions embedded in a design, envision how those assumptions exclude users, and generate more inclusive alternatives. Trigger this skill for any mention of inclusive design, exclusionary design, assumption auditing, accessibility assumptions, stereotype checking in design, who is being excluded, or when someone says "I want to make sure this works for everyone." Also trigger for "CIDER", "assumption audit", "who can't use this", "inclusion check", or "accessibility assumptions".
version: "1.0"
tags: [ethical-design, audit]
---

# CIDER

## Overview

CIDER is an assumption elicitation technique that helps designers critically evaluate the implicit beliefs baked into their designs — beliefs about who users are, what they can do, what they have access to, and what environments they operate in. Every design carries assumptions. Most are invisible to the people who made them. CIDER makes those assumptions visible, then uses them as raw material for more inclusive redesign.

The name is an acronym. Each letter maps to a stage: **C**ritique, **I**magine, **D**esign, **E**xpand, **R**epeat. A full CIDER session moves through all five stages in order. The first three (C → I → D) can run as a standalone exercise. The last two (E → R) add team-level synthesis and a second cycle.

CIDER was developed by Oleson, Solomon, Horowitz et al. (2022) as a teaching tool for inclusive design skills. It works equally well in professional practice — anywhere a designer wants to stop guessing about inclusion and start finding out what their design actually assumes.

> **Mindset check:** Assumption-surfacing is a skill to build, not a failure to correct. Every designer carries assumptions. The goal is to get better at finding them, not to feel bad about having them.

## Use This Skill When

- You want to audit a design for assumptions that exclude users.
- You are building something and want to make sure it works for more people than just people like you.
- A team needs a structured way to discuss who they might be leaving out.
- You are facilitating an inclusive design workshop and need a repeatable exercise.
- You want to grow a shared assumption register across a project or organization.
- You have heard "accessibility" or "inclusive design" and want a concrete method, not just a checklist.

## Inputs

Provide as many of these as are available:

- The product, feature, service, interface, or design artifact to evaluate (name + brief description)
- Who the intended users are and in what context they use it
- Any known accessibility issues or user complaints
- Platform and technology constraints
- Whether this is a solo exercise or a team session

If you have multiple artifacts to evaluate, list them — CIDER can run on more than one design in a session.

## Workflow

CIDER runs in five stages. The first three (C → I → D) form the core cycle. Stage E is for team sessions. Stage R closes the loop with a second pass.

---

### Stage C — Critique: Surface Assumptions

Identify the embedded assumptions about users that the design carries. Probe across four categories:

**Ability** — What the user's body and mind can do. Sensory capabilities, motor skills, cognitive processing, language proficiency, emotional state.

**Capacity** — What the user knows and can handle. Technical literacy, domain knowledge, cognitive load tolerance, time availability, familiarity with conventions.

**Environment** — Where and under what conditions the user operates. Connectivity, lighting, noise, physical space, device type, distraction level.

**Resources** — What the user has access to. Money, tools, social support, institutional backing, permissions, time.

For each assumption found, name it in this format:

> "This design assumes the user [X]."

**Minimum output:** 5 named assumptions, spanning at least 3 of the 4 categories.

See `references/assumption-categories.md` for detailed examples per category and `references/five-stages.md` for facilitation guidance.

---

### Stage I — Imagine: Envision Exclusion

Pick one assumption from Stage C. Envision how that assumption could lead to a specific person being excluded.

Name a **specific user** — not "a user with a disability" but "Mariam, a 68-year-old retired teacher with tremor in both hands who uses a tablet on a shaky bus."

Describe the **failure scenario** — what task becomes difficult, impossible, or humiliating? What does the experience actually feel like for that person?

**Requirements:**
- Name a real-seeming person with specific characteristics
- Describe a concrete moment of exclusion, not a general class of problem
- Make the scenario vivid and humanizing — the reader should be able to see it happen

See `references/exclusion-scenario-guide.md` for techniques on writing effective exclusion scenarios.

---

### Stage D — Design: Generate Alternatives

Brainstorm 3–5 redesign ideas that remove reliance on the assumption identified in Stage I.

Span a range of approaches:
- **Low-tech:** Print, signage, physical aids, alternative workflows
- **High-tech:** Algorithms, adaptive interfaces, sensor-based adjustments
- **Systemic:** Policy changes, service model shifts, distribution changes
- **Interaction-level:** UI adjustments, modality switches, timing changes

No idea is too wild at this stage. Generative divergence is the goal. Polish and feasibility come later.

**Minimum output:** 3 numbered redesign proposals.

See `references/inclusive-redesign-patterns.md` for common patterns organized by assumption category.

---

### Stage E — Expand: Build Shared Register (Team Mode)

In team sessions, collect all assumptions surfaced by individual participants into a shared master list.

1. **Pool** — Each participant shares their Stage C assumptions
2. **Deduplicate** — Merge overlapping assumptions, keep distinct ones
3. **Cluster** — Group related assumptions by theme or category
4. **Tag** — Label each with its category (Ability / Capacity / Environment / Resources)
5. **Flag surprises** — Note which assumptions participants found most surprising

**Output:** A structured assumption register (see format below).

This stage is optional for solo designers. Teams benefit from it because different people notice different assumptions — the shared list is almost always longer and more diverse than any individual's.

---

### Stage R — Repeat: Second Cycle

Select a **different assumption** from the Stage E register (or from Stage C if working solo). Repeat Stages I and D with this new assumption.

This second cycle matters because the first assumption designers pick is usually the most obvious one. The second one is often more revealing.

**Output:** A complete I → D cycle with a new exclusion scenario and new redesign proposals.

---

## Output Format

Default structure unless the user asks otherwise:

### CIDER Session: [Design Name]

Brief framing of what was evaluated and the designer's starting assumptions.

### Stage C — Assumptions Surfaced

- "This design assumes the user [assumption 1]." — **[Category]**
- "This design assumes the user [assumption 2]." — **[Category]**
- (minimum 5, spanning at least 3 categories)

### Stage I — Exclusion Scenario

A vivid narrative paragraph naming a specific person and describing their moment of exclusion.

### Stage D — Redesign Proposals

1. [Redesign idea 1]
2. [Redesign idea 2]
3. [Redesign idea 3]

### Stage E — Shared Assumption Register (Team Mode)

| # | Assumption | Category | Surprising? | Source |
|---|-----------|----------|-------------|--------|
| 1 | This design assumes... | Ability | Yes | Participant A |
| 2 | This design assumes... | Capacity | No | Participant B |

### Stage R — Second Cycle

**New assumption selected:** [assumption]

**Exclusion scenario:** [narrative]

**Redesign proposals:**
1. [idea]
2. [idea]
3. [idea]

### Inclusive Design Commitment

One sentence stating which assumption the designer or team commits to removing and how.

> "We commit to [action] because we learned that [assumption] excludes [who]."

---

## Guardrails

- Do not let the four assumption categories become a checklist you speed through. Each category is a lens — spend real time looking through it.
- Do not accept generic exclusion scenarios. "A visually impaired user might struggle" is not a CIDER scenario. Name the person. Describe the moment.
- Do not jump to solutions before fully describing the exclusion. The scenario has to be vivid enough to generate empathy before redesign begins.
- Do not treat all assumptions as equally impactful. The Expand stage helps teams identify which assumptions are most surprising and most exclusionary — prioritize those.
- Do not skip Stage R. The second cycle catches assumptions the first pass missed.
- Do not frame assumptions as failures. Every design has them. Finding them is the skill.

## Deliverable Quality Bar

A strong CIDER session output:

- surfaces at least 5 distinct assumptions spanning at least 3 of the 4 categories
- names a specific person (not a demographic label) in the exclusion scenario
- describes a concrete moment of failure, not a generalized class of problem
- generates at least 3 redesign proposals spanning different approach types (low-tech, high-tech, systemic, interaction-level)
- in team mode, produces a shared register with more assumptions than any individual surfaced alone
- runs a second I → D cycle on a different assumption than the first
- closes with a commitment specific enough to create accountability

## Integration with Other EDBX Skills

- **edbx-anotherlens** surfaces the designer's worldview and biases. CIDER takes those worldview insights and operationalizes them into specific design assumptions about users.
- **edbx-humane-design-guide** audits whether a design exploits sensitivities. CIDER audits whether a design's assumptions about ability, capacity, environment, or resources cause exclusion.
- **edbx-worrystorming** generates a broad landscape of ethical worries. CIDER focuses specifically on exclusion-causing assumptions and generates redesigns.
- **edbx-responsible-design-prism** places a design on an ethical spectrum. CIDER generates concrete redesign ideas to move the design toward the responsible end.
- **edbx-motivation-matrix** maps why users participate. CIDER maps who *cannot* participate — who is structurally excluded before motivation even matters.

## Hashtags

#newperspectives #identifyvalues #designresponsibility

## See Also

- Inclusive Activity Cards
- GenderMag

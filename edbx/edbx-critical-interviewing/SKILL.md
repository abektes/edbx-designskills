---
name: edbx-critical-interviewing
description: Use when a researcher or designer wants to understand the "why" behind participant responses, uncover implicit values and ethical reasoning in design teams or users, prepare interview protocols with lead-off, back-up, emergency, and follow-up questions, identify covert categories around power, ethics, or belief, or probe ethical discomfort and moral reasoning in design practice. Design and facilitate Critical Interviewing protocols that surface the normative and evaluative judgments underlying participants' behaviors, beliefs, and design decisions. Trigger this skill for any mention of interviewing for values, ethical probing in research, understanding designer beliefs, normative research, critical ethnography in design, or when someone says "I need to understand why people make the decisions they do." Also trigger for "Critical Interviewing", "values interview", "ethical probing", "normative interview", or "designer values research".
metadata:
  version: "1.0"
---

# Critical Interviewing

## Overview

Critical Interviewing guides you to deeply explore the "why" behind what your participants tell you, revealing underlying norms and situated forms of reasoning. Unlike standard UX interview methods, Critical Interviewing focuses your attention on the normative and evaluative judgments that people use to justify, motivate, or make sense of their perspective on the world.

Interviewing people can help designers increase empathy and aid in constructing design insights. However, an interview cannot always give you straightforward answers to complex "why" questions that underlie behaviors, beliefs, or worldviews. Critical Interviewing borrows principles from semistructured interviewing while using a different protocol format — one that highlights attention to specific "topic domains" and uses follow-up questions to probe more deeply into constructs.

The method was developed from Carspecken's (1996) critical ethnography framework and adapted for design research contexts. It is the values excavation tool in the ethical design toolkit.

> **Mindset check:** The goal is to understand the participant's ethical worldview on its own terms — not to judge it, not to change it, but to map it with enough precision that design decisions can be grounded in what people actually believe is right.

## Use This Skill When

- You want to understand why participants hold the views they do, not just what they believe.
- You need to surface implicit values, ethical reasoning, or moral judgment in design teams or users.
- You are preparing an interview protocol that probes ethical discomfort or moral reasoning.
- You want to identify covert categories — things you want to understand without asking leading questions.
- You are conducting post-hoc analysis of an interview to distinguish descriptive findings from normative findings.
- You need a live interview support tool that surfaces value-laden language and suggests targeted probes.

## Inputs

Provide as many of these as are available:

- A research topic or domain of interest (e.g., "designer ethics", "data privacy decisions", "accessibility trade-offs")
- A participant type (e.g., designer, product manager, end user, policy stakeholder)
- **Investigation domain** (select one to unlock domain-specific question bank): `Algorithmic System` / `Data Practice` / `Labor Platform` / `Product Feature` / `Organizational Policy`
- Optionally: a specific ethical tension or construct to investigate
- Optionally: a known incident or decision to use as a probe anchor
- Optionally: covert categories the researcher suspects but cannot ask directly
- Optionally: a participant quote or paraphrase for live interview support mode

## Workflow

Critical Interviewing operates in five modes: Protocol Design, Live Interview Support, and Post-Interview Analysis.

---

### Mode 1 — Protocol Design

Build a complete interview protocol with four components:

**A. Lead-off Question**

One concrete, open, non-leading question that invites narrative. Should:
- Invite storytelling ("Tell me about a time when...")
- Anchor in the past or in a specific experience
- Not embed the construct you're investigating

**B. Back-up Question**

An alternative lead-off for if the participant doesn't engage with the first. Same principles, different angle.

**C. Emergency Question**

A reframe for if the participant narrates as an observer or user rather than a practitioner. Redirects to their professional agency: "Have you ever been in a situation where *you* were responsible for..."

**D. Follow-up Question Bank**

8–12 probing questions organized by:
- **Descriptive probes**: What happened? Who was involved? What did you do?
- **Normative probes**: Why did that feel wrong/right? What should have happened?
- **Evaluative probes**: Was that appropriate? What would you do differently?
- **Construct-building probes**: When they use a value word (e.g., "unfair", "wrong", "uncomfortable") → immediately build on it: "When you say [word], what do you mean by that? Why do you think that is [word]?"

> **The construct-building technique is the heart of this method.** When a participant says "that was manipulative" or "it felt wrong", do not paraphrase or reframe. Mirror their exact language and dig into the construct: "When you say manipulative — what made it feel that way to you?"

**E. Covert Category List**

4–6 categories the researcher wants to illuminate without asking directly. Each phrased as:
> *"I want to understand [X] without asking '[leading question]'"*

Example covert categories from the source:
- Perceived role of ethics in design (conflict/support)
- Awareness of ethical role
- Drivers of ethical sensitivity/awareness
- Personal design values or philosophy

**F. Domain-Specific Question Bank**

When an investigation domain is specified, append technical questions that surface what qualitative methods alone will not reach:

- **Algorithmic System:** Ask about proxy variables used as model inputs; training data provenance and collection period; named fairness metrics evaluated at deployment (demographic parity, equalized odds); post-deployment monitoring cadence; who can challenge an automated decision.
- **Data Practice:** Ask about data minimization decisions and who made them; which third parties receive data and under what terms; what happens to data upon account deletion; whether differential privacy or anonymization is applied and at what threshold.
- **Labor Platform:** Ask how worker classification decisions were made; whether workers can see the algorithm affecting their assignment or pay; what appeal mechanisms exist; how income instability was considered in design.
- **Product Feature:** Ask what metric this feature is optimized for; what the perverse-incentive scenario looks like if users game it; which populations were excluded from beta testing; what the rollback criteria are.
- **Organizational Policy:** Ask who has veto power over ethics concerns; what the escalation path is; the last time a policy was changed due to an ethics objection; whether ethics concerns are documented with the same rigor as legal ones.

**G. Interview Sequencing Rationale**

State which stakeholders to interview first and why — order affects what you can ask:
- Interview **impacted users before engineers**: users name their experience before engineers frame it technically.
- Interview **engineers before executives**: engineers will surface technical decisions executives may not know about.
- Interview **frontline workers before policy owners**: frontline workers reveal the gap between policy intent and implementation reality.

Name the dependency tree for the specific participant types in this research context.

**H. Non-Obvious Harms Inventory (required when interviewing about systems that affect protected-class populations)**

Before sending the protocol into the field, enumerate the non-obvious harms the research could surface or fail to surface. Vague "we'll be careful" is not protection. Name:

| Population (specific) | Non-obvious harm the system may cause | Question(s) in the protocol that surface it | Question(s) that may *prevent* surfacing it (and how to avoid them) |
|---|---|---|---|

Examples of non-obvious harms to scan for:
- **Proxy-variable harms**: zip code → race; school name → class; browser language → immigration status; battery model → income. Each can produce disparate impact under disparate-impact law (US: 4/5 / 80% rule under Title VII; EU: GDPR Art. 22 + EU AI Act Art. 5/6) without ever naming the protected class.
- **Discoverability risk**: research artifacts (notes, recordings, transcripts) can be subpoenaed in litigation. Anything documenting "we knew about disparate impact and did not act" creates legal exposure for the organization. Frame protocols accordingly — surface decisions, not after-the-fact rationalizations.
- **Aggregation harms**: individually innocuous answers combining into a profile (e.g., 5 demographics + working hours + login location → re-identifiable population of 1)
- **Power-asymmetric retaliation risk**: interviews with workers about employer practices can surface information that is protected speech *only if labeled as such*; protocol should make confidentiality architecture explicit before content questions.

Include a **legal proxy-variable lens** when the system uses ranking, scoring, or matching: explicit questions about which variables were considered, which were rejected, and on what basis (technical, legal, ethical) — these are the questions that produce defensible accountability records vs. discoverable embarrassment.

**I. Pre-Interview Design Guardrails (required for power-asymmetric or harm-adjacent topics)**

Before the protocol is run, the researcher must answer:

| Guardrail | Specification |
|---|---|
| **Interviewer selection** | Who is interviewing whom, and what power asymmetry does that create? (e.g., a senior researcher interviewing a junior employee about their manager creates retaliation risk; an external researcher interviewing a marginalized community without representation creates extraction risk) |
| **Confidentiality architecture** | Where do recordings live? Who has access? What is the retention/deletion schedule? Are quotes attributed, anonymized, or aggregated? Is there a mechanism for the participant to redact after the fact? |
| **Compensation and consent** | Is the participant compensated, and is the compensation enough that refusing has no cost? Is consent informed about specific uses (publication, training data, internal-only)? |
| **Trauma-aware framing** | If the topic is harm-adjacent (mental health, abuse, discrimination, immigration status, etc.), name the steps to avoid retraumatization and the support resources available. |
| **Halt/pause protocol** | Under what conditions does the interview pause or stop? Visible distress, disclosure of imminent harm, off-topic disclosure of legally privileged information, participant fatigue. |

**J. Red-Flag / Halt Checklist (required for live interviews)**

A short, scannable list the interviewer keeps visible during the session:

- [ ] Participant shows signs of distress (tearful, defensive, dissociating) → pause, offer break, check willingness to continue
- [ ] Participant discloses imminent harm to self or others → follow your organization's safeguarding protocol
- [ ] Participant discloses information that may create legal exposure (theirs or organizational) → pause and confirm whether to proceed on/off record
- [ ] Power asymmetry becomes activated (e.g., participant says "if my manager hears this...") → re-confirm confidentiality
- [ ] Conversation drifts into protected-attribute territory the protocol did not consent for → return to original frame or close gracefully

This checklist is not a substitute for IRB / ethics review where applicable.

**Minimum output:** Complete protocol with all components (Lead-off, Back-up, Emergency, 8+ Follow-ups, 4+ Covert Categories, Domain-Specific Questions if domain is specified, Interview Sequencing, Non-Obvious Harms Inventory, Pre-Interview Design Guardrails, Red-Flag/Halt Checklist).

---

### Mode 2 — Live Interview Support

If the skill is used during a live interview session:
- Accept participant quotes or paraphrases as input
- Surface normative-evaluative language (values words, moral framing)
- Suggest follow-up probes in real time based on what was said
- Flag moments where a covert category may be emerging

When a participant uses value-laden language (e.g., "manipulative", "unfair", "necessary"), the skill should:
1. Flag the word as a construct-building opportunity
2. Suggest a probe that mirrors their exact language
3. Note which covert category may be emerging

---

### Mode 3 — Post-Interview Analysis

After the interview:
- Identify value constructs surfaced (e.g., "participant expressed strong belief in designer responsibility")
- Map to covert categories: which were confirmed, which were absent, which were surprising
- Generate 3–5 normative insights: statements about *what the participant believes is right/wrong/important*
- Distinguish descriptive findings ("what they did") from normative findings ("what they believe should happen")

---

## Output Format

Default structure unless the user asks otherwise:

### Critical Interviewing Protocol: [Topic Domain]

Framing of the research context and participant type.

### Lead-off Question
[Concrete narrative-opening question]

### Back-up Question
[Alternative lead-off]

### Emergency Question
[Practitioner-agency redirect]

### Follow-up Questions

**Descriptive Probes:**
1. [question]
2. [question]

**Normative Probes:**
1. [question]
2. [question]

**Evaluative Probes:**
1. [question]
2. [question]

**Construct-Building Probes:**
1. [question] — *Build on value words like [examples]*
2. [question]

### Covert Categories
- *"I want to understand [X] without asking '[Y]'"*

---

For live support mode:
### Live Probe Suggestion
- **Flagged language:** "[participant's value word]"
- **Construct-building probe:** "[suggested follow-up]"
- **Emerging covert category:** [category name]

---

For post-interview analysis:
### Normative Insights
1. [Normative insight about what participant believes should happen]
2. [Normative insight]

### Covert Category Mapping

| Covert Category | Status | Evidence |
|---|---|---|
| [Category 1] | Confirmed / Absent / Surprising | [Quote or paraphrase] |

### Values Portrait

A short paragraph capturing the participant's ethical worldview based on the interview — specific to the participant, not generic.

## Guardrails

- Do not embed the construct you're investigating in the lead-off question. The lead-off invites narrative; the construct emerges through follow-ups.
- Do not paraphrase or reframe a participant's value words. If they say "immoral", ask about "immoral" — not "unethical" or "problematic".
- Do not treat covert categories as gotcha traps. They are research intentions — "what I want to understand", not "what I suspect they're hiding".
- Do not rush past construct-building moments. When a participant uses evaluative language, that is the most valuable data point in the interview.
- Do not skip the emergency question. It is designed for the common situation where a participant narrates as an observer rather than a practitioner.
- Do not confuse descriptive findings with normative findings in post-interview analysis. "What they did" and "what they believe should happen" are fundamentally different.

## Deliverable Quality Bar

A strong Critical Interviewing output:

- produces a complete protocol with all components (Lead-off, Back-up, Emergency, Follow-ups, Covert Categories, Domain-Specific Questions when domain is specified, Interview Sequencing, Non-Obvious Harms Inventory, Pre-Interview Design Guardrails, Red-Flag/Halt Checklist)
- includes at least 8 follow-up questions spanning all four probe types
- contains at least 2 construct-building probes with explicit instructions about which value words to watch for
- lists 4–6 covert categories phrased as research intentions, not direct questions
- **produces a Non-Obvious Harms Inventory** identifying proxy-variable harms, discoverability risk, aggregation harms, and retaliation risk for the populations being researched, with named statutes (e.g., 4/5 rule, GDPR Art. 22, EU AI Act Art. 5/6) when applicable
- **specifies Pre-Interview Design Guardrails**: interviewer selection (with power-asymmetry analysis), confidentiality architecture (storage / access / retention / redaction), informed consent specifics, trauma-aware framing, and halt protocol — all named, not implied
- **includes the Red-Flag/Halt Checklist** for live interviews
- when a domain is specified, includes named technical questions specific to that domain (proxy variables, named fairness metrics, appeal mechanisms, etc.)
- provides interview sequencing rationale with dependency tree
- in live mode, correctly identifies value-laden language and generates targeted probes
- in post-interview mode, clearly distinguishes descriptive from normative findings
- produces a values portrait specific enough to differentiate this participant from others

## Integration with Other EDBX Skills

- **edbx-anotherlens** surfaces the designer's assumptions and worldview. Critical Interviewing surfaces the *participant's* values and normative reasoning — the two methods complement each other across the research-analysis boundary.
- **edbx-cider** identifies assumptions in artifacts. Critical Interviewing uncovers the *human reasoning* behind those assumptions.
- **edbx-worrystorming** generates future ethical concerns. Critical Interviewing uncovers the *past ethical decisions* that shaped a product.
- **edbx-humane-design-guide** audits the product for sensitivity exploitation. Critical Interviewing audits the *people* who built it.
- **edbx-motivation-matrix** maps why users participate. Critical Interviewing maps *designer* motivation and values.

## Hashtags

#newperspectives #identifyvalues

## See Also

- Culture Co-Creation Cards
- Normative Design Scheme

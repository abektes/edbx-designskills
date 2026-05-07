# Critical Interviewing

**The short version:** A research interview method designed to surface not just what people say, but the values, beliefs, and power structures that shape *why* they say it.

---

## Who made it

Critical Interviewing in the ethical design context is grounded in **Phil Francis Carspecken's framework for critical ethnographic research** — a method developed in sociology and education research for analyzing how social power and ideology shape discourse. It was adapted for design research as a way to conduct interviews that go beyond surface responses to reveal the implicit ethical reasoning and values embedded in how people talk about technology and design.

The adaptation for design contexts draws on critical theory traditions including work by Carspecken (1996) on critical ethnography, and has been developed further in HCI research on ethical design methods.

---

## The problem it solves

Most user research interviews capture what people say they do, want, or feel. Critical Interviewing captures something deeper: what values they're operating from, what they take for granted, and what power structures are shaping their experience — even when they don't name those things explicitly.

This matters because the people most affected by harmful design decisions are often the least able to name what's happening. They experience the harm; they can describe the symptoms. But the framework for understanding *why* the product is structured to harm them is usually invisible.

Critical Interviewing trains you to listen for that framework — to hear what's being said and also what's being assumed, what's been normalized, and what's structurally absent from the conversation.

---

## When to use it

- **When you're researching a product that affects vulnerable or marginalized populations** — and you want to understand the systemic context of their experience, not just their surface preferences
- **When previous research has felt thin** — when user interviews produced quotes but not real understanding
- **When you're investigating a potentially harmful system** — an algorithmic product, a platform with power asymmetries, a labor system
- **Before publishing research that will influence design decisions** — to ensure the research itself isn't reproducing the same assumptions it's meant to challenge
- **When you want to understand the ethical reasoning of design team members, not just users** — the method applies to any interview context

---

## What it produces

A Critical Interviewing session produces a **research protocol** — a set of structured, sequenced questions designed to surface the covert categories (unstated assumptions and values) in the participant's worldview — plus three safety/ethics layers required for power-asymmetric or harm-adjacent topics.

The protocol includes:

- **Lead-off questions** — open, non-leading questions that let participants frame their own experience
- **Back-up questions** — fallback questions if the lead-off doesn't generate material
- **Emergency questions** — questions for when an interview is going quiet or unproductive
- **Follow-up questions** — at least 8, specific to the domain, probing surface responses for the deeper structure beneath
- **Covert category mapping** — what the participant's language reveals about unstated assumptions, values, and power structures
- **Domain-specific question bank** — calibrated to algorithmic systems, data practices, labor platforms, product features, or organizational policy

Plus three layers that make the protocol safe to run in the field:

- **Non-Obvious Harms Inventory** — for each population being researched, names the specific risks the research itself could create or fail to surface: **proxy-variable harms** (zip code → race; school → class; browser language → immigration status — each producing disparate impact under named statutes like the four-fifths rule, GDPR Art. 22, EU AI Act Art. 5/6); **discoverability risk** (research notes can be subpoenaed in litigation; protocol is framed accordingly); **aggregation harms** (innocuous answers combining into a re-identifiable profile); **retaliation risk** (interviews about employer practices need explicit confidentiality architecture before content questions).
- **Pre-Interview Design Guardrails** — interviewer selection (with named power-asymmetry analysis), confidentiality architecture (where recordings live, who has access, retention/deletion schedule, redaction mechanism), informed consent specifics (publication / training data / internal-only), trauma-aware framing for harm-adjacent topics, and an explicit halt protocol.
- **Red-Flag / Halt Checklist** — a scannable list the interviewer keeps visible during the session (signs of distress → pause; disclosure of imminent harm → safeguarding protocol; legally privileged disclosure → confirm on/off record; activated power asymmetry → re-confirm confidentiality; drift into uncovered protected-attribute territory → return to original frame).

An **interview sequencing rationale** is also included: who to interview first (affected users before system designers; people closest to the harm before people who made the decisions), and why that order matters.

---

## The key insight

The method draws a distinction between what Carspecken calls **communicative acts** — the surface-level content of what people say — and **covert categories** — the deeper assumptions about what's normal, what's possible, who matters, and what doesn't need explaining.

Most interviews stay at the communicative level. Critical Interviewing works at the covert level — the place where ideology lives, where harmful patterns are normalized, and where the most important design insights are hidden.

---

## How to use it with AI

Tell the AI what you're researching, who you're interviewing, and what ethical concerns or questions you're trying to surface. Specify the domain (algorithmic system, data practice, labor platform, product feature, or organizational policy). The AI will generate a complete interview protocol calibrated to that domain, with sequencing rationale and a covert category framework for analyzing what you hear.

---

## A quick example

**Context:** Researching delivery workers on a gig platform to understand how they experience algorithmic management.

**Lead-off:** "Walk me through a typical workday from the moment you log on."

**Follow-up questions (domain-specific for labor platform):**
- "Can you tell me about a time when you felt the algorithm was working against you?"
- "How do you know if you're doing well? Where does that signal come from?"
- "Have you ever been deactivated or warned? What information did you get?"
- "What would you change about how the system works if you could?"
- "Who do you contact when something goes wrong?"
- "Do you know how your rating is calculated?"

**Covert category analysis:** The participant consistently says "the app" rather than "the company" — treating algorithmic management as a force of nature rather than a set of decisions made by people. This normalization of algorithmic authority is a covert category that reveals how power asymmetry has been internalized.

---

## See also

- [Ethicography](ethicography.md) — Critical Interviewing produces research input; Ethicography analyzes that research for ethical trajectory
- [Anti-Heroes](anti-heroes.md) — Critical Interviewing surfaces the experience of people harmed; Anti-Heroes maps the systemic structure of that harm
- [CIDER](cider.md) — both methods work with underrepresented populations, from different angles

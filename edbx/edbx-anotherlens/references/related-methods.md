# Related Methods — Connections Within the EDB Toolkit

Another Lens is one principle in a larger ethical design practice. This reference maps its connections to companion skills and suggests how to sequence them for maximum impact.

---

## Direct Companions

### edb-worrystorming

**What it does:** Generates a structured list of things that could go wrong — risks, harms, failures, unintended consequences.

**How Another Lens connects:** Worrystorming generates external risks; Another Lens surfaces the internal biases driving them. When you Worrystorm, you ask "what could go wrong?" When you apply Another Lens, you ask "what am I not seeing because of who I am?"

**Sequencing:** Run Another Lens first to name your lenses and surface your biases. Then Worrystorm with that self-awareness active. The biases you've identified will help you distinguish between risks you're seeing clearly and risks you're still blind to. After Worrystorming, return to Lens 1 to check whether any new biases surfaced during the risk generation.

**Integration prompt:** "After Worrystorming, look at the risks you generated. Which ones feel distant or abstract? Which ones feel immediate? The distant ones may be distant because of your lenses — not because they're less likely."

### edb-responsible-design-prism

**What it does:** Evaluates a design across multiple ethical dimensions — privacy, consent, equity, autonomy, sustainability, and more.

**How Another Lens connects:** Prism diagnoses the design; Another Lens diagnoses the designer. Prism asks "what are the ethical properties of this product?" Another Lens asks "what assumptions did the designer bring that shaped those properties?"

**Sequencing:** Use Prism on the product first to identify ethical dimensions of concern. Then apply Another Lens on yourself to examine whether your personal lenses shaped which dimensions you prioritized or overlooked. Prism is the structural audit; Another Lens is the personal audit.

**Integration prompt:** "After running Prism, look at the dimensions that scored highest and lowest. Ask: did my lenses influence which dimensions I took seriously and which I rushed through?"

### edb-motivation-matrix

**What it does:** Maps what motivates different user groups in relation to a design, surfacing alignment and misalignment between user motivations and design intent.

**How Another Lens connects:** Motivation Matrix asks what motivates users; Another Lens asks what motivates the designer's assumptions about those users. The gap between the two is where bias lives.

**Sequencing:** Run Motivation Matrix first to map user motivations. Then apply Lens 1 (Balance Your Bias) to check whether the motivations you identified reflect your own assumptions more than your users' actual experience. Lens 2 (Consider the Opposite) can then ask: "What would a user who is motivated differently experience in this design?"

**Integration prompt:** "You've mapped user motivations. Now ask: which of these motivations do I share? Which are foreign to me? How has my comfort with the shared motivations shaped how seriously I took the foreign ones?"

### edb-humane-design-guide

**What it does:** Audits designs for sensitivity exploitation — places where the product leverages emotional vulnerability, cognitive limitations, or situational distress for engagement or conversion.

**How Another Lens connects:** Humane Design Guide audits the product for exploitative patterns; Another Lens asks who told us what "sensitive" means and where the line between "helpful" and "exploitative" was drawn.

**Sequencing:** Run Humane Design Guide to identify potential exploitation points. Then apply Another Lens to examine whether your definition of "sensitive" or "vulnerable" is based on your own experience or on the actual lived experience of the people affected.

**Integration prompt:** "The Humane Design Guide identified areas where the product might exploit sensitivity. Now ask: whose definition of sensitivity informed that analysis? Who would define the boundary differently?"

### edb-cider

**What it does:** Provides a structured framework for ethical evaluation of design decisions, weighing consequences, intentions, duties, and equity.

**How Another Lens connects:** CIDER evaluates the decision; Another Lens ensures the evaluator has checked their own perspective before evaluating. Every ethical evaluation is filtered through the evaluator's worldview — Another Lens makes that filter visible.

**Sequencing:** Apply Another Lens before CIDER to surface biases that might shape the evaluation. After CIDER, return to Lens 1 to check whether any biases influenced how you weighed consequences or prioritized principles.

**Integration prompt:** "Before running CIDER, ask: what do I already believe about this decision? What would someone who disagrees with me see that I might miss?"

---

## Broader Methodological Connections

### Data Feminism

Another Lens shares DNA with Data Feminism's core principle: examine power. When Lens 1 asks "what are my lenses?", it's asking who holds power in the design process. When Lens 2 asks "who might be impacted?", it's asking who bears the consequences of that power. The connection is not incidental — it's structural.

### Hippocratic Oath for Design

"First, do no harm" requires knowing what harm looks like from perspectives other than your own. Another Lens is the method that makes the Hippocratic Oath operational: you cannot avoid harm you cannot see, and you cannot see it through your own lenses alone.

---

## Sequencing Guide

**For a comprehensive ethical review of a new feature:**

1. **Another Lens (Lens 1 + 2)** — Surface designer biases and identify absent perspectives
2. **edb-motivation-matrix** — Map user motivations with awareness of your own lenses
3. **edb-worrystorming** — Generate risks, now aware of which risks your biases might hide
4. **edb-humane-design-guide** — Audit for exploitation, with your definition of "sensitive" checked
5. **edb-responsible-design-prism** — Evaluate the design across ethical dimensions
6. **edb-cider** — Structured ethical evaluation with all perspectives surfaced
7. **Another Lens (Lens 3)** — Reframe what you learned into a growth commitment

**For a quick self-check before shipping:**

1. **Another Lens (Lens 2 only)** — Quick check for absent perspectives and the nervous-person question
2. **edb-worrystorming (quick pass)** — Generate the top 5 risks
3. Act on whatever surfaced

**For team friction or disagreement:**

1. **Another Lens (full session)** — Each team member works through all three lenses individually, then shares
2. Compare lens statements — the differences reveal where the team's lenses diverge
3. Use the divergences as input for **edb-responsible-design-prism** or **edb-cider**

---

## Using This Reference

The connections described here are not prescriptions — they are invitations. The most valuable sequencing will depend on your context, your team, and your product. The principle is simple: no single method is sufficient, and methods that examine the designer complement methods that examine the design.

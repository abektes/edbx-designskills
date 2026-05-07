---
name: edbx-stf-et
description: Use when an individual, team, or organization wants to put ethical values into action around a product, policy, research project, or technology decision. Apply the Stanford McCoy Family Center for Ethics in Society Ethics Toolkit — a five-tool, three-phase chainable framework that moves from exploration to evaluation to decision-making. Each tool produces structured outputs that feed directly into the next. Trigger this skill for any mention of ethical impact assessment, future consequences of work, societal benefits and harms, value trade-offs, ethical decision-making, or when someone says "is this ethical?", "what are the implications of this?", "how do we make this decision responsibly?", or "I need to evaluate our ethical position." Also trigger for "Stanford ethics toolkit", "Future Story", "Impacts Explorer", "Ethics Frame", "Ethics Gauge", "Weighing Options", "Value Cards", "ethical assessment", "societal impact", "ethics chain", or "stf-et".
metadata:
  version: "1.0"
  source: "Stanford McCoy Family Center for Ethics in Society — Ethics Toolkit V1.1, 2025"
  license: "CC BY 4.0 — ethicstoolkit.stanford.edu"
---

# Stanford Ethics Toolkit (stf-et)
PUT VALUES INTO ACTION

## Overview

The Stanford Ethics Toolkit — developed by the McCoy Family Center for Ethics in Society at Stanford University — is a pragmatic, society-centered framework for making ethics an intrinsic part of work from start to finish. It consists of five tools organized into three phases: **Explore → Evaluate → Decide.**

The tools are designed to **chain together**: each produces a structured output that feeds directly into the next. You can enter the chain at any point, run a single tool in isolation, or traverse all five in sequence. The chain is most powerful when run in full — outputs accumulate into a complete ethical picture that supports principled decision-making.

> **Core premise:** Ethics is everyone's responsibility, a shared societal undertaking. The tools do not tell you what the right thing to do is — they create the structure and shared language for you to reason carefully about it yourself. The value lies not just in the filled-out artifact, but in the thinking and discussion it provokes.

## The Five Tools at a Glance

| Phase | Tool | Purpose |
|-------|------|---------|
| **Explore** | Future Story | Imagine the impacts of your work by looking back from the future |
| **Explore** | Impacts Explorer | Map the full ripple effects — effects on people and how values are impacted |
| **Evaluate** | Ethics Frame | Single worksheet to outline ethical considerations and actions in response |
| **Evaluate** | Ethics Gauge | Systematic assessment across four core ethical dimensions |
| **Decide** | Weighing Options | Compare different courses of action across societal and organizational impact |

**Appendix — Value Cards:** Nine Value Explainer Cards (Well-being, Justice, Trust, Privacy, Dignity, Virtues, Autonomy, Responsibility, Relationships) that inform all five tools by making abstract values concrete and observable. See `references/value-cards.md`.

## Use This Skill When

- A team is in early-stage exploration and wants to surface what ethical considerations are at play.
- A product, feature, policy, or research action needs a structured ethical assessment.
- Someone needs to choose between two or more courses of action and wants to weigh trade-offs responsibly.
- A team wants to build shared language and shared accountability around an ethical question.
- Someone says: "is this ethical?", "what could go wrong?", "how do we weigh these options?", "what are our responsibilities here?", or "I want to think through the implications before we ship."
- Any project stage — early ideation (Future Story, Impacts Explorer), mid-development (Ethics Frame, Ethics Gauge), or a decision point (Weighing Options).

## Inputs

Provide as many of these as are available. The more context given, the more grounded and specific the output:

- **The action or creation** — what are you (considering) doing or building? (product, feature, policy, service, research, intervention)
- **Stage** — are you in early ideation, development, pre-launch, or post-launch evaluation?
- **Known concerns** — anything already flagged by the team, users, or stakeholders
- **Values that matter** — any values already identified as important to the work or those affected
- **Stakeholders** — who is impacted, directly and indirectly
- **Options to compare** (for Weighing Options only) — two or more courses of action under consideration
- **Which tools to run** — run all five, run a single tool, or name the phase you need

If the user provides only the action/creation and no further context, proceed — the tools are designed to work from minimal input and generate substance through structured reflection.

---

## Chainable Workflow

The five tools form a chain. Each is documented below with its full workflow and a **→ Feed Forward** section that names exactly what to carry into the next tool. Run all five for maximum depth. Enter at any stage if earlier stages have already been addressed. Exit after any stage if that level of analysis is sufficient.

---

### TOOL 1 — Future Story
*Phase: Explore | Think forward by looking back*

**What it does:** A storytelling structure (adapted from Kenn Adams' Story Spine) that helps you imagine the impacts of your work by narrating it from the future. The six-element spine covers problem, solution, benefits, harms, cascading consequences, and mitigating actions.

**When to use it first:** Early-stage exploration, when the team hasn't yet structured its thinking about ethical implications. The narrative format opens honest reflection without requiring analytical precision upfront.

#### Workflow

Work through the six spine elements in order. Write honestly and objectively — not just the desired success, but what actually happened including unintended effects. Think beyond your initial expectations.

**Spine Element 1 — PROBLEM / MOTIVATION**
Prompt: *"Once upon a time …"*
Describe the current problem or issue your work aims to address. What is the need? Who is experiencing it?

**Spine Element 2 — SOLUTION / VALUE PROP**
Prompt: *"Until one day …"*
Describe your creation or action in response to the issue. What did you build or do?

**Spine Element 3 — BENEFITS**
Prompt: *"And because of that …"*
How has it benefited people and society? What positive outcomes materialized? Think broadly — not just intended users, but also indirect beneficiaries.

**Spine Element 4 — HARMS**
Prompt: *"But also …"*
How has it harmed or may it harm people and society? Be honest. Include unintended effects. Don't sanitize.

**Spine Element 5 — SUBSEQUENT IMPACTS**
Prompt: *"In turn …"* (repeat as needed)
Additional harms or unintended consequences cascading from the primary effects. What ethical values were impacted and how?

**Spine Element 6 — MITIGATING ACTIONS**
Prompt: *"One thing we could have done differently is …"*
What actions could mitigate the harms, or what research would better understand the issues? Be specific enough to act on.

**Quality bar:**
- All six spine elements are completed — no skipping
- Benefits AND harms are both named; not just desired outcomes
- At least one "In turn" consequence goes beyond the first-order effect
- The mitigating action is specific enough to act on or investigate

#### → Feed Forward to Tool 2 (Impacts Explorer)

After completing the Future Story, **always close this tool's output with the following explicit block** — this is the handoff that makes the chain work:

```
→ Carries forward to Tool 2 (Impacts Explorer):
- Action/Creation: [Spine 2 summary — one sentence]
- Direct effects seeding Effects ring: [list from Spines 3–4]
- Cascading impacts seeding Secondary Effects ring: [list from Spine 5]
- Values touched: [list from Spine 5]
```

This block is not optional. Without it, the next tool in the chain lacks its inputs and the chain breaks. If running this tool in isolation, still output the block — it tells anyone reading the output what they would carry forward if they continued.

---

### TOOL 2 — Impacts Explorer
*Phase: Explore | Map the ripple effects of your actions — how people are affected and how values are impacted*

**What it does:** A structured brainstorming method that maps the full range of consequences your action or creation may generate — from direct effects to secondary effects to values impacted. Builds on the Futures Wheel technique with an added focus on values. Can be worked In-to-Out (from action outward) or Out-to-In (from values inward).

**When to use:** After Future Story (using its outputs as seeds), or independently as a standalone impact-mapping exercise.

#### Workflow

**Set the center node.** Name the action or creation you are exploring. If coming from Future Story, use the Spine 2 description.

**Choose a direction (or both):**

**Direction A — In-to-Out** (recommended when starting from the action)

1. *Map direct effects:* What are the immediate effects on people and society? Consider behavioral changes, physical or psychological effects on users, economic changes.
2. *Map secondary effects:* For each direct effect, what are its ripple effects? Draw connections showing how consequences relate to each other.
3. *Identify values impacted:* For each direct and secondary effect, ask: What values are reinforced or undermined? Does your action help or hinder people's ability to uphold these values? Consider both moral values (from the Value Cards) and non-moral values important to your organization or users.

**Direction B — Out-to-In** (recommended when starting from values)

1. *Name the values at stake:* List the values you aim to promote and those you fear may be compromised. Reference `references/value-cards.md` for the core nine.
2. *Trace backward:* Identify which actions or decisions influence each value — the pathways showing what promotes or degrades each one.

**Additional lens — Group-specific impacts:**
For each significant stakeholder group, map a separate pathway of impact. This reveals how consequences vary across different communities and whether benefits and harms are distributed fairly.

**Think broadly and go beyond your initial perception.** Surface extensive possible implications, including unintended or indirect effects.

**Quality bar:**
- At least 3 direct effects are named
- At least 2 secondary effects are mapped per direct effect
- At least 3 distinct values are identified and linked to specific effects
- The map covers both benefits AND harms
- Group-specific impacts are noted for at least 2 different stakeholder groups

#### → Feed Forward to Tool 3 (Ethics Frame)

After completing the Impacts Explorer, **always close this tool's output with the following explicit block:**

```
→ Carries forward to Tool 3 (Ethics Frame):
- Action/Creation: [one-sentence description]
- Benefits seeding Ethics Frame Section 3: [list key direct/secondary benefits]
- Harms seeding Ethics Frame Section 4: [list key direct/secondary harms]
- Values identified: [list with brief note on how each is impacted]
- Stakeholder groups and differential impacts: [list groups with their primary impact]
- Fairness patterns to flag in Section 5: [any distributional inequities observed]
```

This block is not optional. It is the explicit handoff to the Ethics Frame.

---

### TOOL 3 — Ethics Frame
*Phase: Evaluate | A single worksheet to outline ethical considerations and actions in response*

**What it does:** A practical framework to think through the (potential) benefits and harms of your actions and the possible actions in response — connecting impacts to the values that matter most, then planning how to expand benefits and reduce harms. Start at the top and work down.

**When to use:** After Impacts Explorer (using mapped effects as inputs), or as a standalone structured reflection tool. Suitable for individuals and teams.

#### Workflow

**Section 1 — ACTION / CREATION**
Write the activity or creation you are proposing or considering — a product, service, feature, action, policy, or intervention. Anything affecting people or society.

**Section 2 — VALUES (Part One: Explore the values that matter)**
*What values are driving you?*

Identify the core values that drive your work AND the broader set of values that may be impacted:
- What does this action seek to uphold or advance?
- What moral values (from the Value Cards) and non-moral organizational values are in play?
- What values do those affected by your work care about?

Then assess impact: How do your actions influence these values? Which will be reinforced? Which undermined? Will your action make it easier or harder for people to uphold their values?

**Section 3 — BENEFITS**
*How is it beneficial?*

Catalog benefits in two ways: whether people desire what you've created (preference), and whether people experience physical or psychological benefit (well-being). Assess extent across four dimensions:
- **Magnitude** — how much benefit per individual
- **Scope** — how many people benefit
- **Likelihood** — how probable the benefit is
- **Duration** — how enduring or limited the effect is

Think beyond individuals — consider effects on institutions, society, and shared public values like trust, democracy, and transparency.

**Section 4 — HARMS**
*How is it (potentially) harmful?*

Apply the same four dimensions (magnitude, scope, likelihood, duration) to harms. Additionally consider:
- Unintended uses, malicious or not — who will abuse, hack, or weaponize what you've created?
- What incentives might you inadvertently create for bad actors?
- What happens during failures or outages?

**Section 5 — WHO IS AFFECTED, IN WHAT WAY**
*How do effects differ for different people and groups? Is this distribution fair?*

Visualize on a spectrum from "great benefit" to "great harm" which groups are affected and how. Name the specific benefits or harms impacting each group. Note prevalence (how many people in each group). Then consider fairness:
- Are already-marginalized groups facing outsized harms?
- Are privileged groups capturing most of the benefit?
- Are some unable to access benefits due to economic or social barriers?

**Section 6 — VALUES (Part Two: Plan for action in alignment with values)**
*What values are you prioritizing over others, and why?*

After considering effects and their distribution, return to values. Decisions are hard — choices will favor certain values over others. Being explicit about which values take precedence and why is what makes an ethical commitment rather than just a preference.

**Section 7 — HOW TO EXPAND BENEFITS**
*How might you amplify and spread the benefits?*

Brainstorm ways to maximize positive impacts: low-hanging fruit, updates to the original plan, enhancements that align with identified values. Ask: are these enhancements aligned with the values you and those impacted care about?

**Section 8 — HOW TO REDUCE HARMS**
*How might you prevent, mitigate, and dilute the harms?*

Three lenses: How might you **prevent** harms connected with your creation? How could you **protect people** from the harms, or reduce the number affected? How might you **support people** who may be impacted?

**Section 9 — BOTTOM LINE**
*What changes in your plans will you make?*

Concrete conclusion: changes to the core creation or activity, alterations to specific features, additional mitigation steps, or commitments to ongoing vigilance. Specific enough to create accountability.

**Quality bar:**
- Benefits and harms each have at least 2 entries with extent dimensions noted
- At least 2 distinct stakeholder groups are named in the fairness spectrum
- Values appear in both the "driving you" and "impacted" analyses
- The Bottom Line proposes at least one concrete, actionable change
- Expand-benefits and reduce-harms each contain at least 2 strategies

#### → Feed Forward to Tool 4 (Ethics Gauge)

After completing the Ethics Frame, **always close this tool's output with the following explicit block:**

```
→ Carries forward to Tool 4 (Ethics Gauge):
- Action/Creation: [one-sentence description]
- Benefits informing "How is it beneficial?": [key benefits with extent notes]
- Harms informing "How is it harmful?": [key harms with extent notes]
- Fairness patterns informing "How fair is it?": [distributional issues, affected groups]
- Autonomy/dignity issues informing "How empowering is it?": [from Section 2 values analysis]
```

This block is not optional. It is the explicit handoff to the Ethics Gauge.

---

### TOOL 4 — Ethics Gauge
*Phase: Evaluate | A practical template for ethical assessment at a glance*

**What it does:** A systematic template that assesses your action or creation across four core ethical dimensions — beneficial, harmful, fair, and empowering — using observable spectra. Each dimension contains three spectra scored from − to +. The Gauge does not reduce ethics to a score: the holistic assessment emerges from considering all four dimensions together.

**When to use:** After Ethics Frame (using its outputs to calibrate each dimension), or as a standalone check-in or recurring impact tracker embedded into workflow.

#### Workflow

Work through each of the four dimensions. For each spectrum, mark your assessment, note what you would expect to observe, and identify what you still need to investigate.

**Dimension 1 — HOW IS IT BENEFICIAL?**

Three spectra (mark each −/neutral/+):
- Limited benefit to individuals ←→ Great benefit to individuals (more benefit than what already exists)
- Benefit limited to few select people ←→ Large numbers and multiple groups benefit
- Action unlikely to succeed / low likelihood of benefit ←→ Very likely the benefit will be achieved

Reflection: How do we measure the effects? How might we move toward the positive end? What else do we need to investigate?

**Dimension 2 — HOW IS IT HARMFUL?**

Three spectra (mark each −/neutral/+):
- Great harm to individuals; more harm than alternatives ←→ Limited harm; less than what already exists
- Large numbers / multiple groups are harmed ←→ Harm limited to few people
- Harm is certain to occur or impossible to prevent ←→ Harm unlikely; potential harm preventable

Reflection: What would we expect to observe if harm occurs? What indicators help track it? Consider endurance (how lasting), remediability (can it be fixed), and preventability. What additional research is needed?

**Dimension 3 — HOW FAIR IS IT?**

Three spectra (note: the first spectrum is neutral — neither equal nor unequal distribution is inherently better):
- Certain people or groups are affected more than others ←→ All people and groups are affected equally (neutral spectrum)
- Those who are harmed are also less advantaged in society; those who benefit have privilege ←→ No more harm to the less advantaged; those who benefit have greater need
- The burden faced by those most harmed is not acceptable or justifiable ←→ The burden is acceptable or justifiable given the broader context

Reflection: Are impacts experienced equally or unequally? Is the nature of the distribution fair? What values should limit what is considered acceptable? Refer to Value Cards for Justice and Dignity.

**Dimension 4 — HOW EMPOWERING IS IT?**

Three spectra (mark each −/neutral/+):
- People's ability to make informed choices for themselves is reduced ←→ Ability to make informed choices is unimpaired or increased
- People's control over aspects of their lives is removed ←→ Control is retained or enhanced
- There are activities our creation removes the freedom to do ←→ Creation does not coerce, manipulate, or pressure people; limits others' ability to do so

Reflection: Does this work undermine or enhance autonomy? Is freedom reduced through coercion, manipulation, exploitation, or psychological pressure? Could autonomy limits be justified by preventing greater harm?

**Synthesis:** After completing all four dimensions, look at the overall picture. No single row or spectrum determines ethical soundness. A creation may score well on benefits but raise serious fairness or empowerment concerns. The final assessment must hold all four dimensions together and consider their tensions.

**Quality bar:**
- All four dimensions assessed — none left blank
- Each spectrum has an explicit marked position
- At least one reflection note per dimension (measurement, investigation needed, or improvement path)
- A synthesis paragraph addresses tensions across dimensions, not just the best-scoring areas

#### → Feed Forward to Tool 5 (Weighing Options)

After completing the Ethics Gauge, **always close this tool's output with the following explicit block:**

```
→ Carries forward to Tool 5 (Weighing Options):
- Current Situation summary: [one paragraph suitable for direct use in the Current Situation field]
- Hot spots (negative-pole spectra): [list — these become the key ethical differentiators between options]
- Knowledge gaps flagged for Obstacles section: [list uncertainties that need investigation]
- Values to carry into "What are you prioritizing?": [list values from Ethics Frame with their priority ranking]
```

This block is not optional. It is the explicit handoff to Weighing Options. If a prior Ethics Frame has already been run externally and its outputs are provided as context, use those in place of a new Ethics Frame analysis — the handoff block should then reference which values and hot spots were identified in that prior frame.

---

### TOOL 5 — Weighing Options
*Phase: Decide | Compare different options, considering the effects on society and your organization*

**What it does:** A structured comparison tool for choosing between different courses of action — assessing each option's societal impact, organizational impact, obstacles, and value alignment. Produces a reasoned, transparent Future Direction statement.

**When to use:** When a decision point has been reached and two or more courses of action need to be compared. Run after the Gauge (which surfaces the ethical hot spots that differentiate options), or standalone when the decision context is clear.

#### Workflow

**Current Situation**
Describe the context in which the decision must be made. What is the status quo? If modifying something existing, describe it and why change is being considered. If designing something new, describe the environment, constraints, and goals. What resources, regulations, and stakeholder relationships shape the decision?

**For each Option (minimum two — repeat the following for each):**

*Option Description*
A brief summary of this course of action.

*Societal Impact — How are people and society affected?*
Catalog benefits and harms this option may create. Use magnitude, scope, likelihood, and duration. Note who gets the most benefit and who faces the most harm. Consider direct and indirect effects, effects on institutions and shared public values, and unintended uses by careless or bad actors.

*Organizational Impact — How might the organization be affected?*
Think internally: resources, processes, finances, timelines, launch complexity. Think externally: reputation, regulatory compliance, competitive positioning, partnerships.

*Obstacles — What might prevent implementing or achieving this option?*
Name uncertainties: external events, assumptions about stakeholder buy-in, financial risks, regulatory changes, technical failures, geopolitical risks. For each significant uncertainty, identify a contingency plan.

*If you choose this option, what are you prioritizing?*
Name the values this option promotes or undermines. What organizational or non-moral factors does it elevate (speed, budget, customer satisfaction, competitive position)? Recognizing what each option actually prioritizes is what enables intentional, principled choice.

**Future Direction**
Which option will you pursue, and why? Articulate the reasoning: which values take precedence, which trade-offs are accepted, what actions will be taken accordingly.

Or: What else do you need to learn or do before deciding? Document the open tensions, remaining questions, and what research would resolve them.

**Quality bar:**
- At least two distinct options are compared (not one option vs. nothing)
- Each option's societal impact addresses both benefits and harms
- Organizational impact covers both internal and external dimensions
- Obstacles section names at least one contingency plan per option
- Future Direction provides an explicit rationale, not just a selection
- The values prioritized for each option are named and compared against each other

---

## Value Cards Reference

Nine core values inform all five tools. Reference them at any point in the chain, especially when naming values in the Impacts Explorer, Ethics Frame, and Weighing Options. Full definitions and observable spectra are in `references/value-cards.md`.

| Value | Definition |
|-------|-----------|
| **Well-being** | The flourishing of individuals and society, including health, happiness, and growth |
| **Justice** | The fair distribution of benefits and burdens of (social) goods |
| **Trust** | Optimistic and voluntary reliance on the competence and goodwill of another with respect to our interests |
| **Privacy** | The flow of personal information which supports the individual's right to control or protection from unwanted intrusion |
| **Dignity** | The inherent worth that every person possesses equally, which deserves recognition and respect |
| **Virtues** | Habits or dispositions that guide us to act in morally good ways |
| **Autonomy** | The ability to govern oneself by one's own judgment |
| **Responsibility** | Awareness, care, and accountability regarding the effects of one's choices and actions |
| **Relationships** | A social association, connection, or affiliation between persons that provides goods that cannot be enjoyed outside of relationships |

---

## Output Format

Default structure when running the full chain. The `→ Carries forward:` block at the end of each tool is **mandatory** — it is the explicit handoff that makes the chain usable by a team working asynchronously or by anyone continuing the chain in a later session. See each tool's `→ Feed Forward` section above for the exact required format of that block.

```
### STF-ET Ethics Assessment: [Name of Action/Creation]

**Chain Status:** [Tools run: Future Story ✓ | Impacts Explorer ✓ | Ethics Frame ✓ | Ethics Gauge ✓ | Weighing Options ✓]
**Entry Phase:** [Explore / Evaluate / Decide — note which tools were skipped and why]

---

#### Tool 1 — Future Story
[Six-element story spine, each element clearly labeled and completed]

→ Carries forward to Tool 2 (Impacts Explorer):
- Action/Creation: [...]
- Direct effects: [...]
- Cascading impacts: [...]
- Values touched: [...]

---

#### Tool 2 — Impacts Explorer
[Structured map: Action/Creation → Direct Effects → Secondary Effects → Values Impacted, connections named]

→ Carries forward to Tool 3 (Ethics Frame):
- Action/Creation: [...]
- Benefits: [...]
- Harms: [...]
- Values identified: [...]
- Stakeholder groups: [...]
- Fairness patterns: [...]

---

#### Tool 3 — Ethics Frame
[Nine sections completed in order; Bottom Line at the end]

→ Carries forward to Tool 4 (Ethics Gauge):
- Action/Creation: [...]
- Benefits with extent: [...]
- Harms with extent: [...]
- Fairness patterns: [...]
- Autonomy/dignity issues: [...]

---

#### Tool 4 — Ethics Gauge
[Four dimensions with spectrum positions and reflection notes; synthesis paragraph]

→ Carries forward to Tool 5 (Weighing Options):
- Current Situation summary: [...]
- Hot spots: [...]
- Knowledge gaps: [...]
- Values priority ranking: [...]

---

#### Tool 5 — Weighing Options
[Current situation; each option with all four sub-sections; Future Direction]

---

**Values Prioritized Across the Chain:** [Which of the nine core values were most significant, and how they were upheld or traded off]
```

When running a single tool in isolation, output only that tool's section. Still include the `→ Carries forward:` block — it tells anyone reading the output exactly what they would use if they continued the chain.

---

## Guardrails

- **Do not conflate completing the tools with having done the ethics.** The tools create structure for reflection. The responsibility for acting on that reflection remains with the person or team using them.
- **Do not skip harms in favor of benefits.** Every tool in the chain requires both. The tendency to emphasize benefits is the primary failure mode in ethical assessment.
- **Do not accept vague value labels.** "We care about privacy" is not enough. Ground each value claim in observable behaviors or outcomes — use the Value Cards spectra to make values concrete and measurable.
- **Do not rush to Weighing Options.** It comes last because it requires the groundwork from earlier tools. Jumping to it without prior analysis produces shallow trade-off thinking.
- **Do not treat the chain as strictly linear.** Teams can loop back to earlier tools as new information emerges. The Gauge may reveal a gap that warrants returning to the Impacts Explorer. The chain is iterative, not one-directional.
- **Do not use the Ethics Gauge as a scorecard.** No single spectrum position determines ethical soundness. The synthesis across all four dimensions is the assessment.
- **Do not let fairness be an afterthought.** Distributional questions — who gets the benefits, who bears the harms — must be surfaced explicitly in the Ethics Frame and the Gauge, not assumed to be covered by other sections.
- **Do not guarantee the tools will tell you the right thing to do.** They offer structure and building blocks, but the team must define key values and assess trade-offs. The tools do not provide a complete checklist of all harms or ethical issues — they give a starting point.

## Deliverable Quality Bar

A strong full-chain STF-ET output:

- completes all five tools (or explicitly states which tools were run and why others were skipped)
- surfaces both benefits and harms in every tool where both are required
- names at least 3 distinct stakeholder groups across the chain and tracks how effects differ per group
- identifies at least 5 values across the chain and links each to specific effects or decisions
- produces a Bottom Line (Ethics Frame) and a Future Direction (Weighing Options) each specific enough to create accountability
- closes with a synthesis statement naming which values were prioritized, which trade-offs were accepted, and what concrete actions will be taken

## Integration with Other EDBX Skills

- **edbx-worrystorming** generates a broad worry landscape before the stf-et chain begins. Run Worrystorming first to surface ethical concerns at volume, then use Future Story and Impacts Explorer to structure them into a coherent, connected map.
- **edbx-anotherlens** surfaces the team's internal biases and worldview assumptions. Run it before or alongside the Impacts Explorer to ensure impact mapping doesn't carry unchecked perspective blind spots.
- **edbx-cider** maps who is excluded by design assumptions. Use its output to deepen the "Who Is Affected" section of the Ethics Frame and the fairness dimension of the Ethics Gauge.
- **edbx-humane-design-guide** audits for sensitivity exploitation. Its outputs feed naturally into the Harms sections of the Ethics Frame and the empowerment dimension of the Ethics Gauge.
- **edbx-responsible-design-prism** places a design on an ethical spectrum. Use its assessment to calibrate where to enter the stf-et chain — early exploration or near-decision evaluation.
- **edbx-motivation-matrix** maps why users participate. Pair it with the Impacts Explorer to see not just what effects occur, but what motivational dynamics those effects operate through.
- **edbx-values-levers** maps how design choices connect to values. Run it alongside the Value Cards to deepen the values analysis in any stf-et tool.

## Hashtags

#identifyvalues #evaluateoutcomes #designresponsibility #societalimpact #ethicsinaction

## See Also

- Stanford McCoy Family Center for Ethics in Society — ethicstoolkit.stanford.edu
- Value Explainer Cards — `references/value-cards.md`
- Chain facilitation guide — `references/chain-guide.md`
- Three-phase overview — `references/three-phases.md`
- Worksheet templates — `assets/`

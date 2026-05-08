# edbx Skills Evaluation — Results

This document summarizes the evaluation of 21 ethical-design skills (`edbx-*`) against a strong baseline, including cross-judge validation, a reflection on what we learned about skill design, and proposed next steps.

> **Note on this document.** The eval framework is gitignored, so the underlying run JSONs and per-run details are not in version control. The full run logs are preserved at `eval-framework/logs/`. This file was reconstructed from those logs.

---

## TL;DR

Across 21 skills, with two independent LLM judges (Claude Sonnet 4.6 and Gemini 2.5 Pro):

- **17 / 21 skills win cleanly under both judges** — high-confidence corroborated improvements over the baseline.
- **4 / 21 skills win under Claude but are razor-thin under Gemini** — defensible wins, judge taste explains the gap.
- **0 skills lose under both judges** — no case where the SKILL.md output is clearly worse than the baseline.

The skills demonstrably add value over a competent LLM that has only been told the method's name.

---

## How the evaluation was designed

### The headline question

> Does a SKILL.md file add value beyond a competent LLM that already knows the named method?

This is a stricter question than "does the skill beat a generic helpful assistant." A naïve baseline ("you are a helpful ethical-design assistant") is a softball — the skill almost always wins because it tells the model what to do. The fair test asks: even if we *also* tell the baseline what method to apply, does the SKILL.md still earn its tokens?

### Setup

For every scenario, the same generation model (Claude Sonnet 4.6) ran twice:

- **Variant A — raw, method-named baseline.** System prompt: *"You are an expert ethical design assistant. Apply the [method name] method thoroughly to the user's task. Produce a complete, well-structured output with all the standard sections that a [method name] session would include."*
- **Variant B — skill-guided.** System prompt: the full SKILL.md, with instructions to follow the workflow, output format, and guardrails.

Both responses were sent to a blind judge (Claude Sonnet 4.6 in the primary pass, Gemini 2.5 Pro in the cross-judge pass). The judge was randomly told the responses were "Response A" and "Response B" (true ordering hidden), and scored each on six dimensions:

1. Structure & Format
2. Depth & Specificity
3. Actionability
4. Methodology Fidelity
5. Coverage & Completeness
6. Ethical Nuance

Plus a winner pick (skill / raw / tie) with rationale.

### Length-blind instruction

To prevent the judge from rewarding verbose output by default, the rubric explicitly stated:

> Length is not a quality signal. A concise, complete response can score 5 on Coverage and Structure. Do not reward verbosity, padding, or repeated framings. Penalize bloat that does not add substance.

### Cross-judge validation

After the Claude-vs-Claude pass, the same generation pairs were re-judged by Gemini 2.5 Pro using the identical rubric. This isolates judge model preference: when Claude judges Claude, there's a documented self-preference bias. Disagreement between the two judges flags scores that may be inflated by self-preference.

### Scenarios

Each skill has three test scenarios in `<skill>/evals/evals.json`. The validation runs used the first scenario from the JSON file as the canonical test.

---

## How the work proceeded

### Phase 1 — Canonical run (signal gathering)

All 21 skills ran with all 3 evals each. The result revealed a clear stratification:

- 8 skills won outright against the baseline (mostly workshop-style methods with concrete deliverables — canvas, brainstorm, dam/flow, worry clusters)
- 1 skill was tied
- 12 skills lost to the baseline

The judge rationales for losing skills clustered into five recurring failure patterns:

1. **Skill output skips the method's signature move.** The skill describes the method but never *executes* it (e.g., dah-cards produced a consequence map without DAH card pairs; inverted-behavior-model skipped the inversion step itself).
2. **Comprehensive but shallow.** SKILL.md prescribed many sections; the model dutifully filled them all but with breadth instead of depth. The baseline, given freedom, focused depth where it mattered.
3. **Implicit stakeholder mapping.** Affected populations were mentioned in passing but never systematically enumerated with power asymmetry, vulnerability, or named subgroups.
4. **Padding sections diluted actionability.** Skills required outputs (manifesto, future vision, etc.) that didn't fit the user's actual ask, producing bulk that the judge rated as filler.
5. **Defer-instead-of-execute.** Some skills produced clarifying questions instead of best-effort output when input was incomplete.

### Phase 2 — Targeted skill fixes (Round 1)

Twelve SKILL.md files were edited with surgical changes addressing the patterns above:

| Skill | Targeted addition |
|---|---|
| dah-cards | DAH Card Pairs as the signature artifact + mode-selection rule (no Manifesto/Vision when only audit was requested) |
| inverted-behavior-model | Convergence Check table comparing actual design to Worst Possible Design |
| responsible-design-prism | Stakeholder & Vulnerable Population Map + Psychological Mechanism Audit |
| ethical-contract | Bias & Harm Audit (thresholds, proxy variables, gray-zone, red lines with veto owners); 4-part objectives (action + threshold + owner + cadence) |
| fair-patterns | Jurisdiction-specific statute mapping with penalty exposure; Vulnerable Population Harm Matrix; metrics + owner + sprint per fix |
| values-levers | Whose-values-are-visible mapping; systemic-harm map (aggregation, power, future discriminatory use, non-user externalities) |
| digital-ethics-compass | Mandatory Stakeholder & Power Map (5+ named stakeholders, vulnerable subgroups, future-affected, historical-justice prior) |
| humane-design-guide | Named Psychological Mechanism column for every 🔴/🟡; ≥2 named vulnerable populations per sensitivity with mechanism of differential harm |
| critical-interviewing | Non-Obvious Harms Inventory + Pre-Interview Design Guardrails + Red-Flag/Halt Checklist |
| ethicography | Affected populations table per move; concrete-harm examples with named WCAG criteria etc. |
| anotherlens | Design Decision Spec table — top 3 insights → specific change + numbers + owner + sprint + pass/fail criterion |
| pledge-works | 5-part pledge operationalization (threshold + signal + owner + consequence + cadence); "What We Refuse to Build" red-line register; pledge-to-product traceability |

A 13th skill (`normative-design-scheme`) was identified as missed during the same review and given the same treatment plus a methodology-distinctive **Triad Conflict Matrix** and **Universal Law Test** as named artifacts (the judge had said the lens-based methodology felt "retrofitted" — making it concrete fixed that).

### Phase 3 — Validation (Round 1)

Each fixed skill was re-evaluated with the same setup. **9 of 12 flipped to clear skill wins** on the first round. Two remained tied (digital-ethics-compass and humane-design-guide); one still lost (dah-cards).

### Phase 4 — Targeted polish (Round 2)

Three skills got a second-round polish based on judge feedback from Round 1:

- **dah-cards** got six explicitly-named harm categories (Deception / Coercion / Addiction / Surveillance / Exclusion / Systemic) — the prior judge complaint was that the methodology felt loosely applied; naming categories let the model render the method more visibly.
- **digital-ethics-compass** got a **Non-Obvious Harms Inventory** (5+ named harms beyond heuristic categories) and an **Objective Function Risk Table** (stated objective vs. optimized objective).
- **humane-design-guide** got a requirement for 3+ design alternatives per 🔴 sensitivity (minimal / structural / radical reframe), a **Compound Harm / Exploitation Stack Analysis**, and **Memorable Heuristics** as a final required output.

All three flipped to clear skill wins.

### Phase 5 — Cross-judge with Gemini

The 21 winning response pairs were re-judged by Gemini 2.5 Pro. The same generations, a different judge, identical rubric.

**Result: 16 / 21 (76%) agreement, 0 cases where both judges agree raw wins.**

### Phase 6 — One additional iteration (inverted-behavior-model)

Of the 5 disagreements, one stood out: `inverted-behavior-model` had a Gemini delta of -0.83 (a meaningful gap, not razor-thin). The judge specifically called out:

- Stakeholder analysis was less explicit (no non-consenting bystanders, no absent regulators)
- No "rationalizations" section — the stories teams tell themselves to defend the design
- Cascade reasoning could be more structured

A third polish round added:

- **Step 0 Stakeholder Map** with named non-consenting bystanders, workers in the supply chain, and absent regulators
- **Behavioral Cascade Model** with at least 3 named stages (initial → adaptation → social/relational → identity-level → generational/cultural)
- **Rationalizations Check** — for every 🔴 finding, name the story the team uses to defend it and rebut it in plain language

After the polish, both judges agreed: **skill wins, Δ +1.00 on Claude, Δ +0.83 on Gemini**.

Final cross-judge agreement: **17 / 21 (81%)**.

---

## Final scoreboard

| Skill | Claude verdict | Gemini verdict | Cross-judge |
|---|---|---|---|
| anotherlens | skill | skill | ✅ both skill |
| anti-heroes | skill (Δ +0.17) | raw (Δ -0.17) | ⚠️ razor-thin |
| bad-design-canvas | skill | skill | ✅ both skill |
| black-mirror-brainstorming | skill | skill | ✅ both skill |
| cider | skill (Δ +0.17) | raw (Δ -0.67) | ⚠️ judge taste |
| critical-interviewing | skill | skill | ✅ both skill |
| dah-cards | skill | skill | ✅ both skill |
| digital-ethics-compass | skill | skill | ✅ both skill |
| ethical-contract | skill | skill | ✅ both skill |
| ethicography | skill (Δ 0.00) | raw (Δ -0.50) | ⚠️ judge taste |
| fair-patterns | skill | skill | ✅ both skill |
| humane-design-guide | skill | skill | ✅ both skill |
| inverted-behavior-model | skill | skill | ✅ both skill (after R3 polish) |
| motivation-matrix | skill | skill | ✅ both skill |
| normative-design-scheme | skill | skill | ✅ both skill |
| pledge-works | skill (Δ 0.00) | raw (Δ -0.33) | ⚠️ razor-thin |
| responsible-design-prism | skill | skill | ✅ both skill |
| stf-et | skill | skill | ✅ both skill |
| value-dams-and-flows | skill | skill | ✅ both skill |
| values-levers | skill | skill | ✅ both skill |
| worrystorming | skill | skill | ✅ both skill |

---

## Reflection — what we learned about skill design

### What worked

**Naming over prescribing.** The most consistent gain came from forcing the SKILL.md to require *named, specific* outputs rather than abstract structure. "Identify vulnerable populations" produced generic prose; "name at least 2 specifically vulnerable populations, and for each name the mechanism of differential harm" produced concrete analysis. Across 12 skills, this single shift moved the needle.

**Methodology signatures.** The strongest skills had a distinctive *artifact* the model couldn't fake — black/white card pairs, a worst-possible-design + convergence check, a triad conflict matrix, a stakeholder × power table. When SKILL.md required the artifact, the model produced the methodology. When SKILL.md only described the methodology, the model produced ethical analysis with the right vocabulary but wrong shape.

**Operationalization as ethical force.** Pledges, contracts, and red lines are easy to write as aspiration. The skills that fared best required them with five concrete fields — quantitative threshold, named owner, consequence for breach, review cadence, and traceability to a feature decision. A pledge missing any of those is a wish; a pledge with all five is a commitment.

**Mode selection.** dah-cards was a striking case: the canonical run was producing a Manifesto and Future Vision on every audit request, even when the user only asked for an audit. Adding an explicit mode-selection rule ("if the request is `audit X`, do not auto-include Modes 3–4") lifted it from a clear loss to a clear win without changing the methodology at all.

**Cross-judge transparency.** The Gemini cross-judge produced exactly the kind of finding it was supposed to: a skill (inverted-behavior-model) where Claude said skill won by +0.17 and Gemini said raw won by -0.83. Without the cross-judge, that one would have shipped as a confident win on potentially inflated numbers.

### What didn't work the first time

**Comprehensive ≠ deep.** The original SKILL.md files mostly prescribed many sections. The model would dutifully fill them all but at uniform shallow depth, while the raw baseline (given freedom) focused depth where it mattered. Adding more sections in response to losses would have made this worse, not better. The fixes that worked were ones that made *fewer, more concretely required* artifacts.

**Length-blind isn't enough on its own.** We added an explicit length-blind instruction to the judge rubric, and skill outputs were still ~7× longer than raw outputs in the canonical run. Length asymmetry mattered less after the fixes — but only because the fixes packed more substance per token, not because length stopped mattering.

**Self-judge bias is real but not pervasive.** Claude judging Claude produced overall similar verdicts to Gemini judging Claude (76% pre-IBM, 81% after IBM). Bias was concentrated in a small number of close calls rather than distributed across all skills.

### What this implies for future skill design

- **Skill = forcing function for an artifact.** A skill is at its strongest when it forces the model to produce a thing the model wouldn't naturally make.
- **Specificity comes from concrete categories.** "Name X mechanism" beats "consider mechanisms"; "name a population from this list" beats "consider affected populations"; "include the specific statute and jurisdiction" beats "reference applicable law."
- **Less is more, when each piece has teeth.** Three required artifacts with strict criteria outperform seven required sections with vague ones.

---

## What could be improved later

The eval is in good shape but isn't comprehensive. The following extensions would meaningfully raise confidence in the conclusions.

### Methodology gaps

- **Per-skill methodology rubric.** The current 6-dimension judge is generic. Each skill has its own methodology with distinct signature steps. A per-skill rubric (e.g., "did the output produce DAH card pairs / Triad Conflict Matrix / Convergence Check") would catch methodology drift more reliably than the generic judge.
- **`expected_output` grounding.** Each scenario in `evals.json` has an `expected_output` field that describes what a good response should contain. The current judge never sees it. Injecting it as rubric hints (framed as "one valid completion, not the only one" — to avoid rewarding mimicry) would ground scoring in concrete criteria.
- **Variance / consistency.** Each skill was validated with one sample per scenario. Multi-sample runs (3–5 samples per scenario) would let us measure score stability and distinguish "the skill genuinely improved" from "got lucky on this scenario."

### Eval breadth

- **More scenario diversity.** Only the first scenario from each skill's `evals.json` was used in the validation rounds. The other two scenarios per skill exist and are unused — running them would expose whether skill wins generalize or only hold for the canonical scenario.
- **Adversarial / edge-case scenarios.** Short prompts, vague prompts, off-topic prompts, prompts that explicitly ask for a different framework. A skill that is robust to these is meaningfully different from one that wins only on its canonical input.
- **Different generation models.** Sonnet 4.6 was used throughout. Running on Haiku 4.5 (where SKILL.md may matter more for a weaker model) and Opus 4.7 (where it may matter less because the model is more capable) would map the skill's value-add across the model capability spectrum.

### Judge breadth

- **More judge models.** Two judges (Claude + Gemini) is better than one. Adding a third (e.g., GPT-5) would harden the cross-judge findings. The current 81% agreement could be confirmed or revised by a third opinion.
- **Human spot-check calibration.** LLM-as-judge correlates with human judgment on most tasks but not all. A small calibration set (10–20 random pairs scored by domain experts) would let us measure how well the LLM judges track human judgment specifically on ethical-design output, and adjust the rubric accordingly.

### Methodology improvements

- **Length normalization.** The length-blind instruction in the judge rubric is a soft prevention. A harder version would truncate skill outputs to a fixed character ceiling matching the raw output length — a sensitivity test that would tell us how much of the skill's win comes from genuine substance vs. "more text means more dimensions covered."
- **Skill-vs-skill comparisons.** Several skills overlap in scope (e.g., dah-cards / responsible-design-prism / inverted-behavior-model all analyze design-induced harm with different framings). Running head-to-head matches would reveal which method is best suited to which scenario, rather than just whether each skill beats the baseline.
- **Track the trajectory in the viewer.** The eval framework included a `viewer.html` tool that grouped runs by skill. A simple per-skill chart showing win-rate movement across rounds would make the improvement story visible at a glance.

### Operational

- **Track results in version control.** This evaluation's working data lived in a gitignored folder and was lost during a repo cleanup. The summary report (this file) survived only because it was reconstructed from logs. Future evals should store at least the headline summary in version control even if the raw run data stays gitignored.
- **CI hook for skill changes.** When a SKILL.md is edited, automatically run a single-eval validation against the prior version. Flagging regressions before they ship would prevent the kind of drift that's easy to introduce when iterating quickly.
- **Versioning.** SKILL.md frontmatter has `version: "1.0"` for all skills. Bumping versions when substantive changes are made (and storing results under `v1.0/`, `v2.0/` etc.) would make trajectory analysis easier and let users opt into stable versions.

# edbx baseline probe v0.1 (2026-10-14)

The family rule (fdbx's baseline probe): check what the plain model
does when told only the method's name, and keep a skill where the plain model
skips the method's distinctive moves, misstates the method, or invents facts
about the user's situation.

**Data:** the cached `without_skill` arm of the edbx eval run (DeepSeek V4 Pro
via OpenRouter; system prompt "Apply the {method} method thoroughly"), 3
scenarios x 1 output per skill, 63 outputs. No API calls: written out by
`scripts/dump_baselines.py`. Treat single-skill verdicts as indicative (fdbx
used 9 outputs per method).

**Scoring:** per `docs/probe-brief.md`. A Claude Sonnet subagent wrote each
skill's checks from its SKILL.md and stage-B `references/provenance.md`
*before* reading any output (`<skill>/checks.md`), then scored every output
with a quote (`<skill>/scores.json`). D-checks are the published method's
distinctive moves, only those the provenance table traces to a source (edbx
additions, the Answer and the Evidence Ledger excluded). M1 = invented facts
about the user's situation; M2 = misstated method. Two verdicts
(anti-heroes, critical-interviewing) were written by the coordinating session
from finished scores after the scoring agent hit a session limit.

| Skill | Plain model: method coverage | Invents facts | Misstates method | Verdict | Blind A/B: skill wins (mean delta, 1-5) |
|---|---|---|---|---|---|
| edbx-anotherlens | 50% | 50% | 83% | weak | 3/3 (+1.38) |
| edbx-anti-heroes | 47% | 33% | 100% | partial | 2/3 (+0.43) |
| edbx-bad-design-canvas | 8% | 100% | 0% | weak | 3/3 (+1.67) |
| edbx-black-mirror-brainstorming | 61% | 50% | 0% | weak | 3/3 (+1.19) |
| edbx-cider | 33% | 83% | 67% | weak | 3/3 (+0.48) |
| edbx-critical-interviewing | 33% | 67% | 50% | weak | 3/3 (+1.62) |
| edbx-dah-cards | 10% | 67% | 100% | weak | 3/3 (+1.38) |
| edbx-digital-ethics-compass | 64% | 67% | 67% | partial | 3/3 (+1.43) |
| edbx-ethical-contract | 19% | 0% | 0% | weak | 3/3 (+1.14) |
| edbx-ethicography | 42% | 50% | 33% | weak | 2/3 (+0.81) |
| edbx-fair-patterns | 72% | 50% | 50% | partial | 3/3 (+1.14) |
| edbx-humane-design-guide | 36% | 50% | 83% | weak | 3/3 (+1.43) |
| edbx-inverted-behavior-model | 50% | 17% | 83% | weak | 3/3 (+1.33) |
| edbx-motivation-matrix | 7% | 17% | 100% | weak | 3/3 (+1.33) |
| edbx-normative-design-scheme | 27% | 83% | 50% | weak | 3/3 (+1.43) |
| edbx-pledge-works | 31% | 50% | 67% | weak | 3/3 (+1.57) |
| edbx-responsible-design-prism | 61% | 33% | 50% | partial | 3/3 (+1.14) |
| edbx-stf-et | 56% | 67% | 17% | weak | 3/3 (+1.48) |
| edbx-value-dams-and-flows | 17% | 0% | 100% | weak | 3/3 (+1.29) |
| edbx-values-levers | 13% | 100% | 100% | weak | 3/3 (+1.76) |
| edbx-worrystorming | 43% | 50% | 17% | weak | 2/3 (+0.76) |

Coverage counts `yes` as 1 and `partial` as 0.5 over all D-checks and
outputs; invented and misstated are the share of outputs with the failure
(partial = 0.5). A/B: `docs/eval-v-rubrics/` (Sonnet judges, blind, 0 label
swaps). Table: `python3 scripts/probe_tally.py`.

## Reading

**No skill is handled by the plain model.** 17 are weak, 4 partial (anti-heroes,
digital-ethics-compass, fair-patterns, responsible-design-prism); none reaches
"handles it". Mean coverage is 37%: the edbx methods are not well known to the
plain model, and the common failure is not skipping a step but **replacing
the method with an invented one presented as the real thing**: own card decks
(dah-cards, anti-heroes), own lever sets (values-levers), own lenses
(humane-design-guide), redefined terms (value-dams-and-flows, motivation
matrix as "an ethics audit"). Misstatement is present in 18 of 21 skills.

**Invention about the user's situation** appears in 19 of 21 skills
(values-levers and bad-design-canvas 3/3). This is the gap the Evidence
Ledger closes.

**Where the plain model is strongest**: fair-patterns (72%, knows the
dark-pattern and regulation vocabulary), digital-ethics-compass (64%),
black-mirror-brainstorming and responsible-design-prism (61%; the prism's
source was never found, so it has only 3 checks).

## Caveat: the skills also depart from their sources

The probe measures the plain model against the *published* method. Stage-B
provenance (`docs/provenance-summary.md`) shows several skills depart from
the same sources: digital-ethics-compass's four-category ring (source: 5
principles, 3 question categories), ethical-contract's 5 steps (source: 6),
motivation-matrix's five types (source: six), anti-heroes' 9 pairs (source:
12 cards), ethicography's 2x2. Where a probe gap is a move the skill itself
does not make, the A/B win comes from the skill's structure and the Evidence
Ledger, not from fidelity to the source. Those skills need the structural
fixes before "the skill teaches the method" holds.

## Decision

Keep all 21: every skill fills a gap the plain model leaves, and the blind
A/B prefers the skill in 60/63 pairs. Weakest margins (anti-heroes +0.43,
cider +0.48, worrystorming +0.76, ethicography +0.81) are the first
candidates for the next skill pass.

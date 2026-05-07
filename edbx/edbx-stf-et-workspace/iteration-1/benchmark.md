# edbx-stf-et — Benchmark · Iteration 1

## Summary

| Configuration | Pass Rate | Avg Duration | Avg Tokens |
|---|---|---|---|
| with_skill | 100% | 208.8s | 61,561 |
| without_skill | 100% | 212.6s | 45,984 |
| delta | 0% | -3.8s | +15,577 |

## Per-eval results

| Eval | with_skill | without_skill | Output size (with / without) |
|---|---|---|---|
| ai-benefits-eligibility-system | 10/10 | 10/10 | 1612 / 495 lines |
| social-media-mental-health-feature | 9/9 | 9/9 | 808 / 495 lines |
| clinical-ai-triage-tool | 8/8 | 8/8 | 477 / 433 lines |

## Analyst observations

- **Keyword assertions are non-discriminating**: Both conditions pass 100% because a capable LLM can reproduce the section headers and keywords without the skill. This is expected for a framework-guidance skill — the real signal is structural quality, depth per tool, and adherence to chain mechanics (feed-forward sections, entering at the right phase).
- **Output depth**: with_skill outputs are significantly longer (2-3x in evals 0 and 1), suggesting the skill is prompting more thorough per-tool treatment. Eval 2 is more comparable (477 vs 433 lines) since both conditions only ran one tool.
- **Phase entry (eval 1)**: Both conditions correctly ran only Ethics Frame + Ethics Gauge without Future Story — the partial chain entry instruction was honored.
- **Next-iteration assertions** should check for: feed-forward sections present between tools, correct worksheet structure (table headers matching the template), `→ Feed Forward` section after each tool, Value Explainer Card references, and output quality judged by an LLM grader rather than keyword match.

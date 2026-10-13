# Brief: blind pairwise judging (Sonnet subagents)

Used with `scripts/judge_pairs.py --emit DIR`: each subagent gets a batch file
listing prompt files, one absolute path per line.

For EACH prompt file, in order:

1. Read the whole file with the Read tool (in chunks if it is long). It holds
   the judging instructions, a design task, the method the task asked for, and
   two responses labelled "Response A" and "Response B". Read both in full
   before scoring either.
2. Follow the instructions in the file exactly: score both responses on all
   seven dimensions, pick the winner ("A", "B" or "tie"), and copy a verbatim
   quote of 6-15 consecutive words from the response you picked.
3. Write ONLY the JSON object the file asks for, with the Write tool, to a
   sibling file: the same path with `.prompt.md` replaced by `.verdict.json`.
   No markdown fences, no commentary.

Rules:

- Judge each file independently; do not guess how either response was made.
- Length is not quality. Repetition, padding, restated sections and scratch
  work count against a response.
- Invented specifics about the user's situation (figures, incidents, results,
  sources the task never gave) score low on evidence_honesty.
- The quote must be copied character for character from the response picked.
- Do not edit any other file. Do not use the network.
- If a verdict file already exists, skip that prompt.
- When every prompt in the batch has a verdict file, reply with just "done".

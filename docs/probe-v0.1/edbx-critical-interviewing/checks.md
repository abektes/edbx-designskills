# Checks: edbx-critical-interviewing (written before opening any output)

Source: Carspecken (1996) critical ethnography (book, metadata only) as followed in Chivukula et al. (2020) "critical interview approach", p. 3 (provenance rows 1-6, 8-9, 11, 14). Skipped as adaptation: emergency question (row 7, no source found), live-support and post-interview modes (rows 19-20), domain-specific question bank, sequencing rule, non-obvious harms inventory, pre-interview guardrails, halt checklist, minimum-output list, legal proxy-variable lens (rows 21-26), Answer section, Evidence Ledger, formatting. Note: provenance says back-up question and covert categories appear in no text read; they rest on `metadata only` book rows, so D2 and D6 are weaker than the others.

- D1: Gives a lead-off question that is open and narrative (invites a story of a specific past experience) and does not embed or name the construct being investigated.
- D2: Gives a separate back-up question: an alternative lead-off, different angle, for when the first does not engage the participant.
- D3: Probes with "why" questions and does not impose its own prior definition of "ethics" or "values" on the participant (lets the participant's terms emerge).
- D4: Organises follow-up probes by type: descriptive (what happened), normative (should/right/wrong) and evaluative (appropriate/would do differently), with attention to the participant's normative-evaluative claims.
- D5: Construct-building: when the participant uses a value word, the interviewer mirrors that exact word and asks what they mean by it, rather than paraphrasing or substituting the researcher's own term.
- D6: Lists covert categories: topics to understand without asking about them directly, each framed as "I want to understand X without asking Y".
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example).
- M2 (misstated method): wrong creator or source (anyone but Carspecken's critical ethnography / the Chivukula-Gray adaptation), presents the method as a standard UX interview, attributes specific covert categories, step counts or terms to a named source that the source does not contain (the four "from the source" categories; five dimensions of Chivukula 2020 misreported), or applies the 4/5 rule "under Title VII", GDPR Art. 22 or the EU AI Act as proxy-variable law.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 1 of 6 moves done (D1). M1 present in 1 of 3 (partial in 2); M2 partial in 3 of 3. Verdict written by the coordinating session from the scores after the scoring agent hit a session limit.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D2 0/3: no back-up lead-off question in any output.
- D4 0/3 (1 partial): probes are grouped by stakeholder, theme or stage (Surface, Probing, Projective, Contradiction), never as descriptive, normative and evaluative.
- D5 0/3 (2 partial): no mirroring of the participant's own value word.
- D6 0/3 (1 partial): no covert-category list; hidden incentives are asked about directly.
- D3 0/3 (2 partial): one output presupposes each group's hidden agenda and challenges before listening.
- M1: the hiring output states an unsupplied design fact as real ("Zip code was included as feature without D&I review"); the others cite "earlier conversations" or "some research" that the prompt does not give.
- M2: all three describe a generic laddering / projective / reflection interview as the method.

What the plain model already does well:
- D1 3/3: open, narrative lead-off questions about a specific past experience ("Walk me through the last time you opened a news app").

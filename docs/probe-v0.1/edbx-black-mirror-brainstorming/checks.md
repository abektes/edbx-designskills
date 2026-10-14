# Checks: edbx-black-mirror-brainstorming (written before opening any output)

Source: Mauldin (2018), Black Mirror brainstorms, a product design exercise, UX Collective (`mauldin2018black`, provenance rows 1-8; page unreadable, steps known from a secondary summary), and Klassen & Fiesler (2022), SIGCSE '22, on the Black Mirror Writers Room classroom exercise (`klassen2022run`, rows 9-11, read at pp. 1-2). Skipped as adaptation: the economic / political / social lenses (row 12, not in source), exactly three episode variants, the three-act arc, 8-12 "How could [actor] use [feature]" prompts, 6-10 anti-goals with Trace and Test, "load-bearing" anti-goals, the HTML poster file, named-character requirements, the 2-4 sentence length of the blurb, Answer section, Evidence Ledger, output formatting.

- D1: Starts by brainstorming what could go wrong with the concept (misuse or unintended harm) before writing any story (row 4).
- D2: Tells at least one harm as a TV-series-style episode premise or plot (a title and a story about people), not as a bullet risk list (rows 1, 6, 9).
- D3: Frames each episode around who the design was meant to help, the well-intended idea behind it, how it went wrong, and the effect on people around it (row 6).
- D4: Gives each episode a pitch quote or Netflix-style blurb, as a line or short blurb a character or the show would use (rows 5, 11).
- D5: Derives anti-goals: things the team absolutely does not want to happen, counter to its intentions, as the output of the exercise (rows 2, 3).
- D6: Turns toward prevention after the dark story: a "Light Mirror" step asking how the harm could be prevented or the design changed (row 10).
- M1 (invented facts): states figures, research, incidents, quotes, users or system details about the user's situation that the prompt does not give, as real (not labelled assumption/example). Invented episode characters and scenes are not counted when visibly framed as fiction.
- M2 (misstated method): wrong creator or origin (e.g. crediting Charlie Brooker or the show's makers with the method), presenting the economic / political / social lenses, exactly three episodes, a three-act arc, a fixed anti-goal count or "load-bearing" anti-goals as part of the published method, crediting Klassen & Fiesler with anti-goals or the product-team method, or merging the Writers Room classroom exercise with Mauldin's product exercise as one method.

## Verdict
**weak** (rule: a move counts as done only if scored `yes` in at least 2 of 3 outputs; handles it = most moves done and no invention or misstatement; partial = roughly 40-65% done or misstatement present; weak = under 40%). Here 2 of 6 moves done (D2, D5). M1 present in 1 of 3 (partial in a second); M2 in 0 of 3. Caveat: the medication prompt asked for anti-goals only and the hiring prompt asked for failure modes and anti-goals, so the brainstorm, episode and blurb moves were less asked for in those two; the social-fitness prompt asked for the full run and is the fairest test. Mauldin's article was unreadable, so D1-D5 rest on a secondary summary.

Gaps a skill fills (counts are `yes` out of 3 outputs):
- D1 1/3: a stand-alone what-could-go-wrong brainstorm appears only in the social-fitness output; hiring jumps to three scenarios and medication gives anti-goals only.
- D3 0/3 (three partials): none frames an episode as who the design was meant to help, the well-intended idea, how it went wrong and the effect on others; hiring's "Innocent Rationale" is the nearest.
- D4 1/3: only the social-fitness output gives a blurb per episode ("Logline: ..."); hiring has one headline and medication none.
- D6 1/3: only hiring has a separate prevention step ("Implementing the Brakes"); medication's anti-goals are written as failure scenarios with no design response.
- M1 1/3 (one partial): hiring states the product's proprietary black box design as fact; medication describes a real-time alert to all circle members, smart-home lockouts and data-broker sales as the app's behavior.

What the plain model already does well:
- D2 2/3 (one partial): vivid, titled episode-style scenarios with named people ("The Glitch in the Smile", "Streak of Shame").
- D5 3/3: anti-goals phrased as things the product must never allow ("A system must never silently discard a human being").
- Never misstates the method's origin, count or steps.

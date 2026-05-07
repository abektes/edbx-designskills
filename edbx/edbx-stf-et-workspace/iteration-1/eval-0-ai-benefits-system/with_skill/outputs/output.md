# STF-ET Ethics Assessment: AI System for Social Welfare Benefits Screening

**Chain Status:** Tools run: Future Story ✓ | Impacts Explorer ✓ | Ethics Frame ✓ | Ethics Gauge ✓ | Weighing Options ✓

---

## Tool 1 — Future Story

*A narrative exploration of what happens when an AI system screens and determines eligibility for government welfare benefits.*

### Spine Element 1 — PROBLEM / MOTIVATION
**"Once upon a time …"**

Government social welfare agencies face a critical bottleneck: case workers are overwhelmed with manual eligibility screening for housing assistance, food support, and unemployment benefits. Processing times are long, decisions are inconsistent across different workers, and the human workload creates backlogs that delay help to people in urgent need. The motivation is clear: deploy technology to reduce processing times, increase consistency, and ensure that eligible people receive support faster.

### Spine Element 2 — SOLUTION / VALUE PROP
**"Until one day …"**

A government agency develops an AI system trained on historical case data to automatically screen applications and make eligibility determinations. The system is designed to replicate human decision-making and reduce the time from application to initial decision from weeks to days. Two implementation approaches are considered:
- **Option A:** The AI is the primary decision-maker; appeals are reviewed by humans.
- **Option B:** The AI acts as a decision-support tool; all final decisions remain with case workers, who use AI recommendations to inform their judgment.

### Spine Element 3 — BENEFITS
**"And because of that …"**

**For eligible applicants:**
- Faster access to critical support (housing, food, employment assistance) for people in urgent need. Accelerated benefits distribution could prevent homelessness, food insecurity, and unemployment duration for thousands.
- Consistency: Decisions based on standardized criteria reduce the arbitrary variation that occurs when different case workers interpret eligibility rules.
- Potential expansion of reach: If processing becomes more efficient, the same budget and workforce could serve more people.

**For case workers:**
- Reduction in repetitive manual screening work, freeing time for complex cases requiring human judgment, follow-up, and relationship-building.
- Data-driven support tools can help workers understand which factors matter most and identify cases that need escalation.

**For the agency and public:**
- Cost savings from reduced manual processing and faster case resolution, potentially redirecting funds toward benefit amounts or additional support services.
- Improved metrics on processing time and decision consistency, enhancing public accountability.
- Opportunity to build on automated systems for other eligibility determinations across social services.

### Spine Element 4 — HARMS
**"But also …"**

**For applicants denied eligibility (correctly or incorrectly):**
- If the AI makes errors or is biased (e.g., learns patterns of historical discrimination embedded in training data), people in desperate need are incorrectly denied access to survival resources.
- False denials create cascading harms: homelessness, malnutrition, prolonged unemployment, family separation, health deterioration.
- Long appeals processes may mean months without benefits, and applicants may lack resources or knowledge to successfully appeal.

**For vulnerable populations:**
- If training data reflects historical inequities in case worker decisions, the AI replicates and scales that bias. Marginalized communities disproportionately denied or face longer approval times.
- Applicants with non-standard situations (recent migrants, undocumented status, complex family structures, mental health conditions) may not fit algorithmic patterns and are disadvantaged.
- Loss of individualized judgment: case workers historically could use discretion to grant benefits to people in edge cases; AI systems operate on rigid rules.

**For case workers:**
- Deskilling and job loss: If the system is framed as replacing workers, morale and training investments suffer. Workers laid off lose stable employment.
- Pressure to align with algorithmic recommendations even when they believe it's wrong, reducing autonomy and professional judgment.

**For the agency:**
- Reputational and legal risk: High-profile algorithmic errors harming vulnerable people create public backlash and lawsuits.
- Data security and privacy risks: centralized AI system holding sensitive benefit information becomes a target for breaches or misuse.
- Regulatory exposure: If the algorithm is not transparent or cannot be audited, agencies may violate civil rights requirements (disparate impact law).

**For public trust:**
- Perception that government cares more about efficiency than human need. If the system is seen as rationing benefits through opaque technology, trust in institutions erodes.

### Spine Element 5 — SUBSEQUENT IMPACTS
**"In turn …"**

**Cascading from benefits:**
- Faster benefit access reduces upstream costs in emergency services (hospital visits for malnutrition, police involvement with homeless individuals, incarceration).
- Restored dignity and self-sufficiency: People who receive timely support can stabilize housing, employment, and family structure, reducing long-term social costs and enabling economic mobility.
- Workforce stability: Case workers freed from manual work increase job satisfaction and stay with the agency longer, building institutional knowledge.
- Trust spillover: If the system demonstrably improves service without harming people, it builds confidence in government's capacity and good intent, strengthening democratic legitimacy.

**Cascading from harms:**
- Systemic exclusion deepens: If the AI denies benefits more consistently than human workers did, it institutionalizes existing patterns of discrimination. Communities already underserved by government become further marginalized.
- Poverty persistence: Incorrectly denied applicants remain in crisis longer, losing leverage for employment, housing, family reunification. Harms compound across generations.
- Organizational culture shifts: If the agency frames the AI as replacing workers, workplace becomes adversarial. Trust between managers and staff collapses. Workers become less willing to flag problems, creating a culture of silence around errors.
- Erosion of public trust: When people learn the algorithm denied them benefits incorrectly and appeals took months, they lose faith in government fairness. Cynicism spreads.
- Feedback loop amplification: Repeated denied-then-appealed cases teach the agency nothing about bias if the focus is only on processing volume, not fairness. The system learns only that certain demographic patterns are "less likely to be eligible."

**Values impacted:**
- **Dignity:** Automation that treats people as data points rather than individuals undermines their inherent worth.
- **Justice:** If harms and benefits are distributed unequally across socioeconomic or demographic lines, distributive justice is violated.
- **Autonomy:** Case workers lose professional judgment; applicants lose ability to present their full story.
- **Trust:** Government-citizen trust erodes if people believe the system is neither transparent nor fair.
- **Well-being:** Incorrect denials directly harm physical and psychological well-being of applicants and families.
- **Relationships:** Reduction in human interaction in case work erodes the relational support and advocacy that case workers historically provided.
- **Responsibility:** Agency must take accountability for algorithmic errors affecting life-altering decisions.

### Spine Element 6 — MITIGATING ACTIONS
**"One thing we could have done differently is …"**

1. **Implement robust bias auditing before and during deployment:** Conduct disparate impact testing to identify whether the system denies or approves benefits at different rates for different demographic groups. Establish a 6-month pre-deployment audit period and ongoing quarterly audits to catch bias early. If disparate impact is found, retrain the model or change deployment approach.

2. **Design Option B as the default (AI as decision support, not replacement):** Ensure humans remain final decision-makers and can override AI recommendations with documented justification. This preserves autonomy, allows for edge cases, and creates an accountability layer.

3. **Establish a transparent appeals process:** Guarantee that denied applicants can appeal to a human case worker within 5 business days, with expedited review for urgent cases (homelessness, hunger). Publish aggregate data on appeal outcomes quarterly to show whether appeals are succeeding and whether any demographic group appeals more often (a signal of bias).

4. **Preserve case worker jobs; rebrand as augmentation:** Explicitly commit that no case workers will be laid off due to automation. Instead, redeploy freed time toward face-to-face support for complex cases, follow-up on benefit retention, and job training services. This protects workers and acknowledges their continued value.

5. **Build in explainability and contestability:** Require that when the AI recommends a decision, it provides a human-readable summary of the key factors driving that recommendation (e.g., "You meet income threshold for housing assistance; your reported household size exceeds the limit for Unit Type X"). Applicants can see why they were denied and challenge the assumptions.

6. **Establish a multi-stakeholder oversight committee:** Include case workers, applicants or their advocates, civil rights organizations, and the agency's leadership to meet monthly. Review decisions flagged by the system or by applicants as potentially unfair. Use this body to catch systemic patterns and make recommendations to the AI team.

7. **Create a feedback loop for continuous improvement:** Track outcomes for applicants who received benefits (did they exit homelessness? Find employment?) and those who were denied (what happened?). Use this long-term outcome data to assess whether the AI is actually helping, not just processing faster. If an option does not improve outcomes for vulnerable groups, modify it.

---

## Tool 2 — Impacts Explorer

*Mapping the direct, secondary, and value-level effects of deploying an AI system for benefits screening.*

### Center: Action / Creation
**AI System for Automated Eligibility Screening of Social Welfare Benefits**

The government agency implements machine learning to automatically screen applications for housing assistance, food support, and unemployment benefits, with two possible approaches: (A) AI as primary decision-maker with human appeals, or (B) AI as decision-support tool with human final decisions.

---

### Direct Effects (First Ring)

#### From the Solution (Introduction of AI System):

**D1 — Faster Processing Speed**
- Applications processed in days instead of weeks
- Affects: All applicants, case workers

**D2 — Increased Consistency in Decisions**
- Same criteria applied uniformly across cases
- Affects: All applicants, the agency, civil rights compliance

**D3 — Case Worker Workload Reduction (for screening tasks)**
- Manual eligibility screening automated; workers freed for other tasks
- Affects: Case workers, organizational capacity

**D4 — Potential for Scalability**
- Same system could handle growing application volume without proportional hiring
- Affects: The agency, applicant access to service

**D5 — Reduced Agency Processing Costs**
- Labor costs for manual screening decline
- Affects: Agency budget, potential for benefit expansion or redeployment

**D6 — Centralization of Decision-Making (in the algorithm)**
- Decisions driven by a single model rather than distributed human judgment
- Affects: Applicants, case workers, the agency's accountability

**D7 — Loss of Individualized Case Assessment**
- Algorithmic application of rules cannot account for unique circumstances not in the training data
- Affects: Applicants in non-standard situations, case workers' ability to advocate

**D8 — Data Concentration and Privacy Risk**
- All applicant personal/financial data centralized in AI system
- Affects: Applicants' privacy, security vulnerability, potential for misuse

**D9 — Increased Transparency (if designed for it) or Opacity (if not)**
- Depending on implementation, system may reveal decision logic or be a "black box"
- Affects: Applicants' ability to understand and contest decisions

---

### Secondary Effects (Ripple Consequences)

#### From D1 — Faster Processing → D1a, D1b, D1c:

**D1a — Earlier Access to Benefits for Eligible Applicants**
- Reduced time to housing, food, or employment support for people in crisis
- Secondary effect: Reduced homelessness episodes, improved nutrition, faster exit from unemployment
- Secondary effect: Families remain together; children remain in school
- Secondary effect: Reduced reliance on emergency services (hospital, police, shelters)

**D1b — Applicants Face Uncertainty During Processing**
- Faster processing may increase anxiety if appeals process is unclear or backlogged
- Secondary effect: Applicants in limbo may make worse decisions (skip medical care, leave children in unsafe situations to work) rather than wait for outcome
- Secondary effect: Mental health effects from uncertainty

**D1c — Efficiency Pressure Incentivizes Denial**
- If the system is measured on "cases processed per day," it may be biased toward quick denials rather than thorough assessment
- Secondary effect: Eligible applicants incorrectly denied, appealing later at psychological and financial cost

---

#### From D2 — Increased Consistency → D2a, D2b, D2c:

**D2a — Standardized Criteria Applied Equally**
- If the criteria are fair, consistency is good: everyone meets the same bar
- Secondary effect: Eligible people in different regions, handled by different workers, get the same treatment
- Secondary effect: Reduced perception of favoritism or corruption

**D2b — Historical Bias Scaled Up (if criteria embed prior discrimination)**
- If the training data reflects past case worker bias or systemic discrimination, the AI replicates and amplifies it
- Secondary effect: Certain demographic groups (e.g., people of color, immigrants, single mothers) systematically denied or approved at lower rates
- Secondary effect: Perception of algorithmic discrimination erodes trust in institution

**D2c — Edge Cases and Exceptions Excluded**
- Consistency achieved by treating all cases the same, but loses discretion that case workers used for edge cases
- Secondary effect: Applicants who meet the spirit but not the letter of the rule are harmed (e.g., a family $50 over income threshold due to one-time bonus)

---

#### From D3 — Case Worker Workload Reduction → D3a, D3b, D3c:

**D3a — Workers Redeploy to Complex Cases (Best Case)**
- If redeployment is planned and supported, workers focus on cases requiring judgment, advocacy, or follow-up
- Secondary effect: Complex applicants receive better support
- Secondary effect: Workers experience greater job satisfaction and autonomy

**D3b — Workers Lay Off or Deskill (Worst Case)**
- If automation is framed as job replacement, workers are laid off or reassigned to lower-skill tasks
- Secondary effect: Loss of institutional knowledge and case worker expertise
- Secondary effect: Worker morale collapses; organizational culture becomes adversarial
- Secondary effect: High turnover of remaining staff reduces continuity of care

**D3c — Workers Become Rubber Stampers**
- If workers are expected to approve AI recommendations without review, their role becomes validation theater
- Secondary effect: Workers lose professional judgment; they become accountable for system errors they didn't make
- Secondary effect: Workers stop flagging problems because they have no power to change decisions

---

#### From D6 — Centralization of Decision-Making → D6a, D6b, D6c:

**D6a — Reduced Human Discretion Affects Vulnerable Groups Disproportionately**
- Case workers historically had discretion to grant exceptions; applicants could appeal to human judgment and advocacy
- Secondary effect: Applicants who don't fit algorithmic categories (undocumented immigrants, people with disabilities, those in crisis) lose recourse
- Secondary effect: Vulnerable groups experience system as more rigid and less empathetic

**D6b — Accountability Diffuses Across Team**
- When decision is made by algorithm, who is responsible if it's wrong?
- Secondary effect: Agency claims algorithm is neutral; applicants or civil rights groups blame agency; agency deflects to technologists
- Secondary effect: No clear locus of accountability for errors

**D6c — Organizational Learning Stagnates**
- If workers are not reviewing decisions, case worker knowledge about what works and what doesn't is not fed back into the agency
- Secondary effect: The agency becomes less responsive to applicant needs over time
- Secondary effect: Feedback loops that would improve service disappear

---

#### From D7 — Loss of Individualized Assessment → D7a, D7b:

**D7a — Non-Standard Family Structures or Circumstances Disadvantaged**
- Recent immigrants, multigenerational households, people in transition, those with complex mental health or addiction issues
- Secondary effect: Applicants who most need human advocacy are least likely to get it
- Secondary effect: Compounding disadvantage: already-excluded people further excluded by technology

**D7b — No One Advocates for the Applicant**
- Case workers historically served dual roles: administrator and advocate
- Secondary effect: Applicant has no one inside the system arguing for their eligibility or explaining their circumstances
- Secondary effect: Appeals process becomes necessary even for cases that should have succeeded on first review

---

#### From D8 — Data Concentration and Privacy Risk → D8a, D8b:

**D8a — Breach of Sensitive Personal Data**
- Centralized database with all applicant information becomes high-value target for theft
- Secondary effect: Identity theft, fraudulent benefit claims made in applicant names, further harm to vulnerable people
- Secondary effect: Public perceives government as unable to protect sensitive information, eroding trust

**D8b — Misuse of Data Within Government**
- If the benefits database is shared with immigration enforcement, law enforcement, or other agencies without applicant consent
- Secondary effect: Applicants, especially undocumented immigrants, avoid applying out of fear
- Secondary effect: People who need help most do not access it

---

### Values Impacted (Third Ring)

**Well-being:**
- +Enhanced by: Faster access to benefits, reduced homelessness and food insecurity, improved health outcomes for eligible applicants
- −Diminished by: Incorrect denials, prolonged crisis for denied applicants, uncertainty and anxiety during processing, mental health impact of perceived injustice

**Justice:**
- +Enhanced by: Consistent application of rules, reduced arbitrary variation between case workers
- −Diminished by: If historical bias embedded in training data, leading to disparate denial rates; if benefits and harms distributed unequally across demographic groups; if edge cases unfairly excluded

**Trust:**
- +Enhanced by: Faster service, transparent criteria (if made visible)
- −Diminished by: Opaque algorithms, high-profile errors, perception that efficiency matters more than fairness, feeling that government does not understand individual circumstances

**Dignity:**
- +Enhanced by: Respect for efficiency and responsiveness to people's urgent needs
- −Diminished by: Treating applicants as data points, lack of human acknowledgment, feeling that the system does not recognize one's full humanity or circumstances

**Autonomy:**
- +Enhanced by: If Option B (decision-support), human case workers retain authority and can override AI; applicants have human recourse
- −Diminished by: If Option A (AI as primary), applicants lose ability to present their full story or appeal to human judgment; case workers lose professional autonomy

**Responsibility:**
- +Enhanced by: Clear accountability for algorithmic decisions through oversight and audit
- −Diminished by: Diffused accountability, agency deflecting to algorithm, no clear entity responsible for errors

**Relationships:**
- +Enhanced by: If redeployment allows case workers to deepen support relationships with applicants
- −Diminished by: Reduced human interaction, transactional experience of benefits system, loss of relational continuity

---

### Stakeholder-Specific Impacts

#### Group 1: Applicants with Straightforward, Standard Cases
**Effects:** Strong positive. Faster approval, reduced uncertainty. Consistency is beneficial because their case clearly meets criteria.
**Value alignment:** Well-being, autonomy (if option B preserves appeals), justice (if no bias).

#### Group 2: Applicants in Non-Standard Situations (Recent Immigrants, Undocumented, Complex Family Structure, Mental Illness, Addiction, Extreme Poverty)
**Effects:** Likely negative. Algorithm cannot account for their circumstances; likelihood of incorrect denial is high; they have least resources to appeal. They benefit least from speed if the speed means they are quickly rejected.
**Value alignment:** Dignity, justice, autonomy (least preserved).

#### Group 3: Case Workers
**Effects (Best case):** Positive. Freed from repetitive work, can focus on complex cases, greater autonomy and job satisfaction.
**Effects (Worst case):** Negative. Job loss, deskilling, reduced autonomy, pressure to align with AI recommendations they disagree with.
**Value alignment:** Autonomy, responsibility (if their role is clear), relationships (if they can deepen applicant relationships).

#### Group 4: The Government Agency
**Effects:** Mixed. Cost savings, efficiency gains, increased risk of reputational damage, legal liability, and loss of institutional knowledge.

#### Group 5: The Public (Taxpayers, Communities)
**Effects:** Mixed. Reduced costs may mean more benefits available to more people (positive). Perception of uncaring automation may erode trust in government (negative).

---

### Fairness Patterns Observed

- **Distribution of benefits:** Likely unequal. Applicants with straightforward cases benefit from speed; applicants in edge cases benefit less or are harmed.
- **Distribution of harms:** Likely unequal. If bias exists in training data, marginalized groups bear disproportionate harm. Those with least resources (legal, social, informational) to appeal are most harmed by errors.
- **Historical context:** Benefits system itself has a history of discrimination and exclusion; AI risks scaling and institutionalizing those patterns rather than correcting them.

---

### Conclusion of Impacts Explorer

The AI system creates a trade-off between **efficiency** (faster processing for eligible applicants) and **equity** (ensuring non-standard cases and vulnerable groups are not harmed). The direction and magnitude of this trade-off depend heavily on:
1. Whether the AI is the final decision-maker (Option A) or decision-support (Option B)
2. Whether robust bias auditing occurs pre-deployment and ongoing
3. Whether case workers are preserved, supported, and empowered to override algorithmic decisions
4. Whether applicants have meaningful appeal rights and transparency

**→ Carries forward to Tool 3:** Consolidated effects (faster processing, consistency, workload reduction, risk of bias), values (well-being, justice, trust, dignity, autonomy, responsibility, relationships), stakeholder differential impacts (standard vs. non-standard cases; case workers; agency; public), fairness concerns (unequal distribution of benefits, marginalized groups at greater risk of harm).

---

## Tool 3 — Ethics Frame

*Structured evaluation of the ethical considerations, benefits, harms, and actions in response.*

### Section 1 — ACTION / CREATION

**AI System for Automated Eligibility Screening of Social Welfare Benefits**

A government agency proposes to deploy machine learning technology to automatically screen and make initial eligibility determinations for housing assistance, food support, and unemployment benefits. Two implementation options are under consideration:
- **Option A:** AI is the primary decision-maker; applicants can appeal to a human case worker.
- **Option B:** AI provides decision-support recommendations; all final decisions are made by case workers who can see the AI's reasoning and override it.

The system would replace manual case worker screening to reduce processing time, increase consistency, and improve agency efficiency.

---

### Section 2 — VALUES (Part One: Explore the values that matter)

#### Values Driving the Work:
- **Efficiency and Responsiveness:** The agency aims to serve people faster, reducing the time between application and decision so that people in urgent need (facing homelessness, hunger, unemployment) get support quickly.
- **Consistency:** Standardizing eligibility decisions across case workers and regions to reduce arbitrary variation and ensure equal treatment under the law.
- **Stewardship:** Using public resources (case worker time, agency budget) responsibly to maximize the number of people served.

#### Broader Values Impacted:

*From Value Cards:*
- **Well-being:** Rapid access to benefits promotes health and stability; incorrect denials or delays undermine well-being.
- **Justice:** Consistent application of rules supports fairness; but if rules embed bias or edge cases are unfairly excluded, justice is compromised.
- **Dignity:** Respect for people as individuals with unique circumstances; algorithmic processing risks treating people as data points.
- **Autonomy:** People's ability to make informed choices about their own lives; also, case workers' professional autonomy and judgment.
- **Trust:** Public confidence in government institutions to act fairly and in good faith; opacity or high-profile errors erode trust.
- **Responsibility:** The agency's accountability for decisions affecting life-altering access to survival support.
- **Relationships:** The relational support and advocacy case workers historically provided; risk of transactional service model.

#### Assessment of Impact on Values:

**Consistency (Efficiency and Responsiveness):**
- Will be **reinforced** if the system operates as designed: faster processing, uniform rules, more applications handled.
- BUT will be **undermined** if speed incentivizes denial, or if consistency is "consistent unfairness" (systematic denial of edge cases or certain demographic groups).

**Well-being:**
- **Enhanced** for applicants with standard cases who are quickly approved and access benefits.
- **Undermined** for applicants who are incorrectly denied, who face uncertainty, or who lose human advocacy that might have resulted in approval.
- Magnitude of harm: Denial of housing or food assistance directly impacts survival; psychological impact of feeling the system does not understand you.

**Justice:**
- **Enhanced** if the system applies equal criteria to all and reduces arbitrary case-worker variation.
- **Undermined** if historical bias in training data leads to disparate impact (e.g., systematically lower approval rates for certain demographic groups). Also undermined if "equal treatment" means edge cases are treated identically to standard cases and thus unfairly.

**Dignity:**
- **Undermined** if people experience the system as treating them as data points rather than recognizing their humanity, individual circumstances, and worth.
- Reduced when applicants cannot present their full story or appeal to human judgment.

**Autonomy:**
- **For applicants:** Enhanced if they can contest decisions (Option B preserves this more than Option A); undermined if final decisions are algorithmic and appeals are difficult or slow.
- **For case workers:** Enhanced if they remain empowered to override AI and use professional judgment (Option B); undermined if they become rubber-stampers or are laid off (risk under Option A).

**Trust:**
- Enhanced if the system delivers faster, fairer service and is transparent.
- Undermined if errors are high-profile, if certain groups experience disproportionate denial, or if the system is seen as a cost-cutting measure rather than an improvement.

**Responsibility:**
- Enhanced if clear accountability is established for algorithmic decisions and regular auditing occurs.
- Undermined if accountability diffuses ("it was the algorithm") and the agency avoids responsibility for errors.

**Relationships:**
- Undermined if human interaction is reduced and case workers are unable to advocate or provide relational support.
- Enhanced if redeployment allows deeper, more meaningful case worker engagement with complex cases.

---

### Section 3 — BENEFITS

#### Catalog of Benefits:

**Benefit 1: Faster Access to Survival Support**
- **Who benefits:** Applicants with standard cases (straightforward income, household size, housing, employment status). Particularly: families at risk of homelessness, individuals experiencing food insecurity, unemployed people needing urgent support.
- **Preference:** Applicants desire faster approval and immediate relief.
- **Well-being:** Faster benefit access improves health, stability, family cohesion, and exit from crisis.

Extent:
- **Magnitude:** High. Each day of processing delay for someone in housing crisis is a day closer to homelessness. Faster access means the difference between stability and catastrophe.
- **Scope:** All eligible applicants, though benefit accrues most to those in the most urgent situations.
- **Likelihood:** High. System is designed to process faster.
- **Duration:** Enduring. Once benefits are accessed, the applicant can stabilize. Benefit persists.

**Benefit 2: Increased Consistency and Perceived Fairness**
- **Who benefits:** All applicants. Those who would have been rejected by a biased case worker now have equal criteria applied. Those with standard cases experience the same treatment regardless of which case worker reviews them.
- **Preference and well-being:** People desire and experience well-being from a system that treats everyone fairly and consistently.

Extent:
- **Magnitude:** Medium to high. Consistency matters to people's sense of justice and trust in institutions.
- **Scope:** All applicants.
- **Likelihood:** Medium-high. Consistency is likely if the algorithm is properly designed, but depends on whether historical bias is in the training data.
- **Duration:** Enduring.

**Benefit 3: Institutional Efficiency and Cost Reduction**
- **Who benefits:** The agency and the public (through lower costs per benefit distributed, potential for expanded services).
- **Preference and well-being:** Taxpayers and the public benefit from stewardship of public resources; the agency benefits from operational efficiency.

Extent:
- **Magnitude:** Medium. Labor cost savings are significant per decision; across thousands of cases, they accumulate.
- **Scope:** Wide. Benefits the agency, taxpayers, and by extension, all people who rely on government services.
- **Likelihood:** High. Automation typically reduces labor costs.
- **Duration:** Enduring, though diminishing if the system requires ongoing maintenance.

**Benefit 4: Case Worker Redeployment (if managed well)**
- **Who benefits:** Case workers and complex-case applicants.
- **Preference and well-being:** Case workers prefer meaningful work; complex-case applicants prefer personalized attention.

Extent:
- **Magnitude:** Medium to high, if redeployment is genuine and supported with training and job security.
- **Scope:** Limited to case workers and complex-case applicants, but these are vulnerable populations.
- **Likelihood:** Medium. Depends on organizational commitment to redeployment, not displacement.
- **Duration:** Enduring, though diminishing if the agency does not maintain commitment.

**Benefit 5: Reduced Eligibility Errors in Standard Cases (if algorithm is accurate)**
- **Who benefits:** Applicants in standard cases.
- **Well-being:** Fewer eligible people are incorrectly denied because the algorithm is more consistent than human error.

Extent:
- **Magnitude:** Medium. Some human case workers make errors; algorithm would reduce those.
- **Scope:** Applicants with standard cases.
- **Likelihood:** Medium. Depends on algorithm accuracy and whether historical bias is present.
- **Duration:** Enduring.

---

### Section 4 — HARMS

#### Catalog of Harms:

**Harm 1: Algorithmic Bias Leading to Disparate Denial Rates**
- **Who is harmed:** Applicants from demographic groups underrepresented in historical approved cases (people of color, immigrants, recent arrivals, those with non-standard family structures, people with criminal histories).
- **Type of harm:** Systematic denial of eligibility for people who should be approved, based on learned patterns of historical discrimination.
- **Mechanism:** Training data reflects past case worker bias, discriminatory policies, or systemic exclusion. Algorithm learns "people of color are less likely to be approved" → applies this pattern → denies at higher rates.

Extent:
- **Magnitude:** Severe. Denial of housing or food assistance is catastrophic harm: homelessness, malnutrition, family separation, health deterioration.
- **Scope:** Could affect hundreds or thousands across a large agency. If the algorithm is deployed statewide or nationally, even 2-3% disparate impact affects thousands.
- **Likelihood:** Medium to high. Historical data in many social services contains documented bias; machine learning amplifies patterns in training data.
- **Duration:** Enduring. Unless bias is detected and the model is retrained, it persists and compounds over time as the system processes more cases.

**Harm 2: Loss of Discretion and Advocacy for Edge Cases**
- **Who is harmed:** Applicants in non-standard situations (recently immigrated, undocumented, multigenerational households, mental illness, addiction, extreme poverty, recent job loss due to medical emergency).
- **Type of harm:** Algorithmic rigidity means people who meet the spirit of the rule but not the letter are automatically denied. Historically, case workers could grant exceptions; now there is no human recourse at the decision stage.
- **Mechanism:** Algorithm applies rules mechanically; there is no exception pathway for edge cases unless appeals process is robust.

Extent:
- **Magnitude:** High. Edge cases are often the most vulnerable; they have the least resources to appeal and the most to lose from denial.
- **Scope:** Estimate 5-15% of applications fall into edge cases or non-standard categories.
- **Likelihood:** Very high. Algorithmic systems are rigid by design.
- **Duration:** Enduring. Every edge case is harmed until exception is found and appealed.

**Harm 3: Incorrect Denials and Failed Appeals**
- **Who is harmed:** Applicants who are incorrectly denied and lack the resources, knowledge, or time to appeal successfully.
- **Type of harm:** Loss of access to critical support due to system error or misinterpretation of applicant situation.
- **Mechanism:** Algorithm makes a mistake (missing a document, misinterpreting household structure, failing to account for recent income change). Applicant does not appeal because they do not understand the process, lack documentation, or give up. They are denied.

Extent:
- **Magnitude:** High. Loss of housing or food support is catastrophic.
- **Scope:** Depends on algorithm accuracy and appeal process effectiveness. If accuracy is 95%, 5% of applications are incorrect. At 10,000 applications per year, 500 incorrect denials. If 20% successfully appeal, 400 remain denied.
- **Likelihood:** High. No algorithm is 100% accurate. Appeals processes are often backlogged or unclear.
- **Duration:** Enduring for each individual. Months without benefits creates compounding harm.

**Harm 4: Case Worker Displacement, Deskilling, or Loss of Autonomy**
- **Who is harmed:** Case workers.
- **Type of harm:** Job loss, reduced job satisfaction, loss of professional judgment, pressure to align with algorithmic decisions they believe are wrong.
- **Mechanism:** If automation is framed as job replacement, workers are laid off or reassigned to lower-skill work. If workers remain, they may be expected to simply process or approve AI recommendations without review.

Extent:
- **Magnitude:** Medium to high. Loss of stable employment is devastating; deskilling reduces job satisfaction and career prospects.
- **Scope:** All case workers involved in eligibility screening.
- **Likelihood:** Medium to high, depending on organizational messaging and commitment to redeployment.
- **Duration:** Enduring. Job loss is permanent unless alternative employment is available.

**Harm 5: Reduced Relational Support and Advocacy**
- **Who is harmed:** Applicants, particularly vulnerable applicants who benefit from case worker understanding and advocacy.
- **Type of harm:** Loss of relational support, someone advocating within the system for their needs, and personalized guidance.
- **Mechanism:** Case workers moved away from individual case review and into routine processing or higher-volume work. Human interaction and relationship-building replaced by algorithmic transactions.

Extent:
- **Magnitude:** Medium. Loss of relational support is a long-term harm; it affects trust and efficacy of the system over time.
- **Scope:** All applicants, with greatest impact on vulnerable populations who most need advocacy.
- **Likelihood:** High. Reduction in human interaction is inherent to automation.
- **Duration:** Enduring. The relationship is lost.

**Harm 6: Centralization of Data and Privacy Risk**
- **Who is harmed:** Applicants.
- **Type of harm:** Breach of sensitive personal and financial information; misuse by government agencies; identity theft; exploitation.
- **Mechanism:** All applicant data (income, assets, family structure, address, health conditions, criminal history) centralized in the AI system. If breached or shared without consent (e.g., with immigration enforcement), harm cascades.

Extent:
- **Magnitude:** Severe. Identity theft and fraudulent benefit claims compound harm to already-vulnerable people. Fear of government data sharing deters applications.
- **Scope:** All applicants whose data is in the system.
- **Likelihood:** Medium. Breaches are increasingly common; data sharing within government agencies is an ongoing risk.
- **Duration:** Enduring. Once data is breached, identity theft can occur for years. Fear of data misuse persists.

**Harm 7: Eroded Public Trust in Government and Institutions**
- **Who is harmed:** The public, the agency, the legitimacy of democratic institutions.
- **Type of harm:** Loss of trust if the algorithm is seen as uncaring, biased, or failing high-profile cases; perception that the government prioritizes efficiency over human need.
- **Mechanism:** If news reports prominent cases where the algorithm denied benefits to people in desperate circumstances, or if certain communities report disproportionate denials, public trust in government erodes.

Extent:
- **Magnitude:** Medium to high. Trust is foundational to democratic legitimacy; loss of trust has downstream effects on civic participation.
- **Scope:** Wide. Effects entire public's trust in government.
- **Likelihood:** Medium. High-profile algorithmic failures are common; media coverage is likely.
- **Duration:** Enduring. Trust erosion is slow to rebuild.

**Harm 8: Diffused Accountability and Moral Hazard**
- **Who is harmed:** Applicants, public.
- **Type of harm:** No one takes responsibility for algorithmic errors; agency deflects to the technology; technologists claim they only built what was asked for.
- **Mechanism:** When harm occurs (incorrect denial, data breach, disparate impact), responsibility diffuses. Agency claims the algorithm is neutral; applicants have no clear entity to hold accountable.

Extent:
- **Magnitude:** Medium. Lack of accountability means harms are not addressed and the system is not improved.
- **Scope:** All applicants harmed and the public.
- **Likelihood:** High. Diffusion of responsibility is a common problem in algorithmic systems.
- **Duration:** Enduring. Without accountability, patterns are not corrected.

---

### Section 5 — WHO IS AFFECTED, IN WHAT WAY

#### Fairness Spectrum:

```
GREAT BENEFIT  ←————————————————→  GREAT HARM

Applicants with        |          Applicants in
standard cases         |          edge cases and
(clear income,         |          vulnerable
straightforward        |          situations
household, no          |          (immigrant,
complications)         |          undocumented,
                       |          non-standard
Benefit: faster        |          family, mental
approval,              |          illness, extreme
consistency            |          poverty)
                       |          
                       |          Harm: rigid rules,
                       |          lack of discretion,
Case workers          |          higher likelihood
(if redeployed)       |          of incorrect denial,
                       |          no advocacy
Benefit: freed from    |          
repetitive work,       |          Case workers
greater autonomy       |          (if displaced)
                       |          
                       |          Harm: job loss,
Agency                 |          deskilling, loss
                       |          of autonomy
Benefit: cost          |          
reduction, faster      |          Public trust
processing             |          
                       |          Harm: perception
                       |          of uncaring system,
                       |          erosion of trust
```

#### Distributional Fairness Assessment:

**Are already-marginalized groups facing outsized harms?**

Yes. Evidence suggests:
- If training data reflects historical bias in the social services system, people of color, immigrants, and people with stigmatized conditions (mental illness, addiction, involvement with criminal justice) will experience higher denial rates.
- These groups are also most vulnerable to the loss of discretion and advocacy: they have the least resources to appeal, least access to legal representation, and most complex situations that do not fit algorithmic categories.
- They are most at risk from data breaches and misuse (fear of immigration enforcement, exploitation).

**Are privileged groups capturing most of the benefit?**

Implicitly, yes. Applicants with standard cases, clear documentation, and straightforward situations benefit from speed and consistency. These groups are more likely to be people with higher education, stable employment history, and familiarity with bureaucracy. Conversely, people lacking these advantages benefit least.

**Are some unable to access benefits due to economic or social barriers?**

Yes. Even with the system, barriers include:
- Lack of knowledge about how to apply or appeal
- Documentation challenges (lack of ID, proof of residence, income records)
- Language barriers
- Fear of government agencies (undocumented immigrants, criminal justice involvement)
- Complexity of their situation that the algorithm cannot address

With the algorithm, the barrier is higher: if the system quickly denies you, your only recourse is an appeals process that may be slow, unclear, or still algorithmic.

---

### Section 6 — VALUES (Part Two: Plan for action in alignment with values)

#### What values are you prioritizing over others, and why?

After analyzing effects and their distribution, we must make trade-offs between values. Here are the key tensions:

**Efficiency (and Consistency) vs. Dignity and Autonomy:**

The system prioritizes processing speed and consistency over individualized treatment and human judgment. This is a values choice: we are saying that serving more people faster and treating everyone by the same rule is more important than taking time to understand each person's unique situation or empowering case workers to use their judgment.

**Justification:** This trade-off may be justified if:
1. The speed genuinely helps people in crisis (and it may, for the majority with standard cases).
2. Safeguards are in place to prevent dignity-undermining automation: case workers remain empowered to override (Option B), appeals are fast and robust, the system is transparent.
3. We commit to ongoing bias auditing and model correction; the consistency is not "consistent unfairness."

**Well-being (for most) vs. Justice (for the marginalized):**

The system likely improves well-being for most eligible applicants (faster access). But it may worsen justice for marginalized groups if bias is present or edge cases are systematically excluded.

**Justification:** This trade-off is not justified unless:
1. We commit to bias auditing and correction before deployment.
2. We establish a robust appeals and exception process for edge cases.
3. We commit to ongoing outcome tracking to measure whether marginalized groups are experiencing worse outcomes.
4. If disparate impact is found, we are willing to pause or modify deployment.

**Trust vs. Efficiency:**

Building and maintaining public trust takes time, relationship-building, and transparency. Automation prioritizes efficiency and scale. These can conflict.

**Justification:** Justifiable only if:
1. We proactively build trust through transparency, accountability mechanisms, and community engagement.
2. We prioritize fixing high-profile errors quickly, rather than defending the system.
3. We involve affected communities in oversight and governance.

---

### Section 7 — HOW TO EXPAND BENEFITS

#### Strategies to Maximize Positive Impacts:

**Strategy 1: Design for Speed Without Sacrificing Fairness**
- Establish a service level agreement: 80% of standard cases approved or denied within 5 business days, including initial appeals.
- For edge cases, allocate them immediately to human case worker review rather than attempting algorithmic determination.
- Measure: Track approval time by case type and demographic group; ensure speed is equitable across groups.

**Strategy 2: Transparent Decision Reasoning**
- Whenever the system makes a decision (approval or denial), generate a human-readable summary of the key factors: "You met income requirement (✓), household size exceeds threshold for this unit type (✗), so you are eligible for housing support but not the specific unit size you requested."
- Applicants can see why and can contest specific factors.
- Measure: Survey applicants on whether they understand why they were approved or denied.

**Strategy 3: Robust Appeals Process**
- Guarantee a human case worker review within 5 business days of appeal.
- Explicitly authorize case workers to override algorithmic decisions and approve exceptions if they believe the applicant meets the spirit of the rule.
- Publish quarterly data on appeal rates and outcomes (what percentage of appeals succeed? Do any demographic groups appeal more often?).
- Measure: Ensure appeals are successful at a meaningful rate (>30%), indicating they are not just theater.

**Strategy 4: Case Worker Redeployment and Job Security**
- Explicitly commit: no case worker will be laid off due to automation.
- Redeploy to complex case review, applicant follow-up, connection to services beyond benefits (job training, mental health support, housing navigation).
- Provide training on these new roles.
- Track case worker job satisfaction and turnover; ensure meaningful work is available.
- Measure: Retention rate, worker satisfaction scores, quality of follow-up for benefit recipients.

**Strategy 5: Bias Auditing and Correction Pre-Deployment**
- Conduct 6-month pre-deployment disparity impact analysis. Measure approval rates, denials, appeal outcomes by race, ethnicity, national origin, gender, age, disability.
- If disparate impact is found (e.g., 10% lower approval rate for applicants of color), do not deploy until root cause is fixed.
- Establish quarterly ongoing audits during deployment.
- Measure: Disparate impact metrics; model retraining schedule if bias detected.

**Strategy 6: Community Oversight and Governance**
- Establish a multi-stakeholder Benefits Technology Oversight Committee including case workers, applicants or advocates, civil rights organizations, the agency's leadership.
- Meet monthly. Review decisions flagged by applicants or workers as unfair. Discuss trends in appeals and denials by demographic group.
- Give the committee authority to recommend pausing deployment, model retraining, or policy changes.
- Measure: Committee meeting notes, recommendations, implementation tracking.

**Strategy 7: Long-Term Outcome Tracking**
- Track what happens to applicants who receive benefits: Do they exit homelessness? Find employment? How long do they remain on benefits? Are they satisfied with the service?
- Track outcomes for denied applicants: Do they appeal successfully on second or third try? What happens to them (remain in crisis, move away, give up)?
- Use this data to assess whether the AI is actually helping people, not just processing faster.
- Measure: Outcome dashboards; annual outcome reports; use this data to adjust the system.

---

### Section 8 — HOW TO REDUCE HARMS

#### Prevention, Protection, and Support Strategies:

**Prevention — Prevent harms connected with the creation:**

1. **Prevent algorithmic bias through rigorous auditing:** Do not deploy until disparate impact testing is complete. If bias is found, retrain or adjust the model. Commit to quarterly ongoing audits.

2. **Prevent loss of discretion through Option B design:** Ensure human case workers remain final decision-makers and can override AI with documented justification. This is not optional; it is a prerequisite.

3. **Prevent data misuse through governance:** Establish clear policies on data sharing with other agencies. Do not share benefits data with immigration enforcement or law enforcement without explicit legal authority and applicant notice. Encrypt data and implement strong access controls.

4. **Prevent job displacement through commitment:** Commit explicitly that no case workers will be laid off. Establish redeployment plans.

5. **Prevent accountability diffusion through clear responsibility:** Name a specific person or office responsible for algorithmic decisions. Establish that the agency, not the algorithm, is accountable for harms.

**Protection — Protect people from the harms:**

1. **Fast appeals process:** Guarantee human review within 5 business days of appeal. Protect applicants' right to present additional information or contest algorithmic assumptions.

2. **Legal representation:** Offer legal aid or connect applicants to civil rights organizations if they believe they have been wrongfully denied due to discrimination.

3. **Interim support during appeals:** Do not leave denied applicants without resources while appealing. Consider emergency benefits or expedited review for urgent cases.

4. **Data security:** Implement strong cybersecurity controls to prevent breaches. Regular audits, encryption, multi-factor authentication, intrusion detection.

5. **Privacy protections:** Limit data retention (delete applicant data after a set period if case is closed). Restrict who can access applicant data within the agency.

**Support — Support people who may be impacted:**

1. **Applicant support and navigation:** Provide phone/email support to explain decisions, guide appeals, and connect to services. Staffed by people who can actually help, not automated chatbots.

2. **Transparency and accessibility:** Provide decision explanations in plain language, in multiple languages. Make appeals forms available online and offline.

3. **Community engagement:** Hold community meetings in affected neighborhoods to explain the system, collect feedback, and build trust.

4. **Ongoing feedback:** Create channels for applicants to report problems: "I was wrongfully denied," "the system misunderstood my situation," "I need help appealing." Monitor these channels and use feedback to improve the system.

5. **Regular outcome reporting:** Publish quarterly or annual reports on system performance: How many applications received? Approval rates? Appeal rates? Demographic breakdowns? What changes were made in response to feedback?

---

### Section 9 — BOTTOM LINE

#### What changes in your plans will you make?

**Mandatory changes to proceed responsibly:**

1. **Adopt Option B (AI as decision-support, not primary decision-maker):** All final eligibility decisions must be made by human case workers. The AI provides recommendations and reasoning, but case workers can override with documented justification. This is non-negotiable to preserve human autonomy and accountability.

2. **Implement pre-deployment bias audit:** Before any deployment, conduct 6-month disparate impact testing. Do not deploy if disparate impact is found without remediation plan (model retraining, policy adjustment, etc.). Establish quarterly ongoing audits.

3. **Establish robust appeals process:** Guarantee human case worker review within 5 business days. Authorize case workers to override algorithmic recommendations and approve exceptions if justified.

4. **Commit to case worker redeployment:** Guarantee no job losses; redeploy to complex cases and applicant support. Provide training and monitor job satisfaction.

5. **Establish clear accountability:** Name responsible office and individual for algorithmic decisions. Do not allow accountability to diffuse to "the algorithm."

6. **Create multi-stakeholder oversight:** Monthly Benefits Technology Committee including case workers, applicants/advocates, civil rights orgs, leadership. Give them authority to recommend changes.

7. **Implement data governance:** Clear policies on data retention, access, and sharing. Do not share with law enforcement or immigration without explicit authority and applicant notice.

8. **Publish transparent reporting:** Quarterly reports on approval rates, appeal outcomes, demographic breakdowns, and any concerns raised by the Committee. Annual outcome reports on where applicants end up.

**If any of these cannot be committed to, the deployment should not proceed.** The system is too consequential for vulnerable populations to deploy without these safeguards.

**Post-deployment commitments:**

- After 6 months of deployment, conduct full outcome analysis: Are marginalized groups experiencing worse outcomes? Are appeals succeeding? Are case workers satisfied? Adjust as needed.
- After 1 year, decide whether to expand deployment to other benefit types or regions. Do not expand without evidence that the system is working fairly.

---

## Tool 4 — Ethics Gauge

*A systematic assessment across four core ethical dimensions.*

### Dimension 1 — HOW IS IT BENEFICIAL?

**Spectrum 1: Limited benefit to individuals ←→ Great benefit to individuals (more benefit than what already exists)**

Position: **+ (toward great benefit)**

*Assessment:* For applicants with standard cases (estimated 70-85% of applications), the benefit is substantial. Faster approval means faster access to housing, food, or employment support. For someone at risk of homelessness or food insecurity, a 50% reduction in processing time (from 3 weeks to 1 week) translates directly to greater well-being. The existing system is slow; the new system provides meaningful benefit. However, for applicants in edge cases (15-30%), benefit may be neutral or negative, as rigid rules and lack of discretion may result in denial where a case worker would have approved.

**Observation:** Applicants should be faster to access benefits if approved. That is tangible, measurable benefit.

**To move toward the positive end:** 
- Ensure the system is actually faster for the entire pipeline, not just the AI decision. If appeals are slow, the benefit is diluted.
- Measure and publish processing time by case type and demographic group. Ensure speed is equitable.

**What else do we need to investigate:**
- What is the actual processing time reduction for each case type? 
- What percentage of applicants experience faster access? 
- Are there any delays in the appeals process that offset the speed gain?
- For applicants who are denied (correctly or incorrectly), is the time-to-denial plus appeal faster than the existing system?

---

**Spectrum 2: Benefit limited to few select people ←→ Large numbers and multiple groups benefit**

Position: **+ (toward large numbers)**

*Assessment:* The benefit of faster processing applies to all applicants with standard cases. The scope is wide: if the agency processes 10,000 applications per year, and 7,500 are standard cases, then 7,500 people benefit from speed. That is large. However, the benefit is distributed unequally: those in edge cases or with complicated situations benefit much less. Consistency also benefits all, but again, most when you are in a standard case.

**Observation:** The breadth of benefit is large, but the depth varies across groups.

**To move toward the positive end:**
- Explicitly design the system to benefit edge cases too: allocate non-standard cases to human review immediately, rather than attempting to process them algorithmically. This expands benefit to the whole population.
- Track beneficiary numbers by case type and demographic group. Publish.

**What else do we need to investigate:**
- What percentage of applicants are in edge cases or non-standard situations?
- How are benefits distributed across demographic groups? Do certain communities benefit more or less?
- If the system is deployed only for certain benefit types or regions, how many people are reached?

---

**Spectrum 3: Action unlikely to succeed / low likelihood of benefit ←→ Very likely the benefit will be achieved**

Position: **+ (toward very likely)**

*Assessment:* The likelihood of the core benefit (faster processing) is high. Automation typically does reduce processing time; this is well-established. The likelihood is medium-high, not certain, because it depends on:
- The AI system works as designed (no bugs, no crashes, no unexpected delays).
- Downstream processes (appeals, verification, distribution) do not create bottlenecks.
- The agency does not use the speed gain to increase scrutiny or add steps, which could offset the speed.

If all of these are true, benefit is very likely. If any breaks down, benefit may not materialize.

**Observation:** The technical feasibility is high; the organizational feasibility is medium (depends on how well the system is integrated and supported).

**To move toward the positive end:**
- Conduct a thorough process mapping exercise to identify potential bottlenecks downstream.
- Plan for integration carefully: ensure the AI output feeds directly into the decision and distribution pipeline without extra steps.
- Set performance targets (e.g., 80% of cases decided within 5 days) and measure against them.

**What else do we need to investigate:**
- Are there organizational or process barriers that could negate the speed benefit?
- What is the current processing time, and what is the target?
- How will success be measured?
- If the system fails or lags, is there a fallback to manual processing?

---

**Synthesis for Dimension 1 — HOW IS IT BENEFICIAL:**

The system has strong potential for benefit to large numbers of people (standard-case applicants and efficiency beneficiaries). The magnitude of benefit is high for those in crisis (speed means faster relief). The likelihood is high that the technical system will deliver faster processing, though organizational factors could interfere. However, the benefit is not universal: edge cases and vulnerable populations benefit little or may experience harm. The distribution of benefit is unequal. To maximize benefit, the system must be designed to extend benefit to non-standard cases and must ensure that downstream processes (appeals, distribution) remain fast.

---

### Dimension 2 — HOW IS IT HARMFUL?

**Spectrum 1: Great harm to individuals; more harm than alternatives ←→ Limited harm; less than what already exists**

Position: **− (toward great harm)**

*Assessment:* The potential harm is severe, particularly for applicants who are incorrectly denied or who lose the discretionary exception that might have resulted in approval. Denial of housing or food assistance is not a minor harm: it can result in homelessness, malnutrition, family separation, and long-term health consequences. The magnitude of harm per individual is high. Moreover, the potential harm is greater than what already exists in the current (human) system, because humans have discretion to make exceptions and can account for edge cases. Algorithmic systems lack this flexibility. If the new system is more likely to deny edge cases than the old system, it creates new harm that did not exist before.

Moreover, if the system is biased, the harm is not just to individuals but to entire demographic groups, which constitutes systemic harm and injustice.

**Observation:** The harm has high magnitude and is potentially worse than the status quo for vulnerable populations.

**To move toward the positive end (toward limited harm):**
- Implement Option B (human final decision-maker) to preserve discretion for edge cases.
- Establish a robust appeals process so incorrectly denied applicants can be reversed.
- Conduct pre-deployment bias auditing to ensure the system is not systematically denying certain groups.
- If bias is found, retrain the model or adjust policies before deployment.
- Establish a grievance mechanism so applicants who believe they were wrongfully denied can flag it quickly.

**What else do we need to investigate:**
- What is the algorithm's false negative rate (incorrectly denies eligible applicants)? 
- Does the algorithm have lower accuracy for certain demographic groups or case types?
- What is the actual experience of applicants denied by the system? Do they successfully appeal? How long does appeal take? What happens to them during the delay?
- Are there any unintended uses of the system (e.g., leveraging it to deny benefits to politically disfavored groups)?

---

**Spectrum 2: Large numbers / multiple groups are harmed ←→ Harm limited to few people**

Position: **− (toward large numbers)**

*Assessment:* The scope of potential harm is large. If the system is deployed across an entire state or national social services system, and it has even a modest false negative rate (e.g., 3%), that translates to hundreds or thousands of incorrectly denied applicants. If the system is biased, entire demographic groups experience outsized harm. The scope is wide.

However, the harm is not universal. Most applicants (those with standard cases) likely experience no harm; they are simply processed faster. The harm is concentrated among the 15-30% with edge cases or non-standard situations, and disproportionately among marginalized groups if bias is present.

**Observation:** The scope of harm could be large if the system is widely deployed and has significant bias or false negative rate. But it is concentrated among specific groups, not universal.

**To move toward the positive end (limited harm):**
- Identify the high-risk groups (edge cases, specific demographics) and design safeguards specifically for them.
- For edge cases, allocate to human review immediately rather than algorithmic determination.
- For any demographic group showing higher denial rates in audits, investigate and adjust.
- Establish a feedback mechanism so people can report harm. Use this data to understand scope and adjust.

**What else do we need to investigate:**
- What is the current distribution of denials by demographic group in the human system? Use this as a baseline to detect disparate impact.
- If the system is deployed, what percentage of applicants experience harm (incorrectly denied, lost appeal, experienced bias)?
- Which demographic groups experience harm? At what rate?
- How wide is the actual scope if the system is fully deployed?

---

**Spectrum 3: Harm is certain to occur or impossible to prevent ←→ Harm unlikely; potential harm preventable**

Position: **neutral** (harm is likely but preventable)

*Assessment:* Harm is not certain or impossible to prevent. The system could be designed and deployed in ways that minimize harm:
- Option B (human final decision) prevents some harm (rigid algorithmic denial) but not all (bias, speed-induced errors).
- Pre-deployment bias auditing can identify and correct bias.
- Robust appeals processes can prevent harm to specific individuals (though at cost of time and resources).
- Case worker oversight and exception-handling can prevent harm for edge cases.

However, some harms may be difficult to prevent entirely:
- Algorithmic errors are inevitable (no system is 100% accurate).
- Bias in training data may be difficult to fully eliminate.
- Some edge cases will always slip through if the system is not perfectly designed.

The harm is not certain, but it is likely that some harm will occur. The question is whether it is preventable at the systems and policy level.

**Observation:** Significant harm is likely but preventable with robust safeguards. Without safeguards, harm is likely and serious.

**To move toward the positive end (harm unlikely, preventable):**
- Implement all the safeguards listed in the Ethics Frame "How to Reduce Harms" section.
- Treat prevention as an ongoing commitment, not a one-time audit.
- If harm is detected, pause deployment and remediate before continuing.

**What else do we need to investigate:**
- If we implement the safeguards, what is the residual harm? 
- What is the acceptable level of algorithmic error or bias?
- Is there a fallback plan if harm becomes widespread?

---

**Synthesis for Dimension 2 — HOW IS IT HARMFUL:**

The system carries high potential for harm, particularly to vulnerable applicants. The magnitude of harm per individual is severe (denial of housing/food assistance). The scope could be large if deployed widely and without safeguards. However, harm is not inevitable; it is preventable with robust design and governance. The main harm risks are: (1) algorithmic bias leading to disparate impact, (2) rigid rules causing edge cases to be incorrectly denied, (3) false negatives in accuracy, and (4) poor appeals processes that prevent correction. These are all preventable with the right safeguards. But if safeguards are not implemented, harm is likely to be widespread and severe.

---

### Dimension 3 — HOW FAIR IS IT?

**Spectrum 1: Certain people or groups are affected more than others ←→ All people and groups are affected equally (neutral spectrum; neither is inherently better)**

Position: **− (toward "certain people affected more")**

*Assessment:* The impacts are distributed unequally. Applicants with standard cases benefit from speed and consistency. Applicants in edge cases or non-standard situations are harmed by rigid rules and lack of discretion. If bias is present in training data, certain demographic groups experience disproportionate denial rates. Case workers benefit from freed time (if redeployed meaningfully) or are harmed (if displaced). The distribution is decidedly unequal.

This is not inherently wrong — some inequality in impacts may be unavoidable or justifiable. But it should be named explicitly.

**Observation:** The system's impacts are not evenly distributed. Different groups experience different benefits and harms.

**To move toward more equal distribution:**
- Design the system to extend benefits to edge cases (allocate to human review immediately, rather than algorithmic processing).
- Establish appeals and exception processes that are equally accessible to all groups.
- Monitor demographic-specific outcomes and adjust if certain groups are disadvantaged.
- Ensure case worker redeployment is equitable: workers are not laid off, and new roles are accessible to all.

---

**Spectrum 2: Those who are harmed are also less advantaged in society; those who benefit have privilege ←→ No more harm to the less advantaged; those who benefit have greater need**

Position: **− (toward "those harmed are less advantaged")**

*Assessment:* Those most at risk of harm are among the least advantaged: people in poverty, those with unstable housing, recent immigrants, people with criminal histories, those with untreated mental illness or addiction. These are exactly the people who most need and rely on social welfare benefits. Conversely, those who most benefit are also those most likely to have standard situations, good documentation, and familiarity with bureaucracy — which is correlated with higher socioeconomic status and privilege.

This creates a regressive outcome: the system helps the people who already have some advantages and harms those who have none.

**Observation:** The fairness problem is severe. The system risks harming the most vulnerable while benefiting those with greater advantages.

**To move toward the positive end (greater need benefits more):**
- Actively design the system to serve those with greatest need and vulnerability.
- Allocate resources to understanding and serving edge cases and non-standard situations (which disproportionately include vulnerable people).
- Establish exception and appeal mechanisms that are especially accessible to less-advantaged groups.
- Use outcome tracking to monitor whether the system is actually helping the most vulnerable people or harming them.
- If outcome data shows the system is harming vulnerable people disproportionately, pause and redesign.

**What else do we need to investigate:**
- Who are the applicants in edge cases and non-standard situations? What is their demographic and socioeconomic profile?
- Who currently benefits from exceptions and discretion in the human system? Are they more or less advantaged than average?
- If the system removes discretion, who loses it? Are they disproportionately disadvantaged?

---

**Spectrum 3: The burden faced by those most harmed is not acceptable or justifiable ←→ The burden is acceptable or justifiable given the broader context**

Position: **− (toward "burden is not acceptable")**

*Assessment:* The burden of being incorrectly denied access to housing or food assistance is severe and difficult to justify, even in the context of broader efficiency gains. An individual who is denied benefits and ends up homeless cannot accept that burden because it benefits the aggregate system. Fairness requires that systemic harms are not justified by aggregate benefits unless those harmed have consented or have the power to exit the system.

In this case, applicants cannot opt out of the system; if they apply, they are subject to algorithmic determination. Moreover, if they are denied, they face catastrophic harm. That harm cannot be justified by systemic efficiency without strong safeguards and remedies.

**Observation:** The burden on those most harmed is not justifiable without strong safeguards and actual remedies for those wrongfully harmed.

**To move toward the positive end:**
- Implement safeguards that prevent or minimize harm: robust bias auditing, appeals, exception processes, outcome tracking.
- Commit that if harm is detected, it is remedied (people are given the benefits they should have received, appeals are expedited, the system is paused and fixed).
- Involve those who bear the burden (applicants, advocates) in governance and oversight.
- Track outcomes and pause or change deployment if harm is too high.

---

**Synthesis for Dimension 3 — HOW FAIR IS IT:**

The system has significant fairness concerns. Impacts are distributed unequally, with edge cases and vulnerable people at greater risk of harm. Those most at risk of harm are the least advantaged in society, while those most likely to benefit are more advantaged. This is a regressive outcome and is not inherently justifiable. The burden on those harmed is severe (denial of housing/food) and cannot be justified by aggregate system benefits without strong safeguards and remedies. For the system to be fair, it must actively design to serve the most vulnerable, must have robust appeals and exception processes, must track outcomes and adjust if vulnerable people are harmed, and must involve affected communities in governance. Without these, fairness is compromised.

---

### Dimension 4 — HOW EMPOWERING IS IT?

**Spectrum 1: People's ability to make informed choices for themselves is reduced ←→ Ability to make informed choices is unimpaired or increased**

Position: **− (toward reduced ability)**

*Assessment:* Applicants' ability to make informed choices is reduced in several ways:
- The decision is made without their input (unlike human case workers who may ask clarifying questions).
- The reasoning is opaque (unless the system is designed with explainability).
- The appeal process may be unclear or slow, limiting their ability to contest the decision.

However, if the system is designed with transparency (clear reasoning, fast appeals, human override), this can be improved. Option B (human final decision) preserves more informed choice because case workers can explain decisions and applicants can appeal to human judgment.

Case workers' ability to make informed choices is also reduced under Option A (AI as primary decision-maker), because they must either approve the AI recommendation or justify an override, reducing their professional autonomy.

**Observation:** Under Option A, informedness is likely reduced for both applicants and case workers. Under Option B, it can be maintained or improved if transparency and appeal processes are robust.

**To move toward increased informedness:**
- Design for explainability: explain why each decision was made in plain language.
- Ensure appeals are fast and easy to file.
- Ensure case workers have full information about the AI's reasoning and can review and override.
- Provide applicants with support navigating the system (phone support, clear forms, multiple languages).

**What else do we need to investigate:**
- How much of the AI's reasoning can be explained to applicants in plain language?
- Are appeals processes actually fast and accessible?
- Do applicants understand why they were denied or approved?

---

**Spectrum 2: People's control over aspects of their lives is removed ←→ Control is retained or enhanced**

Position: **− (toward control removed)**

*Assessment:* Applicants' control over the decision affecting their lives is removed in the sense that they cannot appeal to human discretion in the same way. The decision is made by algorithm. However, if human case workers retain final decision authority (Option B), control is retained because applicants can appeal to human judgment.

Case workers' control over their work and professional judgment is removed under Option A, because they are expected to approve algorithmic recommendations. Under Option B, control is retained because they can override.

**Observation:** Under Option A, control is reduced for both applicants and case workers. Under Option B, it is retained.

**To move toward control retained/enhanced:**
- Implement Option B: human final decision-makers, with authority to override AI.
- Ensure case workers are supported and encouraged to override when they believe the AI is wrong.
- Ensure applicants can appeal to human judgment and have their appeals taken seriously.

---

**Spectrum 3: There are activities our creation removes the freedom to do ←→ Creation does not coerce, manipulate, or pressure people; limits others' ability to do so**

Position: **neutral** (the system does not inherently coerce or manipulate, but the context of benefits eligibility creates pressure and constraints)

*Assessment:* The AI system itself does not coerce or manipulate applicants. However, the context in which it operates is coercive: applicants must apply and submit to the system's decision or lose access to survival support. There is implicit pressure to accept the system's determination, because the alternative is homelessness or hunger. This is inherent to any means-tested benefits system, not specific to this AI.

The system could coerce or manipulate if:
- Appeals are designed to be difficult (long waits, complex forms), creating pressure to accept the initial decision.
- The system is used to pressure applicants into behaviors (e.g., requiring participation in job training as a condition of approval).
- Data is shared with law enforcement or immigration without consent, creating fear and deterring applications.

The system respects freedom if:
- Appeals are easy and fast.
- Participation in services is genuinely optional.
- Data is protected and not shared without consent.

**Observation:** The system is not inherently coercive, but context and design choices matter. Under Option A with poor appeals, it becomes coercive. Under Option B with robust appeals, it respects autonomy better.

**To move toward freedom:**
- Design appeals to be easy and fast.
- Do not use benefits eligibility as leverage to coerce participation in other services.
- Protect data and do not share without clear legal authority and applicant notice.
- Ensure applicants have genuine choice in what information they disclose (within limits needed for eligibility determination).

---

**Synthesis for Dimension 4 — HOW EMPOWERING IS IT:**

The system reduces autonomy and empowerment for applicants and case workers, particularly under Option A (AI as primary decision-maker). Applicants lose informed choice and control over decisions affecting their lives. Case workers lose professional autonomy and must become algorithm validators. However, these reductions are not inevitable. Under Option B (human final decision) with transparency, appeals, and exception processes, autonomy can be preserved and even enhanced. The key is ensuring that humans remain in the loop and empowered to use their judgment, and that applicants have meaningful ability to contest algorithmic decisions.

---

### Holistic Synthesis: Assessment Across All Four Dimensions

The AI system for benefits eligibility screening presents a profound ethical tension:

**On the positive side:** The system can deliver genuine benefits to large numbers of people (faster access to critical support). If designed well, it can increase consistency and reduce arbitrary human variation. It can free case workers for more meaningful work.

**On the negative side:** The system carries significant risks of harm, particularly to the most vulnerable populations (edge cases, marginalized groups). If biased or rigidly designed, it can systematically deny benefits to people who desperately need them. It concentrates power and decision-making in an algorithm, reducing human autonomy and discretion. It distributes benefits and harms unequally, often along lines of privilege and disadvantage.

**The ethical soundness of this system depends entirely on how it is designed and governed.**

**Option A (AI as primary decision-maker)** is ethically problematic without very strong safeguards. It removes human authority from consequential decisions, concentrates accountability, and increases the risk that harms are scaled and difficult to remedy. The fairness concerns are acute: vulnerable people are most at risk of harm and least able to appeal or contest decisions.

**Option B (AI as decision-support, human final decision)** is more defensible ethically, but still requires substantial safeguards. It preserves human autonomy and accountability but creates new risks: if case workers are pressured to align with AI recommendations, the human override becomes theater rather than meaningful control. If redeployment is not genuine, workers are deskilled and demoralized.

**Critical prerequisites for ethical deployment:**

1. **Pre-deployment bias auditing** that identifies and corrects disparate impact before any deployment. This is non-negotiable.
2. **Robust appeals and exception processes** that allow human judgment to correct algorithmic errors or rigidity.
3. **Genuine case worker empowerment** (Option B structure, training, support to override, no job loss).
4. **Transparent reasoning** so applicants understand why decisions were made.
5. **Ongoing outcome tracking** that measures whether the system is actually helping all groups or harming vulnerable populations.
6. **Meaningful community oversight** that includes affected populations in governance.
7. **Clear accountability** so the agency, not the algorithm, takes responsibility for harms.

**Without these safeguards, the system is unethical and should not be deployed.**

**Even with these safeguards, the system remains ethically complex.** It privileges efficiency and consistency over individualized judgment and relational support. Whether that trade-off is justifiable depends on whether the efficiency gains actually materialize and whether they benefit the people who most need help. That requires empirical evidence, not assumptions.

**Recommendation:** Proceed only under Option B, with all seven safeguards in place, and with a clear commitment to pause or redesign if outcome data shows harm to vulnerable populations.

---

## Tool 5 — Weighing Options

*A structured comparison of two implementation approaches.*

---

### Current Situation

The government social services agency faces pressure to improve benefits eligibility processing. Current state:
- **Status quo challenge:** Manual case worker screening for housing, food, and unemployment benefits creates long delays (average 3-4 weeks from application to initial decision). Backlogs strain staff and leave people in crisis waiting for help. Processing is inconsistent across different workers and regions, leading to variation in outcomes and perceptions of unfairness.
- **Why change:** Delay in accessing benefits causes real human harm: people facing homelessness, food insecurity, and unemployment remain in crisis longer than necessary. Inconsistency creates perception of arbitrariness. Staff are burned out from repetitive work.
- **Opportunity:** AI technology has matured and can automate eligibility screening, reducing processing time and increasing consistency. The agency has resources to pilot deployment.
- **Constraints:** Budget is limited; expanding staff is not an option. The agency is accountable to civil rights law (no disparate impact) and to the public (public trust). Case workers are unionized; workforce reductions are politically and legally difficult.
- **Stakeholder relationships:** Case workers are skeptical of automation and fear job loss. Applicants are demanding faster service. Civil rights organizations and community groups are monitoring for bias and fairness. Elected officials want cost savings and visible improvements in metrics.

---

### Option A: AI as Primary Decision-Maker with Human Appeals

**Option Description**

Deploy an AI system that automatically screens all applications and makes initial eligibility determinations. Applicants who are approved are notified immediately and benefits processing begins. Applicants who are denied receive a decision notice explaining the reason and directing them to appeal to a human case worker. Case workers review appeals on a rolling basis; the target is to complete appeals within 15 business days, but backlogs may cause delays. The AI recommendations are visible to case workers reviewing appeals, but case workers can override if they believe the applicant should be approved.

Case workers are redeployed to appeals review and other tasks (benefit distribution, follow-up with recipients, connection to services). The agency expects to reduce processing time for initial decisions from 3-4 weeks to 3-5 business days for approved applications. The agency expects cost savings of 30-40% in labor costs for screening work.

---

### Option A — Societal Impact: How are people and society affected?

**Benefits:**

1. **Faster approval for eligible applicants with straightforward cases:** 
   - Magnitude: High. Reduction from 3-4 weeks to 3-5 days is significant for someone facing homelessness or food insecurity.
   - Scope: Estimated 70-80% of applications (those with standard income, household size, housing needs).
   - Likelihood: High. The AI will process faster by design.
   - Duration: Enduring. Each person benefits from faster access to ongoing benefits.
   - **Sub-benefit:** Faster access reduces reliance on emergency services (hospitals, shelters, police), saving public money and reducing strain on other systems.

2. **Increased consistency in initial decisions:**
   - Magnitude: Medium to high. People perceive fairness from consistent rules; this builds trust.
   - Scope: Wide. All applicants benefit from the same criteria being applied.
   - Likelihood: High. Algorithms apply rules uniformly.
   - Duration: Enduring.

3. **Cost savings to the agency and public:**
   - Magnitude: Medium. 30-40% labor cost reduction for screening translates to $500K-$1M per year savings (depending on agency size).
   - Scope: Benefit to agency budget; potential for redeployment to expanded services.
   - Likelihood: High.
   - Duration: Enduring, though maintenance costs offset some savings.

4. **Freed case worker capacity for complex cases:**
   - Magnitude: Medium to high. Case workers freed from repetitive work can focus on cases requiring judgment and relationship-building.
   - Scope: Case workers and complex-case applicants.
   - Likelihood: Medium. Depends on organizational commitment to redeployment.
   - Duration: Enduring, if redeployment is sustained.

**Harms:**

1. **Algorithmic bias and disparate impact:**
   - If training data reflects historical discrimination or current bias in case worker decisions, the AI replicates and scales it.
   - Risk: Higher denial rates for applicants of color, immigrants, non-standard family structures, people with criminal histories, those with mental health conditions.
   - Magnitude: Severe. Systematic denial of eligibility to people in desperate need creates homelessness, malnutrition, and long-term harms.
   - Scope: If 5% of applications experience disparate denial impact, and 20,000 applications per year, that is 1,000 people wrongfully denied or approved at lower rates. Across 5 years, 5,000 people experience systemic harm.
   - Likelihood: Medium to high. Historical data in social services contains documented bias; AI amplifies it.
   - Duration: Enduring. Without bias detection and model retraining, harm persists.

2. **Loss of discretionary approval for edge cases:**
   - Applicants who meet the spirit but not the letter of eligibility criteria are automatically denied.
   - Magnitude: High. These are often the most vulnerable people; they have the least resources to appeal successfully.
   - Scope: Estimated 15-30% of applications (recent arrivals, undocumented, non-standard family structures, extreme poverty, mental health crises).
   - Likelihood: Very high. Algorithmic systems lack discretion.
   - Duration: Enduring for each applicant, unless appeals overturn the initial decision.

3. **Incorrect denials and failed appeals:**
   - Even with appeals, some applicants who are incorrectly denied will not successfully appeal due to:
     - Lack of knowledge about how to appeal.
     - Lack of documentation to contest the AI's reasoning.
     - Appeals processing delays.
     - Psychological exhaustion or giving up after denial.
   - Magnitude: High. Denial of benefits is catastrophic harm.
   - Scope: If the AI has 5% false negative rate, and appeals reverse 50% of incorrect denials, then 2.5% of applications remain incorrectly denied. At 20,000 applications per year, 500 people per year remain denied. Across 5 years, 2,500 people.
   - Likelihood: High. No system is 100% accurate; appeals are resource-limited.
   - Duration: Months to years of the applicant remaining in crisis.

4. **Diffused accountability and reduced capacity to fix errors:**
   - When harm occurs, responsibility diffuses: agency claims it was the algorithm; technologists claim they implemented what was requested; case workers say they only reviewed appeals.
   - No clear entity owns the problem, making it difficult for applicants to seek remedy or for the agency to learn from errors.
   - Magnitude: Medium. Accountability diffusion prevents learning and remedy.
   - Scope: All applicants who experience harms; the public.
   - Likelihood: High. Diffusion of responsibility is inherent to algorithmic systems.
   - Duration: Enduring. Without clear accountability, patterns are not corrected.

5. **Loss of relational support and advocacy:**
   - Case workers no longer interact with applicants during initial screening. Applicants experience the system as transactional and uncaring.
   - For vulnerable populations, the loss of a case worker who can advocate for them is significant.
   - Magnitude: Medium to high. Relational support matters to people's trust and sense of being understood.
   - Scope: All applicants, with greatest impact on vulnerable populations.
   - Likelihood: Very high. Automation reduces human interaction.
   - Duration: Enduring.

6. **Risk of case worker displacement (despite redeployment intent):**
   - If redeployment does not materialize (due to budget constraints, union negotiations, organizational culture), case workers may be laid off or reassigned to lower-skill work.
   - Magnitude: High. Job loss is devastating to workers and their families.
   - Scope: Potentially all case workers involved in screening (estimated 20-50 FTE depending on agency size).
   - Likelihood: Medium. Depends on organizational and political commitment to redeployment.
   - Duration: Enduring. Job loss is permanent unless alternative employment available.

7. **Data centralization and privacy risk:**
   - All applicant data in centralized AI system. Risk of breach, misuse, sharing with law enforcement or immigration without consent.
   - Magnitude: Severe. Identity theft, immigration enforcement consequences, exploitation.
   - Scope: All applicants (e.g., 20,000 per year in the system).
   - Likelihood: Medium. Breaches are increasingly common; data sharing within government is routine.
   - Duration: Enduring. Breach consequences can persist for years.

8. **Eroded public trust if high-profile errors occur:**
   - If the system makes visible mistakes (denies a homeless family, denies a veteran, etc.), media coverage and community backlash erode trust in government.
   - Magnitude: Medium to high. Trust is foundational to democratic legitimacy.
   - Scope: Wide. Effects entire public's trust in government.
   - Likelihood: Medium. High-profile algorithmic failures are common.
   - Duration: Enduring. Trust erosion is slow to rebuild.

**Unintended uses and abuse:**
- If data is shared with immigration enforcement, applicants (especially undocumented immigrants) avoid applying, and those most in need do not access support.
- If the system is used as a cost-control mechanism to deny more people (gamed to set thresholds higher), it defeats the stated purpose of helping people.

---

### Option A — Organizational Impact: How might the organization be affected?

**Internal impacts:**

- **Labor cost savings:** 30-40% reduction in screening labor, translating to $500K-$1M+ annual savings. This is significant and demonstrates fiscal responsibility.
- **Redeployment execution risk:** If redeployment of case workers is not well-managed, morale collapses and turnover increases. Institutional knowledge is lost. Organizational culture becomes adversarial.
- **Training and change management:** Significant effort required to train case workers on new roles (appeals review, complex cases, follow-up) and to build trust that their jobs are secure. If this is done poorly, resistance increases.
- **System maintenance and evolution:** Ongoing costs to maintain the AI system, monitor for bias, and retrain models. These costs may offset some labor savings.

**External impacts:**

- **Reputation:** If the system works well and is fair, reputation improves (effective government using technology). If bias is discovered or high-profile errors occur, reputation suffers severely (indifferent government automating away human need).
- **Regulatory compliance:** Risk of civil rights violations if the system has disparate impact. Lawsuits or consent decrees are expensive and damage reputation.
- **Political pressure:** Elected officials will scrutinize the system. If it saves money and improves metrics, political support is high. If it creates public backlash, political support evaporates.
- **Partnership and trust:** Relationships with civil rights organizations, community groups, case worker unions, and advocacy organizations are at risk if the system is perceived as uncaring or biased. Loss of trust makes future collaboration difficult.
- **Competitive positioning:** If the agency successfully deploys a fair, effective system, it becomes a model for other agencies. If it fails, it becomes a cautionary tale.

---

### Option A — Obstacles: What might prevent implementation or success?

**Uncertainty 1: Algorithmic bias is detected or suspected**
- *Scenario:* Pre-deployment audit reveals disparate impact (e.g., applicants of color approved at 10% lower rate than white applicants).
- *Contingency:* Have a clear bias remediation protocol: retrain model with bias correction techniques, adjust decision thresholds, expand training data. Delay deployment until disparate impact is reduced to acceptable levels. If remediation is not successful, pivot to Option B or pause deployment.

**Uncertainty 2: Case worker redeployment does not materialize**
- *Scenario:* Due to budget constraints or union negotiations, the agency cannot redeploy case workers to new roles. Workers are laid off or assigned to undesirable work. Morale collapses; turnover is high.
- *Contingency:* Before deployment, secure labor agreements and budget commitments for redeployment. Involve unions early in planning. If redeployment cannot be committed to, pivot to Option B (human final decisions) to preserve case worker roles. If redeployment is not feasible, delay deployment until resources are available.

**Uncertainty 3: Appeals processing creates new bottleneck**
- *Scenario:* AI reduces initial processing time to 5 days, but appeals pile up because case workers are overwhelmed. Appeals take 20-30 days to process. For denied applicants, the total wait time is not improved.
- *Contingency:* Model the appeals workflow before deployment. Hire additional case workers for appeals review if needed. Set performance targets (e.g., 95% of appeals resolved within 10 days). Monitor appeals metrics; if backlogs grow, escalate. Consider parallel processing (AI decisions and appeals handled simultaneously, not sequentially).

**Uncertainty 4: Data breach or misuse**
- *Scenario:* Centralized database with applicant data is breached. Or data is shared with immigration enforcement without consent.
- *Contingency:* Implement strong cybersecurity controls (encryption, access controls, intrusion detection, regular audits). Establish clear data governance: who can access data, under what circumstances, with what approval. Do not share benefits data with law enforcement or immigration without explicit legal authority and applicant notice. Conduct annual data security audits. If a breach occurs, notify applicants, offer credit monitoring, and implement additional security measures.

**Uncertainty 5: High-profile error damages public trust**
- *Scenario:* Media reports that an elderly veteran or a family of children was denied housing benefits by the algorithm. Public backlash, protests, calls for investigation.
- *Contingency:* Have a rapid response protocol: acknowledge the error publicly, explain what happened, reverse the decision, and commit to preventing similar errors. Use the error as a trigger to audit for systemic problems. Engage community organizations to rebuild trust. Invest in transparency (publish regular reports on system performance, demographic breakdowns, appeals outcomes). If high-profile errors are frequent, pause deployment and redesign.

**Uncertainty 6: Case worker resistance and sabotage**
- *Scenario:* Case workers, fearing job loss or autonomy loss, resist the system. They undermine it (e.g., approving all appeals, ignoring AI recommendations, sharing negative information with media).
- *Contingency:* Involve case workers in system design from the beginning. Be transparent about job security. Frame the system as augmentation, not replacement. Invest in training and support. Establish oversight: monitor appeals decisions to ensure they are reasonable and consistent. If resistance is high, slow deployment and address concerns. If case workers genuinely cannot be won over, reconsider deployment approach.

**Uncertainty 7: Elected officials pressure to increase denial rates for cost savings**
- *Scenario:* Agency leadership, under budget pressure, instructs the system to approve fewer applications to save money (reducing benefits expenditure).
- *Contingency:* Establish clear policy: the system is designed to improve processing efficiency and consistency, not to change eligibility policy. Policy changes (e.g., tighter eligibility) must go through elected officials and the normal policy process, not be hidden in algorithmic decisions. Establish governance: the oversight committee (case workers, advocates, civil rights orgs, leadership) approves any changes to eligibility logic. If pressure to game the system is high, escalate to elected officials and civil society.

---

### Option A — If you choose this option, what are you prioritizing?

**Values prioritized:**
- **Efficiency and speed** over individualized judgment. The system values processing volume and responsiveness to the broader population at the potential cost of some individuals' unique circumstances being overlooked.
- **Consistency** over discretion. Everyone is treated by the same rule, which sounds fair, but may be unfair to those who do not fit the mold.
- **Cost control** over expanded relational support. Labor savings are reinvested elsewhere, not in deeper case worker-applicant relationships.
- **Scalability** over equity. The system can handle growing applicant volumes, but the benefit is distributed unequally (those in standard cases benefit; edge cases are harmed).

**Organizational factors:**
- **Fiscal responsibility and measurable metrics.** The agency prioritizes demonstrated cost savings and faster processing times. These are visible to elected officials and the public.
- **Technology adoption and innovation.** The agency positions itself as forward-thinking and effective.
- **Risk acceptance.** The agency accepts the risk that bias or errors will occur and that some applicants will be harmed, betting that safeguards will catch most problems and appeals will remedy errors.

**Trade-offs accepted:**
- Some eligible applicants (in edge cases or experiencing algorithmic bias) will be denied and must appeal.
- Case workers lose direct interaction with applicants during initial screening, reducing relational support.
- If redeployment does not materialize, case workers experience job insecurity and deskilling.
- Public trust is at risk if high-profile errors occur.
- Applicants experience the system as algorithmic and impersonal, potentially eroding trust in government.

---

### Option B: AI as Decision-Support Tool, Human Final Decisions

**Option Description**

Deploy an AI system that analyzes applications and provides decision recommendations and reasoning to case workers. Case workers receive the AI recommendation but retain full authority to approve or deny each application. Case workers see the key factors driving the AI recommendation (e.g., "Income meets threshold ✓, household size exceeds limit ✗") and can accept the recommendation or override if they believe it is wrong.

The AI reduces case workers' analytical burden by providing consistent eligibility calculations and flagging key decision points. Case workers focus on reviewing the AI analysis, making the final decision, and providing brief documentation if they override the AI. The agency expects to reduce processing time from 3-4 weeks to 7-10 business days by automating analytical work and providing case workers with clear, structured information. (Savings are less than Option A because human review is still required for every case.)

Case workers are fully supported with training, clear documentation of override authority, and performance metrics that measure decision quality (not just speed). The agency expects modest cost savings (10-15% labor reduction from analytics automation), with remaining case workers retained and redeployed to follow-up, complex cases, and applicant support.

---

### Option B — Societal Impact: How are people and society affected?

**Benefits:**

1. **Faster processing with human safeguards:**
   - Magnitude: High. Reduction from 3-4 weeks to 7-10 days is significant and meaningful, especially for people in crisis.
   - Scope: All applicants.
   - Likelihood: High. Automated analytics reduce review time; case workers work more efficiently.
   - Duration: Enduring.

2. **Preservation of human judgment and discretion:**
   - Case workers retain authority to override algorithmic recommendations and approve exceptions for edge cases. An applicant $100 over the income threshold can be approved if the case worker judges it justified.
   - Magnitude: High. Discretion is what allows the system to be fair to those who do not fit standard categories.
   - Scope: Particularly benefits edge cases (15-30% of applications), but benefits everyone because they maintain human recourse.
   - Likelihood: Very high. Human authority is explicit in the design.
   - Duration: Enduring.

3. **Reduced risk of algorithmic bias:**
   - Case workers can recognize bias (if the AI is systematically denying certain demographic groups) and override. The human layer provides a check against algorithmic bias.
   - Magnitude: Medium to high. Bias is not eliminated, but the human layer reduces the risk that bias cascades.
   - Scope: All applicants, particularly vulnerable groups.
   - Likelihood: Medium. Humans can check bias, but may not always notice or act on it. Requires training and awareness.
   - Duration: Enduring, with need for ongoing bias auditing.

4. **Maintained relational support:**
   - Case workers still interact with and review applications. They can provide feedback to applicants on why decisions were made and can offer navigation support.
   - Magnitude: Medium. Relational support matters to people's sense of being understood and valued.
   - Scope: All applicants.
   - Likelihood: High. Case worker involvement is inherent to the design.
   - Duration: Enduring.

5. **Preserved case worker autonomy and job security:**
   - Case workers are not displaced; their role is enhanced with analytical tools, not replaced by algorithms. Job security and professional autonomy are maintained.
   - Magnitude: High for case workers. Autonomy and job security matter to worker well-being and organizational culture.
   - Scope: All case workers in screening roles.
   - Likelihood: High. The design explicitly preserves their role.
   - Duration: Enduring.

6. **Improved consistency with human override:**
   - The AI provides consistent eligibility calculations, reducing case worker inconsistency. But humans can still override for justified reasons, allowing for equity adjustments.
   - Magnitude: Medium. Consistency is good, but balanced with fairness.
   - Scope: All applicants.
   - Likelihood: High.
   - Duration: Enduring.

7. **Reduced cost but not at the expense of people:**
   - Modest cost savings (10-15%) from automation of analytics, without the labor cost reductions of Option A. No case workers are laid off; redeployment is genuine and meaningful.
   - Magnitude: Medium. Cost savings are smaller than Option A but still meaningful.
   - Scope: Benefit to agency budget and public.
   - Likelihood: High.
   - Duration: Enduring.

**Harms:**

1. **Slower processing than Option A:**
   - Processing is faster than the status quo (7-10 days vs. 3-4 weeks), but slower than Option A (7-10 days vs. 3-5 days).
   - For applicants in extreme crisis (hours until eviction), even 7-10 days may feel too slow.
   - Magnitude: Low to medium. The delay is shorter than the status quo, so it is an improvement, but less than Option A.
   - Scope: All applicants, particularly those in extreme crisis.
   - Likelihood: High.
   - Duration: Initial processing delay; benefits mitigate it once approved.

2. **Risk of human bias if case workers are not trained or monitored:**
   - If case workers are not trained to recognize and resist bias, human override authority could become a vector for bias (case workers override AI denials more often for certain demographic groups).
   - Magnitude: High. Allowing human bias to persist is unfair.
   - Scope: Marginalized groups experiencing bias.
   - Likelihood: Medium. Depends on training and monitoring.
   - Duration: Enduring, if not caught and corrected.

3. **Risk that case workers are pressured to align with AI recommendations:**
   - If organizational culture or performance metrics emphasize speed and consistency, case workers may feel pressure to "not waste time" overriding the AI. Override authority becomes nominal, not real.
   - Magnitude: Medium. If case workers do not meaningfully exercise override authority, the system functions like Option A without the transparency or accountability.
   - Scope: All applicants, particularly those who would have benefited from case worker override.
   - Likelihood: Medium. Depends on organizational culture and how override authority is managed.
   - Duration: Enduring, if the culture is not corrected.

4. **Modest cost savings mean less resources for expansion:**
   - While Option B avoids mass job loss, it also generates less cost savings, so there is less money to reinvest in expanded services or improved benefits.
   - Magnitude: Low to medium. Trade-off between job security and service expansion.
   - Scope: Benefit to agency and public (less so than Option A).
   - Likelihood: High.
   - Duration: Enduring.

5. **Data centralization and privacy risk (same as Option A):**
   - All applicant data in centralized AI system. Risk of breach, misuse, sharing with enforcement agencies.
   - Magnitude: Severe.
   - Scope: All applicants.
   - Likelihood: Medium.
   - Duration: Enduring.

---

### Option B — Organizational Impact: How might the organization be affected?

**Internal impacts:**

- **Labor cost savings:** Modest 10-15% reduction in labor cost from analytics automation (fewer hours per case), translating to $150K-$300K annual savings. Less dramatic than Option A but still meaningful.
- **Case worker morale and retention:** If redeployment is genuine and transparent, morale improves. Case workers appreciate that their jobs are secure and that they are valued. Retention is higher. Institutional knowledge is preserved.
- **Change management:** Less dramatic change reduces resistance. Case workers are trained to use the analytics tools and understand that their judgment is still central. Training is focused on how to use the AI, when to override, and how to recognize bias.
- **System maintenance:** Ongoing costs to maintain the AI system and monitor for bias. Costs are similar to Option A but may be lower if the system is less complex.

**External impacts:**

- **Reputation:** If the system works well (faster processing, fair outcomes, maintained human judgment), reputation improves as a government agency that embraced technology thoughtfully. Lower risk of reputational damage than Option A because human judgment is visible.
- **Regulatory compliance:** Lower risk of civil rights violations because human case workers provide a check against algorithmic bias. But civil rights compliance still requires demonstrating that the system (human + AI) does not have disparate impact.
- **Political support:** Political support is dependent on whether the agency can demonstrate that the system is fair and not just cost-cutting. Modest cost savings may not impress elected officials focused on budget cuts, but maintaining jobs may impress labor advocates and community groups.
- **Partnership and trust:** Lower risk of alienating case worker unions, civil rights organizations, and community groups. If they are involved in oversight, trust is maintained.
- **Competitive positioning:** If successful, the model demonstrates that technology can augment human judgment without replacing it. This is attractive to other agencies and the public.

---

### Option B — Obstacles: What might prevent implementation or success?

**Uncertainty 1: Case workers do not meaningfully exercise override authority**
- *Scenario:* Despite official authority to override, case workers feel pressured by speed metrics and organizational culture to approve the AI recommendation without real review. Override authority is nominal.
- *Contingency:* Explicitly measure override rate and override reasoning. If override rate is very low (<5%), investigate: are case workers appropriately exercising authority, or are they rubber-stamping? Retrain if needed. Adjust performance metrics to reward decision quality, not just speed. Hold managers accountable for ensuring case workers understand they have authority to override.

**Uncertainty 2: Case workers introduce their own bias**
- *Scenario:* Case workers, given override authority, systematically override AI decisions in biased ways (e.g., approving white applicants' appeals at higher rates than applicants of color).
- *Contingency:* Monitor override decisions by demographic group. If bias is detected, investigate and retrain case workers. Provide case workers with bias training and resources to recognize and resist bias. Use audits to catch patterns. If case worker bias is systemic, address organizational culture.

**Uncertainty 3: Modest cost savings disappoint elected officials**
- *Scenario:* Elected officials expecting Option A's large cost savings (30-40%) are disappointed with Option B's modest savings (10-15%). Political pressure to cut deeper or reconsider the approach.
- *Contingency:* Frame the savings accurately and highlight the co-benefits: maintained jobs, preserved human judgment, lower legal risk. Make the case that the balance of efficiency and fairness is the right one. Demonstrate outcomes (e.g., faster processing, higher applicant satisfaction, lower appeals rate) to show the system is working. If cost savings are genuinely the priority, acknowledge that Option A would save more but would accept higher risk to vulnerable populations.

**Uncertainty 4: Processing time is not improved as much as expected**
- *Scenario:* Implementation reveals that even with AI analytics, case workers still need significant time to review each application. Processing time is 10-14 days instead of the expected 7-10 days.
- *Contingency:* Model the workflow in detail before deployment. Identify bottlenecks. If case worker review time is high, consider: are case workers spending time on cases that could be streamlined? Can the AI provide more complete analysis? Can case workers be trained to review faster? Adjust targets and communication to match realistic processing time.

**Uncertainty 5: Applicants do not understand that humans are making the final decision**
- *Scenario:* Applicants assume the system is fully automated and do not know they can request case worker review or appeal to human judgment.
- *Contingency:* Clearly communicate to applicants that humans are making the final decision and that they have recourse if they disagree. Provide decision notices that explain: "This decision was made by a case worker using AI analysis. If you disagree, you can appeal to request case worker review." Make appeals process clear and easy.

**Uncertainty 6: System complexity is high; case workers are confused**
- *Scenario:* The AI system is complex; case workers struggle to understand the reasoning and feel overwhelmed. Review quality suffers.
- *Contingency:* Invest in user-centered design and training. The AI system should provide clear, plain-language summaries of the analysis, not raw algorithm scores. Train case workers thoroughly. Provide job aids and support. If case workers cannot use the system effectively, simplify or redesign.

---

### Option B — If you choose this option, what are you prioritizing?

**Values prioritized:**
- **Fairness and individualized judgment** over pure efficiency. The system prioritizes case-by-case assessment and human discretion, even if it means slightly longer processing times.
- **Dignity and human autonomy** (for both applicants and case workers). Case workers are treated as professionals whose judgment matters; applicants are treated as people with unique circumstances worthy of consideration.
- **Accountability and transparency.** Because humans are visibly involved, accountability is clearer. Applicants know who made the decision and can appeal to human judgment.
- **Job security and organizational culture.** The agency prioritizes maintaining its workforce and culture over maximizing cost savings.

**Organizational factors:**
- **Balanced performance metrics.** The agency measures both speed and quality, decision fairness (demographic breakdowns, appeals success rates), and case worker job satisfaction.
- **Risk mitigation.** The agency accepts that cost savings will be modest but benefits from reduced legal and reputational risk.
- **Thoughtful technology adoption.** The agency positions itself as embracing technology where it genuinely helps, while preserving what is valuable about human judgment.

**Trade-offs accepted:**
- Smaller cost savings than Option A (10-15% vs. 30-40%). Some efficiency is sacrificed for fairness and job security.
- Processing time is slower than Option A (7-10 days vs. 3-5 days), though faster than status quo.
- Ongoing need to monitor that case workers are meaningfully exercising override authority and not introducing bias.
- Greater complexity (human + AI system) than pure human or pure AI systems.

---

## Future Direction: Which Option Will You Pursue, and Why?

### Recommendation: Proceed with **Option B**, with strong caveats.

**Rationale:**

**Option A's risks are too high.** While it delivers cost savings and faster processing for the majority, it concentrates consequential power in an algorithm and removes the human layer that can check bias and account for edge cases. The potential harms — systematic denial of eligible applicants due to bias, rigid rules harming vulnerable populations, diffused accountability — are profound and difficult to remedy once deployed at scale. The fairness concerns are acute: the system is likely to harm the most vulnerable while benefiting those with straightforward cases. Once biased decisions are made and scaled, correcting them is slow and incomplete. The reputational and legal risks are substantial.

Option A might be justified if: (1) the pre-deployment bias audit conclusively shows no disparate impact and case worker bias has been historical, (2) robust appeals processes are guaranteed, (3) case worker redeployment is solidly committed and funded, and (4) the agency has demonstrated capacity to manage algorithmic systems responsibly. **If any of these conditions cannot be met, Option A should not proceed.**

**Option B is more defensible** because it preserves the human judgment and oversight that can catch and correct algorithmic errors and bias. Case workers remain decision-makers and can override the AI when they believe it is wrong. This preserves fairness for edge cases. It also preserves job security and organizational trust, which are valuable goods in their own right. The trade-off is smaller cost savings and slower processing than Option A. But the processing time (7-10 days vs. 3-4 weeks) is still a meaningful improvement for people in crisis. And the modest cost savings (10-15%) still provide resources for expanded or improved services.

**However, Option B is not sufficient without strong safeguards:**

1. **Pre-deployment bias auditing:** Before any deployment, conduct 6-month disparate impact testing. Do not deploy if significant disparate impact is found.

2. **Case worker empowerment and monitoring:** Train case workers explicitly that they have authority to override the AI and that overriding is encouraged when they believe the AI is wrong. Monitor override rates and reasoning; if override rate is very low or biased, investigate and retrain. Adjust performance metrics to reward decision quality and fairness, not just speed.

3. **Robust appeals process:** Guarantee human case worker review within 5 business days of appeal. Publish quarterly appeals data: how many appeals, what percentage are approved, demographic breakdowns.

4. **Data governance and privacy:** Clear policies on data retention, access, and sharing. Do not share benefits data with law enforcement or immigration without explicit legal authority and applicant notice.

5. **Community oversight:** Multi-stakeholder Benefits Technology Committee (case workers, applicants/advocates, civil rights orgs, leadership) meets monthly to review concerns, audit outcomes, and recommend changes. Give them authority to recommend pausing or redesigning if harms are detected.

6. **Transparent outcome reporting:** Quarterly reports on system performance (processing time, approval rates, appeals outcomes) by demographic group. Annual outcome reports on where applicants end up (did they exit homelessness? Find employment?). Use this data to adjust the system.

7. **Clear accountability:** Name a specific person or office accountable for algorithmic decisions and their harms. Do not allow accountability to diffuse.

**Post-deployment decision points:**

- **At 6 months:** Conduct full outcome analysis. Are marginalized groups experiencing worse outcomes (higher denial rates, lower appeal success rates)? Are case workers satisfied? If significant harms are detected, pause and redesign.

- **At 1 year:** Decide whether to expand deployment to other benefit types or regions. Do not expand without evidence that the system is working fairly for all populations.

- **If at any point significant bias or harm is detected:** Pause deployment immediately. Investigate root cause. Retrain or redesign. Do not proceed until disparate impact is remediated.

---

### If you cannot commit to these safeguards, do not proceed with deployment.

The system is too consequential for vulnerable populations to deploy without robust oversight and accountability. Faster processing and cost savings are not worth the risk of systematically harming the people who most depend on government support.

---

### What else do you need to learn or do before deciding?

Before final deployment, the following research and planning is needed:

1. **Detailed process mapping:** Map the entire end-to-end workflow (application receipt → AI analysis → case worker review → decision → appeal → distribution). Identify bottlenecks and timeline.

2. **Pre-deployment bias audit:** Train a pilot model on historical data. Test for disparate impact (approval rates, denial rates, appeal outcomes by race, ethnicity, national origin, gender, age, disability). If disparate impact is found, conduct root cause analysis and remediation.

3. **Vendor and technical assessment:** If procuring AI system from vendor, assess: How is the model trained and validated? What safeguards against bias are built in? How is the model monitored post-deployment? What is the SLA for issues and updates?

4. **Case worker stakeholder engagement:** Hold focus groups and interviews with case workers to understand: What are their concerns? What would make them trust the system? What support do they need? What would convince them to meaningfully use override authority?

5. **Community engagement:** Hold focus groups and interviews with applicants, community organizations, civil rights groups. Understand: What are their concerns about automation? What would build trust? How should the system be designed to be fair?

6. **Labor and organizational planning:** Work with case worker unions and leadership to plan redeployment explicitly. Where will case workers go? What training will they receive? When do jobs start? How will success be measured? Get written commitments before deployment.

7. **Legal review:** Assess the system for civil rights compliance (Title VI, Section 504, other applicable laws). What is the legal standard for disparate impact? How will the agency demonstrate compliance?

8. **Governance structure:** Establish the oversight committee and operational procedures before deployment. Who has authority to recommend pausing? How quickly can the agency respond to recommendations?

Once this research is complete and shows that Option B can be implemented safely and fairly, proceed. If any research raises red flags (high disparate impact, case workers will not be trained, community opposition is high), pause and address the issues before deployment.

---

## Values Prioritized Across the Chain

Across all five tools, the following values emerged as most significant:

**Justice** — The central ethical tension is whether the system will distribute benefits and harms fairly across all communities, or whether it will harm the most vulnerable while benefiting the privileged. This is fundamentally a justice issue: fairness in the distribution of access to survival resources.

**Dignity** — Whether the system treats people as individual human beings with unique circumstances or as data points to be processed. Algorithmic systems risk reducing dignity by treating people uniformly rather than recognizing their inherent worth and individual context.

**Autonomy** — Both for applicants (ability to make informed choices and have recourse to human judgment) and for case workers (professional autonomy to use judgment). The choice between Option A and Option B pivots on whether autonomy is preserved.

**Responsibility** — Who is accountable for algorithmic decisions and for harms? Diffused accountability (blaming the algorithm) vs. clear institutional accountability is a critical ethical question. The agency must take responsibility.

**Trust** — Public confidence in government institutions depends on whether the system is perceived as fair, transparent, and accountable. High-profile errors or visible bias erode trust. Long-term legitimacy of government depends on maintaining trust.

**Well-being** — The system aims to improve well-being (faster access to benefits) but risks harming well-being (incorrect denials, loss of relational support, psychological harm from algorithmic judgment).

**Relationships** — The relational support and human connection that case workers historically provided is valuable and at risk of being lost. Preserving or restoring relationships is an ethical good.

### Trade-offs Made:

- **Efficiency vs. Equity:** The system prioritizes processing speed but accepts that some efficiency gains are lost if it means preserving fairness. Option B trades some speed for equity.
  
- **Cost Savings vs. Job Security:** The system accepts modest cost savings (10-15% in Option B) rather than maximum savings (30-40% in Option A) to preserve case worker jobs and morale.

- **Consistency vs. Discretion:** The system accepts that perfect consistency (everyone treated by the same rule) may be unfair to those who do not fit standard categories. Case worker discretion is preserved to allow fairness.

- **Scale and Speed vs. Human Judgment:** The system acknowledges that scaling human judgment is slow, but it is fairer than replacing it with algorithms. Speed is improved (7-10 days vs. 3-4 weeks) but not maximized (would be 3-5 days with Option A).

### Values that had to be constrained or de-prioritized:

- **Fiscal efficiency:** Maximum cost savings are not achieved in favor of fairness and job security.
- **Scalability:** The system cannot grow infinitely fast without human review, in favor of fairness and accountability.

### Conclusion:

The ethical assessment shows that deploying an AI system for benefits eligibility screening is possible, but only with careful design, robust safeguards, and genuine commitment to fairness and accountability. The system must remain a tool that augments human judgment (Option B), not a replacement for it (Option A). It must be continuously audited for bias, overseen by multi-stakeholder governance, and paused or redesigned if harms emerge. Values of justice, dignity, autonomy, responsibility, and trust must be actively protected. Proceeding without these safeguards would be unethical and harmful to vulnerable populations.

---

## End of Assessment

**Chain Status:** All five tools completed. Future Story ✓ | Impacts Explorer ✓ | Ethics Frame ✓ | Ethics Gauge ✓ | Weighing Options ✓

This assessment provides a comprehensive ethical evaluation of AI deployment in government social services. The findings and recommendations are grounded in rigorous analysis of benefits, harms, fairness, autonomy, and accountability. The recommendation is to proceed with **Option B (AI as decision-support, human final decisions)** with strong safeguards, or not to proceed at all.

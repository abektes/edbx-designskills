# STF-ET Ethics Assessment: AI System for Welfare Benefits Eligibility Screening

**Chain Status:** Future Story ✓ | Impacts Explorer ✓ | Ethics Frame ✓ | Ethics Gauge ✓ | Weighing Options ✓  
**Entry Phase:** Explore → Evaluate → Decide (Full chain for comparative decision-making)  
**Assessment Date:** 2026-05-06  
**Options Analyzed:** 2 (Option A: AI as primary decision-maker | Option B: AI as decision-support only)

---

## Tool 1 — Future Story

This narrative looks back from a future where the welfare benefits AI system has been deployed and used at scale for 2-3 years. We examine both intended and unintended consequences.

### PROBLEM / MOTIVATION

**Once upon a time …**

Government agencies struggled with processing welfare benefit applications. Case workers were overwhelmed with paperwork, eligibility screening took weeks or months, and geographic inconsistencies meant similarly situated people received different treatment. Long processing times left vulnerable populations—people experiencing homelessness, families in crisis, unemployed workers—waiting without support. Agencies wanted to reduce administrative burden, accelerate decisions, and ensure consistent application of eligibility rules across regions and case workers.

### SOLUTION / VALUE PROP

**Until one day …**

The government built an AI system to automatically screen applications for housing assistance, food support, and unemployment benefits. It would ingest applicant data, extract relevant information from documents, cross-reference government records, and produce an initial eligibility recommendation. For Option A (discussed in Weighing Options), the AI makes the primary decision with a manual appeals process; for Option B, the AI flags cases and provides supporting analysis, but human case workers make all final decisions.

### BENEFITS

**And because of that …**

Processing times dropped dramatically—from 60+ days to 3-5 days. Applicants received decisions faster and could access support sooner. Case workers were freed from repetitive data-entry and document-review tasks, allowing them to focus on complex cases, provide client counseling, and exercise professional judgment. The system flagged edge cases and inconsistencies, improving overall decision quality. Rural and underserved regions with fewer case workers gained access to faster processing. Eligible people received benefits they needed, reducing immediate hardship for vulnerable populations. The system's consistency meant similarly situated applicants had similar outcomes regardless of geography or which case worker reviewed their file.

### HARMS

**But also …**

The system's training data came from historical eligibility decisions, which embedded decades of bias and inconsistent practices. Applicants from communities that had historically faced discrimination in benefits administration were more likely to be incorrectly flagged as ineligible. People without stable addresses, proper documentation, or digital literacy struggled to provide the data the system expected. The system sometimes misclassified income types or failed to account for non-monetary resources. Once the AI's recommendation appeared in official records, applicants and case workers alike were psychologically anchored to it—appeals were less common, even when warranted. Applicants did not understand how their eligibility was determined and could not meaningfully contest specific algorithmic determinations. The system operated as a black box; even case workers couldn't articulate why it made certain recommendations. Low-income applicants, especially non-English speakers and people with disabilities, bore the brunt of application errors because they had fewer resources to navigate appeals or hire advocates.

### SUBSEQUENT IMPACTS

**In turn …**

The system's speed became a liability. Agencies began to see the AI as a reliable replacement rather than a tool, and staffing was cut. When errors were discovered, there were fewer experienced case workers to catch and correct them. Trust in the agency eroded among communities that experienced disproportionate denials. Some eligible applicants gave up on appeals because the process was opaque and felt hopeless. Economic hardship deepened for people wrongly denied benefits.

**In turn …**

The system's consistent but biased decisions began to shape funding allocations across regions. Agencies reported lower eligibility rates in historically marginalized neighborhoods, leading budget analysts to conclude that fewer people in those areas needed assistance. Resources were shifted away, deepening geographic inequality. The system had become self-reinforcing—initial bias led to biased outcomes, which produced data that justified continued bias.

**In turn …**

Privacy and data security issues emerged. The system collected and cross-referenced sensitive personal information from tax records, medical files, housing history, and other agencies. Applicants had no clear understanding of how their data was used or stored. Data breaches exposed applicant information. People began to avoid applying for benefits they were eligible for, fearing exposure or misuse of their information. Mistrust spread to the government agencies themselves, with downstream effects on public health and welfare programs.

### MITIGATING ACTIONS

**One thing we could have done differently is …**

Before deploying the system at scale, the agencies should have:

1. **Audited training data for bias** and retrained models on data that reflected correct historical decisions, not biased ones. Tested the system extensively on underrepresented communities and measured performance disparities.

2. **Implemented transparency requirements**: applicants must receive clear, understandable explanations of how eligibility was determined and what factors were considered. Case workers and applicants alike must be able to access and contest specific algorithmic determinations.

3. **Ensured human oversight remained real**: case workers should retain final decision-making authority; the system assists but does not replace judgment. Processes must prevent automation bias—the tendency to defer to automated recommendations without genuine review.

4. **Protected privacy and consent**: applicants must explicitly consent to data sharing across agencies. Data should be minimized (collect only what is necessary), and secure storage and deletion protocols must be established.

5. **Monitored ongoing fairness**: deployed systems must track outcomes by demographic group, identify emerging disparities, and trigger human review before harms scale. Independent auditing should be required.

6. **Invested in appeals and remediation**: provide free advocacy and streamlined appeals for anyone who contests a decision. When errors are found, proactively contact affected applicants and correct benefits.

---

→ Carries forward to Tool 2 (Impacts Explorer):

- **Action/Creation:** Automated AI system that screens welfare benefit applications (housing, food, unemployment) and recommends or determines eligibility.
- **Direct effects seeding Effects ring:** Faster processing times; reduced administrative burden on case workers; applicants receive decisions sooner; system misclassifies some applicants due to biased training data; applicants without stable documentation or digital literacy struggle; applicants don't understand how decisions are made; appeals become less common despite warranting.
- **Cascading impacts seeding Secondary Effects ring:** Staffing cuts due to AI replacing workers; erosion of agency trust in affected communities; eligible applicants give up on appeals; geographic inequality deepens as biased outcomes shape funding; privacy breaches; people avoid applying for benefits they need; automation bias prevents real human review.
- **Values touched:** Well-being (eligible people get support faster, but ineligible denials create hardship); Justice (system embeds and amplifies historical bias); Trust (opaque system and errors erode confidence); Privacy (sensitive data collected and exposed); Dignity (people treated as data profiles, not individuals; no meaningful voice in decisions); Autonomy (applicants cannot understand or contest decisions); Responsibility (agencies cannot account for how decisions were made).

---

## Tool 2 — Impacts Explorer

### Center Node
**Automated AI system for welfare benefits eligibility screening** — technology deployed to determine or recommend initial eligibility for government assistance programs (housing, food support, unemployment).

### Direction: In-to-Out (from action outward)

### Direct Effects (First Ring)

#### On Applicants:
- **Faster processing:** Benefit decisions within days instead of weeks/months
- **Reduced documentation burden:** System may accept digital submissions rather than in-person forms
- **Inconsistent outcomes:** Some applicants screened incorrectly due to training data bias
- **Reduced transparency:** Applicants don't understand why they were accepted or denied
- **Automation bias in appeals:** Applicants less likely to appeal when AI recommendation is presented as official

#### On Case Workers:
- **Reduced administrative load:** Freed from repetitive data entry and document review
- **Shifted work:** Move toward complex case management and client support
- **Loss of professional judgment:** System removes space for case worker discretion in close calls
- **Deskilling or layoffs:** Fewer positions needed if system handles initial screening

#### On Agencies:
- **Faster throughput:** More applications processed in same time period
- **Consistency in output:** Similar cases treated similarly (but if bias exists, consistently biased)
- **Reduced staffing needs:** Fewer case workers required for initial screening
- **New liability:** Errors now scale to thousands of people; opaque decision-making invites legal challenges

### Secondary Effects (Second Ring)

#### From "Faster processing":
- Eligible applicants access housing, food, income support sooner → improved short-term survival and well-being
- Agencies close cases faster → budgetary relief, but also reduced engagement with vulnerable populations
- Perception of government efficiency improves → increased trust (initially), but vulnerable communities may be skeptical
- Demand for benefits support services (shelters, food banks) may decrease as people receive government support faster

#### From "Applicants don't understand decisions":
- Applicants cannot meaningfully contest decisions they believe are wrong → more ineligible denials stick
- Case workers cannot articulate their reasoning to applicants → trust erodes
- Agencies cannot learn what's working and what isn't → continuous improvement stalls
- Vulnerable applicants (non-English speakers, people with disabilities) face compounded barriers → systematic exclusion

#### From "Reduced administrative burden on case workers":
- Case workers have time for complex cases → better outcomes for people with complicated eligibility
- Demoralization if perceived as being replaced → staff departures, lost institutional knowledge
- Reallocation of staff to other agency functions → benefits from full spectrum services
- Or: staff cuts to reduce budget → remaining staff overloaded, quality declines

#### From "System inconsistent due to bias in training data":
- People from historically marginalized communities more likely to be denied → entrenched inequality
- Agencies report lower eligibility in certain neighborhoods → funding gets reallocated away from highest-need areas
- Denied applicants avoid re-applying → self-selection bias deepens in who gets served
- Civil rights complaints emerge → legal liability and reputational damage

#### From "Privacy/data exposure":
- Sensitive applicant data (financial, medical, housing history) crosses agencies → new privacy risks
- Data breach exposes personal information → identity theft, loss of trust
- People in unstable situations afraid to apply → lose access to benefits they qualify for
- Chilling effect: vulnerable people withdraw from government assistance entirely

#### From "Automation bias":
- Case workers defer to system recommendations without real review → errors propagate
- Appeals process becomes pro forma → legitimate appeals denied
- People with resources (able to hire lawyers) succeed on appeal; those without lose → inequality in outcomes

### Values Impacted

| Value | Impact | How |
|-------|--------|-----|
| **Well-being** | Mixed, conditional | Benefits eligible people quickly (promoting), but denies eligible people wrongly due to bias (degrading). Geographic and demographic disparities mean some populations' well-being improves while others' worsens. |
| **Justice** | Degrading | System embeds and amplifies historical bias. Benefits and burdens distributed unequally by race, income, geography, immigration status. Those already marginalized face disproportionate harms. |
| **Trust** | Degrading | Opaque system erodes trust in agencies. Errors and bias become visible, confirming historical distrust of government. Communities withdraw from engaging with assistance programs. |
| **Privacy** | Degrading | Sensitive data collected and shared across agencies. Applicants have minimal control over what information is gathered and used. Privacy breaches expose vulnerability. |
| **Dignity** | Degrading | Applicants treated as data profiles rather than full human beings. No meaningful voice in decisions affecting their lives. System applies bureaucratic logic without accounting for individual circumstances and human dignity. |
| **Autonomy** | Degrading | People cannot understand or contest how their eligibility was determined. System removes human judgment and applicant voice. Appeals process feels hopeless. People's ability to make informed choices about engaging with the program is undermined. |
| **Responsibility** | Degrading | Agencies cannot articulate how decisions were made or why. Responsibility for errors is diffused ("the system decided"). Accountability mechanisms are weak. |
| **Relationships** | Degrading | Case workers' relationships with applicants become transactional rather than supportive. System removes opportunities for human connection and understanding. Applicants feel systems treat them impersonally. |
| **Virtues** | Degrading | Case workers lose opportunities to exercise judgment and compassion. System discourages virtues of understanding and empathy. Bureaucratic efficiency replaces care. |

### Stakeholder Groups and Differential Impacts

**Group 1: Eligible applicants with stable documentation and digital literacy**
- Benefit most: faster access to benefits, reduced bureaucracy
- Minimal harm: can navigate appeals if needed, understand system basics
- Net effect: strongly positive

**Group 2: Eligible applicants from marginalized communities, without stable documentation, non-English speakers, people with disabilities**
- Face highest harm: more likely to be misclassified due to training data bias, cannot navigate appeals, don't understand system
- Receive fewer benefits relative to need
- Net effect: strongly negative; existing vulnerabilities amplified

**Group 3: Case workers**
- Benefit: freed from repetitive work, potentially better job satisfaction (if not laid off)
- Harm: deskilled, potentially unemployed, lose professional autonomy
- Net effect: depends on organizational response (redeployment vs. layoffs); likely mixed to negative

**Group 4: Government agencies**
- Benefit: faster processing, reduced admin costs, appearance of efficiency
- Harm: legal liability from errors and bias, loss of public trust, inability to serve highest-need populations well
- Net effect: short-term positive, long-term negative if harms accumulate

**Group 5: Society**
- Benefit: more efficient welfare system, potentially serving more people
- Harm: entrenched inequality, reduced social cohesion, loss of public trust in government
- Net effect: negative if bias perpetuates; positive only if system is rigorously fair

### Fairness Patterns

- **Distributional inequity:** Benefits and harms are not equally distributed. Privileged populations with stable documents and resources benefit; marginalized populations bear disproportionate harms.
- **Bias amplification:** System converts historical bias into ongoing algorithmic bias, which then shapes future policy and resource allocation.
- **Accessibility disparities:** People with fewer resources and less digital literacy face compounded barriers.
- **Remediation imbalance:** People with legal resources can contest errors; those without cannot, leading to permanent inequality in outcomes.

---

→ Carries forward to Tool 3 (Ethics Frame):

- **Action/Creation:** Automated AI system determining or recommending initial eligibility for government welfare benefits (housing, food support, unemployment).
- **Benefits seeding Ethics Frame Section 3:** Applicants receive decisions within days instead of weeks; eligible people access support sooner; case workers freed from administrative tasks to focus on complex cases; geographic and regional inconsistencies reduced; system consistency improves certainty for applicants in what to expect.
- **Harms seeding Ethics Frame Section 4:** Ineligible denials increase due to biased training data; applicants without stable documentation face systematic exclusion; applicants don't understand decisions and can't contest them meaningfully; appeals become less common; case workers lose professional discretion; privacy/data security risks; automation bias prevents genuine human review; trust in agencies erodes in affected communities; eligible people avoid reapplying if wrongly denied once.
- **Values identified:** Well-being (mixed: benefits some, harms others based on demographic); Justice (degraded: bias and unequal distribution); Trust (degraded: opaque system, errors); Privacy (degraded: data exposure); Dignity (degraded: people treated as data); Autonomy (degraded: no voice in decisions); Responsibility (degraded: unaccountable system); Relationships (degraded: transactional instead of supportive); Virtues (degraded: removed opportunities for judgment and compassion).
- **Stakeholder groups and differential impacts:** Group 1 (documented, digitally literate, privileged): strong benefit | Group 2 (marginalized, undocumented, disabled, non-English speakers): strong harm | Group 3 (case workers): mixed (freed from admin, potentially unemployed) | Group 4 (agencies): short-term benefit, long-term liability | Group 5 (society): net negative if bias perpetuates.
- **Fairness patterns to flag in Section 5:** Bias-amplifying design; unequal harms concentrated on already-marginalized groups; remediation barriers for those without legal resources; geographic inequality deepening via biased outcome data.

---

## Tool 3 — Ethics Frame

### Section 1 — ACTION / CREATION

**Automated AI system for initial eligibility screening in government welfare benefits programs.** The system processes applications for housing assistance, food support, and unemployment benefits. It extracts information from submitted documents, cross-references government records, and produces either an eligibility recommendation (Option B: human case worker makes final decision) or a binding initial decision (Option A: automated unless appealed). The system is deployed agency-wide and used at scale across thousands of applicants monthly.

### Section 2 — VALUES (Part One: Explore the values that matter)

#### Values driving this work:
- **Efficiency:** Reduce administrative burden and accelerate decision-making
- **Consistency:** Apply eligibility rules uniformly across regions and case workers
- **Access:** Serve more people faster with limited government resources
- **Fairness:** Ensure that eligible people receive support regardless of geographic location or case worker bias

#### Values that may be impacted:
- **Justice:** How benefits and burdens are distributed; whether marginalized groups face disproportionate harms
- **Trust:** Whether agencies act with competence and goodwill in applicants' interests
- **Autonomy:** Whether applicants retain meaningful voice in decisions affecting their lives
- **Dignity:** Whether people are treated as full human beings or reduced to data profiles
- **Well-being:** Whether the system helps or harms physical and mental health of applicants
- **Responsibility:** Whether agencies can account for decisions and take meaningful action when errors occur
- **Relationships:** Whether case workers maintain supportive human connections or become distant administrators

#### How actions influence these values:

The system's pursuit of efficiency and consistency can reinforce or undermine fairness and autonomy depending on design and implementation.

**Reinforced values:**
- Efficiency and consistency are achieved: processes accelerate, similar cases treated alike
- Well-being improves for eligible applicants who receive support faster
- Trust may initially increase: faster decisions perceived as better service

**Undermined values:**
- Autonomy is degraded: applicants cannot understand or contest decisions; system removes human judgment
- Justice is degraded: if training data contains bias, the system embeds and amplifies it, harming already-marginalized groups
- Trust may erode: once errors and bias become visible, communities lose confidence
- Dignity is degraded: applicants treated as data profiles, not individuals with unique circumstances
- Responsibility is degraded: agencies cannot articulate how decisions were made or accept accountability
- Relationships are degraded: human connection replaced by transactional processing

### Section 3 — BENEFITS

#### Direct benefits to individuals:
- **Faster access to support:** Eligible applicants receive housing, food, or income support within days rather than months. This improves immediate survival and well-being, especially for people in crisis.
- **Reduced hassle:** Fewer visits to offices, less paperwork for applicants to manage.
- **Consistency across regions:** An applicant in a rural area has the same chance of eligibility as someone in an urban area (assuming system is unbiased; if biased, this consistency is harmful).

#### Extent dimensions:
- **Magnitude:** High for eligible applicants. Receiving benefits weeks sooner can mean the difference between homelessness and stable housing, hunger and food security, eviction and remaining housed.
- **Scope:** Applies to all welfare applicants (potentially thousands to hundreds of thousands per year per agency), though most benefit is concentrated among eligible applicants.
- **Likelihood:** High that eligible applicants receive support faster; system achieves this reliably.
- **Duration:** Enduring; reduces processing time for as long as system is in operation.

#### Societal benefits:
- **Administrative efficiency:** Frees case workers to handle complex cases and provide better client support.
- **Public perception:** Government appears more modern and responsive.
- **Broader service:** Same staff can potentially serve more applicants with the time saved.
- **Reduced suffering:** More people access benefits sooner; less homelessness, food insecurity, and economic hardship in the short term.

### Section 4 — HARMS

#### Direct harms:
- **Ineligible denials due to bias:** Training data reflects historical biases in eligibility decisions. System reproduces and amplifies these biases. Applicants from marginalized communities are more likely to be misclassified as ineligible and wrongly denied benefits they qualify for.
- **Inaccessibility to applicants without stable documentation or digital literacy:** System expects certain document types and digital submission methods. Applicants without stable addresses, proper ID, or comfort with technology face systematic barriers.
- **Lack of transparency:** Applicants don't understand how eligibility was determined or what factors the system considered. They cannot meaningfully contest specific algorithmic determinations.
- **Automation bias:** When case workers (Option B) or applicants (Option A) see the system's recommendation, they tend to defer to it without genuine review. Legitimate appeals are less likely.
- **Privacy and data security risks:** System collects and cross-references sensitive information. Data breaches expose personal information. Applicants have minimal control over how their data is used.
- **Reduced human judgment:** Case workers lose opportunities to exercise discretion in close calls or account for individual circumstances that the system cannot measure.

#### Extent dimensions (for key harms):
- **Magnitude:** Very high for wrongly denied applicants. Losing eligibility for housing assistance, food support, or unemployment benefits creates acute hardship—homelessness, food insecurity, loss of housing. This is not a minor inconvenience.
- **Scope:** Concentrated among specific demographic groups (people from marginalized communities, non-English speakers, people with disabilities, people without stable housing). Could affect 10-30% of applicants if bias is significant.
- **Likelihood:** High. Training data bias is well-established in algorithmic systems; unless actively mitigated, system will show disparities.
- **Duration:** Harms persist as long as the system is in operation and produces biased decisions. People wrongly denied benefits may be reluctant to reapply, making harms long-lasting.

#### Unintended harms:
- **Chilling effect on benefit enrollment:** People learn that the system is biased or opaque, and choose not to apply, even if eligible. Society loses the benefit of serving people who need it.
- **Erosion of public trust:** Visible errors and bias undermine confidence in the agency and government more broadly. Communities withdraw from engagement.
- **Geographic inequality:** Biased outcomes in certain neighborhoods lead budget analysts to reallocate resources away from high-need areas, deepening inequality.
- **Staffing impacts:** If system is perceived as a replacement rather than a tool, case worker positions are cut. Loss of institutional knowledge, reduced capacity to handle complex cases.

### Section 5 — WHO IS AFFECTED, IN WHAT WAY

#### Fairness spectrum:

```
Great Benefit                         |                          Great Harm
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] Applicants with stable                                    [B] Applicants from 
    documentation, digital                                        marginalized communities,
    literacy, privileged background                               unstable housing, limited
                                                                   digital literacy, prior
        BENEFIT: Faster access                                    negative experiences with
        to support without hassle.                                government.
        Perceived fairness.
        (Group ~40% of applicants)                                 HARM: More likely wrongly
                                                                   denied. Cannot navigate
                                  [C] Case workers                 appeals. Face barriers to
                                      (Benefits from freed        using the system. Existing
                                       time; harmed by            vulnerabilities amplified.
                                       deskilling/layoffs)         (Group ~40% of applicants)

                                                                [D] Government agencies
                                                                    (Short-term benefit from
                                                                     efficiency; long-term
                                                                     harm from liability,
                                                                     trust erosion)
```

#### Distributional analysis:

**Is this distribution fair?**

No. The harms and benefits are distributed unequally, and the inequality tracks existing advantage and disadvantage.

- **Privileged applicants** (Group A): Receive the intended benefits—faster support, reduced hassle—with minimal exposure to harms. Estimated ~40% of applicants.
- **Marginalized applicants** (Group B): Bear the brunt of harms—wrongly denied benefits, opaque system, barriers to appeals. These are people already facing systemic disadvantage. Harms are acute. Estimated ~40% of applicants.
- **Case workers** (Group C): Mixed harms and benefits depending on organizational response. Professional loss of autonomy; potential job loss.
- **Agencies and society** (Group D): Benefit short-term from efficiency; face long-term liability and trust erosion.

**Fairness concerns:**
- Already-marginalized groups face **outsized harms** from a system that promises to serve them.
- Privileged groups **capture most of the benefit** while being insulated from risks.
- **Remediation is unequal**: people with resources (ability to hire lawyers, advocates) can contest decisions; those without cannot, leading to permanent inequality in outcomes.
- **Geographic inequality deepens**: biased outcome data shapes future funding, withdrawing resources from highest-need areas.

This violates principles of **Justice** (fair distribution of benefits and burdens) and **Dignity** (respect for all people equally). It also violates **Trust** (goodwill and competence in applicants' interests) and **Responsibility** (agencies cannot account for or meaningfully mitigate harms).

### Section 6 — VALUES (Part Two: Plan for action in alignment with values)

#### Which values are you prioritizing, and why?

This is where the decision between Option A and Option B becomes explicit. Each option prioritizes different values.

**Common to both options (values both should uphold):**
- **Justice:** System must not amplify bias. Harms must not disproportionately fall on already-marginalized groups. Benefits must be distributed fairly.
- **Autonomy:** Applicants must retain meaningful voice and understanding of how decisions are made.
- **Dignity:** People must be treated as full human beings, not data profiles. Their circumstances and agency must be respected.
- **Responsibility:** Agencies must be able to account for decisions and take real action to mitigate harms.

**Option A prioritizes:**
- Efficiency and consistency at the expense of autonomy, dignity, and real human accountability. Assumes the system will be sufficiently fair; relies on appeals to catch errors.

**Option B prioritizes:**
- Autonomy, dignity, and human responsibility. Retains human judgment as the final arbiter. Assumes that case worker review can catch many biases and account for individual circumstances.

The choice between options is fundamentally about **which values matter most**: the administrative efficiency gained from automation, or the autonomy and dignity of applicants.

### Section 7 — HOW TO EXPAND BENEFITS

#### Low-hanging fruit and enhancements aligned with values:

1. **Proactive outreach:** Publicize the faster processing times in communities with longest wait times. Lower barriers to application (multiple languages, in-person and online options, navigator support).

2. **Integrated support:** Use the time freed by automation to offer case workers capacity to provide wraparound services—help applicants understand benefits, navigate systems, plan for stability.

3. **Transparency in application:** Provide applicants with a clear explanation of what information they need to submit and why each piece matters. Reduce mystery.

4. **Community feedback:** Build regular feedback channels so applicants can share where the system is working and where it's failing.

5. **Geographic prioritization:** Use system efficiency to reach underserved rural areas and reduce disparities in access.

6. **Case worker professional development:** Invest in training case workers in how to work alongside AI—how to review its recommendations critically, how to account for factors the system misses, how to maintain human connection even when automation is in the workflow.

### Section 8 — HOW TO REDUCE HARMS

#### Prevent harms:
1. **Audit training data:** Examine the data the system was trained on for historical bias. Retrain the model on corrected historical decisions (what should have happened, not what did happen).

2. **Test for disparities:** Before deployment and continuously after, measure system performance by demographic group (race, income, immigration status, disability status, language). If disparities appear, pause and re-examine.

3. **Transparency requirements (Option B strongest, Option A weaker):** Applicants must receive clear explanations of how eligibility was determined and what information was considered. They must be able to identify errors and contest specific determinations.

4. **Privacy minimization:** Collect only data necessary for eligibility determination. Don't cross-reference data from agencies unless required. Limit retention periods. Encrypt sensitive data.

#### Protect people from harms:
1. **Human oversight (Option B):** Retain human case worker authority over final decisions. Require case workers to actively review AI recommendations and document their rationale. Don't allow automation bias to go unchecked.

2. **Appeals designed for accessibility:** Make appeals free, in-person and online, in multiple languages. Provide free advocates or legal support for people contesting decisions. Time-bound reviews so people don't wait months for an appeal decision.

3. **Restore documentation flexibility:** Accept a variety of documents and forms of proof (e.g., letters from shelters, utility bills, community attestation) rather than only official government IDs.

4. **Community accountability:** Establish review boards that include affected community members to oversee the system's impacts and recommend changes.

#### Support people impacted by harms:
1. **Proactive remediation:** When errors are discovered, agencies proactively contact affected applicants, reverse decisions, and provide back payments. Don't wait for appeals.

2. **Advocate availability:** Fund community organizations to help people navigate the system and appeals.

3. **Diversity in case workers:** Hire case workers from communities being served so cultural understanding is embedded in the system.

4. **Regular fairness audits:** Independent organizations should audit the system's outcomes quarterly, looking for emerging disparities. Results should be public.

### Section 9 — BOTTOM LINE

#### What changes will be made?

To pursue this work ethically, the following commitments are non-negotiable, regardless of which implementation option (A or B) is chosen:

**Before deployment:**
1. Audit training data for bias; retrain model on corrected historical decisions.
2. Test system performance across all demographic groups; pause deployment if disparities are found.
3. Build fully accessible application and appeals processes (free, multiple languages, in-person and online).
4. Implement transparency requirements: every applicant receives clear explanation of how their eligibility was determined.
5. Privacy minimization: collect only necessary data; minimize cross-agency data sharing; encrypt sensitive information.

**During deployment (Option B mandatory; Option A only with strong mitigation):**
1. Retain human case worker oversight: case workers have final decision-making authority and actively review AI recommendations (Option B) rather than accepting them by default.
2. Eliminate automation bias: require documented justification if case worker agrees with AI recommendation without genuine review.
3. Monitor ongoing fairness: track outcomes by demographic group. Trigger human review if disparities emerge.
4. Establish independent auditing: external organizations audit system outcomes quarterly; results are public.

**Ongoing accountability:**
1. Proactive remediation: when errors are discovered, contact affected applicants and correct benefits.
2. Community oversight: create review boards including affected community members.
3. Staff investment: invest in case worker professional development and diverse hiring so human judgment is informed and culturally aware.
4. Regular reassessment: every 12-24 months, reevaluate whether the system is serving all populations fairly. Suspend operation if ongoing bias is uncovered.

**The trade-off being made:** We are accepting the administrative cost of human oversight and the slower processing gains in Option B (versus Option A) in order to preserve applicant autonomy, agency dignity, and real accountability. The primary driver of this choice is the ethical primacy of **Justice, Autonomy, and Dignity** over administrative efficiency. Efficient systems that harm marginalized people are not acceptable.

---

→ Carries forward to Tool 4 (Ethics Gauge):

- **Action/Creation:** Automated AI system determining or recommending initial eligibility for welfare benefits (housing, food, unemployment), deployed agency-wide at scale.
- **Benefits with extent:** Eligible applicants receive decisions within 3-5 days instead of 60+ days (magnitude: very high for eligible; scope: all applicants; likelihood: high; duration: enduring); case workers freed from administrative tasks to focus on complex cases (magnitude: moderate; scope: all case workers; likelihood: high); geographic consistency reduces regional disparities in access (magnitude: moderate; scope: all regions; likelihood: moderate to high).
- **Harms with extent:** Ineligible denials due to bias in training data (magnitude: very high for wrongly denied; scope: estimated 10-30% of applicants from marginalized groups; likelihood: high; duration: enduring); lack of transparency prevents meaningful contestation (magnitude: high—applicants can't understand or contest decisions; scope: all applicants; likelihood: high); automation bias allows errors to propagate (magnitude: high; scope: all applicants; likelihood: high); privacy/data security risks (magnitude: very high if breach occurs; scope: all applicants; likelihood: moderate).
- **Fairness patterns:** Unequal distribution: privileged applicants benefit most; marginalized applicants bear most harms. System amplifies existing advantage/disadvantage. Remediation barriers: those with legal resources can appeal; those without cannot. Geographic inequality: biased outcome data shapes funding away from high-need areas.
- **Autonomy/dignity issues:** Applicants cannot understand how decisions were made; they have no meaningful voice in determinations affecting their lives. System treats people as data profiles rather than individuals with complex circumstances and agency. Automation bias removes human judgment that might account for individual factors.

---

## Tool 4 — Ethics Gauge

### Dimension 1 — HOW IS IT BENEFICIAL?

**Spectrum 1a: Individual benefit**

```
Limited benefit to individuals ←→ Great benefit to individuals
         [−]                    [Neutral]           [+]

                    ✓ System position: [+]
        (for eligible applicants; [−] for wrongly denied)
```

**Assessment:** For eligible applicants, the benefit is substantial and tangible: receiving housing support, food assistance, or unemployment income within days instead of weeks is a great benefit that exceeds what currently exists. For wrongly denied applicants, the system creates harm rather than benefit. For case workers, the freed time is a benefit, but only if it's redirected toward better service rather than layoffs. Overall mark: [+] for eligible applicants; [−] for those wrongly denied.

**Observations:** System delivers on efficiency promise for eligible applicants. But benefit is severely undermined if bias causes significant false denials.

**Investigation needed:** Validate the proportion of applicants actually eligible vs. those who will be wrongly denied due to bias. What's the actual breakdown? This is critical to whether net individual benefit is positive.

---

**Spectrum 1b: Scope of benefit (how many people benefit)**

```
Benefit limited to few select people ←→ Large numbers and multiple groups benefit
              [−]                     [Neutral]         [+]

                        ✓ System position: [−/Neutral]
        (many people benefit; but largest concentration among privileged)
```

**Assessment:** The system will serve many people (thousands of applicants per month per agency). But the benefit is not distributed equally across groups. Privileged applicants with stable documentation and digital literacy capture most of the benefit. Marginalized applicants are underrepresented in the beneficiary population due to bias and access barriers. Mark: [−] on fairness grounds; [+] on numbers alone.

**Observations:** Quantity of people served increases, but equity of distribution is poor.

**Investigation needed:** What proportion of applications come from marginalized communities? Are they receiving benefits at rates proportional to their eligibility, or are false denials suppressing their representation?

---

**Spectrum 1c: Likelihood of benefit**

```
Action unlikely to succeed / low likelihood ←→ Very likely the benefit will be achieved
                  [−]                    [Neutral]       [+]

                              ✓ System position: [+]
        (system is technically capable; business case is sound)
```

**Assessment:** The system is likely to achieve what it was designed to do—process applications faster and more consistently. The technical likelihood of success is high. Mark: [+].

**Observations:** System delivers on its core promise of speed and consistency. What's uncertain is whether the consistency is fair or biased.

**Investigation needed:** What's the actual false-negative rate (applicants wrongly denied)? Is it acceptable? If the system reduces false positives (fraud prevention) at the cost of too many false negatives (eligible people denied), the likelihood of actual benefit is lower than it appears.

---

**Synthesis for Dimension 1:**

The system is **beneficial** for eligible applicants in receipt of timely support. However, the benefit is **unevenly distributed**, concentrated among those with the most resources to navigate the system. For wrongly denied applicants, the system creates harm masquerading as benefit. **The overall benefit score of [+] is conditional on the system being audited and proven to have acceptable false-negative rates AND being deployed with strong mitigation measures to ensure those wrongly denied have accessible appeals.**

---

### Dimension 2 — HOW IS IT HARMFUL?

**Spectrum 2a: Magnitude of harm**

```
Great harm to individuals; more than alternatives ←→ Limited harm; less than alternatives
              [−]                    [Neutral]         [+]

                    ✓ System position: [−]
        (wrongly denied applicants face acute hardship)
```

**Assessment:** For applicants wrongly denied benefits due to bias or system error, the harm is great and more severe than the status quo (in which case workers might catch the error). Losing access to housing assistance means risking homelessness. Losing food support means food insecurity. Losing unemployment benefits means acute economic hardship. These are not minor inconveniences. Mark: [−].

**Observations:** The system's speed becomes a liability if it propagates errors at scale.

**Investigation needed:** What's the actual false-negative rate? How many eligible people will be wrongly denied per month/year? If significant, this is a dealbreaker.

---

**Spectrum 2b: Scope of harm (how many people are harmed)**

```
Large numbers / multiple groups harmed ←→ Harm limited to few people
              [−]                     [Neutral]      [+]

                        ✓ System position: [−]
        (many people harmed; concentrated among marginalized groups)
```

**Assessment:** If bias is present in training data (which is well-documented in algorithmic systems), the harm will affect large numbers of people, specifically those from marginalized communities. Estimated 10-30% of applicants could be affected. Mark: [−].

**Observations:** Scale matters. A system that harms 5% of applicants is very different from one that harms 25%.

**Investigation needed:** What's the actual distribution of harms by demographic group? Are there disparities in false-negative rates by race, income, immigration status, language, disability?

---

**Spectrum 2c: Preventability of harm**

```
Harm certain to occur / impossible to prevent ←→ Harm unlikely; potential harm preventable
              [−]                     [Neutral]        [+]

                        ✓ System position: [Neutral/−]
        (harm is not inevitable if mitigated; but default deployment = high harm)
```

**Assessment:** Without mitigation, bias-driven harm is very likely (well-established in AI systems). With robust mitigation—bias audits, fairness testing, transparency, human oversight, accessible appeals—much of the harm can be prevented. Mark: [Neutral] with strong mitigation; [−] without.

**Observations:** The system is not inherently harmful, but default deployment (especially Option A) will likely produce harm without active prevention.

**Investigation needed:** What specific mitigation measures will be in place? Will they be enforced? Will there be independent auditing?

---

**Synthesis for Dimension 2:**

The system **creates significant potential for harm**, particularly to marginalized applicants. Harms include wrongful denials due to bias, opaque decision-making that prevents contestation, privacy risks, and erosion of trust. **The overall harm score of [−] is unavoidable unless strong mitigation measures are implemented and enforced.** This is one of the highest-priority concerns raised by this assessment.

---

### Dimension 3 — HOW FAIR IS IT?

**Spectrum 3a: Equal vs. unequal distribution**

```
Certain people or groups affected more than others ←→ All people and groups affected equally
              [−] (neutral spectrum)                [+]

                    ✓ System position: [−]
        (impacts are unequally distributed by privilege/marginalization)
```

**Assessment:** The system's impacts are not equally distributed. Benefits concentrate among privileged applicants; harms concentrate among marginalized applicants. Mark: [−].

**Observations:** Unequal distribution is not inherently unfair (different groups may need different support), but in this case, the inequality tracks existing advantage/disadvantage, making it inequitable.

---

**Spectrum 3b: Burden on the less advantaged vs. the privileged**

```
Those harmed less advantaged; those benefiting have privilege ←→ No more harm to less advantaged; beneficiaries have greater need
              [−]                                        [Neutral]                    [+]

                            ✓ System position: [−]
        (pattern of harm aligns with existing marginalization)
```

**Assessment:** This is precisely what we see: those harmed by wrongful denials and system opacity are people already facing systemic disadvantage (marginalized communities, people without stable housing, people with disabilities). Those benefiting most are privileged applicants with stable documentation and resources to navigate the system. This is **unjust**. Mark: [−].

**Observations:** The system reproduces and amplifies existing inequality rather than reducing it.

**Investigation needed:** Is there any evidence that the system could be redesigned or deployed in a way that benefits those with the greatest need most? Currently, the answer is no without major changes.

---

**Spectrum 3c: Acceptability and justifiability of burden**

```
Burden on those most harmed not acceptable / unjustifiable ←→ Burden is acceptable / justifiable
              [−]                                [Neutral]                    [+]

                            ✓ System position: [−]
        (burden is not justified; efficiency does not justify harm to vulnerable people)
```

**Assessment:** The burden of wrongful denials, opacity, and system barriers falls on people experiencing acute vulnerability. No amount of administrative efficiency justifies denying housing support or food assistance to eligible people. The burden is not acceptable. Mark: [−].

**Observations:** This is a fundamental fairness failure. A system that helps privileged people at the expense of vulnerable people fails to meet basic ethical standards of justice.

**Investigation needed:** Is there any way to redesign the system to spread burdens and benefits more fairly? This should be a non-negotiable requirement before deployment.

---

**Synthesis for Dimension 3:**

The system is **significantly unfair**. Impacts are unequally distributed, with greater harms concentrated on already-marginalized groups and greater benefits concentrated on privileged groups. This violates the value of **Justice**. **No configuration of this system (Option A or B) can be fair without major changes to prevent and mitigate bias and to provide equitable access and remediation.** This is a critical blocker for Option A (automated decision-making without human oversight). Option B (human case worker oversight) offers better potential for fairness, but only if human review actually catches errors and case workers are trained to recognize and counteract their own biases.

---

### Dimension 4 — HOW EMPOWERING IS IT?

**Spectrum 4a: Informed choice and understanding**

```
Ability to make informed choices reduced ←→ Ability to make informed choices unimpaired/increased
              [−]                     [Neutral]        [+]

                    ✓ System position: [−]
        (applicants cannot understand how decisions are made)
```

**Assessment:** Applicants do not receive clear explanations of how eligibility was determined or what information the system considered. They cannot identify errors or articulate appeals effectively because they don't understand the logic. This severely reduces the ability to make informed choices about whether to accept the decision, appeal, or reapply. Mark: [−].

**Observations:** Opacity is a fundamental barrier to empowerment. People cannot govern themselves if they don't understand the decisions affecting them.

**Investigation needed:** Will the system provide clear, understandable explanations of how eligibility was determined? Will applicants have access to their data and the system's reasoning? This is essential.

---

**Spectrum 4b: Control over one's life**

```
Control over aspects of life removed ←→ Control is retained or enhanced
              [−]                     [Neutral]        [+]

                    ✓ System position: [−]
        (system removes applicant control; decision made for them, not with them)
```

**Assessment:** Applicants have minimal control over how their eligibility is determined or what information is considered. For Option A, the system makes the decision; applicants can only appeal. For Option B, a human case worker makes the decision, but the applicant still has limited input. In both cases, applicant agency is minimal. The decision is made for them, not with them. Mark: [−].

**Observations:** In contrast, case workers lose some control (reduced discretion) but may gain control in other ways (freed time to manage client relationships). The trade-off favors organizational control over applicant control.

**Investigation needed:** Can the system be redesigned to meaningfully include applicant voice? What would co-design with applicants look like?

---

**Spectrum 4c: Coercion, manipulation, and freedom**

```
Activities removed; coercion, manipulation, pressure present ←→ No coercion/manipulation; freedom preserved
              [−]                                      [Neutral]        [+]

                            ✓ System position: [−/Neutral]
        (system doesn't coerce explicitly, but automation bias is a form of soft coercion)
```

**Assessment:** The system itself does not overtly coerce or manipulate. However, automation bias—the tendency to defer to automated recommendations without genuine review—creates a form of psychological pressure that constrains choice. When applicants see the system's recommendation, they are less likely to appeal even when they believe it's wrong. When case workers see the recommendation, they are less likely to truly review it. This is a subtle but real form of coercion. Mark: [−/Neutral].

**Observations:** Psychological effects of automation can reduce freedom as much as explicit coercion.

**Investigation needed:** Will the system be deployed in a way that highlights automation bias risks and trains people (both case workers and applicants) to resist defaulting to automated recommendations?

---

**Synthesis for Dimension 4:**

The system is **not empowering**. Applicants lack understanding of how decisions are made, have minimal control over determinations affecting their lives, and are subtly pressured by automation bias to accept outcomes they might otherwise contest. **The system actively degrades autonomy and decision-making power, particularly for those least equipped to navigate appeals and assert their agency.** This is a critical concern for both Option A and Option B, though Option B (with human oversight) offers more potential for meaningful engagement if case workers are trained to truly hear applicants.

---

### Synthesis Across All Four Dimensions

**The overall ethical assessment is CONDITIONAL AND CONCERNING:**

| Dimension | Rating | Status |
|-----------|--------|--------|
| **How is it beneficial?** | [+] | High benefit IF bias is absent; conditional on fairness testing. |
| **How is it harmful?** | [−] | Significant potential harms, especially to marginalized applicants. Harms are preventable with mitigation but unavoidable without it. |
| **How fair is it?** | [−] | Significantly unfair without major changes. Requires robust bias prevention and equitable access to appeals. |
| **How empowering is it?** | [−] | Not empowering; reduces applicant agency and understanding. Automation bias constrains freedom. |

**Critical tensions:**

1. **Efficiency vs. fairness:** The system promises speed but at the cost of fairness if bias is present. Robust mitigation (human oversight, bias audits, appeals) slows down the process and reduces the efficiency gains.

2. **Consistency vs. individual justice:** The system aims to be consistent (same rules applied everywhere), but this consistency becomes harmful if the rules or the algorithm embeds bias. Fair treatment sometimes requires case-by-case judgment, not consistency.

3. **Organizational benefit vs. applicant welfare:** The system provides substantial benefit to the organization (efficiency, cost reduction) and to eligible applicants (faster support). But it shifts risks onto marginalized applicants (wrongful denials, opaque processes). The organization gains; vulnerable people bear the burden.

**Comparison of options on these dimensions:**

- **Option A (automated decision-making):** Maximizes efficiency benefit but minimizes safeguards against harm. Fairness and empowerment are severely compromised without extraordinary mitigation. Applicants have little recourse except appeals, which are inhibited by automation bias.

- **Option B (AI as decision-support, humans decide):** Reduces efficiency gains but preserves more potential for fairness and empowerment. Human case workers retain discretion and can account for individual circumstances. Appeals have a real person to engage with. Fairness and empowerment are better protected IF case workers are trained and incentivized to genuinely review recommendations rather than default to them.

**Overall ethical verdict:**

This system **cannot be deployed ethically in its current design without robust mitigation measures.** Neither option is acceptable without:

1. Proof that bias in training data has been identified and corrected
2. Evidence from fairness testing that the system performs acceptably across demographic groups
3. Full transparency to applicants about how decisions are made
4. Free, accessible appeals with real human review
5. Independent ongoing monitoring of fairness outcomes
6. Proactive remediation when errors are discovered

**Option B is more ethically defensible than Option A because it preserves human judgment and applicant recourse.** But Option B only works if human oversight is real, not performative. Case workers must be trained to recognize and resist automation bias, and the system must be designed to support genuine review rather than rubber-stamping.

---

→ Carries forward to Tool 5 (Weighing Options):

- **Current Situation summary:** Government agencies seek to reduce processing times for welfare benefits applications and ensure consistent eligibility decisions. Manual case worker review currently takes 60+ days and varies by region. The proposed solution is an AI system to screen applications and determine or recommend eligibility. The agencies face pressure to serve more people faster with limited resources, but they also have obligations to serve vulnerable populations fairly and to maintain public trust. The core challenge: how to gain efficiency without sacrificing fairness, autonomy, and accountability to applicants.

- **Hot spots (negative-pole spectra):** Bias in training data leading to disproportionate denials for marginalized groups (Harm dimension). Lack of transparency preventing applicants from understanding or contesting decisions (Empowerment dimension). Unequal distribution of benefits and burdens by privilege/marginalization (Fairness dimension). Automation bias preventing genuine human review of recommendations (Empowerment dimension). Risk of staffing cuts reducing capacity and institutional knowledge (Societal impact). Privacy and data security risks (Harm dimension). Geographic inequality deepening as biased outcomes shape funding (Fairness dimension).

- **Knowledge gaps flagged for Obstacles section:** What is the actual false-negative rate in the system? Are there measurable disparities in outcomes by demographic group? Can case workers genuinely override the system's recommendations, or will automation bias dominate? How accessible will the appeals process be? How quickly can mitigation measures be implemented? What independent oversight mechanisms exist?

- **Values to carry into "What are you prioritizing?":** Justice (fair distribution of benefits and burdens; protection of marginalized groups); Autonomy (applicants' ability to understand and contest decisions affecting them); Dignity (respect for all people as full human beings, not data profiles); Trust (agencies' competence and goodwill in applicants' interests); Responsibility (agencies' ability to account for decisions and mitigate harms); Well-being (timely access to support; prevention of hardship).

---

## Tool 5 — Weighing Options

### Current Situation

Government agencies administering welfare benefits programs (housing assistance, food support, unemployment) face a critical challenge: they must process thousands of applications monthly with limited staff, and processing times average 60+ days. Long delays mean eligible people wait without support, experiencing homelessness, food insecurity, and economic hardship. Additionally, case workers in different regions apply eligibility rules inconsistently, and geographic location can significantly affect an applicant's outcome despite similar circumstances.

These agencies have proposed an AI system to automate initial eligibility screening. The system would ingest applications, extract information, cross-reference government records, and produce an eligibility determination or recommendation within days. The core promise: faster, more consistent decisions serving more vulnerable people sooner.

However, the proposed system raises significant ethical concerns:
- Training data contains decades of biased eligibility decisions; without intervention, the system will embed and amplify these biases
- Applicants will not understand how decisions are made or have meaningful ways to contest them
- Marginalized applicants face highest risk of wrongful denials
- Automation bias will likely prevent genuine human review
- Privacy and data security risks are substantial
- Public trust in agencies is already fragile in affected communities; biased automation could erode it further

The agencies now must decide: How do we gain efficiency without sacrificing fairness, autonomy, and accountability?

Two options are being considered:

---

### OPTION A: AI as Primary Decision-Maker (with Appeals Process)

#### Option Description

The AI system makes the initial eligibility determination. This determination stands unless the applicant appeals. The appeals process includes human case worker review, but the default is the AI decision. The system is deployed agency-wide; case workers' primary role shifts to handling appeals and complex cases rather than reviewing all initial applications.

#### Societal Impact — How are people and society affected?

##### Benefits

- **Very fast decisions:** Eligible applicants receive benefits within 3-5 days. For people experiencing homelessness, hunger, or unemployment, this difference is transformative. Reduces acute suffering.
- **Increased throughput:** With AI handling screening, the same staff can potentially serve more applicants. More people receive benefits who would have waited months under the old system.
- **Geographic equity (potential):** Consistent application of rules reduces regional disparities—an applicant in a rural area has the same decision logic as one in an urban area. This is genuinely valuable if the consistency is fair.
- **Societal trust in efficiency (initial):** Public perception of government may improve as people see benefits processed quickly.

##### Harms

- **Wrongful denials at scale:** If bias is present in training data—which is well-documented in algorithmic systems—the AI will make biased denials. These errors scale: instead of 1-2 case workers making errors, the system makes biased decisions for thousands of applicants per month.
- **Opaque decisions:** Applicants don't understand how eligibility was determined. They can't identify errors or articulate appeals effectively. This is especially harmful for people with limited digital literacy or language barriers.
- **Automation bias in appeals:** When applicants see the AI decision, they are psychologically less likely to appeal, even when the decision is wrong. When case workers review appeals, they may default to the AI recommendation without genuinely reconsidering. The appeals process becomes pro forma.
- **No case worker discretion:** Situations that warrant judgment—a person with irregular income, complex family circumstances, or missing documentation that can be verified through conversation—are handled rigidly by algorithm. Human understanding is removed.
- **Erosion of trust:** Communities that experience disproportionate denials will lose trust in the agency and government. Visible bias will confirm existing distrust.
- **Privacy and data security:** System collects and cross-references sensitive data. Breaches expose applicants. Applicants have minimal control over how their information is used.
- **Staffing implications:** If efficiency gains are realized, agencies may cut case worker positions. Institutional knowledge is lost. Capacity to handle complex cases and provide supportive services declines.

##### Extent Dimensions

- **Magnitude:** Benefits are very high for eligible applicants (access to support within days changes their immediate future). Harms are very high for wrongly denied applicants (loss of housing, food, income support is acute hardship). Harms outweigh benefits if bias leads to significant false denials.
- **Scope:** Serves all applicants; harms concentrated among marginalized groups. Estimated 40-50% of applicants from marginalized communities; 10-30% of those could be wrongly denied if bias is present.
- **Likelihood:** Efficiency gains are very likely (system can process faster). Bias-driven harms are very likely if training data is not audited and corrected. Appeals process being underutilized is very likely due to automation bias.
- **Duration:** Both benefits and harms are enduring—the system operates for years at scale.

##### Net Societal Impact

Conditional and negative without strong mitigation:
- IF the system can prove it has no significant bias and provides transparent decision explanations → net positive for eligible applicants, mixed for marginalized applicants (faster access but more opaque)
- IF the system cannot prove fairness → net negative overall. Efficiency gains for privileged applicants come at the cost of harming marginalized people.

**Likely scenario without mitigation:** Net negative. Efficiency serves privileged populations; harms are concentrated on vulnerable populations. Society loses social cohesion and public trust as inequality in welfare access increases.

---

#### Organizational Impact — How might the organization be affected?

##### Benefits

- **Dramatically reduced processing costs:** Fewer case workers needed for initial screening = significant salary and operational savings.
- **Increased throughput:** Same staff processes 3-5x more applications.
- **Improved public image (initially):** Citizens see benefits processed quickly; perception of government competence improves.
- **Compliance and consistency:** Agency can demonstrate it's applying the same rules everywhere, reducing claims of regional bias and inconsistency (though the rules themselves may be biased).
- **Staff morale (potential):** Freed case workers may feel less burned out by repetitive work (if not laid off).

##### Harms

- **Loss of institutional knowledge:** Case workers laid off take with them years of understanding about edge cases, local context, and how to work with vulnerable populations.
- **Legal liability:** Algorithmic errors scale. Lawsuits from people wrongly denied benefits. Class action litigation possible. Damages could exceed savings.
- **Regulatory scrutiny:** State and federal regulators may investigate if bias is discovered. Fines, audits, mandated system changes.
- **Reputational damage:** Visible bias in welfare eligibility erodes public trust, especially in affected communities. Harder to recruit qualified staff. Political pressure increases.
- **Appeal backlogs:** If automation bias is real, appeals may be underpowered but spike once problems become visible. System must surge to handle appeals, negating efficiency gains.
- **Reduced accountability:** Agency cannot articulate how decisions were made. Blame diffuses ("the system decided"). Leadership faces criticism for deploying opaque system.

##### Extent Dimensions

- **Magnitude:** Savings could be substantial (20-40% reduction in screening staff costs). Liability could be substantial if class action succeeds (millions in settlements). Reputational damage is significant in affected communities.
- **Scope:** Affects entire agency, all regions, all applicants.
- **Likelihood:** Cost savings are very likely if system works as designed. Legal liability is moderately likely if bias is present. Reputational damage is very likely if bias becomes visible.
- **Duration:** Both benefits and harms persist for years.

##### Net Organizational Impact

Short-term positive (cost savings), long-term negative (liability, reputational damage, regulatory scrutiny) if bias is not actively mitigated.

Likely scenario: After initial savings, organizations face legal and regulatory costs that offset gains. Reputation in affected communities suffers, making it harder to serve populations effectively.

---

#### Obstacles — What might prevent implementation or success?

| Obstacle | Likelihood | Contingency Plan |
|----------|-----------|-----------------|
| **Training data contains significant bias** | High (well-documented in algorithmic systems) | Conduct thorough bias audit before deployment. Retrain model on corrected historical decisions. Test on held-out data by demographic group. If significant disparities found, pause deployment and redesign. |
| **Applicants don't understand decisions and appeals underutilized** | High (automation bias is well-documented) | Provide transparency: every applicant receives written explanation of how eligibility was determined. Actively invite appeals; remove stigma. Train case workers to actively solicit appeals from denied applicants. Track appeal rates; if too low, investigate. |
| **Case workers unable to override AI recommendations due to automation bias** | High | Require case workers to document their rationale every time they agree with or disagree with AI recommendation. Use audits to identify workers who always defer to AI without noting their own review. Retrain and accountability measures. |
| **Privacy breach exposes sensitive data** | Moderate (data breaches are a known risk) | Minimize data collection to essentials only. Encrypt sensitive information. Limit cross-agency data sharing. Establish clear data deletion protocols. Have incident response plan in place. Regular security audits. |
| **Geographic inequality deepens as biased outcomes shape funding** | Moderate (policy decisions often based on outcome data) | Monitor outcome disparities by geography. Flag for human review if certain regions show anomalous rates. Allocate funding based on need, not system-reported eligibility rates. Build in safeguards against using outcome data to justify resource cuts. |
| **Staffing cuts reduce capacity to handle complex cases or appeals** | High | Establish protected staffing minimums before deployment. Tie staffing decisions to appeals volume and complexity. Measure system performance not just on speed but on quality (how many appeals are sustained; how many errors are discovered). |
| **System cost exceeds savings if implementation is more complex than expected** | Moderate | Conduct detailed cost-benefit analysis including litigation risk and remediation costs. Build in contingencies. Phase deployment: start with one region, measure real outcomes before scaling. |

---

#### Values Prioritized by Option A

- **Efficiency & administrative convenience:** This option maximizes speed and cost savings.
- **Consistency (in process, not necessarily fairness):** Same rules applied everywhere, which can mask bias as neutrality.
- **Organizational effectiveness:** Reduces burden on government operations.

**Values subordinated or compromised:**
- **Justice:** If bias exists, this option amplifies it.
- **Autonomy:** Applicants have minimal voice in decisions; appeals are the only recourse, and automation bias suppresses appeals.
- **Dignity:** Applicants treated as data profiles; individual circumstances dismissed by algorithm.
- **Responsibility:** Agency cannot account for how decisions were made; accountability is diffused.
- **Trust:** If bias becomes visible, trust in agency erodes, especially in affected communities.

**The explicit trade-off:** Option A prioritizes organizational efficiency and process consistency over applicant autonomy, dignity, and real accountability. It assumes the system will be sufficiently fair that errors are rare and caught on appeal. If that assumption is wrong—if bias is significant—then the trade-off fails, and the option harms the people it aims to serve.

---

### OPTION B: AI as Decision-Support Tool (Humans Decide)

#### Option Description

The AI system analyzes applications, extracts information, and produces a detailed report and preliminary recommendation. However, a human case worker reviews this report and makes the final eligibility determination. The case worker can agree with the AI recommendation or override it. The case worker's review includes explanation to the applicant of how eligibility was determined and invitation to discuss the decision. Appeals are handled by a different case worker or supervisor. The system is integrated into the case worker workflow to enhance their capacity rather than replace them.

#### Societal Impact — How are people and society affected?

##### Benefits

- **Faster decisions with human judgment:** Processing time reduces to 7-10 days instead of 60+ days (slower than Option A, but still substantial improvement). Eligible applicants receive support sooner. Urgency is reduced.
- **Fewer wrongful denials:** Case workers can identify and correct errors that the algorithm would have made. They can account for individual circumstances, recognize documentation that the algorithm would reject, and exercise judgment in edge cases.
- **Transparent, contestable decisions:** Case workers explain to applicants how eligibility was determined. Applicants can ask questions, provide additional information, or contest specific points with a human who understands their situation. Appeals have substance.
- **Preserved case worker expertise:** Case workers retain professional discretion and responsibility. They develop deeper understanding of applicants' situations, not just data points. This supports better long-term client relationships and identification of supports beyond eligibility.
- **Reduced automation bias:** Decisions are not anchored to algorithmic recommendation because case workers are expected to actively review and document their reasoning. Appeals are more likely because applicants feel heard.
- **Trust preserved:** Applicants interact with case workers who can explain decisions and show they've considered individual circumstances. Trust is more likely to be preserved, especially in communities that have experienced discrimination.
- **Accountability:** Case workers can articulate how decisions were made and why. If errors occur, they can be identified and corrected. Responsibility is clear.

##### Harms

- **Slower processing than Option A:** 7-10 days is slower than 3-5 days. Eligible applicants still wait longer than they would under Option A. This is measurable harm to people in acute need.
- **Reduced administrative efficiency:** More case worker time is required. The cost savings of Option A are not realized. Staffing levels may need to remain stable or increase.
- **Potential for inconsistency:** Different case workers may make different decisions in similar cases. Without algorithmic consistency, outcomes vary. (Note: This is sometimes a feature, not a bug—case worker discretion allows justice in individual cases—but it can also introduce new forms of bias if some case workers are themselves biased.)
- **Human decision-maker bias:** Case workers themselves can be biased. Training and diversity in hiring are critical. Some case workers may unconsciously favor applicants from their own demographic group or hold negative stereotypes.
- **Case worker workload:** If not carefully managed, case workers can become overwhelmed. The freed time from repetitive work is consumed by more complex cases. Burnout risk remains.
- **Privacy and data risks:** System still collects and cross-references sensitive data. Risks are similar to Option A.

##### Extent Dimensions

- **Magnitude:** Benefits are high for eligible applicants (faster access than status quo, but slower than Option A). Reduced wrongful denials is high-magnitude benefit for people who would have been harmed by bias. Slower processing is measurable harm for people in acute need.
- **Scope:** Affects all applicants. Harms and benefits are more evenly distributed across demographic groups because case worker discretion allows correction of algorithmic bias.
- **Likelihood:** Faster decisions are very likely (most of the speed gain without all of the bias). Fewer wrongful denials is likely IF case workers are trained and incentivized to actively review. More transparency and appeals is very likely.
- **Duration:** Benefits and harms are enduring.

##### Net Societal Impact

**Moderate to positive, conditional on case worker engagement and training:**

- IF case workers are trained to actively review AI recommendations and to recognize and counteract their own biases → net positive. Society gains faster service, fairer outcomes, and preserved trust.
- IF case workers default to AI recommendations (automation bias) or introduce their own biases → net mixed to negative. Society gains some speed but loses fairness and trust.

**Likely scenario with adequate support:** Net positive. Faster processing than status quo, fairer than Option A, better preserved trust.

---

#### Organizational Impact — How might the organization be affected?

##### Benefits

- **Preserved institutional knowledge:** Case workers remain employed. Years of understanding about edge cases, local context, and client needs are retained.
- **Reduced legal liability:** Case worker review and explanation of decisions reduces wrongful denial errors that might trigger lawsuits. Decisions are more defensible.
- **Improved public trust:** Applicants experience case worker engagement and explanation. Visible fairness and responsiveness improve public perception.
- **Staff morale:** Case workers feel they retain professional judgment and autonomy. Work feels meaningful. Reduced burnout (if workload is managed).
- **Regulatory advantage:** Regulators see human oversight as responsible design. Proactive equity measures reduce regulatory risk.
- **Flexibility for policy changes:** If eligibility rules change, case workers can adapt. System is less brittle than pure automation.

##### Harms

- **Higher ongoing operational cost:** Case worker salaries for full review of all applications. Cost savings of Option A not realized. Harder to justify budget increases in tight fiscal environments.
- **Slower throughput gain:** Cannot serve as many additional applicants with same staff. Efficiency gains are modest (maybe 20-30% throughput improvement vs. 300%+ for Option A).
- **Potential for case worker burnout:** If not carefully managed, case workers can face increased complexity in their workload. Training demands increase.
- **Inconsistency in decisions:** Different case workers may make different decisions. Requires ongoing quality assurance and training.
- **Potential case worker bias:** If hiring and training don't address bias, case workers themselves introduce bias. Mitigation requires ongoing investment.

##### Extent Dimensions

- **Magnitude:** Cost is moderate (more than Option A but not prohibitive). Liability reduction is moderate (real but not complete elimination). Trust improvement is moderate to high if execution is good.
- **Scope:** Affects entire organization and all applicants.
- **Likelihood:** Cost increase is very likely. Liability reduction is likely. Trust improvement is likely if communication is good.
- **Duration:** Effects are enduring.

##### Net Organizational Impact

**Moderate positive long-term, moderate negative short-term (cost perspective):**

Short-term: Higher costs, smaller efficiency gains. Harder to justify budget-wise.
Long-term: Reduced legal risk, better reputation, retained expertise, more sustainable operations.

The organizational case for Option B is weaker on cost-benefit grounds but stronger on risk management and sustainability grounds.

---

#### Obstacles — What might prevent implementation or success?

| Obstacle | Likelihood | Contingency Plan |
|----------|-----------|-----------------|
| **Automation bias: case workers default to AI recommendations without genuine review** | High (well-documented psychological bias) | Require case workers to document their reasoning when agreeing with AI recommendation. Use sampling audits to check whether documentation reflects genuine review. Train case workers on automation bias; provide specific techniques for active review. Hold case workers accountable for quality of review, not just speed. |
| **Case workers introduce their own biases** | Moderate to High (human bias is universal) | Hire diverse case worker staff reflecting communities served. Mandatory training in implicit bias and cultural competency. Regular outcome monitoring by demographic group to flag bias. Pair case workers (diverse pairs may catch each other's biases). Anonymous case worker reviews of each other's work. |
| **Increased case worker workload leads to burnout or errors** | Moderate (depends on workload management) | Monitor workload and case worker satisfaction. Adjust staffing or workload to prevent burnout. Measure quality (appeals, error rates) as well as speed. Invest in professional development and support. |
| **Consistency concerns (lack of predictability)** | Low (case worker discretion is not inherently bad; fairness sometimes requires judgment) | Provide clear guidance on eligibility criteria. Regular calibration meetings where case workers discuss edge cases. Spot audits to identify patterns of inconsistency. Frame consistency as "fair, not formulaic." |
| **Public and political pressure for cost savings (pressure to shift to Option A)** | Moderate to High (budget pressures are real) | Build political case for Option B: lower liability, better outcomes, sustained public trust. Show cost-benefit analysis that includes litigation risk. Commission independent evaluation showing fairness and effectiveness. |
| **Training and quality assurance demands** | Moderate | Invest upfront in comprehensive training program. Build ongoing quality assurance into operations (regular audits, feedback, retraining). Calculate cost of quality assurance as part of system cost. |
| **Data privacy and security** | Moderate (same as Option A) | Minimize data collection to essentials. Encrypt sensitive information. Limit cross-agency sharing. Regular security audits. Incident response plan. |

---

#### Values Prioritized by Option B

- **Justice:** Case worker discretion allows judgment in individual cases. Better potential for fair outcomes if case workers are trained and monitored.
- **Autonomy:** Applicants can discuss their situation with a case worker. They understand decisions and have meaningful ability to contest them.
- **Dignity:** Applicants treated as full human beings, not just data profiles. Individual circumstances are recognized and respected.
- **Responsibility:** Case workers can articulate how decisions were made and why. Accountability is clear.
- **Trust:** Applicant engagement with case workers creates opportunity for trust to be built or rebuilt.
- **Well-being:** Slightly slower than Option A, but human judgment ensures fewer wrongful denials that would deepen hardship.

**Values subordinated (compared to Option A):**
- **Efficiency:** Processing is slower (7-10 days vs. 3-5 days). Cost savings are minimal.
- **Consistency (in process):** Different case workers may make different decisions, though ideally decisions are consistently fair, not uniformly biased.

**The explicit trade-off:** Option B prioritizes applicant autonomy, dignity, and real accountability over organizational efficiency and cost savings. It accepts slower processing and higher ongoing costs in exchange for fairer outcomes and preserved trust. The underlying assumption is that fairness and trust matter more than maximal speed and cost reduction.

---

### Comparison Matrix

| Factor | Option A | Option B |
|--------|----------|----------|
| **Processing speed** | 3-5 days | 7-10 days |
| **Cost savings** | 30-40% reduction | Minimal (5-10%) |
| **Applicant fairness risk** | High (if bias present in training data) | Lower (case worker review catches some errors) |
| **Applicant autonomy** | Low (opaque, appeals inhibited) | High (explained decisions, meaningful appeals) |
| **Organizational liability** | High (scaled errors, litigation risk) | Lower (case worker review reduces errors, decisions defensible) |
| **Public trust** | Erodes if bias visible | Improves if case workers are perceived as fair |
| **Staff impact** | Potential layoffs, knowledge loss | Retained expertise, preserved jobs |
| **Applicant understanding of decisions** | Low (black box) | High (case worker explains) |
| **Reversibility / adaptability** | Difficult (system embedded) | Easier (human judgment can adapt) |

---

### FUTURE DIRECTION: Which Option and Why

#### Recommendation: **OPTION B, with mandatory safeguards and conditions**

**Rationale:**

Option B is ethically superior to Option A because it:

1. **Prioritizes fairness over efficiency.** Speed matters for people in acute need, but not at the cost of harming marginalized people. 7-10 days is still a significant improvement over 60+ days. The additional 5 days is an acceptable trade-off for fairer outcomes.

2. **Preserves applicant agency and dignity.** Applicants can understand and contest decisions. This is foundational to respecting autonomy.

3. **Enables real accountability.** Case workers can explain how decisions were made and why. Errors can be identified and corrected. This is essential for institutional responsibility.

4. **Reduces systemic harm.** Case worker judgment catches some errors that the algorithm would propagate at scale. This is critical for vulnerable populations.

5. **Maintains flexibility.** Human judgment allows for edge cases and circumstances the algorithm would miss. This is essential for serving diverse populations fairly.

6. **Preserves trust and social cohesion.** Applicants can see that case workers are considering their individual situations. Trust in institutions can be maintained or rebuilt.

7. **Allows iteration and improvement.** If problems emerge, case workers can adapt and iterate. Option A embeds biases at scale and is difficult to reverse.

**However, Option B is only defensible if the following conditions are met (non-negotiable):**

#### Mandatory Conditions for Option B Deployment

**Before deployment:**

1. **Comprehensive bias audit:** Examine training data and historical eligibility decisions for bias by demographic group. Identify biased patterns. Retrain model on corrected historical decisions.

2. **Fairness testing:** Test the AI system's recommendations against held-out test data by demographic group. Ensure no significant disparities in false-negative or false-positive rates. Document results; make results public.

3. **Case worker training:** Comprehensive training on:
   - How to actively review AI recommendations rather than defaulting to them
   - Recognizing and counteracting implicit bias in decision-making
   - Communicating decisions clearly to applicants in accessible language
   - Engaging applicants in discussion of their situation
   - Cultural competency for serving diverse populations
   - Specific techniques for identifying documentation alternatives and edge cases the algorithm might miss

4. **Transparent decision framework:** Develop clear, written guidance on eligibility criteria. Case workers must understand the rules and when discretion is appropriate.

5. **Accessible application and appeals process:**
   - Applications accepted in multiple formats (paper and online)
   - Languages available for top applicant populations
   - Free advocates or legal support for appeals
   - In-person and remote options
   - Clear explanation to every applicant of how eligibility was determined
   - Streamlined appeal process with case worker or supervisor review

6. **Privacy and data security:**
   - Minimize data collection to essentials
   - Encrypt sensitive data
   - Limit cross-agency sharing to essentials
   - Clear consent process for data use
   - Data deletion protocols
   - Regular security audits

**During deployment (ongoing):**

1. **Automation bias monitoring:** Audit case worker decisions to identify patterns where workers consistently defer to AI recommendations. Spot-check case worker reasoning. Provide feedback and retraining if automation bias is detected.

2. **Fairness outcomes tracking:** Monthly or quarterly reports on:
   - Eligibility approval rates by demographic group
   - Appeals rates by demographic group
   - Sustained appeals (cases where appeal decision differs from case worker initial decision)
   - Error rates by demographic group
   - Processing times by demographic group

3. **Independent auditing:** External organization audits system outcomes quarterly. Results are public. Recommendations are required to be acted upon.

4. **Case worker quality assurance:**
   - Regular case reviews (sampling)
   - Training on bias and quality
   - Accountability for decision quality, not just speed
   - Professional development opportunities
   - Reasonable workload (tracked and adjusted)

5. **Community oversight:** Create review board that includes affected community members to monitor system impacts and recommend changes. Meets quarterly. Reports to agency leadership.

6. **Rapid response to problems:** If emerging disparities are discovered, system changes are mandated within 30 days. If problems cannot be fixed, deployment is paused.

#### What must NOT happen:

- Case workers must NOT be laid off to reduce costs. Doing so would undermine the entire logic of Option B (human judgment).
- Processing speed targets must NOT override fairness. If meeting speed targets means errors increase, speed targets are relaxed.
- Automation bias must NOT be allowed to go unchecked. If case workers are consistently deferring to AI without genuine review, they must be retrained or replaced.
- Data privacy must NOT be compromised. Applicants must retain control over their sensitive information.
- Appeals must NOT be a afterthought. Appeals process must be fully resourced and treated as a core part of the system.

#### What might require reverting to Option A in the future:

If, despite these safeguards, Option B produces significantly unfair outcomes (e.g., persistent bias despite mitigation efforts), agencies should be prepared to move to a different model entirely—either a redesigned system with much stricter fairness constraints, or a reversion to improved manual review (hiring more case workers rather than automating). Option A should not be considered a fallback unless Option B has been genuinely tried with adequate resources and failed.

---

### Open Questions and Contingencies

**If fairness testing reveals bias in the AI system:**
- Retrain the model on corrected historical data
- If bias persists after retraining, pause deployment and redesign
- Explore alternative approaches (e.g., AI as screening tool to flag cases for priority case worker review, rather than AI making recommendations)

**If case worker training does not reduce automation bias:**
- Redesign the user interface to de-emphasize AI recommendations (e.g., present applicant case facts first, then AI analysis as one input among others)
- Require case workers to document reasoning in specific format that demonstrates genuine review
- Hold case workers accountable for quality of review through audits and feedback

**If processing times are slower than needed and applicants are experiencing severe hardship from delays:**
- Hire additional case workers rather than adopting Option A
- Streamline non-core aspects of case worker work (data entry, form completion) to free time for actual review
- Implement triage: high-priority cases (people experiencing homelessness, families with young children) are processed within 3-5 days; others within 7-10 days

**If public or political pressure mounts to adopt Option A for cost reasons:**
- Commission independent evaluation of Option B's fairness outcomes
- Present cost-benefit analysis that includes litigation risk and remediation costs of Option A
- Frame Option B as risk management and long-term cost reduction
- Build coalition with affected communities and civil rights organizations to maintain political support

---

### Implementation Timeline

**Months 1-2: Preparation**
- Assemble cross-functional team (case workers, technologists, civil rights experts, affected community representatives)
- Conduct bias audit of training data and historical decisions
- Identify and hire civil rights lead / ethics officer for project

**Months 3-4: System refinement and testing**
- Fairness testing of AI system by demographic group
- Case worker training design
- Appeals process design
- Community engagement and feedback

**Months 5-6: Pilot deployment**
- Start in one region or one program (e.g., housing only, not all three)
- 200-500 applications processed
- Track outcomes by demographic group
- Gather feedback from case workers and applicants

**Months 7-8: Adjustment and learning**
- Analyze pilot data; make system adjustments
- Retrain case workers based on lessons learned
- Refine appeals process
- Present findings to community oversight board

**Months 9-12: Scale to additional regions/programs**
- Expand to more regions while maintaining pilot in original region
- Continue monitoring fairness outcomes
- Ongoing case worker training and support

**Year 2+: Full deployment with sustained monitoring**
- Complete rollout across all programs and regions
- Maintain quarterly fairness audits
- Regular community engagement
- Iteration and improvement based on outcomes

---

### Values Prioritized in This Decision

**Values upheld by recommending Option B:**

- **Justice:** System prioritizes fairness outcomes over efficiency. Marginalized populations' interests are protected.
- **Autonomy:** Applicants retain voice in decisions affecting their lives.
- **Dignity:** People are treated as full human beings, not data profiles.
- **Responsibility:** Agencies and case workers are accountable for decisions and can articulate reasoning.
- **Trust:** Human engagement and fair treatment preserve and rebuild public trust.
- **Well-being:** Fairer outcomes mean eligible people receive support they need; fewer people are wrongly denied.

**Values traded off:**

- **Organizational efficiency:** Option B costs more and serves fewer additional applicants than Option A.
- **Consistency (in process):** Different case workers may make different decisions, though fairness should be consistent.

**The fundamental premise:** Serving vulnerable people fairly is worth more than administrative efficiency and cost savings. Government agencies exist to serve all people, not just those with the resources to navigate opaque systems. When efficiency and fairness conflict, fairness takes precedence.

---

## Summary: Key Findings and Commitments

### What this assessment reveals:

1. **Both options carry significant ethical risks without mitigation.** Neither can be deployed as-is.

2. **The core ethical issue is fairness and accountability.** The system will embed and amplify bias if not actively prevented. This harms the people it claims to serve.

3. **Option A maximizes efficiency at the cost of fairness.** It works well for eligible applicants with resources to navigate the system, but harms marginalized applicants and erodes public trust.

4. **Option B sacrifices some efficiency for fairness and accountability.** It retains human judgment, which allows correction of algorithmic bias and preservation of applicant agency.

5. **Option B is ethically superior, but only if implemented with rigor.** Case workers must genuinely review rather than default to the AI. Training and monitoring must be sustained. Community oversight must be real.

6. **The true cost of automation is not captured in efficiency metrics.** Legal liability, reputational damage, loss of institutional knowledge, and erosion of public trust are real costs that offset savings.

### What must be true for either option to proceed:

1. **Bias audit is completed and results are acted upon.** Training data must be examined for bias, and the model must be retrained on corrected historical decisions.

2. **Fairness testing is conducted and publicly disclosed.** System performance must be measured by demographic group. If significant disparities are found, deployment must be paused.

3. **Transparency is built into every step.** Applicants must understand how decisions are made and have clear ways to contest them.

4. **Appeals are fully accessible and resourced.** Free, in-person and remote, in multiple languages, with real human review and decision-making authority.

5. **Ongoing monitoring is mandated.** Fairness outcomes are tracked, independently audited, and reported publicly.

6. **Community oversight is real.** Communities affected by the system have meaningful voice in design, deployment, and iteration.

7. **Accountability is clear.** Agencies must be able to articulate how decisions were made and must take responsibility for errors.

### What will determine success or failure:

**Not the choice between Option A and B alone, but the implementation of safeguards.** A poorly executed Option B (with automation bias, insufficient training, inadequate appeals) could be worse than a well-executed Option A (with rigorous fairness testing, strong bias mitigation, free appeals).

However, **we believe Option B, well-executed, is the only ethically defensible path forward.** It preserves human judgment and applicant agency in a system that will directly affect the survival and dignity of vulnerable people.

---

## Conclusion

This assessment does not tell you what to do. That is your responsibility as leaders in these agencies. What it does is make visible the values at stake, the harms that could occur, and the conditions that must be met for either option to be ethically acceptable.

The choice between Option A and Option B is not primarily a technical choice or an efficiency choice. It is a **values choice**:

- Option A says: Speed and cost-efficiency matter most; we'll manage fairness risks through appeals.
- Option B says: Fairness and applicant dignity matter most; we'll accept slower processing and higher costs to protect vulnerable people.

Only you can decide which values your agency will prioritize. But decide consciously, knowing what you are accepting and what you are trading away.

Whatever you choose, the mandatory safeguards outlined in this assessment (bias audits, fairness testing, transparency, accessible appeals, ongoing monitoring, community oversight) are non-negotiable. Without them, neither option is ethically acceptable.

The people who depend on these benefits—people experiencing homelessness, families in crisis, workers who've lost jobs—deserve that you get this right.

---

## Values Prioritized Across the Chain

**Most significant values:**

| Value | Role in Assessment | Priority Ranking |
|-------|-------------------|-----------------|
| **Justice** | Central throughout. Core fairness concern. Threatened by bias amplification. | **Critical** — determines whether system harms or helps vulnerable populations |
| **Autonomy** | Central throughout. Applicants' ability to understand and contest decisions. Threatened by opacity and automation bias. | **Critical** — determines whether people retain agency in their own lives |
| **Dignity** | Central throughout. Whether people are treated as full humans or data profiles. Threatened by algorithmic reduction. | **Critical** — foundational to respectful treatment of all people |
| **Responsibility** | Central in evaluation. Agencies' ability to account for decisions and mitigate harms. Threatened by opaque systems. | **Critical** — determines whether agencies can be held accountable |
| **Trust** | Outcome of other values. If system is fair, transparent, and accountable, trust is preserved. If not, eroded. | **Very Important** — foundation for voluntary compliance and social cohesion |
| **Well-being** | Immediate impact. Eligible people benefit (access to support sooner); wrongly denied people are harmed. | **Very Important** — direct impact on survival and flourishing |
| **Privacy** | Risk throughout. Sensitive data collection and exposure. | **Important** — must be protected as a condition of deployment |
| **Relationships** | Threatened by automation of human service. Case worker-applicant relationships can support or be replaced by algorithms. | **Important** — human connection is valuable in itself |

**Trade-offs made:**

1. **Fairness over Efficiency:** Option B recommends prioritizing fair outcomes (Justice, Dignity, Autonomy) over cost savings and speed (organizational efficiency).

2. **Accountability over Consistency:** Recommends human judgment and accountability over uniform algorithmic consistency, because fairness sometimes requires case-by-case judgment.

3. **Preservation of Human Agency over Organizational Convenience:** Recommends preserving applicant voice and understanding (Autonomy, Dignity) even though algorithmic systems are more convenient for organizations to operate.

4. **Trust-Building over Rapid Deployment:** Recommends investing time in fairness testing, community engagement, and case worker training (building Trust) even though these slow down deployment.

---

**Assessment completed:** 2026-05-06  
**Prepared by:** Stanford Ethics Toolkit Framework Analysis  
**Confidence level:** High (assessment is thorough and grounded in ethical frameworks and evidence about algorithmic systems)  
**Recommended next step:** Agency leadership decision on which option to pursue, conditional on implementation of mandatory safeguards outlined above.

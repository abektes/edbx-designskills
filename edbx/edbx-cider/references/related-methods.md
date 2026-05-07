# CIDER — Related Methods and Integration

Methods that complement, extend, or connect to CIDER within the Ethical Design Package and beyond.

---

## Methods Within the EDB Toolkit

### edb-anotherlens

**What it does:** Surfaces the designer's own worldview — their biases, values, and blind spots — as a lens through which design decisions get made.

**How it connects to CIDER:** Anotherlens works upstream of CIDER. Before you can surface assumptions about users, it helps to understand the worldview you are bringing to the design. Anotherlens reveals the designer; CIDER reveals the design. Use Anotherlens first to establish self-awareness, then CIDER to find specific assumptions embedded in the artifact.

**Combined workflow:** Run Anotherlens to identify the designer's worldview. Then run CIDER on the design artifact. Compare: did the designer's worldview blind them to certain categories of assumptions? Often, a designer who values efficiency will miss capacity assumptions. A designer who values aesthetics will miss environment assumptions. The comparison is revealing.

---

### edb-humane-design-guide

**What it does:** Audits whether a design exploits human sensitivities — fear, urgency, social pressure, scarcity — to drive behavior.

**How it connects to CIDER:** Humane Design Guide asks "is this design manipulating people?" CIDER asks "is this design excluding people?" Together they cover two major ethical dimensions: harm to people who can use the design, and harm to people who cannot.

**Combined workflow:** Run CIDER first to identify who is excluded and how. Then run Humane Design Guide on what remains — the design as experienced by the people who *can* use it. Are they being manipulated? The two audits together give a fuller picture of ethical design quality.

---

### edb-worrystorming

**What it does:** Generates a broad landscape of ethical worries about a design through structured, generative anxiety.

**How it connects to CIDER:** Worrystorming casts a wide net — anything that could go wrong, ethically. CIDER focuses specifically on exclusion-causing assumptions. Worrystorming produces volume; CIDER produces specificity. Use Worrystorming first to map the terrain, then CIDER to dig into the exclusion-related worries.

**Combined workflow:** Run Worrystorming and collect all worries. Filter for worries related to exclusion or access. Feed those filtered worries into CIDER's Stage C as starting assumptions. This combination produces both breadth (Worrystorming) and depth (CIDER).

---

### edb-responsible-design-prism

**What it does:** Places a design on a spectrum from irresponsible to responsible across multiple ethical dimensions.

**How it connects to CIDER:** The Prism evaluates where a design falls. CIDER generates specific actions to move it toward the responsible end. Use the Prism first to assess the current state, then CIDER to generate redesign proposals that address the specific exclusion problems the Prism reveals.

**Combined workflow:** Run the Prism to identify which dimensions score lowest. Run CIDER with those low-scoring dimensions in mind. The CIDER redesign proposals become concrete actions to improve the Prism score.

---

### edb-motivation-matrix

**What it does:** Maps why users participate in a design — their motivations, incentives, and emotional drivers.

**How it connects to CIDER:** Motivation Matrix assumes people *can* participate and asks *why* they do. CIDER asks who *cannot* participate at all — who is structurally excluded before motivation even matters. Together they answer: who shows up (Motivation Matrix), who cannot show up (CIDER), and what happens to both groups once they are in the design (Humane Design Guide).

**Combined workflow:** Run CIDER first to identify who is excluded. Then run Motivation Matrix on the included population. The gap between "who the design is for" and "who can actually use it" becomes visible.

---

## External Methods

### GenderMag

**What it does:** A method for finding gender-inclusivity bugs in software. Uses faceted personas (Abi, Tim, Pat, Patrick) to evaluate whether a design supports different problem-solving styles and motivations that correlate with gender.

**How it connects to CIDER:** GenderMag and CIDER share a common intellectual ancestor — both are about finding assumptions in design that exclude people. GenderMag focuses specifically on gender-related exclusion. CIDER is broader (any assumption category) but can be used to dig deeper on gender assumptions in Stage I.

**Academic connection:** Both methods emerged from the inclusive design research community. The CIDER authors cite GenderMag as foundational work.

**For further reading:** Burnett, M., et al. (2016). GenderMag: A method for evaluating software's gender inclusiveness. *Interacting with Computers.*

---

### Inclusive Activity Cards

**What it does:** A card-based activity that helps designers think about who might be excluded from a design activity and how to include them.

**How it connects to CIDER:** Inclusive Activity Cards are a lighter-weight, more portable version of the same underlying practice. Use them for quick exercises or as warm-ups before a full CIDER session.

---

### Inclusive Design Principles (Microsoft)

**What it does:** Three principles — Recognize Exclusion, Solve for One / Extend to Many, Learn from Diversity — that frame inclusive design as a design philosophy.

**How it connects to CIDER:** CIDER is a method for operationalizing the first principle ("Recognize Exclusion"). The Microsoft principles provide the philosophical frame; CIDER provides the practical technique.

**For further reading:** Microsoft Inclusive Design methodology kit. Available at microsoft.com/design/inclusive.

---

### Value Sensitive Design (VSD)

**What it does:** A theoretically grounded approach to designing technology that accounts for human values in a principled manner throughout the design process.

**How it connects to CIDER:** VSD is broader — it addresses all human values (privacy, autonomy, fairness, etc.). CIDER focuses specifically on the value of inclusion. CIDER can be used as a VSD investigation method when the value under investigation is inclusivity or equity.

**For further reading:** Friedman, B., Hendry, D. (2019). *Value Sensitive Design: Shaping Technology with Moral Imagination.* MIT Press.

---

### Ability-Based Design

**What it does:** A design paradigm that asks not "what can the user do?" but "what abilities are required by the system?" — and then redesigns the system to require fewer specific abilities.

**How it connects to CIDER:** Ability-Based Design is the theoretical foundation for CIDER's Ability category. CIDER extends the same logic to Capacity, Environment, and Resources.

**For further reading:** Wobbrock, J., Gajos, K., Kane, S., Vanderheiden, G. (2018). Ability-based design. *Communications of the ACM.*

---

## Recommended Sequences

### Full Inclusive Design Audit

1. **edb-anotherlens** — Understand your worldview
2. **CIDER** — Surface assumptions, imagine exclusion, design alternatives
3. **edb-responsible-design-prism** — Score the redesign on the ethical spectrum
4. **edb-humane-design-guide** — Check that the redesign does not exploit the people it now includes

### Quick Inclusion Check

1. **CIDER (Stages C + I + D only)** — 30-minute solo exercise
2. Review findings and commit to one redesign

### Team Inclusion Workshop

1. **edb-anotherlens** (individual) — Each team member reflects on their worldview
2. **CIDER (full 5 stages)** — Team session with shared Expand register
3. **edb-motivation-matrix** — Map motivations for the now-more-inclusive design
4. Commit to the Inclusive Design Commitment from CIDER Stage R

### Ethical Design Sprint

1. **edb-worrystorming** — Generate broad ethical worries
2. **CIDER** — Focus on exclusion-related worries
3. **edb-responsible-design-prism** — Evaluate current state
4. **edb-humane-design-guide** — Ensure redesign is not manipulative
5. Implement top redesign proposals

# 14 — Experiments

Two pre-registered experiments anchor the dissertation. The prototype
delivers an end-to-end version of Experiment 1 with a single transfer
task; Experiment 2 is implemented in Year 2.

## Experiment 1 — Immediate belief change

**Question.** How do **text features** (POV, vividness, realism,
conflict intensity, moral explicitness) and **reader traits**
(transportability, empathy, NFA, NFC) interact to predict immediate
belief change on a moral dilemma?

**Design.** Factorial:

- Texts that vary in POV, realism, conflict, moral explicitness.
- Agents with trait profiles drawn from theory-constrained ranges.
- Plus a **non-narrative control passage** (factual prose) and a
  **no-story baseline**.

**Outcome measures.** Pre/post `delta_choice`, `delta_confidence`,
`justification_similarity`. Mediator: SWAS scores.

**Hypotheses.**

- H1: High-transportability agents shift more on vivid first-person
  narratives than on flat third-person narratives.
- H2: High-NFC agents are less moved by emotional appeals and more
  responsive to explicit moral framing.
- H3: Non-narrative control produces smaller transfer than narrative
  even when the explicit moral content is matched.

**Configs.** `experiments/exp01_*/config.yaml` and
`configs/prototype.yaml` (for the 3-month subset).

## Experiment 2 — Moral generalization and sleeper effect

**Question.** Does narrative-induced moral shift **generalize** to
new dilemmas, and does it **persist or grow** as source memory fades?

**Design.** Two phases:

- *Generalization*: same agents read a story and answer dilemmas at
  varying foundation distance from the source.
- *Sleeper*: a delayed re-test where source memory is artificially
  weakened (memory-decay manipulation in the agent), but semantic
  content is retained.

**Outcome measures.** Same as Experiment 1, plus
`delta_over_delay = post_delay - post_immediate`.

**Hypotheses.**

- H4: Effects are larger on dilemmas that share foundation profile
  with the source than on unmatched dilemmas.
- H5: Belief shift on matched dilemmas does *not* decay (and may grow)
  as source memory weakens — a computational analog of the sleeper
  effect.

## Negative controls

Each experiment includes:

- A **non-narrative control** (factual prose) with the same explicit
  moral, to separate "narrative-induced" from "argument-induced"
  transfer.
- A **no-story baseline** (agents answer the post-test cold) to
  bound retest effects.

## Open questions

- _Single dilemma or battery?_ Battery for Experiment 2; single for the
  prototype demo.
- _Where does the resistance-to-persuasion / counter-narrative arm
  live — in Experiment 2 or a third experiment in Year 3?_

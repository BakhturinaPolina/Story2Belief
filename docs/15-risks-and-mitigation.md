# 15 — Risks and mitigation

## R1 — LLMs are not human subjects

**Risk.** AI readers are not approximations of any specific population.
Treating their outputs as proxies for human responses would be invalid.

**Mitigation.** We frame AI readers as **theory-informed simulation
instruments** whose outputs must be validated against published
empirical regularities and stress-tested under multiple prompting
conditions (prompt variants, temperature sweeps, model swaps).

## R2 — Construct inflation

**Risk.** Loading too many loosely defined variables (a dozen reader
traits, dozens of feature families) makes the model unwieldy and
underpowered.

**Mitigation.** Split traits into **core** and **secondary** sets (see
[`09-reader-trait-schema.md`](09-reader-trait-schema.md)). The 3-month
prototype uses core traits only. Adding a trait requires a citation in
`docs/12-tools-and-resources.md` and a schema migration entry in
`CHANGELOG.md`.

## R3 — Moral ambiguity

**Risk.** Stories often contain irony, competing normative frames, and
multiple plausible morals. Forcing a single moral label is methodologically
wrong.

**Mitigation.** The schema allows **multiple candidate morals** with
confidence and ambiguity scores (see
[`08-narrative-feature-schema.md`](08-narrative-feature-schema.md)). The
moral-extraction prompt explicitly asks for alternatives.

## R4 — Computational cost

**Risk.** Long-form longitudinal simulations with large cohorts can blow
up runtime and budget.

**Mitigation.** Prototype: 2 short texts × ≤50 readers × 1 transfer task.
Scaling decisions defer to Year 2, after the prototype validates the
pipeline.

## R5 — Tool-integration drift

**Risk.** External tools (BookNLP, Concordia, MoralBERT, SentiArt) are
maintained by other teams; APIs and behavior may shift.

**Mitigation.** Pin versions in `pyproject.toml`. Wrappers in
`src/story2belief/` isolate external APIs behind narrow interfaces so
that swapping a tool only touches one module.

## R6 — Ethical risk in source-material choice

**Risk.** The dissertation context (Russian patriotic education,
indoctrination) is ethically and politically loaded. Misuse of the
methodology is conceivable.

**Mitigation.** See
[`16-ethics-and-positionality.md`](16-ethics-and-positionality.md).

## Open questions

- _Do we need a formal preregistration_ for Experiment 1, even at the
  prototype stage? Probably yes — light-weight via OSF.

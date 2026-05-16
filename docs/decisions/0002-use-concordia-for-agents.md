# ADR 0002 — Use Concordia for AI-reader agents

- **Status**: Tentative (2026-05-16)
- **Context**: Layer 2 simulates a population of readers with memory,
  reflection, and individual differences. Building this from scratch
  duplicates work already done in
  [Concordia](https://github.com/google-deepmind/concordia).
- **Decision**: Plan to use Concordia for the reader agents from W6 of
  the prototype onward. Until then, Layer 2 is implemented as a thinner
  prompt-loop with a `ReaderProfile`-driven system prompt and short-term
  memory in the prompt context.
- **Consequences**:
  - Reader agents inherit a maintained memory + reflection abstraction.
  - Concordia's API surface becomes a project dependency; wrappers in
    `readers/agent.py` keep that surface narrow.
  - If Concordia onboarding is too slow, fallback (thin prompt loop)
    remains usable for the prototype demo.
- **Alternatives considered**: LangGraph (less psych-oriented), bespoke
  agent loop (more control, more code).

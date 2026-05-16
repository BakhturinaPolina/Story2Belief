# ADR 0003 — Use SWAS as the AI-reader self-report layer

- **Status**: Accepted (2026-05-16)
- **Context**: The project needs a reading-experience layer that sits
  between text input and belief output. Inventing a new instrument would
  weaken the methodological argument; aligning with the Story World
  Absorption Scale (Kuijpers et al.) ties our outputs to a validated
  human-reading instrument.
- **Decision**: Use SWAS's four dimensions (attention, emotional
  engagement, mental imagery, transportation) as the structural basis
  for the agent self-report, with two added fields:
  *character alignment* (per-character) and *moral-uptake confidence*.
- **Consequences**:
  - Agent outputs are interpretable and comparable to human SWAS data
    qualitatively.
  - We commit to citing the SWAS resource page in any paper using the
    adapted scale (free for research use with citation).
  - Implementation follows `docs/07-swas-adaptation.md`.
- **Alternatives considered**: Building a bespoke 6-item reading scale
  (cheaper, but methodologically weaker); using only free-text
  reflection (harder to compare across agents).

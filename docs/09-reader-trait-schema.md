# 09 — Reader trait schema

The canonical schema lives in `src/story2belief/readers/profile.py`.

## Core traits (prototype)

| Trait | Range | Source |
|-------|-------|--------|
| `transportability` | 0–10 | Mazzocco et al. |
| `empathy` (trait) | 0–10 | IRI / perspective-taking literature |
| `need_for_affect` | 0–10 | Maio & Esses |
| `need_for_cognition` | 0–10 | Cacioppo & Petty |
| `reading_exposure` | 0–10 | Author Recognition Test family |
| `theme_relevance` | 0–10 | per-text (set at runtime) |
| `realism_preference` | 0–10 | self-reported |
| `baseline_moral_foundation_scores` | dict[5] of 0–10 | MFQ-style |
| `source_memory_decay` | 0–1 | sleeper-effect parameter |

## Secondary traits (Year 1+)

- Personal experience relevance to the story theme.
- Genre familiarity.
- Social conformity orientation.
- Skepticism / resistance to persuasion (separate from need-for-cognition).
- Demographic similarity slots (age, gender, occupation, value).

## Encoding choice

For the prototype, all traits are **0–10 floats** rather than empirically
calibrated distributions. This is *theory-constrained synthetic
initialization*: we do not claim to mirror a real population, only to
demonstrate model tractability and causal structure.

## Sampling

`readers/cohort.py` samples from theory-constrained ranges (e.g., empathy
∈ [2, 8] with a mean of 5.5 and σ=1.5), and ensures coverage of extreme
contrasts (high transportability + low NFC vs. its mirror) so that
trait-driven differences are visible at small N.

## Open questions

- _Should `baseline_moral_foundation_scores` be drawn jointly (clusters of
  liberal / conservative profiles) or independently?_
- _How do we represent the "Russian patriotic education" scenario in the
  trait schema for later years — as a covariate, a bias on baseline
  foundations, or a separate context object?_

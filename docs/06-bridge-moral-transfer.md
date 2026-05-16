# 06 — Moral-transfer bridge (Layer 3)

The bridge is the **conceptual heart** of the project: it operationalizes
the claim that a narrative changes how an agent reasons about *new* moral
situations, not just whether the agent remembers the story.

## Operationalization

For each (text × reader) pair:

1. Extract one or more **moral propositions** from the text (Layer 1).
2. Map each proposition onto a moral-foundation profile (MoralBERT or
   a structured codebook).
3. Pick a **post-reading dilemma** that is *textually dissimilar* from the
   source text but *morally proximate* (similar foundation profile,
   different surface). See
   [`10-dilemma-design.md`](10-dilemma-design.md).
4. Have the reader-agent answer the dilemma both **before** reading
   (baseline) and **after** reading.

## Transfer outputs

For each agent and dilemma, compute:

- `delta_choice` — change in chosen option (categorical).
- `delta_confidence` — change in stated confidence (signed real).
- `justification_similarity` — cosine similarity between the embedding of
  the agent's post-reading justification and the embedding of the story's
  extracted moral.

The third measure is the formal answer to the original "vector-space"
intuition: it makes "the agent now reasons more like the story would
recommend" computable.

## Why this design

- It rules out **mere recall**: the post-reading dilemma is a different
  story, so the agent cannot simply repeat the source.
- It supports the **sleeper-effect** investigation: by running a delayed
  re-test where source memory has decayed, we can see whether the
  semanticized moral content persists.
- It connects literary features (Layer 1) to morally-relevant behavior
  (Layer 3) through a measurable mediator (Layer 2 SWAS).

## Modules

| Module | File | Status |
|--------|------|--------|
| Dilemma loaders | `bridge/dilemmas.py` | placeholder |
| Moral-foundation scorer | `bridge/moral_foundations.py` | placeholder (MoralBERT) |
| Justification similarity | `bridge/similarity.py` | placeholder |
| Transfer metrics | `bridge/transfer.py` | placeholder |

## Open questions

- _How to choose "morally proximate but textually dissimilar"
  dilemmas?_ Likely: matched foundation distribution + low TF-IDF / dense
  similarity to source.
- _How to handle multiple candidate morals per text?_ Aggregate at the
  foundation level rather than at the proposition level.

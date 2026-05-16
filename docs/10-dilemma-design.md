# 10 — Dilemma design

The post-reading dilemma is the *probe* through which we measure moral
transfer. It must satisfy two properties at the same time:

1. **Surface-dissimilar** to the source story (different characters,
   setting, plot) so that high performance cannot be explained by recall.
2. **Morally-proximate** to the source story (similar foundation
   distribution) so that any transfer effect is directionally
   interpretable.

## Construction recipe

For each (text, agent) pair:

1. Extract candidate **moral propositions** from the text (Layer 1).
2. Convert them to a foundation profile via MoralBERT or a structured
   codebook.
3. From the dilemma corpus (MoralStory / Moral Stories / STORAL), pick
   dilemmas whose foundation profile has high cosine similarity to the
   source, **and** whose surface text has low embedding similarity to
   the source.
4. Filter by length and complexity to keep agent reasoning tractable.

## Pre-test / post-test pairing

- The pre-test dilemma is presented to the agent **before reading**, with
  a fresh context. The agent provides: chosen option, confidence (0–10),
  free-text justification.
- The post-test dilemma is **distinct from the pre-test** but matched on
  foundation profile, so we can attribute any change to the reading
  experience rather than to retest effects.
- Output fields recorded in `data/processed/dilemma_responses/`.

## Why we don't reuse the source's exact dilemma

If the post-test dilemma were trivially similar to the source, the
exercise would measure recall, not transfer. The whole point of the
project is to model *generalization* of moral attitudes.

## Open questions

- _Is one transfer task per agent enough for the prototype?_ Probably yes
  — but Year 2 should run multi-task batteries to estimate stability.
- _Do we need a non-narrative control (e.g. an essay arguing the same
  moral) to separate "narrative-induced" from "argument-induced"
  transfer?_ Yes — see [`14-experiments.md`](14-experiments.md).

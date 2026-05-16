<!--
prompt_id: moral_extraction.v0
purpose: Extract candidate moral propositions from a narrative (Hobson-style).
inputs:
  - text (str): full story text
  - text_id (str)
outputs (JSON):
  - propositions: [{text, foundations{...}, confidence, ambiguity}]
  - behavioral_lessons: [str]
written_for: gpt-4o-class models with JSON mode, temperature=0
-->

# Moral-extraction prompt (v0) -- placeholder

Stage 1: summary.
Stage 2: list protagonists and their goals.
Stage 3: emotional tone.
Stage 4: candidate morals (allow multiple, with confidence + ambiguity).
Stage 5: behavioral lessons.

Replace this with the full chained prompt body when wiring up Layer 1.

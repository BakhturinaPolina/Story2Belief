<!--
prompt_id: swas_self_report.v0
purpose: Elicit adapted SWAS self-report from a reader-agent after reading.
inputs:
  - reader_profile (json) - serialized ReaderProfile
  - text (str) - the story (or its summary + key passages)
  - text_id (str)
outputs (JSON, must validate against readers.profile.SwasResponse):
  - attention, emotional_engagement, mental_imagery, transportation (0-10)
  - character_alignment: {character_name -> -10..10}
  - moral_uptake_confidence (0-10)
written_for: gpt-4o-class models with JSON mode, temperature=0
notes:
  - Cite SWAS (Kuijpers et al.) when publishing outputs.
  - Do NOT redistribute the original SWAS items in this file.
-->

# SWAS self-report prompt (v0) -- placeholder

Replace this with the adapted SWAS-style prompt body when wiring up Layer 2.

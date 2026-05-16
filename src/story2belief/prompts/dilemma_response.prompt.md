<!--
prompt_id: dilemma_response.v0
purpose: Elicit a structured response to a single moral dilemma.
inputs:
  - reader_profile (json) - serialized ReaderProfile
  - dilemma (json) - serialized Dilemma (text + options)
  - phase (str) - "pre" or "post"
outputs (JSON, must validate against bridge.transfer.DilemmaResponse):
  - chosen_option (str)
  - confidence (0-10)
  - justification (str)
written_for: gpt-4o-class models with JSON mode, temperature=0
-->

# Dilemma-response prompt (v0) -- placeholder

Replace this with the dilemma-response prompt body when wiring up Layer 3.

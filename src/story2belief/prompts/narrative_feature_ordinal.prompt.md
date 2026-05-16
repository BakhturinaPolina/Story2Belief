<!--
prompt_id: narrative_feature_ordinal.v0
purpose: Score one narrative/discourse feature in a passage on a 0/1/2 ordinal scale.
inputs:
  - passage (str): story passage text
  - feature_statement (str): one feature statement from configs/narrative_discourse_features.yaml
outputs:
  - single token / number: 0, 1, or 2
written_for: gpt-4o-class models, temperature=0
source:
  - "Narrative-Discourse paper, reusable prompt frame + Table 1 feature statements"
-->

# Narrative-feature ordinal prompt (v0)

Today, you are an expert story interpreter.
I will give you a passage from a story and ask you a question about it.
Here is a passage: {passage}
Can you tell me if the following feature is present?
{feature_statement}
Answer only with a number where 2=strongly present, 1=weakly present, or 0=not present.

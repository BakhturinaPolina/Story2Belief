<!--
prompt_id: narrative_feature_ordinal.v1
purpose: >-
  Score one narrative/discourse feature in a passage on a 0/1/2 ordinal
  scale, AND return a verbatim evidence span supporting the rating.
  Replaces v0 (number-only output) so that each rating ships with
  source-grounded evidence consistent with the rest of Layer 1.
inputs:
  - passage (str): story passage text
  - feature_statement (str): one feature statement from
    configs/narrative_discourse_features.yaml
outputs (JSON):
  - rating (int): 0, 1, or 2
  - evidence_span (str): verbatim substring of `passage` that supports the
    rating. Empty string when rating == 0.
written_for: gpt-4o-class models with JSON mode, temperature=0
source:
  - Narrative-Discourse paper (Piper & Bagga lineage), reusable prompt
    frame + Table 1 feature statements.
notes:
  - When called inside the langextract orchestration, the evidence_span
    is realigned to a char_interval by the caller for consistency with
    the other Layer-1 extractions.
-->

# Narrative-feature ordinal prompt (v1)

Today, you are an expert story interpreter.
I will give you a passage from a story and ask you a question about it.

Here is a passage:

{passage}

Can you tell me if the following feature is present?

{feature_statement}

Reply with a single JSON object of the form:

```json
{
  "rating": 0,
  "evidence_span": ""
}
```

Use `rating = 2` if the feature is **strongly present**, `1` if it is
**weakly present**, or `0` if it is **not present**.

When `rating > 0`, set `evidence_span` to a verbatim substring of the
passage that supports the rating. When `rating == 0`, set
`evidence_span` to an empty string.

Output only the JSON object.

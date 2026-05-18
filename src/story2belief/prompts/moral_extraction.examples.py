"""Few-shot exemplars for the moral-extraction prompt.

These are passed to ``langextract.extract(...)`` as ``examples``. Each
``ExampleData`` instance pairs verbatim source text with the target
extractions; ``langextract`` then enforces this schema on the test text
via controlled generation (Gemini) or JSON mode (OpenAI).

Convention (per the langextract README):
    - Use **verbatim** spans from the example text for ``extraction_text``.
    - Order extractions by appearance in the text.
    - Filter results in the caller with
      ``[e for e in result.extractions if e.char_interval]`` to drop
      ungrounded extractions that leak from these examples.

See ``prompts/moral_extraction.prompt.md`` for the prompt description.
"""

from __future__ import annotations

try:
    import langextract as lx
except ImportError:  # pragma: no cover - langextract is an optional dep.
    lx = None  # type: ignore[assignment]


def _build_examples() -> list:
    """Return the moral-extraction ExampleData list.

    Returns
    -------
    list[langextract.data.ExampleData]
        Exemplars covering: a care/harm moral with low ambiguity, a
        loyalty/authority moral with moderate ambiguity, and a
        behavioral lesson + value judgment combination.
    """
    if lx is None:
        return []

    return [
        lx.data.ExampleData(
            text=(
                "The wolf swallowed Little Red Riding Hood whole. "
                "Her mother had warned her not to stray from the path, "
                "but the flowers had been so pretty. "
                "When the woodsman finally cut her free, she resolved "
                "never to disobey again."
            ),
            extractions=[
                lx.data.Extraction(
                    extraction_class="moral_proposition",
                    extraction_text="she resolved never to disobey again",
                    attributes={
                        "proposition": "Disobeying parental warnings leads to harm.",
                        "foundations": {
                            "care_harm": 7.0,
                            "fairness_cheating": 0.0,
                            "loyalty_betrayal": 2.0,
                            "authority_subversion": 8.0,
                            "sanctity_degradation": 0.0,
                        },
                        "confidence": 8.0,
                        "ambiguity": 2.0,
                    },
                ),
                lx.data.Extraction(
                    extraction_class="behavioral_lesson",
                    extraction_text="not to stray from the path",
                    attributes={
                        "lesson": "If you stray from the path, harm follows.",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="mft_evidence",
                    extraction_text="The wolf swallowed Little Red Riding Hood whole.",
                    attributes={
                        "foundation": "care_harm",
                        "polarity": "violate",
                    },
                ),
            ],
        ),
        lx.data.ExampleData(
            text=(
                "Anna knew the truth would shatter her father. "
                "Still, she chose to stay silent at the dinner table, "
                "telling herself that some loyalties weigh more than honesty."
            ),
            extractions=[
                lx.data.Extraction(
                    extraction_class="moral_proposition",
                    extraction_text=(
                        "telling herself that some loyalties weigh more than honesty"
                    ),
                    attributes={
                        "proposition": "Loyalty to family can outweigh the duty of truthfulness.",
                        "foundations": {
                            "care_harm": 4.0,
                            "fairness_cheating": 5.0,
                            "loyalty_betrayal": 8.0,
                            "authority_subversion": 2.0,
                            "sanctity_degradation": 0.0,
                        },
                        "confidence": 6.0,
                        "ambiguity": 7.0,
                    },
                ),
                lx.data.Extraction(
                    extraction_class="value_judgment",
                    extraction_text="some loyalties weigh more than honesty",
                    attributes={
                        "valence": "endorse",
                        "target_value": "loyalty",
                    },
                ),
            ],
        ),
    ]


#: Lazily-built ExampleData list. Empty if langextract is not installed,
#: which lets the calling code import this module without taking the
#: optional ``nlp`` extra.
MORAL_EXTRACTION_EXAMPLES = _build_examples()

"""Schema for an AI-reader profile.

This is the canonical data contract that drives Layer 2. Update
``docs/09-reader-trait-schema.md`` whenever this file changes.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from story2belief.narrative.schema import FoundationDistribution

#: Pseudo-Big5 tuple: (Openness, Conscientiousness, Extraversion, Agreeableness,
#: Neuroticism). Each component is a 0-10 float. Sampled independently of the
#: other trait fields for the prototype (see ``docs/09-reader-trait-schema.md``).
PseudoBig5 = tuple[float, float, float, float, float]


@dataclass(frozen=True, slots=True)
class ReaderProfile:
    """A single AI-reader profile.

    All trait scores are floats in [0, 10] unless otherwise documented.
    Values are theory-constrained synthetic samples, not empirically
    calibrated population estimates.

    Trait set distilled from van Laer et al. (2014), Mazzocco et al. (2010),
    Appel & Richter (2010), Zwarun & Hall (2012), Thompson et al. (2018),
    and Cohen et al. (2018). See ``docs/09-reader-trait-schema.md``.
    """

    reader_id: str

    transportability: float = 5.0
    empathy: float = 5.0
    need_for_affect: float = 5.0
    need_for_cognition: float = 5.0
    sensation_seeking: float = 5.0
    prior_familiarity: float = 5.0
    reading_exposure: float = 5.0

    baseline_moral_foundation_scores: FoundationDistribution = field(
        default_factory=FoundationDistribution
    )

    #: Pseudo-Big5 OCEAN tuple. Drives reader-character cosine similarity at
    #: read-time. Not a validated personality measurement; see
    #: ``docs/09-reader-trait-schema.md`` for the deliberate independence
    #: choice.
    pseudo_big5: PseudoBig5 = (5.0, 5.0, 5.0, 5.0, 5.0)

    source_memory_decay: float = 0.0


@dataclass(frozen=True, slots=True)
class SwasResponse:
    """Adapted SWAS self-report.

    Four original SWAS dimensions plus three Story2Belief-specific fields.
    Item text is loaded from ``configs/instruments/swas.yaml``. See
    ``docs/07-swas-adaptation.md``.
    """

    attention: float = 0.0
    emotional_engagement: float = 0.0
    mental_imagery: float = 0.0
    transportation: float = 0.0
    character_alignment: dict[str, float] = field(default_factory=dict)
    moral_uptake_confidence: float = 0.0

    #: Per-character cosine similarity between reader and character pseudo-Big5.
    #: Keys match character names in the corresponding ``NarrativeFeatures``.
    character_similarity: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ReadingResponse:
    """Output of one reader-agent reading one text."""

    reader_id: str
    text_id: str
    interpretation: str
    swas: SwasResponse = field(default_factory=SwasResponse)
    verbalized_moral: str = ""

    #: One-item agent-elicited rating of perceived similarity to the protagonist
    #: (Ooms et al. 2019). 0-10. See ``docs/09-reader-trait-schema.md``.
    perceived_similarity: float = 0.0

    #: One-item agent-elicited rating of self-referencing during reading
    #: (de Graaf 2014). 0-10.
    self_referencing: float = 0.0

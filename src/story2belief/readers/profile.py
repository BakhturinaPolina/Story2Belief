"""Schema for an AI-reader profile.

This is the canonical data contract that drives Layer 2. Update
``docs/09-reader-trait-schema.md`` whenever this file changes.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from story2belief.narrative.schema import FoundationDistribution


@dataclass(frozen=True, slots=True)
class ReaderProfile:
    """A single AI-reader profile.

    All trait scores are floats in [0, 10] unless otherwise documented.
    Values are theory-constrained synthetic samples, not empirically
    calibrated population estimates.
    """

    reader_id: str

    transportability: float = 5.0
    empathy: float = 5.0
    need_for_affect: float = 5.0
    need_for_cognition: float = 5.0
    reading_exposure: float = 5.0
    theme_relevance: float = 5.0
    realism_preference: float = 5.0

    baseline_moral_foundation_scores: FoundationDistribution = field(
        default_factory=FoundationDistribution
    )

    source_memory_decay: float = 0.0


@dataclass(frozen=True, slots=True)
class SwasResponse:
    """Adapted SWAS self-report.

    Four original SWAS dimensions plus two added fields. See
    ``docs/07-swas-adaptation.md``.
    """

    attention: float = 0.0
    emotional_engagement: float = 0.0
    mental_imagery: float = 0.0
    transportation: float = 0.0
    character_alignment: dict[str, float] = field(default_factory=dict)
    moral_uptake_confidence: float = 0.0


@dataclass(frozen=True, slots=True)
class ReadingResponse:
    """Output of one reader-agent reading one text."""

    reader_id: str
    text_id: str
    interpretation: str
    swas: SwasResponse = field(default_factory=SwasResponse)
    verbalized_moral: str = ""

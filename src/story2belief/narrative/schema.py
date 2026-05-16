"""Schema for the output of the narrative-analysis pipeline.

This is the canonical data contract between Layer 1 and Layers 2 and 3.
Update :doc:`docs/08-narrative-feature-schema.md` whenever this file changes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

PovType = Literal["first_person", "close_third", "omniscient", "multi_perspective"]


@dataclass(frozen=True, slots=True)
class CharacterAffect:
    """Reader-relevant affective stance toward a single character."""

    sympathy: float = 0.0
    compassion: float = 0.0
    empathy: float = 0.0
    perspective_taking: float = 0.0
    valence: float = 0.0


@dataclass(frozen=True, slots=True)
class CharacterLayer:
    """Character-level features extracted from a narrative."""

    count: int = 0
    protagonist: str = ""
    pov_type: PovType = "close_third"
    dialogue_share: float = 0.0
    salience: dict[str, float] = field(default_factory=dict)
    affect_map: dict[str, CharacterAffect] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class EventLayer:
    """Event-level features."""

    eventfulness: float = 0.0
    conflict_density: float = 0.0
    causal_clarity: float = 0.0
    temporal_linearity: float = 0.0
    narrative_distance: float = 0.0
    realism: float = 0.0


@dataclass(frozen=True, slots=True)
class StoryWorldLayer:
    """Story-world features."""

    concreteness: float = 0.0
    sensory_density: float = 0.0
    named_place_density: float = 0.0
    world_proximity: float = 0.0
    imagery_passages: int = 0


@dataclass(frozen=True, slots=True)
class FoundationDistribution:
    """Moral-foundations distribution for a single proposition or text."""

    care_harm: float = 0.0
    fairness_cheating: float = 0.0
    loyalty_betrayal: float = 0.0
    authority_subversion: float = 0.0
    sanctity_degradation: float = 0.0


@dataclass(frozen=True, slots=True)
class MoralProposition:
    """One candidate moral proposition extracted from a text."""

    text: str
    foundations: FoundationDistribution = field(default_factory=FoundationDistribution)
    confidence: float = 0.0
    ambiguity: float = 0.0


@dataclass(frozen=True, slots=True)
class MoralLayer:
    """Moral-level features."""

    propositions: tuple[MoralProposition, ...] = ()
    behavioral_lessons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Provenance:
    """Reproducibility metadata attached to every record."""

    prompt_versions: dict[str, str] = field(default_factory=dict)
    tool_versions: dict[str, str] = field(default_factory=dict)
    model_id: str = ""
    git_sha: str = ""
    created_at: str = ""


@dataclass(frozen=True, slots=True)
class NarrativeFeatures:
    """Top-level structured representation of a single narrative.

    See ``docs/08-narrative-feature-schema.md`` for the JSON shape.
    """

    text_id: str
    title: str
    genre: str
    language: str
    character: CharacterLayer = field(default_factory=CharacterLayer)
    event: EventLayer = field(default_factory=EventLayer)
    story_world: StoryWorldLayer = field(default_factory=StoryWorldLayer)
    moral: MoralLayer = field(default_factory=MoralLayer)
    provenance: Provenance = field(default_factory=Provenance)

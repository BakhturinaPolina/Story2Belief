"""Schema for the output of the narrative-analysis pipeline.

This is the canonical data contract between Layer 1 and Layers 2 and 3.
Update :doc:`docs/08-narrative-feature-schema.md` whenever this file changes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

PovType = Literal["first_person", "close_third", "omniscient", "multi_perspective"]

#: Method used to derive a character's pseudo-Big5.
PseudoBig5Method = Literal["sentiart", "llm_fallback"]

#: Pseudo-Big5 tuple: (Openness, Conscientiousness, Extraversion, Agreeableness,
#: Neuroticism). Each component is a 0-10 float. See ``docs/04-narrative-pipeline.md``
#: family #8 and Jacobs (2019) §"Pseudo-Big 5".
PseudoBig5 = tuple[float, float, float, float, float]

#: Optional inclusive character-interval pointing into the source text.
#: Provided by ``langextract`` for moral propositions and other grounded items.
CharInterval = tuple[int, int]


@dataclass(frozen=True, slots=True)
class CharacterAffect:
    """Reader-relevant affective stance toward a single character.

    The five relational fields (sympathy / compassion / empathy /
    perspective_taking / valence) are reader-relative constructs filled in
    at Layer-2 read-time. The three ``*_percentile`` fields are the
    Jacobs (2019) emotional figure profile: percentiles within the
    within-text distribution of characters (0-100).
    """

    sympathy: float = 0.0
    compassion: float = 0.0
    empathy: float = 0.0
    perspective_taking: float = 0.0
    valence: float = 0.0

    valence_percentile: float = 0.0
    arousal_percentile: float = 0.0
    ep_percentile: float = 0.0


@dataclass(frozen=True, slots=True)
class CharacterLayer:
    """Character-level features extracted from a narrative.

    Primary tagger: BookNLP (entities, coref, quotes) with ``langextract``
    overlay for POV, traits, goals; SentiArt for ``affect_map`` percentile
    fields and ``pseudo_big5``.
    """

    count: int = 0
    protagonist: str = ""
    pov_type: PovType = "close_third"
    pov_confidence: float = 0.0
    dialogue_share: float = 0.0
    identifiability: float = 0.0
    salience: dict[str, float] = field(default_factory=dict)
    affect_map: dict[str, CharacterAffect] = field(default_factory=dict)

    #: Pseudo-Big5 (O, C, E, A, N) per major character.
    pseudo_big5: dict[str, PseudoBig5] = field(default_factory=dict)
    #: Provenance flag per character indicating whether ``pseudo_big5`` came
    #: from SentiArt's seed-word projection or the LLM fallback.
    pseudo_big5_method: dict[str, PseudoBig5Method] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class EventLayer:
    """Event-level features.

    Combines existing eventfulness-style fields with the Cho et al. (2014)
    five-dimensional perceived-realism breakdown plus the two computational
    consistency signals (BookNLP coref stability and DeBERTa-MNLI
    contradiction density).
    """

    eventfulness: float = 0.0
    conflict_density: float = 0.0
    causal_clarity: float = 0.0
    temporal_linearity: float = 0.0
    narrative_distance: float = 0.0
    realism: float = 0.0

    #: Cho et al. (2014) perceived-realism sub-dimensions.
    plausibility: float = 0.0  # Vera-derived, 0-10.
    typicality: float = 0.0  # Embedding NN distance to per-genre corpus, 0-10.
    factuality: float = 0.0  # WikiData entity-linking ratio, 0-10.
    consistency: float = 0.0  # Cross-link of coref_stability + (1 - contradiction).
    perceptual_quality: float = 0.0  # AAP smoothness + concreteness, 0-10.

    #: BookNLP cluster mention consistency, 0-1.
    coref_stability: float = 0.0
    #: DeBERTa-MNLI sliding-window contradictions per 100 sentence pairs.
    contradiction_density: float = 0.0


@dataclass(frozen=True, slots=True)
class StoryWorldLayer:
    """Story-world features.

    ``aap_arc`` is the SentiArt scene-level Emotion-Potential percentile
    series in scene order; ``aap_mean`` is the story-level mean;
    ``emo_peaks`` is the count of scenes with EP z-score > 2.
    """

    concreteness: float = 0.0
    sensory_density: float = 0.0
    named_place_density: float = 0.0
    world_proximity: float = 0.0
    imagery_passages: int = 0

    aap_mean: float = 0.0
    aap_arc: tuple[float, ...] = ()
    emo_peaks: int = 0


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
    """One candidate moral proposition extracted from a text.

    ``char_interval`` is the source-grounded character span provided by
    ``langextract``; downstream Layer-3 justification-similarity is
    computed against this grounded passage rather than the whole story.
    """

    text: str
    foundations: FoundationDistribution = field(default_factory=FoundationDistribution)
    confidence: float = 0.0
    ambiguity: float = 0.0
    char_interval: CharInterval | None = None


@dataclass(frozen=True, slots=True)
class MoralLayer:
    """Moral-level features."""

    propositions: tuple[MoralProposition, ...] = ()
    behavioral_lessons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Provenance:
    """Reproducibility metadata attached to every record.

    ``tool_versions`` records the exact tagger versions so that runs can
    be compared across BookNLP / Vera / NLI / SentiArt upgrades. Keys
    used by the prototype: ``booknlp``, ``langextract``, ``sentiart_commit``,
    ``vera_model``, ``nli_model``, ``fasttext_vsm``.
    """

    prompt_versions: dict[str, str] = field(default_factory=dict)
    tool_versions: dict[str, str] = field(default_factory=dict)
    model_id: str = ""
    git_sha: str = ""
    created_at: str = ""


@dataclass(frozen=True, slots=True)
class NarrativeFeatures:
    """Top-level structured representation of a single narrative.

    See ``docs/08-narrative-feature-schema.md`` for the JSON shape and
    ``docs/04-narrative-pipeline.md`` for the per-family tagger
    responsibilities.
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

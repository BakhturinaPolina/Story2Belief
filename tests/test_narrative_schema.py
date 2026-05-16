"""Schema-shape tests for the narrative layer."""

from __future__ import annotations

from story2belief.narrative.schema import (
    CharacterLayer,
    EventLayer,
    FoundationDistribution,
    MoralLayer,
    MoralProposition,
    NarrativeFeatures,
    StoryWorldLayer,
)


def test_narrative_features_constructs_with_defaults() -> None:
    nf = NarrativeFeatures(
        text_id="demo",
        title="Demo",
        genre="fairy_tale",
        language="en",
    )
    assert isinstance(nf.character, CharacterLayer)
    assert isinstance(nf.event, EventLayer)
    assert isinstance(nf.story_world, StoryWorldLayer)
    assert isinstance(nf.moral, MoralLayer)


def test_moral_proposition_has_foundations() -> None:
    prop = MoralProposition(text="Be kind to strangers.")
    assert isinstance(prop.foundations, FoundationDistribution)

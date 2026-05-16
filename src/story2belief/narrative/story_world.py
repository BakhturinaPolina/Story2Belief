"""Story-world layer: concreteness, sensory density, world proximity."""

from __future__ import annotations

from story2belief.narrative.schema import StoryWorldLayer


def extract_story_world(text: str) -> StoryWorldLayer:
    """Return the story-world features for the given narrative text."""
    raise NotImplementedError("story_world.extract_story_world is a stub.")

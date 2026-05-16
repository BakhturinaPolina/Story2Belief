"""Layer 1 -- narrative-analysis pipeline.

Turns a short story into a structured :class:`NarrativeFeatures` record.
See ``docs/04-narrative-pipeline.md`` for the full design.
"""

from story2belief.narrative.schema import NarrativeFeatures

__all__ = ["NarrativeFeatures"]

"""Story2Belief: a computational model of narrative persuasion.

The package is organized into three layers, mirroring the architecture in
``docs/01-three-layer-architecture.md``:

- :mod:`story2belief.narrative` -- text -> ``NarrativeFeatures`` (Layer 1).
- :mod:`story2belief.readers`   -- ``ReaderProfile`` x text -> ``ReadingResponse`` (Layer 2).
- :mod:`story2belief.bridge`    -- pre/post moral-dilemma deltas (Layer 3).

Layer boundaries are enforced by convention: do not import upward.
"""

from __future__ import annotations

__version__ = "0.0.1"

__all__ = ["__version__"]

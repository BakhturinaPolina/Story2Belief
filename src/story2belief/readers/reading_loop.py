"""Reading loop: ReaderProfile x text -> ReadingResponse.

The four-step reading loop:

1. Receive text + small structured summary.
2. Reflect (private interpretation).
3. Self-report (adapted SWAS).
4. Express moral uptake.
"""

from __future__ import annotations

from story2belief.readers.profile import ReaderProfile, ReadingResponse


def run_reading(profile: ReaderProfile, text_id: str, text: str) -> ReadingResponse:
    """Run the full reading loop for one agent on one text."""
    raise NotImplementedError("reading_loop.run_reading is a stub.")

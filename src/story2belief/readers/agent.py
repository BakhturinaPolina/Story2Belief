"""Reader-agent factory.

Wraps Concordia (or a thinner prompt-loop fallback) to instantiate a
reader-agent from a ``ReaderProfile``. See ADR
``docs/decisions/0002-use-concordia-for-agents.md``.
"""

from __future__ import annotations

from story2belief.readers.profile import ReaderProfile


class ReaderAgent:
    """A single reader-agent. Stub interface."""

    def __init__(self, profile: ReaderProfile) -> None:
        self.profile = profile

    def read(self, text: str) -> str:
        """Return the agent's free-text interpretation of ``text``."""
        raise NotImplementedError("ReaderAgent.read is a stub.")


def build_agent(profile: ReaderProfile) -> ReaderAgent:
    """Build a reader-agent for the given profile."""
    return ReaderAgent(profile)

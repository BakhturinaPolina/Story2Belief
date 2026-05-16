"""Provider-agnostic LLM client (placeholder).

Wraps OpenAI / Anthropic / HuggingFace endpoints behind a small interface so
that the rest of the codebase does not need to know which backend is in use.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LLMResponse:
    """Normalized response across LLM providers."""

    text: str
    model_id: str
    prompt_tokens: int
    completion_tokens: int


def complete(prompt: str, *, model: str | None = None, json_mode: bool = False) -> LLMResponse:
    """Run a single completion against the configured LLM.

    Parameters
    ----------
    prompt : str
        Full prompt text. Prompt files in ``src/story2belief/prompts/`` should
        be loaded by the caller.
    model : str or None
        Provider/model identifier; defaults to ``S2B_DEFAULT_MODEL`` from env.
    json_mode : bool
        If True, ask the provider for JSON-only output.
    """
    raise NotImplementedError("LLM client is a stub.")

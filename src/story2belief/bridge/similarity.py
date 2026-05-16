"""Embedding-based similarity between texts.

Used to compute the ``justification_similarity`` field of
:class:`TransferDeltas` -- how close the agent's post-reading justification
is to the story's extracted moral.
"""

from __future__ import annotations


def cosine(a_text: str, b_text: str) -> float:
    """Return the cosine similarity between embeddings of two texts.

    Will use ``sentence-transformers`` under the hood; backend is configured
    via :mod:`story2belief.config`.
    """
    raise NotImplementedError("similarity.cosine is a stub.")

"""Synthetic-cohort sampler.

Draws ``ReaderProfile`` instances from theory-constrained ranges (see
``docs/09-reader-trait-schema.md``). The sampler guarantees coverage of
extreme contrasts so trait-driven differences are visible at small N.
"""

from __future__ import annotations

from collections.abc import Sequence

from story2belief.readers.profile import ReaderProfile


def sample_cohort(n: int, *, seed: int = 0, config_path: str | None = None) -> Sequence[ReaderProfile]:
    """Sample a cohort of ``n`` reader profiles.

    Parameters
    ----------
    n : int
        Cohort size.
    seed : int
        Random seed for reproducibility.
    config_path : str or None
        Optional path to ``configs/reader_profiles.yaml``.
    """
    raise NotImplementedError("cohort.sample_cohort is a stub.")

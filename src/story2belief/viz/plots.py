"""Plotting helpers (placeholder)."""

from __future__ import annotations

from collections.abc import Sequence

from story2belief.bridge.transfer import TransferDeltas


def cohort_swas_heatmap(swas_records: Sequence[object]) -> object:
    """Heatmap of SWAS dimensions across the cohort. Returns a Figure."""
    raise NotImplementedError("plots.cohort_swas_heatmap is a stub.")


def transfer_delta_plot(deltas: Sequence[TransferDeltas]) -> object:
    """Plot of pre/post transfer deltas, grouped by reader type."""
    raise NotImplementedError("plots.transfer_delta_plot is a stub.")

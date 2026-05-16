# Story2Belief — top-level Makefile.
# All targets are placeholders today; they delegate to scripts in scripts/
# which are stubs until the corresponding pipeline is implemented.

PY ?= uv run python
CONFIG ?= configs/prototype.yaml

.PHONY: help install sync lock test lint format typecheck \
        pipeline cohort reading bridge all clean

help:
	@echo "Story2Belief — make targets"
	@echo ""
	@echo "  install     Create the uv environment and install dependencies."
	@echo "  sync        Sync the environment with uv.lock."
	@echo "  lock        Refresh uv.lock without installing."
	@echo ""
	@echo "  pipeline    Run the narrative-analysis pipeline (Layer 1)."
	@echo "  cohort      Build the synthetic reader cohort (Layer 2 setup)."
	@echo "  reading     Run the reading session for the cohort (Layer 2)."
	@echo "  bridge      Run the moral-transfer bridge (Layer 3)."
	@echo "  all         pipeline -> cohort -> reading -> bridge."
	@echo ""
	@echo "  test        Run pytest."
	@echo "  lint        Run ruff."
	@echo "  format      Run ruff format."
	@echo "  typecheck   Run mypy."
	@echo "  clean       Remove caches and build artifacts."

install:
	uv sync --all-extras

sync:
	uv sync

lock:
	uv lock

# --- Pipeline targets (stubs) ---

pipeline:
	$(PY) scripts/run_narrative_pipeline.py --config $(CONFIG)

cohort:
	$(PY) scripts/build_reader_cohort.py --config $(CONFIG)

reading:
	$(PY) scripts/run_reading_session.py --config $(CONFIG)

bridge: reading
	$(PY) scripts/run_dilemma_assessment.py --config $(CONFIG)
	$(PY) scripts/compute_transfer_metrics.py --config $(CONFIG)

all: pipeline cohort reading bridge

# --- Quality targets ---

test:
	$(PY) -m pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +

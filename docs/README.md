# Story2Belief — documentation

This folder is the conceptual core of the project. Code in `src/` and configs
in `configs/` are scaffolding for the ideas worked out here.

## Reading order

For a first pass, read the docs in numerical order. Each file is small and has
an **Open questions** section at the bottom — that is where new ideas land
before they harden.

| # | File | What it covers |
|---|------|----------------|
| 00 | [`00-vision-and-scope.md`](00-vision-and-scope.md) | What the project is and is *not* trying to do. |
| 01 | [`01-three-layer-architecture.md`](01-three-layer-architecture.md) | The narrative / reader / bridge architecture, with diagram. |
| 02 | [`02-prototype-roadmap-3mo.md`](02-prototype-roadmap-3mo.md) | 12-week prototype plan with weekly deliverables. |
| 03 | [`03-three-year-plan.md`](03-three-year-plan.md) | Year 1 / 2 / 3 phasing for the dissertation. |
| 04 | [`04-narrative-pipeline.md`](04-narrative-pipeline.md) | Layer 1: feature families and tools. |
| 05 | [`05-reader-pipeline.md`](05-reader-pipeline.md) | Layer 2: AI-reader design and reading loop. |
| 06 | [`06-bridge-moral-transfer.md`](06-bridge-moral-transfer.md) | Layer 3: pre/post moral dilemma and transfer metrics. |
| 07 | [`07-swas-adaptation.md`](07-swas-adaptation.md) | SWAS dimensions adapted as agent self-report. |
| 08 | [`08-narrative-feature-schema.md`](08-narrative-feature-schema.md) | JSON schema for `NarrativeFeatures` with worked example. |
| 09 | [`09-reader-trait-schema.md`](09-reader-trait-schema.md) | Core / secondary reader traits and sampling ranges. |
| 10 | [`10-dilemma-design.md`](10-dilemma-design.md) | How dilemmas are matched to story morals. |
| 11 | [`11-data-sources.md`](11-data-sources.md) | Texts, dilemma corpora, licensing notes. |
| 12 | [`12-tools-and-resources.md`](12-tools-and-resources.md) | Open-source tools and conceptual / empirical references. |
| 13 | [`13-methodology.md`](13-methodology.md) | Draft methodology section for the exposé. |
| 14 | [`14-experiments.md`](14-experiments.md) | Experiment 1 (immediate) and Experiment 2 (transfer + sleeper). |
| 15 | [`15-risks-and-mitigation.md`](15-risks-and-mitigation.md) | Risks: LLM ≠ humans, construct inflation, ambiguity. |
| 16 | [`16-ethics-and-positionality.md`](16-ethics-and-positionality.md) | Ethics of simulated readers, indoctrination angle. |
| 17 | [`17-glossary.md`](17-glossary.md) | Empathy, sympathy, perspective-taking, transportation, etc. |
| 18 | [`18-validation-plan.md`](18-validation-plan.md) | Annotation / simulation / theoretical validation. |

## Supporting material

- `references.bib` — BibTeX for all cited works.
- `references/` — local PDFs (SWAS paper, LIWC manual, persuasion synthesis).
  **Gitignored**; see [`references/README.md`](references/README.md).
- `diagrams/` — mermaid sources for figures.
- `decisions/` — lightweight Architecture Decision Records (ADRs).

## Cross-references

- Source layout and conventions live in [`../AGENTS.md`](../AGENTS.md).
- AI-coding-agent rules live in [`../.cursor/rules/`](../.cursor/rules/).
- Roadmap and timeline are referenced from [`../README.md`](../README.md).

# Tooling Evaluation

Status: **APPROVED v1.1 — extraction and study-tool decisions resolved for pre-study**

## Selection principles

Prefer tools that are simple, inspectable, low-maintenance, portable, and measurably useful. Study-tool eligibility is governed by `docs/15-study-tool-policy.md`: an official Fedora package, official Flatpak, or official Docker/OCI image is required; FOSS is preferred, while a free tier is acceptable when it contains all required features.

## Approved extraction toolchain

The validated AWS v1 stack is:

- provider-native AWS Markdown when available;
- Python 3 deterministic acquisition/provenance/bundle scripts;
- Trafilatura for HTML extraction fallback;
- Markdown + JSON for normalized content/provenance;
- Git/GitHub for controls, code, prompts, QA, state, and artifacts;
- ChatGPT for controlled extraction, enrichment, instruction, coordination, and QA under versioned prompts.

Approved fallback/optional extraction tools:

- Pandoc — HTML fallback;
- `pdftotext -layout` — simple PDF fallback;
- PyMuPDF4LLM — optional high-fidelity PDF path where structure matters.

Not selected for AWS v1 because no measured need exists:

- MarkItDown;
- vector database/custom RAG;
- knowledge graph;
- multi-agent/autonomous framework;
- custom study web application.

## Approved learner-facing study tools

The operational study-tool policy is `docs/15-study-tool-policy.md`.

Current core:

- Ghostwriter — personal Markdown notes;
- Git — repository interaction/version control;
- ripgrep — local search/retrieval.

Optional:

- Neovim;
- Kate.

A dedicated SRS application is not required for v1. Controlled flashcard artifacts plus ChatGPT/session/mastery state provide the retention workflow without introducing a second authoritative database.

## Knowledge-management decision

Plain Markdown + Git remains sufficient. Personal learner notes are local-only by default and remain non-authoritative. Backlinks, graph databases, or dedicated knowledge-management applications are not justified without a measured navigation/retrieval problem.

## Diagram decision

No mandatory diagram application is required before study start. Architecture diagrams may be created with an eligible versionable tool when a session/lab needs one; diagram tooling is therefore an on-demand convenience, not a pre-study gate.

## Lab tooling decision

Official AWS labs/workshops remain the primary hands-on sources. Local CLI/IaC tooling is introduced only when a controlled lab benefits from repeatability, teardown, failure injection, or architecture evidence. No additional lab platform is a pre-study prerequisite.

## Local AI decision

Local LLM tooling is not part of the trusted production extraction path. It may later handle low-risk/repetitive work only after passing the same source-fidelity and regression controls required for any model/toolchain change.

## Validation evidence

See:

- `qa/pilot-plan.md`
- `qa/pilot-gold-v1.md`
- `qa/pilot-results.md`
- `pipeline/README.md`
- `.github/workflows/pipeline-smoke.yml`
- `.github/workflows/artifact-qa.yml`
- `.github/workflows/control-plane.yml`
- `state/pipeline-health.json`

Current pipeline use is allowed only while pipeline health is `GREEN` for the current fingerprint.

## Upgrade rule

Add a tool only when a documented study/pipeline bottleneck or quality defect cannot be solved acceptably with the current simpler stack. Tool adoption must not create duplicate authoritative state.

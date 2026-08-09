# Tooling Evaluation

Status: **PARTIAL APPROVAL — extraction toolchain approved; other study-tool areas remain open**

## Selection principles

Prefer tools that are:

1. open source;
2. Fedora/Linux friendly;
3. simple to install and remove;
4. inspectable and scriptable;
5. able to export portable formats such as Markdown/JSON;
6. low-maintenance;
7. measurably useful for quality or study-time reduction.

A proprietary/cloud tool may be recommended when it provides a material advantage that would otherwise require disproportionate engineering effort.

## Approved minimum extraction toolchain

Issue #3 validated the following AWS-specific stack in a clean Fedora container:

- **provider-native AWS Markdown** — primary ingestion format for canonical `docs.aws.amazon.com` content when the companion Markdown page exists;
- **Python 3** — deterministic acquisition/provenance/bundle scripts;
- **Trafilatura** — preferred HTML-to-Markdown extraction when native Markdown is unavailable;
- **Markdown + JSON** — inspectable normalized content and provenance;
- **Git/GitHub** — specifications, scripts, prompts, QA evidence, approved artifacts, and change history;
- **ChatGPT** — controlled grounded extraction, architectural enrichment, instruction, coordination, and QA under versioned prompts.

This is the default v1 path. No additional retrieval platform is required.

## Approved fallbacks / optional extraction tools

### Pandoc — approved HTML fallback

Strengths:
- Fedora package;
- deterministic;
- strong structural conversion for headings/lists/tables.

Pilot limitation:
- generic conversion retained navigation/footer boilerplate in the synthetic HTML test.

Decision: keep as fallback when Trafilatura is unavailable or when deterministic full-document conversion is useful.

### `pdftotext -layout` — approved low-dependency PDF fallback

Strengths:
- available through Fedora `poppler-utils`;
- simple and fast;
- adequate for plain text PDFs.

Pilot limitation:
- semantic heading/list structure was weaker than Markdown/high-fidelity extraction.

Decision: use only for simple PDF sources; escalate architecture-significant layouts.

### PyMuPDF4LLM — approved optional high-fidelity PDF path

Fedora CI successfully installed and executed the tested current version.

Strengths:
- stronger structure/layout-oriented Markdown conversion;
- useful for PDF-only sources where headings/tables/layout matter.

Cost:
- materially larger dependency footprint; the tested installation pulled PyMuPDF Layout, ONNX Runtime, NumPy, and related dependencies.

Decision: **do not install as a permanent minimum dependency** for AWS study. Install/use when a PDF-only source actually needs it.

## Evaluated but not selected for AWS v1

### MarkItDown

Potential value:
- useful general-purpose conversion across PDF/Office/other document formats.

Why not selected:
- the AWS canonical source path already provides native HTML/Markdown for the material we need;
- Trafilatura + optional PDF tooling covers the remaining current ingestion cases;
- another general converter would add a tool without solving a demonstrated AWS pipeline problem.

Reconsider for Azure/Microsoft material or mixed Office-document workflows if the source inventory demonstrates a need.

### Vector database / custom RAG

Not selected. The curriculum deliberately uses small, objective-driven source packets, and Issue #3 did not reveal a retrieval problem that justifies embeddings/vector infrastructure.

### Knowledge graph

Not selected. Architecture relationships can initially be represented through approved Markdown artifacts/objective mappings. Add only if navigation/relationship management becomes a measured bottleneck.

### Multi-agent / autonomous agent framework

Not selected. It would increase orchestration/debugging surface without improving the validated extraction quality.

### Custom study web application

Not selected. GitHub + Markdown + ChatGPT currently cover governance and content workflow. Build software only for a demonstrated study-process bottleneck.

## Extraction validation evidence

See:
- [`../qa/pilot-plan.md`](../qa/pilot-plan.md)
- [`../qa/pilot-gold-v1.md`](../qa/pilot-gold-v1.md)
- [`../qa/pilot-results.md`](../qa/pilot-results.md)
- [`../pipeline/README.md`](../pipeline/README.md)
- [`.github/workflows/pipeline-smoke.yml`](../.github/workflows/pipeline-smoke.yml)

Key pilot outcomes:
- live AWS native-Markdown ingestion passed in Fedora;
- Trafilatura HTML fallback passed;
- PyMuPDF4LLM PDF smoke test passed;
- source provenance and deterministic prompt bundles passed;
- source-fidelity/qualifier/inference controls passed the representative LLM benchmark.

## Functional areas still to evaluate

### Schema and QA enforcement — next gate
Evaluate:
- JSON Schema / Pydantic-style validation;
- Markdown/front-matter validation;
- citation/provenance checks;
- repeatability/regression tests for extraction/artifact prompts.

### Knowledge management
Plain Markdown + Git remains the default until production study demonstrates a navigation/search problem. If a dedicated app is considered, it must support Linux and portable files.

### Flashcards
Evaluate open-source spaced-repetition tooling and simple import/export formats. Flashcard generation must remain controlled by artifact policy to avoid trivia overload.

### Diagrams
Evaluate text-based or open-source diagram tools that keep architecture diagrams versionable in Git.

### Labs
Official AWS lab/workshop options are already inventoried. Local Terraform/CLI tooling should be added only where it improves architecture learning, repeatability, teardown, or failure testing.

### Local AI
Existing local LLM tooling may be considered for low-risk repetitive transforms/offline processing, but it must pass the same source-fidelity regression set before any approved pipeline stage is delegated.

## Evaluation scorecard

Each future candidate tool should be scored on:

- study-time saved;
- output quality;
- source fidelity;
- Linux/Fedora support;
- setup effort;
- maintenance effort;
- interoperability;
- reproducibility;
- automation potential;
- lock-in;
- privacy/security implications;
- cost.

## Upgrade rule

Add a new tool only when a documented pipeline/study bottleneck or quality defect cannot be solved acceptably with the current simpler stack.

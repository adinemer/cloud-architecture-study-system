# Tooling Evaluation

Status: **DRAFT — research in progress**

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

## Minimum viable toolchain hypothesis

The pilot should first attempt to work with only:

- browser/HTTP retrieval;
- a reliable HTML/PDF-to-text or Markdown converter;
- ChatGPT for controlled extraction, enrichment, instruction, coordination, and QA assistance;
- Markdown files;
- Git/GitHub for versioning, control documents, reviews, and change history;
- optional structured JSON/YAML for schema/QA checks.

No vector database, custom RAG platform, knowledge graph, or multi-agent framework is approved for v1.

## Functional areas to research

### Source acquisition and conversion
Evaluate tools for:
- web-page capture;
- clean HTML to Markdown;
- PDF to Markdown/text with headings/tables preserved;
- detecting changed provider pages.

### Schema and QA enforcement
Evaluate:
- JSON Schema / Pydantic-style validation;
- Markdown linting;
- citation/provenance checks;
- repeatability/regression tests for extraction prompts.

### Knowledge management
Evaluate whether plain Markdown + Git is sufficient before adding a dedicated knowledge-base application. If needed, candidates must support Linux and portable files.

### Flashcards
Evaluate open-source spaced-repetition tooling and simple import/export formats. Flashcard generation must remain controlled by artifact policy to avoid trivia overload.

### Diagrams
Evaluate text-based or open-source diagram tools that keep architecture diagrams versionable in Git.

### Labs
Inventory official AWS lab/workshop options first. Add local Terraform/CLI tooling only where it improves architecture learning or repeatability.

### Local AI
Existing local LLM tooling may be considered for low-risk repetitive transforms or offline processing, but source fidelity and QA performance must be measured before delegation from the primary model.

## Evaluation scorecard

Each candidate tool should be scored on:

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

Add a new tool only when a documented pipeline bottleneck or quality defect cannot be solved acceptably with the current simpler stack.

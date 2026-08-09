# Extraction Pipeline Specification

Status: **APPROVED v1 — validated by Issue #3 pilot**  
Pilot evidence: [`../qa/pilot-results.md`](../qa/pilot-results.md)

## Goal

Transform official provider material into trustworthy, concise, architecture-oriented study material while preserving source fidelity, traceability, and human control.

## Design constraint

Version 1 stays deliberately small and inspectable. Complex retrieval infrastructure is out of scope unless measured production use demonstrates a need.

## Pipeline

```text
approved source
  -> acquire
  -> normalize
  -> classify document/sections
  -> extract provider-grounded information
  -> QA grounded extraction against source
  -> required human reading by source class
  -> summarize at appropriate depth
  -> enrich with architectural context
  -> synthesize across approved sources
  -> generate required study artifacts
  -> artifact QA
  -> approve/version
```

The key control is that **grounded extraction is validated before architectural enrichment**. This prevents inferred design meaning from being silently blended into provider facts.

## Stage 1 — Acquire

Requirements:
- Preserve canonical source identity.
- Do not treat model memory as acquired source material.
- Record retrieval time plus visible source version/update date where available.
- Store source and normalized hashes.

### AWS v1 acquisition order

1. For canonical `docs.aws.amazon.com` HTML pages, try the provider companion `.md` page first.
2. If native Markdown is unavailable, use HTML extraction.
3. Use PDF processing only for PDF-only/diagram-dependent material or when the canonical source requires it.

Implementation: [`../pipeline/ingest.py`](../pipeline/ingest.py).

## Stage 2 — Normalize

Goal: produce clean, inspectable text suitable for deterministic processing.

Approved outputs:
- Markdown/text for human inspection and LLM input;
- JSON provenance sidecar.

### Approved v1 normalizers

- AWS provider-native Markdown: primary;
- Trafilatura: preferred non-native HTML extractor;
- Pandoc: HTML fallback;
- PyMuPDF4LLM: optional high-fidelity PDF path;
- `pdftotext -layout`: low-dependency PDF fallback.

Normalization should preserve headings, lists, tables, warnings, notes, important code/configuration, and source anchors when available.

If a source contains architecture-significant diagrams/tables that are not faithfully represented after normalization, require visual/direct human review rather than trusting text extraction alone.

## Stage 3 — Classify

Apply [`03-source-policy.md`](03-source-policy.md) at document and section level.

Required output:
- processing class;
- human-reading scope;
- reason for classification;
- relevant exam objectives and architecture domains.

## Stage 4 — Grounded extraction

Use [`../prompts/extract-v1.md`](../prompts/extract-v1.md).

Extraction must answer only what the supplied source supports. It should capture:

- problem/capability;
- scope and boundaries;
- explicit provider recommendations;
- prerequisites/dependencies;
- alternatives mentioned by the source;
- security implications;
- reliability/DR behavior;
- performance/scaling behavior;
- networking/data-flow implications;
- cost drivers;
- operational implications;
- constraints, quotas, and caveats;
- failure/troubleshooting information where architecture-relevant;
- migration/integration implications;
- source locators;
- unresolved questions.

At this stage architectural inference is prohibited.

Semantic labels:
- `PROVIDER_FACT`
- `PROVIDER_RECOMMENDATION`

Unsupported fields are recorded as unsupported/not stated rather than filled from model memory.

## Stage 5 — Grounded-extraction QA

Use [`../prompts/qa-v1.md`](../prompts/qa-v1.md) plus applicable artifact/schema checks from Gate #4.

Critical failures include:
- unsupported provider claim;
- material exception/constraint reversed or lost;
- example converted to universal rule;
- architectural inference represented as provider guidance.

A failed extraction does not proceed to enrichment.

## Stage 6 — Human reading

Human reading follows source policy:

- `READ_FULL_CONTEXTUALIZE`: read approved scope completely;
- `READ_SELECTIVE_EXTRACT`: read selected high-value sections identified/approved for reasoning and caveats;
- `EXTRACT_VALIDATE`: read only flagged/high-impact passages when QA and policy permit;
- `REFERENCE_ONLY`: no scheduled reading;
- `HANDS_ON`: use during lab/workshop activity.

AI accelerates reading but does not remove human reading where reasoning continuity is part of the learning objective.

## Stage 7 — Summary

Summary depth depends on processing class:
- `READ_FULL_CONTEXTUALIZE`: concise companion summary after human reading;
- `READ_SELECTIVE_EXTRACT`: cover unread architecture-relevant material while surfacing uncertainty;
- `EXTRACT_VALIDATE`: dense structured compression;
- `REFERENCE_ONLY`: none by default.

## Stage 8 — Architectural enrichment

Use [`../prompts/enrich-v1.md`](../prompts/enrich-v1.md).

Every derived claim must be labeled as one of:
- `CROSS_SOURCE_SYNTHESIS`
- `ARCHITECTURAL_INFERENCE`
- `EXAM_INTERPRETATION`

Enrichment should cover when relevant:
- decision drivers;
- alternatives and trade-offs;
- blast radius/failure domains;
- security boundaries;
- scalability/performance;
- operational burden;
- cost consequences;
- organizational implications;
- migration implications;
- conditions that would change the decision.

Derived claims identify their supporting provider facts. Do not turn inference into an AWS recommendation.

## Stage 9 — Cross-source synthesis

Only combine sources whose identity and status are known. Conflicting or apparently superseded guidance must be surfaced rather than silently reconciled.

## Stage 10 — Artifact generation

Generate only artifacts required by the approved study workflow. Candidate artifacts include:
- concise summary;
- architecture note;
- service architecture card;
- decision matrix;
- ADR;
- architecture pattern/anti-pattern;
- failure-mode note;
- flashcards;
- lab brief;
- architecture scenario;
- misconception record.

Artifact schemas and approval rules are owned by Gate #4.

## Stage 11 — Artifact QA and approval

Minimum gates:
1. source validity;
2. source-to-output fidelity;
3. extraction completeness;
4. inference labeling;
5. cross-source consistency;
6. schema compliance;
7. exam-objective traceability;
8. architecture usefulness;
9. duplication/redundancy control;
10. human review where required.

Lifecycle:

`DRAFT -> QA_PENDING -> REVIEW_REQUIRED (optional) -> APPROVED -> SUPERSEDED`

Only `APPROVED` artifacts belong in the trusted study knowledge base.

## Provenance minimum

Every normalized source carries:
- canonical requested source;
- actual retrieval source;
- retrieval timestamp;
- content type;
- normalizer;
- source SHA-256;
- normalized SHA-256.

Gate #4 adds artifact-level certification/objective/schema/QA metadata.

## Operational tooling policy

Minimum AWS v1 stack:
- Python 3;
- provider-native Markdown;
- Trafilatura when HTML extraction is required;
- Markdown/JSON;
- Git/GitHub;
- ChatGPT with versioned prompts.

Fallback/optional:
- Pandoc;
- `pdftotext`;
- PyMuPDF4LLM.

Not approved as necessary for v1:
- MarkItDown in the AWS-only path;
- embeddings/vector database/RAG framework;
- autonomous agent framework;
- custom study web application.

## Validation results

Issue #3 pilot demonstrated:
- clean Fedora compatibility in CI;
- live AWS native-Markdown retrieval;
- HTML and PDF fallback execution;
- source provenance;
- deterministic prompt bundling;
- 100% capture of the pilot mandatory gold items and architecture-changing qualifiers;
- zero unsupported provider claims in the validated sample;
- zero inference-as-provider-guidance defects;
- conservative direct-reading reduction above 40% for the selective/extraction samples.

See [`../qa/pilot-gold-v1.md`](../qa/pilot-gold-v1.md) and [`../qa/pilot-results.md`](../qa/pilot-results.md).

## Production guardrails

- Per-source QA remains mandatory; the pilot does not authorize blind bulk summarization.
- First real study unit records actual learner reading/review time to calibrate the pilot word-count proxy.
- Current/volatile sources are re-retrieved before use.
- Visual architecture content requires visual/manual inspection when Markdown is insufficient.
- Pipeline/model/prompt changes that can affect output quality require regression validation under Gate #4/change-control policy.

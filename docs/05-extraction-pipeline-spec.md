# Extraction Pipeline Specification

Status: **DRAFT — design for rapid pilot**

## Goal

Transform official provider material into trustworthy, concise, architecture-oriented study material while preserving source fidelity, traceability, and human control.

## Design constraint

Version 1 must be simple enough to implement, inspect, modify, and approve quickly. Complex retrieval infrastructure is explicitly out of scope unless the pilot proves it necessary.

## Pipeline

```text
approved source
  -> acquire
  -> normalize
  -> classify document/sections
  -> extract provider-grounded information
  -> summarize at appropriate depth
  -> enrich with architectural context
  -> synthesize across approved sources
  -> generate required study artifacts
  -> QA against source
  -> human review where policy requires
  -> approve/version
```

## Stage 1 — Acquire

Requirements:
- Preserve canonical source identity.
- Prefer provider-native HTML/Markdown/PDF where practical.
- Record retrieval date and visible source version/update date where available.
- Do not treat model memory as acquired source material.

## Stage 2 — Normalize

Goal: produce clean, inspectable text suitable for deterministic processing.

Preferred pilot outputs:
- Markdown for human inspection;
- optional JSON for schema validation.

Normalization should remove navigation noise while preserving headings, lists, tables, warnings, notes, code blocks when architecturally relevant, and source anchors when possible.

## Stage 3 — Classify

Apply `docs/03-source-policy.md` at document and section level.

Required output:
- processing class;
- human-reading scope;
- reason for classification;
- relevant exam objectives and architecture domains.

## Stage 4 — Grounded extraction

Extraction must answer only what the source supports. Initial schema should capture:

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
- cited source locations;
- unresolved questions.

At this stage, architectural inference is prohibited except as an explicitly flagged question for the enrichment stage.

## Stage 5 — Summary

Summary depth depends on processing class:
- `READ_FULL_CONTEXTUALIZE`: concise companion summary after human reading;
- `READ_SELECTIVE_EXTRACT`: detailed enough to cover unread sections without obscuring uncertainty;
- `EXTRACT_VALIDATE`: dense structured compression;
- `REFERENCE_ONLY`: none by default.

## Stage 6 — Architectural enrichment

Use extracted facts to derive design meaning. Every enriched claim must be labeled as one of:

- `PROVIDER_RECOMMENDATION`
- `CROSS_SOURCE_SYNTHESIS`
- `ARCHITECTURAL_INFERENCE`
- `EXAM_INTERPRETATION`

Enrichment should cover when relevant:
- decision drivers;
- alternatives and trade-offs;
- blast radius;
- availability and failure domains;
- security boundaries;
- scalability;
- operational burden;
- cost consequences;
- organizational implications;
- migration implications;
- when the preferred decision changes.

## Stage 7 — Cross-source synthesis

Only combine sources whose identity and status are known. Conflicting or apparently superseded guidance must be surfaced rather than silently reconciled.

## Stage 8 — Artifact generation

Generate only artifacts requested by the approved study workflow. Candidate artifacts include:
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

Schemas will be defined separately and versioned.

## Stage 9 — QA

Minimum gates:
1. source validity;
2. source-to-output fidelity;
3. extraction completeness;
4. inference labeling;
5. cross-source consistency;
6. schema compliance;
7. exam-objective traceability;
8. architecture usefulness;
9. duplicate/redundancy control;
10. human review where required.

## Stage 10 — Approval

Artifacts have lifecycle states:

`DRAFT -> QA_PENDING -> REVIEW_REQUIRED (optional) -> APPROVED -> SUPERSEDED`

Only `APPROVED` artifacts belong in the trusted study knowledge base.

## Pilot success criteria

The first implementation should demonstrate:
- materially less human reading time than an all-manual workflow;
- no important architectural omissions in the tested sample beyond the agreed tolerance;
- no unsupported provider claims;
- reliable separation of provider statements and inference;
- repeatable output shape;
- inspectable provenance;
- low operational overhead on Fedora Linux.

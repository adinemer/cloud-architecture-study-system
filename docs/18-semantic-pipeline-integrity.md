# Semantic Pipeline Integrity Specification

Status: **APPROVED v1 — pre-unfreeze hardening**

## Purpose

Make extraction/enrichment content quality a machine-enforced prerequisite for trusted study material. Operational pipeline success alone is insufficient.

## Hard invariant

A source packet may proceed to trusted artifact generation only when both are true:

1. operational pipeline health is `GREEN` for the current fingerprint;
2. the packet has a schema-valid semantic-integrity report with `semantic_status=PASS` and no validator findings.

Any uncertainty that can change an architecture, security, reliability, networking, data, cost, quota, or exam decision fails closed or becomes explicit `NEEDS_REVIEW`/unresolved work.

## Accounting rule — no silent gaps

Every selected source section must be represented in the semantic report as exactly one of:

- `PROCESSED`;
- `INTENTIONALLY_EXCLUDED` with an explicit reason;
- `FAILED`;
- `MISSING`.

`FAILED` or `MISSING` blocks trusted use. An architecture-significant processed section may not contain zero extracted claims unless an explicit no-relevant-claims reason is recorded.

Empty output is never allowed to ambiguously mean both “nothing relevant was stated” and “the pipeline missed content.”

## Grounded extraction gate

Every provider claim must:

- be `PROVIDER_FACT` or `PROVIDER_RECOMMENDATION`;
- resolve to an accounted source section;
- contain a non-empty source locator;
- preserve scope, conditions, exceptions, prerequisites, recommendation strength, and negative constraints;
- remain separate from architectural inference.

All `HIGH` severity provider claims require explicit human review before semantic PASS.

For initial production qualification and any packet used to establish a new decision pattern, architecture-changing HIGH claims are reviewed at 100%; statistical spot checking does not replace this requirement.

## Enrichment gate

Every `CROSS_SOURCE_SYNTHESIS`, `ARCHITECTURAL_INFERENCE`, or `EXAM_INTERPRETATION` claim must:

- have explicit rationale;
- list one or more supporting provider-grounded extraction claim IDs;
- never depend only on another inference;
- not inflate an inference into an AWS recommendation;
- preserve uncertainty and decision conditions.

Unsupported/orphan enrichment fails the packet.

## Conflict rule

Cross-source conflicts must be represented explicitly. Any unresolved `HIGH` conflict blocks semantic PASS. A conflict marked `RESOLVED` must record the resolution basis.

The system must never silently choose between apparently contradictory or superseded sources.

## Strict production thresholds

For semantic PASS:

- factual fidelity = **5/5**;
- qualifier/exception preservation = **5/5**;
- unsupported-claim avoidance = **5/5**;
- inference separation = **5/5**;
- architecture completeness >= **4.5/5**;
- locator quality >= **4.5/5**;
- all HIGH provider claims reviewed;
- zero missing/failed selected source sections;
- zero unresolved HIGH conflicts;
- no material semantic drift across at least two compared runs.

Averages cannot compensate for a critical failure.

## Repeatability

At least two independent reasoning runs are compared during qualification/regression. Wording may differ, but architecture-significant facts, constraints, qualifiers, decision boundaries, and inference lineage must not materially drift.

Material semantic drift causes failure or required review; it cannot be hidden by deterministic acquisition/bundling success.

## Machine contract

Canonical semantic QA report:

`schemas/semantic-pipeline-v1.schema.json`

Validation:

- `qa/validate_semantic_pipeline.py`
- `qa/semantic_pipeline_regression.py`
- `qa/fixtures/semantic-valid.json`

The regression suite deliberately tests missing sections, unreviewed HIGH claims, orphan source claims, orphan inference support, weakened fidelity/qualifier scores, unresolved conflicts, silent empty architecture sections, and repeatability drift.

## Production relationship

This specification strengthens, and does not replace:

- `docs/05-extraction-pipeline-spec.md`;
- `docs/08-quality-assurance-spec.md`;
- `prompts/extract-v1.md`;
- `prompts/qa-v1.md`;
- `prompts/enrich-v1.md`.

The semantic report is QA/control evidence. It does not itself become learner study content.

## Fail-closed behavior

If semantic validation fails:

- enrichment/artifact approval is blocked where grounded extraction is defective;
- trusted output must not be produced from missing/unaccounted source coverage;
- defects are corrected or surfaced for human review;
- the complete semantic regression/integration checks are rerun;
- no PASS may be inferred from a previous packet or previous model run.

## Study-start boundary

`semantic_pipeline_integrity=PASS` is a mandatory pre-unfreeze gate but does not grant study-start approval. The explicit user start gate remains independent.

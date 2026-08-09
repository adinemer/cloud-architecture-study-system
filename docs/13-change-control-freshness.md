# Change Control, Versioning, and Freshness Specification

Status: **APPROVED v1**

## Purpose

Control changes to certification scope, provider guidance, study policy, prompts/models, schemas, source packets, and derived artifacts without silently invalidating study history.

## Change classes

### C0 — editorial
No semantic effect: spelling, formatting, link cleanup. No study-state invalidation.

### C1 — source refresh, no material semantic change
Canonical source content/hash changes but architecture/exam meaning remains equivalent after review.

Action:
- update retrieval/hash metadata;
- record refresh;
- no automatic mastery invalidation.

### C2 — material provider-content change
Service behavior, constraints, recommendation, quota model, architecture guidance, availability, or exam-relevant distinction changes.

Action:
- identify affected artifacts/objectives/units;
- mark affected artifacts `REVIEW_REQUIRED` or `SUPERSEDED`;
- mark affected mastery evidence potentially stale;
- schedule targeted remediation/retest if needed.

### C3 — certification scope/blueprint change
Exam guide, task statements, weights, in-scope concepts, or exam code/scope changes materially.

Action:
- freeze current scope version;
- update objective map/resource inventory;
- run coverage-gap analysis;
- replan affected units;
- invalidate completion/readiness only where affected.

### C4 — control-system change
Changes to governance, source policy, sequence policy, artifact schema, QA, mastery rules, session rules, or coordinator governance.

Action:
- version the affected specification;
- record migration/compatibility effect;
- regression-test before production use;
- update control snapshot requirements.

### C5 — prompt/model/toolchain change
LLM prompt, model, parser, renderer, validator, or important tool version changes.

Action:
- run required regression corpus/CI;
- compare fidelity/anti-drift behavior;
- approve before production use;
- preserve old version identifiers in existing artifacts/sessions.

## Change record

Every governed C1–C5 change has a record containing:

- change ID;
- change class;
- date;
- initiator/source;
- old version/hash;
- new version/hash;
- reason;
- affected files/sources;
- affected units/objectives/artifacts/sessions;
- required QA/regression;
- migration/remediation actions;
- approval status;
- effective date.

Store under:

`changes/<YYYY>/<change-id>.json`

## Semantic versioning

Use semantic versions for controlled internal contracts:

- MAJOR — incompatible contract/process change;
- MINOR — backward-compatible capability/field/rule addition;
- PATCH — correction with no material workflow incompatibility.

Existing artifacts/session records retain the versions they were created under.

## Exam scope version

The exam scope version is a dated/versioned snapshot of the current canonical SAP-C02 guide and task pages. It is not assumed static because the documentation is living content.

Every session/artifact records its exam scope version.

## Freshness tiers

### Tier F0 — immutable/historical
Historical evidence/session records. Never “refreshed”; supersede/correct instead.

### Tier F1 — low volatility
Architecture principles/framework material whose meaning changes infrequently.

Check:
- at source-packet approval;
- when AWS signals relevant revision;
- before major capstone/readiness use if old.

### Tier F2 — medium volatility
Service architecture/design/security/resilience documentation.

Check:
- before first use in a unit;
- before reuse after a meaningful interval;
- on relevant AWS change signal.

### Tier F3 — high volatility
Quotas, pricing, service availability, exam/training catalog availability, rapidly evolving features.

Check at decision/use time. Do not rely on old artifact values when live confirmation is practical.

## Source freshness record

Source metadata should track:

- canonical URL;
- last retrieved date;
- source/normalized hash;
- visible revision/date where available;
- freshness tier;
- last semantic review;
- current state: `CURRENT`, `REVIEW_REQUIRED`, `SUPERSEDED`, `UNAVAILABLE`.

## Hash change behavior

A hash change is a **signal**, not proof of semantic change.

Process:
1. retrieve current canonical source;
2. compare changed content;
3. classify C0/C1/C2 or other applicable class;
4. update only affected downstream knowledge;
5. preserve previous evidence/history.

## Artifact dependency propagation

Artifacts must list source IDs/hashes. When a source becomes `REVIEW_REQUIRED`/`SUPERSEDED`, dependent artifacts are discoverable and cannot remain silently trusted for affected claims.

High-volatility flashcards/artifacts require a recent review marker under artifact QA rules.

## Mastery dependency propagation

Mastery is evidence-based. A source/control change only reduces current mastery confidence when it affects the evidence's correctness/relevance.

Do not reset everything because AWS updated a page. Perform targeted impact analysis.

## Prompt/model regression

Before adopting a new production model/prompt combination:

- run the extraction gold corpus;
- run artifact valid/invalid fixtures;
- verify inference separation;
- verify source locator/provenance behavior;
- verify deterministic structured-output contract;
- compare omissions/unsupported claims with approved baseline.

A newer/bigger model is not automatically approved.

## Tool dependency policy

Prefer loose/minimal dependencies. Pin versions in CI where reproducibility materially matters, but do not create maintenance-heavy lockfiles without need.

When provider-native Markdown remains available, it outranks adding parsing complexity.

## Freshness cadence automation

The system may use scheduled GitHub/automation checks later to detect source hash changes, but automation only raises a review event. It cannot autonomously rewrite approved architecture knowledge or mastery state.

## Final pre-exam freshness gate

Before real exam readiness is declared:

- refresh SAP-C02 exam guide/task/scope pages;
- resolve material C2/C3 changes;
- refresh high-volatility references used in exam distinctions;
- rerun affected assessments/remediation;
- record final exam-scope version.

# Architectural Enrichment QA Prompt v1

Validate architectural enrichment only after grounded extraction has already passed source-to-extraction QA.

## Hard checks

For every enrichment claim:

1. label must be exactly one of `CROSS_SOURCE_SYNTHESIS`, `ARCHITECTURAL_INFERENCE`, or `EXAM_INTERPRETATION`;
2. at least one supporting provider-grounded extraction claim ID must resolve;
3. rationale must explain how the supporting provider facts justify the derived statement;
4. no derived statement may be presented as an AWS recommendation unless an extracted `PROVIDER_RECOMMENDATION` explicitly supports that recommendation strength;
5. uncertainty, scope, conditions, and decision boundaries must be preserved;
6. derived claims must not use another inference as their only support;
7. conflicting or apparently superseded sources must be surfaced explicitly rather than silently reconciled;
8. architecture-significant dimensions must not disappear silently: if a requested dimension is unsupported or not relevant, mark it `NOT_STATED`, `NOT_APPLICABLE`, or `UNRESOLVED` with a reason.

## Architecture completeness dimensions

Check applicable coverage of:

- decision drivers;
- alternatives and trade-offs;
- failure domains / blast radius;
- security boundaries;
- reliability / recovery implications;
- performance / scaling implications;
- networking / data-flow implications;
- operating burden;
- cost drivers;
- migration / organizational implications;
- conditions that change the decision;
- SAP-C02 objective relevance;
- direct-reading recommendations.

## Critical failures

Return FAIL for any:

- orphan inference/support reference;
- inference represented as provider fact/recommendation;
- architecture-changing qualifier or condition lost;
- unresolved HIGH source conflict;
- silent omission of a known architecture-significant dimension;
- unsupported certainty or recommendation strength;
- material semantic drift between repeated enrichment runs.

## Production PASS thresholds

- factual-boundary preservation: 5/5;
- inference separation: 5/5;
- unsupported-derived-claim avoidance: 5/5;
- qualifier/condition preservation: 5/5;
- architecture completeness: >=4.5/5;
- support lineage quality: >=4.5/5;
- zero critical failures.

The final machine-readable semantic packet must also pass `schemas/semantic-pipeline-v1.schema.json` and `qa/validate_semantic_pipeline.py`.

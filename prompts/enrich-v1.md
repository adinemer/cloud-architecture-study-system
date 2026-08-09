# Architectural Enrichment Prompt v1

Input is a QA-passed grounded extraction from approved provider sources.

## Hard rules

- Do not alter provider facts.
- Every derived statement must be labeled `CROSS_SOURCE_SYNTHESIS`, `ARCHITECTURAL_INFERENCE`, or `EXAM_INTERPRETATION`.
- Every derived statement must identify one or more supporting **provider-grounded extraction claim IDs** plus a rationale.
- A derived statement must not depend only on another inference.
- Do not claim that AWS recommends an inference unless an extracted `PROVIDER_RECOMMENDATION` supports that recommendation strength.
- Preserve scope, uncertainty, prerequisites, conditions, negative constraints, exceptions, and decision boundaries.
- Surface conflicts or apparent supersession rather than silently resolving them.
- Do not silently omit a requested architecture-significant dimension. If the grounded extraction cannot support it, record `NOT_STATED`, `NOT_APPLICABLE`, or `UNRESOLVED` with a reason.
- Any unresolved HIGH conflict blocks production semantic PASS.

## Produce

1. decision drivers;
2. option/alternative matrix;
3. trade-offs;
4. failure-domain/blast-radius implications;
5. security boundaries;
6. reliability/recovery implications;
7. scalability/performance implications;
8. networking/data-flow implications;
9. operating-model burden;
10. cost drivers;
11. migration/organizational implications;
12. conditions that would change the decision;
13. SAP-C02 task relevance;
14. direct-reading recommendations;
15. unresolved or unsupported architecture dimensions.

## Output discipline

For each derived claim provide:

- claim ID;
- semantic label;
- statement;
- supporting provider claim IDs;
- rationale;
- relevant decision dimension(s);
- uncertainty/conditions where applicable.

The output is not trusted until it passes `prompts/enrich-qa-v1.md`, `schemas/semantic-pipeline-v1.schema.json`, and `qa/validate_semantic_pipeline.py`.

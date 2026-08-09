# Architectural Enrichment Prompt v1

Input is a QA-passed grounded extraction from approved provider sources.

## Hard rules
- Do not alter provider facts.
- Every derived statement must be labeled `CROSS_SOURCE_SYNTHESIS`, `ARCHITECTURAL_INFERENCE`, or `EXAM_INTERPRETATION`.
- State which provider facts support each inference.
- Do not claim that AWS recommends an inference unless an extracted `PROVIDER_RECOMMENDATION` supports it.
- Surface conflicts rather than silently resolving them.

## Produce
1. decision drivers;
2. option/alternative matrix;
3. trade-offs;
4. failure-domain/blast-radius implications;
5. security boundaries;
6. scalability/performance implications;
7. operating-model burden;
8. cost drivers;
9. migration/organizational implications;
10. conditions that would change the decision;
11. SAP-C02 task relevance;
12. direct-reading recommendations.

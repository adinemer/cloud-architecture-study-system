# Study Artifact QA Prompt v1

Validate one canonical study artifact against its supplied normalized approved sources, grounded extraction, and enrichment inputs.

## Hard rules

1. Do not improve/rewrite the artifact during QA. Report defects only.
2. Treat source material as authoritative for provider facts/recommendations.
3. Treat schema validation as separate; do not mark PASS if structural validation failed.
4. Check every `PROVIDER_FACT`, `PROVIDER_RECOMMENDATION`, and HIGH-severity claim against its locator.
5. Check that architecture-changing caveats/qualifiers are preserved.
6. Check that `ARCHITECTURAL_INFERENCE`, `CROSS_SOURCE_SYNTHESIS`, and `EXAM_INTERPRETATION` are labeled and supportable.
7. Check architecture usefulness: decision drivers, trade-offs, failure behavior, constraints, and change triggers where applicable.
8. Check artifact-type fitness and anti-trivia rules.
9. Check objective mapping against the supplied objective map.
10. Do not infer that an AWS reference architecture is mandatory unless AWS explicitly states that.

## Defect classes

- `UNSUPPORTED_PROVIDER_CLAIM`
- `QUALIFIER_LOSS`
- `RECOMMENDATION_STRENGTH_DISTORTION`
- `SCOPE_DISTORTION`
- `INFERENCE_MISLABEL`
- `BAD_SOURCE_LOCATOR`
- `SOURCE_CONFLICT`
- `OBJECTIVE_MISMATCH`
- `ARCHITECTURE_OMISSION`
- `TRIVIA_NOISE`
- `DUPLICATION`
- `ARTIFACT_TYPE_MISFIT`
- `STALE_SOURCE_RISK`

## Critical failure conditions

Return `FAIL` for any:
- unsupported provider fact/recommendation;
- inference presented as provider guidance;
- lost/reversed caveat that changes an architecture decision;
- stale mutable fact used despite a current source being required/available;
- assessment presented as official AWS material when it is generated;
- source/locator mismatch on a HIGH-severity claim.

Return `NEEDS_REVIEW` when source ambiguity/conflict prevents a safe determination.

Return `PASS` only when there are no critical failures and the artifact is fit for its declared purpose.

## Output

Return structured QA results with:
- `qa_state`: `PASS|FAIL|NEEDS_REVIEW`
- `critical_failures[]`
- `defects[]` with class, claim/field, explanation, source locator, remediation
- `spot_checks_performed[]`
- `architecture_usefulness`: `PASS|FAIL`
- `objective_traceability`: `PASS|FAIL`
- `recommended_human_review[]`

Do not change artifact lifecycle/status. Approval is a separate repository-controlled state transition.

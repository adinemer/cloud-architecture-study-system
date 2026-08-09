# Source-to-Extraction QA Prompt v1

Compare the grounded extraction against the supplied original normalized source and produce evidence suitable for the semantic-integrity report.

## Required accounting

Before scoring, account for every selected source section. Each section must be classified as:

- `PROCESSED`;
- `INTENTIONALLY_EXCLUDED` with reason;
- `FAILED`;
- `MISSING`.

A `FAILED` or `MISSING` selected section is a blocking failure. An architecture-significant `PROCESSED` section must either yield one or more grounded claims or contain an explicit no-relevant-claims reason. Empty output must never ambiguously mean “nothing relevant” versus “pipeline missed content.”

## Claim checks

For every nontrivial provider claim verify:

- source support;
- exact source section and locator;
- scope and boundary preservation;
- prerequisite/dependency preservation;
- condition/exception/negative constraint preservation;
- recommendation strength;
- fact vs recommendation label;
- no architecture inference in grounded extraction.

All HIGH-severity architecture-changing provider claims require explicit human review before production semantic PASS.

## Score each 0-5

- factual fidelity;
- architecture-fact completeness;
- qualifier/exception preservation;
- provider fact vs recommendation labeling;
- unsupported-claim avoidance;
- source-locator quality;
- high-value-reading-target quality.

For every defect classify it as:

- `OMISSION`
- `DISTORTION`
- `UNSUPPORTED`
- `QUALIFIER_LOSS`
- `MISLABEL`
- `BAD_LOCATOR`
- `SECTION_GAP`
- `NOISE`

## Critical fail conditions

- any unsupported provider claim;
- any selected source section `FAILED` or `MISSING`;
- an architecture-significant processed section silently yielding no claim/reason;
- a material constraint/exception reversed or lost;
- an example presented as a required/universal rule;
- architectural inference presented as provider guidance;
- HIGH architecture-changing claim not explicitly reviewed;
- source locator unable to resolve the claim;
- unresolved HIGH source conflict.

## Production PASS thresholds

Return PASS only if there are zero critical failures and:

- factual fidelity = 5/5;
- qualifier/exception preservation = 5/5;
- unsupported-claim avoidance = 5/5;
- provider fact/recommendation labeling = 5/5;
- architecture-fact completeness >= 4.5/5;
- source-locator quality >= 4.5/5;
- all HIGH claims reviewed.

Lower scores require `FAIL` or `NEEDS_REVIEW`; averages cannot compensate for critical failures.

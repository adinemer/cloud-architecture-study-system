# Source-to-Extraction QA Prompt v1

Compare the grounded extraction against the supplied original normalized source.

Score each 0-5:
- factual fidelity;
- architectural-fact completeness;
- qualifier/exception preservation;
- provider fact vs recommendation labeling;
- unsupported-claim avoidance;
- source-locator quality;
- high-value-reading-target quality.

For every defect, classify it as:
- `OMISSION`
- `DISTORTION`
- `UNSUPPORTED`
- `QUALIFIER_LOSS`
- `MISLABEL`
- `BAD_LOCATOR`
- `NOISE`

Critical fail conditions:
- any unsupported provider claim;
- a material constraint/exception reversed or lost;
- an example presented as a required rule;
- architectural inference presented as provider guidance.

Return PASS only if there are no critical failures and every score is >=4.

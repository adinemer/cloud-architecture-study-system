# Quality Assurance and Anti-Drift Specification

Status: **APPROVED v1**  
Issue: **#4**  
Date: **2026-08-09**

## 1. Purpose

Define the quality gates that must pass before generated study material becomes trusted, and the controls that prevent curriculum, source, semantic, schema, and formatting drift over a multi-month study program.

## 2. Trust boundary

Only artifacts with all of the following are trusted study material:

- schema-valid canonical JSON;
- `status=APPROVED`;
- `qa_state=PASS`;
- valid source provenance;
- no critical QA failures;
- rendered Markdown reproducible from canonical JSON.

Everything else is draft or working material.

## 3. QA layers

### Q0 — source eligibility

Check:
- source is allowed by `docs/03-source-policy.md`;
- canonical/provider identity is known;
- retrieval metadata exists;
- stale/superseded/conflicting status is not hidden;
- required source hash/provenance exists.

Failure: artifact cannot proceed.

### Q1 — schema compliance

Check:
- artifact matches the declared JSON Schema version;
- required fields exist;
- enumerations/IDs/status values are valid;
- no undeclared top-level fields are silently introduced;
- claim objects use valid labels;
- provenance objects are structurally complete.

Failure: artifact cannot proceed.

### Q2 — provider-fidelity

For every `PROVIDER_FACT` or `PROVIDER_RECOMMENDATION`:
- verify source supports the claim;
- verify qualifier/exception language has not been lost when it changes architecture meaning;
- verify recommendation strength has not been inflated;
- verify scope (account/Region/AZ/resource/global) is not altered;
- verify mutable facts are current enough for the activity.

Critical failures:
- unsupported provider claim;
- inference presented as provider guidance;
- omitted qualifier that reverses/changes a design decision;
- stale fact used despite an available current source.

Any critical failure -> `FAIL`.

### Q3 — extraction completeness

For `READ_SELECTIVE_EXTRACT` and `EXTRACT_VALIDATE` material:
- compare against mandatory/gold requirements where defined;
- confirm architecture-significant constraints/caveats were captured;
- confirm required unread sections are represented by extraction;
- record unresolved/ambiguous source items rather than guessing.

Default gate:
- no known architecture-changing omission;
- mandatory source checklist complete where one exists.

### Q4 — inference separation

Check:
- `ARCHITECTURAL_INFERENCE` has rationale and supporting source(s);
- `CROSS_SOURCE_SYNTHESIS` identifies its sources;
- `EXAM_INTERPRETATION` maps to objective/task IDs;
- provider-grounded fields do not contain unlabeled AI reasoning.

Failure -> artifact cannot be approved.

### Q5 — cross-source consistency

When multiple sources are used:
- flag contradictions;
- flag apparent supersession;
- prefer current canonical docs over training/blog mirrors;
- do not silently reconcile conflicts;
- document the resolution or leave an open question.

### Q6 — exam traceability

Check:
- certification and scope version recorded;
- objective IDs exist and are valid in the approved objective map;
- artifact relevance is plausible for those objectives;
- generated assessment questions map to what they actually test.

### Q7 — architecture usefulness

Human/AI review checks whether the artifact improves architectural judgment rather than merely repeating product features.

For architecture-focused artifacts, require meaningful coverage of applicable dimensions such as:
- decision drivers;
- trade-offs;
- failure modes;
- security boundaries;
- reliability;
- performance/scaling;
- operations;
- cost;
- when the preferred decision changes.

Not every dimension must contain content, but empty relevance must be intentional rather than forgotten.

### Q8 — anti-trivia / artifact fitness

Check artifact-specific quality:
- flashcards emphasize concepts/decisions/constraints over arbitrary details;
- comparison matrices use decision-relevant criteria;
- ADRs contain genuine alternatives and trade-offs;
- labs validate behavior rather than console-click memorization;
- assessments do not leak answers or masquerade as official AWS questions.

### Q9 — duplication and contradiction

Before approving a new artifact:
- search approved artifacts for overlapping topic/decision;
- update/supersede existing artifact when appropriate rather than creating near-duplicates;
- surface contradiction rather than letting two approved notes silently disagree.

### Q10 — render integrity

Check:
- Markdown renderer completes without error;
- re-rendering is deterministic;
- committed Markdown equals freshly rendered Markdown;
- manually edited generated Markdown fails CI.

## 4. QA outcome model

Allowed `qa_state`:
- `QA_PENDING`
- `PASS`
- `FAIL`
- `NEEDS_REVIEW`

Critical QA failures always force `FAIL` or `NEEDS_REVIEW`; they cannot be averaged away by other scores.

## 5. Human-review requirements by source class

### `READ_FULL_CONTEXTUALIZE`
Human requirements:
- complete approved reading scope;
- confirm reading completion before artifact approval;
- review summary/contextualization for conceptual distortion.

### `READ_SELECTIVE_EXTRACT`
Human requirements:
- read the approved selected sections;
- review extracted architecture-changing constraints/caveats;
- spot-check unread-section extraction against sources.

Minimum spot-check policy for production v1:
- at least **20% of claim-bearing source sections**, rounded up;
- always check HIGH-impact constraints/recommendations.

### `EXTRACT_VALIDATE`
Human requirements:
- no full reading by default;
- inspect all HIGH-impact or volatile claims;
- spot-check at least **10% of factual claims**, rounded up, until production telemetry demonstrates a safer/lower level can be approved.

### `REFERENCE_ONLY`
No artifact generated by default; verify exact current reference when used for a decision/lab.

### `HANDS_ON`
Human executes or observes required lab evidence. AI cannot self-certify completion.

### `ASSESSMENT`
Learner answer must be captured before solution/rationale is exposed when used as mastery evidence.

## 6. Approval lifecycle

1. AI/learner creates structured JSON as `DRAFT`.
2. Schema validation -> if valid, set workflow state to `QA_PENDING`.
3. Automated semantic checks run.
4. Source-grounded ChatGPT QA uses the current QA prompt/version.
5. Human review is applied where required.
6. Artifact is set to `APPROVED` only if `qa_state=PASS`.
7. Later material changes create a new artifact version; prior artifact becomes `SUPERSEDED`.

Approval is a repository-controlled state transition, not a conversational phrase.

## 7. Automated anti-drift checks

CI must fail on:
- invalid JSON Schema;
- unknown artifact types/status/labels;
- missing source references for provider claims;
- inference claims missing rationale/support;
- exam interpretation missing objective IDs;
- generated Markdown not matching deterministic rendering;
- schema version not found;
- approved artifact with `qa_state != PASS`;
- duplicate `artifact_id` among active artifacts;
- source ID referenced but absent from the artifact source registry;
- flashcard set exceeding default 20 cards without `exception_reason`;
- `HIGH` volatility facts without retrieval/review metadata;
- direct editing of generated Markdown detected by render mismatch.

## 8. Model/prompt regression policy

Changing model, extraction prompt, enrichment prompt, QA prompt, or artifact-generation prompt can change outputs even when schemas remain stable.

Before a changed prompt/model is approved for production artifact generation:

1. run the Issue #3 gold corpus;
2. run artifact regression fixtures;
3. require zero critical fidelity failures;
4. require schema compliance;
5. require all architecture-changing qualifiers in the gold set;
6. compare semantic outputs, allowing wording differences;
7. record model/prompt versions in the regression result.

A model upgrade is **not** automatically approved because it is newer.

## 9. Regression fixture set v1

The minimum fixture set must include:

- source summary with provider facts and caveats;
- architecture note with provider grounding plus labeled inference;
- decision record with at least two real options;
- flashcard set including a prohibited/volatile-card negative fixture;
- lab brief with H3/H4 solution-leak check;
- assessment set labeled generated;
- invalid provenance fixture;
- inference-as-provider negative fixture;
- Markdown drift fixture.

CI tests both expected-valid and expected-invalid artifacts.

## 10. Freshness controls

A source/artifact must be rechecked when:
- the architecture unit starts and retrieval is older than the unit’s freshness threshold;
- AWS announces a material change;
- a referenced page hash changes and the change is architecture-significant;
- before late exam-readiness review;
- before relying on volatile quotas/pricing/service availability.

Freshness thresholds are source-type dependent; v1 defaults:
- exam scope: check before every unit and before exam-readiness phase;
- service behavior/security/reliability: re-retrieve when used if older than 90 days;
- pricing/quotas/availability: re-retrieve when used if older than 30 days;
- durable framework principles: check for change at least every 180 days or when AWS publishes a new revision.

These thresholds are operational defaults, not claims that sources necessarily change on those schedules.

## 11. Architecture-claim severity

Claims can be tagged:
- `LOW` — explanatory detail;
- `MEDIUM` — affects implementation choice;
- `HIGH` — can change architecture/security/reliability/cost decision.

HIGH claims require:
- explicit source locator;
- review of qualifier/exception;
- current-enough source;
- human review before approval for selective/extract classes.

## 12. Assessment integrity

Generated assessment QA requires:
- explicit label `GENERATED_ASSESSMENT`;
- no claim of AWS authorship;
- answer supported by source/decision artifacts;
- distractors plausibly wrong for stated requirements rather than arbitrary;
- no answer leakage in prompt metadata shown to learner;
- architecture questions evaluated with rubrics where multiple designs could be defensible.

Official AWS questions/practice exams remain separate and are never stored as generated artifacts unless licensing permits and the workflow explicitly calls for metadata only.

## 13. Lab integrity

Lab QA requires:
- clear objective and architecture behavior;
- cleanup/cost-risk controls;
- acceptance evidence;
- no destructive production target;
- H3/H4 does not reveal full implementation steps before learner attempt;
- failure/change injection is safe and scoped.

## 14. Flashcard quality controls

Reject cards that are:
- trivial wording transformations;
- duplicated concepts;
- volatile price memorization;
- arbitrary service limits with no architecture/exam value;
- ambiguous without context;
- sourced only from AI inference.

Prefer cards that test:
- decision boundary;
- requirement-to-choice mapping;
- failure implication;
- constraint/caveat;
- compare/contrast;
- mental-model correction.

## 15. Drift categories and required response

- **Curriculum drift** -> stop and map activity to approved unit/objective.
- **Source drift** -> replace/revalidate with approved authoritative source.
- **Schema drift** -> CI failure; version schema explicitly.
- **Format drift** -> deterministic render failure.
- **Semantic drift** -> run QA/regression, supersede artifact if needed.
- **Depth drift** -> architecture-usefulness review and unit acceptance criteria.
- **Mastery drift** -> future mastery policy controls evidence/state.
- **Model drift** -> regression gate before production use.

## 16. CI is necessary but not sufficient

Automated checks can validate structure, provenance relationships, deterministic rendering, and many policy violations. They cannot prove architectural correctness by themselves.

Source-grounded QA and required human review remain part of the trust model.

## 17. Gate decision

Issue #4 is complete when:
- artifact schema specification is committed;
- JSON Schema and validator are committed;
- deterministic renderer is committed;
- valid/invalid regression fixtures exist;
- CI passes the fixture set in Fedora;
- ChatGPT operating spec is updated from draft to approved anti-drift behavior.

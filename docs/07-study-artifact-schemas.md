# Study Artifact Schemas

Status: **APPROVED v1**  
Issue: **#4**  
Date: **2026-08-09**

## 1. Purpose

Define the canonical artifact types, required provenance, lifecycle, and anti-drift structure for all AI-generated or AI-assisted study material.

The machine-authoritative form is **JSON** validated against versioned JSON Schema. Human-readable Markdown is rendered deterministically from validated JSON. AI must not bypass the schema by directly authoring final approved Markdown.

## 2. Governing principles

1. **Provider material remains source of truth.** Artifacts are derived study aids, never authorities.
2. **Canonical machine form is structured JSON.** Markdown is a presentation layer.
3. **Every factual or provider-recommendation claim must be traceable to one or more approved sources.**
4. **Inference must be labeled.** Provider facts/recommendations and AI synthesis/inference must never share an unlabeled field.
5. **Artifacts are generated only when the approved study workflow calls for them.** Do not create artifact bloat.
6. **Schemas are versioned.** A schema change requires explicit repository change control; the model may not improvise field changes.
7. **Approved artifacts are immutable in meaning.** Material changes create a new version and supersede the old artifact.

## 3. Common provenance envelope

Every artifact contains a top-level `meta` object with these required fields:

```json
{
  "artifact_id": "aws-sap-c02-u03-vpc-routing-architecture-note",
  "artifact_type": "architecture_note",
  "schema_version": "1.0.0",
  "artifact_version": "1.0.0",
  "status": "DRAFT",
  "provider": "AWS",
  "certification": "SAP-C02",
  "exam_scope_version": "2026-08-09",
  "unit_ids": ["U03"],
  "objective_ids": ["1.1"],
  "architecture_domains": ["networking"],
  "processing_classes": ["READ_SELECTIVE_EXTRACT"],
  "source_ids": ["aws-vpc-gateway-route-tables"],
  "prompt_versions": ["extract-v1", "enrich-v1"],
  "model_id": "recorded-at-generation-time",
  "generated_at": "RFC3339 timestamp",
  "last_reviewed_at": null,
  "qa_state": "QA_PENDING"
}
```

### Required source object

Each referenced source must exist in `sources` and include:

```json
{
  "source_id": "aws-vpc-gateway-route-tables",
  "title": "Gateway route tables",
  "canonical_url": "https://docs.aws.amazon.com/...",
  "retrieved_url": "https://docs.aws.amazon.com/...md",
  "provider": "AWS",
  "retrieved_at": "RFC3339 timestamp",
  "source_sha256": "...",
  "normalized_sha256": "...",
  "source_type": "service_user_guide",
  "processing_class": "READ_SELECTIVE_EXTRACT",
  "human_reading_scope": "Rules and considerations",
  "visible_revision": null
}
```

### Required claim object

Content that asserts provider behavior, recommendations, synthesis, inference, or exam interpretation must use claim objects:

```json
{
  "claim_id": "c001",
  "label": "PROVIDER_FACT",
  "text": "...",
  "source_refs": [
    {
      "source_id": "aws-vpc-gateway-route-tables",
      "locator": "Rules and considerations > middlebox routing"
    }
  ],
  "confidence": "HIGH"
}
```

Allowed labels:
- `PROVIDER_FACT`
- `PROVIDER_RECOMMENDATION`
- `CROSS_SOURCE_SYNTHESIS`
- `ARCHITECTURAL_INFERENCE`
- `EXAM_INTERPRETATION`

Rules:
- `PROVIDER_FACT` and `PROVIDER_RECOMMENDATION` require at least one source reference.
- `CROSS_SOURCE_SYNTHESIS` requires at least two source references unless the synthesis is explicitly between sections of one source.
- `ARCHITECTURAL_INFERENCE` requires at least one supporting source reference plus an inference rationale.
- `EXAM_INTERPRETATION` requires an SAP-C02 objective/task reference and at least one supporting source.
- Claims must not cite model memory.

## 4. Lifecycle

Allowed artifact states:

`DRAFT -> QA_PENDING -> REVIEW_REQUIRED -> APPROVED -> SUPERSEDED`

`REVIEW_REQUIRED` may be skipped only when the QA specification explicitly permits automatic approval eligibility; final `APPROVED` status still follows the approved workflow.

No artifact may be used as trusted study material unless `status=APPROVED` and `qa_state=PASS`.

## 5. Core artifact families

The v1 system uses **nine** primary artifact families. Additional formats require an explicit schema change.

### 5.1 `source_summary`

Purpose: compress an approved source at the depth required by its processing class.

Required content:
- `purpose`
- `key_claims[]`
- `constraints_and_caveats[]`
- `unresolved_questions[]`
- `human_reading_completed` (`true|false|not_required`)
- `human_reading_scope`

Rules:
- For `READ_FULL_CONTEXTUALIZE`, summary is a companion **after** human reading.
- For `READ_SELECTIVE_EXTRACT`, summary must cover architecture-relevant unread material and identify the selected reading scope.
- For `EXTRACT_VALIDATE`, output should be dense and factual; do not add architecture inference here.

### 5.2 `architecture_note`

Purpose: put one topic into system-design context.

Required content:
- `problem_statement`
- `requirements_and_drivers[]`
- `provider_grounding[]`
- `design_implications[]`
- `tradeoffs[]`
- `failure_modes[]`
- `security_implications[]`
- `reliability_implications[]`
- `performance_implications[]`
- `cost_implications[]`
- `operational_implications[]`
- `decision_change_triggers[]`
- `open_questions[]`

Provider grounding is separated from inference by claim labels.

### 5.3 `decision_record`

Purpose: reusable ADR-like architecture decision material.

Required content:
- `decision_title`
- `context`
- `requirements[]`
- `constraints[]`
- `options[]`
- `decision`
- `rationale[]`
- `consequences_positive[]`
- `consequences_negative[]`
- `risks[]`
- `when_to_revisit[]`
- `exam_relevance[]`

Each option requires:
- name;
- conditions where it fits;
- conditions where it does not fit;
- tradeoffs;
- supporting claims.

### 5.4 `comparison_matrix`

Purpose: compare plausible alternatives without reducing architecture to a feature table.

Required content:
- `decision_question`
- `options[]`
- `criteria[]`
- `cells[]`
- `selection_rules[]`
- `dangerous_simplifications[]`

Every criterion must be decision-relevant. Avoid trivia columns.

### 5.5 `pattern_note`

Purpose: document an architecture pattern or anti-pattern.

Required content:
- `pattern_kind` (`PATTERN|ANTI_PATTERN`)
- `problem`
- `context`
- `forces[]`
- `structure`
- `when_to_use[]`
- `when_not_to_use[]`
- `failure_behavior[]`
- `tradeoffs[]`
- `related_decisions[]`

### 5.6 `flashcard_set`

Purpose: spaced-repetition material with strict anti-trivia controls.

Allowed card types:
- `CONCEPT`
- `DECISION`
- `CONSTRAINT`
- `COMPARE`
- `FAILURE_MODE`

Required per card:
- `card_id`
- `card_type`
- `front`
- `back`
- `why_it_matters`
- `source_refs[]`
- `objective_ids[]`
- `volatility` (`LOW|MEDIUM|HIGH`)

Rules:
- no unsupported cards;
- no volatile numeric price cards;
- quota numbers are allowed only when architecturally/exam-significant and must be marked `HIGH` volatility;
- prefer “when/why/what changes the decision” over raw recall;
- default maximum: **20 new cards per architecture unit**, unless a reviewed exception is recorded.

### 5.7 `lab_brief`

Purpose: hands-on exercise that validates behavior and architecture understanding.

Required content:
- `lab_level` (`H0|H1|H2|H3|H4`)
- `learning_objectives[]`
- `scenario`
- `requirements[]`
- `constraints[]`
- `allowed_sources[]`
- `acceptance_criteria[]`
- `evidence_to_capture[]`
- `failure_or_change_injection[]`
- `cleanup_requirements[]`
- `estimated_cost_risk` (`NONE|LOW|MEDIUM|HIGH`)

H3/H4 labs must not include full solution steps before the learner attempts the task.

### 5.8 `assessment_set`

Purpose: generated factual/selection/architecture assessment when permitted by QA.

Question types:
- `KNOWLEDGE`
- `SELECTION`
- `ARCHITECTURE`

Required per question:
- prompt;
- type;
- mapped objectives;
- answer/rubric;
- explanation;
- distractor rationale for selected-response questions;
- source references;
- difficulty;
- tested misconception.

Generated assessments must be labeled as generated; never imply they are official AWS questions.

### 5.9 `misconception_record`

Purpose: capture durable errors in the learner’s mental model.

Required content:
- `misconception`
- `evidence`
- `correct_model`
- `root_cause` (`FACT_GAP|DECISION_GAP|REQUIREMENT_MISS|IMPLEMENTATION_GAP|TIME_PRESSURE|OTHER`)
- `source_refs[]`
- `remediation_actions[]`
- `retest_criteria[]`

## 6. Progress/mastery evidence

Mastery state itself is governed by the future mastery specification, but evidence objects used by artifacts must already be structured.

Allowed evidence types:
- `READING`
- `EXPLANATION`
- `LAB`
- `SCENARIO`
- `ASSESSMENT`
- `REMEDIATION`

Evidence records must include:
- unit/objective;
- date;
- evidence type;
- result;
- artifact/lab/assessment reference;
- observed weakness;
- reviewer/assessor provenance.

No evidence object may directly set mastery level without the mastery policy.

## 7. Artifact directory convention

Recommended layout:

```text
artifacts/
  aws/
    sap-c02/
      U03/
        architecture-note-vpc-routing.json
        architecture-note-vpc-routing.md
        decision-tgw-vs-peering.json
        decision-tgw-vs-peering.md
```

JSON is canonical. Markdown must be reproducible from JSON.

## 8. Artifact naming

Use stable lowercase kebab-case names. IDs must encode provider, certification, unit, topic, and type where practical.

Do not include model name in filenames; model identity belongs in metadata.

## 9. Deterministic rendering rule

Rendering rules:
- fixed section order by artifact type;
- no AI-authored headings outside schema fields;
- claim labels rendered visibly where useful;
- source references rendered consistently;
- empty optional sections omitted deterministically;
- the rendered Markdown contains a generated-file warning and artifact/schema version.

A Markdown file edited manually is considered drift unless the corresponding JSON changes and the renderer reproduces it.

## 10. Schema-change policy

Any change to required fields, allowed labels, artifact families, lifecycle, or semantics requires:

1. schema version increment;
2. documentation update;
3. regression fixtures update;
4. CI passing;
5. migration decision for existing approved artifacts.

ChatGPT may propose schema changes but may not apply them implicitly during study.

## 11. Explicit non-artifacts

The following do not automatically become trusted repository artifacts:
- casual chat explanations;
- brainstorming;
- raw extraction output before QA;
- raw lab terminal logs;
- temporary prompts;
- unreviewed diagrams;
- copied AWS documentation;
- practice answers before assessment completion.

## 12. Approval

This specification becomes operational together with `docs/08-quality-assurance-spec.md` and executable schema/QA checks from Issue #4.

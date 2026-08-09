# Source Classification Policy

Status: **APPROVED v1 POLICY — AI execution requires pipeline validation**  
Policy approval date: **2026-08-09**

## Scope

Define which provider materials enter the study system and how each document or section is treated.

## Default source policy

For the AWS SAP-C02 pilot, official AWS material is the default authoritative corpus. Third-party certification courses are excluded from the curriculum unless this policy is deliberately changed.

The classifications below are now the approved **study-treatment policy**. Issue #3 must still demonstrate that the extraction pipeline can execute `READ_SELECTIVE_EXTRACT` and `EXTRACT_VALIDATE` with acceptable completeness, fidelity, consistency and time savings before AI-derived material becomes trusted study content.

## Processing classes

### `READ_FULL_CONTEXTUALIZE`
Use only when the value lies in architectural reasoning, principles, decision process, or an integrated argument that should be understood as a whole **and the approved reading scope is sufficiently high-value to justify full human reading**.

Processing:
1. Human reads the complete approved scope.
2. AI produces a source-grounded companion summary.
3. AI extracts decisions, trade-offs, principles, and implications.
4. AI places the material in architectural context.
5. Human/AI discussion tests understanding.

Typical material:
- SAP-C02 exam guide/task definitions;
- Well-Architected framework-level foundation and short pillar design-principle scopes;
- selected high-value architecture/strategy/decision sources whose reasoning continuity is important.

**Full reading is the exception, not the default.** A large document is not assigned this class merely because it is important.

### `READ_SELECTIVE_EXTRACT`
Default class for large architecture/service sources that contain important reasoning but whose full end-to-end reading would have low marginal value.

Processing:
1. Source packet identifies the relevant architecture problem/objectives.
2. AI/pipeline identifies candidate high-value sections and extracts architecture-relevant information from the approved remainder.
3. Human reads selected passages/sections.
4. AI contextualizes and synthesizes only after grounded extraction.
5. QA validates the unread-section extraction according to Issue #3/#4 controls.

Typical material:
- detailed Well-Architected pillar guidance;
- service user guides;
- AWS Security Reference Architecture;
- Prescriptive Guidance;
- security/resilience/networking/performance sections;
- large decision/strategy guides;
- extensive best-practice collections.

### `EXTRACT_VALIDATE`
Use for dense factual or volatile material where structured AI compression should save substantial time and architectural reasoning continuity is limited.

Processing:
1. AI extracts against a fixed versioned schema.
2. QA checks source fidelity/completeness and required provenance.
3. Human reads source only for flagged/high-impact items, QA sampling, contradictions, or unresolved questions.
4. Volatile facts are refreshed rather than memorized blindly.

Typical material:
- feature matrices;
- FAQs;
- limits/quotas;
- service scope/availability details;
- pricing mechanics;
- configuration capability references;
- selected monitoring/troubleshooting facts.

### `REFERENCE_ONLY`
Do not summarize by default. Retrieve when a decision, implementation, lab, troubleshooting task, or exact confirmation requires it.

Typical material:
- API references;
- SDK/CLI references;
- exhaustive parameter documentation;
- low-value implementation detail;
- document history except for freshness checks.

### `HANDS_ON`
Use to build or validate practical capability rather than as a primary reading source.

Candidate material:
- Builder Labs;
- SimuLearn;
- AWS Workshops;
- Well-Architected Labs;
- selected tutorials/implementation guides;
- custom controlled AWS-account challenges where no official lab fits.

Hands-on exists to validate **behavior and architectural consequences**, not simply completion of console steps.

Hands-on levels:
- `H0` — no lab required;
- `H1` — focused mechanic/behavior;
- `H2` — integrated multi-service scenario;
- `H3` — open requirements challenge with limited implementation guidance;
- `H4` — failure/change injection after a working design.

### `ASSESSMENT`
Use for readiness measurement and feedback, not primary teaching.

Candidate material:
- official Practice Question Set;
- official Practice Exam;
- official exam-prep questions;
- system-generated assessments after QA approval.

Assessment controls:
- early official question set is diagnostic;
- official full practice exam is preserved for late readiness measurement;
- repeated memorized questions are not mastery evidence.

## Section-level override

Classification applies at both document and section level. A single service guide can contain:

- architecture/security/resilience sections as `READ_SELECTIVE_EXTRACT`;
- how-to material as `HANDS_ON`;
- quotas as `EXTRACT_VALIDATE`;
- API/CLI material as `REFERENCE_ONLY`.

This is the default for large service guides rather than assigning the entire guide one treatment.

## Architecture-first ordering rule

For normal architecture units, source use follows this sequence:

1. exam objective/requirements;
2. approved architecture principles/guidance;
3. decision alternatives;
4. targeted service documentation;
5. factual/volatile references;
6. hands-on behavior validation;
7. failure/change challenge;
8. assessment and mastery update.

Do not start a unit by walking a service manual from beginning to end.

See `04-study-sequence-spec.md` for the full workflow.

## Required source metadata

Every selected/inventoried source should capture:

- source ID;
- exact title;
- provider;
- canonical URL or stable identifier;
- source/document type;
- certification/objective mapping;
- architecture-domain mapping;
- processing class;
- required human-reading scope;
- publication/update/version metadata when available;
- retrieval date;
- access model where relevant;
- QA status;
- notes about supersession, conflicts or freshness risk.

## Source-packet size control

Initial source packets should remain small and expand only when demonstrated gaps remain. The default target is:

- one scope/objective source;
- one or two core architecture sources;
- one decision/reference-architecture source where useful;
- targeted service sections for the main alternatives;
- factual references only as needed;
- one primary hands-on activity plus optional challenge extension.

Do not preload dozens of documents simply because they are official.

## Freshness and conflict rule

- Prefer current canonical provider documentation.
- When official sources appear contradictory or superseded, surface the conflict rather than silently merging guidance.
- Model memory is never a substitute for current authoritative material when the pipeline expects source grounding.
- Newly launched services are mapped to existing architecture decisions before being added to the curriculum.

## Pipeline-validation boundary

Policy approval does **not** mean AI summaries/extractions are trusted automatically.

Before study starts, Issue #3 must validate at least:

- source acquisition/normalization;
- section selection quality;
- extraction completeness;
- fidelity to provider statements;
- separation of provider statements from architectural inference;
- repeatability/consistency;
- material human-reading time savings;
- acceptable operational overhead on Fedora Linux.

Issue #4 must then define artifact schemas/provenance/QA enforcement.

Only outputs that pass those controls can enter the approved study knowledge base.

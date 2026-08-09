# Source Classification Policy

Status: **APPROVED v1.1 — pipeline and artifact controls validated**  
Policy approval date: **2026-08-09**

## Scope

Define which provider materials enter the study system and how each document or section is treated.

For the AWS SAP-C02 pilot, current official AWS material is the default authoritative corpus. Third-party certification courses are excluded unless this policy is deliberately changed.

The processing classes below are operational. Trusted AI-derived material still requires the current extraction pipeline to be `GREEN`, source-grounded QA to pass, and downstream artifact controls to pass where applicable.

## Processing classes

### `READ_FULL_CONTEXTUALIZE`
Use when architectural reasoning, principles, decision process, or integrated argument should be understood as a whole and the approved scope is sufficiently high-value to justify full human reading.

Processing:
1. Human reads the complete approved scope.
2. AI produces a source-grounded companion summary.
3. AI extracts decisions, trade-offs, principles, and implications.
4. AI places the material in architectural context after grounded QA.
5. Human/AI discussion tests understanding.

Typical material:
- SAP-C02 exam guide/task definitions;
- Well-Architected framework-level foundation and short pillar design-principle scopes;
- selected high-value architecture/strategy/decision sources whose reasoning continuity matters.

Full reading is the exception, not the default.

### `READ_SELECTIVE_EXTRACT`
Default for large architecture/service sources containing valuable reasoning where complete reading has low marginal value.

Processing:
1. Source packet identifies the architecture problem/objectives.
2. Pipeline identifies candidate high-value sections and extracts architecture-relevant information from the approved remainder.
3. Grounded extraction passes QA before enrichment.
4. Human reads selected passages/sections.
5. AI contextualizes/synthesizes only from approved, grounded material.

Typical material:
- detailed Well-Architected pillar guidance;
- service user guides;
- AWS Security Reference Architecture;
- Prescriptive Guidance;
- security/resilience/networking/performance sections;
- large decision/strategy guides.

### `EXTRACT_VALIDATE`
Use for dense factual or volatile material where structured compression saves substantial time and reasoning continuity is limited.

Processing:
1. AI extracts against the versioned contract.
2. QA checks source fidelity, completeness, qualifiers, and provenance.
3. Human reads source only for flagged/high-impact items, QA sampling, contradictions, or unresolved questions.
4. Volatile facts are refreshed at use time rather than memorized blindly.

Typical material:
- feature matrices;
- FAQs;
- limits/quotas;
- service scope/availability;
- pricing mechanics;
- capability/configuration references;
- selected monitoring/troubleshooting facts.

### `REFERENCE_ONLY`
Do not summarize by default. Retrieve only when a decision, implementation, lab, troubleshooting task, or exact confirmation requires it.

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
- custom controlled AWS-account challenges when no official lab fits.

Hands-on validates behavior and architectural consequences, not console-step completion.

Levels:
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

Controls:
- early official question set is diagnostic;
- official full practice exam is preserved for late readiness measurement;
- repeated memorized questions are not mastery evidence.

## Section-level override

Classification applies at document and section level. A service guide can contain architecture/security/resilience sections as `READ_SELECTIVE_EXTRACT`, how-to material as `HANDS_ON`, quotas as `EXTRACT_VALIDATE`, and API/CLI material as `REFERENCE_ONLY`.

## Architecture-first ordering rule

For normal architecture units:

1. exam objective/requirements;
2. approved architecture principles/guidance;
3. decision alternatives;
4. targeted service documentation;
5. factual/volatile references;
6. hands-on behavior validation;
7. failure/change challenge;
8. assessment and mastery update.

Do not begin a unit by walking a service manual from beginning to end. See `04-study-sequence-spec.md`.

## Required source metadata

Every selected/inventoried source should capture:

- source ID;
- exact title;
- provider;
- canonical URL/stable identifier;
- source/document type;
- certification/objective mapping;
- architecture-domain mapping;
- processing class;
- required human-reading scope;
- publication/update/version metadata when available;
- retrieval date;
- access model where relevant;
- QA status;
- supersession/conflict/freshness notes.

## Source-packet size control

Initial source packets remain small and expand only when demonstrated gaps remain. Default target:

- one scope/objective source;
- one or two core architecture sources;
- one decision/reference-architecture source where useful;
- targeted service sections for main alternatives;
- factual references only as needed;
- one primary hands-on activity plus optional challenge extension.

Do not preload dozens of documents simply because they are official.

## Freshness and conflict rule

- Prefer current canonical provider documentation.
- Surface official-source conflicts/supersession rather than silently merging them.
- Model memory never substitutes for current authoritative material when source grounding is required.
- Newly launched services map to existing architecture decisions before entering curriculum.
- Apply `docs/13-change-control-freshness.md` freshness tiers and impact rules.

## Pipeline/QA boundary

Policy approval does not make AI output trusted automatically.

Before trusted extraction/enrichment or pipeline-derived artifact generation:

- `state/pipeline-health.json` must be `GREEN` for the current pipeline fingerprint;
- source acquisition/normalization and provenance must be valid;
- grounded extraction must pass source-fidelity/completeness QA;
- provider facts and inference must remain separated;
- human-reading requirements for the processing class must be satisfied;
- artifact schema/provenance/QA rules must pass before artifact approval.

The representative pipeline pilot and artifact QA gates have passed; production per-source QA remains mandatory.

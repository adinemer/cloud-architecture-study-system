# Study System Architecture

Status: **APPROVED v1.0 — pre-study architecture**

## Logical architecture

```text
GOVERNANCE / CONTROL
  - charter + ChatGPT operating spec
  - certification source of truth + objective map
  - source policy + study sequence
  - extraction/pipeline-health controls
  - artifact schema + QA
  - progress/mastery state
  - study-session + ChatGPT-chat controls
  - operating routine + tool policy
  - change/freshness control
          |
          v
KNOWLEDGE PIPELINE
  discover -> validate -> classify -> acquire -> normalize
  -> grounded extraction -> extraction QA -> required human reading
  -> summarize -> architecture enrichment -> cross-source synthesis
  -> artifact generation -> artifact QA -> approve/version
          |
          v
STUDY EXPERIENCE
  orient -> cold recall -> read/review/discuss -> decide
  -> lab/failure exercise -> retrieve/assess -> remediate
  -> evidence/mastery update -> close/archive session
```

## Design principles

### 1. Control before content
Repository specifications and state govern the process. ChatGPT chats execute the process but do not redefine it implicitly.

### 2. Repository before recommendation
Before substantive study-system recommendations or controlled actions, ChatGPT resolves the current authoritative GitHub controls/state. Conversation memory is not authority.

### 3. Separate extraction from interpretation
The pipeline first establishes provider-grounded facts/recommendations and validates them. Architectural enrichment happens only after grounded extraction passes QA.

### 4. Section-level classification
Large provider documents may contain architecture reasoning, tutorials, references, quotas, and troubleshooting. Processing class therefore applies at document and section level.

### 5. Minimum viable pipeline
Use inspectable Markdown/JSON, deterministic scripts, and small objective-driven source packets. Add RAG/vector/agent/custom-app infrastructure only after measured need.

### 6. Explicit pipeline health
Trusted extraction/enrichment requires `state/pipeline-health.json` to be `GREEN` for the current pipeline fingerprint. Failed/stale pipeline state blocks downstream trust.

### 7. Persistent provenance
Every approved study artifact remains traceable to certification scope/objectives, provider sources, source hashes, processing class, schema/prompt versions, model ID, QA state, and study session.

### 8. Evidence-based learning state
Reading and generated notes are activities, not mastery. Exam readiness, architecture mastery, and hands-on capability are tracked independently from controlled evidence.

### 9. Single-purpose chat/session model
One controlled ChatGPT chat maps to one repository study session and one meaningful learning purpose. GitHub stores resumable/authoritative state so conversation history is optional context.

## Implemented control document set

- `00-system-charter.md`
- `01-system-architecture.md`
- `02-chatgpt-operating-spec.md`
- `03-source-policy.md`
- `04-study-sequence-spec.md`
- `05-extraction-pipeline-spec.md`
- `07-study-artifact-schemas.md`
- `08-quality-assurance-spec.md`
- `09-progress-mastery-spec.md`
- `10-tooling-evaluation.md`
- `11-study-session-management.md`
- `12-coordinator-governance.md`
- `13-change-control-freshness.md`
- `14-study-operating-routine.md`
- `15-study-tool-policy.md`
- `16-chat-session-management.md`
- `17-pipeline-health-spec.md`
- `aws/sap-c02/source-inventory.md`
- `aws/sap-c02/objective-map.md`

Architecture enrichment does **not** require a separate `06-*` governance document in v1. Its contract is intentionally owned by `05-extraction-pipeline-spec.md`, `prompts/enrich-v1.md`, artifact schemas, and QA controls to avoid duplicate authority.

## Machine-control layers

- `schemas/` — artifact/session/chat/state/change/pipeline-health contracts;
- `state/` — authoritative project, mastery, and pipeline-health state;
- `sessions/` — controlled learner session/chat history;
- `pipeline/` — deterministic source acquisition/normalization/bundling;
- `prompts/` — versioned extraction/enrichment/artifact/QA contracts;
- `qa/` — validators, regressions, dry runs, readiness evidence;
- `.github/workflows/` — Fedora pipeline, artifact, and control-plane CI.

## Study-start boundary

Technical readiness and explicit study-start approval are independent. Even when every technical control passes, real SAP-C02 study remains blocked while `state/project-state.json` has `study_start_approval=BLOCKED`.

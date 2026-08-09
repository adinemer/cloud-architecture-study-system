# Study Session Management Specification

Status: **APPROVED v1**  
Certification: **AWS SAP-C02**

## Purpose

Make each study session a controlled, recoverable, auditable unit of work. A ChatGPT conversation is only an interaction surface; it is not the authoritative session record.

## Session identity

Every session has an immutable ID:

`SAP-C02-<UNIT>-S<NNN>`

Example: `SAP-C02-U03-S004`.

IDs are never reused. Resumed work continues the same session unless the original session was completed/aborted and a new controlled session is required.

## Lifecycle

```text
PLANNED -> READY -> ACTIVE -> REVIEW_PENDING -> COMPLETED -> ARCHIVED
             |        |            |
             v        v            v
           BLOCKED  PAUSED       BLOCKED

terminal exception: ABORTED
historical replacement: SUPERSEDED
```

### PLANNED
Coordinator has proposed the session from the approved plan.

Required:
- unit/objective mapping;
- session type;
- intended sources/activities;
- entry criteria.

### READY
All prerequisites, required governance reads, source approvals, and required prior sessions are satisfied.

### ACTIVE
Learner has started the session. Only one normal SAP-C02 study session may be `ACTIVE` at a time unless the coordinator records an explicit parallel-session exception.

### PAUSED
Session is intentionally interrupted. Resume data must be sufficient to continue without reconstructing state from chat memory.

### REVIEW_PENDING
Primary activity is done but closure checks remain: artifact QA, assessment grading, mastery update, unresolved questions, cleanup, or summary.

### COMPLETED
All completion criteria pass. Completion is a controlled state transition, not a conversational phrase.

### ARCHIVED
Completed historical record retained for retrieval. Archival does not remove evidence links.

### BLOCKED
A required dependency, source, control check, lab environment, or unresolved critical issue prevents progress.

### ABORTED
Session intentionally ended without meeting completion criteria. Reason and useful evidence are retained.

### SUPERSEDED
Historical record replaced/corrected by a newer explicitly linked record; original remains immutable.

## Session types

Allowed v1 types:

- `SCOPE_BASELINE`
- `READING`
- `EXTRACTION_REVIEW`
- `INSTRUCTION_DISCUSSION`
- `ARCHITECTURE_DECISION`
- `LAB`
- `ASSESSMENT`
- `REMEDIATION`
- `CAPSTONE`
- `READINESS_REVIEW`

A session may combine closely related activities, but its declared primary type controls required fields and completion checks.

## Mandatory session manifest

Each session records:

- session ID and schema version;
- certification/exam scope version;
- unit IDs and objective IDs;
- primary session type;
- status;
- control snapshot ID;
- authoritative documents consulted at session creation;
- source packet IDs/URLs;
- prerequisite session IDs;
- required artifact types;
- planned activity and exit criteria;
- start/end timestamps;
- elapsed learner time where measurable;
- human-reading minutes;
- activities actually completed;
- artifacts created/updated;
- assessments/lab evidence;
- misconceptions opened/resolved;
- mastery changes proposed/applied;
- unresolved questions/blockers;
- next permitted action;
- completion QA result.

## Authoritative location

```text
sessions/<session-id>/session.json
sessions/<session-id>/summary.md
```

`session.json` is canonical. `summary.md` is deterministic/rendered or coordinator-maintained from the canonical record and must not contradict it.

Artifacts remain under `artifacts/`; session records link to them rather than embedding duplicate authoritative copies.

## Creation control

Before creating a session, the coordinator must consult the repository authority set defined in `docs/12-coordinator-governance.md`.

The coordinator must prove:

1. the proposed session follows the approved sequence or has an approved exception;
2. prerequisites are satisfied;
3. no conflicting active session exists;
4. objectives exist in the current objective map;
5. source processing follows policy;
6. the source packet is current enough for the planned work;
7. required artifact schemas/prompts are current;
8. any required lab/assessment is allowed at this stage.

If these cannot be established, the session is `BLOCKED`, not improvised.

## Session startup contract

At the beginning of an actual learner interaction, ChatGPT internally resolves and records:

- current session ID;
- current unit/objectives;
- session purpose;
- allowed source packet;
- current mastery state;
- prior unresolved misconceptions;
- required outputs;
- exit criteria;
- current control snapshot.

The learner should receive a concise orientation, not the full administrative manifest unless requested.

## During-session control

ChatGPT must:

- use only approved sources for authoritative claims;
- record new unresolved questions rather than invent answers;
- create only artifacts permitted by the session manifest;
- link artifacts/evidence to the session ID;
- detect scope drift and return to the session objective;
- record meaningful plan deviations explicitly;
- distinguish teaching discussion from mastery evidence;
- preserve H3/H4 lab solution withholding rules;
- update pause/resume information before a session is interrupted.

## Pause/resume

A paused session must record:

- last completed activity;
- exact next activity;
- pending reading/source location;
- pending artifacts/QA;
- unresolved questions;
- lab state/cleanup risk if applicable;
- learner evidence already captured.

On resume, ChatGPT consults `session.json` before using conversational context. Old conversation content may help presentation but does not override session state.

## Completion gate

A session may transition to `COMPLETED` only if:

1. declared exit criteria are satisfied;
2. required reading/activity is recorded;
3. required artifacts exist and have required QA state;
4. required lab cleanup is complete or explicitly transferred to a controlled follow-up;
5. assessment result is recorded when applicable;
6. misconceptions discovered are recorded;
7. mastery/progress updates have been evaluated under `docs/09-progress-mastery-spec.md`;
8. unresolved HIGH-severity blocker is zero or explicitly moves the session to `BLOCKED` instead;
9. `next_permitted_action` is resolved from repository state;
10. session completion QA passes.

ChatGPT must not mark a session complete because the learner says “done” if mandatory controls are unmet. It should explain the remaining controlled step concisely.

## Session summary

Every completed session must have a compact summary optimized for future retrieval:

- purpose;
- what was completed;
- key architecture decisions/mental models;
- artifacts/evidence;
- misconceptions/gaps;
- mastery impact;
- unresolved items;
- next permitted action.

This summary is an index, not a replacement for approved artifacts.

## Historical retrieval

When asked to revisit older study work, ChatGPT should search GitHub by session ID, unit, objective, artifact ID, or topic, then consult the canonical session/artifact state.

It should not reconstruct old sessions from model memory when repository records exist.

## Corrections

Completed session history is append-only in meaning.

If a material error is discovered:

1. create correction/superseding record;
2. link original session;
3. update affected artifact/mastery state under change control;
4. preserve the original audit trail.

## Administrative burden rule

Routine session creation, state transitions, summaries, evidence linking, and mastery updates are coordinator responsibilities. The learner should not be asked to manually maintain GitHub records unless automation is unavailable and the missing action is genuinely necessary.

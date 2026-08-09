# Study Session Management Specification

Status: **APPROVED v1.1**  
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
- entry criteria;
- predecessor session/handoff relationship if one exists.

### READY
All prerequisites, required governance reads, source approvals, required prior sessions, and predecessor-handoff checks are satisfied.

### ACTIVE
Learner has started the session. Only one normal SAP-C02 study session may be `ACTIVE` at a time unless the coordinator records an explicit parallel-session exception.

A successor with a predecessor may not become ACTIVE until it has formally consumed the predecessor handoff.

### PAUSED
Session is intentionally interrupted. Resume data must be sufficient to continue without reconstructing state from chat memory.

### REVIEW_PENDING
Primary activity is done but closure checks remain: artifact QA, assessment grading, mastery update, unresolved questions, cleanup, summary, or handoff preparation.

### COMPLETED
All completion criteria pass, including mandatory formal handoff creation. Completion is a controlled state transition, not a conversational phrase.

### ARCHIVED
Completed historical record retained for retrieval. Archival does not remove evidence or handoff links.

### BLOCKED
A required dependency, source, control check, lab environment, or unresolved critical issue prevents progress.

### ABORTED
Session intentionally ended without meeting normal completion criteria. Reason/useful evidence are retained and a formal handoff still records what can safely continue.

### SUPERSEDED
Historical record replaced/corrected by a newer explicitly linked record; original remains immutable and retains a formal handoff/correction trail.

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
- predecessor session ID where one exists;
- consumed predecessor handoff ID where applicable;
- its own mandatory terminal handoff ID when terminal;
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
sessions/<session-id>/chat.json
sessions/<session-id>/handoff.json
sessions/<session-id>/summary.md
```

`session.json` is canonical for session state. `handoff.json` is canonical for cross-session continuity. `summary.md` is an index and must not contradict canonical records.

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
8. any required lab/assessment is allowed at this stage;
9. if a predecessor exists, its handoff exists, is current, and is linked to this successor correctly.

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
- current control snapshot;
- predecessor handoff consumption/reconciliation where applicable.

The learner should receive a concise orientation, not the full administrative manifest unless requested.

## During-session control

ChatGPT must:

- use only approved sources for authoritative claims;
- require semantic-integrity PASS for trusted extraction/enrichment outputs;
- record new unresolved questions rather than invent answers;
- create only artifacts permitted by the session manifest;
- link artifacts/evidence to the session ID;
- detect scope drift and return to the session objective;
- record meaningful plan deviations explicitly;
- distinguish teaching discussion from mastery evidence;
- preserve H3/H4 lab solution withholding rules;
- update pause/resume information before interruption.

## Pause/resume

A paused session must record:

- last completed activity;
- exact next activity;
- pending reading/source location;
- pending artifacts/QA;
- unresolved questions;
- lab state/cleanup risk if applicable;
- learner evidence already captured.

On resume, ChatGPT consults `session.json` before conversational context. Old conversation content may help presentation but does not override session state.

Pause/resume within the same session does not create a successor handoff. A transfer to a different controlled session follows `docs/19-session-handoff-continuity.md`.

## Completion gate

A session may transition to `COMPLETED` only if:

1. declared exit criteria are satisfied;
2. required reading/activity is recorded;
3. required artifacts exist and have required QA state;
4. required lab cleanup is complete or explicitly represented in continuity state;
5. assessment result is recorded when applicable;
6. misconceptions discovered are recorded;
7. mastery/progress updates have been evaluated under `docs/09-progress-mastery-spec.md`;
8. unresolved HIGH-severity blocker is zero or session becomes `BLOCKED` instead;
9. `next_permitted_action` is resolved from repository state;
10. mandatory `handoff.json` is created and validates;
11. chat closure/target state matches the handoff;
12. session completion QA passes.

`ABORTED` and `SUPERSEDED` are also terminal and require formal handoff records describing what state can safely continue.

ChatGPT must not mark a session complete because the learner says “done” if mandatory controls are unmet.

## Session summary

Every completed session must have a compact summary optimized for future retrieval:

- purpose;
- what was completed;
- key architecture decisions/mental models;
- artifacts/evidence;
- misconceptions/gaps;
- mastery impact;
- unresolved items;
- next permitted action;
- handoff ID.

This summary is an index, not a replacement for approved artifacts or the handoff record.

## Formal handoff continuity

Cross-session continuity is governed by `docs/19-session-handoff-continuity.md`.

A terminal session always produces handoff state even if no successor has yet been selected. A successor must explicitly record `predecessor_session_id` and `consumed_handoff_id`; active-or-later successor state without that consumption is invalid.

The coordinator, not the learner, creates and consumes these records.

## Historical retrieval

When asked to revisit older study work, ChatGPT should search GitHub by session ID, unit, objective, artifact ID, or topic, then consult canonical session/chat/handoff/artifact state.

It should not reconstruct old sessions from model memory when repository records exist.

## Corrections

Completed session history is append-only in meaning.

If a material error is discovered:

1. create correction/superseding record;
2. link original session/handoff;
3. update affected artifact/mastery state under change control;
4. preserve original audit trail.

## Administrative burden rule

Routine session creation, state transitions, summaries, evidence linking, mastery updates, handoff generation, and handoff consumption are coordinator responsibilities. The learner should not be asked to manually maintain GitHub records unless automation is unavailable and the missing action is genuinely necessary.

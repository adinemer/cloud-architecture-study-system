# ChatGPT Chat Session Management

Status: **APPROVED v1 — study start remains frozen**

## Purpose

Bind each controlled repository study session to an organized, single-purpose ChatGPT conversation so chat history remains understandable and recoverable without becoming authoritative state.

## Core rule

**One ChatGPT chat = one controlled learning purpose.**

A chat may contain multiple tightly related activities required to complete that purpose, but it must not accumulate unrelated curriculum topics, labs, assessments, planning, or troubleshooting.

GitHub remains authoritative. ChatGPT chat is the working interaction surface.

## Chat identity

Every controlled study chat is bound to exactly one `session_id`.

Recommended title format:

`SAP-C02 | <UNIT> | <SESSION-ID> | <short purpose>`

Example:

`SAP-C02 | U07 | SAP-C02-U07-S003 | S3 data-protection decisions`

The stable session ID is the primary lookup key even if the visible ChatGPT title is edited.

## Chat contract

Each controlled chat records:

- `session_id`;
- `chat_title`;
- one-sentence `purpose`;
- `primary_session_type`;
- `allowed_scope[]`;
- `out_of_scope[]`;
- `startup_repository_snapshot_id`;
- `status` (`PLANNED|OPEN|PAUSED|CLOSED|SUPERSEDED`);
- `opened_at` / `closed_at` where applicable;
- `handoff_required`;
- `handoff_target_session_id` where applicable;
- `resume_anchor` for paused chats.

Canonical representation:

`sessions/<session-id>/chat.json`

## Creation rule

A controlled study chat must not be created before the repository session reaches `READY`.

Before opening the chat, the coordinator must resolve from GitHub:

- certification/unit/objectives;
- current session purpose;
- allowed sources;
- current mastery/misconceptions;
- required artifacts/evidence;
- exit criteria;
- valid control snapshot;
- study-start permission.

If study start is frozen/blocked, no real study chat may be created.

## Startup behavior

At the first learner interaction in the chat, ChatGPT should present a concise orientation:

- session purpose;
- what will be accomplished;
- source/activity mode;
- expected exit condition.

It should not dump governance metadata unless requested.

## Single-purpose scope enforcement

Examples of acceptable same-chat activity:

- read selected S3 replication sections;
- discuss their architecture implications;
- challenge the learner with a changed-RPO scenario;
- produce/update the required decision artifact for that same purpose.

Examples that require another session/chat:

- moving from S3 replication to unrelated Transit Gateway architecture;
- beginning a Kubernetes lab;
- performing general exam-readiness assessment during a reading session;
- redesigning the study plan;
- troubleshooting the learner's workstation unless that troubleshooting is the declared controlled session purpose.

## Tangent rule

When the learner asks an out-of-scope question during an active chat:

1. if it is a tiny clarification necessary to understand the active topic, answer it and remain in scope;
2. otherwise record it as a future-question/session candidate;
3. provide a short answer only if doing so cannot alter study state or derail the current purpose;
4. return to the active purpose;
5. create a new controlled chat only when repository state authorizes that new session.

Do not silently broaden the current chat.

## Chat purpose granularity

Do not make chats so narrow that administration overwhelms learning.

Good purpose:
- “Understand and decide S3 data-protection architecture.”

Too broad:
- “Learn AWS storage.”

Too narrow:
- “Read paragraph 3 of the S3 Versioning page.”

The purpose should normally map to one meaningful learning/assessment/lab outcome.

## Pause/resume

If the chat is paused, `chat.json` and `session.json` must record enough resume state to continue without rereading the full conversation:

- last completed activity;
- next activity;
- current source locator;
- current question/decision;
- pending artifact/QA;
- unresolved misconception;
- lab cleanup risk where applicable.

On resume, ChatGPT reads GitHub state first. Conversation history is supporting context only.

## Chat closure

A chat is closed when:

- its repository session reaches `COMPLETED`, `ABORTED`, or `SUPERSEDED`; or
- work is intentionally transferred to a different authorized session/chat.

Closure behavior:

1. verify session completion/exception state;
2. ensure canonical session/artifact/state writes are complete;
3. create/update compact session summary;
4. set `chat.status=CLOSED`;
5. record the next permitted session/action.

A learner saying “done” does not itself close the controlled chat if completion requirements remain.

## Handoff to a new chat

A handoff must state:

- source session/chat;
- reason for split;
- target purpose;
- relevant artifact/session IDs;
- unresolved items transferred;
- what is deliberately not transferred.

Do not require the learner to copy long conversation transcripts between chats.

## Historical retrieval

To revisit old work:

1. search by session ID/unit/topic/artifact in GitHub;
2. read `session.json`, `chat.json`, and session summary;
3. consult approved artifacts/evidence;
4. use old chat history only if additional conversational nuance is useful.

A new review/remediation purpose normally receives a new session/chat while linking the historical session.

## Non-study chats

Planning, system design, pipeline testing, tool evaluation, and casual certification questions are **not automatically controlled study chats** and do not receive mastery credit.

When study is unfrozen, the coordinator must keep these management conversations separate from real learner sessions.

## Administrative burden

Chat title, chat/session mapping, scope, pause/resume metadata, closure, and handoff records are coordinator responsibilities. The learner should not manually maintain them during normal operation.

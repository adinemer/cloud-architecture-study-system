# Session Handoff Continuity Specification

Status: **APPROVED v1 — pre-unfreeze hardening**

## Purpose

Guarantee seamless continuity between controlled ChatGPT study sessions without relying on conversation memory or requiring the learner to manually transfer context.

## Hard invariant

Every controlled study session that reaches `COMPLETED`, `ABORTED`, or `SUPERSEDED` must produce a canonical `handoff.json` before the session/chat is considered properly closed.

Every successor session with a predecessor must explicitly consume the predecessor handoff before it may become `ACTIVE`.

No terminal session may silently end without continuity state, and no successor may infer continuity from chat history alone.

## Canonical locations

For each controlled session:

```text
sessions/<session-id>/session.json
sessions/<session-id>/chat.json
sessions/<session-id>/handoff.json
```

Machine contract:

`schemas/handoff-v1.schema.json`

Validation:

`qa/validate_handoffs.py`

## Required handoff content

A handoff records at minimum:

- handoff ID;
- source session ID and chat title;
- source terminal status;
- source control-snapshot ID;
- completed purpose;
- objectives covered;
- sources used;
- artifact IDs;
- evidence IDs;
- mastery changes;
- active misconceptions;
- unresolved items;
- decisions and mental models established;
- pending QA;
- lab cleanup obligations;
- deferred questions;
- next-session disposition;
- target session ID when already selected;
- next recommended purpose;
- next prerequisites;
- authorities the successor must reload;
- facts/state the successor must **not infer** from prior conversation memory;
- continuity notes.

## Next-session disposition

Allowed values:

- `TARGET_SELECTED` — an exact successor session ID has already been resolved;
- `NEXT_SESSION_PENDING_COORDINATOR_SELECTION` — continuity is preserved but the coordinator has not yet selected the next controlled session;
- `NO_FURTHER_SESSION_REQUIRED` — terminal study path or explicitly completed workflow.

A handoff must not invent a target session merely to satisfy the contract.

## Successor consumption

A successor `session.json` records:

- `predecessor_session_id`;
- `consumed_handoff_id`.

Before activation, ChatGPT must:

1. read the predecessor handoff from GitHub;
2. reload current mandatory authorities/state;
3. compare handoff assumptions with current repository state and freshness;
4. surface any conflict, supersession, stale source, changed mastery state, changed pipeline state, or changed next action;
5. record the exact predecessor handoff ID as consumed;
6. only then open/activate the successor learning purpose.

If the handoff conflicts with current authoritative GitHub state, current GitHub state wins and the discrepancy must be resolved explicitly.

## Chat closure

A controlled ChatGPT chat may be marked `CLOSED` only when:

- the repository session has reached an appropriate terminal state;
- canonical state/artifact writes are complete;
- the mandatory handoff has been created;
- the chat's handoff target, if any, matches the handoff record;
- the next permitted action is recorded.

`handoff_required` is therefore always true for controlled study chats.

## Pause versus handoff

Normal pause/resume within the same controlled chat uses the existing resume anchor and does not require a successor handoff.

If work is intentionally transferred to a different controlled chat/session instead of resumed in the same chat, the source session must produce the formal handoff appropriate to its terminal/transfer state.

## Administrative responsibility

The coordinator creates, validates, stores, and consumes handoff records. The learner must not be asked to copy conversation summaries between chats during normal operation.

## Negative controls

CI/regression must fail for at least:

- terminal session with no `handoff.json`;
- handoff source session mismatch;
- handoff/chat snapshot mismatch;
- chat target different from handoff target;
- successor references predecessor but does not consume its handoff;
- successor consumes an unrelated handoff;
- predecessor targets a different successor;
- handoff marked resolved/targeted without required target information.

## End-to-end proof

Synthetic pre-study validation must exercise at least:

`Session A -> COMPLETED/CLOSED -> handoff A -> Session B consumes handoff A -> ACTIVE -> COMPLETED/CLOSED -> handoff B`

The synthetic chain must leave learner mastery unchanged and preserve the explicit study-start freeze.

## Study-start boundary

`mandatory_session_handover=PASS` is required before technical readiness returns to `READY_TO_START`. It does not itself unfreeze study.

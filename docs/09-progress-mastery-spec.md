# Progress and Mastery Specification

Status: **APPROVED v1**  
Certification: **AWS SAP-C02**

## Purpose

Track learning progress from evidence rather than conversation impressions, reading completion, or ChatGPT memory.

GitHub state is authoritative. ChatGPT maintains the state on the learner's behalf; the learner should not have to perform routine bookkeeping.

## Three independent mastery dimensions

Every curriculum unit/objective may have three scores:

- `E` — **Exam readiness**: ability to recognize requirements, eliminate distractors, and choose/justify the best answer under exam conditions.
- `A` — **Architecture mastery**: ability to reason from requirements, compare alternatives, defend trade-offs, account for failure/security/operations/cost, and adapt when constraints change.
- `H` — **Hands-on capability**: ability to implement, observe, diagnose, modify, and clean up the relevant architecture behavior.

Do not collapse these into one score.

## Evidence scale

Use 0–5 for each applicable dimension:

- `0 UNASSESSED` — no valid evidence.
- `1 RECOGNIZE` — recognizes terminology/concepts with support; cannot yet make independent decisions.
- `2 EXPLAIN` — explains core behavior and routine selection criteria; needs support for complex scenarios.
- `3 APPLY` — independently solves standard scenarios and can justify the principal decision.
- `4 ADAPT` — handles trade-offs, failure/change injection, conflicting requirements, and plausible alternatives.
- `5 DEFEND_TEACH` — consistently handles novel constraints, defends the architecture under challenge, connects across domains, and can teach/correct the mental model.

A score is an evidence claim, not a reward. It may decrease when later evidence exposes a gap.

## Valid evidence

Evidence must link to a completed or active controlled session and, where applicable, an approved artifact.

Examples:

- `E`: timed assessment result, scenario reasoning, misconception-free retest.
- `A`: architecture scenario, decision record, oral/written defense, changed-requirement redesign, capstone review.
- `H`: lab acceptance evidence, troubleshooting output, failure/change experiment, cleanup confirmation.

Reading, watching a course, generating notes, or repeatedly seeing the same question are **activities**, not mastery evidence by themselves.

## Confidence

Every score also records `confidence`:

- `LOW` — single weak/old evidence item;
- `MEDIUM` — at least one independent valid evidence item with no unresolved contradiction;
- `HIGH` — multiple recent evidence items or one strong novel/challenge result plus successful retest where relevant.

## Unit state

Allowed unit states:

`NOT_STARTED -> IN_PROGRESS -> REVIEW_REQUIRED -> COMPLETE`

Exception states:

- `BLOCKED`
- `SUPERSEDED`

A unit may move from `COMPLETE` back to `REVIEW_REQUIRED` if new evidence, exam-scope change, source change, or knowledge decay invalidates the previous completion basis.

## Unit completion gate

A unit is `COMPLETE` only when all are true:

1. required activities in the approved study-sequence/source packet are complete;
2. required human reading is recorded;
3. required artifacts are `APPROVED`;
4. unresolved HIGH-severity misconceptions are zero;
5. objective coverage has no mandatory gap;
6. `A >= 3` for architecture units;
7. `E >= 3` where the unit maps to scored SAP-C02 objectives;
8. `H` meets the unit's required lab level where hands-on is mandatory;
9. the latest evidence is not contradicted by an unresolved later result;
10. the completion decision is recorded by the coordinator under the current control snapshot.

`H` scoring is `NOT_APPLICABLE` for units where the approved plan requires no hands-on activity.

## Readiness targets

These are stage targets, not promises of exam success:

- **Unit completion:** normally `E >= 3`, `A >= 3`, applicable `H >= 3` or required lab evidence.
- **Capstone readiness:** architecture-heavy core units should generally reach `A >= 4` through changed-constraint/failure reasoning.
- **Final exam readiness:** all scored objectives must have current evidence; no objective may be `E < 3`; weak objectives are remediated before readiness is declared.

A global average must never hide a weak objective.

## Misconception effect

A HIGH-severity active misconception blocks completion of its mapped objective/unit. A corrected misconception remains in history and requires explicit retest evidence before it is considered resolved.

## Knowledge decay and stale evidence

Evidence can become stale because of:

- provider/exam change;
- later contradictory assessment;
- long time without successful retrieval/application;
- artifact/source supersession.

Staleness does not automatically erase history. It changes current confidence/status and may trigger `REVIEW_REQUIRED`.

## State files

Canonical state is stored under:

```text
state/
  project-state.json
  mastery-state.json
```

Session records are stored separately under `sessions/` and provide the evidence trail.

## Coordinator rules

ChatGPT may update mastery only after consulting:

- this specification;
- current `state/mastery-state.json`;
- current session record;
- linked evidence/artifacts;
- objective map;
- current control snapshot.

ChatGPT must not infer mastery from conversation fluency or familiarity with the learner.

## Auditability

Every mastery update records:

- previous value;
- new value;
- dimension;
- unit/objective;
- evidence IDs;
- session ID;
- timestamp;
- reason;
- control snapshot ID.

The current state is a projection of the evidence history; evidence history is not deleted when scores change.

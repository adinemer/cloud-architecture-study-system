# Study Operating Routine and Retention System

Status: **APPROVED v1.1 — study start remains frozen**  
Certification pilot: **AWS SAP-C02**  
Work constraint: **SUN–THU, 08:00–16:00 employment schedule**  
Weekend: **FRI–SAT**

## Purpose

Define a sustainable routine integrating controlled ChatGPT sessions, official-source reading, architecture reasoning, hands-on work, retrieval practice, note-taking, and spaced review with low administrative overhead.

## Core learning loop

```text
LEARN -> RECALL -> EXPLAIN/DECIDE -> APPLY -> DELAY -> RETRIEVE -> MIX -> RETEST
```

Reading and AI-generated material are input. Retrieval, explanation, scenario decisions, labs, and delayed retest are the primary retention mechanisms.

## Workday routine — Sunday through Thursday

A workday after 16:00 must not automatically become a long high-intensity study block.

### Optional pre-work micro-retrieval

Recommended window: **07:15–07:35**, only when sleep/recovery is adequate.

- 10–20 minutes;
- prior knowledge only;
- no new dense reading or complex lab;
- skipping it does not create backlog.

### Primary post-work session

Default duration: **75–105 minutes**, after normal decompression from work.

Typical structure:

1. **5–10 min cold retrieval** — recall prior mental models, decisions, constraints, or failure modes without notes.
2. **35–50 min targeted work** — approved reading, extraction review, architecture discussion, or focused exercise.
3. **20–30 min active processing** — explain from memory, choose from requirements, compare alternatives, or handle changed constraints.
4. **10–15 min consolidation** — learner-specific notes, misconceptions, controlled flashcards where required, coordinator state update.

Do not add a second full evening session by default. A separate **10–20 minute** spaced-retrieval block is allowed when useful.

## Workweek intensity pattern

Default cognitive-load template:

- **Sunday — Learn / architecture understanding**
- **Monday — Learn / decision reasoning**
- **Tuesday — Learn or focused scenario application**
- **Wednesday — lighter consolidation + retrieval / remediation**
- **Thursday — scenario reasoning + weekly consolidation; reduce load when fatigue is elevated**

This is a cognitive-load template, not a curriculum reorder. Repository state decides actual session content.

## Weekend routine — Friday and Saturday

### Friday — deep work by default

Default: **2–3 hours with breaks**.

Best uses:
- `LAB`;
- `ARCHITECTURE_DECISION`;
- `CAPSTONE`;
- complex scenario work;
- failure/change injection;
- accumulated remediation.

Do not fill the block with passive reading.

### Saturday — cumulative retrieval / recovery by default

Default cumulative retrieval: **45–75 minutes**.

Use interleaved retrieval across previously covered material: architecture decisions, comparisons, failure modes, security/reliability/cost implications, short scenarios, architecture reconstruction, and rejected-alternative reasoning.

Saturday may instead become the deep-work day and Friday the retrieval/recovery day when scheduling or fatigue requires it. At least one weekend day should remain free of substantial new study when recovery requires it.

## Retention schedule

Default retrieval opportunities after first meaningful learning:

- **R0:** end of same session;
- **R1:** next day or next available study day;
- **R2:** ~3–4 days;
- **R3:** ~7–10 days;
- **R4:** ~21–30 days;
- **R5:** cumulative capstone/readiness review.

These are target windows, not calendar debt. Missed reviews are prioritized by weakness and importance rather than stacked onto the next workday.

## Retrieval hierarchy

Prefer:

1. free recall;
2. decision retrieval;
3. compare/contrast;
4. failure prediction;
5. changed constraints;
6. implementation recall;
7. recognition/multiple choice when appropriate.

Recognition-heavy practice must not replace architecture retrieval.

## Personal note-taking policy

Personal notes are not copies of AWS documentation or controlled artifacts. Record learner-specific value only: misconceptions, own-word mental models, missed decision rules, surprising failure modes, why an attractive alternative was wrong, concise sketches, revisit questions, and links to authoritative session/artifact IDs.

Use one Markdown note per meaningful topic/misconception. If note maintenance exceeds roughly **10–15%** of study time, reduce it.

## Fatigue controls

On high-fatigue SUN–THU workdays:

- replace new dense reading with retrieval/remediation;
- shorten the main session to 45–60 minutes;
- avoid H3/H4 labs;
- preserve sleep.

Two consecutive poor-quality sessions trigger a lighter consolidation session before additional new content.

## Missed-day behavior

Do not create backlog equal to missed hours. On return, coordinator reads repository/session state, runs a short retrieval check, resumes the highest-value pending activity, reschedules due reviews by weakness/importance, then continues the approved sequence.

## Weekly coordinator review

Once each week, ChatGPT reviews completed sessions, retrieval performance, misconceptions, due reviews, E/A/H evidence, overload signals, and next permitted sessions. The learner receives a concise summary.

## Study-time target

Default target around the SUN–THU 08:00–16:00 job:

- **5–8 hours/week focused primary study**;
- **1–2 hours/week retrieval/review**;
- deeper FRI/SAT work as evidence and recovery permit.

Quality, retention, sleep, and consistency outrank raw clock hours.

## Relationship to study-start freeze

This is control design only. It does not authorize a real SAP-C02 study session while `study_start_approval=BLOCKED`.

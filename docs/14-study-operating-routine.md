# Study Operating Routine and Retention System

Status: **APPROVED v1 — study start remains frozen**  
Certification pilot: **AWS SAP-C02**  
Work constraint: **08:00–16:00 employment schedule**

## Purpose

Define a sustainable study routine that integrates controlled ChatGPT sessions, official-source reading, architecture reasoning, hands-on work, retrieval practice, note-taking, and spaced review without turning study administration into a second job.

The routine optimizes for:

1. long-term retention;
2. architecture judgment;
3. exam readiness;
4. sustainable cognitive load around full-time work;
5. low administrative overhead.

## Core learning loop

The system uses this cycle:

```text
LEARN -> RECALL -> EXPLAIN/DECIDE -> APPLY -> DELAY -> RETRIEVE -> MIX -> RETEST
```

Reading and AI-generated material are input. Retrieval, explanation, scenario decisions, labs, and delayed retest are the primary retention mechanisms.

## Daily cognitive-load rule

A workday after 16:00 must not automatically become a long high-intensity study block.

Weekdays use one primary controlled session plus a short retrieval block. Weekends carry the heavier lab, architecture challenge, and cumulative-review work.

The coordinator adjusts the mode based on current repository state, but must preserve the approved sequence and session-purpose rules.

## Weekday routine

### Before work — optional micro-retrieval

Recommended window: **07:15–07:35**, only when sleep/recovery is adequate.

Purpose:
- retrieve previously learned concepts from memory;
- review due flashcard/retrieval prompts;
- no new dense reading;
- no complex lab work.

Target: **10–20 minutes**.

Skipping this block does not create backlog.

### After work decompression

Recommended: do not begin the main study session immediately at 16:00.

Allow a normal transition for food, movement, errands, and mental recovery. The routine does not prescribe a universal exact start time; the coordinator should schedule the primary session when the learner can sustain focused reasoning.

### Primary weekday session

Default duration: **75–105 minutes**.

One session has one primary purpose. Suitable weekday session types:

- `READING`
- `EXTRACTION_REVIEW`
- `INSTRUCTION_DISCUSSION`
- `ARCHITECTURE_DECISION`
- focused `ASSESSMENT`
- focused `REMEDIATION`

Typical structure:

1. **5–10 min — cold retrieval**
   - no notes initially;
   - recall prior mental model, decisions, constraints, or failure modes.
2. **35–50 min — new/targeted work**
   - approved human reading, extraction review, architecture discussion, or focused exercise.
3. **20–30 min — active processing**
   - explain from memory;
   - make a decision from requirements;
   - compare alternatives;
   - answer a changed-constraint question.
4. **10–15 min — consolidation**
   - personal notes only for learner-specific insights/gaps;
   - record misconceptions;
   - generate/update controlled flashcards only when required;
   - session state updated by coordinator.

### Evening retrieval block

Do **not** add a second full study session by default.

If useful, perform **10–20 minutes** of spaced retrieval later in the evening. Stop when the due retrieval set is complete. The goal is memory strengthening, not additional content volume.

## Weekday intensity pattern

Default sustainable pattern:

- **Monday — Learn / architecture understanding**
- **Tuesday — Learn / decision reasoning**
- **Wednesday — lighter consolidation + retrieval / remediation**
- **Thursday — Learn / scenario reasoning**
- **Friday — light cumulative retrieval or rest**

This is a cognitive-load template, not a curriculum reorder. Repository state decides the actual unit/session content.

Wednesday and Friday deliberately reduce new-content pressure to improve recovery and retention.

## Weekend routine

### One deep-work block

Default duration: **2–3 hours**, with breaks.

Best uses:
- `LAB`
- `ARCHITECTURE_DECISION`
- `CAPSTONE`
- complex scenario work
- failure/change injection
- accumulated remediation

Do not fill the entire block with reading.

### One cumulative-retrieval block

Default duration: **45–75 minutes** on the other weekend day or separated from the deep-work block.

Use interleaved retrieval across previously covered material:

- architecture decisions;
- compare/contrast;
- failure modes;
- security/reliability/cost implications;
- short exam-style scenarios;
- reconstruct a diagram or architecture from memory;
- explain why rejected alternatives are wrong.

At least one day each week should remain free of substantial new study when fatigue is elevated.

## Retention schedule

New knowledge is revisited by successful retrieval rather than passive rereading.

Default review opportunities after first meaningful learning:

- **R0:** end of same session — immediate recall;
- **R1:** next day or next available study day;
- **R2:** approximately 3–4 days later;
- **R3:** approximately 7–10 days later;
- **R4:** approximately 21–30 days later;
- **R5:** cumulative review during capstone/readiness phases.

These are target windows, not rigid calendar debts. Missed reviews are rescheduled by priority; they are not all stacked into the next evening.

## Retrieval hierarchy

Prefer the most cognitively useful form available:

1. **Free recall:** explain the concept/decision without prompts.
2. **Decision retrieval:** requirements -> choose an architecture and justify it.
3. **Contrast:** distinguish two plausible AWS options.
4. **Failure retrieval:** predict what breaks and how the design responds.
5. **Changed constraint:** modify RTO, cost, security, scale, Region, or organizational requirement.
6. **Implementation retrieval:** recall or reproduce important lab behavior.
7. **Recognition:** multiple-choice/factual recall only where appropriate.

Do not let recognition-heavy question practice replace architecture retrieval.

## Interleaving

After a unit reaches basic competence, retrieval should mix related domains rather than repeatedly testing one isolated service.

Examples:
- storage + reliability + cost;
- networking + security;
- deployment + observability + rollback;
- migration + target architecture + cost.

Interleaving starts after the learner has a usable initial mental model; it should not make first exposure unnecessarily chaotic.

## Personal note-taking policy

Personal notes are **not** a duplicate of AWS documentation or controlled artifacts.

Write a note only when it captures something learner-specific or cognitively useful:

- “I kept confusing X with Y.”
- a mental model in the learner's own words;
- a decision rule the learner initially missed;
- a failure mode that was surprising;
- why an attractive alternative was wrong;
- a concise architecture sketch/reference;
- a question to revisit;
- a link to the authoritative artifact/session.

Do not manually copy:
- provider feature lists;
- long summaries already generated by the pipeline;
- full decision matrices already stored as controlled artifacts;
- flashcards already controlled by artifact JSON;
- session administration.

### Personal note format

Use one Markdown file per meaningful topic or misconception, not one giant notebook.

Suggested structure:

```markdown
# Topic / mental model

Session: SAP-C02-Uxx-Sxxx
Artifact: <artifact-id if applicable>

## From memory
<learner's concise explanation>

## Decision rule
<when/why>

## What I got wrong
<misconception or weak distinction>

## Revisit
<question or trigger>
```

## Note-maintenance rule

If personal note maintenance exceeds roughly **10–15% of total study time**, the coordinator should reduce note-taking and rely more on controlled artifacts/retrieval. Note volume is not a progress metric.

## Retention instrumentation

The coordinator tracks evidence through sessions/mastery state. It should additionally classify retrieval attempts as:

- `RECALLED_CLEANLY`
- `RECALLED_WITH_PROMPT`
- `PARTIAL`
- `INCORRECT`
- `MISCONCEPTION_REVEALED`

A failed retrieval is useful evidence and schedules remediation; it is not treated as a reason to simply reread everything.

## Fatigue controls

On high-fatigue weekdays:

- replace new dense reading with retrieval/remediation;
- shorten the primary session to 45–60 minutes;
- avoid H3/H4 labs;
- preserve sleep rather than extending study late into the night.

Two consecutive poor-quality sessions trigger a lighter consolidation session before more new material.

## Missed-day behavior

Do not create a backlog equal to missed calendar hours.

On return:
1. coordinator reads repository/session state;
2. perform a short retrieval check;
3. resume the highest-value pending activity;
4. reschedule due reviews based on weakness/importance;
5. continue the sequence.

## Weekly review

Once per week, ChatGPT coordinator performs a short controlled review of:

- sessions completed;
- retrieval performance;
- unresolved misconceptions;
- due reviews;
- current E/A/H evidence;
- fatigue/overload signals;
- next permitted sessions.

The learner receives a concise summary, not an administrative report dump.

## Study-time target

With an 08:00–16:00 job, the default system aims for approximately:

- **5–8 hours/week of focused primary study**;
- **1–2 hours/week of retrieval/review**;
- deeper weekend work as needed.

This is deliberately below a maximal-hours plan. Quality, retention, and consistency outrank raw clock time.

The coordinator may increase/decrease load based on actual evidence and recovery, but should not exceed sustainable quality merely to meet a weekly-hour target.

## Relationship to study-start freeze

This routine is approved control design only. It does not authorize creation of a real SAP-C02 study session while `study_start_approval=BLOCKED`.

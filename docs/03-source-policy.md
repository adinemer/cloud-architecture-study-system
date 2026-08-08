# Source Classification Policy

Status: **DRAFT — requires pilot validation**

## Scope

Define which provider materials enter the study system and how each document or section is treated.

## Default source policy

For the AWS SAP-C02 pilot, official AWS material is the default authoritative corpus. Third-party certification courses are excluded from the curriculum unless this policy is deliberately changed.

## Provisional processing classes

These classes are hypotheses to be tested, not final rules.

### `READ_FULL_CONTEXTUALIZE`
Use when the value lies in architectural reasoning, principles, decision process, or an integrated framework that should be understood as a whole.

Processing:
1. Human reads the complete approved scope.
2. AI produces a source-grounded summary.
3. AI extracts decisions, trade-offs, principles, and implications.
4. AI places the material in architectural context.
5. Human/AI discussion tests understanding.

Candidate material types:
- Well-Architected foundational material and selected pillar guidance;
- high-value architecture frameworks;
- major migration/governance/security architecture guidance;
- selected decision guides and important whitepapers.

### `READ_SELECTIVE_EXTRACT`
Use when a source contains important architecture material but reading the full document would have low marginal value.

Processing:
1. AI identifies high-value sections.
2. AI extracts the rest of the architecture-relevant content.
3. Human reads selected passages/sections.
4. AI contextualizes and synthesizes.

Candidate material types:
- service user guides;
- security/resilience/networking subsections;
- prescriptive guidance with mixed implementation detail;
- extensive best-practice collections.

### `EXTRACT_VALIDATE`
Use for dense factual material where AI compression is likely to save substantial time and architectural reasoning is limited.

Processing:
1. AI extracts against a fixed schema.
2. QA checks source fidelity/completeness.
3. Human reads source only for flagged/high-impact items.

Candidate material types:
- feature matrices;
- FAQs;
- limits/quotas;
- configuration capability references;
- service scope/availability details;
- pricing mechanics.

### `REFERENCE_ONLY`
Do not summarize by default. Retrieve when a decision, implementation, lab, or question requires it.

Candidate material types:
- API references;
- CLI references;
- exhaustive parameter documentation;
- low-value implementation detail.

### `HANDS_ON`
Use to build or validate practical capability rather than as a primary reading source.

Candidate material types:
- Skill Builder labs;
- AWS Workshops;
- tutorials;
- implementation guides used during labs.

### `ASSESSMENT`
Use for readiness measurement and feedback, not primary teaching.

Candidate material types:
- official sample questions;
- official practice assessments;
- system-generated assessments that have passed QA.

## Section-level override

Document-level classification may be overridden per section. A service guide can simultaneously contain `READ_SELECTIVE_EXTRACT`, `HANDS_ON`, and `REFERENCE_ONLY` sections.

## Required source metadata

Every inventoried source should eventually capture:

- title;
- provider;
- canonical URL or stable identifier;
- document type;
- certification objective mapping;
- architecture-domain mapping;
- processing class;
- publication/update/version metadata when available;
- retrieval date;
- required human reading scope;
- QA status;
- notes about supersession or conflicts.

## Approval condition

These classes become operational only after the extraction pilot demonstrates acceptable completeness, fidelity, and time savings for representative document types.

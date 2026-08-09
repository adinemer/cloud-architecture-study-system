# Study System Charter

Status: **APPROVED v1.0 — study start remains frozen**  
System version: `1.0-prestudy`  
Pilot certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Technical study state: **READY_TO_START**  
Study-start approval: **BLOCKED by explicit user freeze**

## Purpose

Design, validate, and operate a controlled AI-assisted study system with two equal outcomes:

1. Pass the target cloud certification exam.
2. Improve professional cloud-architecture knowledge, decision-making, and hands-on capability.

## Source-of-truth hierarchy

1. Current official certification exam guide and objective definitions.
2. Current official provider architecture guidance and documentation.
3. Approved repository specifications and current authoritative state.
4. Approved study artifacts generated from those sources.
5. Model background knowledge only when explicitly identified as supplementary and never as a substitute for an authoritative source.

Conversation context and model memory are not authoritative study state.

## Core operating rules

- Real certification study may begin only when all technical/control gates pass **and** explicit study-start approval is unblocked.
- Official provider material is authoritative for provider/exam facts.
- Third-party certification courses are excluded from the default curriculum unless source policy is deliberately changed.
- AI must distinguish provider facts, provider recommendations, cross-source synthesis, architectural inference, and exam interpretation.
- AI-generated material is unapproved until it passes applicable QA gates.
- Human reading is concentrated on reasoning-heavy material; repetitive factual/reference material is compressed only when controls permit it.
- The extraction pipeline must be simple, inspectable, testable, and `GREEN` for the current fingerprint before trusted pipeline-dependent work.
- Additional infrastructure (RAG, vector DBs, agent frameworks, custom applications) is added only after measured need is demonstrated.
- Study sequence is controlled by approved curriculum/prerequisites, not conversational drift.
- One controlled ChatGPT chat has one controlled learning purpose and maps to one repository session.
- GitHub must be consulted before substantive study-system recommendations or controlled actions.
- Mastery is evidence-based; reading, note generation, or conversational fluency alone cannot award mastery.
- Work schedule assumptions are SUN–THU 08:00–16:00, with FRI–SAT weekend, unless explicitly changed under governance.

## ChatGPT roles

ChatGPT may act as:

- coordinator;
- study partner;
- instructor;
- documentation analyst;
- architecture mentor;
- assessor.

Each role operates under repository specifications rather than improvising a new process per chat.

## Technical readiness gate

The system is technically ready to start only when all of the following are current and passing:

- official resource inventory and objective map;
- source classification/read/extract/reference/lab policy;
- study sequence;
- ChatGPT operating specification;
- extraction and architectural-enrichment pipeline;
- current `GREEN` pipeline-health record/fingerprint;
- study-artifact schemas, provenance, QA, and deterministic rendering;
- progress/mastery model;
- controlled study-session lifecycle;
- ChatGPT chat-session lifecycle;
- repository-first coordinator governance;
- study operating/retention routine;
- approved study-tool policy;
- change/version/freshness controls;
- representative extraction-pipeline validation;
- artifact/control-plane regressions;
- synthetic end-to-end control dry run;
- final readiness audit.

Technical readiness does **not** override explicit user study-start approval. The authoritative project state in `state/project-state.json` controls whether study may actually begin.

## Change control

Material changes to certification scope, source policy, extraction/toolchain behavior, schemas, QA policy, mastery rules, session/chat rules, coordinator governance, or study sequence require a governed repository change and applicable regression validation before becoming operational.

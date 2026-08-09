# Cloud Architecture Study System

A controlled, AI-assisted study system for professional cloud architecture certifications.

## Pilot certification

**AWS Certified Solutions Architect – Professional (SAP-C02)**

Equal goals:

1. Pass the certification exam.
2. Improve professional cloud-architecture knowledge, judgment, and hands-on skill.

## Current phase

**Pre-unfreeze hardening validation. Real certification study remains explicitly frozen.**

Validated/control areas include:

- authoritative AWS SAP-C02 resource inventory and complete scored-objective map;
- architecture-first study sequence and read/extract/reference/lab policy;
- Fedora-compatible extraction pipeline with explicit `GREEN` fingerprint health state;
- grounded extraction before architectural enrichment;
- strict packet-level semantic extraction/enrichment integrity with no silent selected-section gaps;
- 100% human review requirement for HIGH provider claims before semantic PASS;
- explicit provider-claim → architectural-inference lineage and conflict/repeatability controls;
- study-artifact schemas, provenance, QA, deterministic rendering, and anti-drift CI;
- evidence-based E/A/H progress/mastery model;
- controlled study-session lifecycle and resumable history;
- single-purpose ChatGPT chat/session contracts;
- mandatory formal handoff from every terminal controlled session;
- explicit predecessor-handoff consumption by every successor before activation;
- repository-first ChatGPT governance for substantive recommendations and actions;
- SUN–THU 08:00–16:00 work-aware study/retention routine with FRI–SAT weekend;
- approved study-tool policy and local-only personal-note default;
- change-control/versioning/freshness policy;
- machine-readable project/mastery/session/chat/handoff/semantic/change/pipeline-health contracts;
- negative-path semantic, handoff, and governance regressions;
- static pre-study readiness audit;
- synthetic two-session end-to-end semantic + ChatGPT chat + handoff continuity dry run.

## Governing principle

Provider material is the source of truth for provider/exam facts. Versioned specifications and current state in this repository control the process. ChatGPT must resolve GitHub authority/state before substantive study-system recommendations or controlled actions; conversation context/model memory do not override it.

## Pipeline trust model

Trusted extraction/enrichment requires two independent conditions:

1. `state/pipeline-health.json` is `GREEN` and its recorded fingerprint matches current extraction/semantic-QA-affecting files;
2. the current source packet has a strict semantic-integrity `PASS` with complete selected-section accounting, grounded claim locators, required HIGH-claim review, inference lineage, resolved HIGH conflicts, and no material repeatability drift.

Operational success alone is not content-quality approval. Failed/stale operational or semantic state blocks downstream trusted work.

## Session/chat continuity model

A ChatGPT conversation is an interaction surface, not authoritative state. Each real controlled study chat has one purpose and maps to one repository session under `sessions/`.

Every terminal controlled session produces `handoff.json`. A successor with a predecessor must read and reconcile that exact handoff against current GitHub state and record its consumption before becoming `ACTIVE`. Conversation history can support presentation but cannot substitute for canonical continuity state.

## Artifact trust model

Canonical study artifacts are schema-valid JSON. Markdown is rendered deterministically from JSON. Only artifacts with approved lifecycle state, passing semantic/artifact QA, valid provenance, and required human review are trusted study material.

## Study-start boundary

Technical readiness does not authorize study by itself. `study_start_approval` remains `BLOCKED` until the learner explicitly unfreezes study in a separate instruction. No real controlled session/chat may be created before then.

Authoritative current state: [`state/project-state.json`](state/project-state.json).

## Repository map

- [`docs/`](docs/) — governance and operating specifications
- [`aws/sap-c02/`](aws/sap-c02/) — provider inventory/objective mapping
- [`schemas/`](schemas/) — machine contracts
- [`state/`](state/) — authoritative project/mastery/pipeline state
- [`pipeline/`](pipeline/) — deterministic source ingestion/bundling
- [`prompts/`](prompts/) — versioned AI contracts
- [`qa/`](qa/) — validation, regression, pilot, dry-run, readiness evidence
- [`sessions/`](sessions/) — controlled learner session/chat/handoff history when study begins
- [`changes/`](changes/) — governed change records

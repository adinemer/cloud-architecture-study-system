# Cloud Architecture Study System

A controlled, AI-assisted study system for professional cloud architecture certifications.

## Pilot certification

**AWS Certified Solutions Architect – Professional (SAP-C02)**

Equal goals:

1. Pass the certification exam.
2. Improve professional cloud-architecture knowledge, judgment, and hands-on skill.

## Current phase

**Final pre-study readiness audit in progress. Real certification study has not started.**

Implemented control areas:

- authoritative AWS SAP-C02 resource inventory and objective map;
- architecture-first study sequence and read/extract/reference/lab policy;
- Fedora-compatible extraction pipeline with explicit `GREEN` fingerprint health state;
- grounded extraction before architectural enrichment;
- study-artifact schemas, provenance, QA, deterministic rendering, and anti-drift CI;
- evidence-based E/A/H progress/mastery model;
- controlled study-session lifecycle and resumable history;
- single-purpose ChatGPT chat/session contracts;
- repository-first ChatGPT governance for substantive recommendations and actions;
- SUN–THU 08:00–16:00 work-aware study/retention routine with FRI–SAT weekend;
- approved study-tool policy and local-only personal-note default;
- change-control/versioning/freshness policy;
- machine-readable project/mastery/session/chat/change/pipeline-health schemas;
- negative regressions and synthetic end-to-end session/chat dry run.

## Governing principle

Provider material is the source of truth for provider/exam facts. Versioned specifications and current state in this repository control the process. ChatGPT must resolve GitHub authority/state before substantive study-system recommendations or controlled actions; conversation context/model memory do not override it.

## Pipeline trust model

Trusted extraction/enrichment is allowed only when `state/pipeline-health.json` is `GREEN` and its recorded fingerprint matches current extraction-affecting files. Failed/stale pipeline state blocks downstream trusted work until a complete successful validation restores green.

## Session/chat trust model

A ChatGPT conversation is an interaction surface, not authoritative state. Each real controlled study chat has one purpose and maps to one repository session under `sessions/`. A session control snapshot is bound to current governance hashes, project/mastery state, objective map, prompt/schema versions, and pipeline-health fingerprint.

## Artifact trust model

Canonical study artifacts are schema-valid JSON. Markdown is rendered deterministically from JSON. Only artifacts with approved lifecycle state, passing QA, valid provenance, and required human review are trusted study material.

## Study-start boundary

Technical readiness does not itself authorize study. The explicit user study-start gate is independent and currently remains blocked/frozen.

Authoritative current state: [`state/project-state.json`](state/project-state.json).

## Repository map

- [`docs/`](docs/) — governance and operating specifications
- [`aws/sap-c02/`](aws/sap-c02/) — provider inventory/objective mapping
- [`schemas/`](schemas/) — machine contracts
- [`state/`](state/) — authoritative project/mastery/pipeline state
- [`pipeline/`](pipeline/) — deterministic source ingestion/bundling
- [`prompts/`](prompts/) — versioned AI contracts
- [`qa/`](qa/) — validation, regression, pilot, dry-run, readiness evidence
- [`sessions/`](sessions/) — controlled learner session/chat history when study begins
- [`changes/`](changes/) — governed change records

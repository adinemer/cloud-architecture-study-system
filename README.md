# Cloud Architecture Study System

A controlled, AI-assisted study system for professional cloud architecture certifications.

## Pilot certification

**AWS Certified Solutions Architect – Professional (SAP-C02)**

The pilot has two equal goals:

1. Pass the certification exam.
2. Improve professional cloud-architecture knowledge, judgment, and hands-on skill.

## Current phase

**Pre-study control system complete — real certification study has not started yet.**

Completed gates:

- ✅ authoritative AWS SAP-C02 resource inventory;
- ✅ controlled study sequence and read/extract/reference/lab policy;
- ✅ Fedora-compatible extraction pipeline pilot and benchmark;
- ✅ study-artifact schemas, provenance, QA, deterministic rendering, and anti-drift CI;
- ✅ evidence-based progress/mastery model;
- ✅ controlled study-session lifecycle and historical session records;
- ✅ repository-first ChatGPT coordinator governance;
- ✅ change-control/versioning/freshness policy;
- ✅ machine-readable project/mastery/session/change schemas;
- ✅ cross-file control-plane validation and negative regression tests;
- ✅ synthetic end-to-end study control dry run in Fedora CI;
- ✅ final READY_TO_START integrity validation.

Still required before real study starts:

- **explicit user study-start approval under the charter.**

## Governing principle

Provider material is the source of truth. Versioned specifications and state in this repository control the process. ChatGPT must consult the authoritative repository state before controlled study decisions or artifact creation; conversation context and model memory do not override GitHub.

## Session trust model

A ChatGPT conversation is an interaction surface, not the authoritative study record. Real study work is organized into schema-controlled sessions under `sessions/`, with controlled creation, pause/resume, completion, artifact/evidence links, mastery updates, and retrieval history.

## Artifact trust model

Canonical study artifacts are schema-valid JSON. Markdown is rendered deterministically from JSON. Only artifacts with approved lifecycle state, passing QA, valid provenance, and required human review are trusted study material.

## Repository status

- System version: `1.0-prestudy`
- Pilot: `AWS SAP-C02`
- Study status: `READY_TO_START` (study-start approval pending)
- Resource inventory: `APPROVED_V1`
- Study sequence/source policy: `APPROVED_V1`
- Extraction pipeline: `APPROVED_V1_WITH_GUARDRAILS`
- Artifact/QA controls: `APPROVED_V1`
- Progress/mastery controls: `APPROVED_V1`
- Session management: `APPROVED_V1`
- Coordinator governance: `APPROVED_V1`
- Change/freshness controls: `APPROVED_V1`
- End-to-end dry run: `PASS`

Authoritative current state: [`state/project-state.json`](state/project-state.json).

See [`docs/`](docs/), [`schemas/`](schemas/), [`state/`](state/), [`pipeline/`](pipeline/), and [`qa/`](qa/).

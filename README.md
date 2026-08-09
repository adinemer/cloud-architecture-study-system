# Cloud Architecture Study System

A controlled, AI-assisted study system for professional cloud architecture certifications.

## Pilot certification

**AWS Certified Solutions Architect – Professional (SAP-C02)**

The pilot has two equal goals:

1. Pass the certification exam.
2. Improve professional cloud-architecture knowledge, judgment, and hands-on skill.

## Current phase

**System design — no certification study has started yet.**

Completed gates:

- ✅ authoritative AWS SAP-C02 resource inventory;
- ✅ controlled study sequence and read/extract/reference/lab policy;
- ✅ Fedora-compatible extraction pipeline pilot and benchmark;
- ✅ study-artifact schemas, provenance, QA, deterministic rendering, and anti-drift CI.

Still required before study starts:

- progress/mastery-state specification;
- change-control/versioning/freshness operating specification;
- final end-to-end dry run of one unit using the complete control stack;
- explicit study-start approval under the charter.

## Governing principle

Provider material is the source of truth. Versioned specifications in this repository control the process. AI executes within those controls rather than inventing the study process session by session.

## Artifact trust model

Canonical study artifacts are schema-valid JSON. Markdown is rendered deterministically from JSON. Only artifacts with approved lifecycle state, passing QA, valid provenance, and required human review are trusted study material.

## Repository status

- System version: `0.4-planning`
- Pilot: `AWS SAP-C02`
- Study status: `NOT STARTED`
- Resource inventory: `APPROVED_V1`
- Study sequence/source policy: `APPROVED_V1`
- Extraction pipeline: `APPROVED_V1_WITH_GUARDRAILS`
- Artifact/QA controls: `APPROVED_V1`

See [`docs/`](docs/), [`schemas/`](schemas/), [`pipeline/`](pipeline/), and [`qa/`](qa/).

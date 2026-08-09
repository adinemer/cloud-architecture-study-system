# Extraction Pipeline Health Specification

Status: **APPROVED v1**  
Study start remains frozen.

## Purpose

Make extraction-pipeline health an explicit prerequisite for trusted extraction, enrichment, and downstream study-artifact generation.

## Hard invariant

The extraction pipeline is usable only when its authoritative health state is `GREEN` and the recorded fingerprint matches the current extraction-affecting files.

A failed or stale pipeline must never be left represented as usable.

## Health states

- `GREEN` — full required validation passed for the current fingerprint.
- `VALIDATING` — validation is in progress; trusted pipeline-dependent work is blocked.
- `FAILED` — latest complete validation failed; pipeline-dependent work is blocked.
- `STALE` — extraction-affecting files changed after the last successful validation; pipeline-dependent work is blocked until revalidated.
- `BLOCKED` — validation cannot complete because of an unresolved dependency/environment/control problem.

## Completion rule

Pipeline work is not complete merely because code was changed or one failing test was fixed.

Completion requires:

1. full pipeline smoke validation executes;
2. every mandatory stage passes;
3. current extraction fingerprint is recorded;
4. authoritative `state/pipeline-health.json` is updated to `GREEN`;
5. broader control-plane validation passes after governed control changes.

If any validation fails, ChatGPT must continue diagnosis/fix/revalidation within the current task when possible. If it cannot restore green, the final authoritative state must remain blocked/failed and the blocker must be reported explicitly.

## Required validation coverage

The v1 full pipeline validation includes at least:

- Fedora runtime/dependencies;
- AWS provider-native Markdown acquisition;
- service-guide acquisition plus architecture-significant constraint preservation;
- factual/quota source acquisition;
- HTML normalization fallback;
- PDF normalization fallback;
- provenance output;
- deterministic extraction prompt bundling.

Grounded extraction/artifact regression remains governed by the extraction/artifact QA suites and must also stay passing when affected files change.

## Pipeline fingerprint

The pipeline fingerprint is a SHA-256 over a deterministic manifest of extraction-affecting files. The authoritative implementation is `qa/pipeline_fingerprint.py`.

Initial fingerprint scope:

- `pipeline/ingest.py`
- `pipeline/make_bundle.py`
- `prompts/extract-v1.md`
- `prompts/enrich-v1.md`
- `prompts/qa-v1.md`
- `.github/workflows/pipeline-smoke.yml`

Any intentional change to fingerprint scope is a governed control change.

## Invalidation rule

When an extraction-affecting file changes, the prior green record is no longer sufficient for production use. Until a full passing rerun is recorded, health is logically `STALE`/blocked even if the state file has not yet been rewritten.

Machine checks compare current fingerprint to the recorded green fingerprint; mismatch fails closed.

## Failure rule

A failed run means:

- no trusted extraction/enrichment;
- no approval of pipeline-derived artifacts;
- no claim that the pipeline is healthy;
- diagnose and fix;
- rerun the **complete** required validation, not only the failed step;
- record the replacement successful run/fingerprint before resuming use.

Transient external failures may occur physically. The guarantee is that the system is never treated as usable while such failure remains unresolved.

## Authoritative state

`state/pipeline-health.json` records:

- schema/version;
- health state;
- pipeline fingerprint;
- validated commit SHA;
- successful workflow run ID/job ID;
- validation timestamp;
- workflow name;
- required stages;
- last failure reference when applicable;
- next permitted action.

## Coordinator requirement

Before any pipeline-dependent recommendation or action, ChatGPT must consult this health state and verify the fingerprint. Conversation memory or an earlier successful run is insufficient.

## Study freeze

A green pipeline does not authorize study start. `study_start_approval=BLOCKED` remains independently controlling.

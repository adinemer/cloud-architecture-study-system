# Study System Architecture

Status: **DRAFT**

## Logical architecture

```text
GOVERNANCE / CONTROL
  - charter
  - certification source of truth
  - source policy
  - curriculum and sequence
  - ChatGPT operating rules
  - QA policy
  - progress/mastery state
  - change control
          |
          v
KNOWLEDGE PIPELINE
  discover -> validate -> classify -> acquire -> normalize
  -> extract -> summarize -> architecture enrichment
  -> cross-source synthesis -> QA -> approve
          |
          v
STUDY EXPERIENCE
  read -> discuss -> teach -> lab -> architecture exercise
  -> flashcards/notes -> assessment -> remediation -> mastery update
```

## Design principles

### 1. Control before content
The repository specifications govern the study process. Chat sessions execute the process but do not redefine it implicitly.

### 2. Separate extraction from interpretation
The pipeline must first establish what the provider states, then enrich that information with architectural meaning. Provider fact and AI inference must never be blended invisibly.

### 3. Section-level classification
A long service guide may contain architecture concepts, implementation tutorials, API references, resilience material, quotas, and troubleshooting. Classification therefore applies at both document and section level.

### 4. Minimum viable pipeline first
The initial target is a transparent workflow using inspectable text/Markdown and a small number of tools. A more complex retrieval platform is justified only by measured shortcomings.

### 5. Persistent provenance
Every approved study artifact must remain traceable to its certification objective, source material, processing method, schema version, and QA state.

## Planned document set

- `00-system-charter.md`
- `01-system-architecture.md`
- `02-chatgpt-operating-spec.md`
- `03-source-policy.md`
- `04-study-sequence-spec.md`
- `05-extraction-pipeline-spec.md`
- `06-architecture-enrichment-spec.md`
- `07-study-artifact-schemas.md`
- `08-quality-assurance-spec.md`
- `09-progress-mastery-spec.md`
- `10-tooling-evaluation.md`
- `11-change-control.md`
- `aws/sap-c02/source-inventory.md`
- `aws/sap-c02/objective-map.md`
- `qa/pilot-plan.md`
- `qa/pilot-results.md`

This list is intentionally provisional; redundant control documents should be merged during refinement.

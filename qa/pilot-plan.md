# Extraction Pipeline Pilot Plan

Status: **EXECUTING**  
Issue: #3  
Date: 2026-08-09

## Goal

Validate the minimum Fedora-friendly pipeline before it is allowed to generate trusted study material.

The pilot tests two independent concerns:

1. **Acquisition/normalization quality** — can official AWS sources be converted into stable, inspectable text/Markdown with useful structure and provenance?
2. **LLM transformation quality** — can ChatGPT perform grounded extraction, architectural enrichment, and source-to-output QA consistently without blending inference into provider guidance?

## Minimum toolchain under test

- Python 3;
- provider-native AWS Markdown where available;
- Trafilatura for non-native HTML;
- Pandoc as HTML fallback;
- `pdftotext -layout` as low-dependency PDF fallback;
- PyMuPDF4LLM as optional higher-fidelity PDF path;
- Markdown + JSON provenance sidecars + Git/GitHub;
- ChatGPT using versioned prompts in `prompts/`.

Explicitly excluded from v1: vector DB, embeddings, RAG framework, autonomous agents, custom web application, MarkItDown for the AWS-only path.

## Representative official AWS corpus

Use at least one source from each category:

| Class | Representative source | What the pilot checks |
|---|---|---|
| Framework/reasoning | AWS Well-Architected Framework — general design principles / framework overview | Qualifier preservation, reasoning continuity, direct-reading target selection |
| Prescriptive architecture | AWS Security Reference Architecture — core architecture | Example/reference-vs-recommendation distinction, living-guidance metadata, alternatives/tailoring caveat |
| Service user guide | Amazon VPC route-table/gateway-route-table guidance | Structural extraction, constraints, routing behavior, failure/return-path caveats |
| Factual/quotas | AWS Service Quotas user guide / quota tables | Dense factual compression, scope/adjustability distinctions, volatile-value handling |
| Decision/reference guidance | AWS Decision Guide or reference architecture selected during the run | Alternatives/trade-offs and high-value reading selection |

## Manual baseline

For each source sample, manually record a compact gold checklist containing:

- mandatory facts/recommendations;
- qualifiers/exceptions that must not be lost;
- statements that are examples rather than universal rules;
- architecture-relevant constraints;
- passages that should be read directly by the learner;
- questions the source does not answer.

The gold checklist is not an exhaustive rewrite of the source. It is the minimum set of important points against which pipeline output is judged.

## Parser/normalizer tests

### P1 — provider-native Markdown

For a current `docs.aws.amazon.com` HTML URL:
- attempt the `.md` companion first;
- verify Markdown is actually returned;
- confirm headings/lists/tables and warning/note text survive;
- confirm source URL, retrieval URL, hashes, content type, normalizer and retrieval time are recorded.

### P2 — HTML extraction

For a page without native Markdown:
- run Trafilatura;
- measure navigation/footer/boilerplate retention;
- verify headings, lists and tables where present;
- compare with Pandoc fallback.

Pass preference: Trafilatura may discard irrelevant chrome but must not discard architecture-relevant main content.

### P3 — PDF fallback

Use a known text PDF fixture plus a real PDF-only source if one is required by the curriculum:
- compare `pdftotext -layout` and PyMuPDF4LLM where available;
- verify headings/tables/lists/notes;
- if structure is materially lost, classify the source as direct-reading or require the higher-fidelity parser rather than trusting extraction.

### P4 — Fedora compatibility

Run smoke tests in a Fedora container:
- install the minimum tools;
- create an isolated Python environment;
- install optional extractors;
- ingest live official AWS sources;
- fail CI on retrieval/normalization/provenance defects.

## LLM tests

### L1 — grounded extraction

Run `prompts/extract-v1.md` against each normalized sample.

Critical failures:
- unsupported provider claim;
- inference introduced during extraction;
- exception/constraint reversed or materially lost;
- example converted into a universal rule;
- source locator absent for a nontrivial claim.

### L2 — architectural enrichment

Run `prompts/enrich-v1.md` only from QA-passed extraction(s).

Check:
- every derived statement has an allowed inference label;
- supporting provider facts are identified;
- provider recommendations are not invented;
- conflicts remain visible;
- decision drivers and “when the decision changes” are useful.

### L3 — independent QA pass

Use `prompts/qa-v1.md` with original normalized source + extraction.

Pass only if:
- no critical failure;
- every QA dimension >= 4/5;
- manual reviewer agrees with PASS on a sample.

### L4 — repeatability

Repeat extraction on at least two representative samples.

Require:
- same mandatory facts present;
- no contradictory provider claims;
- output schema stable;
- optional phrasing differences acceptable.

## Quantitative pilot metrics

For each sample record:

- mandatory gold facts total/captured;
- important qualifiers total/captured;
- unsupported claims;
- mislabeled fact/recommendation/inference;
- source-locator accuracy;
- normalization noise/structure defects;
- source word count;
- direct-reading word count recommended by pipeline;
- estimated/manual reading time;
- pipeline-guided reading/review time;
- estimated human reading reduction.

### Initial acceptance thresholds

- mandatory fact recall: **>= 95%** for `EXTRACT_VALIDATE`, **>= 90%** for large `READ_SELECTIVE_EXTRACT` samples (because direct reading covers selected high-value sections);
- important qualifier recall: **100%** for known architecture-changing qualifiers in the gold checklist;
- unsupported provider claims: **0**;
- inference-as-provider-guidance errors: **0**;
- source locator usable: **>= 95%**;
- repeatability: all gold mandatory facts preserved across repeated runs;
- expected human reading reduction: **>= 40%** on selective/extraction classes without failing the quality thresholds.

These are pilot thresholds and can be tightened after Gate 3 automation.

## Approval rule

Pipeline status may be:

- `REJECTED` — unsafe or not useful;
- `CONDITIONAL` — architecture is sound but one or more required live/tool/model checks remain incomplete;
- `APPROVED_V1` — parser/normalizer, LLM, QA, Fedora and time-saving checks pass.

No study artifact generated by this pipeline is trusted merely because it reads well.

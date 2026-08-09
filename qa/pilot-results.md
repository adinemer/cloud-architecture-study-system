# Extraction Pipeline Pilot Results

Status: **APPROVED_V1 WITH OPERATIONAL GUARDRAILS**  
Issue: #3  
Date: 2026-08-09

## Executive result

The minimal pipeline is approved for the SAP-C02 study-system pilot.

Approved path:

```text
AWS canonical source
  -> provider-native Markdown when available
  -> Trafilatura HTML fallback
  -> Pandoc fallback if needed
  -> optional PDF path (PyMuPDF4LLM; pdftotext fallback)
  -> normalized source + provenance sidecar
  -> Grounded Extraction Prompt v1
  -> source-to-extraction QA
  -> human reading required by source class
  -> Architectural Enrichment Prompt v1
  -> artifact generation under Gate #4 schemas
```

Approval does **not** mean unrestricted AI summarization is safe. It means the pipeline is sufficiently reliable when the source policy, prompts, provenance, QA gates, and required human-reading rules are enforced.

## 1. Fedora / tooling validation

A GitHub Actions smoke test was run in a clean `fedora:latest` container. The observed container identified itself as Fedora 44.

Verified in the successful run:

- Python 3.14.6;
- Trafilatura 2.2.0;
- Pandoc 3.7.0.2;
- `pdftotext` 26.01.0;
- PyMuPDF4LLM 1.28.2 installed and executed;
- live outbound retrieval from `docs.aws.amazon.com`;
- provenance JSON generation;
- deterministic prompt-bundle creation.

### CI result

The first observable run passed all actual ingestion tests but failed at the final bundle comparison because the Fedora package set did not include the incidental `cmp` shell utility. The check was replaced with a Python byte comparison. The second run completed successfully with every step passing.

Successful run:
- workflow: `pipeline-smoke`;
- run id: `31304647132`;
- job id: `93222943797`;
- result: **success**.

This is evidence that the proposed v1 toolchain works in a clean Fedora environment rather than merely being documented as Linux-compatible.

## 2. Native AWS Markdown validation

The live Fedora run retrieved three current AWS Docs pages by transforming the canonical `.html` URL to the provider companion `.md` URL.

| Source | Normalizer | Result |
|---|---|---|
| Well-Architected General design principles | `native-text` | PASS |
| Amazon VPC Gateway route tables | `native-text` | PASS |
| AWS Service Quotas introduction | `native-text` | PASS |

The run confirmed that the source provenance recorded both the canonical requested URL and the actual retrieved `.md` URL plus source/normalized SHA-256 hashes.

### Decision

For AWS Docs/Prescriptive Guidance/Decision Guide pages that expose provider Markdown, **native Markdown is the mandatory first choice**. It is cleaner, simpler, and more structurally faithful than scraping rendered HTML.

## 3. HTML fallback validation

A structured HTML fixture containing navigation, main content, headings, lists, and footer content was tested.

### Trafilatura

Result: **PASS**.

It preserved the tested main architecture content and was selected as the preferred non-native-HTML extractor.

### Pandoc

A separate local fallback test showed that Pandoc preserved headings, lists, and tables, but retained navigation/footer boilerplate in the fixture.

Decision: Pandoc remains a deterministic fallback, not the preferred web extractor.

## 4. PDF fallback validation

### PyMuPDF4LLM

The Fedora run generated a text PDF fixture and successfully normalized it with PyMuPDF4LLM.

Result: **PASS** for the functional smoke test.

### `pdftotext -layout`

A separate local fallback test preserved the fixture text but lost useful semantic heading/list structure.

Decision:
- PDF is not a primary AWS ingestion path because current canonical AWS documentation commonly provides HTML/Markdown;
- PyMuPDF4LLM is an **optional** high-fidelity PDF tool, not a base dependency;
- `pdftotext -layout` is a low-dependency fallback for simple text PDFs;
- if a PDF-only source loses architecture-significant structure, the source is escalated to a better parser or direct human reading rather than silently trusted.

## 5. LLM grounded-extraction benchmark

Manual gold checklist: [`pilot-gold-v1.md`](pilot-gold-v1.md).

Representative source classes:

1. framework/reasoning — Well-Architected General design principles;
2. service user guide — VPC Gateway route tables;
3. factual/reference — Service Quotas introduction;
4. prescriptive/reference architecture — AWS Security Reference Architecture core guidance.

The extraction schema was tested against the gold checklist with the hard rule that architectural inference is prohibited in the extraction stage.

### Results

| Sample | Processing class | Mandatory gold items | Captured | Important qualifiers | Qualifiers preserved | Unsupported provider claims | Inference-as-provider errors | Usable locators |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| WAF general principles | `READ_FULL_CONTEXTUALIZE` | 6 | 6 | 3 | 3 | 0 | 0 | 6/6 |
| VPC gateway route tables | `READ_SELECTIVE_EXTRACT` | 12 | 12 | 3 | 3 | 0 | 0 | 12/12 |
| Service Quotas intro | `EXTRACT_VALIDATE` | 11 | 11 | 4 | 4 | 0 | 0 | 11/11 |
| AWS SRA core | `READ_SELECTIVE_EXTRACT` | 8 | 8 | 3 | 3 | 0 | 0 | 8/8 |

Observed mandatory-item recall: **37/37 (100%)**.  
Observed architecture-changing qualifier recall: **13/13 (100%)**.  
Unsupported provider claims: **0**.  
Inference presented as provider guidance: **0**.  
Usable source locators for scored mandatory items: **37/37 (100%)**.

### Critical-failure probes

The QA baseline explicitly tested against common overgeneralizations, including:

- treating every SRA component as mandatory;
- claiming asymmetric gateway-route-table middlebox routing is supported;
- claiming gateway route tables intercept Transit Gateway traffic;
- claiming every service quota is adjustable;
- claiming quota-increase approval is guaranteed.

None of those defects occurred in the validated extraction output.

## 6. Architectural-enrichment benchmark

The enrichment stage was evaluated only after grounded facts passed source QA.

Observed behavior:

- decision drivers were derived from provider facts rather than substituted for them;
- SRA/reference-architecture guidance retained the distinction between recommended baseline/placement and environment-specific tailoring;
- gateway-route-table constraints were translated into design implications without claiming AWS endorsed unrelated inspection architectures;
- quota scope/adjustability became reliability/capacity-planning implications without memorizing volatile quota numbers;
- derived statements were kept separate from provider recommendations.

Result: **PASS** for pilot use under the `CROSS_SOURCE_SYNTHESIS`, `ARCHITECTURAL_INFERENCE`, and `EXAM_INTERPRETATION` labels.

## 7. Repeatability check

Two separately generated grounded-extraction passes were compared on representative selective/factual samples.

Requirements checked:
- all gold mandatory facts present in both passes;
- no contradictory provider claims;
- no critical qualifier loss;
- same semantic output sections;
- wording differences allowed.

Result: **PASS** for the pilot sample.

Gate #4 will turn the currently semantic output requirements into stricter schemas/regression checks, which is necessary before large-scale artifact generation.

## 8. Human-reading reduction proxy

Actual learner elapsed time cannot be honestly measured until the first real study unit. The pilot therefore uses a conservative **direct-reading word-count proxy**, and requires real timing telemetry during the first production unit.

### VPC selective-reading sample

- normalized source: **757 words**;
- approved direct-reading target (`Rules and considerations`): **363 words**;
- source words removed from required direct reading: **52.0%**.

The omitted portion is not discarded; it remains represented by the grounded extraction and source links.

### Service Quotas factual sample

For a deliberately conservative measurement:

- normalized source: **1,084 words**;
- direct-read proxy (`Terminology in Service Quotas`): **398 words**;
- source words removed from required direct reading: **63.3%**.

In normal `EXTRACT_VALIDATE` operation the human-reading requirement may be lower when QA passes, so this is conservative.

### WAF sample

No reduction is claimed. The source is only **365 words** and is reasoning-dense; policy correctly classifies it for complete human reading.

### Result

The selective/extraction samples exceeded the pilot target of **40% expected human reading reduction** without removing direct reading from the short reasoning-heavy sample.

Operational requirement: record actual reading/review minutes during the first production unit and revisit the proxy if real savings differ materially.

## 9. Tool-selection decisions

### Approved minimum

- provider-native AWS Markdown;
- Python 3 standard library pipeline;
- Trafilatura for HTML fallback;
- Markdown + JSON provenance + Git/GitHub;
- ChatGPT with versioned extraction/enrichment/QA prompts.

### Approved fallback

- Pandoc for HTML;
- `pdftotext -layout` for simple PDF text extraction.

### Optional only

- PyMuPDF4LLM for PDF-only material whose layout/structure matters.

Reason: it performed well, but its installation pulls a materially larger dependency stack (including PyMuPDF Layout/ONNX Runtime/Numpy in the tested version). Since AWS canonical sources normally expose HTML/Markdown, carrying this stack continuously is unnecessary.

### Not selected for AWS v1

- MarkItDown — useful general-purpose converter, but no unique value in the current AWS source path;
- vector database / embeddings / RAG framework — no demonstrated need;
- autonomous/multi-agent framework — no demonstrated need;
- custom study web application — no demonstrated need.

## 10. Known limitations and guardrails

1. The LLM benchmark is representative, not exhaustive; per-source QA remains mandatory.
2. Direct source reading is still required by `READ_FULL_CONTEXTUALIZE` and the selected sections of `READ_SELECTIVE_EXTRACT`.
3. A source with diagrams/tables that are not faithfully represented in Markdown requires visual/manual review.
4. Volatile quotas/pricing/service behavior must be re-retrieved rather than trusted from old generated notes.
5. The pipeline does not crawl the entire AWS documentation corpus. Source packets are deliberately small and curriculum-driven.
6. Gate #4 must define artifact schemas and automated anti-drift/provenance checks before generated flashcards/ADRs/notes become trusted study artifacts.
7. First production unit must collect real human reading/review time so the time-saving proxy can be calibrated.

## 11. Gate decision

### Parser/acquisition
**PASS**

### Fedora compatibility
**PASS**

### Provenance
**PASS**

### Grounded extraction fidelity
**PASS**

### Inference separation
**PASS**

### Repeatability
**PASS for pilot sample**

### Expected reading-time reduction
**PASS by conservative word-count proxy; real-time measurement required in first production unit**

## Final status

**APPROVED_V1 WITH OPERATIONAL GUARDRAILS**.

Issue #3 may close. Study itself remains blocked by the system charter until Gate #4 and the remaining governance specifications are complete.

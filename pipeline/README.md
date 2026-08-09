# Minimal Fedora Extraction Pipeline

Status: **PILOT v1**  
Purpose: acquire and normalize approved provider sources before ChatGPT extraction/enrichment.

## Design

Keep acquisition deterministic and local; keep reasoning in ChatGPT under versioned prompts.

```text
approved URL/file
  -> provider-native Markdown when available
  -> HTML cleanup fallback
  -> PDF fallback only when needed
  -> normalized Markdown/text + provenance sidecar
  -> versioned extraction prompt bundle
  -> ChatGPT grounded extraction
  -> ChatGPT architectural enrichment
  -> source-to-output QA
```

No vector database, embeddings, RAG framework, agent framework, or API integration is required for v1.

## AWS acquisition priority

1. **AWS native Markdown**: for `docs.aws.amazon.com/.../*.html`, try the companion `.md` URL first. Current AWS Docs, Well-Architected, Prescriptive Guidance, service user guides, and Decision Guides expose Markdown links on many pages.
2. **Trafilatura** for HTML without provider-native Markdown, especially `aws.amazon.com` pages such as FAQs. It is preferred over generic HTML conversion because it is designed to remove page boilerplate and can output Markdown.
3. **Pandoc** is a deterministic HTML fallback when Trafilatura is unavailable. It preserves structure but can retain navigation/footer noise; therefore it is not preferred for live web pages.
4. **PDF** is not a normal AWS path because canonical AWS publications normally have HTML/Markdown. For a PDF-only source:
   - use `pymupdf4llm` when layout/heading/table fidelity is important;
   - otherwise `pdftotext -layout` is an acceptable low-dependency fallback for plain text;
   - if PDF normalization materially damages structure, require direct human reading rather than trusting extraction.
5. **MarkItDown is not in the minimum AWS toolchain.** It remains a candidate later for mixed Office/document formats; AWS v1 does not need its breadth.

## Fedora setup

Minimum system tools:

```bash
sudo dnf install curl pandoc poppler-utils python3
```

Preferred HTML extractor:

```bash
# use an isolated environment/tool installer; one option:
uv tool install trafilatura
```

Optional high-fidelity PDF path:

```bash
uv tool install --with pymupdf4llm pymupdf4llm
```

The PDF command is optional; exact packaging should be re-checked when installing because PyMuPDF4LLM evolves quickly.

## Commands

Normalize a current AWS Docs page:

```bash
python pipeline/ingest.py \
  --url 'https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html' \
  --out work/reliability-pillar.md
```

The program first tries the AWS `.md` companion. It writes:

- normalized source, e.g. `work/reliability-pillar.md`;
- provenance sidecar, e.g. `work/reliability-pillar.md.source.json`.

Create the deterministic ChatGPT extraction bundle:

```bash
python pipeline/make_bundle.py \
  --source work/reliability-pillar.md \
  --prompt prompts/extract-v1.md \
  --out work/reliability-pillar.extract-bundle.md
```

## What is versioned

Commit:
- scripts;
- prompt templates;
- source metadata/manifests;
- approved derived study artifacts;
- QA results.

Do **not** automatically commit complete copies of provider documentation. Keep canonical URLs, hashes, retrieval dates, and only store source snapshots when there is a deliberate reason and licensing permits it.

## Failure behavior

- Native Markdown unavailable -> try HTML.
- Trafilatura unavailable -> Pandoc fallback, but mark output for noise review.
- PDF loses structure -> use higher-fidelity parser or direct reading.
- Source appears stale/conflicting -> do not proceed to enrichment until source policy resolves it.
- Any unsupported provider claim in extraction -> critical QA failure.

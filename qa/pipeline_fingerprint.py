#!/usr/bin/env python3
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    'pipeline/ingest.py',
    'pipeline/make_bundle.py',
    'prompts/extract-v1.md',
    'prompts/enrich-v1.md',
    'prompts/qa-v1.md',
    'prompts/enrich-qa-v1.md',
    'schemas/semantic-pipeline-v1.schema.json',
    'qa/validate_semantic_pipeline.py',
    'qa/semantic_pipeline_regression.py',
    'qa/fixtures/semantic-valid.json',
    '.github/workflows/pipeline-smoke.yml',
]

def fingerprint():
    h = hashlib.sha256()
    for rel in FILES:
        p = ROOT / rel
        data = p.read_bytes()
        h.update(rel.encode('utf-8'))
        h.update(b'\0')
        h.update(hashlib.sha256(data).hexdigest().encode('ascii'))
        h.update(b'\n')
    return h.hexdigest()

if __name__ == '__main__':
    print(fingerprint())

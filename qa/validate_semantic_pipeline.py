#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT/'schemas/semantic-pipeline-v1.schema.json').read_text())
V = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def semantic_errors(doc):
    errs = [e.message for e in V.iter_errors(doc)]
    if errs:
        return errs

    sections = {s['section_id']: s for s in doc['source_sections']}
    claims = {c['claim_id']: c for c in doc['extraction_claims']}
    enrichment = {c['claim_id']: c for c in doc['enrichment_claims']}

    if len(sections) != len(doc['source_sections']):
        errs.append('duplicate source section_id')
    if len(claims) != len(doc['extraction_claims']):
        errs.append('duplicate extraction claim_id')
    if set(claims) & set(enrichment):
        errs.append('claim IDs must be unique across extraction and enrichment')

    for s in doc['source_sections']:
        sid = s['section_id']
        if s['processing_status'] in {'FAILED','MISSING'}:
            errs.append(f'{sid}: source section not successfully accounted for')
        if s['processing_status'] == 'INTENTIONALLY_EXCLUDED' and not s['reason']:
            errs.append(f'{sid}: intentional exclusion requires reason')
        if s['architecture_significant'] and s['processing_status'] == 'PROCESSED' and not s['extracted_claim_ids'] and not s['reason']:
            errs.append(f'{sid}: architecture-significant processed section has no claims or explicit no-relevant-claims reason')
        for cid in s['extracted_claim_ids']:
            if cid not in claims:
                errs.append(f'{sid}: references unknown extraction claim {cid}')
            elif claims[cid]['section_id'] != sid:
                errs.append(f'{sid}: claim {cid} section linkage mismatch')

    for cid, c in claims.items():
        if c['section_id'] not in sections:
            errs.append(f'{cid}: orphan provider claim section')
        elif sections[c['section_id']]['processing_status'] != 'PROCESSED':
            errs.append(f'{cid}: provider claim points to non-processed section')
        if not c['locator'].strip():
            errs.append(f'{cid}: missing source locator')
        if c['severity'] == 'HIGH' and not c['human_reviewed']:
            errs.append(f'{cid}: HIGH provider claim requires human review')

    for cid, c in enrichment.items():
        for support in c['support_claim_ids']:
            if support not in claims:
                errs.append(f'{cid}: enrichment support must resolve to provider-grounded extraction claim: {support}')
        if not c['rationale'].strip():
            errs.append(f'{cid}: enrichment requires rationale')

    for conflict in doc['conflicts']:
        if conflict['severity'] == 'HIGH' and conflict['status'] != 'RESOLVED':
            errs.append(f"{conflict['conflict_id']}: unresolved HIGH conflict blocks semantic PASS")
        if conflict['status'] == 'RESOLVED' and not conflict['resolution']:
            errs.append(f"{conflict['conflict_id']}: resolved conflict requires resolution")

    scores = doc['quality_scores']
    strict_fives = ['factual_fidelity','qualifier_preservation','unsupported_claim_avoidance','inference_separation']
    for k in strict_fives:
        if scores[k] != 5:
            errs.append(f'{k} must equal 5 for production semantic PASS')
    for k in ['architecture_completeness','locator_quality']:
        if scores[k] < 4.5:
            errs.append(f'{k} must be >= 4.5 for production semantic PASS')

    if doc['repeatability']['material_semantic_drift']:
        errs.append('material semantic drift detected across repeated runs')
    if doc['repeatability']['runs_compared'] < 2:
        errs.append('repeatability requires at least two compared runs')

    if doc['semantic_status'] == 'PASS' and errs:
        errs.append('semantic_status=PASS is inconsistent with blocking semantic defects')
    if doc['semantic_status'] != 'PASS':
        errs.append(f"semantic_status must be PASS for trusted pipeline use, got {doc['semantic_status']}")
    return errs


def main():
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('report'); a=p.parse_args()
    doc=json.loads(Path(a.report).read_text())
    errs=semantic_errors(doc)
    if errs:
        for e in errs: print('FAIL', e)
        return 1
    print('PASS semantic pipeline integrity')
    print(f"sections={len(doc['source_sections'])} extraction_claims={len(doc['extraction_claims'])} enrichment_claims={len(doc['enrichment_claims'])}")
    return 0

if __name__=='__main__': raise SystemExit(main())

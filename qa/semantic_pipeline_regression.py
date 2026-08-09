#!/usr/bin/env python3
import copy, json
from pathlib import Path
from validate_semantic_pipeline import semantic_errors

ROOT=Path(__file__).resolve().parents[1]
BASE=json.loads((ROOT/'qa/fixtures/semantic-valid.json').read_text())

def ok(name, doc):
    e=semantic_errors(doc); assert not e, f'{name}: {e}'; print('PASS valid', name)

def bad(name, mutate, contains):
    d=copy.deepcopy(BASE); mutate(d); e=semantic_errors(d)
    assert e, f'{name}: unexpectedly valid'
    assert any(contains in x for x in e), f'{name}: expected {contains!r}, got {e}'
    print('PASS invalid', name)

def main():
    ok('baseline semantic packet', BASE)
    bad('missing source section', lambda d: d['source_sections'][1].update(processing_status='MISSING'), 'not successfully accounted for')
    bad('silent high claim review gap', lambda d: d['extraction_claims'][1].update(human_reviewed=False), 'HIGH provider claim requires human review')
    bad('orphan provider claim', lambda d: d['extraction_claims'][0].update(section_id='unknown'), 'orphan provider claim section')
    bad('orphan enrichment support', lambda d: d['enrichment_claims'][0].update(support_claim_ids=['a2']), 'must resolve to provider-grounded')
    bad('qualifier score not perfect', lambda d: d['quality_scores'].update(qualifier_preservation=4.5), 'qualifier_preservation must equal 5')
    bad('fidelity score not perfect', lambda d: d['quality_scores'].update(factual_fidelity=4.5), 'factual_fidelity must equal 5')
    bad('completeness below threshold', lambda d: d['quality_scores'].update(architecture_completeness=4.0), 'architecture_completeness must be >= 4.5')
    bad('repeatability semantic drift', lambda d: d['repeatability'].update(material_semantic_drift=True), 'material semantic drift')
    def open_conflict(d):
        d['conflicts']=[{'conflict_id':'x1','severity':'HIGH','status':'OPEN','description':'Two approved sources appear inconsistent.','resolution':None}]
    bad('unresolved high conflict', open_conflict, 'unresolved HIGH conflict')
    def silent_section(d):
        d['source_sections'][0]['extracted_claim_ids']=[]; d['source_sections'][0]['reason']=None
    bad('architecture section silently empty', silent_section, 'has no claims or explicit no-relevant-claims reason')
    print('ALL SEMANTIC PIPELINE REGRESSIONS PASS')

if __name__=='__main__': main()

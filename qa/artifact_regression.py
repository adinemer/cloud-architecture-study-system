#!/usr/bin/env python3
import copy, json, subprocess, tempfile
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from validate_artifacts import semantic_errors
from render_artifact import render

ROOT = Path(__file__).resolve().parents[1]
BASE = json.loads((ROOT/'qa/fixtures/valid-architecture-note.json').read_text())
SCHEMA = json.loads((ROOT/'schemas/artifact-v1.schema.json').read_text())
V = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def errors(doc):
    return [e.message for e in V.iter_errors(doc)] + semantic_errors(doc)


def artifact(kind, content):
    d = copy.deepcopy(BASE)
    d['meta']['artifact_type'] = kind
    d['meta']['artifact_id'] = f'aws-sap-c02-u03-regression-{kind.replace("_", "-")}'
    d['content'] = content
    return d


def expect_valid(name, doc):
    e = errors(doc)
    assert not e, f'{name} unexpectedly invalid: {e}'
    print('PASS valid', name)


def expect_invalid(name, doc, contains=None):
    e = errors(doc)
    assert e, f'{name} unexpectedly valid'
    if contains:
        assert any(contains in x for x in e), f'{name} missing expected error {contains!r}: {e}'
    print('PASS invalid', name)


def main():
    valid = {
        'source_summary': {
            'purpose':'Summarize routing constraints', 'key_claims':['c001'],
            'constraints_and_caveats':['Review symmetry constraints'], 'unresolved_questions':[],
            'human_reading_completed':True, 'human_reading_scope':'Rules and considerations'
        },
        'architecture_note': BASE['content'],
        'decision_record': {
            'decision_title':'Inspection routing choice','context':'Need traffic inspection','requirements':['Supported routing'],
            'constraints':['VPC routing constraints'],'options':[{'name':'Gateway route table','fit':'Supported paths'},{'name':'Alternative design','fit':'Other paths'}],
            'decision':'Select based on traffic path','rationale':['Preserve supported routing'],'consequences_positive':['Explicit design'],
            'consequences_negative':['Added routing complexity'],'risks':['Misconfiguration'],'when_to_revisit':['Traffic topology changes'],'exam_relevance':['1.1']
        },
        'comparison_matrix': {
            'decision_question':'Which routing mechanism fits?','options':['A','B'],'criteria':['Traffic path','Operational burden'],
            'cells':[{'option':'A','criterion':'Traffic path','value':'Depends'}],'selection_rules':['Match constraints'],
            'dangerous_simplifications':['Do not choose from feature count alone']
        },
        'pattern_note': {
            'pattern_kind':'PATTERN','problem':'Traffic inspection','context':'VPC routing','forces':['Security','Reliability'],
            'structure':'Inspection path','when_to_use':['Supported symmetric path'],'when_not_to_use':['Unsupported routing'],
            'failure_behavior':['Traffic loss on invalid path'],'tradeoffs':['Control vs complexity'],'related_decisions':['Routing architecture']
        },
        'flashcard_set': {'cards':[{
            'card_id':'fc001','card_type':'DECISION','front':'What must be checked before gateway route-table middlebox insertion?',
            'back':'Whether the intended traffic path is supported by the routing constraints.','why_it_matters':'Avoid invalid inspection architectures.',
            'source_refs':[{'source_id':'aws-vpc-gateway-route-tables','locator':'Rules and considerations'}], 'objective_ids':['1.1'],'volatility':'LOW'
        }]},
        'lab_brief': {
            'lab_level':'H3','learning_objectives':['Validate routing behavior'],'scenario':'Design an inspection path','requirements':['Supported traffic path'],
            'constraints':['Use a sandbox'],'allowed_sources':['aws-vpc-gateway-route-tables'],'acceptance_criteria':['Explain observed routing'],
            'evidence_to_capture':['Route-table state'],'failure_or_change_injection':['Change a route and diagnose'],'cleanup_requirements':['Remove test resources'],
            'estimated_cost_risk':'LOW'
        },
        'assessment_set': {
            'assessment_label':'GENERATED_ASSESSMENT','questions':[{
                'type':'SELECTION','prompt':'Choose a supported inspection approach for the stated path.','objective_ids':['1.1'],
                'answer':'Evaluate the routing constraints first.','explanation':'The service behavior constrains the architecture.',
                'tested_misconception':'Feature availability implies every path is supported.'
            }]
        },
        'misconception_record': {
            'misconception':'Any middlebox path can be inserted using a gateway route table.','evidence':'Incorrect scenario answer',
            'correct_model':'Validate supported gateway route-table traffic paths and constraints.','root_cause':'DECISION_GAP',
            'source_refs':[{'source_id':'aws-vpc-gateway-route-tables','locator':'Rules and considerations'}],
            'remediation_actions':['Re-read routing constraints'],'retest_criteria':['Solve changed-path scenario correctly']
        }
    }

    for kind, content in valid.items():
        expect_valid(kind, artifact(kind, content))

    d = copy.deepcopy(BASE); d['claims'][0]['source_refs'] = []
    expect_invalid('provider claim without source', d, 'provider claim requires source')

    d = copy.deepcopy(BASE); d['claims'][1].pop('inference_rationale')
    expect_invalid('inference without rationale', d, 'requires inference_rationale')

    d = copy.deepcopy(BASE); d['meta']['qa_state'] = 'QA_PENDING'
    expect_invalid('approved without QA pass', d, 'APPROVED artifact requires qa_state=PASS')

    d = artifact('assessment_set', copy.deepcopy(valid['assessment_set'])); d['content']['assessment_label']='AWS_OFFICIAL'
    expect_invalid('assessment masquerades as official', d)

    d = artifact('flashcard_set', {'cards': valid['flashcard_set']['cards'] * 21})
    # unique card IDs are not enforced by JSON schema yet; size control must still fail.
    expect_invalid('flashcard overflow', d, '>20 cards')

    # Deterministic renderer regression.
    r1, r2 = render(BASE), render(copy.deepcopy(BASE))
    assert r1 == r2, 'renderer not deterministic'
    assert 'GENERATED FILE' in r1
    print('PASS deterministic rendering')

    print('ALL ARTIFACT REGRESSIONS PASS')

if __name__ == '__main__':
    main()

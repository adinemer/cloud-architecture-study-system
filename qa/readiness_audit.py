#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXPECTED_OBJECTIVES={'1.1','1.2','1.3','1.4','1.5','2.1','2.2','2.3','2.4','2.5','2.6','3.1','3.2','3.3','3.4','3.5','4.1','4.2','4.3','4.4'}
EXPECTED_UNITS={f'U{i:02d}' for i in range(16)}
CONTROL_DOCS=[
'docs/00-system-charter.md','docs/01-system-architecture.md','docs/02-chatgpt-operating-spec.md','docs/03-source-policy.md',
'docs/04-study-sequence-spec.md','docs/05-extraction-pipeline-spec.md','docs/07-study-artifact-schemas.md','docs/08-quality-assurance-spec.md',
'docs/09-progress-mastery-spec.md','docs/10-tooling-evaluation.md','docs/11-study-session-management.md','docs/12-coordinator-governance.md',
'docs/13-change-control-freshness.md','docs/14-study-operating-routine.md','docs/15-study-tool-policy.md','docs/16-chat-session-management.md','docs/17-pipeline-health-spec.md'
]
REQUIRED_FILES=CONTROL_DOCS+[
'aws/sap-c02/source-inventory.md','aws/sap-c02/objective-map.md',
'schemas/artifact-v1.schema.json','schemas/session-v1.schema.json','schemas/chat-session-v1.schema.json','schemas/state-v1.schema.json','schemas/change-v1.schema.json','schemas/pipeline-health-v1.schema.json',
'state/project-state.json','state/mastery-state.json','state/pipeline-health.json',
'qa/validate_artifacts.py','qa/artifact_regression.py','qa/validate_control_plane.py','qa/control_regression.py','qa/validate_chat_sessions.py','qa/validate_pipeline_health.py','qa/end_to_end_dry_run.py',
'.github/workflows/pipeline-smoke.yml','.github/workflows/artifact-qa.yml','.github/workflows/control-plane.yml'
]
STALE_PHRASES={
'docs/00-system-charter.md':['Status: **DRAFT**','Study state: **NOT STARTED**'],
'docs/01-system-architecture.md':['Status: **DRAFT**','Planned document set','06-architecture-enrichment-spec.md'],
'docs/03-source-policy.md':['Issue #3 must still demonstrate','Issue #4 must then define'],
'docs/04-study-sequence-spec.md':['study remains blocked until pipeline/QA gates pass','Issue #3 proves','Issue #4 defines','remaining mastery/change-control specifications are approved'],
'docs/10-tooling-evaluation.md':['PARTIAL APPROVAL','Functional areas still to evaluate','Schema and QA enforcement — next gate'],
'aws/sap-c02/source-inventory.md':['classifications remain provisional','All classifications below are **PROVISIONAL**','Next dependency: **Issue #2','Planning Gate 2 will decide'],
'docs/15-study-tool-policy.md':['must be explicitly decided before real study']
}

def fail(problems, area, message): problems.append((area,message))
def text(rel): return (ROOT/rel).read_text()

def main():
    problems=[]
    for rel in REQUIRED_FILES:
        if not (ROOT/rel).exists(): fail(problems,'file',f'missing required file: {rel}')

    for rel in CONTROL_DOCS:
        if not (ROOT/rel).exists(): continue
        first='\n'.join(text(rel).splitlines()[:6])
        if 'Status:' not in first or 'APPROVED' not in first:
            fail(problems,'document-status',f'{rel} is not explicitly APPROVED near the top')

    for rel,phrases in STALE_PHRASES.items():
        if not (ROOT/rel).exists(): continue
        body=text(rel)
        for phrase in phrases:
            if phrase in body: fail(problems,'stale-language',f'{rel} still contains obsolete phrase: {phrase}')

    routine=text('docs/14-study-operating-routine.md')
    if 'SUN–THU' not in routine or 'FRI–SAT' not in routine:
        fail(problems,'calendar','study routine must explicitly use SUN–THU workdays and FRI–SAT weekend')
    if '08:00–16:00' not in routine:
        fail(problems,'calendar','study routine must retain 08:00–16:00 work constraint')

    tools=text('docs/15-study-tool-policy.md')
    if 'local-only by default' not in tools:
        fail(problems,'tools','personal-note storage default is unresolved')

    arch=text('docs/01-system-architecture.md')
    if 'does **not** require a separate `06-*` governance document' not in arch:
        fail(problems,'architecture','intentional absence of docs/06 is not explained')

    objective=text('aws/sap-c02/objective-map.md')
    found=set(re.findall(r'\*\*([1-4]\.[1-6])\s',objective))
    if found != EXPECTED_OBJECTIVES:
        fail(problems,'coverage',f'objective map coverage mismatch missing={sorted(EXPECTED_OBJECTIVES-found)} extra={sorted(found-EXPECTED_OBJECTIVES)}')

    mastery=json.loads((ROOT/'state/mastery-state.json').read_text())
    if set(mastery.get('units',{})) != EXPECTED_UNITS:
        fail(problems,'mastery','mastery state must cover U00-U15 exactly')
    if set(mastery.get('objectives',{})) != EXPECTED_OBJECTIVES:
        fail(problems,'mastery','mastery state must cover all scored objectives exactly')
    for kind,entries in [('unit',mastery.get('units',{})),('objective',mastery.get('objectives',{}))]:
        for key,val in entries.items():
            if val.get('status') not in {'NOT_STARTED','UNASSESSED'}:
                fail(problems,'mastery',f'pre-study {kind} {key} unexpectedly has status {val.get("status")}')
            for dim in ('E','A','H'):
                score=val.get(dim)
                if isinstance(score,int) and score != 0:
                    fail(problems,'mastery',f'pre-study {kind} {key} has nonzero {dim}={score}')

    project=json.loads((ROOT/'state/project-state.json').read_text())
    if project.get('current_unit') is not None or project.get('active_session_id') is not None or project.get('last_completed_session_id') is not None:
        fail(problems,'project-state','pre-study project must have no current/active/completed learner session')
    gates=project.get('control_gate_status',{})
    for gate,value in gates.items():
        if gate in {'final_readiness_audit','study_start_approval'}: continue
        if value not in {'PASS','NOT_REQUIRED'}:
            fail(problems,'project-state',f'gate {gate} is {value}, expected PASS/NOT_REQUIRED')
    if gates.get('study_start_approval') != 'BLOCKED':
        fail(problems,'freeze','study_start_approval must remain BLOCKED during readiness audit')
    if gates.get('final_readiness_audit') not in {'PENDING','PASS'}:
        fail(problems,'project-state','final_readiness_audit must be PENDING or PASS')

    pipeline=json.loads((ROOT/'state/pipeline-health.json').read_text())
    if pipeline.get('health') != 'GREEN':
        fail(problems,'pipeline',f'pipeline health is {pipeline.get("health")}, expected GREEN')

    ss=json.loads((ROOT/'schemas/session-v1.schema.json').read_text())
    if ss.get('properties',{}).get('schema_version',{}).get('const') != '1.1.0':
        fail(problems,'session-schema','session schema must be 1.1.0 for pipeline-bound snapshots')
    snap=ss.get('properties',{}).get('control_snapshot',{})
    required=set(snap.get('required',[]))
    for name in {'pipeline_health_state_version','pipeline_health','pipeline_fingerprint'}:
        if name not in required: fail(problems,'session-schema',f'control snapshot missing required pipeline field {name}')

    control=text('qa/control_snapshot.py')
    for marker in ['pipeline_health_state_version','pipeline_fingerprint',"pipeline.get('health') != 'GREEN'"]:
        if marker not in control: fail(problems,'snapshot',f'control snapshot implementation missing {marker}')

    chat_validator=text('qa/validate_chat_sessions.py')
    if "status in {'PLANNED','READY','BLOCKED'}" not in chat_validator:
        fail(problems,'chat','chat validator does not permit pre-open session states without chat.json')
    if 'startup_repository_snapshot_id must match session control snapshot' not in chat_validator:
        fail(problems,'chat','chat validator does not bind chat to session snapshot')

    dry=text('qa/end_to_end_dry_run.py')
    for marker in ['chat_fixture','PAUSED chat validates with resume anchor','study-start freeze remains intact','END-TO-END CONTROL + CHAT DRY RUN PASS']:
        if marker not in dry: fail(problems,'dry-run',f'end-to-end dry run missing required lifecycle marker: {marker}')

    if problems:
        for area,msg in problems: print(f'FAIL [{area}] {msg}')
        print(f'READINESS AUDIT FAILED ({len(problems)} findings)')
        return 1

    print('PASS required files and approved document statuses')
    print('PASS stale/provisional gate language removed')
    print('PASS SUN-THU / FRI-SAT calendar and note-storage decision')
    print('PASS SAP-C02 20-task objective coverage')
    print('PASS pre-study mastery/project state remains clean and frozen')
    print('PASS pipeline health GREEN')
    print('PASS session snapshots are pipeline-health bound')
    print('PASS chat/session lifecycle enforcement markers')
    print('PASS synthetic end-to-end dry-run coverage markers')
    print('PRE-STUDY READINESS STATIC AUDIT PASS')
    return 0

if __name__=='__main__': raise SystemExit(main())

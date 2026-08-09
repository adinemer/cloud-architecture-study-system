#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_OBJECTIVES = {'1.1','1.2','1.3','1.4','1.5','2.1','2.2','2.3','2.4','2.5','2.6','3.1','3.2','3.3','3.4','3.5','4.1','4.2','4.3','4.4'}
ALLOWED_UNITS = {f'U{i:02d}' for i in range(16)}
REQUIRED_AUTHORITIES = {
    'docs/00-system-charter.md','docs/02-chatgpt-operating-spec.md','docs/03-source-policy.md',
    'docs/04-study-sequence-spec.md','docs/05-extraction-pipeline-spec.md','docs/07-study-artifact-schemas.md',
    'docs/08-quality-assurance-spec.md','docs/09-progress-mastery-spec.md','docs/11-study-session-management.md',
    'docs/12-coordinator-governance.md','docs/13-change-control-freshness.md','docs/14-study-operating-routine.md',
    'docs/15-study-tool-policy.md','docs/16-chat-session-management.md','docs/17-pipeline-health-spec.md',
    'aws/sap-c02/objective-map.md','state/project-state.json','state/mastery-state.json','state/pipeline-health.json'
}
GOVERNANCE_HASH_FILES = REQUIRED_AUTHORITIES - {'aws/sap-c02/objective-map.md','state/project-state.json','state/mastery-state.json'}

def sha256_path(rel):
    return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()

def validate_schema(doc, schema_path):
    schema = json.loads((ROOT/schema_path).read_text())
    return [e.message for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(doc)]

def validate_project(project):
    errors=[]
    if project['study_status'] == 'IN_PROGRESS' and not project['active_session_id']:
        errors.append('IN_PROGRESS requires active_session_id')
    if project['study_status'] in {'NOT_STARTED','READY_FOR_DRY_RUN','READY_TO_START','COMPLETED'} and project['active_session_id']:
        errors.append(f"{project['study_status']} cannot have active_session_id")
    gates=project.get('control_gate_status',{})
    if project['study_status']=='READY_TO_START':
        blockers=[k for k,v in gates.items() if k!='study_start_approval' and v not in {'PASS','NOT_REQUIRED'}]
        if blockers: errors.append(f'READY_TO_START with incomplete gates: {blockers}')
    return errors

def validate_mastery(mastery):
    errors=[]
    if set(mastery['units']) != ALLOWED_UNITS: errors.append('mastery units must exactly cover U00-U15')
    if set(mastery['objectives']) != ALLOWED_OBJECTIVES: errors.append('mastery objectives must exactly cover scored SAP-C02 task IDs')
    for target, entry in list(mastery['units'].items())+list(mastery['objectives'].items()):
        if entry['status']=='COMPLETE':
            if entry['A']!='NOT_APPLICABLE' and isinstance(entry['A'],int) and entry['A']<3: errors.append(f'{target}: COMPLETE with A < 3')
            if target in ALLOWED_OBJECTIVES and isinstance(entry['E'],int) and entry['E']<3: errors.append(f'{target}: COMPLETE with E < 3')
            if entry.get('active_misconception_ids'): errors.append(f'{target}: COMPLETE with active misconceptions')
    return errors

def validate_snapshot(snap):
    errors=[]
    expected=set(GOVERNANCE_HASH_FILES)
    actual=set(snap.get('governance_hashes',{}))
    if actual != expected:
        errors.append(f'control snapshot governance hash set mismatch; missing={sorted(expected-actual)} extra={sorted(actual-expected)}')
    for rel,digest in snap.get('governance_hashes',{}).items():
        p=ROOT/rel
        if not p.exists(): errors.append(f'control snapshot authority missing from repository: {rel}'); continue
        if sha256_path(rel) != digest: errors.append(f'control snapshot stale governance hash: {rel}')
    obj='aws/sap-c02/objective-map.md'
    if sha256_path(obj) != snap.get('objective_map_hash'): errors.append('control snapshot stale objective_map_hash')
    pipeline=json.loads((ROOT/'state/pipeline-health.json').read_text())
    if pipeline.get('health') != 'GREEN': errors.append(f"current pipeline health is {pipeline.get('health')}, expected GREEN")
    if snap.get('pipeline_health_state_version') != pipeline.get('state_version'): errors.append('control snapshot pipeline_health_state_version mismatch')
    if snap.get('pipeline_health') != pipeline.get('health'): errors.append('control snapshot pipeline_health mismatch')
    if snap.get('pipeline_fingerprint') != pipeline.get('pipeline_fingerprint'): errors.append('control snapshot pipeline_fingerprint mismatch')
    return errors

def validate_session(session, project, mastery, all_sessions):
    errors=[]
    units=set(session['unit_ids']); objs=set(session['objective_ids'])
    if not units <= ALLOWED_UNITS: errors.append(f'unknown units: {sorted(units-ALLOWED_UNITS)}')
    if not objs <= ALLOWED_OBJECTIVES: errors.append(f'unknown objectives: {sorted(objs-ALLOWED_OBJECTIVES)}')
    auth=set(session.get('authorities_consulted',[])); missing=REQUIRED_AUTHORITIES-auth
    if missing: errors.append(f'missing mandatory authorities: {sorted(missing)}')
    for sid in session.get('prerequisite_sessions',[]):
        if sid not in all_sessions: errors.append(f'unknown prerequisite session: {sid}')
        elif all_sessions[sid].get('status') not in {'COMPLETED','ARCHIVED'}: errors.append(f'prerequisite session not completed: {sid}')
    status=session['status']
    if status in {'ACTIVE','PAUSED','REVIEW_PENDING','COMPLETED','ARCHIVED'} and not session.get('started_at'): errors.append(f'{status} requires started_at')
    if status in {'COMPLETED','ARCHIVED'}:
        if not session.get('ended_at'): errors.append(f'{status} requires ended_at')
        if session.get('completion_qa')!='PASS': errors.append(f'{status} requires completion_qa=PASS')
        if session.get('unresolved_items'): errors.append(f'{status} cannot have unresolved_items')
        if not session.get('next_permitted_action'): errors.append(f'{status} requires next_permitted_action')
        if session.get('required_artifact_types') and not session.get('artifacts'): errors.append('completed session with required artifact types must link artifacts')
    if status=='PAUSED' and not session.get('pause_state'): errors.append('PAUSED requires pause_state')
    if status=='BLOCKED' and session.get('completion_qa')=='PASS': errors.append('BLOCKED cannot have completion_qa=PASS')
    if status=='ACTIVE' and project.get('active_session_id') not in {None,session['session_id']}: errors.append('ACTIVE session conflicts with project active_session_id')
    snap=session['control_snapshot']
    if snap['project_state_version'] != project['state_version']: errors.append('control snapshot project_state_version mismatch')
    if snap['mastery_state_version'] != mastery['state_version']: errors.append('control snapshot mastery_state_version mismatch')
    errors += validate_snapshot(snap)
    return errors

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--project',default='state/project-state.json'); ap.add_argument('--mastery',default='state/mastery-state.json'); ap.add_argument('--sessions-root',default='sessions'); args=ap.parse_args()
    project=json.loads((ROOT/args.project).read_text()); mastery=json.loads((ROOT/args.mastery).read_text()); problems=[]
    problems += [('project',x) for x in validate_schema(project,'schemas/state-v1.schema.json')+validate_project(project)]
    problems += [('mastery',x) for x in validate_schema(mastery,'schemas/state-v1.schema.json')+validate_mastery(mastery)]
    root=ROOT/args.sessions_root; session_docs={}
    if root.exists():
        for path in sorted(root.glob('*/session.json')):
            doc=json.loads(path.read_text()); session_docs[doc['session_id']]=doc
        active=[s['session_id'] for s in session_docs.values() if s['status']=='ACTIVE']
        if len(active)>1: problems.append(('sessions',f'multiple ACTIVE sessions: {active}'))
        if project.get('active_session_id') and project['active_session_id'] not in active: problems.append(('project','active_session_id does not resolve to ACTIVE session'))
        for sid,doc in session_docs.items():
            errs=validate_schema(doc,'schemas/session-v1.schema.json')+validate_session(doc,project,mastery,session_docs); problems += [(sid,x) for x in errs]
    elif project.get('active_session_id'): problems.append(('project','active_session_id set but sessions directory missing'))
    if problems:
        for where,msg in problems: print(f'FAIL {where}: {msg}')
        return 1
    print('PASS project state'); print('PASS mastery state'); print(f'PASS sessions ({len(session_docs)})'); print('CONTROL PLANE VALID'); return 0

if __name__=='__main__': raise SystemExit(main())

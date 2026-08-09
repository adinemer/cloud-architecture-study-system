#!/usr/bin/env python3
import copy, json
from pathlib import Path
from control_snapshot import build as build_snapshot
from validate_control_plane import validate_project, validate_mastery, validate_session, validate_schema, REQUIRED_AUTHORITIES

ROOT=Path(__file__).resolve().parents[1]
PROJECT=json.loads((ROOT/'state/project-state.json').read_text())
MASTERY=json.loads((ROOT/'state/mastery-state.json').read_text())

def session_fixture():
    sid='SAP-C02-U00-S001'
    return {
      'session_id':sid,'schema_version':'1.1.0','certification':'SAP-C02','exam_scope_version':PROJECT['exam_scope_version'],
      'unit_ids':['U00'],'objective_ids':[],'session_type':'SCOPE_BASELINE','status':'PLANNED',
      'control_snapshot':build_snapshot(sid),
      'authorities_consulted':sorted(REQUIRED_AUTHORITIES),'sources':[],'prerequisite_sessions':[],'required_artifact_types':[],
      'planned_activity':'Dry-run controlled session creation.','exit_criteria':['Control checks pass.'],'started_at':None,'ended_at':None,
      'elapsed_minutes':None,'human_reading_minutes':None,'activities_completed':[],'artifacts':[],'evidence':[],
      'misconceptions':[],'mastery_changes':[],'unresolved_items':[],'next_permitted_action':None,'completion_qa':'NOT_RUN',
      'pause_state':None,'exception_reason':None,'supersedes_session_id':None
    }

def errors(s):
    return validate_schema(s,'schemas/session-v1.schema.json') + validate_session(s,PROJECT,MASTERY,{s['session_id']:s})

def expect(name, condition):
    assert condition, name
    print('PASS',name)

def main():
    s=session_fixture()
    expect('current valid fixture passes', not errors(s))

    p=copy.deepcopy(PROJECT); p['study_status']='IN_PROGRESS'; p['active_session_id']=None
    expect('in-progress requires active session', bool(validate_project(p)))

    m=copy.deepcopy(MASTERY); m['objectives']['1.1']['status']='COMPLETE'; m['objectives']['1.1']['E']=2; m['objectives']['1.1']['A']=3
    expect('objective cannot complete below E3', any('E < 3' in x for x in validate_mastery(m)))

    s=session_fixture(); s['authorities_consulted'].remove('docs/12-coordinator-governance.md')
    expect('missing authority fails closed', any('missing mandatory authorities' in x for x in errors(s)))

    s=session_fixture(); s['status']='PAUSED'; s['started_at']='2026-08-09T09:30:00Z'; s['pause_state']=None
    expect('paused session requires resume state', any('PAUSED requires pause_state' in x for x in errors(s)))

    s=session_fixture(); s['status']='COMPLETED'; s['started_at']='2026-08-09T09:30:00Z'; s['ended_at']='2026-08-09T10:00:00Z'; s['completion_qa']='NOT_RUN'; s['next_permitted_action']='Next'
    expect('completion requires QA pass', any('completion_qa=PASS' in x for x in errors(s)))

    s=session_fixture(); s['control_snapshot']['mastery_state_version']='9.9.9'
    expect('stale mastery snapshot rejected', any('mastery_state_version mismatch' in x for x in errors(s)))

    s=session_fixture(); s['control_snapshot']['pipeline_fingerprint']='0'*64
    expect('stale pipeline fingerprint rejected', any('pipeline_fingerprint mismatch' in x or 'stale governance hash' in x for x in errors(s)))

    s=session_fixture(); s['control_snapshot'].pop('pipeline_health')
    expect('missing pipeline snapshot field fails schema', bool(validate_schema(s,'schemas/session-v1.schema.json')))

    print('ALL CONTROL REGRESSIONS PASS')

if __name__=='__main__': main()

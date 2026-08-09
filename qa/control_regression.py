#!/usr/bin/env python3
import copy, json
from pathlib import Path
from validate_control_plane import validate_project, validate_mastery, validate_session

ROOT=Path(__file__).resolve().parents[1]
PROJECT=json.loads((ROOT/'state/project-state.json').read_text())
MASTERY=json.loads((ROOT/'state/mastery-state.json').read_text())

def session_fixture():
    auth=[
      'docs/00-system-charter.md','docs/02-chatgpt-operating-spec.md','docs/03-source-policy.md','docs/04-study-sequence-spec.md',
      'docs/05-extraction-pipeline-spec.md','docs/07-study-artifact-schemas.md','docs/08-quality-assurance-spec.md',
      'docs/09-progress-mastery-spec.md','docs/11-study-session-management.md','docs/12-coordinator-governance.md',
      'docs/13-change-control-freshness.md','aws/sap-c02/objective-map.md','state/project-state.json','state/mastery-state.json']
    return {
      'session_id':'SAP-C02-U00-S001','schema_version':'1.0.0','certification':'SAP-C02','exam_scope_version':'2026-08-09',
      'unit_ids':['U00'],'objective_ids':[],'session_type':'SCOPE_BASELINE','status':'PLANNED',
      'control_snapshot':{'snapshot_id':'snap-test','repository_commit_sha':'0'*40,'created_at':'2026-08-09T09:30:00Z',
        'governance_hashes':{'docs/00-system-charter.md':'0'*64},'objective_map_hash':'0'*64,'artifact_schema_version':'1.0.0',
        'session_schema_version':'1.0.0','prompt_versions':['extract-v1'],'project_state_version':'1.0.0','mastery_state_version':'1.0.0'},
      'authorities_consulted':auth,'sources':[],'prerequisite_sessions':[],'required_artifact_types':[],
      'planned_activity':'Dry-run controlled session creation.','exit_criteria':['Control checks pass.'],'started_at':None,'ended_at':None,
      'elapsed_minutes':None,'human_reading_minutes':None,'activities_completed':[],'artifacts':[],'evidence':[],
      'misconceptions':[],'mastery_changes':[],'unresolved_items':[],'next_permitted_action':None,'completion_qa':'NOT_RUN',
      'pause_state':None,'exception_reason':None,'supersedes_session_id':None
    }

def expect(name, condition):
    assert condition, name
    print('PASS',name)

def main():
    p=copy.deepcopy(PROJECT); p['study_status']='IN_PROGRESS'; p['active_session_id']=None
    expect('in-progress requires active session', bool(validate_project(p)))

    m=copy.deepcopy(MASTERY); m['objectives']['1.1']['status']='COMPLETE'; m['objectives']['1.1']['E']=2; m['objectives']['1.1']['A']=3
    expect('objective cannot complete below E3', any('E < 3' in x for x in validate_mastery(m)))

    s=session_fixture(); s['authorities_consulted'].remove('docs/12-coordinator-governance.md')
    expect('missing authority fails closed', any('missing mandatory authorities' in x for x in validate_session(s,PROJECT,MASTERY,{s['session_id']:s})))

    s=session_fixture(); s['status']='PAUSED'; s['started_at']='2026-08-09T09:30:00Z'; s['pause_state']=None
    expect('paused session requires resume state', any('PAUSED requires pause_state' in x for x in validate_session(s,PROJECT,MASTERY,{s['session_id']:s})))

    s=session_fixture(); s['status']='COMPLETED'; s['started_at']='2026-08-09T09:30:00Z'; s['ended_at']='2026-08-09T10:00:00Z'; s['completion_qa']='NOT_RUN'; s['next_permitted_action']='Next'
    expect('completion requires QA pass', any('completion_qa=PASS' in x for x in validate_session(s,PROJECT,MASTERY,{s['session_id']:s})))

    s=session_fixture(); s['control_snapshot']['mastery_state_version']='9.9.9'
    expect('stale state snapshot rejected', any('mastery_state_version mismatch' in x for x in validate_session(s,PROJECT,MASTERY,{s['session_id']:s})))

    print('ALL CONTROL REGRESSIONS PASS')

if __name__=='__main__': main()

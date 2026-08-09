#!/usr/bin/env python3
import copy, json, tempfile
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

from control_snapshot import build as build_snapshot
from validate_control_plane import validate_schema, validate_project, validate_mastery, validate_session, REQUIRED_AUTHORITIES
from validate_artifacts import semantic_errors
from render_artifact import render

ROOT=Path(__file__).resolve().parents[1]
ART_SCHEMA=json.loads((ROOT/'schemas/artifact-v1.schema.json').read_text())
ART_VALIDATOR=Draft202012Validator(ART_SCHEMA,format_checker=FormatChecker())

def iso(): return datetime.now(timezone.utc).isoformat()

def check(cond,msg):
    if not cond: raise AssertionError(msg)
    print('PASS',msg)

def artifact_fixture():
    base=json.loads((ROOT/'qa/fixtures/valid-architecture-note.json').read_text())
    base['meta'].update({
      'artifact_id':'control-dry-run-source-summary','artifact_type':'source_summary','status':'APPROVED','qa_state':'PASS',
      'unit_ids':['U00'],'objective_ids':[],'architecture_domains':['control-dry-run'],'artifact_version':'1.0.0',
      'generated_at':iso(),'last_reviewed_at':iso(),'model_id':'control-dry-run-fixture'})
    base['claims']=[]
    base['content']={
      'purpose':'Exercise the artifact lifecycle without creating learner mastery evidence.',
      'key_claims':[], 'constraints_and_caveats':['Synthetic control dry run only; not study material.'],
      'unresolved_questions':[], 'human_reading_completed':'not_required','human_reading_scope':None}
    return base

def session_fixture(project,mastery):
    sid='SAP-C02-U00-S999'
    return {
      'session_id':sid,'schema_version':'1.1.0','certification':'SAP-C02','exam_scope_version':project['exam_scope_version'],
      'unit_ids':['U00'],'objective_ids':[],'session_type':'SCOPE_BASELINE','status':'PLANNED',
      'control_snapshot':build_snapshot(sid),'authorities_consulted':sorted(REQUIRED_AUTHORITIES),'sources':['aws-vpc-gateway-route-tables'],
      'prerequisite_sessions':[],'required_artifact_types':['source_summary'],
      'planned_activity':'Synthetic end-to-end control dry run; no certification learning or mastery credit.',
      'exit_criteria':['Session lifecycle validates.','Artifact validates and renders deterministically.','Mastery state remains unchanged.'],
      'started_at':None,'ended_at':None,'elapsed_minutes':0,'human_reading_minutes':0,'activities_completed':[],
      'artifacts':[],'evidence':[],'misconceptions':[],'mastery_changes':[],'unresolved_items':[],
      'next_permitted_action':None,'completion_qa':'NOT_RUN','pause_state':None,'exception_reason':'Synthetic control-plane dry run; session ID S999 is reserved for CI.','supersedes_session_id':None}

def session_errors(s,p,m):
    return validate_schema(s,'schemas/session-v1.schema.json')+validate_session(s,p,m,{s['session_id']:s})

def main():
    project=json.loads((ROOT/'state/project-state.json').read_text()); mastery=json.loads((ROOT/'state/mastery-state.json').read_text())
    mastery_before=json.dumps(mastery,sort_keys=True)
    check(not validate_project(project),'initial project state valid')
    check(not validate_mastery(mastery),'initial mastery state valid')

    s=session_fixture(project,mastery)
    check(not session_errors(s,project,mastery),'PLANNED session validates with live control snapshot including pipeline health')

    s['status']='READY'
    check(not session_errors(s,project,mastery),'READY transition validates')

    p_active=copy.deepcopy(project); p_active['study_status']='IN_PROGRESS'; p_active['current_unit']='U00'; p_active['active_session_id']=s['session_id']
    s['status']='ACTIVE'; s['started_at']=iso()
    check(not validate_project(p_active),'ACTIVE project state validates')
    check(not session_errors(s,p_active,mastery),'ACTIVE session validates')

    art=artifact_fixture(); art_errors=[e.message for e in ART_VALIDATOR.iter_errors(art)]+semantic_errors(art)
    check(not art_errors,'synthetic artifact passes schema and semantic QA')
    md1=render(art); md2=render(copy.deepcopy(art))
    check(md1==md2 and 'GENERATED FILE' in md1,'artifact renders deterministically')

    s['activities_completed']=['Created and validated synthetic source-summary artifact.','Verified deterministic rendering.']
    s['artifacts']=[art['meta']['artifact_id']]
    s['status']='REVIEW_PENDING'
    check(not session_errors(s,p_active,mastery),'REVIEW_PENDING transition validates')

    s['status']='COMPLETED'; s['ended_at']=iso(); s['completion_qa']='PASS'; s['next_permitted_action']='Return project to READY_FOR_DRY_RUN/then mark dry-run gate PASS; no real study started.'
    check(not session_errors(s,p_active,mastery),'COMPLETED session passes completion gate')

    p_done=copy.deepcopy(project); p_done['study_status']='READY_FOR_DRY_RUN'; p_done['current_unit']=None; p_done['active_session_id']=None; p_done['last_completed_session_id']=None
    check(not validate_project(p_done),'post-dry-run project state validates without recording synthetic session as learner history')
    check(json.dumps(mastery,sort_keys=True)==mastery_before,'mastery remains unchanged')

    with tempfile.TemporaryDirectory() as d:
        Path(d,'session.json').write_text(json.dumps(s,indent=2)+'\n'); Path(d,'artifact.json').write_text(json.dumps(art,indent=2)+'\n'); Path(d,'artifact.md').write_text(md1)
        check(Path(d,'session.json').exists() and Path(d,'artifact.md').exists(),'dry-run outputs are reproducible artifacts')

    print('END-TO-END CONTROL DRY RUN PASS')

if __name__=='__main__': main()

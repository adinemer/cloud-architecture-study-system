#!/usr/bin/env python3
import copy, json, tempfile
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

from control_snapshot import build as build_snapshot
from validate_control_plane import validate_schema, validate_project, validate_mastery, validate_session, REQUIRED_AUTHORITIES
from validate_chat_sessions import validate_chat
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

def session_fixture(project):
    sid='SAP-C02-U00-S999'
    return {
      'session_id':sid,'schema_version':'1.1.0','certification':'SAP-C02','exam_scope_version':project['exam_scope_version'],
      'unit_ids':['U00'],'objective_ids':[],'session_type':'SCOPE_BASELINE','status':'PLANNED',
      'control_snapshot':build_snapshot(sid),'authorities_consulted':sorted(REQUIRED_AUTHORITIES),'sources':['aws-vpc-gateway-route-tables'],
      'prerequisite_sessions':[],'required_artifact_types':['source_summary'],
      'planned_activity':'Synthetic end-to-end control dry run; no certification learning or mastery credit.',
      'exit_criteria':['Session/chat lifecycle validates.','Artifact validates and renders deterministically.','Mastery state remains unchanged.'],
      'started_at':None,'ended_at':None,'elapsed_minutes':0,'human_reading_minutes':0,'activities_completed':[],
      'artifacts':[],'evidence':[],'misconceptions':[],'mastery_changes':[],'unresolved_items':[],
      'next_permitted_action':None,'completion_qa':'NOT_RUN','pause_state':None,'exception_reason':'Synthetic control-plane dry run; session ID S999 is reserved for CI.','supersedes_session_id':None}

def chat_fixture(session):
    return {
      'session_id':session['session_id'],'schema_version':'1.0.0',
      'chat_title':'SAP-C02 | U00 | SAP-C02-U00-S999 | synthetic control dry run',
      'purpose':'Validate one-chat/one-session control lifecycle without conducting study.',
      'primary_session_type':session['session_type'],
      'allowed_scope':['Synthetic control lifecycle validation only.'],
      'out_of_scope':['Real SAP-C02 learning.','Mastery credit.','Unrelated troubleshooting.'],
      'startup_repository_snapshot_id':session['control_snapshot']['snapshot_id'],
      'status':'PLANNED','opened_at':None,'closed_at':None,
      'handoff_required':False,'handoff_target_session_id':None,'resume_anchor':None
    }

def session_errors(s,p,m):
    return validate_schema(s,'schemas/session-v1.schema.json')+validate_session(s,p,m,{s['session_id']:s})

def chat_errors(c,s):
    return validate_schema(c,'schemas/chat-session-v1.schema.json')+validate_chat(c,s)

def main():
    project=json.loads((ROOT/'state/project-state.json').read_text()); mastery=json.loads((ROOT/'state/mastery-state.json').read_text())
    mastery_before=json.dumps(mastery,sort_keys=True)
    check(not validate_project(project),'initial project state valid')
    check(not validate_mastery(mastery),'initial mastery state valid')

    s=session_fixture(project)
    check(not session_errors(s,project,mastery),'PLANNED session validates with live pipeline-bound control snapshot')
    check(s['status']=='PLANNED','PLANNED lifecycle intentionally precedes ChatGPT chat creation')

    s['status']='READY'
    check(not session_errors(s,project,mastery),'READY transition validates')
    c=chat_fixture(s)
    check(not chat_errors(c,s),'READY session permits a PLANNED single-purpose chat contract')

    p_active=copy.deepcopy(project); p_active['study_status']='IN_PROGRESS'; p_active['current_unit']='U00'; p_active['active_session_id']=s['session_id']
    s['status']='ACTIVE'; s['started_at']=iso(); c['status']='OPEN'; c['opened_at']=iso()
    check(not validate_project(p_active),'ACTIVE project state validates')
    check(not session_errors(s,p_active,mastery),'ACTIVE session validates')
    check(not chat_errors(c,s),'ACTIVE repository session binds to OPEN ChatGPT chat')

    # Prove pause/resume state is recoverable without chat memory.
    s['status']='PAUSED'; s['pause_state']={'last_completed_activity':'control preflight','next_activity':'resume synthetic validation'}
    c['status']='PAUSED'; c['resume_anchor']={'last_completed_activity':'control preflight','next_activity':'resume synthetic validation','source_locator':None,'current_question_or_decision':None,'pending_artifact_or_qa':None,'unresolved_item':None}
    check(not session_errors(s,p_active,mastery),'PAUSED session validates with restart state')
    check(not chat_errors(c,s),'PAUSED chat validates with resume anchor')

    s['status']='ACTIVE'; s['pause_state']=None; c['status']='OPEN'; c['resume_anchor']=None
    check(not session_errors(s,p_active,mastery) and not chat_errors(c,s),'resume returns to ACTIVE/OPEN coherently')

    art=artifact_fixture(); art_errors=[e.message for e in ART_VALIDATOR.iter_errors(art)]+semantic_errors(art)
    check(not art_errors,'synthetic artifact passes schema and semantic QA')
    md1=render(art); md2=render(copy.deepcopy(art))
    check(md1==md2 and 'GENERATED FILE' in md1,'artifact renders deterministically')

    s['activities_completed']=['Created and validated synthetic source-summary artifact.','Verified deterministic rendering.']
    s['artifacts']=[art['meta']['artifact_id']]
    s['status']='REVIEW_PENDING'
    check(not session_errors(s,p_active,mastery),'REVIEW_PENDING transition validates')
    check(not chat_errors(c,s),'REVIEW_PENDING session remains in same OPEN chat')

    s['status']='COMPLETED'; s['ended_at']=iso(); s['completion_qa']='PASS'; s['next_permitted_action']='Return project to frozen READY_TO_START state; no real study started.'
    c['status']='CLOSED'; c['closed_at']=iso()
    check(not session_errors(s,p_active,mastery),'COMPLETED session passes completion gate')
    check(not chat_errors(c,s),'COMPLETED session requires and validates CLOSED chat')

    p_done=copy.deepcopy(project); p_done['study_status']='READY_TO_START'; p_done['current_unit']=None; p_done['active_session_id']=None; p_done['last_completed_session_id']=None
    check(not validate_project(p_done),'post-dry-run project state returns to READY_TO_START without recording synthetic session as learner history')
    check(p_done['control_gate_status']['study_start_approval']=='BLOCKED','study-start freeze remains intact')
    check(json.dumps(mastery,sort_keys=True)==mastery_before,'mastery remains unchanged')

    with tempfile.TemporaryDirectory() as d:
        Path(d,'session.json').write_text(json.dumps(s,indent=2)+'\n')
        Path(d,'chat.json').write_text(json.dumps(c,indent=2)+'\n')
        Path(d,'artifact.json').write_text(json.dumps(art,indent=2)+'\n')
        Path(d,'artifact.md').write_text(md1)
        check(all(Path(d,x).exists() for x in ['session.json','chat.json','artifact.json','artifact.md']),'dry-run outputs are reproducible artifacts')

    print('END-TO-END CONTROL + CHAT DRY RUN PASS')

if __name__=='__main__': main()

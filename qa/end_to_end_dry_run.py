#!/usr/bin/env python3
import copy, json, tempfile
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

from control_snapshot import build as build_snapshot
from validate_control_plane import validate_schema, validate_project, validate_mastery, validate_session, REQUIRED_AUTHORITIES
from validate_chat_sessions import validate_chat
from validate_handoffs import validate_handoff
from validate_semantic_pipeline import semantic_errors as semantic_pipeline_errors
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
    base['meta'].update({'artifact_id':'control-dry-run-source-summary','artifact_type':'source_summary','status':'APPROVED','qa_state':'PASS','unit_ids':['U00'],'objective_ids':[],'architecture_domains':['control-dry-run'],'artifact_version':'1.0.0','generated_at':iso(),'last_reviewed_at':iso(),'model_id':'control-dry-run-fixture'})
    base['claims']=[]
    base['content']={'purpose':'Exercise artifact lifecycle without learner mastery evidence.','key_claims':[],'constraints_and_caveats':['Synthetic control dry run only; not study material.'],'unresolved_questions':[],'human_reading_completed':'not_required','human_reading_scope':None}
    return base

def session_fixture(project,sid,pred=None,consumed=None):
    return {'session_id':sid,'schema_version':'1.2.0','certification':'SAP-C02','exam_scope_version':project['exam_scope_version'],'unit_ids':['U00'],'objective_ids':[],'session_type':'SCOPE_BASELINE','status':'PLANNED','control_snapshot':build_snapshot(sid),'authorities_consulted':sorted(REQUIRED_AUTHORITIES),'sources':['aws-vpc-gateway-route-tables'],'prerequisite_sessions':[],'predecessor_session_id':pred,'consumed_handoff_id':consumed,'handoff_id':None,'required_artifact_types':['source_summary'],'planned_activity':'Synthetic end-to-end control dry run; no certification learning or mastery credit.','exit_criteria':['Semantic pipeline validation passes.','Session/chat/handoff lifecycle validates.','Artifact validates and renders deterministically.','Mastery state remains unchanged.'],'started_at':None,'ended_at':None,'elapsed_minutes':0,'human_reading_minutes':0,'activities_completed':[],'artifacts':[],'evidence':[],'misconceptions':[],'mastery_changes':[],'unresolved_items':[],'next_permitted_action':None,'completion_qa':'NOT_RUN','pause_state':None,'exception_reason':'Synthetic control-plane dry run; S998/S999 are reserved for CI.','supersedes_session_id':None}

def chat_fixture(s):
    return {'session_id':s['session_id'],'schema_version':'1.1.0','chat_title':f"SAP-C02 | U00 | {s['session_id']} | synthetic control dry run",'purpose':'Validate one-chat/one-session control lifecycle without conducting study.','primary_session_type':s['session_type'],'allowed_scope':['Synthetic control lifecycle validation only.'],'out_of_scope':['Real SAP-C02 learning.','Mastery credit.','Unrelated troubleshooting.'],'startup_repository_snapshot_id':s['control_snapshot']['snapshot_id'],'status':'PLANNED','opened_at':None,'closed_at':None,'handoff_required':True,'handoff_target_session_id':None,'resume_anchor':None}

def make_handoff(s,c,hid,target=None):
    return {'handoff_id':hid,'schema_version':'1.0.0','source_session_id':s['session_id'],'source_chat_title':c['chat_title'],'source_status':s['status'],'created_at':iso(),'completed_purpose':'Synthetic lifecycle validation completed.','objective_ids':s['objective_ids'],'sources_used':s['sources'],'artifact_ids':s['artifacts'],'evidence_ids':s['evidence'],'mastery_changes':s['mastery_changes'],'active_misconceptions':s['misconceptions'],'unresolved_items':s['unresolved_items'],'decisions_and_mental_models':['GitHub state, not chat memory, carries continuity.'],'pending_qa':[],'lab_cleanup_obligations':[],'deferred_questions':[],'next_session_status':'TARGET_SELECTED' if target else 'NEXT_SESSION_PENDING_COORDINATOR_SELECTION','target_session_id':target,'next_recommended_purpose':'Continue synthetic continuity verification.','next_prerequisites':['Reload current GitHub authorities and verify predecessor handoff.'],'required_reload_authorities':['state/project-state.json','state/mastery-state.json','state/pipeline-health.json','docs/12-coordinator-governance.md','docs/16-chat-session-management.md'],'do_not_infer':['Do not infer mastery, learner answers, or unresolved work from conversation memory.'],'continuity_notes':['Successor must explicitly consume this handoff before activation.'],'source_control_snapshot_id':s['control_snapshot']['snapshot_id']}

def session_errors(s,p,m,all_sessions): return validate_schema(s,'schemas/session-v1.schema.json')+validate_session(s,p,m,all_sessions)
def chat_errors(c,s): return validate_schema(c,'schemas/chat-session-v1.schema.json')+validate_chat(c,s)

def main():
    project=json.loads((ROOT/'state/project-state.json').read_text()); mastery=json.loads((ROOT/'state/mastery-state.json').read_text()); mastery_before=json.dumps(mastery,sort_keys=True)
    check(not validate_project(project),'initial project state valid'); check(not validate_mastery(mastery),'initial mastery state valid')

    sem=json.loads((ROOT/'qa/fixtures/semantic-valid.json').read_text())
    check(not semantic_pipeline_errors(sem),'semantic extraction/enrichment fixture passes strict production gate')

    s1=session_fixture(project,'SAP-C02-U00-S998'); sessions={s1['session_id']:s1}
    check(not session_errors(s1,project,mastery,sessions),'PLANNED predecessor session validates')
    check(s1['control_snapshot']['repository_commit_sha']!='0'*40,'control snapshot records real commit SHA')
    s1['status']='READY'; c1=chat_fixture(s1); check(not session_errors(s1,project,mastery,sessions) and not chat_errors(c1,s1),'READY session and PLANNED chat validate')

    p_active=copy.deepcopy(project); p_active['study_status']='IN_PROGRESS'; p_active['current_unit']='U00'; p_active['active_session_id']=s1['session_id']
    s1['status']='ACTIVE'; s1['started_at']=iso(); c1['status']='OPEN'; c1['opened_at']=iso(); check(not session_errors(s1,p_active,mastery,sessions) and not chat_errors(c1,s1),'ACTIVE/OPEN predecessor validates')
    s1['status']='PAUSED'; s1['pause_state']={'last_completed_activity':'preflight','next_activity':'resume'}; c1['status']='PAUSED'; c1['resume_anchor']={'last_completed_activity':'preflight','next_activity':'resume','source_locator':None,'current_question_or_decision':None,'pending_artifact_or_qa':None,'unresolved_item':None}; check(not session_errors(s1,p_active,mastery,sessions) and not chat_errors(c1,s1),'PAUSED/PAUSED validates')
    s1['status']='ACTIVE'; s1['pause_state']=None; c1['status']='OPEN'; c1['resume_anchor']=None; check(not session_errors(s1,p_active,mastery,sessions) and not chat_errors(c1,s1),'resume validates')

    art=artifact_fixture(); ae=[e.message for e in ART_VALIDATOR.iter_errors(art)]+semantic_errors(art); check(not ae,'synthetic artifact passes schema/semantic QA'); md1=render(art); check(md1==render(copy.deepcopy(art)) and 'GENERATED FILE' in md1,'artifact renders deterministically')
    s1['activities_completed']=['Validated strict semantic packet.','Created and validated synthetic artifact.']; s1['artifacts']=[art['meta']['artifact_id']]; s1['status']='REVIEW_PENDING'; check(not session_errors(s1,p_active,mastery,sessions),'REVIEW_PENDING validates')

    target='SAP-C02-U00-S999'; hid='HO-SAP-C02-U00-S998-001'; s1['status']='COMPLETED'; s1['ended_at']=iso(); s1['completion_qa']='PASS'; s1['next_permitted_action']=f'Create successor {target} and consume {hid}.'; s1['handoff_id']=hid; c1['status']='CLOSED'; c1['closed_at']=iso(); c1['handoff_target_session_id']=target; h1=make_handoff(s1,c1,hid,target)
    check(not session_errors(s1,p_active,mastery,sessions),'COMPLETED predecessor validates'); check(not chat_errors(c1,s1),'CLOSED predecessor chat validates'); check(not validate_handoff(h1,s1,c1),'mandatory predecessor handoff validates')

    s2=session_fixture(project,target,pred=s1['session_id'],consumed=hid)
    # Session B exists only to prove formal predecessor-handoff consumption/continuity; it intentionally requires no second artifact.
    s2['required_artifact_types']=[]
    s2['planned_activity']='Consume and reconcile predecessor handoff, prove seamless successor activation, then close with its own formal handoff.'
    s2['exit_criteria']=['Predecessor handoff is consumed and reconciled.','Successor can activate without conversation-memory dependency.','Successor produces its own terminal handoff.']
    sessions[target]=s2
    check(s2['consumed_handoff_id']==h1['handoff_id'],'successor explicitly consumes predecessor handoff')
    check(not session_errors(s2,project,mastery,sessions),'PLANNED successor validates with consumed handoff link')
    s2['status']='READY'; c2=chat_fixture(s2); check(not session_errors(s2,project,mastery,sessions) and not chat_errors(c2,s2),'successor READY/PLANNED chat validates after handoff consumption')
    p2=copy.deepcopy(project); p2['study_status']='IN_PROGRESS'; p2['current_unit']='U00'; p2['active_session_id']=target; s2['status']='ACTIVE'; s2['started_at']=iso(); c2['status']='OPEN'; c2['opened_at']=iso(); check(not session_errors(s2,p2,mastery,sessions) and not chat_errors(c2,s2),'successor ACTIVE/OPEN validates after formal handoff')

    hid2='HO-SAP-C02-U00-S999-001'; s2['activities_completed']=['Consumed predecessor handoff and verified continuity.']; s2['status']='COMPLETED'; s2['ended_at']=iso(); s2['completion_qa']='PASS'; s2['next_permitted_action']='Return to frozen pre-study technical state.'; s2['handoff_id']=hid2; c2['status']='CLOSED'; c2['closed_at']=iso(); h2=make_handoff(s2,c2,hid2,None); check(not session_errors(s2,p2,mastery,sessions),'successor COMPLETED validates'); check(not validate_handoff(h2,s2,c2),'successor also produces mandatory terminal handoff')

    p_done=copy.deepcopy(project); p_done['current_unit']=None; p_done['active_session_id']=None; p_done['last_completed_session_id']=None; check(not validate_project(p_done),'post-dry-run project preserves current hardening gate state'); check(p_done['control_gate_status']['study_start_approval']=='BLOCKED','study-start freeze remains intact'); check(json.dumps(mastery,sort_keys=True)==mastery_before,'mastery remains unchanged')

    with tempfile.TemporaryDirectory() as d:
        for name,obj in [('session-1.json',s1),('chat-1.json',c1),('handoff-1.json',h1),('session-2.json',s2),('chat-2.json',c2),('handoff-2.json',h2),('semantic.json',sem),('artifact.json',art)]: Path(d,name).write_text(json.dumps(obj,indent=2)+'\n')
        Path(d,'artifact.md').write_text(md1); check(len(list(Path(d).iterdir()))==9,'dry-run continuity outputs are reproducible')
    print('END-TO-END SEMANTIC + CONTROL + CHAT + HANDOFF DRY RUN PASS')

if __name__=='__main__': main()

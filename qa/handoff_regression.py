#!/usr/bin/env python3
import copy, json
from pathlib import Path
from validate_handoffs import validate_handoff

ROOT=Path(__file__).resolve().parents[1]

def base():
    s={'session_id':'SAP-C02-U00-S001','status':'COMPLETED','handoff_id':'HO-SAP-C02-U00-S001-001','control_snapshot':{'snapshot_id':'snap-1'}}
    c={'chat_title':'SAP-C02 | U00 | SAP-C02-U00-S001 | test','handoff_target_session_id':'SAP-C02-U00-S002'}
    h={'handoff_id':'HO-SAP-C02-U00-S001-001','schema_version':'1.0.0','source_session_id':'SAP-C02-U00-S001','source_chat_title':c['chat_title'],'source_status':'COMPLETED','created_at':'2026-08-09T13:00:00Z','completed_purpose':'Test continuity.','objective_ids':[],'sources_used':[],'artifact_ids':[],'evidence_ids':[],'mastery_changes':[],'active_misconceptions':[],'unresolved_items':[],'decisions_and_mental_models':['State lives in GitHub.'],'pending_qa':[],'lab_cleanup_obligations':[],'deferred_questions':[],'next_session_status':'TARGET_SELECTED','target_session_id':'SAP-C02-U00-S002','next_recommended_purpose':'Continue test.','next_prerequisites':['Reload state.'],'required_reload_authorities':['state/project-state.json'],'do_not_infer':['Do not infer mastery from chat memory.'],'continuity_notes':[],'source_control_snapshot_id':'snap-1'}
    return s,c,h

def expect_valid(name,mut=None):
    s,c,h=base()
    if mut: mut(s,c,h)
    e=validate_handoff(h,s,c); assert not e, f'{name}: {e}'; print('PASS valid',name)

def expect_invalid(name,mut,contains):
    s,c,h=base(); mut(s,c,h); e=validate_handoff(h,s,c)
    assert e, f'{name}: unexpectedly valid'
    assert any(contains in x for x in e), f'{name}: expected {contains!r}, got {e}'
    print('PASS invalid',name)

def main():
    expect_valid('baseline handoff')
    expect_invalid('wrong source session',lambda s,c,h:h.update(source_session_id='SAP-C02-U00-S009'),'source_session_id must match')
    expect_invalid('wrong snapshot',lambda s,c,h:h.update(source_control_snapshot_id='other'),'source_control_snapshot_id must match')
    expect_invalid('wrong chat target',lambda s,c,h:c.update(handoff_target_session_id='SAP-C02-U00-S003'),'target_session_id must match')
    expect_invalid('target selected without target',lambda s,c,h:h.update(target_session_id=None),'TARGET_SELECTED requires target_session_id')
    def pending_with_target(s,c,h):
        h['next_session_status']='NEXT_SESSION_PENDING_COORDINATOR_SELECTION'; h['target_session_id']='SAP-C02-U00-S002'
    expect_invalid('pending selection invents target',pending_with_target,'non-target-selected handoff must not invent')
    print('ALL HANDOFF REGRESSIONS PASS')

if __name__=='__main__': main()

#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'schemas/handoff-v1.schema.json').read_text())
V=Draft202012Validator(SCHEMA,format_checker=FormatChecker())
TERMINAL={'COMPLETED','ABORTED','SUPERSEDED'}

def validate_handoff(handoff, session, chat):
    errs=[e.message for e in V.iter_errors(handoff)]
    if handoff.get('source_session_id') != session.get('session_id'):
        errs.append('handoff source_session_id must match session_id')
    if handoff.get('source_chat_title') != chat.get('chat_title'):
        errs.append('handoff source_chat_title must match chat title')
    if handoff.get('source_control_snapshot_id') != session.get('control_snapshot',{}).get('snapshot_id'):
        errs.append('handoff source_control_snapshot_id must match session snapshot')
    if session.get('handoff_id') != handoff.get('handoff_id'):
        errs.append('session handoff_id must match handoff document')
    if handoff.get('target_session_id') != chat.get('handoff_target_session_id'):
        errs.append('handoff target_session_id must match chat handoff_target_session_id')
    if handoff.get('source_status') != session.get('status'):
        errs.append('handoff source_status must match terminal session status')
    if handoff.get('next_session_status')=='TARGET_SELECTED' and not handoff.get('target_session_id'):
        errs.append('TARGET_SELECTED requires target_session_id')
    if handoff.get('next_session_status')!='TARGET_SELECTED' and handoff.get('target_session_id') is not None:
        errs.append('non-target-selected handoff must not invent target_session_id')
    return errs

def main():
    root=ROOT/'sessions'; failed=False; docs={}
    if root.exists():
        for sp in sorted(root.glob('*/session.json')):
            docs[json.loads(sp.read_text())['session_id']]=(sp,json.loads(sp.read_text()))
    for sid,(sp,s) in docs.items():
        hp=sp.with_name('handoff.json'); cp=sp.with_name('chat.json')
        if s['status'] in TERMINAL:
            if not hp.exists() or not cp.exists():
                print(f'FAIL {sid}: terminal session requires chat.json and handoff.json'); failed=True; continue
            h=json.loads(hp.read_text()); c=json.loads(cp.read_text()); errs=validate_handoff(h,s,c)
            if errs:
                failed=True
                for e in errs: print(f'FAIL {sid}: {e}')
            else: print(f'PASS handoff {sid}')
        elif s.get('handoff_id') and not hp.exists():
            print(f'FAIL {sid}: session references handoff_id but handoff.json missing'); failed=True

        pred=s.get('predecessor_session_id'); consumed=s.get('consumed_handoff_id')
        if pred:
            if pred not in docs:
                print(f'FAIL {sid}: predecessor session not found: {pred}'); failed=True; continue
            psp,ps=docs[pred]; php=psp.with_name('handoff.json')
            if not php.exists():
                print(f'FAIL {sid}: predecessor handoff missing'); failed=True; continue
            ph=json.loads(php.read_text())
            if consumed != ph.get('handoff_id'):
                print(f'FAIL {sid}: consumed_handoff_id does not match predecessor handoff'); failed=True
            if s['status'] in {'ACTIVE','PAUSED','REVIEW_PENDING','COMPLETED','ARCHIVED'} and not consumed:
                print(f'FAIL {sid}: active-or-later successor must consume predecessor handoff'); failed=True
            if ph.get('next_session_status')=='TARGET_SELECTED' and ph.get('target_session_id') != sid:
                print(f'FAIL {sid}: predecessor explicitly targets another session'); failed=True
        elif consumed:
            print(f'FAIL {sid}: consumed_handoff_id present without predecessor_session_id'); failed=True
    if not docs: print('PASS handoff contracts (0 sessions)')
    return 1 if failed else 0

if __name__=='__main__': raise SystemExit(main())

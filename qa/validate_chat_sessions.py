#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'schemas/chat-session-v1.schema.json').read_text())
V=Draft202012Validator(SCHEMA,format_checker=FormatChecker())


def validate_chat(chat, session):
    errs=[e.message for e in V.iter_errors(chat)]
    if chat.get('session_id') != session.get('session_id'):
        errs.append('chat.session_id must match session.session_id')
    if chat.get('primary_session_type') != session.get('session_type'):
        errs.append('chat primary_session_type must match session_type')
    expected_snapshot=session.get('control_snapshot',{}).get('snapshot_id')
    if chat.get('startup_repository_snapshot_id') != expected_snapshot:
        errs.append('chat startup_repository_snapshot_id must match session control snapshot')

    status=session.get('status')
    cstatus=chat.get('status')
    if status=='READY' and cstatus not in {'PLANNED','OPEN'}:
        errs.append('READY repository session chat must be PLANNED or OPEN when chat exists')
    if status=='ACTIVE' and cstatus!='OPEN':
        errs.append('ACTIVE repository session requires OPEN chat')
    if status=='PAUSED' and cstatus!='PAUSED':
        errs.append('PAUSED repository session requires PAUSED chat')
    if status=='REVIEW_PENDING' and cstatus not in {'OPEN','PAUSED'}:
        errs.append('REVIEW_PENDING repository session requires OPEN or PAUSED chat')
    if status in {'COMPLETED','ARCHIVED','ABORTED'} and cstatus!='CLOSED':
        errs.append('terminal repository session requires CLOSED chat')
    if status=='SUPERSEDED' and cstatus not in {'CLOSED','SUPERSEDED'}:
        errs.append('SUPERSEDED repository session requires CLOSED or SUPERSEDED chat')
    if cstatus in {'OPEN','PAUSED','CLOSED','SUPERSEDED'} and not chat.get('opened_at'):
        errs.append(f'{cstatus} chat requires opened_at')
    if cstatus=='PAUSED' and not chat.get('resume_anchor'):
        errs.append('PAUSED chat requires resume_anchor')
    if cstatus=='CLOSED' and not chat.get('closed_at'):
        errs.append('CLOSED chat requires closed_at')
    if chat.get('handoff_required') and not chat.get('handoff_target_session_id'):
        errs.append('handoff_required requires handoff_target_session_id')
    return errs


def main():
    failed=False
    root=ROOT/'sessions'
    if not root.exists():
        print('PASS chat contracts (0 sessions)')
        return 0
    for session_path in sorted(root.glob('*/session.json')):
        session=json.loads(session_path.read_text())
        chat_path=session_path.with_name('chat.json')
        status=session.get('status')

        # A PLANNED session must exist before its ChatGPT chat. READY/BLOCKED may
        # also exist before the learner-facing chat has been opened.
        if not chat_path.exists():
            if status in {'PLANNED','READY','BLOCKED'}:
                print(f'PASS {session_path.parent.name}: chat not required yet for {status}')
                continue
            print(f'FAIL {session_path.parent.name}: missing chat.json for {status} session')
            failed=True
            continue

        if status=='PLANNED':
            print(f'FAIL {session_path.parent.name}: PLANNED session must not have chat.json')
            failed=True
            continue

        chat=json.loads(chat_path.read_text())
        errs=validate_chat(chat,session)
        if errs:
            failed=True; print(f'FAIL {chat_path}')
            for e in errs: print('  -',e)
        else:
            print(f'PASS {chat_path}')
    return 1 if failed else 0

if __name__=='__main__': raise SystemExit(main())

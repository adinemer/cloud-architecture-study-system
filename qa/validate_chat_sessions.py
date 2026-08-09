#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'schemas/chat-session-v1.schema.json').read_text())
V=Draft202012Validator(SCHEMA,format_checker=FormatChecker())

def main():
    failed=False
    root=ROOT/'sessions'
    if not root.exists():
        print('PASS chat contracts (0 sessions)')
        return 0
    for session_path in sorted(root.glob('*/session.json')):
        session=json.loads(session_path.read_text())
        chat_path=session_path.with_name('chat.json')
        if not chat_path.exists():
            print(f'FAIL {session_path.parent.name}: missing chat.json')
            failed=True; continue
        chat=json.loads(chat_path.read_text())
        errs=[e.message for e in V.iter_errors(chat)]
        if chat.get('session_id') != session.get('session_id'):
            errs.append('chat.session_id must match session.session_id')
        if chat.get('primary_session_type') != session.get('session_type'):
            errs.append('chat primary_session_type must match session_type')
        status=session.get('status')
        cstatus=chat.get('status')
        if status in {'ACTIVE','REVIEW_PENDING'} and cstatus not in {'OPEN','PAUSED'}:
            errs.append('active/review-pending repository session requires OPEN or PAUSED chat')
        if status in {'COMPLETED','ARCHIVED','ABORTED','SUPERSEDED'} and cstatus not in {'CLOSED','SUPERSEDED'}:
            errs.append('terminal repository session requires CLOSED/SUPERSEDED chat')
        if cstatus=='PAUSED' and not chat.get('resume_anchor'):
            errs.append('PAUSED chat requires resume_anchor')
        if cstatus=='CLOSED' and not chat.get('closed_at'):
            errs.append('CLOSED chat requires closed_at')
        if chat.get('handoff_required') and not chat.get('handoff_target_session_id'):
            errs.append('handoff_required requires handoff_target_session_id')
        if errs:
            failed=True; print(f'FAIL {chat_path}')
            for e in errs: print('  -',e)
        else: print(f'PASS {chat_path}')
    return 1 if failed else 0

if __name__=='__main__': raise SystemExit(main())

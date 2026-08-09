#!/usr/bin/env python3
import argparse, hashlib, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GOVERNANCE=[
'docs/00-system-charter.md','docs/02-chatgpt-operating-spec.md','docs/03-source-policy.md','docs/04-study-sequence-spec.md',
'docs/05-extraction-pipeline-spec.md','docs/07-study-artifact-schemas.md','docs/08-quality-assurance-spec.md','docs/09-progress-mastery-spec.md',
'docs/11-study-session-management.md','docs/12-coordinator-governance.md','docs/13-change-control-freshness.md',
'docs/14-study-operating-routine.md','docs/15-study-tool-policy.md','docs/16-chat-session-management.md','docs/17-pipeline-health-spec.md',
'state/pipeline-health.json']

def h(rel): return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()

def git_sha():
    try: return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    except Exception: return '0'*40

def build(session_id):
    project=json.loads((ROOT/'state/project-state.json').read_text())
    mastery=json.loads((ROOT/'state/mastery-state.json').read_text())
    return {
      'snapshot_id':f"{session_id}-snapshot-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
      'repository_commit_sha':git_sha(),
      'created_at':datetime.now(timezone.utc).isoformat(),
      'governance_hashes':{x:h(x) for x in GOVERNANCE},
      'objective_map_hash':h('aws/sap-c02/objective-map.md'),
      'artifact_schema_version':'1.0.0','session_schema_version':'1.0.0',
      'prompt_versions':['extract-v1','enrich-v1','qa-v1','artifact-v1','artifact-qa-v1'],
      'project_state_version':project['state_version'],'mastery_state_version':mastery['state_version']
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--session-id',required=True); p.add_argument('--out'); a=p.parse_args(); d=build(a.session_id)
    text=json.dumps(d,indent=2)+'\n'
    if a.out: Path(a.out).write_text(text)
    else: print(text,end='')

if __name__=='__main__': main()

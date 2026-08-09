#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from pipeline_fingerprint import fingerprint

ROOT = Path(__file__).resolve().parents[1]


def main():
    state_path = ROOT / 'state/pipeline-health.json'
    if not state_path.exists():
        print('FAIL pipeline health: state/pipeline-health.json missing')
        return 1
    state = json.loads(state_path.read_text())
    schema = json.loads((ROOT/'schemas/pipeline-health-v1.schema.json').read_text())
    errors = [e.message for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(state)]
    if state.get('health') != 'GREEN':
        errors.append(f"pipeline health is {state.get('health')}, expected GREEN")
    current = fingerprint()
    if state.get('pipeline_fingerprint') != current:
        errors.append('pipeline health fingerprint is stale for current extraction-affecting files')
    if errors:
        for e in errors:
            print('FAIL pipeline health:', e)
        return 1
    print('PASS pipeline health GREEN')
    print('fingerprint', current)
    print('workflow run', state['workflow_run_id'], 'job', state['workflow_job_id'])
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

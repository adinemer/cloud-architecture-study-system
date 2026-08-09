#!/usr/bin/env python3
import sys
from pathlib import Path
from render_artifact import render
import json


def main():
    root = Path('artifacts')
    if not root.exists():
        print('No production artifacts yet; render integrity check skipped.')
        return 0
    failed = False
    for jp in sorted(root.rglob('*.json')):
        mp = jp.with_suffix('.md')
        if not mp.exists():
            print(f'FAIL {jp}: missing rendered Markdown {mp}')
            failed = True
            continue
        expected = render(json.loads(jp.read_text()))
        actual = mp.read_text()
        if actual != expected:
            print(f'FAIL {mp}: differs from deterministic render of {jp}')
            failed = True
        else:
            print(f'PASS {mp}')
    return 1 if failed else 0

if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Create a deterministic prompt bundle from normalized source and a prompt template."""
import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--source', type=Path, required=True)
ap.add_argument('--prompt', type=Path, required=True)
ap.add_argument('--out', type=Path, required=True)
a = ap.parse_args()
meta_path = a.source.with_suffix(a.source.suffix + '.source.json')
meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
bundle = (
    a.prompt.read_text().rstrip()
    + "\n\n---\n\n## SOURCE METADATA\n\n```json\n"
    + json.dumps(meta, indent=2)
    + "\n```\n\n## SOURCE CONTENT\n\n"
    + a.source.read_text().rstrip()
    + "\n"
)
a.out.parent.mkdir(parents=True, exist_ok=True)
a.out.write_text(bundle)
print(a.out)

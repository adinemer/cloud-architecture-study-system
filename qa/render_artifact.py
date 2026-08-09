#!/usr/bin/env python3
import argparse, json
from pathlib import Path


def titleize(key):
    return key.replace('_', ' ').strip().title()


def render_value(key, value, level=2):
    lines = []
    heading = '#' * level + ' ' + titleize(key)
    if isinstance(value, str):
        lines += [heading, '', value, '']
    elif value is None:
        return []
    elif isinstance(value, bool):
        lines += [heading, '', str(value).lower(), '']
    elif isinstance(value, list):
        lines += [heading, '']
        for item in value:
            if isinstance(item, dict):
                lines.append('- ' + '; '.join(f'**{titleize(k)}:** {v}' for k, v in item.items()))
            else:
                lines.append(f'- {item}')
        lines.append('')
    elif isinstance(value, dict):
        lines += [heading, '']
        for k, v in value.items():
            lines += render_value(k, v, level + 1)
    else:
        lines += [heading, '', str(value), '']
    return lines


def render(doc):
    m = doc['meta']
    out = [
        '<!-- GENERATED FILE: edit canonical JSON, then re-render. -->',
        '',
        f'# {titleize(m["artifact_type"])} — {m["artifact_id"]}',
        '',
        f'- Artifact version: `{m["artifact_version"]}`',
        f'- Schema version: `{m["schema_version"]}`',
        f'- Status: `{m["status"]}`',
        f'- QA: `{m["qa_state"]}`',
        f'- Certification: `{m["certification"]}`',
        f'- Units: {", ".join(m["unit_ids"])}',
        f'- Objectives: {", ".join(m["objective_ids"])}',
        '',
        '## Content',
        ''
    ]
    for k, v in doc['content'].items():
        out += render_value(k, v, 3)

    if doc.get('claims'):
        out += ['## Claims', '']
        for c in doc['claims']:
            out.append(f'### {c["claim_id"]} — `{c["label"]}`')
            out.append('')
            out.append(c['text'])
            out.append('')
            if c.get('inference_rationale'):
                out += [f'**Inference rationale:** {c["inference_rationale"]}', '']
            for r in c.get('source_refs', []):
                out.append(f'- Source: `{r["source_id"]}` — {r["locator"]}')
            out.append('')

    out += ['## Sources', '']
    for s in doc['sources']:
        out += [
            f'### {s["source_id"]}', '',
            f'- Title: {s["title"]}',
            f'- Canonical URL: {s["canonical_url"]}',
            f'- Retrieved: {s["retrieved_at"]}',
            f'- Processing class: `{s["processing_class"]}`',
            ''
        ]
    return '\n'.join(out).rstrip() + '\n'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('input')
    p.add_argument('--out', required=True)
    args = p.parse_args()
    doc = json.loads(Path(args.input).read_text())
    Path(args.out).write_text(render(doc))
    print(args.out)

if __name__ == '__main__':
    main()

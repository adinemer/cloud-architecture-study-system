#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print('ERROR: install jsonschema', file=sys.stderr)
    raise

ALLOWED_OBJECTIVES = {
    '1.1','1.2','1.3','1.4','1.5',
    '2.1','2.2','2.3','2.4','2.5','2.6',
    '3.1','3.2','3.3','3.4','3.5',
    '4.1','4.2','4.3','4.4'
}


def semantic_errors(doc):
    errors = []
    meta = doc.get('meta', {})
    sources = {s.get('source_id'): s for s in doc.get('sources', [])}
    source_ids = set(sources)

    if set(meta.get('source_ids', [])) != source_ids:
        errors.append('meta.source_ids must exactly match sources[].source_id')

    bad_obj = set(meta.get('objective_ids', [])) - ALLOWED_OBJECTIVES
    if bad_obj:
        errors.append(f'unknown SAP-C02 objective ids: {sorted(bad_obj)}')

    claim_ids = set()
    for c in doc.get('claims', []):
        cid = c.get('claim_id')
        if cid in claim_ids:
            errors.append(f'duplicate claim_id: {cid}')
        claim_ids.add(cid)

        refs = c.get('source_refs', [])
        for ref in refs:
            if ref.get('source_id') not in source_ids:
                errors.append(f'{cid}: source ref not registered: {ref.get("source_id")}')

        label = c.get('label')
        if label in {'PROVIDER_FACT','PROVIDER_RECOMMENDATION'} and not refs:
            errors.append(f'{cid}: provider claim requires source reference')
        if label == 'ARCHITECTURAL_INFERENCE':
            if not refs:
                errors.append(f'{cid}: architectural inference requires supporting source')
            if not c.get('inference_rationale'):
                errors.append(f'{cid}: architectural inference requires inference_rationale')
        if label == 'CROSS_SOURCE_SYNTHESIS' and len({r.get('source_id') for r in refs}) < 2:
            errors.append(f'{cid}: cross-source synthesis requires at least two distinct sources')
        if label == 'EXAM_INTERPRETATION':
            objs = c.get('objective_ids', [])
            if not refs or not objs:
                errors.append(f'{cid}: exam interpretation requires source refs and objective_ids')
            bad = set(objs) - ALLOWED_OBJECTIVES
            if bad:
                errors.append(f'{cid}: unknown objective ids: {sorted(bad)}')

        if c.get('severity') == 'HIGH':
            if not refs or any(not r.get('locator') for r in refs):
                errors.append(f'{cid}: HIGH claim requires explicit source locator')

    if meta.get('status') == 'APPROVED' and meta.get('qa_state') != 'PASS':
        errors.append('APPROVED artifact requires qa_state=PASS')

    if meta.get('artifact_type') == 'flashcard_set':
        cards = doc.get('content', {}).get('cards', [])
        if len(cards) > 20 and not meta.get('exception_reason'):
            errors.append('flashcard set >20 cards requires meta.exception_reason')
        for card in cards:
            for ref in card.get('source_refs', []):
                if ref.get('source_id') not in source_ids:
                    errors.append(f'flashcard {card.get("card_id")}: unknown source_id')
            if card.get('volatility') == 'HIGH' and not meta.get('last_reviewed_at'):
                errors.append(f'flashcard {card.get("card_id")}: HIGH volatility requires last_reviewed_at')

    if meta.get('artifact_type') == 'assessment_set':
        if doc.get('content', {}).get('assessment_label') != 'GENERATED_ASSESSMENT':
            errors.append('generated assessment must declare GENERATED_ASSESSMENT')

    return errors


def main():
    p = argparse.ArgumentParser()
    p.add_argument('files', nargs='+')
    p.add_argument('--schema', default='schemas/artifact-v1.schema.json')
    args = p.parse_args()
    schema = json.loads(Path(args.schema).read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failed = False
    seen_artifact_ids = {}

    for name in args.files:
        path = Path(name)
        doc = json.loads(path.read_text())
        problems = [e.message for e in validator.iter_errors(doc)] + semantic_errors(doc)
        aid = doc.get('meta', {}).get('artifact_id')
        status = doc.get('meta', {}).get('status')
        if aid and status != 'SUPERSEDED':
            if aid in seen_artifact_ids:
                problems.append(f'duplicate active artifact_id also in {seen_artifact_ids[aid]}')
            else:
                seen_artifact_ids[aid] = str(path)
        if problems:
            failed = True
            print(f'FAIL {path}')
            for problem in problems:
                print(f'  - {problem}')
        else:
            print(f'PASS {path}')

    return 1 if failed else 0

if __name__ == '__main__':
    raise SystemExit(main())

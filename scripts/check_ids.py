#!/usr/bin/env python3
"""
Make sure no chapter or topic id disappears. Learners' saved progress is keyed on ids,
so an id may only go away if data/redirects.json maps it to its replacement.

  python scripts/check_ids.py                 compare the working tree with origin/main
  python scripts/check_ids.py --base v1.0.0   compare with any git ref

Exit code 1 lists every id that vanished without a redirect.
"""

import io, json, pathlib, subprocess, sys, tarfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def ids_from_chapters(chapters):
    ch, tp = set(), set()

    def walk(items):
        for t in items:
            if t.get('id'):
                tp.add(t['id'])
            walk(t.get('sub', []))

    for c in chapters:
        ch.add(c['id'])
        walk(c.get('topics', []))
    return ch, tp


def read_tree(files):
    """files: {relative path: text}. Handles both the per-chapter layout and old single files."""
    chapters = []
    for path, text in files.items():
        parts = path.split('/')
        if parts[:2] != ['data', 'disciplines'] or not path.endswith('.json'):
            continue
        doc = json.loads(text)
        if len(parts) == 3:                      # old layout: data/disciplines/<id>.json
            chapters += doc.get('chapters', [])
        elif parts[3] != 'discipline.json':      # new layout: data/disciplines/<id>/<chapter>.json
            chapters.append(doc)
    return ids_from_chapters(chapters)


def main():
    args = sys.argv[1:]
    base = args[args.index('--base') + 1] if '--base' in args else 'origin/main'
    try:
        raw = subprocess.run(['git', 'archive', '--format=tar', base, 'data'], cwd=ROOT,
                             capture_output=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        sys.exit(f'could not read {base}: {e.stderr.decode().strip()}')
    with tarfile.open(fileobj=io.BytesIO(raw)) as tar:
        old = read_tree({m.name: tar.extractfile(m).read().decode('utf-8') for m in tar.getmembers() if m.isfile()})

    here = {str(p.relative_to(ROOT)).replace('\\', '/'): p.read_text(encoding='utf-8')
            for p in (ROOT / 'data' / 'disciplines').rglob('*.json')}
    new = read_tree(here)
    redirects = json.loads((ROOT / 'data' / 'redirects.json').read_text(encoding='utf-8'))

    problems = []
    for kind, i in (('chapters', 0), ('topics', 1)):
        moves = redirects.get(kind, {})
        for old_id, new_id in moves.items():
            if new_id not in new[i]:
                problems.append(f'redirect {old_id} -> {new_id}: target {kind[:-1]} does not exist')
            if old_id in new[i]:
                problems.append(f'redirect {old_id} -> {new_id}: {old_id} still exists, so the redirect is wrong')
        for gone in sorted(old[i] - new[i] - set(moves)):
            problems.append(f'{kind[:-1]} id "{gone}" was removed or renamed. Restore it, or add it to '
                            f'data/redirects.json under "{kind}"')

    if problems:
        print('\n'.join('ERROR   ' + p for p in problems))
        sys.exit(1)
    print(f'OK: all {len(old[0])} chapter and {len(old[1])} topic ids from {base} are still reachable')


if __name__ == '__main__':
    main()

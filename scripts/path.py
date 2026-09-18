#!/usr/bin/env python3
"""
Print everything you need to learn before one or more chapters, in a valid order.

  python scripts/path.py ae-liquid-rocket-engines
  python scripts/path.py ph-cosmology ae-orbital-mechanics-fundamentals --tsv
  python scripts/path.py --find "rocket"          search chapter names/ids

Reads the generated knowledge_base.json, so run scripts/build.py after editing data/.
"""

import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    kb = json.loads((ROOT / 'knowledge_base.json').read_text(encoding='utf-8'))
    ch = {c['id']: (s, c) for s in kb['subjects'] for c in s['chapters']}

    if args[0] == '--find':
        q = ' '.join(args[1:]).lower()
        for cid, (s, c) in ch.items():
            if q in cid or q in c['name'].lower():
                print(f'{cid}\t{s["id"]}\tL{c["level"]}\t{c["name"]}')
        return

    tsv = '--tsv' in args
    targets = [a for a in args if not a.startswith('--')]
    missing = [t for t in targets if t not in ch]
    if missing:
        sys.exit(f'unknown chapter id(s): {", ".join(missing)} (try --find)')

    need = set()

    def walk(cid):
        for p in ch[cid][1]['prerequisites']:
            if p not in need:
                need.add(p)
                walk(p)

    for t in targets:
        walk(t)
    order = sorted(need - set(targets), key=lambda i: (ch[i][1]['depth'], ch[i][0]['id'], ch[i][1]['order']))
    for i in order + targets:
        s, c = ch[i]
        mark = '  <- target' if i in targets else ''
        if tsv:
            print(f'{c["depth"]}\t{i}\t{s["id"]}\tL{c["level"]}\t{c["name"]}\t{",".join(c["prerequisites"])}')
        else:
            print(f'step {c["depth"]:>2}  {s["icon"]} {c["name"]}  [{i}, L{c["level"]}]{mark}')
    print(f'\n{len(order)} chapter(s) before {", ".join(targets)}', file=sys.stderr)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Validate data/ and generate knowledge_base.js + knowledge_base.json.

  python scripts/build.py            validate, assign missing topic ids, generate
  python scripts/build.py --check    validate only (no writes); exit 1 on errors
  python scripts/build.py --only physics   limit printed warnings to lines mentioning "physics"
  python scripts/build.py --discipline chemistry
                                     validate one discipline file (no writes); other
                                     files are only used to resolve cross-references

See data/SCHEMA.md for the format.
"""

import json, pathlib, sys, datetime, collections, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
LEVELS = {1, 2, 3, 4, 5}
PRIORITIES = ['core', 'important', 'advanced', 'optional']


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def assign_topic_ids(chapter):
    """Give every topic/sub-topic without an id a stable one. Returns True if anything changed."""
    changed = False

    def fill(items, prefix):
        nonlocal changed
        used = set()
        for t in items:
            m = re.fullmatch(re.escape(prefix) + r'-(\d+)', t.get('id', ''))
            if m:
                used.add(int(m.group(1)))
        n = max(used, default=0)
        for t in items:
            if not t.get('id'):
                n += 1
                t['id'] = f'{prefix}-{n}'
                changed = True
            if t.get('sub'):
                fill(t['sub'], t['id'])

    fill(chapter.get('topics', []), chapter['id'])
    return changed


def flatten(topics, chapter, depth=0, parent=None):
    out = []
    for t in topics:
        row = {'id': t['id'], 'name': t['name'], 'priority': t.get('priority', chapter['priority'])}
        if depth:
            row['depth'] = depth
            row['parent'] = parent
        out.append(row)
        out += flatten(t.get('sub', []), chapter, depth + 1, t['id'])
    return out


def find_cycle(nodes, edges):
    """edges: id -> list of prerequisite ids. Returns one cycle as a list, or None."""
    WHITE, GREY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}
    stack = []

    def visit(n):
        color[n] = GREY
        stack.append(n)
        for p in edges.get(n, []):
            if color.get(p) == GREY:
                return stack[stack.index(p):] + [p]
            if color.get(p) == WHITE:
                c = visit(p)
                if c:
                    return c
        stack.pop()
        color[n] = BLACK
        return None

    sys.setrecursionlimit(20000)
    for n in nodes:
        if color[n] == WHITE:
            c = visit(n)
            if c:
                return c
    return None


def main():
    scope = sys.argv[sys.argv.index('--discipline') + 1] if '--discipline' in sys.argv else None
    check_only = '--check' in sys.argv or scope is not None
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    manifest = load(DATA / 'manifest.json')
    errors, warnings = [], []

    disciplines = []
    for did in manifest['disciplines']:
        path = DATA / 'disciplines' / f'{did}.json'
        try:
            doc = load(path)
        except (OSError, ValueError) as e:
            if scope and did != scope:
                print(f'note: skipping unreadable {path.name} ({e.__class__.__name__})')
                continue
            raise
        changed = False
        for ch in doc['chapters']:
            changed |= assign_topic_ids(ch)
        if changed and not check_only:
            dump(path, doc)
        disciplines.append(doc)

    # ---- index + field validation -------------------------------------------------
    chapters, owner, topic_ids = {}, {}, collections.Counter()
    for d in disciplines:
        prefix = d.get('prefix')
        for ch in d['chapters']:
            cid = ch.get('id', '?')
            if cid in chapters:
                errors.append(f'duplicate chapter id {cid}')
            chapters[cid], owner[cid] = ch, d['id']
            if prefix and not cid.startswith(prefix + '-'):
                warnings.append(f'{d["id"]}: {cid} does not start with "{prefix}-"')
            for field in ('name', 'category'):
                if not ch.get(field):
                    errors.append(f'{cid}: missing {field}')
            if ch.get('level') not in LEVELS:
                errors.append(f'{cid}: level must be 1-5 (got {ch.get("level")!r})')
            if ch.get('priority') not in PRIORITIES:
                errors.append(f'{cid}: priority must be one of {PRIORITIES} (got {ch.get("priority")!r})')
            if not ch.get('summary'):
                warnings.append(f'{cid}: missing summary')
            if not ch.get('topics'):
                warnings.append(f'{cid}: has no topics')

            def count(ts):
                for t in ts:
                    topic_ids[t['id']] += 1
                    count(t.get('sub', []))
            count(ch.get('topics', []))
    for tid, n in topic_ids.items():
        if n > 1:
            errors.append(f'duplicate topic id {tid}')

    edges = {}
    for cid, ch in chapters.items():
        prereqs = ch.get('prerequisites', [])
        for p in prereqs:
            if p not in chapters:
                errors.append(f'{cid}: unknown prerequisite {p}')
            elif p == cid:
                errors.append(f'{cid}: lists itself as a prerequisite')
        if len(set(prereqs)) != len(prereqs):
            warnings.append(f'{cid}: duplicate prerequisites')
        for r in ch.get('related', []):
            if r not in chapters:
                errors.append(f'{cid}: unknown related chapter {r}')
        edges[cid] = [p for p in prereqs if p in chapters and p != cid]

    cycle = find_cycle(list(chapters), edges)
    if cycle:
        errors.append('prerequisite cycle: ' + ' -> '.join(cycle))

    if scope:
        owned = {cid for cid, o in owner.items() if o == scope}

        def mine(msg):
            return msg.startswith(scope + ':') or any(
                tok in owned for tok in re.findall(r'[a-z0-9]+(?:-[a-z0-9]+)+', msg))
        errors[:] = [e for e in errors if mine(e)]

    if errors:
        print('\n'.join('ERROR   ' + e for e in errors))
        print(f'\n{len(errors)} error(s); nothing generated.')
        sys.exit(1)

    # ---- derived data ---------------------------------------------------------------
    ancestors = {}

    def closure(cid):
        if cid not in ancestors:
            acc = set()
            for p in edges[cid]:
                acc.add(p)
                acc |= closure(p)
            ancestors[cid] = acc
        return ancestors[cid]

    gdepth = {}

    def depth(cid):
        if cid not in gdepth:
            gdepth[cid] = 1 + max((depth(p) for p in edges[cid]), default=0)
        return gdepth[cid]

    unlocks = collections.defaultdict(list)
    for cid in chapters:
        closure(cid), depth(cid)
        for p in edges[cid]:
            unlocks[p].append(cid)
        redundant = [p for p in edges[cid] if any(p in closure(q) for q in edges[cid] if q != p)]
        if redundant:
            warnings.append(f'{cid}: redundant prerequisites (already implied): {", ".join(redundant)}')

    # A discipline's stages are its chapters' global depths (which count prerequisites
    # from every discipline), renumbered 1..N. A chapter therefore always sits in a later
    # stage than anything it depends on, inside or outside its own discipline.
    stage = {}
    for d in disciplines:
        ids = [c['id'] for c in d['chapters']]
        rank = {g: i + 1 for i, g in enumerate(sorted({gdepth[i] for i in ids}))}
        stage.update({i: rank[gdepth[i]] for i in ids})

    if scope:
        warnings = [w for w in warnings if mine(w)]
        print('\n'.join('WARN    ' + w for w in warnings))
        mine_chs = [c for c in chapters.values() if owner[c['id']] == scope]
        n_topics = sum(1 for c in mine_chs for _ in flatten(c.get('topics', []), c))
        n_stages = max((stage[c['id']] for c in mine_chs), default=0)
        print(f'\nOK {scope}: {len(mine_chs)} chapters, {n_topics} topics, {n_stages} stages, '
              f'{len(warnings)} warning(s)')
        return

    # ---- roadmaps -------------------------------------------------------------------
    roadmaps = []
    for rid in manifest.get('roadmaps', []):
        rm = load(DATA / 'roadmaps' / f'{rid}.json')
        position = {}
        for si, st in enumerate(rm['stages']):
            for ii, it in enumerate(st['items']):
                cid = it['chapter']
                if cid not in chapters:
                    errors.append(f'roadmap {rid}: unknown chapter {cid}')
                    continue
                if cid in position:
                    warnings.append(f'roadmap {rid}: {cid} listed twice')
                position.setdefault(cid, (si, ii))
                for f in it.get('focus', []):
                    if f not in topic_ids:
                        errors.append(f'roadmap {rid}: {cid}: unknown focus topic {f}')
        for si, st in enumerate(rm['stages']):
            for ii, it in enumerate(st['items']):
                cid = it['chapter']
                if cid not in chapters:
                    continue
                for p in edges[cid]:
                    if p not in position:
                        warnings.append(f'roadmap {rid}: {cid} needs {p}, which is not in the roadmap')
                    elif position[p] >= (si, ii):
                        warnings.append(f'roadmap {rid}: {cid} needs {p}, which comes later (stage {position[p][0] + 1})')
        roadmaps.append(rm)

    if errors:
        print('\n'.join('ERROR   ' + e for e in errors))
        print(f'\n{len(errors)} error(s); nothing generated.')
        sys.exit(1)

    # ---- output -----------------------------------------------------------------------
    prio_rank = {p: i for i, p in enumerate(PRIORITIES)}
    subjects = []
    for d in disciplines:
        chs = d['chapters']
        index = {c['id']: i for i, c in enumerate(chs)}
        ordered = sorted(chs, key=lambda c: (stage[c['id']], c['level'], prio_rank[c['priority']], index[c['id']]))
        order = {c['id']: i + 1 for i, c in enumerate(ordered)}
        categories = list(dict.fromkeys(c['category'] for c in chs))
        out_chs = []
        for c in chs:
            cid = c['id']
            out_chs.append({
                'id': cid, 'name': c['name'], 'category': c['category'],
                'level': c['level'], 'priority': c['priority'], 'summary': c.get('summary', ''),
                'prerequisites': c.get('prerequisites', []), 'related': c.get('related', []),
                'unlocks': unlocks.get(cid, []),
                'order': order[cid], 'stage': stage[cid], 'depth': gdepth[cid],
                'ancestorCount': len(ancestors[cid]),
                'topics': flatten(c.get('topics', []), c),
            })
        subjects.append({k: d.get(k, '') for k in ('id', 'name', 'icon', 'color', 'prefix', 'description')}
                        | {'categories': categories, 'chapters': out_chs})

    total_ch = sum(len(s['chapters']) for s in subjects)
    total_t = sum(len(c['topics']) for s in subjects for c in s['chapters'])
    data = {
        'version': '4.0.0',
        'generatedAt': datetime.date.today().isoformat(),
        'stats': {'disciplines': len(subjects), 'chapters': total_ch, 'topics': total_t,
                  'roadmaps': len(roadmaps), 'prerequisiteLinks': sum(len(v) for v in edges.values())},
        'subjects': subjects,
        'roadmaps': roadmaps,
        'learningPaths': {},
    }

    shown = [w for w in warnings if not only or only in w]
    if shown:
        print('\n'.join('WARN    ' + w for w in shown[:400]))
        if len(shown) > 400:
            print(f'... {len(shown) - 400} more')
    print(f'\n{len(subjects)} disciplines, {total_ch} chapters, {total_t} topics, '
          f'{data["stats"]["prerequisiteLinks"]} prerequisite links, {len(roadmaps)} roadmaps')
    for s in subjects:
        n_t = sum(len(c['topics']) for c in s['chapters'])
        n_st = max((c['stage'] for c in s['chapters']), default=0)
        print(f'  {s["id"]:<12} {len(s["chapters"]):>4} chapters {n_t:>5} topics  {n_st} stages')
    print(f'{len(warnings)} warning(s)')

    if check_only:
        return
    js = ('// Generated by scripts/build.py from data/. Do not edit by hand.\n'
          'var knowledgeBaseData = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')
    (ROOT / 'knowledge_base.js').write_text(js, encoding='utf-8')
    dump(ROOT / 'knowledge_base.json', data)
    print('wrote knowledge_base.js, knowledge_base.json')


if __name__ == '__main__':
    main()

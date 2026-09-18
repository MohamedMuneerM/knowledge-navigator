#!/usr/bin/env python3
"""
Validate data/ and generate knowledge_base.js + knowledge_base.json.

  python scripts/build.py                 validate, fill in missing topic ids, tidy the
                                          formatting of data files, generate the outputs
  python scripts/build.py --check         validate only (no writes); exit 1 on errors
  python scripts/build.py --strict        like --check, but warnings also fail (used by CI)
  python scripts/build.py --only rocket   print only warnings that mention "rocket"
  python scripts/build.py --discipline chemistry
                                          validate one discipline; the others are only used
                                          to resolve cross-references

No dependencies beyond Python 3.9+. See data/SCHEMA.md for the format.
"""

import collections, datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
LEVELS = {1, 2, 3, 4, 5}
PRIORITIES = ['core', 'important', 'advanced', 'optional']
CHAPTER_KEYS = ['id', 'name', 'category', 'level', 'priority', 'summary', 'prerequisites', 'related', 'topics']
ID_RE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:   # LF on every OS
        f.write(text)


def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + '\n'


def canonical_topics(items):
    out = []
    for t in items:
        row = {'id': t.get('id'), 'name': t.get('name')}
        row.update({k: v for k, v in t.items() if k not in ('id', 'name', 'sub')})
        if t.get('sub'):
            row['sub'] = canonical_topics(t['sub'])
        out.append(row)
    return out


def canonical_chapter(ch):
    out = {k: ch[k] for k in CHAPTER_KEYS if k in ch}
    out.setdefault('prerequisites', [])
    out.setdefault('related', [])
    out['topics'] = canonical_topics(ch.get('topics', []))
    out.update({k: v for k, v in ch.items() if k not in CHAPTER_KEYS})
    return out


def assign_topic_ids(chapter):
    """Give every topic/sub-topic without an id a stable one: <parent>-<next number>."""
    def fill(items, prefix):
        used = [int(m.group(1)) for t in items
                if (m := re.fullmatch(re.escape(prefix) + r'-(\d+)', t.get('id') or ''))]
        n = max(used, default=0)
        for t in items:
            if not t.get('id'):
                n += 1
                t['id'] = f'{prefix}-{n}'
            if t.get('sub'):
                fill(t['sub'], t['id'])

    fill(chapter.get('topics', []), chapter['id'])


def flatten(topics, chapter, depth=0, parent=None):
    out = []
    for t in topics:
        row = {'id': t['id'], 'name': t['name']}
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


def load_discipline(did, errors, save):
    """Read data/disciplines/<did>/: discipline.json plus one <chapter-id>.json per chapter."""
    ddir = DATA / 'disciplines' / did
    meta = load(ddir / 'discipline.json')
    if meta.get('id') != did:
        errors.append(f'{did}: discipline.json id must be "{did}"')
    chapters, unformatted = [], 0
    for path in sorted(ddir.glob('*.json')):
        if path.name == 'discipline.json':
            continue
        rel = f'{did}/{path.name}'
        try:
            ch = load(path)
        except ValueError as e:
            errors.append(f'{rel}: invalid JSON ({e})')
            continue
        if not isinstance(ch, dict) or not ch.get('id'):
            errors.append(f'{rel}: missing "id"')
            continue
        if ch['id'] != path.stem:
            errors.append(f'{rel}: id "{ch["id"]}" must match the file name ({path.stem})')
        assign_topic_ids(ch)
        ch = canonical_chapter(ch)
        if dumps(ch) != path.read_text(encoding='utf-8'):
            unformatted += 1
            if save:
                write(path, dumps(ch))
        chapters.append(ch)
    meta['chapters'] = chapters
    return meta, unformatted


def main():
    args = sys.argv[1:]
    scope = args[args.index('--discipline') + 1] if '--discipline' in args else None
    strict = '--strict' in args
    check_only = '--check' in args or strict or scope is not None
    only = args[args.index('--only') + 1] if '--only' in args else None
    manifest = load(DATA / 'manifest.json')
    errors, warnings = [], []

    disciplines, unformatted = [], 0
    for did in manifest['disciplines']:
        meta, n = load_discipline(did, errors, save=not check_only)
        disciplines.append(meta)
        unformatted += n
    on_disk = {p.name for p in (DATA / 'disciplines').iterdir() if p.is_dir()}
    for extra in sorted(on_disk - set(manifest['disciplines'])):
        errors.append(f'data/disciplines/{extra}/ is not listed in data/manifest.json')

    # ---- index + field validation -------------------------------------------------
    chapters, owner, topic_ids = {}, {}, collections.Counter()
    for d in disciplines:
        prefix, cats = d.get('prefix'), d.get('categories', [])
        for ch in d['chapters']:
            cid = ch['id']
            if cid in chapters:
                errors.append(f'duplicate chapter id {cid}')
            chapters[cid], owner[cid] = ch, d['id']
            if not ID_RE.fullmatch(cid):
                errors.append(f'{cid}: ids use lowercase letters, digits and hyphens only')
            if prefix and not cid.startswith(prefix + '-'):
                errors.append(f'{cid}: {d["id"]} chapter ids must start with "{prefix}-"')
            if not ch.get('name'):
                errors.append(f'{cid}: missing name')
            if ch.get('category') not in cats:
                errors.append(f'{cid}: category "{ch.get("category")}" is not listed in '
                              f'data/disciplines/{d["id"]}/discipline.json')
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
                    if not t.get('name'):
                        errors.append(f'{cid}: a topic has no name')
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
            elif chapters[p]['level'] > ch.get('level', 5):
                warnings.append(f'{cid}: prerequisite {p} has a higher level ({chapters[p]["level"]} > {ch["level"]})')
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
            return msg.startswith(scope) or any(tok in owned for tok in re.findall(r'[a-z0-9]+(?:-[a-z0-9]+)+', msg))
        errors[:] = [e for e in errors if mine(e)]

    if errors:
        print('\n'.join('ERROR   ' + e for e in errors))
        print(f'\n{len(errors)} error(s); nothing generated.')
        sys.exit(1)

    # ---- derived data ---------------------------------------------------------------
    ancestors, gdepth = {}, {}

    def closure(cid):
        if cid not in ancestors:
            acc = set()
            for p in edges[cid]:
                acc.add(p)
                acc |= closure(p)
            ancestors[cid] = acc
        return ancestors[cid]

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
        n_topics = sum(len(flatten(c.get('topics', []), c)) for c in mine_chs)
        n_stages = max((stage[c['id']] for c in mine_chs), default=0)
        print(f'\nOK {scope}: {len(mine_chs)} chapters, {n_topics} topics, {n_stages} stages, '
              f'{len(warnings)} warning(s)')
        sys.exit(1 if strict and warnings else 0)

    # ---- roadmaps -------------------------------------------------------------------
    roadmaps = []
    rm_files = {p.stem for p in (DATA / 'roadmaps').glob('*.json')}
    for extra in sorted(rm_files - set(manifest.get('roadmaps', []))):
        errors.append(f'data/roadmaps/{extra}.json is not listed in data/manifest.json')
    for rid in manifest.get('roadmaps', []):
        rm = load(DATA / 'roadmaps' / f'{rid}.json')
        if rm.get('id') != rid:
            errors.append(f'roadmap {rid}: id must match the file name')
        for field in ('name', 'icon', 'tagline', 'description', 'stages'):
            if not rm.get(field):
                errors.append(f'roadmap {rid}: missing {field}')
        for r in rm.get('related', []):
            if r not in manifest['roadmaps']:
                errors.append(f'roadmap {rid}: unknown related roadmap {r}')
        position = {}
        for si, st in enumerate(rm.get('stages', [])):
            for ii, it in enumerate(st['items']):
                cid = it['chapter']
                if cid not in chapters:
                    errors.append(f'roadmap {rid}: unknown chapter {cid}')
                    continue
                if cid in position:
                    warnings.append(f'roadmap {rid}: {cid} listed twice')
                position.setdefault(cid, (si, ii))
                if it.get('depth', 'full') not in ('full', 'selected'):
                    errors.append(f'roadmap {rid}: {cid}: depth must be "full" or "selected"')
                for f in it.get('focus', []):
                    if f not in topic_ids:
                        errors.append(f'roadmap {rid}: {cid}: unknown focus topic {f}')
        for si, st in enumerate(rm.get('stages', [])):
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

    redirects = load(DATA / 'redirects.json')
    for old, new in redirects.get('chapters', {}).items():
        if new not in chapters:
            errors.append(f'redirects.json: chapter {old} -> {new}: target does not exist')
    for old, new in redirects.get('topics', {}).items():
        if new not in topic_ids:
            errors.append(f'redirects.json: topic {old} -> {new}: target does not exist')

    if errors:
        print('\n'.join('ERROR   ' + e for e in errors))
        print(f'\n{len(errors)} error(s); nothing generated.')
        sys.exit(1)

    # ---- output -----------------------------------------------------------------------
    prio_rank = {p: i for i, p in enumerate(PRIORITIES)}
    subjects = []
    for d in disciplines:
        cats = [c for c in d['categories'] if any(ch['category'] == c for ch in d['chapters'])]
        teach = lambda c: (stage[c['id']], c['level'], prio_rank[c['priority']], c['name'].lower())
        order = {c['id']: i + 1 for i, c in enumerate(sorted(d['chapters'], key=teach))}
        # Display order: category order from discipline.json, then teaching order inside it.
        chs = sorted(d['chapters'], key=lambda c: (cats.index(c['category']), order[c['id']]))
        out_chs = [{
            'id': c['id'], 'name': c['name'], 'category': c['category'],
            'level': c['level'], 'priority': c['priority'], 'summary': c.get('summary', ''),
            'prerequisites': c['prerequisites'], 'related': c['related'],
            'unlocks': unlocks.get(c['id'], []),
            'order': order[c['id']], 'stage': stage[c['id']], 'depth': gdepth[c['id']],
            'ancestorCount': len(ancestors[c['id']]),
            'topics': flatten(c['topics'], c),
        } for c in chs]
        subjects.append({k: d.get(k, '') for k in ('id', 'name', 'icon', 'color', 'prefix', 'description')}
                        | {'categories': cats, 'chapters': out_chs})

    total_ch = sum(len(s['chapters']) for s in subjects)
    total_t = sum(len(c['topics']) for s in subjects for c in s['chapters'])
    data = {
        'version': manifest.get('version', ''),
        'generatedAt': datetime.date.today().isoformat(),
        'stats': {'disciplines': len(subjects), 'chapters': total_ch, 'topics': total_t,
                  'roadmaps': len(roadmaps), 'prerequisiteLinks': sum(len(v) for v in edges.values())},
        'subjects': subjects,
        'roadmaps': roadmaps,
        'redirects': {k: v for k, v in redirects.items() if not k.startswith('_')},
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
    if unformatted:
        print(f'{unformatted} chapter file(s) {"need" if check_only else "got"} tidying '
              f'(missing topic ids or formatting){"; run python scripts/build.py" if check_only else ""}')

    if check_only:
        sys.exit(1 if strict and warnings else 0)
    js = ('// Generated by scripts/build.py from data/. Do not edit by hand.\n'
          'var knowledgeBaseData = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')
    write(ROOT / 'knowledge_base.js', js)
    write(ROOT / 'knowledge_base.json', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    print('wrote knowledge_base.js, knowledge_base.json')


if __name__ == '__main__':
    main()

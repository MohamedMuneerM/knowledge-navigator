#!/usr/bin/env python3
"""
One-off migration: legacy/L notes (2).md + legacy knowledge_base.json
  -> data/disciplines/{physics,math,ai,electronics}.json  (new source of truth)

Fixes the bugs in the old parse_notes.py while keeping every existing
chapter/topic id, so progress saved in the browser still matches:
  * category headers containing "\\-" or lowercase letters (IoT, FPGAs, APIs)
    were silently skipped, so their chapters inherited the previous category
  * indented sub-bullets were dropped entirely (now restored, nested under "sub")
  * the un-numbered "**3D Vision**" block was glued onto the previous chapter
  * two different chapters shared the id el-configuration-management
"""

import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / 'legacy' / 'L notes (2).md'
OLD = ROOT / 'legacy' / 'knowledge_base.json'
OUT = ROOT / 'data' / 'disciplines'

RE_SUBJECT = re.compile(r'^#\s+\*\*(.+?)\*\*\s*:?\s*$')
RE_MAJOR_CAT = re.compile(r'^\*\*(\d+)\\?\.\s+([^*]+?)\*\*\s*$')
RE_CHAPTER_A = re.compile(r'^\*\*\d+\\?\.\s*\d+\s+(.+?)\*\*\s*$')
RE_CHAPTER_B = re.compile(r'^\*\*([A-Z0-9][^*\n]{3,}?)\*\*\s*$')
RE_TOPIC = re.compile(r'^(\s*)[*-]\s+(.+)$')

SUBJECT_META = {
    'physics': dict(name='Physics', icon='⚛️', color='#60c5f8', prefix='ph'),
    'math': dict(name='Mathematics', icon='∑', color='#fbbf24', prefix='ma'),
    'ai': dict(name='AI, Machine Learning & Robotics', icon='🤖', color='#a78bfa', prefix='ai'),
    'electronics': dict(name='Electronics, Embedded & IoT', icon='🔌', color='#10b981', prefix='el'),
}


def clean(text):
    text = re.sub(r'\*{1,3}', '', text.strip())
    return re.sub(r'\\(.)', r'\1', text).strip()


def title_case_category(raw):
    """'COMMUNICATION PROTOCOLS - WIRED' -> 'Communication Protocols – Wired'."""
    small = {'and', 'of', 'for', 'on', 'the', 'in', 'to', 'a'}
    keep = {'AI', 'ML', 'DL', 'RL', 'NLP', 'CV', 'IOT', 'IoT', 'FPGAS', 'FPGAs', 'HDL', 'APIS', 'APIs',
            'MLOPS', 'PCB', 'TSN', 'EMC', 'GOFAI', '(AI)', '(ML)', '(DL)', '(RL)', '(NLP)', '(CV)', '(FPGAs)'}
    fixes = {'IOT': 'IoT', 'FPGAS': 'FPGAs', 'APIS': 'APIs', 'MLOPS': 'MLOps', '(FPGAS)': '(FPGAs)'}
    words = []
    for i, w in enumerate(raw.split()):
        if w in fixes:
            words.append(fixes[w])
        elif w in keep or not w.isupper():
            words.append(w)
        elif w == '-':
            words.append('–')
        elif i and w.lower() in small:
            words.append(w.lower())
        else:
            words.append('-'.join(p.capitalize() for p in w.split('-')))
    return ' '.join(words).replace('Machine Learning (ML)', 'Machine Learning (ML)')


def parse_md():
    """Return {subject_id: [ {name, category, topics:[(depth, text)]} ]} in file order."""
    lines = MD.read_text(encoding='utf-8').splitlines()
    subjects, cur, chapter, category, variant_b = {}, None, None, None, False
    for raw in lines:
        m = RE_SUBJECT.match(raw)
        if m:
            name = clean(m.group(1)).lower()
            sid = ('physics' if 'physics' in name else 'math' if 'math' in name
                   else 'ai' if 'machine' in name else 'electronics')
            cur = subjects.setdefault(sid, [])
            chapter, category, variant_b = None, None, sid == 'electronics'
            continue
        if cur is None:
            continue
        m = RE_MAJOR_CAT.match(raw)
        if m and not RE_CHAPTER_A.match(raw):
            category, chapter = title_case_category(clean(m.group(2))), None
            continue
        if not variant_b:
            m = RE_CHAPTER_A.match(raw)
            if m:
                chapter = dict(name=clean(m.group(1)), category=category or 'General', topics=[])
                cur.append(chapter)
                continue
        else:
            m = RE_CHAPTER_B.match(raw)
            if m:
                chapter = dict(name=clean(m.group(1)), category=category or 'General', topics=[])
                cur.append(chapter)
                continue
        m = RE_TOPIC.match(raw)
        if m and chapter is not None:
            text = clean(m.group(2))
            if text:
                chapter['topics'].append((1 if len(m.group(1)) >= 2 else 0, text))
    return subjects


def nest(flat):
    """[(depth, topicDict)] -> nested list using 'sub'."""
    out, parent = [], None
    for depth, t in flat:
        if depth and parent is not None:
            parent.setdefault('sub', []).append(t)
        else:
            out.append(t)
            parent = t
    return out


def main():
    old = json.loads(OLD.read_text(encoding='utf-8'))
    parsed = parse_md()
    OUT.mkdir(parents=True, exist_ok=True)
    report, restored = [], [0]
    for subj in old['subjects']:
        sid = subj['id']
        new_chs = [c for c in parsed[sid]]
        # The legacy parser created a chapter for every variant-B bold line; our
        # parser additionally recognises "3D Vision" (starts with a digit).
        extra = [c for c in new_chs if c['name'] == '3D Vision']
        new_chs = [c for c in new_chs if c['name'] != '3D Vision']
        assert len(new_chs) == len(subj['chapters']), (sid, len(new_chs), len(subj['chapters']))
        chapters = []
        for oc, nc in zip(subj['chapters'], new_chs):
            assert oc['name'] == nc['name'], (oc['name'], nc['name'])
            if oc['id'] == 'el-stereo-vision-depth':
                nc['topics'] = nc['topics'] + extra[0]['topics']
            # The legacy parser dropped every indented sub-bullet; top-level
            # bullets line up 1:1 with the old topic ids.
            top = [x for x in nc['topics'] if x[0] == 0]
            assert [t['name'] for t in oc['topics']] == [x[1] for x in top], oc['id']
            ch = dict(id=oc['id'], name=oc['name'], category=nc['category'])
            old_ids = iter(t['id'] for t in oc['topics'])
            flat, parent_id, k = [], None, 0
            for d, text in nc['topics']:
                if d == 0:
                    parent_id, k = next(old_ids), 0
                    flat.append((0, dict(id=parent_id, name=text)))
                else:
                    k += 1
                    flat.append((1, dict(id=f'{parent_id}-{k}', name=text)))
                    restored[0] += 1
            ch['topics'] = nest(flat)
            if oc['category'] != nc['category']:
                report.append(f'{sid}: {oc["name"]}: "{oc["category"]}" -> "{nc["category"]}"')
            chapters.append(ch)

        if sid == 'electronics':
            # Split "3D Vision" back out of "Stereo Vision & Depth" (topic ids kept).
            stereo = next(c for c in chapters if c['id'] == 'el-stereo-vision-depth')
            n3d = len(extra[0]['topics'])
            moved = stereo['topics'][-n3d:]
            assert [t['name'] for t in moved] == [x[1] for x in extra[0]['topics']]
            stereo['topics'] = stereo['topics'][:-n3d]
            idx = chapters.index(stereo) + 1
            chapters.insert(idx, dict(id='el-3d-vision', name='3D Vision', category=stereo['category'], topics=moved))
            report.append('electronics: split "3D Vision" out of "Stereo Vision & Depth"')
            # De-duplicate the clashing id (second occurrence is the field/device one).
            dups = [c for c in chapters if c['id'] == 'el-configuration-management']
            dups[1]['id'] = 'el-device-configuration-management'
            for t in dups[1]['topics']:
                t['id'] = t['id'].replace('el-configuration-management', 'el-device-configuration-management', 1)
            report.append('electronics: second "Configuration Management" id -> el-device-configuration-management')

        doc = dict(id=sid, **SUBJECT_META[sid], description='', chapters=chapters)
        (OUT / f'{sid}.json').write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(f'{sid}: {len(chapters)} chapters')
    print('\n'.join(report))


if __name__ == '__main__':
    main()

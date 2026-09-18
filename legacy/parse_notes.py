#!/usr/bin/env python3
"""
parse_notes.py – Parses "L notes (2).md" and writes the complete
knowledge_base.json used by knowledge_map_v2.html.

File structure (two variants):
  Variant A  (Physics, Math, AI):
    # **Subject:**
    **1. MAJOR CATEGORY**
    **1.2 Chapter Name**
    * **Topic**
      * **Sub-topic**           <- appended to parent topic list

  Variant B  (Electronics / IoT):
    # **Electronics, IOT... :**
    **1. MAJOR CATEGORY**
    **Chapter Name**            <- un-numbered bold line (no N.M prefix)
    * Topic text                <- plain bullet (no ** around text)
"""

import re, json, textwrap

# ── helpers ──────────────────────────────────────────────────────────────────

def slug(text: str) -> str:
    """Turn a display name into a safe, lowercase id fragment."""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text[:60]

def strip_md_bold(text: str) -> str:
    """Remove surrounding ** / * and trailing backslash-escapes."""
    text = text.strip()
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'\\(.)', r'\1', text)   # unescape \. \- etc.
    return text.strip()

PRIORITY_KEYWORDS = {
    'core': ['fundamental', 'basic', 'introduc', 'overview', 'core',
             'essential', 'foundation'],
    'advanced': ['advanced', 'frontier', 'emerging', 'quantum', 'theoretical',
                 'specialized', 'niche', 'modern', 'cutting-edge'],
    'optional': ['history', 'philosophy', 'education', 'aesthetic',
                 'meta', 'community', 'resource', 'writing'],
}

def guess_priority(text: str) -> str:
    lower = text.lower()
    if any(k in lower for k in PRIORITY_KEYWORDS['optional']):
        return 'optional'
    if any(k in lower for k in PRIORITY_KEYWORDS['advanced']):
        return 'advanced'
    if any(k in lower for k in PRIORITY_KEYWORDS['core']):
        return 'core'
    return 'important'

# ── regexes ──────────────────────────────────────────────────────────────────

RE_SUBJECT   = re.compile(r'^#\s+\*\*(.+?)\*\*\s*:?\s*$')
RE_MAJOR_CAT = re.compile(r'^\*\*\d+[\\.]+\s+([A-Z][A-Z &,/\-()&]+)\*\*\s*$')
RE_CHAPTER_A = re.compile(r'^\*\*\d+[\\.]+\s*\d+\s+(.+?)\*\*\s*$')  # N.M Title
RE_CHAPTER_B = re.compile(r'^\*\*([A-Z][^*\n]{3,}?)\*\*\s*$')        # plain bold
RE_TOPIC     = re.compile(r'^[*-]\s+(.+)$')

# ── parser ────────────────────────────────────────────────────────────────────

def parse(filepath: str) -> dict:
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    subjects = []
    cur_subject   = None
    cur_category  = None   # string label for the category
    cur_chapter   = None   # dict
    cur_topic_depth = 0    # indentation of last bullet (spaces)

    def new_subject(name):
        nonlocal cur_subject, cur_category, cur_chapter
        # clean display name: remove trailing "Topics" / "topics" etc.
        display_name = re.sub(r'\s*(topics?|:)\s*$', '', name, flags=re.IGNORECASE).strip()
        # shorten AI subject name
        if 'machine learning' in display_name.lower():
            display_name = 'AI, Machine Learning & Robotics'
        if 'electronics' in display_name.lower():
            display_name = 'Electronics & IoT'
        # use clean short ID if known, otherwise slug the full name
        lower = name.lower()
        clean_id = next(
            (v for k, v in SUBJECT_ID_MAP.items() if k in lower),
            slug(name)
        )
        obj = {
            'id':       clean_id,
            'name':     display_name,
            'icon':     subject_icon(name),
            'color':    subject_color(name),
            'chapters': []
        }
        subjects.append(obj)
        cur_subject  = obj
        cur_category = None
        cur_chapter  = None

    def new_chapter(title, category):
        nonlocal cur_chapter
        base = slug(title)
        prefix = (cur_subject['id'][:2] + '-') if cur_subject else ''
        ch = {
            'id':           prefix + base,
            'name':         title,
            'category':     category or 'General',
            'priority':     guess_priority(title),
            'prerequisites': [],
            'topics':       []
        }
        if cur_subject is not None:
            cur_subject['chapters'].append(ch)
        cur_chapter = ch

    def add_topic(text, sub=False):
        if cur_chapter is None:
            return
        idx = len(cur_chapter['topics']) + 1
        prefix = cur_chapter['id']
        topic_id = f"{prefix}-{idx}"
        cur_chapter['topics'].append({
            'id':       topic_id,
            'name':     text,
            'priority': guess_priority(text)
        })

    # detect whether we are in variant-B (Electronics) subject
    variant_b_active = False

    for raw_line in lines:
        line = raw_line.rstrip('\n')

        # ── subject header ────────────────────────────────────────────────
        m = RE_SUBJECT.match(line)
        if m:
            name = strip_md_bold(m.group(1))
            # clean trailing colon / asterisks
            name = re.sub(r'[:\*]+$', '', name).strip()
            new_subject(name)
            # Electronics section uses variant-B chapter style
            variant_b_active = 'electronic' in name.lower() or 'iot' in name.lower()
            continue

        if cur_subject is None:
            continue

        # ── major category  **N\. UPPER CASE** ───────────────────────────
        m = RE_MAJOR_CAT.match(line)
        if m:
            cur_category = strip_md_bold(m.group(1))
            cur_chapter  = None   # reset chapter on new category
            continue

        # ── chapter: N.M Title  (variant A) ──────────────────────────────
        if not variant_b_active:
            m = RE_CHAPTER_A.match(line)
            if m:
                title = strip_md_bold(m.group(1))
                new_chapter(title, cur_category)
                continue

        # ── chapter: plain bold  (variant B) ─────────────────────────────
        if variant_b_active:
            m = RE_CHAPTER_B.match(line)
            if m:
                title = strip_md_bold(m.group(1))
                # ignore pure-separator lines (e.g. "---")
                if title and len(title) > 3:
                    new_chapter(title, cur_category)
                continue

        # ── topic bullet ──────────────────────────────────────────────────
        m = RE_TOPIC.match(line)
        if m:
            raw_text = m.group(1)
            text = strip_md_bold(raw_text)
            if not text:
                continue
            # detect indentation to distinguish sub-bullets
            leading = len(raw_line) - len(raw_line.lstrip(' '))
            add_topic(text, sub=(leading > 2))
            continue

    # ── build learning paths ──────────────────────────────────────────────────
    learning_paths = build_learning_paths(subjects)

    return {
        'version':       '3.0.0',
        'lastUpdated':   '2026-02-22',
        'subjects':      subjects,
        'learningPaths': learning_paths
    }


def build_learning_paths(subjects: list) -> dict:
    paths = {}
    for subj in subjects:
        sid = subj['id']
        # first 5 chapters as a starter path
        seq = [ch['id'] for ch in subj['chapters'][:5]]
        paths[sid + '-intro'] = {
            'name':        subj['name'] + ' – Introduction',
            'description': 'First steps into ' + subj['name'],
            'sequence':    seq
        }
    return paths


def subject_icon(name: str) -> str:
    name = name.lower()
    if 'physics' in name:   return '⚛'
    if 'math'    in name:   return '∑'
    if 'ai'      in name or 'machine' in name: return '🤖'
    if 'electron' in name or 'iot' in name:    return '🔌'
    return '📚'


def subject_color(name: str) -> str:
    name = name.lower()
    if 'physics' in name:   return '#60c5f8'
    if 'math'    in name:   return '#fbbf24'
    if 'ai'      in name or 'machine' in name: return '#a78bfa'
    if 'electron' in name or 'iot' in name:    return '#10b981'
    return '#94a3b8'


# Clean short IDs for known subjects
SUBJECT_ID_MAP = {
    'physics':     'physics',
    'math':        'math',
    'ai':          'ai',
    'machine':     'ai',
    'electron':    'electronics',
    'iot':         'electronics',
}


# ── main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import os, sys

    md_path   = r'L notes (2).md'
    json_path = r'knowledge_base.json'
    js_path   = r'knowledge_base.js'

    print(f'Parsing {md_path} …')
    data = parse(md_path)

    total_topics   = sum(len(ch['topics'])   for s in data['subjects'] for ch in s['chapters'])
    total_chapters = sum(len(s['chapters'])  for s in data['subjects'])
    print(f'  Subjects  : {len(data["subjects"])}')
    print(f'  Chapters  : {total_chapters}')
    print(f'  Topics    : {total_topics}')

    # Write JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'Written → {json_path}')

    # Write JS (works via file:// without CORS issues)
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    js_content = f'// Auto-generated by parse_notes.py – do not edit manually\n// Re-run: python parse_notes.py\nvar knowledgeBaseData = {json_str};\n'
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f'Written → {js_path}')

#!/usr/bin/env python3
"""
update_html.py – Patches knowledge_map_v2.html so it:
  1. Loads knowledge_base.js (the full parsed data) via a <script> tag
  2. Replaces the former embedded knowledgeBase literal with a one-liner
     that just picks up the variable exposed by knowledge_base.js
"""

import re, pathlib, shutil

HTML = pathlib.Path(r'knowledge_map_v2.html')
BACKUP = HTML.with_suffix('.html.bak')

# ── back up original ──────────────────────────────────────────────────────────
shutil.copy(HTML, BACKUP)
print(f'Backup → {BACKUP}')

src = HTML.read_text(encoding='utf-8')

# ── 1. inject <script src="knowledge_base.js"> into <head> ───────────────────
INJECT_AFTER = '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>'
INJECT_TAG   = '<script src="knowledge_base.js"></script>'

if INJECT_TAG not in src:
    src = src.replace(
        INJECT_AFTER,
        INJECT_AFTER + '\n' + INJECT_TAG
    )
    print('Injected <script src="knowledge_base.js"> into <head>')
else:
    print('<script> tag already present – skipping')

# ── 2. remove the embedded knowledgeBase literal ─────────────────────────────
# The block starts with the comment line just before `let knowledgeBase = {`
# and ends with the `};` that precedes `let userProgress`.

EMBED_START_MARKER = '// Embedded knowledge base data'
EMBED_END_MARKER   = '\nlet userProgress = {'

start = src.find(EMBED_START_MARKER)
end   = src.find(EMBED_END_MARKER, start)

if start == -1:
    print('ERROR: could not find embedded data start marker!')
    exit(1)
if end == -1:
    print('ERROR: could not find end marker (let userProgress)!')
    exit(1)

# The replacement: a short comment + one-liner assignment
REPLACEMENT = (
    '// Knowledge base loaded from knowledge_base.js\n'
    'let knowledgeBase = (typeof knowledgeBaseData !== "undefined")\n'
    '  ? knowledgeBaseData\n'
    '  : { version: "error", subjects: [], learningPaths: {} };\n'
)

src = src[:start] + REPLACEMENT + src[end:]
print(f'Replaced embedded data block ({end - start:,} chars → {len(REPLACEMENT)} chars)')

# ── 3. write patched HTML ─────────────────────────────────────────────────────
HTML.write_text(src, encoding='utf-8')
print(f'Written → {HTML}')
print('Done.')

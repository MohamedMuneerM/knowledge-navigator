# Knowledge Navigator

A personal map of STEM: **11 disciplines, 1,432 chapters and 14,439 topics**, each with a
level and the chapters you need first. There are also **13 goal roadmaps** (Cosmos, Rocket
Science, Robotics, Iron Man…) that turn it all into a learning order.

## Use it

Double-click **`index.html`**. No server or install is needed (only the font loads from the internet).

| View | What it's for |
|---|---|
| **Home** | Chapters you're learning, what's unlocked next, all roadmaps and disciplines |
| **Roadmaps** | A goal ("Rocket Science & Spaceflight") as staged steps, with why each chapter matters and a *Next up* marker |
| **Disciplines** | Every chapter of a field, as *Learning order* (stages) or *By category*. Filter by priority and status |
| **Path finder** | Pick any chapter and see everything you need before it, across all disciplines, in order |
| **Chapter panel** | Prerequisites, what it unlocks, related chapters elsewhere, the topic checklist, notes and links |

- Progress, notes and links are saved in the browser (`localStorage`). Use **Data → Export
  progress** now and then as a backup, and **Import** to restore it or move it to another machine.
- `knowledge_map_v2.html` is the older tracker. It still works on the same data and shares the
  same saved progress.

From the command line:

```bash
python scripts/path.py ae-liquid-rocket-engines   # ordered path to a chapter
python scripts/path.py --find "black hole"         # find chapter ids
```

## How it's organised

```
data/
  disciplines/<id>.json   the source of truth: chapters, topics, levels, prerequisites
  roadmaps/<id>.json      goal roadmaps
  manifest.json           discipline and roadmap order
  SCHEMA.md               field-by-field format and the rules for prerequisites
scripts/
  build.py                validates data/ and generates knowledge_base.js/.json
  path.py                 prerequisite path finder (CLI)
  migrate_v3.py           one-off import from the original notes (history)
docs/
  AUDIT.md                what was checked, what was wrong, what was added
  audit/<id>.md           per-discipline coverage reports with sources
index.html                the dashboard
knowledge_base.js/.json   generated; don't edit by hand
legacy/                   the original notes, old parser and old HTML
```

## Editing

1. Edit a file in `data/` (see `data/SCHEMA.md`). New topics can leave out `id`; the build
   fills one in.
2. Run `python scripts/build.py`. It refuses errors (unknown ids, prerequisite cycles) and
   warns about redundant prerequisites and incomplete roadmaps.
3. Reload `index.html`.

**Never rename or delete a chapter or topic id.** Saved progress is keyed on them.

## Levels and priorities

| Level | Meaning |
|---|---|
| 1 | Foundations: start here with high-school basics |
| 2 | Core: first two years of a degree |
| 3 | Advanced undergraduate |
| 4 | Graduate / specialist |
| 5 | Frontier / research |

Priority is relative to the discipline: **core** (must learn), **important** (complete
coverage), **advanced** (specialisation), **optional** (history, tools, community).

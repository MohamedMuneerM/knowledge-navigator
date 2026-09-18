# Contributing to Knowledge Navigator

Thanks for helping. The goal is simple: **a learner should be able to follow this map and know
they haven't missed anything, in an order that always makes sense.** Every fix makes that more
true for everyone.

You don't need to be a programmer. Pick the path that suits you.

| I want to… | Easiest way |
|---|---|
| Point out a missing topic, a wrong prerequisite, a bad level | [Open an issue](../../issues/new/choose): a short form, no git needed |
| Fix one chapter myself | Open the chapter in the app → **✎ Edit on GitHub**. GitHub makes the fork and pull request for you |
| Add chapters, a discipline or a roadmap | Clone the repo, edit `data/`, run the build, open a pull request |
| Improve the app | Edit `index.html` (plain HTML/CSS/JS, no framework, no build step) |

## How the data is organised

```
data/
  manifest.json                     order of disciplines and roadmaps
  disciplines/<discipline>/
    discipline.json                 name, colour, prefix, ordered list of categories
    <chapter-id>.json               one file per chapter
  roadmaps/<roadmap-id>.json        goal roadmaps
  redirects.json                    old id -> new id, when an id ever has to change
```

The full field reference is in [`data/SCHEMA.md`](data/SCHEMA.md). A chapter file looks like this:

```json
{
  "id": "ph-waves-oscillations",
  "name": "Waves & Oscillations",
  "category": "Mechanics, Waves & Fluids",
  "level": 2,
  "priority": "core",
  "summary": "The mathematics and physics of vibrations and waves.",
  "prerequisites": ["ph-classical-mechanics"],
  "related": ["ph-acoustics"],
  "topics": [
    { "id": "ph-waves-oscillations-1", "name": "Simple harmonic oscillator" },
    { "name": "A new topic: leave out the id, the build adds one" }
  ]
}
```

## Working locally

You need Python 3.9 or newer. Nothing else.

```bash
git clone https://github.com/MohamedMuneerM/knowledge-navigator.git
cd knowledge-navigator
python scripts/build.py          # validate data/, add missing topic ids, generate the site data
# open index.html in your browser
```

Before you open a pull request:

```bash
python scripts/build.py --strict  # errors and warnings must both be zero
python scripts/check_ids.py       # no id may disappear (compares with origin/main)
```

CI runs the same two commands on every pull request.

## The rules that keep the map trustworthy

1. **Ids are forever.** People's saved progress is keyed on chapter and topic ids. Never delete
   or rename one. If you really must, for example after a merge, add the old id to
   `data/redirects.json` and the app will move saved progress across.
2. **Prerequisites are direct, hard and minimal.** List only what you genuinely need *before
   starting* the chapter, and nothing already implied by another prerequisite. The build flags
   redundant ones.
3. **Never point up.** A prerequisite must not have a higher level than the chapter.
4. **No cycles.** The build rejects them.
5. **Chapter ≈ one university course** (about 15–60 hours). Topics are its syllabus, in teaching
   order. Use `sub` for one level of breakdown, never deeper.
6. **Use `related` for overlap.** If two disciplines cover the same ground (e.g. maths and
   physics both teach Lagrangian mechanics), keep both and link them. Don't merge them.
7. **Roadmaps must be complete.** Followed top to bottom, a roadmap never reaches a chapter whose
   prerequisites haven't come earlier. The build checks this.

### Levels and priorities

| Level | Meaning |
|---|---|
| 1 | Foundations: high-school background is enough |
| 2 | Core: first two years of a university degree |
| 3 | Advanced undergraduate |
| 4 | Graduate / specialist |
| 5 | Frontier: research-level or emerging |

Priority is relative to the discipline: `core` (everyone must learn it), `important` (complete
coverage), `advanced` (a specialisation), `optional` (history, tools, community).

## Common tasks

**Add a topic.** Append `{ "name": "…" }` to the chapter's `topics`. The build assigns the id.

**Add a chapter.** Create `data/disciplines/<discipline>/<prefix>-<kebab-name>.json`. The id must
equal the file name and start with the discipline's prefix (`ma`, `ph`, `ch`, `bi`, `ea`, `cs`,
`el`, `ai`, `me`, `mt`, `ae`). Use a category that already exists in that discipline's
`discipline.json`, or add a new one there. Then run the build and fix what it reports.

**Add a roadmap.** Create `data/roadmaps/<id>.json` (copy an existing one) and add the id to
`data/manifest.json`. `python scripts/path.py <chapter-id>` prints the full prerequisite path
to any chapter, which is the fastest way to build a complete roadmap.

**Add a discipline.** Create `data/disciplines/<id>/discipline.json` with a unique two-letter
`prefix`, add the id to `data/manifest.json`, then add chapters. Please open an issue first so
the scope and its overlap with existing disciplines can be agreed.

## Quality bar for content

- Prefer established curricula as evidence: university course lists, professional-body
  guidelines, standard textbook tables of contents. Mention your sources in the pull request.
- Topics should be concrete and learnable ("Gauss's law and its applications"), not vague
  ("Other topics").
- Keep summaries to one plain sentence.
- **AI-assisted contributions are welcome**, but a human must check every line. Say in the pull
  request that AI helped. Unchecked bulk dumps will be closed.

## Pull requests

- One logical change per pull request (e.g. "add superconducting circuits chapter", not a mix of
  ten unrelated edits).
- CI must pass. A maintainer reviews the content, and may ask for sources.
- By contributing you agree to license data under CC BY-SA 4.0 and code under MIT
  (see [LICENSE-DATA.md](LICENSE-DATA.md) and [LICENSE](LICENSE)).

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

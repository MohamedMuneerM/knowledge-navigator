# Contributing to Knowledge Navigator

Thanks for helping. The aim is that a learner can follow this map, trust that nothing important is
missing, and always meet chapters in an order that makes sense. Every fix gets it closer to that.

You don't need to be a programmer. Pick whichever way suits you:

| I want to… | Easiest way |
|---|---|
| Point out a missing topic, a wrong prerequisite or a wrong level | [Open an issue](../../issues/new/choose). It's a short form and needs no git. |
| Fix one chapter myself | Open the chapter in the app and click **Edit on GitHub**. GitHub creates the fork and the pull request for you. |
| Add chapters, a discipline or a roadmap | Clone the repo, edit `data/`, run the build and open a pull request. |
| Improve the app | Edit `index.html`. It's plain HTML, CSS and JavaScript with no framework and no build step. |

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

[`data/SCHEMA.md`](data/SCHEMA.md) describes every field. A chapter file looks like this:

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

You need Python 3.9 or newer, and nothing else.

```bash
git clone https://github.com/MohamedMuneerM/knowledge-navigator.git
cd knowledge-navigator
python scripts/build.py          # validate data/, add missing topic ids, generate the site data
# open index.html in your browser
```

Before you open a pull request, run:

```bash
python scripts/build.py --strict  # errors and warnings must both be zero
python scripts/check_ids.py       # no id may disappear (compares with origin/main)
```

If you changed `index.html`, also run the browser test. It checks desktop and phone layouts and the
main interactions:

```bash
pip install playwright && python -m playwright install chromium   # once
python scripts/ui_test.py
```

CI runs all three on every pull request.

## Rules that keep the map trustworthy

1. Ids never change. Saved progress is stored against chapter and topic ids, so don't delete or
   rename one. If you have to (after merging two chapters, say), add the old id to
   `data/redirects.json` and the app will move people's progress to the new one.
2. Prerequisites are direct, hard and minimal. List only what you need *before starting* the
   chapter, and leave out anything another prerequisite already implies. The build flags redundant
   ones.
3. A prerequisite can't have a higher level than the chapter that needs it.
4. There can be no cycles. The build rejects them.
5. A chapter is roughly one university course, about 15 to 60 hours of study. Its topics are the
   syllabus, in teaching order. Use `sub` for one level of breakdown and never go deeper.
6. When two disciplines cover the same ground (maths and physics both teach Lagrangian mechanics,
   for example), keep both chapters and link them with `related` instead of merging them.
7. Roadmaps must be complete. Read from top to bottom, a roadmap never reaches a chapter whose
   prerequisites haven't already appeared. The build checks this.

### Levels and priorities

| Level | Meaning |
|---|---|
| 1 | Foundations: high-school background is enough |
| 2 | Core: first two years of a university degree |
| 3 | Advanced undergraduate |
| 4 | Graduate / specialist |
| 5 | Frontier: research-level or emerging |

Priority is relative to the discipline: `core` means everyone must learn it, `important` is needed
for complete coverage, `advanced` is a specialisation, and `optional` covers history, tools and
community.

## Common tasks

To add a topic, append `{ "name": "…" }` to the chapter's `topics`. The build assigns the id.

To add a chapter, create `data/disciplines/<discipline>/<prefix>-<kebab-name>.json`. The id must
match the file name and start with the discipline's prefix (`ma`, `ph`, `ch`, `bi`, `ea`, `cs`,
`el`, `ai`, `me`, `mt`, `ae`). Use a category that already exists in that discipline's
`discipline.json`, or add a new one there. Then run the build and fix whatever it reports.

To add a roadmap, copy an existing file in `data/roadmaps/`, give it a new id and add that id to
`data/manifest.json`. `python scripts/path.py <chapter-id>` prints the full prerequisite path to any
chapter, which is the quickest way to make a roadmap complete.

To add a discipline, create `data/disciplines/<id>/discipline.json` with an unused two-letter
`prefix`, add the id to `data/manifest.json`, then add chapters. Please open an issue first, so we
can agree on the scope and how it overlaps with existing disciplines.

## What good content looks like

- Back changes with established curricula: university course lists, professional-body guidelines,
  or the tables of contents of standard textbooks. Mention your sources in the pull request.
- Make topics concrete and learnable ("Gauss's law and its applications"), not vague ("Other
  topics").
- Keep each summary to one plain sentence.
- AI-assisted contributions are welcome, but a person has to check every line. Say in the pull
  request that AI helped. Unchecked bulk dumps will be closed.

## Pull requests

- Keep each pull request to one change, such as "add superconducting circuits chapter" rather than
  ten unrelated edits.
- CI must pass. A maintainer reviews the content and may ask for sources.
- By contributing, you agree to license data under CC BY-SA 4.0 and code under MIT (see
  [LICENSE-DATA.md](LICENSE-DATA.md) and [LICENSE](LICENSE)).

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

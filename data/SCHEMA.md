# Data schema

Everything the app shows is generated from the JSON files in this folder. Edit them, then run
`python scripts/build.py` to validate and regenerate `knowledge_base.js` / `knowledge_base.json`.

```
data/
  manifest.json                        version, discipline order, roadmap order
  disciplines/<discipline>/
    discipline.json                    discipline metadata + ordered categories
    <chapter-id>.json                  one file per chapter (file name = chapter id)
  roadmaps/<roadmap-id>.json           one file per goal roadmap
  redirects.json                       renamed ids -> their replacements
```

## discipline.json

```jsonc
{
  "id": "physics",                     // same as the folder name
  "name": "Physics",
  "icon": "⚛️",
  "color": "#60c5f8",
  "prefix": "ph",                      // every chapter id starts with "<prefix>-"
  "description": "One or two sentences on what the discipline covers.",
  "categories": [                      // display order, foundational -> advanced/applied
    "Foundations & Introductory Physics",
    "Mechanics, Waves & Fluids"
  ]
}
```

## Chapter file: `disciplines/<discipline>/<chapter-id>.json`

```jsonc
{
  "id": "ph-classical-mechanics",      // = file name; stable forever (progress is keyed on it)
  "name": "Classical Mechanics",
  "category": "Mechanics, Waves & Fluids",   // must be listed in discipline.json
  "level": 2,                          // 1-5, see below
  "priority": "core",                  // core | important | advanced | optional
  "summary": "One sentence: what this chapter is about and why it matters.",
  "prerequisites": ["ma-multivariable-calculus", "ph-introductory-mechanics"],
  "related": ["ma-classical-mechanics"],
  "topics": [
    { "id": "ph-classical-mechanics-1", "name": "Kinematics",
      "sub": [ { "id": "ph-classical-mechanics-1-1", "name": "Projectile motion" } ] },
    { "name": "A new topic without an id" }   // build.py assigns ph-classical-mechanics-<n>
  ]
}
```

Within each category, chapters are shown in teaching order, which the build works out from the
prerequisite graph. There's no manual ordering to maintain.

### Levels

| level | meaning | typical learner |
|---|---|---|
| 1 | Foundations | high school / first contact |
| 2 | Core | first two years of a university degree |
| 3 | Advanced undergraduate | final years of a degree |
| 4 | Graduate / specialist | master's, PhD coursework, professional specialty |
| 5 | Frontier | research-level, emerging, or highly niche |

### Priority (within the discipline)

- `core`: everyone serious about the discipline must learn it.
- `important`: needed for complete, well-rounded coverage.
- `advanced`: a specialisation.
- `optional`: peripheral material such as history, philosophy, tool catalogues, communities and business.

### Prerequisites

- List only direct, hard prerequisites: what you need before starting. Leave out anything another
  prerequisite already implies. The build warns about redundant ones.
- Prerequisites may come from any discipline, and must not have a higher `level` than the chapter.
- Cycles aren't allowed, and the build rejects them.
- `related` means "the same subject seen from another angle". It doesn't imply order.

### Ids

- Chapter ids look like `<prefix>-<kebab-case-name>` and use only lowercase letters, digits and
  hyphens.
- Topic ids are optional when you add a topic. The build fills in `<chapterId>-<n>` (for sub-topics,
  `<topicId>-<n>`) and writes it back.
- Never delete or rename an id. If one has to change, add `"old-id": "new-id"` to
  `redirects.json` (under `chapters` or `topics`). The app moves saved progress across, and
  `scripts/check_ids.py` checks that every id that ever existed is still reachable.

## Roadmap file: `roadmaps/<roadmap-id>.json`

```jsonc
{
  "id": "rocket-science",
  "name": "Rocket Science & Spaceflight",
  "icon": "🚀",
  "tagline": "Design, fly and understand rockets and spacecraft.",
  "description": "Who this is for and what the journey looks like.",
  "outcomes": ["Size a launch vehicle with the rocket equation"],
  "stages": [
    {
      "name": "Mathematical foundations",
      "description": "Why this stage exists.",
      "items": [
        { "chapter": "ma-calculus", "why": "Everything in flight mechanics is rates of change.", "depth": "full" },
        { "chapter": "ph-thermodynamics-statistical-mechanics", "depth": "selected",
          "focus": ["ph-thermodynamics-statistical-mechanics-1"], "why": "…" }
      ]
    }
  ],
  "related": ["cosmos"]
}
```

- `depth`: `full` (study the whole chapter) or `selected` (only the topics in `focus`).
- Every item's prerequisites must appear earlier in the roadmap. The build warns when they don't.
  `python scripts/path.py <chapter-id>` prints the full, ordered prerequisite path to any chapter.
- Electives go in the last stage, with `why` starting "Elective:".

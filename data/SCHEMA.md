# Data schema

Everything the dashboard shows is generated from the JSON files in this folder.
Edit these, then run `python scripts/build.py` to validate and regenerate
`knowledge_base.js` / `knowledge_base.json`.

```
data/
  manifest.json            discipline order + roadmap file list
  disciplines/<id>.json    one file per discipline (chapters + topics)
  roadmaps/<id>.json       one file per goal roadmap ("I want to learn X / become Y")
```

## Discipline file

```jsonc
{
  "id": "physics",                 // short, lowercase
  "name": "Physics",
  "icon": "⚛️",
  "color": "#60c5f8",
  "prefix": "ph",                  // every chapter id starts with "<prefix>-"
  "description": "One or two sentences on what the discipline covers.",
  "chapters": [
    {
      "id": "ph-classical-mechanics",      // stable forever; progress is keyed on it
      "name": "Classical Mechanics",
      "category": "Classical Physics",     // grouping inside the discipline
      "level": 2,                          // 1-5, see below
      "priority": "core",                  // core | important | advanced | optional
      "summary": "One sentence: what this chapter is about and why it matters.",
      "prerequisites": ["ma-calculus", "ph-kinematics"],   // DIRECT hard prerequisites, any discipline
      "related": ["ma-classical-mechanics"],               // optional: overlapping chapters elsewhere
      "topics": [
        { "id": "ph-classical-mechanics-1", "name": "Kinematics",
          "sub": [ { "id": "ph-classical-mechanics-1-1", "name": "Projectile motion" } ] },
        { "name": "A new topic without an id" }            // build.py assigns an id
      ]
    }
  ]
}
```

### Levels

| level | meaning | typical learner |
|---|---|---|
| 1 | Foundations | high school / first contact, no university background |
| 2 | Core | first two years of a university degree |
| 3 | Advanced undergraduate | final years of a degree |
| 4 | Graduate / specialist | master's, PhD coursework, professional specialty |
| 5 | Frontier | research-level, emerging, or highly niche |

### Priority (within the discipline)

- **core**: everyone serious about the discipline must learn it.
- **important**: part of a complete, well-rounded coverage.
- **advanced**: a specialisation. Learn it if you go deep in that direction.
- **optional**: peripheral: history, philosophy, tooling catalogues, communities, business.

### Prerequisites

- List only **direct, hard** prerequisites: what you genuinely need before you can start
  the chapter. Don't list something that is already implied by another listed prerequisite
  (if B needs A, and C needs B, C lists only B).
- Cross-discipline prerequisites are encouraged (physics → maths, robotics → control theory).
- A chapter's prerequisites must never lead back to itself (no cycles); build.py rejects cycles.
- `related` is for "same subject seen from another discipline"; it doesn't imply order.

### Ids

- Chapter ids: `<prefix>-<kebab-slug-of-name>`, globally unique, **never renamed or deleted**
  once published (browser progress is stored against them).
- Topic ids: optional when adding. build.py fills in `<chapterId>-<n>` and writes it back.

## Roadmap file

```jsonc
{
  "id": "rocket-science",
  "name": "Rocket Science & Spaceflight",
  "icon": "🚀",
  "tagline": "Design, fly and understand rockets and spacecraft.",
  "description": "Who this is for and what you'll be able to do at the end.",
  "outcomes": ["Size a launch vehicle with the rocket equation", "..."],
  "stages": [
    {
      "name": "Mathematical foundations",
      "description": "Why this stage exists.",
      "items": [
        { "chapter": "ma-calculus", "why": "Everything in flight mechanics is rates of change.", "depth": "full" },
        { "chapter": "ph-thermodynamics-statistical-mechanics", "depth": "selected",
          "focus": ["ph-thermodynamics-statistical-mechanics-1"], "why": "..." }
      ]
    }
  ],
  "related": ["cosmos"]
}
```

- `depth`: `full` (study the whole chapter) or `selected` (only the topics listed in `focus`,
  or the parts relevant to the roadmap if `focus` is omitted).
- build.py warns when a chapter in a roadmap has a prerequisite that neither appears in an
  earlier stage nor is already covered transitively. A clean roadmap has zero warnings, so
  following it top to bottom never hits a missing prerequisite.

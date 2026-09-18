# Knowledge Navigator

An open map of STEM that tells you what to learn, and in what order.

Pick a goal, such as understanding the cosmos, building rockets or becoming a robotics engineer, or
pick any single topic. Knowledge Navigator shows everything you need to learn first, across maths,
physics, chemistry, biology, computer science and engineering, in an order where each step builds on
the ones before it.

**[Open the app](https://mohamedmuneerm.github.io/knowledge-navigator/)**. It's free, there's no
sign-up, and your progress stays in your browser.

![Rocket Science roadmap](docs/images/roadmap.png)

## What's inside

11 disciplines, 1,432 chapters, 14,439 topics, 2,430 prerequisite links and 13 roadmaps.

The disciplines are Mathematics, Physics, Chemistry, Biology, Earth & Environmental Science,
Computer Science, Electrical & Electronics Engineering, AI, Machine Learning & Robotics, Mechanical
Engineering, Materials Science & Engineering, and Aerospace Engineering.

The roadmaps are Cosmos & Space Science, Rocket Science & Spaceflight, Astrobiology, Robotics
Engineer, Iron Man: Build a Powered Exosuit, Electrical & Electronics Engineer, Embedded & IoT
Engineer, Computer Engineer, Software Engineer, AI / ML Engineer, Data Scientist, Quantum Computing,
and Theoretical Physicist.

Each chapter has a level from 1 (high-school background is enough) to 5 (research frontier), a
topic checklist that reads like a university course syllabus, and its direct prerequisites. Those
prerequisites can come from other disciplines: rocket engines need heat transfer, heat transfer
needs thermodynamics, and thermodynamics needs calculus.

## Features

- Roadmaps turn a goal into a staged route. Every chapter comes with one line on why it matters,
  and a *Next up* marker shows where you are. The build checks that no roadmap asks for a chapter
  before its prerequisites.
- The path finder takes any chapter and lists everything you need to learn before it, in order.
- Each discipline can be read in learning order, as stages worked out from the prerequisite
  graph, or browsed by category.
- You can track progress and keep notes and links for each chapter. Everything is saved in your
  browser, and you can export and import it as JSON.
- It works offline. The app is one HTML file and one data file, with no framework and no server.

![Path finder](docs/images/path.png)

## Where the content comes from

The map started as one person's study notes. Each discipline was then checked against its standard
classification and against real curricula: MSC2020 for maths, APS PhySH for physics, ACM/IEEE CS2023
for computer science, the ACS and RSC guidelines for chemistry, the ABET and NCEES specifications for
engineering, the NASA Technology Taxonomy, and course lists from MIT, Cambridge, Stanford and others.
Gaps found that way were filled. The curation was done with heavy AI assistance. Every discipline has
an audit report that lists its sources and decisions: see [`docs/AUDIT.md`](docs/AUDIT.md) and
[`docs/audit/`](docs/audit/).

The aim is to cover what a strong degree plus graduate coursework covers. It doesn't try to list
every niche research topic, and levels and prerequisites are judgement calls. If you know a field
well, reviewing it is the most useful thing you can contribute.

## Contributing

You don't need to write code to help:

- In the app, open a chapter and click **Report a problem** or **Edit on GitHub**.
- [Suggest a chapter or topic](../../issues/new?template=suggest-content.yml), or
  [propose a roadmap](../../issues/new?template=roadmap-idea.yml).
- For larger changes, read [CONTRIBUTING.md](CONTRIBUTING.md). The data is plain JSON with one file
  per chapter, and Python is the only tool you need.

```bash
git clone https://github.com/MohamedMuneerM/knowledge-navigator.git
cd knowledge-navigator
python scripts/build.py            # validate + generate the app's data file
# then open index.html in a browser

python scripts/path.py ae-liquid-rocket-engines   # print the path to any chapter
```

## Using the data

The whole map is published as JSON at
`https://mohamedmuneerm.github.io/knowledge-navigator/knowledge_base.json`, so you can build your
own tools on it. The source files are in [`data/`](data/), and [`data/SCHEMA.md`](data/SCHEMA.md)
describes the format.

## Ideas for what's next

- Free learning resources (courses, books, videos) for every chapter. This is the biggest gap.
- More disciplines: civil, chemical and biomedical engineering, and statistics.
- More roadmaps. Open an issue with yours.
- An interactive view of the prerequisite graph.
- Translations.

## Licence

The code (`index.html`, `scripts/`, `.github/`) is under the [MIT licence](LICENSE). The content
(`data/`, `docs/`) is under [CC BY-SA 4.0](LICENSE-DATA.md): you can share and adapt it freely as
long as you give credit and keep your version open under the same licence.

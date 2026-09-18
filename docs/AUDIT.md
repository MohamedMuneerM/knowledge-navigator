# Knowledge base audit, September 2026

This audit asks two questions. If someone works through a discipline chapter by chapter, will they
have covered the whole field? And is everything grouped and ordered correctly?

Before the audit, the answer to both was no. Now each discipline covers what a full university
curriculum covers, plus the main research areas. Each one was checked against its standard
classification and against real degree programmes, the gaps were filled, and every chapter now
lists what has to be learned before it. The detailed evidence is in [`docs/audit/`](audit/), one
report per discipline.

## Problems in the original data

The original notes were fine. These problems came from the old import script, `parse_notes.py`,
which is preserved together with the notes in the `legacy-v2` git tag.

| Problem | Effect | Fix |
|---|---|---|
| Indented bullets were never parsed | 497 sub-topics in the notes never reached the dashboard | Restored as nested sub-topics |
| Category headings containing `\-`, "IoT", "FPGAs" or "APIs" were skipped | 60 chapters sat under the wrong category, e.g. 28 protocol, wireless and IoT-cloud chapters under "Sensors" and 7 FPGA chapters under "Operating Systems" | Regrouped |
| An unnumbered heading ("3D Vision") was merged into the chapter before it | One chapter was hidden inside another | Split out |
| Two different chapters shared the id `el-configuration-management` | Ticking one ticked the other | The second became `el-device-configuration-management` |
| Priorities were guessed from keywords ("quantum" meant advanced, "history" meant optional) | "Quantum Mechanics" was marked advanced | Every chapter was re-rated by hand |
| There were no prerequisites, and each "learning path" was just the first five chapters of a subject | No learning order | 2,430 prerequisite links, 332 of them across disciplines |

Apart from the duplicate above, no chapter or topic id was deleted or renamed, so progress saved
in a browser still matches.

## Coverage before and after

| Discipline | Checked against | Before | Now |
|---|---|---|---|
| Mathematics | MSC2020 (all 63 classes), Cambridge Tripos, MIT 18, MAA CUPM | 186 chapters, 666 topics, no on-ramp, 114 stub chapters | 218 chapters, 1,737 topics, from arithmetic to research level |
| Physics | APS PhySH, arXiv, MIT 8, Cambridge NST | 58 chapters, 501 topics, no on-ramp, thin astronomy | 101 chapters, 1,118 topics, including a 25-chapter astronomy track |
| Chemistry | ACS guidelines, RSC/QAA, IUPAC, MIT 5, Cambridge | Didn't exist | 102 chapters, 1,091 topics |
| Biology | Vision & Change, Campbell, Alberts, MIT 7, Cambridge | Didn't exist | 100 chapters, 1,104 topics |
| Earth & Environmental Science | AGU sections, Earth Science Literacy Principles, NSF GEO, MIT 12 | Didn't exist | 83 chapters, 854 topics |
| Computer Science | ACM/IEEE CS2023 (all 17 areas), ACM CCS, MIT, Stanford, OSSU | Didn't exist (fragments in AI and electronics) | 84 chapters, 1,026 topics |
| Electrical & Electronics Eng. | NCEES FE, ABET, MIT 6-5, Imperial | 300 chapters, 1,848 topics; strong on embedded and IoT, but no power systems, machines, RF, communications or VLSI | 354 chapters, 2,615 topics |
| AI, ML & Robotics | ACM CCS, AIMA, Stanford CS229/224N/231N/234, *Modern Robotics* | 89 chapters, 1,057 topics, about 70% coverage | 121 chapters, 1,666 topics |
| Mechanical Engineering | ABET, NCEES FE and three PE exams, ASME, MIT 2 | Didn't exist | 75 chapters, 928 topics |
| Materials Science & Eng. | ABET, MIT 3, Callister, Ashby, TMS/MRS | Didn't exist | 83 chapters, 1,011 topics |
| Aerospace Engineering | ABET, MIT 16, NASA Technology Taxonomy, Sutton, Curtis, SMAD | Didn't exist | 111 chapters, 1,289 topics |
| Total | | 4 disciplines, 632 chapters, about 3,575 topics | 11 disciplines, 1,432 chapters, 14,439 topics |

## How the learning order works

Every chapter has a level (1 Foundations, 2 Core, 3 Advanced undergraduate, 4 Graduate,
5 Frontier) and a priority within its discipline (core, important, advanced or optional).

Every chapter also lists its direct prerequisites, which can come from any discipline. *Liquid
Rocket Engines* needs *Heat Transfer* from mechanical engineering, which needs *Engineering
Thermodynamics*, which needs *Calculus* from maths.

The build rejects cycles and flags redundant prerequisites, and no chapter depends on a chapter of a
higher level. Only 24 chapters have no prerequisites, and each is a genuine starting point: an
introductory course, lab safety or history.

A discipline's stages follow the full graph, so a chapter always comes after everything it depends
on, including chapters in other disciplines.

## Roadmaps

There are 13 goal roadmaps. Each is complete: read from top to bottom, it never reaches a chapter
whose prerequisites haven't already appeared. The build checks this, and currently finds no gaps.

| Roadmap | Stages | Chapters | Disciplines used |
|---|---|---|---|
| Cosmos & Space Science | 10 | 70 | 4 |
| Rocket Science & Spaceflight | 11 | 154 | 8 |
| Astrobiology & Life in the Universe | 10 | 93 | 5 |
| Robotics Engineer | 10 | 138 | 9 |
| Iron Man: Build a Powered Exosuit | 10 | 224 | 10 |
| Electrical & Electronics Engineer | 10 | 133 | 7 |
| Embedded & IoT Engineer | 10 | 136 | 4 |
| Computer Engineer | 10 | 105 | 6 |
| Software Engineer | 10 | 60 | 3 |
| AI / ML Engineer | 10 | 96 | 3 |
| Data Scientist | 10 | 76 | 3 |
| Quantum Computing & Quantum Technology | 10 | 78 | 7 |
| Theoretical Physicist | 10 | 72 | 3 |

The large roadmaps are large because their goals are broad. Iron Man draws on mechanics, materials,
biology, power electronics, AI and flight. When only part of a chapter is needed, the roadmap marks
it "Selected topics" and lists those topics.

## Limits and judgement calls

"Complete" here means curriculum-complete: everything a strong degree plus graduate coursework
covers, plus the main research areas. It doesn't mean every niche research topic. Each audit report
lists what was left out on purpose.

Some overlaps are deliberate. They are kept and cross-linked as "related" instead of merged, for
example maths' *Mathematical Physics* chapters and their physics counterparts,
`ma-discrete-mathematics` and `cs-discrete-mathematics`, and three robot-kinematics chapters.
Merging would mean deleting ids that people's progress may be stored under.

A few chapters could move in future, although they haven't been moved in order to keep their ids
stable. Some AI "Data Science" chapters (databases, data engineering, big data) and the electronics
chapters on software practice (Git, CI/CD, testing) now have fuller Computer Science equivalents.

Chemistry covers propellants and energetic materials at a conceptual level only, with no synthesis
routes.

Civil, chemical and biomedical engineering aren't covered yet, and statistics lives inside
mathematics rather than being a discipline of its own. Any of these could be added the same way.

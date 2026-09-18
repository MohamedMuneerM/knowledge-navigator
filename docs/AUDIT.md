# Knowledge base audit: September 2026

The question: **if I follow this knowledge base discipline by discipline, will I have
covered the whole of each field, and is everything grouped and ordered correctly?**

Short answer: **before, no; now, yes, to the level of a full university curriculum plus
the main research areas.** Each discipline was checked against its authoritative
classification and against real degree programmes, and every gap found was filled. Every
chapter now also says what must be learned before it. The detailed evidence is in
[`docs/audit/`](audit/), one report per discipline.

## What was wrong with the original data

These problems came from the old `parse_notes.py`. The notes themselves were fine.

| Problem | Effect | Fix |
|---|---|---|
| Indented bullets were never parsed | **497 sub-topics** from the notes never reached the dashboard | Restored as nested sub-topics |
| Category headings with `\-`, "IoT", "FPGAs" or "APIs" were skipped | **60 chapters** sat under the wrong category, e.g. 28 protocol/wireless/IoT-cloud chapters under "Sensors" and 7 FPGA chapters under "Operating Systems" | Regrouped |
| An unnumbered heading ("3D Vision") was merged into the chapter before it | One chapter hidden inside another | Split out |
| Two different chapters shared the id `el-configuration-management` | Ticking one ticked the other | Second one renamed `el-device-configuration-management` |
| Priorities were guessed from keywords ("quantum" meant advanced, "history" meant optional) | "Quantum Mechanics" was marked advanced | Every chapter re-rated by hand |
| No prerequisites anywhere; each "learning path" was just the first 5 chapters | No learning order | 2,430 prerequisite links, 332 of them across disciplines |

No chapter or topic id was deleted or renamed, apart from the duplicate above, so progress
saved in the browser still lines up.

## Coverage: before and after

| Discipline | Checked against | Before | Now |
|---|---|---|---|
| Mathematics | MSC2020 (all 63 classes), Cambridge Tripos, MIT 18, MAA CUPM | 186 ch · 666 topics, no on-ramp, 114 stub chapters | 218 ch · 1,737 topics, arithmetic → research |
| Physics | APS PhySH, arXiv, MIT 8, Cambridge NST | 58 ch · 501 topics, no on-ramp, thin astronomy | 101 ch · 1,118 topics, 25-chapter astronomy track |
| Chemistry | ACS guidelines, RSC/QAA, IUPAC, MIT 5, Cambridge | didn't exist | 102 ch · 1,091 topics |
| Biology | Vision & Change, Campbell, Alberts, MIT 7, Cambridge | didn't exist | 100 ch · 1,104 topics |
| Earth & Environmental Science | AGU sections, Earth Science Literacy Principles, NSF GEO, MIT 12 | didn't exist | 83 ch · 854 topics |
| Computer Science | ACM/IEEE CS2023 (all 17 areas), ACM CCS, MIT, Stanford, OSSU | didn't exist (fragments in AI/electronics) | 84 ch · 1,026 topics |
| Electrical & Electronics Eng. | NCEES FE, ABET, MIT 6-5, Imperial | 300 ch · 1,848 topics, strong embedded/IoT but no power systems, machines, RF, comms, VLSI | 354 ch · 2,615 topics |
| AI, ML & Robotics | ACM CCS, AIMA, Stanford CS229/224N/231N/234, *Modern Robotics* | 89 ch · 1,057 topics, ~70% coverage | 121 ch · 1,666 topics |
| Mechanical Engineering | ABET, NCEES FE + 3 PE exams, ASME, MIT 2 | didn't exist | 75 ch · 928 topics |
| Materials Science & Eng. | ABET, MIT 3, Callister, Ashby, TMS/MRS | didn't exist | 83 ch · 1,011 topics |
| Aerospace Engineering | ABET, MIT 16, NASA Technology Taxonomy, Sutton, Curtis, SMAD | didn't exist | 111 ch · 1,289 topics |
| **Total** | | **4 disciplines · 632 chapters · ~3,575 topics** | **11 · 1,432 · 14,439** |

## How the learning order works

- Every chapter has a **level**: 1 Foundations, 2 Core, 3 Advanced undergraduate,
  4 Graduate, 5 Frontier. It also has a **priority** within its discipline (core,
  important, advanced or optional).
- Every chapter lists its **direct prerequisites**, which can come from any discipline.
  For example, *Liquid Rocket Engines* needs *Heat Transfer* (Mechanical), which needs
  *Engineering Thermodynamics*, which needs *Calculus* (Math).
- The build refuses **cycles**, flags **redundant** prerequisites, and no chapter depends on
  a higher-level chapter. Only 24 chapters have no prerequisites, and all of them are genuine
  entry points: intro courses, lab safety, history.
- A discipline's **stages** follow the full graph, so a chapter always comes after everything
  it depends on, including chapters in other disciplines.

## Roadmaps

13 goal roadmaps. Each is **prerequisite-complete**: followed top to bottom, it never reaches a
chapter whose prerequisites haven't come earlier. The build checks this and reports 0 issues.

| Roadmap | Stages | Chapters | Disciplines used |
|---|---|---|---|
| 🌌 Cosmos & Space Science | 10 | 70 | 4 |
| 🚀 Rocket Science & Spaceflight | 11 | 154 | 8 |
| 👽 Astrobiology & Life in the Universe | 10 | 93 | 5 |
| 🦾 Robotics Engineer | 10 | 138 | 9 |
| 🦸 Iron Man: Build a Powered Exosuit | 10 | 224 | 10 |
| ⚡ Electrical & Electronics Engineer | 10 | 133 | 7 |
| 📟 Embedded & IoT Engineer | 10 | 136 | 4 |
| 🖥️ Computer Engineer | 10 | 105 | 6 |
| 👩‍💻 Software Engineer | 10 | 60 | 3 |
| 🧠 AI / ML Engineer | 10 | 96 | 3 |
| 📊 Data Scientist | 10 | 76 | 3 |
| ⚛️ Quantum Computing & Quantum Technology | 10 | 78 | 7 |
| 🌀 Theoretical Physicist | 10 | 72 | 3 |

Large roadmaps are large because the goal is broad. Iron Man touches mechanics, materials,
biology, power electronics, AI and flight. Chapters needed only in part are marked
"Selected topics", with the specific topics listed.

## Known limits and judgement calls

- **"Complete" means curriculum-complete.** Everything a strong degree plus graduate
  coursework covers, plus the main research areas. It is not every niche research topic.
  Each audit report lists what was deliberately left out.
- **Deliberate overlaps** are kept and cross-linked as "related" rather than merged (e.g.
  math's *Mathematical Physics* chapters vs physics, `ma-discrete-mathematics` vs
  `cs-discrete-mathematics`, three robot-kinematics chapters). Merging would have meant
  deleting ids that your progress may be stored under.
- **Suggested future moves** (not done, to protect ids): some AI "Data Science" chapters
  (databases, data engineering, big data) and electronics' software-practice chapters (Git,
  CI/CD, testing) now have fuller Computer Science equivalents.
- Chemistry keeps propellants and energetic materials **conceptual** (no synthesis routes).
- Disciplines not covered yet: civil, chemical and biomedical engineering, and statistics as
  its own discipline (it lives in Math). Each could be added the same way.

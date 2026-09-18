# Audit: Computer Science (`cs`)

## 1. Verdict

**Before:** the discipline was an empty stub, with no description and 0 chapters.
**Now:** 84 chapters and 1,026 topics in 18 categories. They run from a level-1 on-ramp (computational thinking, Python, the command line, Git, web basics) to level-5 frontier chapters. All 17 CS2023 knowledge areas are covered, either here or by a deliberate link to the Math or AI discipline. The same goes for every top-level branch of the ACM CCS 2012 and all nine teachyourselfcs.com subjects. The validator reports 0 errors and 0 warnings.

## 2. Sources checked

- ACM/IEEE-CS/AAAI, *Computer Science Curricula 2023 (CS2023)*. The list of knowledge areas is at https://csed.acm.org/knowledge-areas/. All 17 areas and roughly 150 knowledge units were taken from the full report: https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm
- ACM Computing Classification System 2012: https://dl.acm.org/ccs (mirror used: https://cran.r-project.org/web/classifications/ACM-2012.html)
- ACM/IEEE, *Computer Engineering Curricula 2016 (CE2016)*: https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf (subject-area list checked via https://www.ccny.cuny.edu/sites/default/files/2023-10/ACM-IEEE--computer-engineering-2016--excerpts.pdf)
- MIT EECS Course 6 subject listing (6.1xxx undergraduate and 6.5xxx graduate CS subjects): https://catalog.mit.edu/subjects/6/
- Stanford CS B.S. core and tracks (Systems, Theory, AI, HCI, Information, Visual Computing): https://bulletin.stanford.edu/programs/CS-BS
- teachyourselfcs.com, a self-learner guide covering 9 subjects: https://teachyourselfcs.com/
- OSSU Computer Science open curriculum (intro, core, advanced and final project): https://github.com/ossu/computer-science
- Standard textbooks used for chapter syllabi: CS:APP (Bryant & O'Hallaron), OSTEP, Kurose & Ross, *Crafting Interpreters*, *Designing Data-Intensive Applications*, CLRS/Kleinberg-Tardos, Hennessy & Patterson, *Saltzer & Kaashoek* (MIT 6.1800), and *The Missing Semester* (MIT).

## 3. Coverage checklist

### CS2023 knowledge areas

| CS2023 area | Chapters | Status |
|---|---|---|
| SDF: Software Development Fundamentals | cs-programming-fundamentals, cs-program-design, cs-data-structures, cs-command-line-shell, cs-version-control-git | ➕ added |
| AL: Algorithmic Foundations (AL-Foundational, Strategies, Complexity) | cs-data-structures, cs-algorithms, cs-advanced-algorithms | ➕ added |
| AL-Models (automata, formal languages, computability) | math: ma-automata-theory, ma-formal-languages, ma-computability-theory, ma-complexity-theory | ⛔ owned by Mathematics (Theoretical CS); linked via `related` and prerequisites |
| AR: Architecture & Organization (Logic, Representation, Assembly, Memory, IO, Organization, Performance-Energy, Heterogeneity, Quantum) | cs-computer-organization, cs-computer-architecture, cs-advanced-computer-architecture, cs-quantum-computing | ➕ added (digital logic linked to el-combinational-logic / el-sequential-logic) |
| AI: Artificial Intelligence | ai-* discipline | ⛔ owned by the AI discipline. CS links to it via `related` (e.g. ai-large-language-models-llms, ai-hardware-for-ai) |
| DM: Data Management (Data, Core, Modeling, Relational, Querying, Processing, Internals, NoSQL, Security, Analytics, Distributed, Unstructured) | cs-databases, cs-database-internals, cs-nosql-data-systems, cs-data-engineering, cs-information-retrieval | ➕ added (analytics/ML side linked to ai-data-engineering, ai-big-data-technologies) |
| FPL: Foundations of Programming Languages (OOP, Functional, Logic, Scripting, Event-driven, Parallel, Types, Translation, Syntax, Semantics, Analysis, Code, Run-time, Constructs, Formalism, Methodologies, Design) | cs-object-oriented-programming, cs-functional-programming, cs-programming-languages, cs-compilers, cs-optimizing-compilers, cs-interpreters-runtime-systems, cs-type-systems-semantics, cs-program-analysis-verification, cs-concurrent-programming | ➕ added |
| GIT: Graphics & Interactive Techniques (Rendering, Modeling, Shading, Animation, Simulation, Visualization, Immersion, Interaction, Image, Physical) | cs-computer-graphics, cs-advanced-rendering, cs-geometric-modeling, cs-computer-animation-simulation, cs-information-visualization, cs-virtual-augmented-reality, cs-game-development | ➕ added. GIT-Image (image processing) is ⚠️ partial: it is owned by ai-image-processing-fundamentals / el-image-processing. GIT-Physical (tangible computing) is covered by the electronics discipline. |
| HCI (User, Accountability, Accessibility, Evaluation, Design) | cs-hci, cs-ux-design, cs-accessibility | ➕ added |
| MSF: Mathematical & Statistical Foundations (Discrete, Probability, Statistics, Linear, Calculus) | cs-discrete-mathematics, cs-probability-statistics-for-cs; ma-linear-algebra and ma-calculus used as prerequisites | ➕ added. Linear algebra and calculus are ⛔ owned by Math. |
| NC: Networking & Communication (Fundamentals, Applications, Reliability, Routing, SingleHop, Security, Mobility, Emerging) | cs-computer-networks, cs-advanced-networking, cs-network-security | ➕ added |
| OS: Operating Systems (Purpose → Faults, Virtualization, Real-time) | cs-operating-systems, cs-virtualization-containers, cs-advanced-operating-systems | ➕ added. Real-time/embedded OS is ⚠️ overview only; the depth is in el-real-time-operating-systems-rtos. |
| PDC: Parallel & Distributed Computing (Programs, Communication, Coordination, Evaluation, Algorithms) | cs-concurrent-programming, cs-parallel-computing, cs-gpu-programming, cs-high-performance-computing, cs-distributed-systems, cs-distributed-algorithms, cs-system-design | ➕ added |
| SE: Software Engineering (Teamwork, Tools, Requirements, Design, Construction, Validation, Refactoring, Reliability, Formal) | cs-software-construction, cs-software-design-patterns, cs-software-testing, cs-software-engineering-process, cs-requirements-engineering, cs-software-maintenance-evolution, cs-software-architecture, cs-program-analysis-verification, cs-devops-cicd | ➕ added |
| SEC: Security (Foundations, Coding, Crypto, Engineering, Forensics, Governance) | cs-computer-security, cs-applied-cryptography, cs-application-security, cs-network-security, cs-systems-security, cs-offensive-security, cs-security-operations-forensics, cs-security-governance-privacy, cs-advanced-cryptographic-systems | ➕ added (theory in ma-cryptography) |
| SEP: Society, Ethics & the Profession (Context, Ethics, IP, Privacy, Communication, Sustainability, History, Economies, Security, DEIA) | cs-computing-ethics, cs-professional-practice, cs-history-of-computing, cs-security-governance-privacy, cs-research-methods | ➕ added |
| SF: Systems Fundamentals (Overview, Foundations, Resource, Performance, Evaluation, Reliability, Security, Design) | cs-computer-systems-principles, cs-performance-engineering, plus the OS and networks chapters | ➕ added |
| SPD: Specialized Platform Development (Web, Mobile, Game, Interactive, Robot, Embedded) | cs-web-fundamentals, cs-frontend-development, cs-backend-development, cs-mobile-development, cs-game-development, cs-virtual-augmented-reality | ➕ added. Robot and Embedded platforms are ⛔ owned by AI (robotics) and Electronics (embedded). |
| AI-Assisted development (new CS2023 theme) | cs-ai-assisted-software-development | ➕ added (frontier) |

### ACM CCS 2012 top-level branches

| CCS branch | Where | Status |
|---|---|---|
| Hardware | cs-computer-organization, cs-computer-architecture; circuits in el-* | ✅ / ⛔ circuits in Electronics |
| Computer systems organization | architecture, embedded (el-*), real-time (el-*), cs-parallel-computing | ✅ |
| Networks | cs-computer-networks, cs-advanced-networking, cs-network-security | ✅ |
| Software and its engineering | Software Engineering category, Programming Languages & Compilers category, cs-operating-systems | ✅ |
| Theory of computation | cs-algorithms, cs-advanced-algorithms, cs-distributed-algorithms, cs-type-systems-semantics; the rest in ma-* | ✅ / ⛔ Math |
| Mathematics of computing | cs-discrete-mathematics, cs-probability-statistics-for-cs, cs-high-performance-computing; ma-* | ✅ |
| Information systems | Data Management category, cs-information-retrieval, web chapters | ✅ |
| Security and privacy | Security category (9 chapters) | ✅ |
| Human-centered computing | HCI category, cs-information-visualization, cs-accessibility | ✅ (collaborative/social and ubiquitous computing are topics within cs-hci) |
| Computing methodologies | graphics chapters, cs-high-performance-computing, cs-parallel-computing; AI/ML/vision in ai-* | ✅ / ⛔ AI |
| Applied computing | Largely owned by the other disciplines (bio, chem, earth, engineering) | ⛔ belongs to the application disciplines |
| Social and professional topics | Society, Ethics & Profession category | ✅ |
| General and reference | cs-research-methods (evaluation, measurement) | ✅ |

### CE2016 (computer engineering) areas relevant to CS

| CE2016 area | Where | Status |
|---|---|---|
| CE-CAO Computer Architecture & Organization | cs-computer-organization, cs-computer-architecture | ✅ |
| CE-DIG Digital Design | el-combinational-logic, el-sequential-logic (related from cs-computer-organization) | ⛔ Electronics |
| CE-ESY Embedded Systems | el-* embedded chapters | ⛔ Electronics |
| CE-NWK Computer Networks | cs-computer-networks | ✅ |
| CE-SEC Information Security | Security category | ✅ |
| CE-SRM Systems Resource Management | cs-operating-systems, cs-virtualization-containers | ✅ |
| CE-SWD Software Design | Software Engineering category | ✅ |
| CE-CAL Computing Algorithms | cs-data-structures, cs-algorithms, cs-parallel-computing | ✅ |
| CE-PPP Preparation for Professional Practice | cs-computing-ethics, cs-professional-practice | ✅ |
| CE-CAE / CE-SGP (circuits, signal processing) | el-*, ma-signal-processing | ⛔ Electronics / Math |

### Curricula cross-check

| Course / subject | Chapter |
|---|---|
| teachyourselfcs: Programming (SICP) / Architecture (CS:APP) / Algorithms / Math for CS / OS / Networking / Databases / Languages & Compilers / Distributed Systems | cs-functional-programming + cs-program-design / cs-computer-organization + cs-systems-programming / cs-algorithms / cs-discrete-mathematics / cs-operating-systems / cs-computer-networks / cs-databases + cs-database-internals / cs-programming-languages + cs-compilers / cs-distributed-systems ✅ |
| OSSU: The Missing Semester | cs-command-line-shell, cs-version-control-git ✅ |
| OSSU: Nand2Tetris I & II | cs-computer-organization (Nand2Tetris project topic), cs-compilers ✅ |
| OSSU: Software Architecture, Object-Oriented Design, Software Testing, Software Debugging | cs-software-architecture, cs-software-design-patterns, cs-software-testing ✅ |
| OSSU: Core Security, Advanced Information Security (web security, governance, forensics, secure SDLC) | Security category ✅ |
| OSSU: Computer Graphics, Databases (3 courses) | cs-computer-graphics; cs-databases, cs-nosql-data-systems ✅ |
| OSSU: Core Ethics (ethics, IP, data privacy) | cs-computing-ethics, cs-security-governance-privacy ✅ |
| OSSU: Parallel Programming, Compilers, Haskell, Prolog | cs-parallel-computing, cs-compilers, cs-functional-programming, cs-programming-languages (Prolog topic) ✅ |
| MIT 6.1010 / 6.1020 / 6.1040 / 6.1060 | cs-program-design / cs-software-construction / cs-software-design-patterns + cs-ux-design / cs-performance-engineering ✅ |
| MIT 6.1100 / 6.1120 (language engineering) | cs-compilers, cs-interpreters-runtime-systems ✅ |
| MIT 6.1200 / 6.1210 / 6.1220 | cs-discrete-mathematics / cs-data-structures + cs-algorithms / cs-algorithms ✅ |
| MIT 6.1600 / 6.5610 / 6.5660 | cs-computer-security / cs-applied-cryptography / cs-systems-security ✅ |
| MIT 6.1800 / 6.1810 / 6.1820 / 6.1830 | cs-computer-systems-principles / cs-advanced-operating-systems / cs-mobile-development / cs-data-engineering ✅ |
| MIT 6.1903 / 6.1910 / 6.1920 / 6.5900 | cs-systems-programming / cs-computer-organization / cs-computer-architecture / cs-advanced-computer-architecture ✅ |
| MIT 6.5080 / 6.5920 (multicore, parallel) | cs-concurrent-programming, cs-parallel-computing ✅ |
| MIT 6.5210 / 6.5220 / 6.5230 / 6.5240 | cs-advanced-algorithms ✅ |
| MIT 6.5110 / 6.5120 / 6.5130 (program analysis, formal reasoning, synthesis) | cs-program-analysis-verification, cs-type-systems-semantics, cs-ai-assisted-software-development ✅ |
| MIT 6.5250 / 6.5840 | cs-distributed-algorithms / cs-distributed-systems ✅ |
| MIT 6.5820 / 6.5830 | cs-advanced-networking / cs-database-internals ✅ |
| MIT 6.5930 / 6.5950 (DL hardware, secure hardware) | cs-advanced-computer-architecture, cs-systems-security (and ai-hardware-for-ai) ✅ |
| Stanford CS106B/107/110/111/140/144/145/147/148/155/161/166 | data structures / systems programming / OS / networks / databases / HCI / graphics / security / algorithms / advanced data structures ✅ |

## 4. Grouping changes

The discipline was new, so no existing chapters were regrouped. The 18 categories run from foundational to applied:
Computing Foundations → Mathematical Foundations → Programming & Paradigms → Data Structures & Algorithms → Software Engineering → Computer Architecture & Systems Programming → Operating Systems → Computer Networks → Data Management → Programming Languages & Compilers → Parallel & Distributed Computing → Cloud Computing & DevOps → Web & Mobile Development → Security → Human-Computer Interaction → Graphics, Visualization & Games → Emerging Computing & Frontiers → Society, Ethics & Profession.

Three placements are judgement calls:
- Principles of Computer System Design (MIT 6.1800 style) opens Parallel & Distributed Computing, because it bridges OS and networks to distributed systems.
- Linux System Administration sits under Cloud Computing & DevOps rather than Operating Systems, since it covers operations practice rather than OS internals.
- Web Fundamentals is level 1 and gives a second on-ramp next to Python, even though its category appears later in the list.

## 5. What was added

All 84 chapters are new:
- On-ramp (level 1): cs-computational-thinking, cs-programming-fundamentals, cs-command-line-shell, cs-version-control-git, cs-web-fundamentals, cs-history-of-computing.
- Core spine: discrete math and probability for CS, program design, OOP, data structures, algorithms, software construction, computer organization, systems programming in C, computer architecture, operating systems, networks, databases, programming-language concepts, concurrent programming, distributed systems, computer security, computing ethics.
- Breadth: functional programming, Modern C++ & Rust, performance engineering, virtualization and containers, NoSQL, data engineering, compilers, parallel computing, cloud, DevOps, SRE, large-scale system design, web frontend and backend, mobile, the full security track (applied crypto, application, network, systems, offensive, SOC/forensics, governance/privacy), HCI, UX, accessibility, graphics, visualization, rendering, geometric modeling, animation, XR, game development, quantum computing, blockchain.
- Frontier (level 5): AI-assisted software development and program synthesis, advanced cryptographic systems (post-quantum, ZK, MPC, FHE), and frontiers in computer systems (CXL, disaggregation, CHERI, confidential computing, carbon-aware computing).

## 6. Learning-order notes

Four spines run through the discipline:
- Programming: Computational Thinking → Programming Fundamentals (Python) → Program Design → OOP → Software Construction → Design Patterns / Testing → Software Architecture.
- Theory: Discrete Math → Data Structures → Algorithms → Advanced Algorithms (with ma-complexity-theory etc. as related reading).
- Systems: Computer Organization → Systems Programming in C → Operating Systems / Computer Networks / Computer Architecture → Concurrent Programming → Distributed Systems → Large-Scale System Design / SRE.
- Security: OS and Networks → Foundations of Computer Security → Applied Cryptography → Network Security → Offensive Security / Forensics.

## 7. Recommended moves and open questions

- Math has no introductory discrete-math chapter, since its combinatorics and logic chapters are specialist ones. cs-discrete-mathematics fills that gap, with `related` links to ma-logic-proof-theory, ma-set-theory, ma-graph-theory, ma-enumerative-combinatorics and ma-elementary-number-theory. If Math later adds a general "Discrete Mathematics" chapter, it should be linked as `related`.
- CS has no AI survey chapter. Overlaps with AI are handled with `related` links (ai-databases, ai-data-engineering, ai-hardware-for-ai, ai-large-language-models-llms, ai-fairness-in-ml and others). ai-databases and ai-big-data-technologies overlap with cs-databases and cs-data-engineering, and the CS versions are the full courses.
- el-version-control, el-software-testing, el-continuous-integration-continuous-deployment-cicd, el-containers-virtualization, el-network-security and el-cryptography-fundamentals are embedded-flavoured duplicates of general CS subjects. The CS chapters link to them as `related`. The electronics chapters link back as `related` and use CS chapters as prerequisites where needed.
- Image processing (CS2023 GIT-Image) is left to ai-image-processing-fundamentals and el-image-processing.

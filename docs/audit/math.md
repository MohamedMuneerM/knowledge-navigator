# Mathematics: curation audit

## 1. Verdict

**Before:** 186 chapters and 666 topics. The list was broad (almost every MSC area had a name), but 114 chapters were stubs of 2 or 3 bullet labels. There was no on-ramp at all (no arithmetic, trigonometry, precalculus, multivariable or vector calculus, series or intro proofs), "Calculus" had only 5 topics, and no chapter had a level, priority, summary or prerequisites.

**Now:** 217 chapters and 1,726 topics (1,652 topics plus 74 sub-topics). Every chapter has a level, priority, one-sentence summary and minimal direct prerequisites. The validator reports 0 errors and 0 warnings. Someone with only high-school basics can start at level 1 and follow prerequisites all the way to research-level chapters. All 63 top-level MSC2020 classes now map to at least one chapter.

## 2. Sources checked

- MSC2020, the 63 top-level classes: <https://msc2020.org/>, <https://en.wikipedia.org/wiki/Mathematics_Subject_Classification>. zbMATH's classification browser (<https://zbmath.org/classification/>) returned 403, so these mirrors were used instead.
- Cambridge Mathematical Tripos, Schedules of Lecture Courses (Parts IA, IB, II): <https://www.maths.cam.ac.uk/undergrad/files/schedules.pdf>
- MIT Mathematics (Course 18) subject listing: <https://catalog.mit.edu/subjects/18/>, and MIT OpenCourseWare <https://ocw.mit.edu/>
- MAA 2015 CUPM Curriculum Guide to Majors in the Mathematical Sciences, including the Calculus, Linear Algebra and Applied Statistics & Data Analysis course-area reports: <https://www.amstat.org/docs/default-source/amstat-documents/cupmguide_print.pdf>, <https://maa.org/resource/cupm-guide/>
- Standard textbook tables of contents, used to write topic syllabi: Stewart *Calculus*, Rosen *Discrete Mathematics*, Axler/Strang *Linear Algebra*, Dummit & Foote, Rudin, Stein & Shakarchi, Hatcher, Lee, Durrett, Casella & Berger, Boyd & Vandenberghe, Sipser, Horn & Johnson and Davey & Priestley.

## 3. Coverage checklist

### MSC2020 top-level classes

| MSC | Area | Chapters | Status |
|---|---|---|---|
| 00 | General | (general works, not a subject) | ⛔ not a study area |
| 01 | History and biography | ma-history-of-mathematics, ma-foundations-philosophy | ✅ |
| 03 | Mathematical logic and foundations | ma-introduction-to-proofs, ma-logic-proof-theory, ma-set-theory, ma-model-theory, ma-recursion-computability | ✅ (+ intro proofs added) |
| 05 | Combinatorics | ma-discrete-mathematics, ma-enumerative-combinatorics, ma-graph-theory, designs, Ramsey, extremal, probabilistic, algebraic, matroids | ✅ (+ discrete maths added) |
| 06 | Order, lattices, ordered algebraic structures | ma-order-lattices | ➕ added |
| 08 | General algebraic systems | ma-universal-algebra | ➕ added |
| 11 | Number theory | ma-elementary-number-theory … ma-modular-forms, ma-additive-combinatorics | ✅ |
| 12 | Field theory and polynomials | ma-field-theory | ✅ |
| 13 | Commutative algebra | ma-commutative-algebra, ma-computer-algebra (13P) | ✅ |
| 14 | Algebraic geometry | ma-algebraic-geometry, ma-arithmetic-geometry, ma-derived-algebraic-geometry, ma-tropical-geometry | ✅ |
| 15 | Linear and multilinear algebra; matrix theory | ma-linear-algebra, ma-matrix-analysis | ✅ (+ matrix analysis added) |
| 16 | Associative rings and algebras | ma-ring-theory (noncommutative rings, Artin-Wedderburn) | ✅ |
| 17 | Nonassociative rings and algebras | ma-lie-theory, ma-specialized-algebraic-structures (octonions, Jordan algebras) | ⚠️ partial: no dedicated chapter, niche |
| 18 | Category theory; homological algebra | ma-category-theory, ma-homological-algebra, ma-higher-dimensional-algebra | ✅ |
| 19 | K-theory | ma-k-theory | ✅ |
| 20 | Group theory | ma-abstract-algebra, ma-group-theory, ma-representation-theory | ✅ (+ representation theory added) |
| 22 | Topological groups, Lie groups | ma-lie-theory, ma-abstract-harmonic-analysis | ✅ |
| 26 | Real functions | ma-real-analysis, ma-real-functions | ➕ added |
| 28 | Measure and integration | ma-measure-theory-integration | ✅ |
| 30 | Functions of a complex variable | ma-complex-analysis, ma-riemann-surfaces | ✅ (+ Riemann surfaces added) |
| 31 | Potential theory | ma-potential-theory | ✅ |
| 32 | Several complex variables | ma-several-complex-variables | ➕ added |
| 33 | Special functions | ma-special-functions | ✅ |
| 34 | Ordinary differential equations | ma-ordinary-differential-equations-odes, ma-boundary-value-problems | ✅ |
| 35 | Partial differential equations | ma-partial-differential-equations-pdes, ma-mathematical-methods | ✅ (+ methods course added) |
| 37 | Dynamical systems and ergodic theory | ma-dynamical-systems, ma-ergodic-theory, ma-symbolic-dynamics | ✅ |
| 39 | Difference and functional equations | ma-difference-equations, ma-functional-equations | ✅ |
| 40 | Sequences, series, summability | ma-sequences-series, ma-summability-divergent-series | ➕ added |
| 41 | Approximations and expansions | ma-approximation-theory, ma-asymptotic-methods | ✅ (+ asymptotics added) |
| 42 | Harmonic analysis on Euclidean spaces | ma-harmonic-analysis | ✅ |
| 43 | Abstract harmonic analysis | ma-abstract-harmonic-analysis | ➕ added |
| 44 | Integral transforms, operational calculus | ma-integral-transforms | ✅ |
| 45 | Integral equations | ma-integral-equations | ✅ |
| 46 | Functional analysis | ma-functional-analysis | ✅ |
| 47 | Operator theory | ma-operator-theory | ➕ added |
| 49 | Calculus of variations, optimal control, optimisation | ma-variational-methods, ma-calculus-of-variations-optimal-control, Optimization category | ✅ |
| 51 | Geometry | ma-euclidean-geometry, ma-analytic-geometry, ma-non-euclidean-geometry, ma-projective-geometry | ✅ |
| 52 | Convex and discrete geometry | ma-convex-geometry, ma-discrete-computational-geometry, ma-integral-geometry | ✅ (+ integral geometry added) |
| 53 | Differential geometry | ma-differential-geometry, ma-riemannian-geometry, ma-symplectic-geometry, ma-tensor-analysis | ✅ (+ 3 added) |
| 54 | General topology | ma-general-topology | ✅ |
| 55 | Algebraic topology | ma-algebraic-topology, ma-homotopy-theory, ma-fiber-bundles | ✅ (+ homotopy theory added) |
| 57 | Manifolds and cell complexes | ma-manifolds-cell-complexes, ma-geometric-topology, ma-low-dimensional-topology | ➕ added |
| 58 | Global analysis | ma-global-analysis, ma-differential-topology | ✅ |
| 60 | Probability theory, stochastic processes | ma-elementary-probability, ma-probability-theory, ma-measure-theoretic-probability, ma-stochastic-processes, ma-stochastic-calculus | ✅ (+ 2 added) |
| 62 | Statistics | Probability & Statistics category, incl. ma-mathematical-statistics and ma-causal-inference | ✅ (+ 2 added) |
| 65 | Numerical analysis | Numerical Analysis category (11 chapters) | ✅ |
| 68 | Computer science | Theoretical Computer Science category, ma-computer-algebra | ✅ |
| 70 | Mechanics of particles and systems | ma-classical-mechanics | ✅ |
| 74 | Mechanics of deformable solids | ma-solid-mechanics | ✅ |
| 76 | Fluid mechanics | ma-fluid-mechanics | ✅ |
| 78 | Optics, electromagnetic theory | ma-optics, ma-electromagnetism | ✅ |
| 80 | Classical thermodynamics | ma-thermodynamics | ✅ |
| 81 | Quantum theory | ma-quantum-mechanics, ma-quantum-field-theory, ma-quantum-computation-theory | ✅ |
| 82 | Statistical mechanics | ma-statistical-mechanics | ✅ |
| 83 | Relativity and gravitation | ma-relativity | ✅ |
| 85 | Astronomy and astrophysics | ma-mathematical-aspects-of-astronomy | ✅ |
| 86 | Geophysics | ma-geophysics, ma-geophysical-environmental-mathematics | ✅ |
| 90 | Operations research, mathematical programming | Optimization category, ma-operations-research, ma-mathematical-programming | ✅ |
| 91 | Game theory, economics, finance | ma-game-theory, ma-mathematical-economics, ma-financial-mathematics, ma-actuarial-mathematics | ✅ |
| 92 | Biology and other natural sciences | ma-mathematical-biology, ma-mathematical-chemistry | ✅ |
| 93 | Systems theory; control | ma-control-theory, ma-systems-theory-control | ✅ |
| 94 | Information and communication, circuits | ma-information-theory, ma-information-communication-theory, ma-signal-processing, ma-circuit-theory | ✅ |
| 97 | Mathematics education | ma-mathematics-education | ✅ |

### Curriculum check (Cambridge / MIT / CUPM)

| Course in real curricula | Chapter | Status |
|---|---|---|
| Arithmetic, algebra, geometry, trigonometry, precalculus (CUPM calculus-readiness) | ma-arithmetic-pre-algebra, ma-elementary-intermediate-algebra, ma-euclidean-geometry, ma-trigonometry, ma-precalculus | ➕ 3 added |
| MIT 18.01 / Cambridge IA Analysis I (single-variable calculus) | ma-calculus (5 → 17 topics), ma-sequences-series | ➕ |
| MIT 18.02 / Cambridge IA Vector Calculus | ma-multivariable-calculus, ma-vector-calculus | ➕ added |
| MIT 18.090, Cambridge IA Numbers & Sets (proofs) | ma-introduction-to-proofs, ma-elementary-number-theory | ➕ |
| MIT 18.062 Mathematics for CS (discrete maths) | ma-discrete-mathematics | ➕ added |
| MIT 18.06 / Cambridge IB Linear Algebra | ma-linear-algebra (8 → 15) | ✅ enriched |
| MIT 18.03, Cambridge IA Differential Equations | ma-ordinary-differential-equations-odes | ✅ enriched |
| MIT 18.075 / Cambridge IB Methods | ma-mathematical-methods | ➕ added |
| Cambridge Part II Asymptotic Methods, MIT 18.305 | ma-asymptotic-methods | ➕ added |
| MIT 18.05 / 18.600 / Cambridge IA Probability | ma-elementary-probability, ma-probability-theory | ➕ / ✅ |
| Cambridge Part II Probability & Measure | ma-measure-theoretic-probability | ➕ added |
| MIT 18.655, Cambridge Principles of Statistics | ma-mathematical-statistics | ➕ added |
| Cambridge Part II Representation Theory | ma-representation-theory | ➕ added |
| Cambridge Part II Riemann Surfaces, MIT 18.116 | ma-riemann-surfaces | ➕ added |
| MIT 18.117 Several Complex Variables | ma-several-complex-variables | ➕ added |
| Cambridge Part II Linear Analysis / Analysis of Functions, MIT 18.102 | ma-functional-analysis, ma-operator-theory | ✅ / ➕ |
| MIT 18.965 Manifolds & Lie groups, 18.950 Differential Geometry | ma-differential-topology, ma-riemannian-geometry, ma-lie-theory | ✅ / ➕ |
| Cambridge Part II Coding & Cryptography, Automata & Formal Languages, Logic & Set Theory, Graph Theory, Galois Theory, Number Fields, Algebraic Topology, Algebraic Geometry, Dynamical Systems, Integrable Systems, Stochastic Financial Models, Mathematics of ML, Mathematical Biology, Numerical Analysis | matching existing chapters | ✅ all present, enriched |
| CUPM Applied Statistics & Data Analysis | descriptive → inferential → regression → experimental design | ✅ |

## 4. Grouping changes

- A new level-1 category, "Pre-University Foundations", holds arithmetic, algebra, Euclidean geometry, trigonometry, precalculus and analytic geometry. Euclidean and analytic geometry moved here from "Geometry", and elementary algebra moved here from "Algebra".
- A new "Calculus" category holds calculus, moved out of "Analysis", plus the new series, multivariable and vector calculus chapters.
- "Meta-Mathematics & Education" is now "History, Philosophy & Education". The chapter "Foundations & Philosophy" (philosophy, history, aesthetics and metamathematics) moved here from "Foundations & Mathematical Logic".
- Categories now run from foundational to applied: Pre-University → Calculus → Foundations & Logic → Combinatorics & Discrete → Algebra → Number Theory → Analysis → Differential Equations → Geometry → Topology → Probability & Statistics → Numerical → Optimization & Control → Theoretical CS → ML Mathematics → Mathematical Physics → Applied → Emerging → History/Philosophy/Education. Within each category, chapters are ordered by level.
- Three topics moved, keeping their ids: `ma-calculus-3` "Multivariable calculus" → ma-multivariable-calculus, `ma-calculus-4` "Vector calculus" → ma-vector-calculus, and `ma-calculus-5` "Calculus of variations" → ma-variational-methods. Each got a clearer name, and Calculus is now a single-variable syllabus.
- Mathematical Physics (15 chapters) and ML & Data Science Mathematics (10 chapters) stay. They are set to `advanced` (ma-geophysics is `optional`) and linked with `related` to their physics (ph-*) and AI (ai-*) counterparts.

## 5. What was added

31 new chapters:
ma-arithmetic-pre-algebra, ma-trigonometry, ma-precalculus, ma-sequences-series, ma-multivariable-calculus, ma-vector-calculus, ma-introduction-to-proofs, ma-discrete-mathematics, ma-representation-theory, ma-matrix-analysis, ma-order-lattices, ma-universal-algebra, ma-real-functions, ma-asymptotic-methods, ma-operator-theory, ma-abstract-harmonic-analysis, ma-several-complex-variables, ma-riemann-surfaces, ma-summability-divergent-series, ma-mathematical-methods, ma-tensor-analysis, ma-riemannian-geometry, ma-symplectic-geometry, ma-integral-geometry, ma-manifolds-cell-complexes, ma-homotopy-theory, ma-elementary-probability, ma-mathematical-statistics, ma-measure-theoretic-probability, ma-causal-inference, ma-computer-algebra.

Existing chapters with the largest gains (topics before → after):
Calculus 5 → 17 (limits, derivative rules as sub-topics, applications, integration techniques, improper integrals, applications of integration); Linear Algebra 8 → 15; Real Analysis 6 → 9 (plus sub-topics); Abstract Algebra 6 → 10; Group Theory 7 → 12; Ring Theory 6 → 11; Field Theory 5 → 9; ODEs 5 → 11; PDEs 6 → 15; Probability Theory 7 → 13; Graph Theory 9 → 13; Complex Analysis 8 → 16; General Topology 6 → 11; Algebraic Topology 7 → 11; Functional Analysis 7 → 14; Elementary Number Theory 6 → 13; Control Theory 6 → 13; Game Theory 6 → 13. Most former 2- or 3-topic advanced chapters now have 4 to 8 concrete topics. Only ma-mathematical-aesthetics (optional) still has 3.

The discipline description was also filled in.

## 6. Learning-order notes

The main spine is Arithmetic → Algebra → Geometry → Trigonometry → Precalculus → Calculus → Sequences & Series → Multivariable → Vector Calculus. Linear Algebra (after precalculus) and ODEs (after calculus) run alongside it. From there, three tracks branch off:

- Pure: Intro to Proofs → Real Analysis → General Topology / Measure Theory → Functional Analysis, and Intro to Proofs + Linear Algebra → Abstract Algebra → Group/Ring/Field theory → Commutative Algebra → Algebraic Geometry.
- Applied: ODEs + Vector Calculus → Mathematical Methods → PDEs → Numerical PDEs.
- Probability & statistics: Elementary Probability → Probability Theory → Inferential Statistics → Regression, then Measure-Theoretic Probability → Stochastic Calculus.

The graph has 12 in-discipline stages. The main roots other disciplines should use are ma-calculus, ma-multivariable-calculus, ma-vector-calculus, ma-linear-algebra, ma-ordinary-differential-equations-odes, ma-mathematical-methods, ma-probability-theory, ma-discrete-mathematics and ma-precalculus.

ODEs deliberately require only Calculus, not Linear Algebra, as in MIT 18.03, where the course teaches the matrix facts it needs. This also avoids redundant-prerequisite warnings in physics, chemistry, mechanical and aerospace chapters that list both. Dynamical systems, control theory, classical mechanics and quantum mechanics list Linear Algebra explicitly.

## 7. Recommended moves / open questions

- These overlapping chapters were kept and cross-linked with `related`: ma-computability-theory ↔ ma-recursion-computability; ma-topological-data-analysis-tda ↔ ma-topological-data-analysis (true duplicates, one in Topology and one in Emerging); ma-information-geometry ↔ ma-information-geometry-ml-context; ma-algebraic-coding-theory ↔ ma-error-correcting-codes ↔ ma-coding-theory-combinatorial-aspects; ma-cryptography ↔ ma-cryptographic-number-theory; ma-linear-programming ↔ ma-mathematical-programming; ma-control-theory ↔ ma-systems-theory-control; ma-convex-analysis ↔ ma-convex-optimization / ma-convex-geometry; ma-variational-methods ↔ ma-calculus-of-variations-optimal-control; ma-high-dimensional-probability ↔ ma-measure-concentration; ma-philosophy-of-mathematics ↔ ma-foundations-philosophy ↔ ma-history-of-mathematics; ma-discrete-mathematics ↔ ma-introduction-to-proofs.
- Some chapters arguably belong in another discipline but were left in place: the Theoretical Computer Science category (automata, formal languages, complexity, algorithm analysis, algorithmic graph theory, type theory, formal verification) → CS; the ML & Data Science Mathematics category → AI; ma-circuit-theory and ma-signal-processing → Electronics; ma-control-theory / ma-systems-theory-control → Electronics/Mechanical; ma-geophysics and ma-geophysical-environmental-mathematics → Earth science; the Mathematical Physics category → Physics.
- Nonassociative algebras (MSC 17, apart from Lie theory) have no dedicated chapter because the area is too niche. There is no separate "Metric Spaces" chapter either, because General Topology and Real Analysis already cover it.

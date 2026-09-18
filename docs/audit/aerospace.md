# Audit: Aerospace Engineering (`aerospace`, prefix `ae`)

## 1. Verdict

**Before:** the discipline was an empty stub (0 chapters, 0 topics).
**Now:** 109 chapters and 1,271 topics in 18 categories. The path starts with six level-1 on-ramp chapters and runs to level-4/5 specialist chapters. It covers every topic in the ABET aeronautical and astronautical program criteria and every aerospace-relevant area of the NASA Technology Taxonomy. It is weighted towards rockets and spacecraft, which the project's space roadmaps depend on. Aeronautics still gets a full degree's worth of coverage.

## 2. Sources checked

- ABET, *Criteria for Accrediting Engineering Programs 2025–2026*, Aerospace program criteria: https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2025-2026/
- MIT Course 16 (AeroAstro) subject listing: https://catalog.mit.edu/subjects/16/
- Georgia Tech AE course catalogue (undergraduate and graduate): https://catalog.gatech.edu/coursesaz/ae/
- Purdue AAE degree map and course list: https://engineering.purdue.edu/AAE/academics/undergraduate/pos/2025_2026_aae_degree_map and https://engineering.purdue.edu/AAE/academics/course-descriptions
- Stanford Aeronautics & Astronautics courses: https://bulletin.stanford.edu/departments/AEROASTRO/courses
- NASA 2020 Technology Taxonomy (TX01–TX17, levels 2 and 3 extracted from the PDF): https://www.nasa.gov/wp-content/uploads/2015/03/2020_nasa_technology_taxonomy_lowres.pdf
- NASA Systems Engineering Handbook, SP-2016-6105 Rev 2: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
- Curtis, *Orbital Mechanics for Engineering Students* (table of contents): https://www.sciencedirect.com/book/9780080977478/orbital-mechanics-for-engineering-students
- Sutton & Biblarz, *Rocket Propulsion Elements*, 9th ed.: https://www.wiley.com/en-us/Rocket+Propulsion+Elements,+9th+Edition-p-9781118753651
- Anderson, *Fundamentals of Aerodynamics*, 6th ed. (table of contents): https://catdir.loc.gov/catdir/toc/ecip0513/2005015910.html
- Wertz, Everett & Puschell, *Space Mission Engineering: The New SMAD*: https://books.google.com/books/about/Space_Mission_Engineering.html?id=4JM7tAEACAAJ
- Fortescue, Swinerd & Stark, *Spacecraft Systems Engineering*, 4th ed.: https://onlinelibrary.wiley.com/doi/book/10.1002/9781119971009
- NAR and Tripoli safety codes, and FAA 14 CFR Part 101 (for the amateur rocketry on-ramp chapter)

## 3. Coverage checklist

| Area (source) | Chapters | Status |
|---|---|---|
| Intro to aerospace / how things fly (MIT 16.00, Stanford AA 100, GT AE 1601) | ae-introduction-to-aerospace-engineering, ae-principles-of-flight, ae-rocketry-basics, ae-space-and-orbits-at-a-glance, ae-history-of-flight-and-spaceflight | ➕ added |
| Model/amateur rocketry and safety codes | ae-model-and-amateur-rocketry | ➕ added |
| Dynamics (MIT 16.07, GT AE 2220/2221) | ae-aerospace-dynamics | ➕ added |
| Thermodynamics (MIT 16.004, GT AE 2010) | ae-aerospace-thermodynamics | ➕ added |
| Signals and control (MIT 16.002/16.06/16.30) | ae-feedback-control-aerospace | ➕ added (related: el-control-theory, ma-control-theory, ai-control-systems) |
| Computation and instrumentation (MIT 16.C20, GT AE 2610) | ae-computational-methods-aerospace, ae-aerospace-instrumentation | ➕ added |
| **ABET: aerodynamics** (incompressible, compressible, viscous, hypersonic) | ae-aerodynamics-fundamentals, ae-incompressible-aerodynamics, ae-compressible-flow-gas-dynamics, ae-viscous-flow-boundary-layers, ae-applied-aerodynamics-flight-vehicles, ae-hypersonic-aerothermodynamics | ➕ added |
| Experimental aerodynamics, CFD, aeroacoustics (TX15.1) | ae-experimental-aerodynamics, ae-computational-fluid-dynamics, ae-unsteady-aerodynamics-aeroacoustics | ➕ added |
| **ABET: flight mechanics; stability and control** | ae-aircraft-performance, ae-aircraft-stability-control, ae-flight-dynamics, ae-flight-control-systems | ➕ added |
| Aircraft, rotorcraft and UAV design (GT AE 4311/4331) | ae-aircraft-design, ae-rotorcraft-engineering, ae-uav-drone-engineering, ae-electric-aircraft-advanced-air-mobility | ➕ added |
| Air traffic management (TX16) | ae-air-transportation-traffic-management | ➕ added (optional) |
| **ABET: structures, aerospace materials; space structures** | ae-aerospace-materials, ae-aerospace-structures, ae-structural-dynamics-vibration, ae-finite-element-analysis-aerospace, ae-composite-structures, ae-fatigue-fracture-damage-tolerance, ae-lightweight-structural-design, ae-spacecraft-structures-mechanisms | ➕ added |
| Aeroelasticity (TX15.1.3, GT AE 4220) | ae-aeroelasticity | ➕ added |
| Manufacturing and NDE (TX12.4) | ae-aerospace-manufacturing | ➕ added |
| **ABET: propulsion** (air-breathing, TX01.3) | ae-combustion-fundamentals, ae-gas-turbine-engines, ae-propellers-piston-electric-propulsion, ae-turbomachinery, ae-ramjets-scramjets-combined-cycle | ➕ added |
| **ABET: rocket propulsion** (Sutton chapters 1–22; TX01.1) | ae-rocket-propulsion-fundamentals, ae-rocket-propellants-performance, ae-rocket-nozzles-thrust-vector-control, ae-liquid-rocket-engines, ae-engine-cycles-turbopumps-feed-systems, ae-combustion-instability, ae-solid-rocket-motors, ae-hybrid-rocket-propulsion | ➕ added |
| Propulsion testing (TX13.2.2, Sutton chapter 22) | ae-propulsion-testing | ➕ added |
| Electric, nuclear and advanced propulsion (TX01.2, TX01.4) | ae-electric-propulsion, ae-nuclear-propulsion, ae-advanced-propulsion-concepts | ➕ added |
| **ABET: orbital mechanics** (Curtis chapters 1–8 and 12) | ae-orbital-mechanics, ae-orbital-maneuvers, ae-orbital-perturbations, ae-interplanetary-trajectories, ae-constellations-coverage-analysis, ae-orbit-determination, ae-rendezvous-proximity-operations | ➕ added (related: ph-classical-mechanics) |
| Three-body problem, trajectory optimisation | ae-three-body-problem, ae-trajectory-optimization | ➕ added |
| Launch vehicles and ascent (Curtis chapter 11; TX13.3) | ae-ascent-trajectories, ae-launch-vehicle-design, ae-launch-vehicle-dynamics-control, ae-launch-operations-range-safety, ae-reusable-launch-systems | ➕ added |
| Entry, descent and landing (TX09, TX14.3) | ae-atmospheric-entry, ae-thermal-protection-systems, ae-descent-landing-systems | ➕ added |
| **ABET: space environment** | ae-space-environment | ➕ added (related: ph-space-physics) |
| **ABET: attitude determination and control** (Curtis chapters 9–10; TX17.3/17.4) | ae-attitude-kinematics-dynamics, ae-attitude-determination, ae-attitude-control | ➕ added |
| GNC (TX17) | ae-estimation-kalman-filtering, ae-aerospace-navigation-systems, ae-guidance-algorithms, ae-gnc-system-design-verification | ➕ added |
| Spacecraft subsystems (Fortescue, SMAD; TX03, TX14.2) | ae-spacecraft-bus-fundamentals, ae-spacecraft-power-systems, ae-spacecraft-thermal-control, ae-command-data-handling, ae-spacecraft-propulsion-systems, ae-space-payloads-remote-sensing | ➕ added |
| **ABET: telecommunications** (TX05.1–5.5) | ae-space-communications-link-budgets | ➕ added (related: el-satellite-communication) |
| Avionics and flight software (TX02, TX11.1) | ae-avionics-systems-integration, ae-flight-software | ➕ added (built on el-avionics-systems; related: el-avionics-buses-protocols, el-spacecraft-electronics) |
| Autonomy (TX10) | ae-autonomy-onboard-decision-making | ➕ added |
| Mission design, spacecraft design (SMAD; GT AE 4321/4322) | ae-space-mission-design, ae-spacecraft-design | ➕ added |
| Mission operations and ground segment (TX07.3, TX13.4) | ae-mission-operations-ground-systems | ➕ added |
| Small satellites / CubeSats | ae-small-satellites-cubesats | ➕ added |
| Human spaceflight and life support (TX06; MIT 16.423) | ae-human-spaceflight-life-support | ➕ added |
| Planetary exploration: rovers, landers, sample return (TX04.2, TX07) | ae-planetary-exploration-systems | ➕ added |
| ISRU and surface systems (TX07.1) | ae-space-resources-surface-systems | ➕ added |
| In-space servicing, assembly and manufacturing (TX07.2, TX12.3) | ae-in-space-servicing-assembly-manufacturing | ➕ added |
| SSA and orbital debris (TX05.6) | ae-space-situational-awareness-debris | ➕ added |
| Systems engineering (NASA SE Handbook) | ae-aerospace-systems-engineering, ae-model-based-systems-engineering, ae-multidisciplinary-design-optimization | ➕ added |
| Integration and test (TX13.2; Fortescue AIT chapter) | ae-spacecraft-assembly-integration-test | ➕ added |
| Flight testing (TX15.2.3; MIT 16.64) | ae-flight-testing | ➕ added |
| Safety, reliability, certification (MIT 16.63; GT AE 4376) | ae-aerospace-safety-reliability, ae-airworthiness-certification | ➕ added |
| Space policy, law and business | ae-space-policy-law, ae-space-business-economics | ➕ added (optional) |
| Robotics (TX04 manipulation/HRI) | robotics lives in `ai`; aerospace-specific parts are in planetary exploration and OSAM | ⚠️ partial by design |
| Human health and medicine (TX06.3) | one topic block in ae-human-spaceflight-life-support | ⚠️ partial: space medicine belongs to biology/medicine |
| Exascale and ground computing (TX11.6) | none | ⛔ out of scope: computing, not aerospace engineering |
| Weapons and missile warheads | none; only missile aerodynamics and proportional navigation | ⛔ out of scope: defence-specific |
| Propellant synthesis and formulation recipes | propellants covered conceptually only | ⛔ out of scope by design (safety) |

## 4. Grouping

The categories below are new; there were no existing chapters to move. They run from foundational to applied:

1. Introduction to Aerospace (level-1 on-ramp)
2. Engineering Foundations
3. Aerodynamics
4. Flight Mechanics & Control
5. Air Vehicle Design
6. Structures & Materials
7. Air-Breathing Propulsion & Combustion
8. Rocket Propulsion
9. Space & Advanced Propulsion
10. Orbital Mechanics & Astrodynamics
11. Launch Vehicles
12. Entry, Descent & Landing
13. Spacecraft Subsystems
14. Guidance, Navigation & Control
15. Avionics & Flight Software
16. Space Missions & Exploration
17. Systems Engineering, Test & Safety
18. Space Policy & Business

Within each category, chapters are ordered by level and then by teaching order.

## 5. What was added

All 109 chapters are new. Some points worth knowing:

- **Rocket propulsion is split finely**, following Sutton's structure and the rocket-science focus. It has separate chapters for propellants and thermochemistry, nozzles and TVC, liquid engines, engine cycles and turbopumps, combustion instability, solids, hybrids, testing, electric, nuclear and advanced propulsion.
- **Astrodynamics** follows Curtis and graduate courses (GT AE 6353/6357). It runs from the two-body problem through perturbations, OD, RPO, the three-body problem and trajectory optimisation.
- **Propellants are conceptual only**: selection, performance and hazards. There are no formulations. The amateur rocketry chapter stresses the safety codes, certification and licensing.
- **Level-1 on-ramp**: six chapters need only high-school maths.

## 6. Learning-order notes

- **Rocket and space spine:** How Rockets Work and Space & Orbits at a Glance → Dynamics, Thermodynamics, Control → Rocket Propulsion Fundamentals and Orbital Mechanics → Propellants, Nozzles → Liquid Engines → Ascent Trajectories → Launch Vehicle Design; in parallel, Space Environment → Spacecraft Systems → subsystems → Attitude Dynamics/Determination/Control → Space Mission Design → Spacecraft Design.
- **Aeronautics spine:** Principles of Flight → Aerodynamics Fundamentals → Incompressible Aerodynamics → Performance → Stability & Control → Flight Dynamics → Aircraft Design (together with Structures and Gas Turbines).
- The external prerequisites are ma-calculus, ma-linear-algebra, ma-ordinary-differential-equations-odes, ma-probability-theory, ph-classical-mechanics, ph-classical-electromagnetism, ph-classical-optics, el-circuit-theory, el-signal-processing-fundamentals and el-avionics-systems. Specialist chapters also use ma-numerical-solutions-of-pdes, ma-dynamical-systems, ma-calculus-of-variations-optimal-control, ma-nonlinear-programming and ph-nuclear-physics.

## 7. Recommended moves and open questions

- **ph-fluid-mechanics is level 3**, so it can't sit under the level-2 ae-aerodynamics-fundamentals. That chapter depends on ph-classical-mechanics and teaches the fluid basics itself (it lists ph-fluid-mechanics as `related`). Once the mechanical discipline has a level-2 fluid mechanics chapter, that should become the prerequisite.
- **Overlaps kept on purpose** (linked with `related`):
  - ae-feedback-control-aerospace overlaps el-control-theory, ma-control-theory and ai-control-systems. It is kept because aerospace courses teach control with flight examples, and the aerospace roadmap needs it inside the discipline.
  - The electronics chapters el-space-satellite-systems and el-spacecraft-electronics are thin summaries of subsystems that are covered in depth here.
- **Possible legacy clean-up:** ph-classical-mechanics has an "Orbital mechanics" topic, and el-space-satellite-systems has "Orbital mechanics and attitude control". Those topics could point to ae-orbital-mechanics and ae-attitude-control, since these chapters now cover the subjects in depth.

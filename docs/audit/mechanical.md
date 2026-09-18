# Audit: Mechanical Engineering (`mechanical`, prefix `me`)

## 1. Verdict

**Before:** the discipline did not exist. The file was an empty stub with no description and no chapters.
**Now:** 75 chapters with 913 topics and 15 sub-topics (928 items in total) in 19 categories. They run from a level-1 on-ramp (intro to engineering design, how machines work, workshop practice, engineering drawing) to level-5 frontiers (soft robotics, mechanical metamaterials). Every knowledge area in the NCEES FE Mechanical specification and in all three PE Mechanical specifications maps to at least one chapter. So do both ABET "thermal and mechanical systems" requirements and the core and elective course lists of MIT, Georgia Tech and Purdue. The owner's Iron Man suit and robotics goals get dedicated chapters: fluid power, actuators and drive trains, lightweight structures, wearable mechanisms and exoskeletons, compact-system thermal management, and energy-storage integration.

## 2. Sources checked

- ABET, *Criteria for Accrediting Engineering Programs 2025-2026*, Mechanical program criteria: https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2025-2026/
- NCEES FE Mechanical CBT exam specifications (14 knowledge areas): https://ncees.org/wp-content/uploads/FE-Mechanical-CBT-specs.pdf
- NCEES PE Mechanical: Machine Design & Materials specifications: https://ncees.org/wp-content/uploads/MDM_Apr-2020_CBT.pdf
- NCEES PE Mechanical: Thermal & Fluid Systems specifications: https://ncees.org/wp-content/uploads/TF_Apr-2020_CBT.pdf
- NCEES PE Mechanical: HVAC & Refrigeration specifications: https://ncees.org/wp-content/uploads/HVAC-Apr-2020_CBT.pdf
- NCEES PE Mechanical overview: https://ncees.org/exams/pe-exam/mechanical
- ASME Vision 2030 (curriculum recommendations: design/build spine, practice-based learning, codes and standards, professional skills): https://www.asme.org/asme-programs/students-and-faculty/engineering-education/strategy-vision-2030 and https://peer.asee.org/asme-vision-2030-s-recommendations-for-mechanical-engineering-education.pdf
- MIT Course 2 subject listing (2.00x core, 2.03x dynamics, 2.07x solid mechanics, 2.09x computation, 2.1xx robotics/control/instrumentation): https://catalog.mit.edu/subjects/2/
- Georgia Tech ME undergraduate course catalog: https://catalog.gatech.edu/courses-undergrad/me/
- Purdue ME graduate courses by area of interest (acoustics, fluid power, tribology, motorsports, robotics, HVAC, and more): https://engineering.purdue.edu/ME/Graduate/OnCampus/Registration/Courses
- Standard textbook tables of contents used as syllabus checks: Hibbeler (*Statics*, *Dynamics*, *Mechanics of Materials*), Cengel & Boles (*Thermodynamics*), Incropera (*Heat and Mass Transfer*), Fox & McDonald / White (*Fluid Mechanics*), Shigley (*Mechanical Engineering Design*), Norton (*Design of Machinery*), Rao (*Mechanical Vibrations*), Kalpakjian (*Manufacturing Engineering and Technology*), Lynch & Park (*Modern Robotics*), Ulrich & Eppinger (*Product Design and Development*), Ashby (*Materials Selection in Mechanical Design*).

## 3. Coverage checklist

| Taxonomy area (source) | Chapter(s) | Status |
|---|---|---|
| Intro to engineering, units, problem solving (MIT 2.00, GT ME 1670) | `me-introduction-to-engineering-mechanical-design`, `me-how-machines-work` | ➕ added |
| Workshop / hands-on practice (ASME Vision 2030 "practice-based") | `me-workshop-practice-hand-tools` | ➕ added |
| FE 1: Mathematics (numerical methods, algorithms) | `me-engineering-computation` + math chapters (`ma-calculus`, ODEs, linear algebra) | ➕ added |
| FE 2: Probability & statistics | math chapters as prerequisites; applied in `me-measurements-instrumentation`, `me-reliability-safety-engineering`, `me-manufacturing-systems-quality` | ✅ covered (via math) |
| FE 3: Ethics & professional practice; ASME codes & standards emphasis | `me-professional-practice-engineering-economics` | ➕ added |
| FE 4: Engineering economics | `me-professional-practice-engineering-economics` | ➕ added |
| FE 5: Electricity & magnetism, motors | `el-circuit-theory` (prerequisite), `me-system-dynamics`, `me-mechatronics` | ✅ covered (via electronics) |
| FE 6: Statics | `me-statics` | ➕ added |
| FE 7: Dynamics, kinematics, vibrations | `me-dynamics`, `me-kinematics-of-mechanisms`, `me-mechanical-vibrations` | ➕ added |
| FE 8: Mechanics of materials | `me-mechanics-of-materials`, `me-advanced-mechanics-of-materials` | ➕ added |
| FE 9: Material properties & processing | `me-engineering-materials`, `me-materials-selection`, `me-manufacturing-processes` | ➕ added |
| FE 10: Fluid mechanics (incl. compressible, pumps, scaling laws) | `me-fluid-mechanics`, `me-advanced-fluid-mechanics`, `me-turbomachinery` | ➕ added |
| FE 11: Thermodynamics (cycles, psychrometrics, combustion) | `me-engineering-thermodynamics`, `me-applied-thermodynamics` | ➕ added |
| FE 12: Heat transfer | `me-heat-transfer` | ➕ added |
| FE 13: Measurements, instrumentation & controls | `me-measurements-instrumentation`, `me-system-dynamics`, `me-feedback-control` | ➕ added |
| FE 14: Mechanical design & analysis (springs, bearings, screws, power transmission, joining, fits, GD&T, hydraulic/pneumatic components) | `me-machine-design-fundamentals`, `me-shafts-bearings-seals`, `me-gears-power-transmission`, `me-fasteners-joints-springs`, `me-tolerancing-gdt-metrology`, `me-hydraulics-pneumatics` | ➕ added |
| PE MDM: pressure vessels & piping | `me-pressure-vessels-piping` | ➕ added |
| PE MDM: dampers, clutches, brakes, belts, chains, mechanisms, basic mechatronics | `me-gears-power-transmission`, `me-kinematics-of-mechanisms`, `me-dynamics-of-machinery`, `me-mechatronics` | ➕ added |
| PE MDM: welding, bolts, adhesives | `me-fasteners-joints-springs`, `me-welding-joining` | ➕ added |
| PE MDM: FEA/CAE and their limitations | `me-finite-element-analysis` | ➕ added |
| PE MDM: QA/QC, design methodology, risk | `me-manufacturing-systems-quality`, `me-product-design-development`, `me-reliability-safety-engineering` | ➕ added |
| PE TFS: hydraulic & fluid equipment, distribution systems, control valves, actuators | `me-thermal-fluid-systems-design`, `me-hydraulics-pneumatics`, `me-turbomachinery` | ➕ added |
| PE TFS: turbines, boilers, IC engines, cooling towers, combined cycles, energy recovery | `me-power-plants-energy-conversion`, `me-internal-combustion-engines`, `me-thermal-fluid-systems-design` | ➕ added |
| PE HVAC: loads, psychrometrics, equipment, air/fluid distribution, refrigeration, controls, IAQ, acoustics | `me-hvac-refrigeration`, `me-acoustics-noise-control` | ➕ added |
| Engineering graphics / CAD (GT ME 1670, ME 4042) | `me-engineering-drawing-sketching`, `me-cad-solid-modeling` | ➕ added |
| Manufacturing: machining, casting, forming, welding, AM (MIT 2.008, GT ME 4215) | `me-machining-processes`, `me-casting-forming-molding`, `me-welding-joining`, `me-additive-manufacturing` | ➕ added |
| CNC / CAM | `me-cnc-cam` | ➕ added |
| DFM/DFA (Purdue ME 557) | `me-design-for-manufacture-assembly` | ➕ added |
| Product development and design spine (MIT 2.009, ASME Vision 2030) | `me-product-design-development` | ➕ added |
| System dynamics (GT ME 3017, MIT 2.003) | `me-system-dynamics` | ➕ added |
| Advanced dynamics (MIT 2.032, Purdue ME 562) | `me-advanced-dynamics-multibody` | ➕ added |
| Continuum mechanics, elasticity, plasticity (MIT 2.071-2.074) | `me-continuum-mechanics-elasticity-plasticity` | ➕ added |
| Fatigue & fracture (engineering side) | `me-fatigue-fracture-creep` | ➕ added |
| Composites, lightweight structures (GT ME 4791, Purdue lightweight vehicle structures) | `me-lightweight-structures-composites` | ➕ added |
| Tribology (Purdue ME 556, GT ME 4193) | `me-tribology` | ➕ added |
| Precision / compliant mechanisms (MIT 2.145, 2.75) | `me-precision-design-compliant-mechanisms` | ➕ added |
| Vibrations, structural dynamics, rotordynamics (MIT 2.060, Purdue ME 563/664) | `me-mechanical-vibrations`, `me-advanced-vibrations-rotordynamics` | ➕ added |
| Acoustics & noise control (GT ME 4760, Purdue ME 513) | `me-acoustics-noise-control` | ➕ added |
| Control systems (MIT 2.14, 2.151-2.153) | `me-feedback-control` (with intro topics on LQR/MPC/robust/adaptive); deeper theory lives in `el-control-theory` and `ma-control-theory` | ✅ covered |
| Mechatronics (GT ME 4405, Purdue ME 588) | `me-mechatronics` | ➕ added |
| Robotics mechanics & mechanism design (MIT 2.12, Purdue ME 572) | `me-robot-mechanics`, `me-robot-mechanism-design` | ➕ added |
| Actuators & drive trains (owner goal) | `me-actuators-drive-trains`, `me-smart-materials-artificial-muscles` | ➕ added |
| Fluid power (Purdue ME 535; owner goal) | `me-hydraulics-pneumatics`, `me-servo-hydraulics-advanced-fluid-power` | ➕ added |
| Wearable mechanisms / exoskeletons, human-machine joints (owner goal) | `me-wearable-mechanisms-exoskeletons`, `me-biomechanics` | ➕ added |
| Thermal management of compact power (owner goal; Purdue ME 511, GT ME 4754) | `me-thermal-management-compact-power` | ➕ added |
| Power-dense energy storage (owner goal; GT ME 4759, 4325) | `me-energy-storage-power-integration` | ➕ added |
| FEA, CFD (MIT 2.095-2.097, GT ME 4342) | `me-finite-element-analysis`, `me-computational-fluid-dynamics` | ➕ added |
| Design optimization and topology optimization (MIT 2.083) | `me-design-optimization` | ➕ added |
| Reliability (Purdue ME 571, GT ME 4725) | `me-reliability-safety-engineering` | ➕ added |
| Combustion (Purdue ME 525) | `me-combustion-engineering` | ➕ added |
| IC engines, turbomachinery, power plants, renewables (GT ME 4011, 4324, 4332; Purdue ME 533) | `me-internal-combustion-engines`, `me-turbomachinery`, `me-power-plants-energy-conversion`, `me-renewable-energy-systems` | ➕ added |
| Automotive & vehicle dynamics (GT ME 4014, Purdue ME 565 / motorsports) | `me-automotive-engineering`, `me-vehicle-dynamics` | ➕ added |
| Biomechanics (GT ME 4758, Purdue ME 577) | `me-biomechanics` | ➕ added |
| Frontier: soft robotics, metamaterials, micro/nano mechanics, ML (MIT 2.075, 2.0911; Purdue ME 539) | `me-soft-robotics-mechanics`, `me-mechanical-metamaterials`, `me-micro-nano-mechanics`, `me-machine-learning-digital-twins` | ➕ added |
| Rocket propulsion, aircraft/spacecraft structures, flight mechanics, orbital mechanics | none | ⛔ out of scope: owned by the separate aerospace discipline |
| Materials science in depth (crystallography, metallurgy, polymer science) | intro only (`me-engineering-materials`) | ⛔ out of scope: owned by the materials discipline |
| Naval architecture / ocean engineering (MIT 2.016, 2.019), nuclear reactor engineering, pulp & paper | none (power-plant overview topics only) | ⛔ out of scope: separate engineering disciplines |
| PLC programming | covered by `el-plc-programmable-logic-controller-programming`; linked from `me-manufacturing-systems-quality` | ✅ covered (electronics) |

## 4. Grouping

This is a new discipline, so nothing was moved. The 19 categories run from foundational to applied:

1. Foundations & Professional Practice
2. Engineering Graphics, CAD & Tolerancing
3. Engineering Mechanics
4. Engineering Materials
5. Solid Mechanics & Structures
6. Thermal-Fluid Sciences
7. System Dynamics, Measurement & Control
8. Vibrations & Acoustics
9. Mechanisms & Kinematics of Machinery
10. Machine Design & Machine Elements
11. Manufacturing Engineering
12. Computational Engineering & Simulation
13. Design Methodology, Product Development & Reliability
14. Fluid Power
15. Mechatronics & Robotics
16. Biomechanics & Wearable Systems
17. Energy & Power Systems
18. Automotive & Vehicle Engineering
19. Frontiers of Mechanical Engineering

Fluid Power, Biomechanics & Wearable Systems, and the compact-power chapters in Energy & Power Systems are separate from the standard ME core on purpose. That makes the Iron Man suit and robotics roadmap easy to assemble.

## 5. What was added

All 75 chapters are new: 25 core, 34 important and 16 advanced. By level: 4 at level 1, 11 at level 2, 39 at level 3, 19 at level 4 and 2 at level 5. Chapters driven by the owner's goals:

- `me-hydraulics-pneumatics` and `me-servo-hydraulics-advanced-fluid-power`: EHAs, compact high-pressure hydraulics for legged robots and exoskeletons.
- `me-actuators-drive-trains`: quasi-direct drive, series elastic actuators, harmonic and cycloidal reducers, cable drives, inertia matching.
- `me-lightweight-structures-composites`: thin-walled and sandwich structures, laminates, lattices, crash energy absorption.
- `me-wearable-mechanisms-exoskeletons`: joint alignment, physical human-robot interface, power and thermal budgets for full-body suits.
- `me-thermal-management-compact-power`: cold plates, heat pipes, phase-change materials, skin-contact thermal limits.
- `me-energy-storage-power-integration`: pack mechanics, thermal runaway, structural batteries, compact power sources, mission power budgets.
- `me-smart-materials-artificial-muscles` and `me-soft-robotics-mechanics`.

## 6. Learning-order notes

- **Mechanics spine:** Intro to Engineering → Statics → Mechanics of Materials → Machine Design → Shafts/Gears/Fasteners → Product Design.
- **Dynamics and control spine:** Statics → Dynamics → System Dynamics → Vibrations / Feedback Control → Mechatronics → Actuators & Drive Trains → Robot Mechanism Design → Wearable Exoskeletons.
- **Thermal-fluids spine:** Thermodynamics → Fluid Mechanics → Heat Transfer → Applied Thermodynamics → Thermal Systems Design → HVAC / Power / Compact Thermal Management.
- **Manufacturing spine:** Drawing → CAD → Engineering Materials → Manufacturing Processes → Machining → CNC/CAM, with Tolerancing/GD&T feeding Manufacturing Systems & Quality.
- The longest prerequisite chain in the discipline has 9 stages.

## 7. Recommended moves and open questions

- **Physics on-ramp:** `me-statics` and `me-dynamics` list `ph-classical-mechanics` as `related`, not as a prerequisite. That chapter includes Lagrangian and Hamiltonian mechanics, which is too heavy for a first engineering-mechanics course. If the physics agent adds an introductory mechanics chapter, it should become a prerequisite of `me-statics`.
- `me-mechanical-vibrations` lists both `me-system-dynamics` (which needs `ma-ordinary-differential-equations-odes`) and `ma-linear-algebra`. If the math discipline makes ODEs depend on linear algebra, the validator will flag `ma-linear-algebra` as redundant. It is safe to drop it then.
- Control theory exists in three places (`el-control-theory`, `ma-control-theory`, `me-feedback-control`). The ME chapter keeps the mechanical-systems focus, and the three are linked with `related`.
- Robot kinematics overlaps with `ai-kinematics-dynamics` and `el-kinematics-dynamics`. `me-robot-mechanics` is the rigorous mechanics version (screw theory, statics, dynamics, parallel mechanisms), linked with `related`.
- **Phase B cross-links wanted** (targets did not exist yet):
  - `me-engineering-materials` → introductory chemistry (chemistry) as prerequisite; materials-science fundamentals (materials) as related
  - `me-fatigue-fracture-creep` → mechanical behaviour / fracture of materials (materials), related
  - `me-lightweight-structures-composites` → composite materials (materials) and aerospace structures (aerospace), related
  - `me-materials-selection`, `me-tribology`, `me-welding-joining`, `me-additive-manufacturing`, `me-casting-forming-molding` → matching materials-processing, surface-engineering and metallurgy chapters (materials), related
  - `me-smart-materials-artificial-muscles`, `me-mechanical-metamaterials`, `me-micro-nano-mechanics` → functional, architected and nano materials (materials), related
  - `me-advanced-fluid-mechanics`, `me-computational-fluid-dynamics` → gas dynamics / aerodynamics / CFD (aerospace), related
  - `me-turbomachinery`, `me-combustion-engineering` → jet and rocket propulsion (aerospace), related
  - `me-advanced-dynamics-multibody` → flight dynamics and spacecraft attitude dynamics (aerospace), related
  - `me-advanced-vibrations-rotordynamics` → aeroelasticity (aerospace), related
  - `me-thermal-management-compact-power` → spacecraft thermal control (aerospace), related
  - `me-energy-storage-power-integration` → electrochemistry (chemistry), prerequisite
  - `me-combustion-engineering` → chemical kinetics (chemistry), prerequisite
  - `me-biomechanics` → human anatomy and physiology (biology), prerequisite
  - `me-engineering-computation` → programming fundamentals (cs), related or prerequisite

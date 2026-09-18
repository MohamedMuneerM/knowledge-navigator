# Audit: Materials Science & Engineering (`materials`, prefix `mt`)

## 1. Verdict

**Before:** the discipline was an empty stub with 0 chapters. Some materials topics were scattered across physics (`ph-materials-physics`, `ph-solid-state-physics`, `ph-soft-matter-physics`) and electronics (`el-advanced-materials`, `el-cmos-technology`, `el-battery-technologies`).

**Now:** 83 chapters and about 1,010 topics in 20 categories. The discipline runs from a level-1 "Introduction to Materials" to frontier research. It covers everything in Callister's textbook, Ashby's materials-selection book, the ABET program criteria, the MIT DMSE core and the TMS/MRS technical areas. It also goes deeper into the owner's goal areas: aerospace and extreme-environment materials, lightweight and protective structures, energy materials and smart materials.

## 2. Sources checked

- ABET, Criteria for Accrediting Engineering Programs 2025-2026, Materials/Metallurgical/Ceramics program criteria: https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2025-2026/
- MIT Course Catalog, Course 3 subject listing (3.001 to 3.23): https://catalog.mit.edu/subjects/3/
- MIT Course 3 SB degree chart (the required core: 3.010, 3.013, 3.020, 3.023, 3.029, 3.030, 3.033, 3.042, 3.044): https://catalog.mit.edu/degree-charts/materials-science-engineering-course-3/
- Callister & Rethwisch, *Materials Science and Engineering: An Introduction*, 10th ed. (22 chapters): https://www.wiley.com/en-us/Materials+Science+and+Engineering:+An+Introduction,+10th+Edition-p-9781119405498 and https://www.perlego.com/book/1504087/materials-science-and-engineering-an-introduction-pdf
- Ashby, *Materials Selection in Mechanical Design*, 5th ed., table of contents: https://shop.elsevier.com/books/materials-selection-in-mechanical-design/ashby/978-0-08-100599-6
- TMS divisions and technical committees: https://www.tms.org/portal/portal/Divisions___Committees/Divisions___Committees1.aspx
- MRS Fall 2025 topical clusters (via the MRS Meeting Scene summary): https://mrsmeetingscene.substack.com/p/the-2025-mrs-fall-meeting-and-exhibit and https://www.mrs.org/meetings-events/annual-meetings/2025-mrs-fall-meeting/symposium-sessions

## 3. Coverage checklist

| Taxonomy area (source) | Chapter(s) | Status |
|---|---|---|
| Structure, properties, processing and performance (ABET element i) | `mt-intro-to-materials` and the structure, mechanical and processing categories | ➕ added |
| Selection and design of materials and processes (ABET ii) | `mt-materials-selection`, `mt-lightweight-structures` | ➕ added |
| Experimental, statistical and computational methods (ABET iii) | `mt-characterization-fundamentals` (statistics, DOE, Weibull), the characterization category, the computational category | ➕ added |
| Callister 1: Introduction | `mt-intro-to-materials`, `mt-materials-history-society` | ➕ added |
| Callister 2: Atomic structure and bonding (MIT 3.091) | `mt-atomic-bonding` | ➕ added |
| Callister 3: Crystal structures (MIT 3.010) | `mt-crystal-structures`, `mt-crystallography-diffraction` | ➕ added |
| Callister 4: Imperfections | `mt-defects` | ➕ added |
| Callister 5: Diffusion | `mt-diffusion` | ➕ added |
| Callister 6-8: Mechanical properties, dislocations and strengthening, failure (MIT 3.013, 3.22) | `mt-mechanical-properties`, `mt-plasticity-strengthening`, `mt-creep`, `mt-fracture-mechanics`, `mt-fatigue-failure-analysis` | ➕ added |
| Callister 9-10: Phase diagrams and transformations (MIT 3.020, 3.030, 3.20, 3.21) | `mt-thermodynamics-of-materials`, `mt-phase-diagrams`, `mt-phase-transformations`, `mt-interfaces-microstructure-evolution` | ➕ added |
| Callister 11: Metal alloys (MIT 3.14; TMS Steels, Titanium, High-Temperature Alloys, Refractory committees) | `mt-steels`, `mt-nonferrous-alloys`, `mt-superalloys-refractory`, `mt-heat-treatment` | ➕ added |
| Callister 12-13: Ceramics (MIT 3.07, 3.071) | `mt-ceramics`, `mt-glasses`, `mt-construction-materials`, `mt-powder-processing` | ➕ added |
| Callister 14-15: Polymers (MIT 3.063, 3.064) | `mt-polymer-structure`, `mt-polymer-properties`, `mt-polymer-processing`, `mt-soft-materials` | ➕ added |
| Callister 16: Composites (TMS Composite Materials) | `mt-composites`, `mt-fibre-composites-mechanics-manufacturing`, `mt-ceramic-matrix-composites` | ➕ added |
| Callister 17: Corrosion and degradation (TMS Corrosion committee) | `mt-electrochemistry`, `mt-corrosion`, `mt-high-temperature-oxidation` | ➕ added |
| Callister 18-21: Electrical, thermal, magnetic and optical properties (MIT 3.033, 3.15, 3.152, 3.156) | `mt-electronic-properties`, `mt-semiconductor-materials`, `mt-dielectric-ferroic`, `mt-magnetic-materials`, `mt-optical-photonic-materials`, `mt-thermal-properties` | ➕ added |
| Callister 22: Environmental and societal issues (MIT 3.081; TMS Recycling) | `mt-sustainability-lca` | ➕ added |
| Ashby 1-5, 8-11: Property charts, indices, multiple constraints, shape | `mt-materials-selection` | ➕ added |
| Ashby 6-7: Process selection and cost | `mt-materials-selection` (process topics) plus the processing category | ➕ added |
| Ashby 12-13: Hybrid materials | `mt-lightweight-structures` | ➕ added |
| Ashby 14, 16: Environment and sustainability | `mt-sustainability-lca` | ➕ added |
| Ashby 15: Industrial design | `mt-materials-selection` (topic) | ➕ added |
| Materials processing (MIT 3.044, 3.17; TMS MPMD) | `mt-casting-solidification`, `mt-deformation-processing`, `mt-heat-treatment`, `mt-powder-processing`, `mt-polymer-processing`, `mt-joining`, `mt-thin-films-coatings`, `mt-additive-manufacturing` | ➕ added |
| Extraction and processing (TMS EPD: pyro-, hydro-, electrometallurgy) | `mt-extractive-metallurgy` | ➕ added |
| Characterization (MIT 3.040, 3.074; MRS cluster; TMS Characterization) | `mt-characterization-fundamentals`, `mt-xray-neutron-methods`, `mt-electron-microscopy`, `mt-surface-spectroscopy-probe`, `mt-thermal-analysis`, `mt-nondestructive-evaluation` | ➕ added |
| Tribology and wear | `mt-tribology` | ➕ added |
| Nanomaterials (MIT 3.052; TMS Nanomaterials; MRS cluster) | `mt-nanomaterials`, `mt-2d-materials` | ➕ added |
| Biomaterials (MIT 3.051, 3.055; TMS Biomaterials) | `mt-biomaterials`, `mt-biological-bioinspired` | ➕ added |
| Energy materials (MIT 3.18; TMS Energy Conversion and Storage; MRS Energy and Sustainability) | `mt-battery-materials`, `mt-fuel-cell-hydrogen`, `mt-photovoltaic-materials`, `mt-thermoelectric-thermal-energy` | ➕ added |
| Electronic packaging and interconnects (TMS) | `mt-semiconductor-materials` (packaging topics) | ➕ added |
| Smart materials (piezo, SMA, EAP, artificial muscles) | `mt-dielectric-ferroic`, `mt-smart-materials`, `mt-shape-memory-alloys`, `mt-electroactive-polymers-artificial-muscles` | ➕ added |
| Aerospace materials (superalloys, CFRP, TPS, ablatives, CMCs) | `mt-aerospace-materials`, `mt-superalloys-refractory`, `mt-fibre-composites-mechanics-manufacturing`, `mt-ceramic-matrix-composites`, `mt-thermal-protection-systems` | ➕ added |
| Extreme environments (MIT 3.154; TMS Nuclear Materials): cryogenic, high temperature, radiation, space | `mt-cryogenic-materials`, `mt-high-temperature-oxidation`, `mt-radiation-nuclear-materials`, `mt-space-environment-materials` | ➕ added |
| Lightweight structures (MIT 3.054, 3.172) | `mt-lightweight-structures` | ➕ added |
| Impact-resistant and protective materials | `mt-impact-protective-materials` (kept at a conceptual materials-science level) | ➕ added |
| Computational materials (MIT 3.021, 3.041; MRS Theory, Computation and Data Science) | `mt-computational-materials-intro`, `mt-dft`, `mt-molecular-dynamics-monte-carlo`, `mt-calphad-icme`, `mt-phase-field-mesoscale`, `mt-materials-informatics` | ➕ added |
| Frontier: HEAs, 2D, metamaterials, self-healing, quantum materials | `mt-high-entropy-alloys`, `mt-2d-materials`, `mt-metamaterials`, `mt-self-healing-materials`, `mt-emerging-materials` | ➕ added |
| Solid-state physics and band theory in depth | `ph-solid-state-physics` (linked as `related`) | ⛔ out of scope: owned by physics |
| Semiconductor device physics and the CMOS process flow | `el-semiconductor-physics`, `el-cmos-technology` (related) | ⛔ out of scope: owned by electronics |
| Machining and manufacturing systems | one surface-integrity topic in `mt-deformation-processing` | ⛔ out of scope: belongs to mechanical engineering |
| Structural mechanics (beams, FEA of structures) | `ma-solid-mechanics` (related) | ⛔ out of scope: belongs to mechanical engineering |
| Business and innovation (MIT 3.085, 3.086) | none | ⛔ out of scope: business/entrepreneurship is peripheral |

## 4. Grouping

The 20 categories go from foundational to applied:

1. Foundations
2. Structure of Materials
3. Thermodynamics & Kinetics
4. Mechanical Behaviour
5. Electronic, Optical, Magnetic & Thermal Properties
6. Metals & Alloys
7. Ceramics & Glasses
8. Polymers & Soft Matter
9. Composites
10. Materials Characterization
11. Materials Processing & Manufacturing
12. Corrosion, Wear & Degradation
13. Materials Selection, Design & Sustainability
14. Nanomaterials & Biomaterials
15. Energy Materials
16. Smart & Active Materials
17. Aerospace & Extreme-Environment Materials
18. Lightweight & Protective Structures
19. Computational Materials Science
20. Frontier Materials

Grouping decisions:

- **Material classes (categories 6 to 9)** follow Callister's grouping.
- **Application categories (15 to 18)** reflect the owner's goals, so a roadmap can pick a whole block. Two chapters sit in their material-class category even though they are aerospace-critical: superalloys (Metals & Alloys) and CFRP (Composites).
- **Thermal properties** is grouped with the other functional properties but set to level 2, because materials selection depends on it.

## 5. What was added

All 83 chapters are new. Chapters to note:

- **On-ramp:** `mt-intro-to-materials` (L1, core) and `mt-materials-history-society` (L1, optional).
- **Aerospace depth:**
  - `mt-superalloys-refractory` (single-crystal blades, TBCs, C-103 nozzle alloys)
  - `mt-fibre-composites-mechanics-manufacturing` (laminate theory, CAI, AFP, COPVs, cryotanks)
  - `mt-ceramic-matrix-composites` (CVI/PIP/MI, C/C, EBCs)
  - `mt-thermal-protection-systems` (tiles, RCC, PICA/AVCOAT/carbon-phenolic, ablation physics, UHTCs, arc-jet testing)
  - `mt-aerospace-materials` (allowables, MMPDS/CMH-17, qualification)
- **Extreme environments:** `mt-cryogenic-materials` (LH2/LOX tanks, superconducting magnet conductors), `mt-radiation-nuclear-materials`, `mt-space-environment-materials` (atomic oxygen, outgassing, MMOD/Whipple shields), `mt-high-temperature-oxidation`.
- **Iron Man suit direction:**
  - `mt-lightweight-structures` (cellular and architected materials, exoskeleton frames)
  - `mt-impact-protective-materials` (high-rate behaviour, fibre and ceramic protection concepts, helmets; conceptual only)
  - `mt-battery-materials`
  - `mt-smart-materials`, `mt-shape-memory-alloys`, `mt-electroactive-polymers-artificial-muscles`
- **Statistics and experimental methods** (ABET element iii) are topics in `mt-characterization-fundamentals`, not a separate chapter.

## 6. Learning-order notes

**Main spine:** Intro to Materials → Atomic Bonding → Crystal Structures → Defects → Thermodynamics → Phase Diagrams → Diffusion → Phase Transformations → Mechanical Properties → Plasticity → Fracture → Fatigue. The material-class chapters (steels, ceramics, polymers, composites) and processing come next, followed by the applied specialisations.

**Branches:**
- **Functional:** Crystallography + Quantum Mechanics → Electronic Properties → Semiconductors, Dielectrics, Magnetic, Optical → Energy and Smart materials.
- **Aerospace:** Composites + Light Alloys + Fatigue → Aerospace Materials → Space Environment. Composites + Ceramics → CMCs → Thermal Protection Systems.
- **Computational:** Diffusion + Numerical PDEs → Intro Computational → DFT, MD, CALPHAD/ICME, Phase-Field → Informatics.

The prerequisite graph has 9 stages, and every prerequisite is at the same or a lower level.

## 7. Recommended moves and open questions

- **Chapter count:** 83 is above the 40 to 65 guideline. This is deliberate: the owner asked for proper depth in six application areas, which added about 20 specialist chapters. Each one maps to a real course or book section. Candidates to merge if the count must come down:
  - `mt-space-environment-materials` into `mt-radiation-nuclear-materials`
  - `mt-thermal-analysis` into `mt-characterization-fundamentals`
  - `mt-self-healing-materials` into `mt-emerging-materials`
- **Overlap with physics:** `ph-materials-physics` duplicates parts of this discipline (alloys, ceramics, composites, smart materials). It is linked as `related` from several `mt-` chapters. Physics should consider treating it as a pointer to `materials`.
- **Overlap with electronics:** `el-advanced-materials` overlaps with `mt-2d-materials` and `mt-emerging-materials`, and `el-battery-technologies` overlaps with `mt-battery-materials`. They are linked via `related`. The mt chapters take the materials-science view and the el chapters the device view.
- **Phase-B cross-links wanted** (targets don't exist yet):
  - `mt-atomic-bonding` → general and inorganic chemistry (chemistry)
  - `mt-polymer-structure` → organic chemistry and polymer chemistry (chemistry)
  - `mt-electrochemistry` → electrochemistry and physical chemistry (chemistry)
  - `mt-computational-materials-intro` → programming fundamentals in Python (cs)
  - `mt-mechanical-properties` → statics and mechanics of materials (mechanical)
  - `mt-fibre-composites-mechanics-manufacturing` → mechanics of materials / structural analysis (mechanical)
  - `mt-casting-solidification` → heat transfer and fluid mechanics (mechanical)
  - `mt-deformation-processing` and `mt-additive-manufacturing` → manufacturing processes (mechanical)
  - `mt-tribology` → machine elements (mechanical)
  - `mt-impact-protective-materials` → dynamics / FEA (mechanical)
  - `mt-thermal-protection-systems` → aerothermodynamics / hypersonics (aerospace)
  - `mt-aerospace-materials` → aircraft and spacecraft structures (aerospace)
  - `mt-biomaterials` → cell biology (biology)

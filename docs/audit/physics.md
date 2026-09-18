# Physics audit

## 1. Verdict

**Before:** 58 chapters and 501 topics. The research-level coverage was broad, but there was no on-ramp: nothing below calculus-based mechanics. Several standard areas were missing, including waves, AMO, plasma physics, lasers and the graduate-core "advanced" courses. Astronomy was thin: one 14-topic survey chapter plus a few short satellite chapters. No chapter had a level, priority, summary or prerequisites.

**After:** 98 chapters and 1,083 topics in 23 categories. Every chapter has metadata and direct prerequisites. The validator reports zero errors and zero warnings. There is now a level-1 on-ramp for physics and for astronomy, the full undergraduate and graduate core, the PhySH disciplines that were missing, and a 25-chapter astronomy and astrophysics track running from naked-eye observing to cosmological perturbation theory.

## 2. Sources checked

- APS Physics Subject Headings (PhySH), 17 disciplines and 5 facets: https://physh.org/ and https://journals.aps.org/authors/physh
- arXiv category taxonomy (astro-ph, cond-mat, gr-qc, hep, math-ph, nlin, nucl, physics.*, quant-ph): https://arxiv.org/category_taxonomy
- MIT Course 8 subject listing (8.01 to 8.591, undergraduate and graduate core): https://catalog.mit.edu/subjects/8/
- MIT OCW 8.901 Astrophysics I syllabus: https://ocw.mit.edu/courses/8-901-astrophysics-i-spring-2006/pages/syllabus/
- MIT OCW 8.962 General Relativity (graduate): https://ocw.mit.edu/courses/8-962-general-relativity-spring-2020/
- Cambridge Cavendish undergraduate courses (NST Part IA/IB/II physics): https://www.phy.cam.ac.uk/study/undergraduate/undergraduate-courses/
- Cambridge Institute of Astronomy, Part II Astrophysics teaching (Structure and Evolution of Stars, Stellar Dynamics and Galaxies, Astrophysical Fluid Dynamics, Cosmology, Relativity, Statistical Physics): https://www.ast.cam.ac.uk/current-students/undergraduate/part-ii/teaching-and-learning
- Unified Astronomy Thesaurus (AAS), used for the astronomy top-level branches: https://astrothesaurus.org/
- Standard graduate core, as reflected in MIT 8.309/8.311/8.321-322/8.333-334/8.323: classical mechanics, electrodynamics, quantum theory, statistical mechanics and QFT.

## 3. Coverage checklist

| Area (source) | Chapters | Status |
|---|---|---|
| On-ramp: units, measurement, vectors (MIT 8.01 prep, any intro text) | ph-measurement-units-vectors | ➕ added |
| Algebra-based intro physics (mechanics, heat, waves/light, E&M) | ph-introductory-mechanics, ph-introductory-heat-thermodynamics, ph-introductory-waves-sound-light, ph-introductory-electricity-magnetism | ➕ added |
| Classical mechanics (MIT 8.01/8.09/8.309; arXiv physics.class-ph) | ph-classical-mechanics | ✅ covered (canonical transformations, Hamilton-Jacobi, normal modes and non-inertial frames added) |
| Waves & oscillations (MIT 8.03; Cambridge IB Oscillations, Waves and Optics) | ph-waves-oscillations | ➕ added |
| Fluid dynamics (PhySH; physics.flu-dyn) | ph-fluid-mechanics, ph-astrophysical-fluid-dynamics | ✅ / ➕ |
| Acoustics | ph-acoustics | ✅ covered |
| Electromagnetism, undergraduate and graduate (MIT 8.02/8.07/8.311) | ph-classical-electromagnetism, ph-advanced-electrodynamics | ✅ / ➕ |
| Thermal and statistical physics (PhySH Statistical Physics; cond-mat.stat-mech; MIT 8.044/8.333-334) | ph-thermodynamics-statistical-mechanics, ph-advanced-statistical-mechanics | ✅ / ➕ |
| Modern physics bridge course | ph-modern-physics | ➕ added |
| Quantum mechanics, undergraduate and graduate (MIT 8.04-8.06, 8.321-322) | ph-quantum-mechanics, ph-advanced-quantum-mechanics | ✅ (harmonic oscillator, hydrogen atom, Dirac notation added) / ➕ |
| Quantum information (PhySH; quant-ph) | ph-quantum-information-science, ph-quantum-sensing-metrology | ✅ covered |
| QFT and particles & fields (PhySH; hep-th, hep-ph, hep-lat) | ph-quantum-field-theory-qft, ph-particle-physics | ✅ covered |
| Relativity and gravitation (gr-qc; MIT 8.033/8.962) | ph-special-relativity, ph-general-relativity, ph-black-hole-physics, ph-quantum-gravity | ✅ covered |
| String theory (MIT 8.251; hep-th) | ph-string-theory | ➕ added |
| Mathematical physics (math-ph) | ph-mathematical-physics, ph-symmetry-group-theory, ph-advanced-theoretical-methods | ✅ covered. The level-2 "maths methods" content is left to the math discipline and linked via prerequisites and `related` |
| Computational physics (physics.comp-ph) | ph-computational-physics | ✅ covered (ODE/PDE/FFT/N-body/HPC topics added) |
| Data analysis and statistics (physics.data-an; MIT 8.16) | ph-data-analysis-statistics | ➕ added |
| Optics (physics.optics) | ph-classical-optics, ph-modern-optics, ph-quantum-optics, ph-nanophotonics-plasmonics, ph-ultrafast-physics | ✅ covered |
| Laser physics | ph-laser-physics | ➕ added (was one topic in Modern Optics) |
| Atomic, molecular & optical (PhySH AMO; physics.atom-ph; MIT 8.421-422) | ph-atomic-physics, ph-molecular-physics, ph-atom-light-interaction-laser-cooling, ph-cold-atom-physics | ➕ added / ✅ |
| Nuclear physics (nucl-ex, nucl-th) | ph-nuclear-physics | ✅ covered |
| Condensed matter and materials (cond-mat.*) | ph-solid-state-physics, ph-materials-physics, ph-cryophysics, ph-spintronics, ph-topological-phases-of-matter, ph-quantum-materials | ✅ covered |
| Many-body theory (MIT 8.513) | ph-quantum-many-body-theory | ➕ added |
| Polymers & soft matter (PhySH) | ph-soft-matter-physics | ✅ covered |
| Plasma physics (PhySH; physics.plasm-ph) | ph-plasma-physics, ph-fusion-energy | ➕ added |
| Nonlinear dynamics (PhySH; nlin.*) | ph-chaos-theory-nonlinear-dynamics | ✅ covered |
| Networks and complex systems (PhySH Networks; physics.soc-ph) | ph-complex-systems-networks, ph-econophysics, ph-sociophysics | ➕ / ✅ |
| Accelerators & beams (PhySH; physics.acc-ph) | ph-accelerator-physics | ✅ covered |
| Instrumentation and detectors (physics.ins-det) | ph-measurement-instrumentation, ph-detector-physics, ph-experimental-techniques, ph-vacuum-cryogenic-systems, ph-high-energy-experimental-physics | ✅ covered |
| Electronics for physicists | ph-electronics-for-physicists | ➕ added (lab-focused, `related` to the el-* circuit chapters, not duplicating them) |
| Biological physics (PhySH; physics.bio-ph) | ph-biophysics | ✅ covered |
| Chemical physics (physics.chem-ph) | ph-chemical-physics-physical-chemistry | ✅ covered |
| Medical physics, energy, geophysics, atmospheric physics (physics.med-ph, geo-ph, ao-ph; MIT 8.21) | ph-medical-physics, ph-energy-physics, ph-geophysics, ph-atmospheric-environmental-physics | ✅ covered (energy topics expanded) |
| Physics education, history & philosophy (PhySH PER; physics.ed-ph, hist-ph) | ph-physics-education, ph-history-of-physics, ph-philosophy-of-physics | ✅ covered |
| **Astronomy (UAT branches, astro-ph.*)** | | |
| First contact with the sky and the Universe | ph-introductory-astronomy, ph-sky-observing-amateur-astronomy | ➕ added |
| Positional astronomy and time | ph-positional-astronomy | ➕ added |
| Survey astrophysics (MIT 8.901/8.902, 8.284) | ph-astrophysics | ✅ extended (toolkit, HR diagram, binaries, ISM, Milky Way, distance ladder) |
| Observational astronomy (UAT; astro-ph.IM; MIT 8.287) | ph-observational-astronomy-telescopes, ph-radio-astronomy, ph-astrostatistics | ➕ added |
| Astrophysical processes (UAT) | ph-radiative-processes, ph-astrophysical-fluid-dynamics | ➕ added |
| Stellar astronomy (UAT; astro-ph.SR; Cambridge Structure and Evolution of Stars) | ph-stellar-astrophysics | ➕ added |
| Solar physics (UAT; astro-ph.SR; physics.space-ph) | ph-sun-heliophysics, ph-space-physics | ➕ added / ✅ extended |
| Interstellar medium (UAT) | ph-interstellar-medium-star-formation | ➕ added |
| Solar System astronomy (UAT; astro-ph.EP) | ph-celestial-mechanics, ph-planetary-science | ➕ / ✅ extended |
| Exoplanet astronomy (UAT; MIT 8.290) | ph-exoplanets | ➕ added |
| Interdisciplinary astronomy: astrobiology (UAT) | ph-astrobiology | ➕ added |
| Galactic and extragalactic astronomy (UAT; astro-ph.GA; Cambridge Stellar Dynamics and Galaxies) | ph-galaxies-galactic-dynamics, ph-galaxy-formation-evolution | ➕ added |
| Cosmology (UAT; astro-ph.CO; MIT 8.286) | ph-cosmology, ph-advanced-cosmology | ✅ extended / ➕ |
| High-energy astrophysics (UAT; astro-ph.HE) | ph-compact-objects, ph-astroparticle-physics, ph-gravitational-wave-astronomy, ph-neutrino-astronomy | ➕ / ✅ extended |
| Spaceflight, rocketry, orbital mechanics for spacecraft | none | ⛔ out of scope: belongs to the aerospace discipline (linked via `related`) |
| Pure mathematics methods (calculus, linear algebra, ODE/PDE, complex analysis) | none | ⛔ out of scope: math discipline, used as prerequisites |
| Circuit design and electronics engineering | none | ⛔ out of scope: electronics discipline, linked via `related` |

## 4. Grouping changes

The 11 old categories were replaced by 23 categories, ordered from foundational to applied:

- **Classical Physics** was split into *Mechanics, Waves & Fluids*, *Electromagnetism*, *Thermal & Statistical Physics* and *Optics & Photonics*. Chaos moved to *Nonlinear Dynamics & Complex Systems*.
- **Modern Physics** was split into *Quantum Physics*, *Relativity & Gravitation* and *Nuclear & Particle Physics*.
- **Emerging & Advanced Fields** was a grab bag, so it was dissolved and each chapter moved to its subject. Quantum gravity and black-hole physics went to Relativity & Gravitation, cold atoms and quantum sensing to AMO, ultrafast physics to Optics & Photonics, and cryophysics, spintronics and quantum materials to Condensed Matter.
- **Theoretical & Mathematical Physics** became *Mathematical & Computational Methods*, and computational physics moved into it from Applied Physics.
- **Astronomy & Astrophysics** (6 chapters) became six categories: *Astronomy Foundations*, *Observational Astronomy & Data*, *Stars, the Sun & Interstellar Medium*, *Planetary Science & Exoplanets*, *Galaxies & Cosmology*, and *High-Energy & Multi-Messenger Astrophysics*.
- **Experimental Physics** became *Experimental Physics & Instrumentation*. **Interdisciplinary Fields** became *Interdisciplinary Physics*. **Foundations & Meta-Physics** became *Foundations, History & Education*.
- New categories: *Introductory Physics*, *Atomic, Molecular & Optical Physics* and *Plasma Physics*.
- Topics inside several legacy chapters were reordered into teaching order. All ids are unchanged, and no chapter or topic was deleted.

## 5. What was added

**40 new chapters.**

- **On-ramp:** ph-measurement-units-vectors, ph-introductory-mechanics, ph-introductory-heat-thermodynamics, ph-introductory-waves-sound-light, ph-introductory-electricity-magnetism, ph-modern-physics.
- **Core and graduate core:** ph-waves-oscillations, ph-advanced-electrodynamics, ph-advanced-statistical-mechanics, ph-advanced-quantum-mechanics, ph-string-theory.
- **Optics and AMO:** ph-laser-physics, ph-atomic-physics, ph-molecular-physics, ph-atom-light-interaction-laser-cooling.
- **Condensed matter, plasma and complex systems:** ph-quantum-many-body-theory, ph-plasma-physics, ph-fusion-energy, ph-complex-systems-networks.
- **Astronomy (19 chapters):**
  - ph-introductory-astronomy, ph-sky-observing-amateur-astronomy, ph-positional-astronomy
  - ph-observational-astronomy-telescopes, ph-astrostatistics, ph-radio-astronomy
  - ph-radiative-processes, ph-stellar-astrophysics, ph-sun-heliophysics, ph-astrophysical-fluid-dynamics, ph-interstellar-medium-star-formation
  - ph-celestial-mechanics, ph-exoplanets, ph-astrobiology
  - ph-galaxies-galactic-dynamics, ph-galaxy-formation-evolution, ph-advanced-cosmology
  - ph-compact-objects, ph-astroparticle-physics
- **Experimental:** ph-data-analysis-statistics, ph-electronics-for-physicists.

**Notable topics added to existing chapters:**

- **Classical Mechanics:** non-inertial frames, normal modes, canonical transformations, Hamilton-Jacobi.
- **Electromagnetism:** vector calculus, method of images, multipoles, Faraday's law, Poynting theorem.
- **Quantum Mechanics:** square wells, harmonic oscillator, hydrogen atom, Dirac notation, two-state systems. These central items were missing before.
- **General Relativity:** tensor calculus, classic tests, linearized gravity.
- **Quantum Field Theory:** classical field theory, Yang-Mills, the Standard Model as a QFT.
- **Particle Physics:** kinematics and cross-sections, quark model.
- **Nuclear Physics:** semi-empirical mass formula, radiation-matter interaction.
- **Solid State Physics:** Drude and Sommerfeld free-electron models.
- **Mathematical Physics:** Sturm-Liouville theory, Frobenius method, calculus of variations, asymptotics.
- **Computational Physics:** ODE/PDE solvers, FFT, N-body/PIC, HPC.
- **Astrophysics:** 6 survey topics.
- **Cosmology:** Friedmann equations, thermal history, distance measures, observational tests and the Hubble tension.
- **Planetary Science:** 7 topics, including surfaces, magnetospheres, the Kuiper Belt and Oort Cloud, missions and planetary defence.
- **Space Physics:** 6 topics, including radiation belts, aurorae and spacecraft environment.
- **Gravitational-Wave Astronomy:** 6 topics, including waveforms, matched filtering and pulsar timing arrays.
- **Neutrino Astronomy:** MSW effect, cosmic neutrino background.
- **Measurement & Instrumentation:** standards and traceability, GUM, noise.
- **Energy Physics:** 6 topics.
- **Symmetry & Group Theory:** point groups, SU(2)/SU(3), Lorentz/Poincaré groups.
- **Black Hole Physics:** Penrose process.
- **Statistical Mechanics:** a sub-topic on ideal quantum gases.

## 6. Learning-order notes

**Main spine:** Measurement, Units & Vectors → Introductory Mechanics → (Intro Heat / Waves & Light / E&M) → Classical Mechanics → Waves & Oscillations → Modern Physics → Quantum Mechanics → Advanced QM → QFT. The parallel classical branch is Classical E&M → Optics → Laser Physics, and Thermo & Stat Mech → Advanced Stat Mech.

**Astronomy spine:** Introductory Astronomy → Astrophysics (survey, after Modern Physics) → Radiative Processes → Stellar Structure & Evolution → Galaxies → Cosmology (after GR) → Galaxy Formation / Cosmological Perturbations. Side branches: the Sun → Space Physics; Planetary Science → Exoplanets → Astrobiology; Compact Objects → Gravitational-Wave Astronomy.

Relativity runs Special Relativity → General Relativity → Black Hole Physics → Quantum Gravity. String Theory needs QFT and GR.

## 7. Recommended moves / open questions

- **Mathematical methods.** No level-2 "Mathematical Methods for Physicists" chapter was added, to avoid duplicating math. Core physics chapters point straight at ma-calculus, ma-linear-algebra, ma-ordinary-differential-equations-odes and ma-partial-differential-equations-pdes. ph-mathematical-physics is the level-3 physics-flavoured toolbox. ph-classical-electromagnetism and ph-fluid-mechanics build on ma-vector-calculus, and the introductory chapters on ma-precalculus.
- **Overlaps kept on purpose and linked:**
  - ph-astrophysics (survey) overlaps the new deep chapters. Topics such as "Black holes" or "Gamma-ray bursts" appear at survey level there and in depth in ph-compact-objects.
  - ph-planetary-science topics "Exoplanets" and "Astrobiology" overlap the new chapters.
  - ph-space-physics topics "Solar physics" and "Heliophysics" overlap ph-sun-heliophysics.
  - ph-modern-optics topic "Lasers and laser physics" overlaps ph-laser-physics.
  - ph-classical-electromagnetism topic "Plasma physics (classical)" overlaps ph-plasma-physics.
  - ph-materials-physics topic "Phase transitions" overlaps ph-advanced-statistical-mechanics.
  - ph-engineering-physics overlaps the electronics discipline.
- **Recommended moves (not done):**
  - ph-engineering-physics topics on control, power engineering and signal processing belong to electronics or mechanical engineering.
  - ph-geophysics and ph-atmospheric-environmental-physics overlap the new earth discipline. They are linked via `related`.
  - ph-chemical-physics-physical-chemistry overlaps the new chemistry discipline.
  - ph-materials-physics and ph-nanoscience-nanotechnology overlap the new materials discipline.
  - ph-biophysics overlaps biology.
- **Elasticity and solid continuum mechanics** has only a "Continuum mechanics" topic inside Fluid Mechanics. Solid mechanics is expected to live in the mechanical or materials disciplines, so it was not added here.
- **Math prerequisites.** Physics relies on the math discipline's own ordering, for example that ma-ordinary-differential-equations-odes requires ma-calculus. If the math agent adds prerequisites such as ma-ordinary-differential-equations-odes → ma-linear-algebra, a few physics prerequisites (ma-linear-algebra on Quantum Mechanics and General Relativity) may become "redundant" warnings. Prune them then.

# Audit: Electrical & Electronics Engineering (`electronics`)

## 1. Verdict

**Before:** 300 chapters, 1,848 topics, 32 categories, and no chapter had a level, priority, summary or prerequisites. It was very strong on embedded systems, IoT and product engineering. As an Electrical & Electronics Engineering (EEE) discipline it had large holes: no beginner on-ramp, no signals & systems, no transistor-amplifier courses, no electromagnetic waves, transmission lines, RF/microwave or antennas, no communication systems, no electrical machines, no power-systems engineering, no VLSI/IC design flow, no analog IC design and no electrical-measurements course.

**Now:** 353 chapters (+53), 2,604 topics (+756), 26 categories. Every chapter has a level, priority, one-sentence summary and minimal direct prerequisites. Every area in the NCEES FE Electrical & Computer specification and in the MIT 6-5 EE tracks is covered, apart from the pure computing subjects that belong to the new CS discipline. The validator reports 0 errors and 0 warnings.

The display name changed from "Electronics, Embedded & IoT" to **"Electrical & Electronics Engineering"**. The id is still `electronics`, and the description notes the deep embedded and IoT coverage.

## 2. Sources checked

- NCEES, *FE Electrical and Computer CBT Exam Specifications* (17 knowledge areas): https://ncees.org/wp-content/uploads/FE-Electrical-and-Computer-CBT-specs.pdf
- ABET, *Criteria for Accrediting Engineering Programs 2025-26* (Electrical/Computer program criteria; IEEE is the lead society): https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2025-2026/
- MIT EECS, *6-5 Electrical Engineering with Computing* degree chart: https://catalog.mit.edu/degree-charts/electrical-engineering-computing-course-6-5/
- MIT EECS, *EECS Tracks: Electrical Engineering Track Subjects* (Biomedical, Communications, Computer Architecture, Devices/Circuits, EM & Photonics, Embedded, Energy, Hardware Design, Nanoelectronics, Quantum, Systems Science): https://catalog.mit.edu/degree-charts/electrical-engineering-computer-science-tracks/
- Imperial College London, *MEng Electrical and Electronic Engineering programme specification 2025-26* (module list, years 1 to 4): https://www.imperial.ac.uk/media/imperial-college/study/programme-specifications/eee/25x2f26/H604-MEng-Electrical-and-Electronic-Engineering-2025-26.pdf
- Georgia Tech ECE, technical interest areas (bioengineering, computer systems, DSP, electrical energy, electromagnetics, electronic design, microsystems, optics/photonics, systems & controls, telecommunications, VLSI): https://ece.gatech.edu/research/tigs
- ACM/IEEE-CS, *Computer Engineering Curricula 2016 (CE2016)*, used to check embedded, SoC and computer-engineering coverage: https://www.acm.org/binaries/content/assets/education/ce2016-final-report.pdf
- Standard textbook tables of contents used to plan chapter syllabi: Hayt/Kemmerly (circuits), Oppenheim & Willsky (signals), Sedra/Smith (microelectronics), Hayt/Ulaby (electromagnetics), Pozar (microwave), Balanis (antennas), Proakis/Haykin (communications), Goldsmith (wireless), Ogata/Franklin (control), Erickson (power electronics), Chapman/Fitzgerald (machines), Glover/Grainger & Stevenson/Kundur (power systems), Kuffel (high voltage), Weste & Harris / Rabaey (VLSI), Razavi (analog/RF IC), Plummer (fabrication), Pierret (devices).

## 3. Coverage checklist

| Taxonomy area (source) | Chapters | Status |
|---|---|---|
| Beginner on-ramp: charge, voltage, current, safety, schematics, breadboarding | el-basic-electricity, el-hands-on-electronics, el-intro-microcontrollers | ➕ added |
| Mathematics, probability (FE 1-2, ABET) | el-mathematical-foundations (+ `related` to ma-*), math discipline | ✅ covered |
| Ethics & professional practice, IP, safety (FE 3) | el-engineering-ethics-practice | ➕ added |
| Engineering economics (FE 4) | el-cost-engineering (economics topics added) | ✅ covered |
| Properties of electrical materials (FE 5) | el-electrical-materials, el-semiconductor-physics | ➕ added |
| Circuit analysis DC/AC, phasors, three-phase (FE 6) | el-circuit-theory (enriched), el-ac-circuits-power | ➕ added |
| Linear systems, Laplace, transfer functions (FE 7) | el-signals-and-systems | ➕ added |
| Signal processing: sampling, analog & digital filters (FE 8) | el-signal-processing-fundamentals, el-filters, el-digital-signal-processing-dsp, el-statistical-signal-processing | ✅ / ➕ |
| Electronics: devices, amplifiers, op-amps (FE 9) | el-diode-transistor-circuits, el-amplifier-design, el-operational-amplifiers, el-analog-circuits | ➕ added |
| Instrumentation & measurement (FE 9D) | el-electrical-measurements, measurement/testing category | ➕ added |
| Power electronics (FE 9E, Imperial) | el-power-electronics-fundamentals, el-high-power-converters + 12 existing | ➕ added |
| Power systems: power theory, T&D, transformers, machines (FE 10, MIT Energy track) | el-magnetic-circuits-transformers, el-electrical-machines, el-power-system-fundamentals, el-transmission-distribution, el-power-flow-analysis, el-power-system-fault-analysis, el-power-system-protection, el-power-system-stability | ➕ added |
| Generation & renewables, grid integration, storage | el-power-generation, el-renewable-grid-integration, el-smart-grid-energy | ➕ added |
| HVDC, FACTS, power quality, markets (Imperial electives) | el-hvdc-facts, el-power-quality, el-power-system-operation | ➕ added |
| High-voltage engineering | el-high-voltage-engineering | ➕ added |
| Electrical installations & earthing | el-electrical-installations | ➕ added |
| Electric drives, BLDC/PMSM machine theory | el-electric-drives, el-pm-special-machines (+ el-motor-control) | ➕ added |
| Electromagnetics: statics, Maxwell (FE 11) | el-electromagnetics (rebuilt as a full course) | ✅ enriched |
| EM waves, waveguides (MIT 6.2300) | el-electromagnetic-waves | ➕ added |
| Transmission lines (FE 11C) | el-transmission-lines | ➕ added |
| RF & microwave engineering (Imperial) | el-rf-microwave-engineering | ➕ added |
| Antennas & propagation | el-antennas-propagation | ➕ added |
| Radar (Imperial) | el-radar-systems | ➕ added |
| Computational electromagnetics | el-computational-electromagnetics | ➕ added |
| Control systems: classical (FE 12) | el-control-theory (enriched as Feedback Control Systems) | ✅ enriched |
| Modern, digital, nonlinear, robust, MPC (Imperial electives) | el-state-space-digital-control, el-advanced-control-systems | ➕ added |
| Communications: AM/FM, digital, multiplexing (FE 13) | el-analog-communications, el-digital-communications | ➕ added |
| Channel coding & information theory | el-channel-coding | ➕ added |
| Wireless communications: fading, OFDM, MIMO, link budgets | el-wireless-communications | ➕ added |
| Optical communications, photonics (MIT EM & Photonics) | el-optical-fiber-communications, el-photonics-silicon-photonics, el-optoelectronic-devices | ➕ / ✅ |
| Computer networks (FE 14) | el-ethernet-networking, el-network-security (embedded view) | ⛔ theory out of scope: belongs to the CS discipline |
| Digital systems (FE 15) | Digital Electronics category, HDL/FPGA chapters | ✅ enriched |
| Computer systems: microprocessors, memory, interfacing (FE 16) | Microcontrollers category, el-memory-devices, el-buses-communication | ✅ covered |
| Software engineering, algorithms, data structures (FE 17) | el-programming-languages, dev-practices category | ⛔ core CS belongs to the CS discipline |
| Semiconductor device physics (MIT Devices, Imperial) | el-semiconductor-physics (enriched), el-semiconductor-devices | ➕ added |
| Semiconductor fabrication, packaging (MIT 6.2600) | el-cmos-technology, el-semiconductor-fabrication, el-ic-packaging | ➕ added |
| Digital VLSI / RTL to GDSII / verification (GT VLSI, Imperial SoC) | el-digital-vlsi-design, el-asic-physical-design, el-design-verification, el-system-on-chip-soc | ➕ added |
| Analog & RF IC design (Imperial) | el-analog-ic-design, el-rf-ic-design | ➕ added |
| Nanoelectronics / beyond CMOS (MIT Nanoelectronics track) | el-nanoelectronics, el-advanced-materials | ➕ added |
| Quantum systems engineering (MIT track) | el-quantum-technologies (qubit hardware topics added) | ✅ enriched |
| Embedded systems (MIT, CE2016) | el-embedded-systems-fundamentals + 3 existing categories | ✅ strong (➕ a unifying intro chapter) |
| FPGA & HDL | FPGA, ASIC & VLSI Design category | ✅ covered |
| Sensors & actuators, instrumentation | Sensors category (17 chapters) | ✅ covered |
| PCB design, SI/PI, EMC | PCB category | ✅ covered |
| Biomedical electronics (MIT Biomedical track, Imperial) | Medical chapters, el-biomedical-signal-processing | ✅ covered |
| Robotics (overlaps AI) | Control Systems & Robotics category, `related` to ai-* | ✅ covered |
| Machine learning / computer vision on the edge (overlaps AI) | Machine Learning & Edge AI category, `related` to ai-* | ✅ covered |
| Security, IoT, standards, product lifecycle | existing categories | ✅ covered |

## 4. Grouping changes

The 32 categories became 26, ordered from foundations through core EE, systems, embedded and IoT, and application domains, to professional topics.

- **New:** Getting Started; Electromagnetics, RF & Microwave; Signal Processing & Communications; Electrical Machines & Power Systems.
- **Renamed:** "Semiconductors, Integrated Circuits & Devices" became **Semiconductor Devices & Fabrication**. "Field-Programmable Gate Arrays (FPGAs) & HDL" became **FPGA, ASIC & VLSI Design** and now also holds the IC-design chapters.
- **Merged:**
  - "Embedded Software & Firmware" and "Real-Time Systems & Operating Systems" became **Embedded Software, Firmware & RTOS**.
  - "Robotics & Control Systems" plus the control chapters became **Control Systems & Robotics**.
  - "Communication Protocols - Wired", "Communication Protocols - Wireless & IoT" and "Time-Sensitive & Industrial Networks" became **Communication Protocols & Connectivity**.
  - "IoT Architectures, Platforms & Cloud" and "Data Formats, Interoperability & APIs" became **IoT Architectures, Platforms & Data**.
  - "Software Engineering & Development Practices" and "Debugging & Instrumentation" became **Embedded Development Practices & Debugging**.
  - "Machine Learning & AI for Embedded Systems" and "Computer Vision & Perception on Edge" became **Machine Learning & Edge AI**.
  - "Automotive & Mobility Systems" and "Aerospace, Defense & Avionics" became **Automotive, Aerospace & Defense Systems**.
  - "Medical & Healthcare Electronics" and "Niche & Specialized Domains" became **Medical, Industrial & Other Application Domains**.
  - "Business, Product & Lifecycle Management" and "Education, Community & Resources" became **Professional Practice, Business & Community**.
- **Dissolved:** "Practical Cross-Cutting Techniques". Its chapters moved next to their subject: low-power strategies to Microcontrollers; OTA strategies, device configuration, i18n and boot-time optimization to Embedded Software; observability, field diagnostics and data compression to IoT; time synchronization to Protocols; multi-platform development to Dev Practices.
- **Other moves:**
  - DSP moved from Digital Electronics to Signal Processing & Communications.
  - SDR moved from Wireless IoT to Signal Processing & Communications.
  - Semiconductor physics moved from Fundamentals to Semiconductor Devices & Fabrication.
  - Control theory moved from Fundamentals to Control Systems & Robotics.
  - Electromagnetics moved from Fundamentals to Electromagnetics, RF & Microwave.
  - Smart grid moved from Niche to Electrical Machines & Power Systems.
  - Software Testing moved from Measurement to Dev Practices.
- **Clarified names** (ids unchanged): Engineering Electromagnetics, Feedback Control Systems, CMOS Process Technology, Analog Building Blocks, Analog & Active Filters, Buses & Bus Interfacing, Robot Kinematics & Dynamics, Robot Perception & Sensing, Robot Actuators & Drives, High-Speed PCB Design, PCB Thermal Design, PCB Manufacturing & Assembly Processes, Production & Functional Testing, Power Measurement & Analysis, Programming Languages for Embedded Systems, Embedded Memory Management, Firmware Architecture & Development, RTOS Landscape, System-on-Chip (SoC) Design, PLC Programming, Time Synchronization & Timekeeping, IoT Data Management, IoT Analytics & Visualization, Engineering Documentation, Hardware Accelerators for Edge ML, Reinforcement Learning for Embedded Control, Automotive Testing & Validation (XiL), Avionics Safety & Certification, Harsh-Environment Electronics, Medical Device Regulation & Standards, Cost Engineering & Engineering Economics, Mathematical Foundations for Electrical Engineering.
- **Name clashes fixed:** there were two chapters called "Configuration Management". They are now "Software Configuration Management" (el-configuration-management) and "Device Configuration Management" (el-device-configuration-management).
- **`related` links:**
  - Fundamentals, signals, control, coding and crypto chapters link to the matching `ma-*` chapters (e.g. ma-circuit-theory, ma-signal-processing, ma-control-theory, ma-information-theory, ma-error-correcting-codes, ma-cryptography).
  - Every robotics, computer-vision and edge-ML chapter links to its `ai-*` counterpart.
  - Physics overlaps link to `ph-*` (solid-state physics, EM, optics, energy, medical physics, spintronics).

## 5. What was added

**53 new chapters:**

- **Getting Started:** el-basic-electricity, el-hands-on-electronics, el-intro-microcontrollers
- **Fundamentals:** el-ac-circuits-power, el-electrical-materials
- **EM/RF:** el-electromagnetic-waves, el-transmission-lines, el-antennas-propagation, el-rf-microwave-engineering, el-radar-systems, el-computational-electromagnetics
- **Semiconductors:** el-semiconductor-devices, el-semiconductor-fabrication, el-ic-packaging
- **Analog:** el-diode-transistor-circuits, el-amplifier-design
- **Measurement:** el-electrical-measurements
- **Signals & communications:** el-signals-and-systems, el-statistical-signal-processing, el-analog-communications, el-digital-communications, el-channel-coding, el-wireless-communications, el-optical-fiber-communications
- **Control:** el-state-space-digital-control, el-advanced-control-systems
- **Power electronics:** el-power-electronics-fundamentals, el-high-power-converters
- **Machines & power systems:** el-magnetic-circuits-transformers, el-electrical-installations, el-electrical-machines, el-pm-special-machines, el-electric-drives, el-power-system-fundamentals, el-power-generation, el-transmission-distribution, el-power-flow-analysis, el-power-system-fault-analysis, el-power-system-protection, el-power-system-stability, el-power-quality, el-hvdc-facts, el-renewable-grid-integration, el-power-system-operation, el-high-voltage-engineering
- **Embedded:** el-embedded-systems-fundamentals
- **IC design:** el-digital-vlsi-design, el-design-verification, el-asic-physical-design, el-analog-ic-design, el-rf-ic-design
- **Emerging:** el-nanoelectronics
- **Professional:** el-engineering-ethics-practice

**Notable topic additions to existing chapters (topic ids preserved):**

- **Full syllabi:** el-circuit-theory (sources, dividers, first- and second-order transients, SPICE); el-electromagnetics (electrostatics through Faraday and Poynting); el-semiconductor-physics (carrier statistics, transport, recombination, contacts, MOS, heterojunctions); el-control-theory (modelling, time-domain specs, Routh, Nyquist, lead-lag); el-digital-signal-processing-dsp (FIR/IIR design, finite word length, implementation).
- **Missing foundations:** number systems and hazards (combinational logic); FSM design procedure (sequential logic); engineering economics (cost engineering); qubit control electronics and cryo-CMOS (quantum technologies).
- **Thin chapters brought to 6+ topics:** 36 practical core/important chapters (e.g. serial/SPI/I2C buses, linear regulators, inverters, TinyML, cross-compilation, PLC programming, reliability and fault tolerance).

## 6. Learning-order notes

- **Main EE spine:** Basic Electricity → Circuit Theory → AC Circuits & Three-Phase → Signals & Systems → (Analog electronics: Diode & Transistor Circuits → Amplifier Design → Analog IC Design) | (EM: Engineering Electromagnetics → EM Waves / Transmission Lines → RF & Microwave / Antennas) | (Comms: Analog → Digital → Wireless / Coding) | (Control: Feedback Control → State-Space → Advanced) | (Power: Magnetic Circuits & Transformers → Machines → Power System Fundamentals → Load Flow / Faults → Protection / Stability → Renewables integration).
- **Devices & chips:** Electrical Materials → Semiconductor Physics → Semiconductor Devices → CMOS Process → Fabrication; Logic Families + Devices → Digital VLSI → ASIC flow; HDL → FPGA flow → Verification → SoC.
- **Embedded & IoT spine:** Hands-On Electronics → Intro to Microcontrollers → Embedded Systems Fundamentals → Bare-Metal → Concurrency → Real-Time → RTOS; and Embedded Systems Fundamentals → Serial/Ethernet → IoT protocols → Cloud platforms → Device management → Fleet OTA.
- Cross-discipline entry points: ma-elementary-intermediate-algebra (on-ramp), ma-calculus (circuits, math foundations), ph-classical-electromagnetism (EM, materials), ph-quantum-mechanics (nanoelectronics, quantum), ma-linear-algebra, ma-probability-theory, ma-stochastic-processes, ma-root-finding-algorithms and ma-numerical-solutions-of-pdes where needed, plus ai-neural-network-foundations, ai-core-ml-concepts, ai-convolutional-neural-networks-cnns and ai-rl-fundamentals for edge ML.

## 7. Recommended moves / open questions

- **Chapters that are really computer science** (left in place because the discipline is a legacy one): el-version-control, el-build-systems, el-api-architectures, el-data-serialization-formats, el-message-schemas, el-file-formats, el-cloud-computing-for-iot, el-data-management, el-network-security, el-agile-devops-for-embedded, el-project-management. Consider linking them to the new CS discipline in phase B.
- **Overlaps with AI** (kept, linked via `related`): the robotics chapters (el-kinematics-dynamics, el-robot-control, el-perception-sensing, el-path-planning-navigation, el-simultaneous-localization-and-mapping-slam) and the CV/edge-ML chapters. el-reinforcement-learning and el-federated-learning are mostly AI content.
- **Overlapping pairs inside this file** (kept, linked via `related`):
  - el-low-power-design / el-low-power-design-strategies
  - el-firmware-updates-ota / el-over-the-air-ota-update-strategies
  - el-configuration-management / el-device-configuration-management
  - el-prototyping / el-prototyping-rapid-development
  - el-blockchain-for-iot / el-blockchain-distributed-ledger
  - el-testing-strategies / el-software-testing
  - el-automotive-protocols / el-in-vehicle-networking
  - el-industrial-protocols / el-industrial-ethernet / el-field-level-buses
  - el-high-speed-digital-design / el-high-speed-design
  - el-thermal-management / el-thermal-design
  - el-mems-devices / el-mems-sensor-technologies
  - el-compliance-regulations / el-cybersecurity-standards
  - el-spacecraft-electronics / el-space-satellite-systems
  - el-smart-grid-energy / el-renewable-grid-integration
  - el-power-analysis / el-power-quality
  - el-motor-control / el-electric-drives
  - el-actuators / el-actuators-drives
  - el-signal-conditioning / el-sensor-interfacing
  - el-edge-ai-for-vision / el-deep-learning-on-edge
  - el-cmos-technology / el-semiconductor-fabrication (intro vs in depth)
  - el-debug-interfaces / el-hardware-debugging
  - el-open-source-hardware / el-development-kits-evaluation-boards
- **Phase-B prerequisites** that could not be added because the CS discipline does not exist yet:
  - Programming fundamentals / C: el-programming-languages, el-embedded-systems-fundamentals
  - Operating systems: el-concurrency-synchronization, el-rtos-concepts, el-embedded-linux
  - Computer networks: el-ethernet-networking, el-iot-application-protocols, el-network-security
  - Computer architecture (`related`): el-processor-architecture-concepts
  - Graph algorithms: el-path-planning-navigation
  - Linux and Python: el-robot-operating-system-ros
  - Databases: el-data-management
  - Software testing: el-testing-strategies
- **Other disciplines that could supply prerequisites later:** materials (el-electrical-materials), mechanical heat transfer (el-thermal-management) and thermodynamics (el-power-generation), aerospace (el-avionics-systems, el-spacecraft-electronics), chemistry/electrochemistry (el-battery-technologies, el-chemical-sensors), biology/physiology (el-biosensors-medical-sensors).
- **Level 3 is heavy** (about 190 chapters), because most embedded/IoT practice chapters sit at final-year-degree depth. This is deliberate, but the owner may want to lower some practical IoT chapters to level 2.
- **Not added (judged out of scope or too niche):** railway electrification, lighting/illumination engineering, audio/speech processing as a separate chapter (covered partly by DSP and the AI discipline), and the theory of electronic circuit simulation (SPICE algorithms).

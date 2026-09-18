# Audit: AI, Machine Learning & Robotics (`ai`)

## 1. Verdict

**Before:** 89 chapters and 1,057 topics with no levels, priorities, summaries or prerequisites. Deep learning and computer vision were well covered. Several standard areas were missing or reduced to a single line: logic and inference, constraint satisfaction, automated planning, multi-agent systems, speech, recommender systems, time series, causal inference, graph neural networks, LLM application engineering, most robot platforms, and a beginner on-ramp. Coverage was about 70% of a full AI/ML/robotics curriculum.

**After:** 120 chapters (31 new) and 1,656 topics, in 22 categories. Every chapter now has a level, priority, one-sentence summary and minimal prerequisites. The validator reports 0 errors and 0 warnings. Measured against AIMA 4e, the ACM CCS AI/ML subtree, the Stanford core courses and the main robotics texts, coverage is now essentially complete. Remaining gaps are niche and listed in section 7.

## 2. Sources checked

- ACM Computing Classification System 2012, Computing methodologies → Artificial intelligence / Machine learning: https://dl.acm.org/ccs (subtree summarised at https://aima.cs.berkeley.edu/topics.html)
- Russell & Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., table of contents: https://aima.cs.berkeley.edu/contents.html
- Goodfellow, Bengio & Courville, *Deep Learning*, TOC: https://www.deeplearningbook.org/
- Prince, *Understanding Deep Learning* (2023), TOC: https://udlbook.github.io/udlbook/ and https://mitpress.mit.edu/9780262048644/understanding-deep-learning/
- Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.: http://incompleteideas.net/book/the-book-2nd.html
- Stanford CS229 Machine Learning: https://cs229.stanford.edu/
- Stanford CS224N NLP with Deep Learning (Winter 2026 schedule): https://web.stanford.edu/class/cs224n/
- Stanford CS231N Deep Learning for Computer Vision (Spring 2026 schedule): https://cs231n.stanford.edu/schedule.html
- Stanford CS234 Reinforcement Learning: https://web.stanford.edu/class/cs234/
- Lynch & Park, *Modern Robotics: Mechanics, Planning, and Control*: https://hades.mech.northwestern.edu/index.php/Modern_Robotics
- Siciliano & Khatib (eds.), *Springer Handbook of Robotics*, 2nd ed. (Part A foundations to Part G robots and humans; ch. 16 Legged Robots, 44 Aerial Robotics, 53 Multiple Mobile Robot Systems, 67 Humanoids, 70 Human–Robot Augmentation / wearable robots): https://link.springer.com/book/10.1007/978-3-319-32552-1
- Tedrake, *Underactuated Robotics* (MIT 6.8210), used for legged locomotion and trajectory optimization: https://underactuated.mit.edu/
- Tedrake, *Robotic Manipulation* (MIT 6.4210), used for manipulation, perception and soft robots: https://manipulation.mit.edu/

## 3. Coverage checklist

| Area (source) | Chapter(s) | Status |
|---|---|---|
| First contact / what AI is (AIMA 1) | `ai-introduction-to-ai-ml`, `ai-core-ai-concepts` | ➕ added on-ramp |
| Intelligent agents (AIMA 2) | `ai-core-ai-concepts` (new topic) | ➕ |
| Uninformed/heuristic/local/adversarial search (AIMA 3–5; CCS Search methodologies) | `ai-classical-ai-gofai-good-old-fashioned-ai`, `ai-evolutionary-computation` | ✅ |
| Constraint satisfaction (AIMA 6) | `ai-constraint-satisfaction` | ➕ |
| Propositional/first-order logic, inference, SAT (AIMA 7–9) | `ai-logic-automated-reasoning` | ➕ |
| Knowledge representation (AIMA 10; CCS KR&R) | `ai-knowledge-representation-reasoning` | ✅ (+ nonmonotonic, event calculus, Semantic Web) |
| Automated planning (AIMA 11; CCS Planning & scheduling) | `ai-automated-planning` | ➕ |
| Probabilistic reasoning, incl. over time (AIMA 12–14) | `ai-probabilistic-ai` | ✅ (+ HMM/Kalman/DBN, particle filtering) |
| Probabilistic programming (AIMA 15) | `ai-probabilistic-programming` | ➕ |
| Decision theory, MDPs (AIMA 16–17) | `ai-probabilistic-ai`, RL chapters | ✅ |
| Multiagent decision making (AIMA 18; CCS Distributed AI) | `ai-multi-agent-systems` | ➕ |
| Supervised/unsupervised learning (AIMA 19–20; CS229) | `ai-core-ml-concepts`, `ai-types-of-machine-learning`, `ai-ensemble-methods`, `ai-probabilistic-ml` | ✅ |
| ML practical methodology (Goodfellow 11; Prince 8) | `ai-ml-experimentation-evaluation` | ➕ |
| Learning theory (CS229; Prince 20) | `ai-statistical-learning-theory` | ✅ |
| Feed-forward nets, regularization, optimization (Goodfellow 6–8; Prince 3–9) | `ai-neural-network-foundations`, `ai-regularization-normalization`, `ai-optimization-theory` | ✅ (+ init, schedules, autodiff) |
| CNNs, RNNs, transformers (Goodfellow 9–10; Prince 10–12) | CNN, RNN, attention chapters | ✅ |
| Graph neural networks (Prince 13) | `ai-graph-neural-networks` | ➕ |
| Representation / self-supervised learning (Goodfellow 15; CS231N L12) | `ai-self-supervised-representation-learning` | ➕ |
| Deep generative models (Goodfellow 20; Prince 14–18) | `ai-generative-models` | ✅ (+ autoregressive, flow matching, evaluation) |
| Bandits (Sutton & Barto 2; CS234) | `ai-multi-armed-bandits` | ➕ |
| MDPs, DP, MC, TD, function approximation, policy gradients (S&B 3–13) | RL chapters | ✅ (+ n-step, function approximation) |
| Deep, offline, imitation, model-based RL, RLHF (CS234) | `ai-deep-reinforcement-learning`, `ai-advanced-rl-topics`, `ai-llm-fine-tuning` | ✅ |
| RL and psychology/neuroscience (S&B 14–15) | `ai-bio-inspired-ai` | ⚠️ partial, peripheral |
| Classical and neural NLP (AIMA 23–24; CS224N) | NLP chapters | ✅ |
| Speech recognition and synthesis (CCS NLP → speech) | `ai-speech-audio-processing` | ➕ |
| Voice assistants / dialogue | `ai-conversational-ai-voice-assistants` | ➕ |
| LLM pretraining, post-training, PEFT (CS224N) | `ai-large-language-models-llms`, `ai-llm-fine-tuning` | ➕ |
| Prompting, agents, tool use, RAG (CS224N) | `ai-prompt-engineering`, `ai-llm-application-engineering`, `ai-retrieval-augmented-generation`, `ai-autonomous-agents` | ➕ |
| Benchmarking and evaluation of LLMs (CS224N) | `ai-llm-evaluation` | ➕ |
| Computer vision (AIMA 25; CS231N; CCS Computer vision) | CV chapters | ✅ (+ camera models, datasets/metrics, video architectures) |
| Multimodal / vision-language (CS231N L16) | Multimodal AI chapters | ✅ |
| Distributed training, hardware, inference (CS231N L11) | AI Systems & Infrastructure chapters | ✅ |
| Time series and forecasting | `ai-time-series-forecasting` | ➕ |
| Anomaly detection | `ai-anomaly-detection` | ➕ |
| Recommender systems | `ai-recommender-systems` | ➕ |
| Causal inference and causal ML | `ai-causal-inference` | ➕ |
| Data science workflow | Data Science chapters | ✅ |
| MLOps | MLOps chapters | ✅ (+ ML system design, CI/CD, training-serving skew) |
| Philosophy, ethics, safety (AIMA 27) | Safety, Ethics & Governance chapters | ✅ |
| Rigid-body motion, kinematics, dynamics (Modern Robotics 2–8) | `ai-kinematics-dynamics` | ✅ (+ rigid-body motions, screw theory, closed chains) |
| Trajectory generation and motion planning (MR 9–10) | `ai-motion-planning-navigation` | ✅ (+ C-space, collision checking, optimization) |
| Robot control (MR 11; Handbook A) | `ai-control-systems` | ✅ (+ computed torque, operational space) |
| Grasping and manipulation (MR 12; Tedrake) | `ai-manipulation` | ✅ (+ grippers, bin picking, deformables) |
| Wheeled mobile robots (MR 13) | `ai-mobile-robotics` | ➕ |
| Robot software architectures and ROS (Handbook A) | `ai-robot-software-ros` | ➕ |
| Legged robots (Handbook 16; Underactuated 4–5) | `ai-legged-locomotion` | ➕ |
| Aerial robotics (Handbook 44) | `ai-aerial-robotics-drones` | ➕ |
| Humanoids (Handbook 67) | `ai-humanoid-robotics` | ➕ |
| Wearable robots and exoskeletons (Handbook 70) | `ai-wearable-robotics-exoskeletons` | ➕ |
| Multi-robot systems and swarms (Handbook 53) | `ai-swarm-multi-robot-systems` | ➕ |
| Soft robots (Tedrake manipulation 12) | `ai-soft-robotics` | ➕ |
| Intelligent vehicles | `ai-autonomous-driving` | ➕ |
| Perception, SLAM, HRI, robot learning | existing chapters | ✅ (+ VLA models, diffusion policies) |
| AR/HUD wearable assistants (Iron Man roadmap) | `ai-wearable-ai-assistants-ar` | ➕ |
| Medical, field, space, underwater, agricultural, micro robots | `ai-types-of-robots-applications` | ⚠️ survey-level only |
| Mathematics (linear algebra, calculus, probability, optimization) | `ai-mathematics-statistics` (survey) plus math discipline | ⛔ full courses live in the math discipline |
| Programming, data structures and algorithms | `ai-programming-tools` (toolkit only) | ⛔ belongs to the CS discipline being created |

## 4. Grouping changes

The 14 old categories came from all-caps headings, e.g. "Artificial Intelligence (AI) - Foundations" and "Machine Learning (ML)". They are now 22 Title Case categories, ordered from foundational to applied: Getting Started → Classical AI: Search, Logic & Planning → Reasoning Under Uncertainty & Decision Making → Machine Learning Foundations → Deep Learning → Theory of Machine Learning → Reinforcement Learning → Natural Language & Speech Processing → Computer Vision → Large Language Models & LLM Engineering → Multimodal AI → Applied ML Problem Domains → Data Science → MLOps & ML Engineering → AI Systems & Infrastructure → Robotics Foundations → Robot Platforms & Locomotion → Manipulation & Robot Learning → Human-Centred Robotics & Augmentation → AI Safety, Ethics & Governance → Cognitive & Nature-Inspired AI → Emerging & Frontier Fields.

Notable moves:
- `ai-programming-tools` and `ai-mathematics-statistics` moved from Data Science to **Getting Started**, because every ML chapter builds on them.
- `ai-deep-learning-frameworks` moved from Systems to **Deep Learning**, since you use PyTorch as you learn DL.
- `ai-autonomous-agents` and `ai-foundation-models-large-scale-ai` moved from Frontier to the new **LLM** category.
- `ai-graph-based-ml` moved from ML Foundations to **Applied ML Problem Domains**.
- `ai-evolutionary-computation` and `ai-cognitive-architectures` joined `ai-bio-inspired-ai` and `ai-cognitive-ai` in **Cognitive & Nature-Inspired AI**.
- The single old Robotics category was split into four: Foundations, Platforms & Locomotion, Manipulation & Robot Learning, and Human-Centred Robotics & Augmentation.

Renames that clarify without changing meaning:
- `ai-classical-ai-gofai-good-old-fashioned-ai` → "Classical AI: Search, Games & Planning (GOFAI)"
- `ai-programming-tools` → "Programming & Tools for Data Science"
- `ai-mathematics-statistics` → "Mathematics & Statistics for Data Science"
- `ai-dynamic-programming` / `ai-monte-carlo-methods` → suffixed "(RL)" to separate them from the math chapters with the same names
- `ai-model-free-methods` → "Model-Free RL: TD Learning & Policy Gradients"

Topic typo fixes: "A\\" → "A*", "RRT\\" → "RRT*", "D and D Lite" → "D* and D* Lite", "Informed search (A, …)" → "(A*, …)".

Mega-lists restructured, with every id kept:
- **Types of Machine Learning** went from 21 flat topics to 8. The 16 paradigm topics are now sub-topics under three new groups: "Learning with limited labels", "Transfer, few-shot and meta-learning", and "Learning settings: online, federated, multitask, curriculum and continual".
- **Model-Free Methods** went from 15 flat algorithms to 5 groups: TD prediction, TD control, value-function approximation (new), policy-gradient methods and actor-critic methods.

## 5. What was added

31 new chapters:
- **On-ramp:** `ai-introduction-to-ai-ml`
- **Classical AI and reasoning:** `ai-logic-automated-reasoning`, `ai-constraint-satisfaction`, `ai-automated-planning`, `ai-multi-agent-systems`, `ai-causal-inference`, `ai-probabilistic-programming`
- **ML:** `ai-ml-experimentation-evaluation`, `ai-time-series-forecasting`, `ai-anomaly-detection`, `ai-recommender-systems`, `ai-graph-neural-networks`, `ai-self-supervised-representation-learning`, `ai-multi-armed-bandits`
- **Speech and assistants:** `ai-speech-audio-processing`, `ai-conversational-ai-voice-assistants`
- **LLM engineering:** `ai-prompt-engineering`, `ai-llm-application-engineering`, `ai-retrieval-augmented-generation`, `ai-llm-evaluation`, `ai-llm-fine-tuning`
- **Robotics:** `ai-robot-software-ros`, `ai-mobile-robotics`, `ai-autonomous-driving`, `ai-aerial-robotics-drones`, `ai-legged-locomotion`, `ai-humanoid-robotics`, `ai-soft-robotics`, `ai-swarm-multi-robot-systems`, `ai-wearable-robotics-exoskeletons`, `ai-wearable-ai-assistants-ar`

About 200 topics were also added to thin existing chapters. Highlights:
- Intelligent agents in `ai-core-ai-concepts`
- Temporal models and particle filtering in `ai-probabilistic-ai`
- EM and latent-variable models in `ai-probabilistic-ml`
- Initialization, vanishing gradients and autodiff in `ai-neural-network-foundations`
- Decoding strategies in `ai-attention-transformers`
- Function approximation and n-step methods in RL
- Rigid-body motions and screw theory in `ai-kinematics-dynamics`
- Computed-torque and operational-space control
- Configuration space and optimization-based planning
- Series-elastic and quasi-direct-drive actuators
- VLA models and diffusion policies in `ai-robot-learning`
- MCP, orchestration patterns and agent evaluation in `ai-autonomous-agents`
- EU AI Act, NIST RMF and ISO 42001 in governance
- SQL and normalization in `ai-databases`
- ML system design and CI/CD in MLOps

## 6. Learning-order notes

- **Main spine:** Introduction to AI & ML → Programming & Tools + Maths & Stats for DS → Core ML Concepts → Types of ML → Neural Network Foundations → Regularization → CNNs / RNNs → Transformers → LLMs → Fine-tuning, VLMs, Frontier.
- **Classical AI branch:** Core AI Concepts → Classical AI (search) → Logic & Automated Reasoning → KR&R / Automated Planning; Classical AI → Constraint Satisfaction.
- **Uncertainty and RL branch:** Probabilistic AI (needs `ma-probability-theory`) → Probabilistic ML → Probabilistic Programming; Core ML → RL Fundamentals → DP → Monte Carlo → Model-Free → Deep RL → Advanced RL.
- **LLM engineering fast track** (no heavy maths needed): Introduction → Prompt Engineering (L2) → LLM Application Engineering → RAG → Agents → LLM Evaluation. The full LLM internals route goes through Transformers.
- **Robotics spine:** Robot Fundamentals (L1) → Actuators & Sensors / ROS → Kinematics & Dynamics (needs `ma-linear-algebra`, `ph-classical-mechanics`) → Control Systems → Motion Planning → Perception → Mobile / Aerial / Legged → Humanoids. The Iron Man path is Control Systems + HRI → Wearable Robotics & Exoskeletons, and Speech → Conversational AI → Wearable AI Assistants & AR.
- The deepest chain in the discipline is 11 stages.

## 7. Recommended moves / open questions

- **For a future CS discipline:**
  - `ai-programming-tools` (Python and tooling)
  - `ai-databases` (SQL/NoSQL)
  - `ai-data-engineering`, `ai-big-data-technologies` (distributed data systems)
  - `ai-computational-complexity` (algorithms and complexity)
  - Parts of `ai-model-deployment` (containers, APIs)

  They stay here for now. Once CS exists, they should be linked with `related`, and CS programming and algorithms chapters should become prerequisites of `ai-programming-tools`, the Classical AI chapter and `ai-robot-software-ros`.
- **Data Science and MLOps** fit reasonably inside AI. `ai-business-analytics` (priority optional) could move to a future data-science or business-analytics discipline.
- **Overlaps kept and linked with `related`:**
  - Classical AI ↔ Constraint Satisfaction / Automated Planning (the old chapter keeps its overview topics; the new chapters go deep)
  - `ai-types-of-machine-learning` (anomaly detection, continual learning) ↔ `ai-anomaly-detection`, `ai-continual-lifelong-learning`
  - `ai-special-deep-learning-topics` (GNNs, compression) ↔ `ai-graph-neural-networks`, `ai-inference-optimization`
  - `ai-large-language-models-llms` (fine-tuning and alignment sub-topics) ↔ `ai-llm-fine-tuning`
  - `ai-advanced-nlp` (RAG, chain-of-thought) ↔ `ai-retrieval-augmented-generation`, `ai-prompt-engineering`
  - CNN detection/segmentation/3D sub-topics ↔ `ai-core-vision-tasks`, `ai-3d-computer-vision`
  - `ai-motion-planning-navigation` (SLAM, localization) ↔ `ai-mobile-robotics`
  - `ai-robustness-security` ↔ `ai-privacy-in-ai`
  - `ai-business-analytics` ↔ `ai-causal-inference`
- **Cross-discipline overlaps** (linked via `related`): robotics chapters ↔ electronics robotics chapters (`el-robot-operating-system-ros`, `el-kinematics-dynamics`, `el-robot-control`, `el-simultaneous-localization-and-mapping-slam`, `el-autonomous-driving`); control ↔ `ma-control-theory` / `el-control-theory`; theory chapters ↔ `ma-information-theory`, `ma-statistical-learning-theory`, `ma-optimization-algorithms`; edge AI ↔ `el-tinyml-tiny-machine-learning`.
- **Still thin (survey-level only):** medical/surgical, agricultural, space, underwater and micro/nano robotics, all inside `ai-types-of-robots-applications`. Dedicated chapters (e.g. "Medical & Surgical Robotics") could be added later.

# AI digest — 2026-06-11

Rolling 7-day window. Generated automatically.

---

## Read deeply (46 items)

_High relevance and substantial depth — worth full attention._

### [AdaMEM: Test-Time Adaptive Memory for Language Agents](https://arxiv.org/abs/2606.05684)
**Source:** arxiv | **Authors:** Yunxiang Zhang; Yiheng Li; Ali Payani; Lu Wang
**Relevance:** 5/5 — Directly addresses core LLM-agent capability: adaptive memory mechanisms that enable agents to leverage past experience and dynamically adjust behavior during long-horizon task execution.
**Depth:** 4/5 — Provides clear methodology (hybrid long-term/short-term memory architecture, STEP-MFT training technique) and concrete empirical results (13% gains on ALFWorld, 11% on WebShop) with explicit problem motivation around static guidance limitations.

### [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806)
**Source:** arxiv | **Authors:** Dongsheng Zhu; Xuchen Ma; Yucheng Shen; Xiang Li; Yukun Zhao; Shuaiqiang Wang; Lingyong Yan; Dawei Y...
**Relevance:** 5/5 — Directly addresses a core LLM agent capability—tool use, error recovery, and dynamic replanning—with systematic evaluation of failure modes that are critical to real-world deployment.
**Depth:** 4/5 — Provides rigorous benchmark methodology with a 2D perturbation taxonomy, concrete quantitative results (37% PRR drop, 3.66× scaling gap), and identifies dynamic replanning as a distinct bottleneck separate from model scale.

### [Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts](https://arxiv.org/abs/2606.05922)
**Source:** arxiv | **Authors:** Wenbo Pan; Shujie Liu; Chin-Yew Lin; Jingying Zeng; Xianfeng Tang; Xiangyang Zhou; Yan Lu; Xiaohua J...
**Relevance:** 5/5 — Directly addresses LLM agent optimization through harness (tools/skills/workflows) improvement with self-supervised learning, core to frontier agent capability development.
**Depth:** 4/5 — Presents clear methodology (self-validation, self-consistency, pairwise self-preference) with concrete results (SWE-Bench Pro 59%→78%) and analysis of failure mode targeting across multiple domains.

### [Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents](https://arxiv.org/abs/2606.06036)
**Source:** arxiv | **Authors:** Shuo Ji; Yibo Li; Bryan Hooi
**Relevance:** 5/5 — Directly addresses a core LLM agent capability (memory management for long-horizon reasoning) with novel architectural mechanisms (graph-based associative memory with active reconstruction).
**Depth:** 4/5 — Presents clear methodology (Cue-Tag-Content graph structure, active reconstruction mechanism with iterative pruning) and concrete benchmark results (up to 23% improvement on LoCoMo and LongMemEval) with efficiency gains.

### [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090)
**Source:** arxiv | **Authors:** Yaoqi Chen; Haibin Lai; Yuru Feng; Chuyu Han; Qianxi Zhang; Baotong Lu; Menghao Li; Xinjiang Wang; Z...
**Relevance:** 5/5 — Directly addresses LLM-based agent memory architecture for long-horizon task execution, a core frontier capability enabling complex reasoning and planning.
**Depth:** 4/5 — Proposes novel hierarchical state-tree mechanism with four coupled operations (Grow, Compress, Maintain, Revise) and demonstrates substantial empirical improvements (7.8–20.4 pp success rate gain, 55.1% token reduction) on MemoryArena benchmark.

### [ToolChoiceConfusion: Causal Minimal Tool Filtering for Reliable LLM Agents](https://arxiv.org/abs/2606.06284)
**Source:** arxiv | **Authors:** Rahul Suresh Babu; Laxmipriya Ganesh Iyer
**Relevance:** 5/5 — Directly addresses a core LLM-agent capability—reliable tool selection and use—with clear methodology and comprehensive evaluation across multiple benchmarks.
**Depth:** 4/5 — Proposes a novel training-free mechanism (causal-sufficiency filtering via precondition-effect contracts) with rigorous empirical validation across 2448 runs, four LLM backends, and concrete metrics (90% token reduction, wrong-tool call reduction).

### [RUBAS: Rubric-Based Reinforcement Learning for Agent Safety](https://arxiv.org/abs/2606.04051)
**Source:** arxiv | **Authors:** Xian Qi Loye; Qinglin Su; Zhexin Zhang; Shiyao Cui; Qi Zhu; Fei Mi; Hongning Wang; Minlie Huang
**Relevance:** 5/5 — Directly addresses safety alignment for LLM-based agents with tool use, a frontier capability challenge that materially affects what agents can reliably do.
**Depth:** 4/5 — Provides explicit methodology (rubric-based RL with four interpretable dimensions), concrete experimental results across multiple benchmarks, and identifies limitations of prior coarse-grained alignment approaches.

### [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304)
**Source:** arxiv | **Authors:** Chen Huang; Yuhao Wu; Wenxuan Zhang
**Relevance:** 4/5 — Directly addresses multi-agent LLM systems, focusing on communication efficiency and architectural design that materially affects agent coordination and performance.
**Depth:** 4/5 — Provides systematic methodology (analysis of five communication strategies, PACT protocol design), concrete quantitative results (token reduction, performance metrics on OpenHands and SWE-agent), and identifies limitations of unconstrained natural language communication.

### [SentinelBench: A Benchmark for Long-Running Monitoring Agents](https://arxiv.org/abs/2606.05342)
**Source:** arxiv | **Authors:** Matheus Kunzler Maldaner; Adam Fourney; Amanda Swearngin; Hussein Mozzanar; Gagan Bansal; Maya Murad...
**Relevance:** 4/5 — Directly addresses a frontier challenge in LLM-based agent design: sustaining long-running tasks through monitoring and event-driven response rather than continuous action.
**Depth:** 4/5 — Provides concrete benchmark with 100 tasks across 10 environments, establishes baseline results across models and harnesses, and identifies explicit design tradeoffs (responsiveness vs. cost) that motivate the contribution.

### [LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization](https://arxiv.org/abs/2606.05400)
**Source:** arxiv | **Authors:** Yuanhe Zhang; Yuekai Sun; Taiji Suzuki; Jason D. Lee; Fanghui Liu
**Relevance:** 4/5 — LeanMarathon is a multi-agent system that directly addresses long-horizon reasoning, planning, and coordination challenges central to LLM-based agents, with explicit methodology for managing state, dependencies, and failure recovery across complex tasks.
**Depth:** 4/5 — The work provides substantial technical methodology (blueprint abstraction, contract-scoped agents, two-stage orchestration, parallel transaction model) and concrete results (7 theorems formalized, 258 lemmas proved across research papers), with clear articulation of limitations motivating the harness design.

### [Agents' Last Exam](https://arxiv.org/abs/2606.05405)
**Source:** arxiv | **Authors:** Yiyou Sun; Xinyang Han; Weichen Zhang; Yuanbo Pang; Tianyu Wang; Yuhan Cao; Yixiao Huang; Chris Duro...
**Relevance:** 4/5 — Directly addresses evaluation of LLM-based agents on real-world tasks with concrete methodology and benchmark design, materially affecting how agent capabilities are measured.
**Depth:** 4/5 — Provides substantial methodology (task taxonomy, 1K+ tasks across 13 industry clusters, collaboration with 250+ experts) and concrete results (2.6% average pass rate on hardest tier), with clear findings about evaluation gaps.

### [Step-by-Step Optimization-like Reasoning in LLMs over Expanding Search Spaces](https://arxiv.org/abs/2606.05464)
**Source:** arxiv | **Authors:** Nicol\'as Astorga; Nabeel Seedat; Mihaela van der Schaar
**Relevance:** 4/5 — Directly addresses LLM step-by-step reasoning and planning over expanding search spaces with concrete training methodologies and evaluation frameworks.
**Depth:** 4/5 — Provides substantial methodology (solver-guided online policy optimization and search-based offline RL), theoretical grounding (information extraction per search budget), and empirical ablations demonstrating what makes optimization-like reasoning efficient.

### [EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts](https://arxiv.org/abs/2606.05513)
**Source:** arxiv | **Authors:** Yiming Lu; Sihang Zeng; Zhengxu Tang; Max Lau; Fei Liu; Wei Jin
**Relevance:** 4/5 — EpiEvolve demonstrates LLM-based agent mechanisms (episodic memory, reflection, retrieval, rule distillation) applied to streaming forecasting with explicit handling of regime shifts, directly addressing agent adaptation and reasoning.
**Depth:** 4/5 — The paper provides clear methodology for self-evolution (hierarchical episodic memory, reflection on delayed labels, regime-aware retrieval), concrete streaming results (0.629 vs 0.561 accuracy, 5→2 week recovery lag), and ablations validating each component's contribution.

### [FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](https://arxiv.org/abs/2606.05644)
**Source:** arxiv | **Authors:** Zhe Yu; Wenpeng Xing; Tiancheng Zhao; Mohan Li; Changting Lin; Meng Han
**Relevance:** 4/5 — Directly addresses retrieval-augmented generation (RAG) for LLM-based agents, a core capability for grounding agent reasoning and tool use with external knowledge.
**Depth:** 4/5 — Provides clear methodology (token-level conflict detection via three internal signals) with concrete results across 18 settings and scales up to 70B, identifying both the problem (uniform contrastive weighting) and solution (adaptive intervention).

### [Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647)
**Source:** arxiv | **Authors:** Jingheng Ye; Huiqi Zou; Simon Yu; Weiyan Shi
**Relevance:** 4/5 — Directly studies LLM agent behavior, safety, and human-agent interaction in real-world coding scenarios with frontier models, addressing agent deployment and oversight challenges.
**Depth:** 4/5 — Large-scale empirical study (100+ participants, 5-hour tasks, 4 frontier models) with concrete results (94% sabotage detection failure rate), human factors analysis, and actionable safety mechanism recommendations grounded in systematic participant feedback.

### [Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments](https://arxiv.org/abs/2606.05661)
**Source:** arxiv | **Authors:** Parth Asawa; Christopher M. Glaze; Gabriel Orlanski; Ramya Ramakrishnan; Benji Xu; Asim Biswal; Vinc...
**Relevance:** 4/5 — Directly addresses a core LLM-based agent capability (continual learning through experience) with rigorous evaluation methodology across frontier models and agent architectures.
**Depth:** 4/5 — Provides substantial methodology (benchmark design with expert validation, gain metric isolating learning from priors), concrete empirical results across six domains, and explicit findings about failure modes of memory systems versus ICL.

### [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670)
**Source:** arxiv | **Authors:** Yuhang Fu; Ruishan Fang; Jiaqi Shao; Huiyu Zheng; Zhengtao Zhu; Bing Luo; Tao Lin
**Relevance:** 4/5 — Directly addresses LLM-based agent workflows through controlled evaluation of single vs. multi-agent systems, which is core frontier work on agent architecture and effectiveness.
**Depth:** 4/5 — Provides substantial methodology (normalized evaluation protocol across heterogeneous agent systems, controlled substrate conditions) and concrete quantitative results (accuracy-cost trade-offs across 10 benchmarks), revealing important limitations of multi-agent approaches.

### [DiG-Plan: Mitigating Early Commitment for Tool-Graph Planning via Diffusion Guidance](https://arxiv.org/abs/2606.05728)
**Source:** arxiv | **Authors:** Yansi Li; Zhuosheng Zhang
**Relevance:** 4/5 — Directly addresses tool-use planning for LLM-based agents, a core agent capability, with methodology for mitigating a fundamental decoding problem.
**Depth:** 4/5 — Provides clear mechanistic insight (early commitment problem in AR decoding), controlled empirical validation (Pass@10 coverage improvement from 0.320 to 0.943), and a concrete architectural solution (diffusion-based propose-refine-select) with results on multiple benchmarks.

### [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](https://arxiv.org/abs/2606.05761)
**Source:** arxiv | **Authors:** Wenxuan Wang; Haoyu Sun; Fukuan Hou; Mingyang Song; Weinan Zhang; Yu Cheng; Yang Yang
**Relevance:** 4/5 — Directly addresses a frontier capability gap in LLM-based agents—fine-grained relational memory discrimination in long-horizon interactions—with methodology and systematic evaluation.
**Depth:** 4/5 — Introduces a well-designed benchmark with 1,522 instances, diagnostic protocols revealing distinct capability profiles, and empirical results across six memory systems and agent variants, exposing concrete weaknesses in current approaches.

### [TAPO: Tool-Aware Policy Optimization via Credit Transfer for Multimodal Search Agents](https://arxiv.org/abs/2606.05784)
**Source:** arxiv | **Authors:** Chengqi Dong; Chuhuai Yue; Hang He; yandong liu; Fenghe Tang; S Kevin Zhou; Xiaohan Wang; Jiajun Cha...
**Relevance:** 4/5 — Directly addresses a core failure mode in training LLM-based agents for tool use, with methodology to improve RL-based agent optimization.
**Depth:** 4/5 — Provides formal characterization of credit misassignment, empirical quantification (>50% of failing trajectories affected), and a principled solution with no additional overhead, tested across multiple RL algorithms and benchmarks.

### [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805)
**Source:** arxiv | **Authors:** Yuhao Sun; Jiacheng Zhang; Shaanan Cohney; Zhexin Zhang; Feng Liu; Xingliang Yuan
**Relevance:** 4/5 — Directly addresses LLM agent safety through guardrail-integrated planning and feedback mechanisms that materially affect agent behavior and decision-making.
**Depth:** 4/5 — Provides clear methodology (three-decision framework with structured feedback injection into agent planning loop), concrete experimental results on benchmarks (10.42% attack success rate), and addresses limitations of prior guardrails (binary blocking vs. plan revision).

### [The Self-Correction Illusion: LLMs Correct Others but Not Themselves](https://arxiv.org/abs/2606.05976)
**Source:** arxiv | **Authors:** Kuan-Yen Chen; Fang-Yi Su; Jung-Hsien Chiang
**Relevance:** 4/5 — Directly addresses a critical limitation of LLM-based agents' self-correction capabilities—a core reasoning and evaluation challenge for autonomous agent systems.
**Depth:** 4/5 — Provides rigorous methodology (controlled SHA-256-verified experiments across 13 model-domain cells), concrete quantitative results (23-93 percentage point corrections), mechanistic decomposition, and a deployable prompt-based intervention.

### [Beyond Vector Similarity: A Structural Analysis of Graph-Augmented Retrieval for Industrial Knowledge Graphs](https://arxiv.org/abs/2606.06003)
**Source:** arxiv | **Authors:** Grama Chethan
**Relevance:** 4/5 — Directly addresses LLM-based agent tool use and reasoning (query planning with typed primitives), a core frontier capability for agent systems operating over structured knowledge.
**Depth:** 4/5 — Provides explicit methodology (operator vocabulary thesis, LLM Query Planner design, 9 typed traversal primitives), concrete benchmark results (F1 scores, generalization to unseen queries), and identifies systematic limitations of prior vector-only approaches.

### [Beyond Similarity: Trustworthy Memory Search for Personal AI Agents](https://arxiv.org/abs/2606.06054)
**Source:** arxiv | **Authors:** Jiawen Zhang; Kejia Chen; Jiachen Ma; Yangfan Hu; Lipeng He; Yechao Zhang; Jian Liu; Xiaohu Yang; Ti...
**Relevance:** 4/5 — Directly addresses memory mechanisms in LLM-based agents, a frontier capability that materially affects agent reasoning, planning, and reliability.
**Depth:** 4/5 — Provides clear methodology (query-conditioned neural gate), concrete threat characterization (cross-domain leakage, jailbreaks), empirical evaluation across multiple memory frameworks and agent settings, and explicit limitations of similarity-based memory retrieval.

### [When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents](https://arxiv.org/abs/2606.06055)
**Source:** arxiv | **Authors:** Lingxiang Xu; Jiaoyun Yang; Min Hu; Hongtu Chen; Ning An
**Relevance:** 4/5 — Directly addresses a frontier capability gap in memory-augmented LLM agents: measuring when and how agents should use retrieved memory, with safety implications.
**Depth:** 4/5 — Presents controlled experimental methodology (RBI-Eval probe set with matched no-memory baseline) and substantial quantitative results across four LLMs showing 8.9%-82.9% variation in sensitive memory integration, with control experiments isolating content-specificity.

### [Towards Healthy Evolution: Exploring the Role and Mechanisms of Human-Agent Interaction in Self-Evolving Systems](https://arxiv.org/abs/2606.06114)
**Source:** arxiv | **Authors:** Dianxing Shi; Junqi He; Junhao Chen; Bowen Wang; Yuta Nakashima
**Relevance:** 4/5 — Directly addresses LLM-based agent self-evolution, safety, and human oversight—core frontier concerns for autonomous agent systems.
**Depth:** 4/5 — Provides concrete methodology (ANCHOR framework simulating human feedback at multiple evolution phases), empirical results across three domains, and actionable insights on when supervision is most effective.

### [From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents](https://arxiv.org/abs/2606.06223)
**Source:** arxiv | **Authors:** Patrick Wilhelm; Odej Kao
**Relevance:** 4/5 — Directly addresses safety and monitoring of LLM-based agents (ReAct-style) with mechanistic analysis of internal states that affect agentic behavior and risk.
**Depth:** 4/5 — Provides concrete methodology (adapter fine-tuning, activation scoring, entropy analysis, context-calibration) and empirical results across Gameable ALFWorld and WebShop showing how internal features predict risky agent actions.

### [Closing the Loop on Latent Reasoning via Test-Time Reconstruction](https://arxiv.org/abs/2606.06252)
**Source:** arxiv | **Authors:** Xiaopeng Yuan; Haibo Jin; Ye Yu; Peng Kuang; Lijun Yu; Yushun Dong; Haohan Wang
**Relevance:** 4/5 — Directly addresses a frontier capability for LLM-based reasoning: latent reasoning efficiency and fidelity verification, which are core to scaling agent capabilities and enabling more complex planning loops.
**Depth:** 4/5 — Provides clear methodology (reconstruction-guided test-time optimization cycle), concrete benchmark results (AIME 2024: 56.7% → 73.3%), and diagnostic insight into why latent reasoning fails without anchoring to the original query.

### [TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management](https://arxiv.org/abs/2606.06337)
**Source:** arxiv | **Authors:** Shweta Mishra
**Relevance:** 4/5 — TokenMizer directly addresses a critical constraint for LLM-based agents operating in long-horizon tasks—context window management—by proposing a structured memory system that preserves semantic relationships essential for agent reasoning and resumption.
**Depth:** 4/5 — The work provides detailed methodology (typed knowledge graph schema, hybrid extraction pipeline, three-tier compression), concrete benchmarks across 21 sessions with task/decision/file recall metrics, and ablation studies identifying fuzzy label matching as the dominant factor, demonstrating substantial technical substance.

### [Unsupervised Skill Discovery for Agentic Data Analysis](https://arxiv.org/abs/2606.06416)
**Source:** arxiv | **Authors:** Zhisong Qiu; Kangqi Song; Shengwei Tang; Shuofei Qiao; Lei Liang; Huajun Chen; Shumin Deng
**Relevance:** 4/5 — Directly addresses LLM-based agent capability improvement through skill discovery and inference-time augmentation, a frontier technique for enhancing agent reasoning and planning.
**Depth:** 4/5 — Presents concrete methodology (verifier-guided skill discovery with two instantiations: Adaptive Checklist and Answer Agreement verifiers) and substantial empirical results (9.71–32.30% improvements across multiple model settings).

### [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448)
**Source:** arxiv | **Authors:** Yasmine Omri; Ziyu Gan; Zachary Broveak; Robin Geens; Zexue He; Alex Pentland; Marian Verhelst; Tsac...
**Relevance:** 4/5 — Directly addresses agent memory systems—a core capability enabling LLM-based agents to reason over extended horizons—with systems-level characterization and methodology.
**Depth:** 4/5 — Provides concrete taxonomy, phase-aware profiling methodology, empirical characterization across ten systems with benchmarks, and ten actionable system recommendations grounded in measured tradeoffs.

### [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453)
**Source:** arxiv | **Authors:** Zhuoming Chen; Xinrui Zhong; Qilong Feng; Ranajoy Sadhukhan; Yang Zhou; Michael Qizhe Shieh; Zhihao ...
**Relevance:** 4/5 — Directly addresses LLM serving infrastructure that materially affects agent deployment and long-context reasoning capabilities through sparse attention optimization.
**Depth:** 4/5 — Provides explicit methodology (Python-embedded DSL, page-centric tensor abstraction, backend integration), concrete benchmarks (3.46× throughput gains, 4.7× on GLM-4.7-Flash), and demonstrates AI agents autonomously generating and refining algorithms.

### [Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement](https://arxiv.org/abs/2606.06468)
**Source:** arxiv | **Authors:** Jui-Hui Chung; Ziyang Cai; Zihao Li; Qishuo Yin; Rohit Agarwal; Simon Park; Rodrigo Porto; Narutatsu...
**Relevance:** 4/5 — Goedel-Architect is a directly on-criterion LLM-based agent system for formal theorem proving, combining planning (blueprint generation), tool use (Lean prover), and refinement—core agent capabilities.
**Depth:** 4/5 — The work presents clear methodology (blueprint generation and refinement strategy as alternative to recursive decomposition), concrete SOTA results (99.2% on MiniF2F, 88.8% on PutnamBench, IMO/Putnam solutions), and explicit motivation addressing inefficiencies in prior recursive approaches.

### [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473)
**Source:** arxiv | **Authors:** Shangheng Du; Xiangchao Yan; Jinxin Shi; Zongsheng Cao; Shiyang Feng; Zichen Liang; Boyuan Sun; Tian...
**Relevance:** 4/5 — Directly addresses LLM-based agent design for long-horizon tasks with explicit focus on memory, planning, and multi-agent coordination mechanisms that enable sustained self-evolution.
**Depth:** 4/5 — Contributes substantive methodology (Progressive MCGS with graph-based information flow, Retrospective Memory architecture, adaptive coding modes) and concrete evaluation results on MLE-Bench with state-of-the-art performance metrics.

### [Large Language Models Hack Rewards, and Society](https://arxiv.org/abs/2606.04075)
**Source:** arxiv | **Authors:** Wei Liu; Xinyi Mou; Hanqi Yan; Zhongyu Wei; Yulan He
**Relevance:** 4/5 — Directly addresses a critical frontier capability issue affecting LLM agents: reward hacking during RL training and its implications for agent alignment and deployment in real-world settings.
**Depth:** 4/5 — Introduces SocioHack benchmark with 72 environments, demonstrates concrete emergence of regulatory loophole discovery, identifies limitations of current safeguards, and articulates a next-generation post-training paradigm requirement.

### [When Autoregressive Consistency Hurts Safety Alignment](https://arxiv.org/abs/2606.04168)
**Source:** arxiv | **Authors:** Bochen Lyu; Yiyang Jia; Xiaohao Cai; Zhanxing Zhu
**Relevance:** 4/5 — Directly addresses LLM safety alignment and a mechanistic failure mode (autoregressive consistency) that affects agent behavior and robustness, with implications for reliable agent deployment.
**Depth:** 4/5 — Provides mechanistic analysis of why safety alignment is shallow, demonstrates the failure mode with concrete attacks (random insertion), and proposes adversarial safety alignment as a solution with empirical validation.

### [RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training](https://arxiv.org/abs/2606.04272)
**Source:** arxiv | **Authors:** Rachit Bansal; Clara Mohri; Tian Qin; David Alvarez-Melis; Sham Kakade
**Relevance:** 4/5 — Directly addresses frontier LLM training methodology that affects agent capabilities by examining when and how RL should be applied during pre-training to optimize reasoning and task performance.
**Depth:** 4/5 — Provides systematic methodology (RL at multiple pre-training stages), concrete benchmark results across reasoning tasks, and mechanistic insights (e.g., how SFT causes distribution sharpening vs. RL expansion) that challenge standard training assumptions.

### [Smart Picks in the Dark: Towards Efficient RLVR for Reasoning via Tracing Metacognitive Pivots](https://arxiv.org/abs/2606.04503)
**Source:** arxiv | **Authors:** Guangcheng Zhu; Shenzhi Yang; Haobo Wang; Xing Zheng; Yingfan MA; Xuening Feng; Zhongqi Chen; Bowen ...
**Relevance:** 4/5 — Directly addresses training efficiency for large reasoning models via reinforcement learning with verifiable rewards, a frontier capability-enabling method that materially affects what LLM agents can accomplish.
**Depth:** 4/5 — Provides concrete methodology (PivotTrace framework using attention dynamics and pivot density for uncertainty estimation) and empirical results (29.3% annotation efficiency, 2.75× faster convergence) with clear motivation grounded in limitations of prior data selection and unsupervised approaches.

### [GeoMin: Data-Efficient Semi-Supervised RLVR via Geometric Distribution Modeling](https://arxiv.org/abs/2606.04516)
**Source:** arxiv | **Authors:** Guangcheng Zhu; Shenzhi Yang; Haobo Wang; Xing Zheng; Yingfan MA; Xuening Feng; Zhongqi Chen; Kai Ta...
**Relevance:** 4/5 — Directly addresses training methods for LLM reasoning via reinforcement learning with verifiable rewards, a frontier capability that materially affects agent performance.
**Depth:** 4/5 — Provides concrete methodology (geometric distribution modeling to assess rollout reliability), explicit limitations of prior work (coarse heuristics causing data-efficiency bottlenecks), and quantified empirical results (+4.1% improvement, 10% annotation efficiency).

### [Harnessing Generalist Agents for Contextualized Time Series](https://arxiv.org/abs/2606.05404)
**Source:** arxiv | **Authors:** Zihao Li; Kaifeng Jin; Yuanchen Bei; Jiaru Zou; Avaneesh Kumar; Xuying Ning; Yanjun Zhao; Mengting A...
**Relevance:** 4/5 — Directly addresses LLM-based agent design for temporal reasoning with concrete architectural components (temporal tools, memory, capability evolution) that enable agents to reason over structured time series data.
**Depth:** 3/5 — Presents a substantive framework with three integrated components (executable tools, experience-driven evolution, episodic memory) and empirical evaluation across multiple domains, though the paper appears focused on integration rather than introducing novel capabilities to the underlying LLM.

### [Critic-Guided Heterogeneous Multi-Agent Reasoning for Reliable Mathematical Problem Solving](https://arxiv.org/abs/2606.05704)
**Source:** arxiv | **Authors:** Muhammad Talha Sharif; Abdul Rehman
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent reasoning with a critic-guided framework for improving reliability in complex problem-solving, a core agent architecture pattern.
**Depth:** 3/5 — Provides clear methodology (generator-validator with critic feedback loop) and concrete benchmark results (13% improvement on GSM8K), though the core mechanism is relatively incremental over existing multi-agent and verification approaches.

### [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828)
**Source:** arxiv | **Authors:** Zeyu Gan; Huayi Tang; Yong Liu
**Relevance:** 4/5 — Directly addresses LLM-based personal agents' skill selection and preference learning, a core agent capability, with explicit focus on local deployment constraints and semantic intent parsing.
**Depth:** 3/5 — Presents a novel decoupled architecture for preference learning and demonstrates concrete evaluation metrics (cumulative regret, test accuracy), though the methodology section lacks detailed algorithmic specifics on how statistical priors modulate LLM decisions.

### [Evaluating Agentic Configuration Repair for Computer Networks](https://arxiv.org/abs/2606.06212)
**Source:** arxiv | **Authors:** Rufat Asadli; Benjamin Hoffman; Ioannis Protogeros; Laurent Vanbever
**Relevance:** 4/5 — Directly addresses LLM-based agents applied to a concrete domain, demonstrating how agentic architectures (tool use, iterative validation, context management) improve performance over base LLMs.
**Depth:** 3/5 — Provides concrete benchmarking results (12% and 17% improvements) and explains the mechanisms (dynamic context management, iterative validation) that enable agent superiority, though the novelty is primarily in application rather than fundamental agent methodology.

### [DragOn: A Benchmark and Dataset for Drag-Based GUI Interactions](https://arxiv.org/abs/2606.06322)
**Source:** arxiv | **Authors:** Nathan Bout; Maxime Langevin; Ronan Riochet
**Relevance:** 4/5 — Directly addresses a frontier agent capability (GUI interaction via drag operations) with concrete methodology and evaluation across multiple state-of-the-art models.
**Depth:** 3/5 — Solid contribution with large-scale dataset (3.5M tasks), systematic evaluation across proprietary and open models, and demonstrated improvements, though primarily a data/benchmark contribution rather than novel architectural methodology.

### [Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration](https://arxiv.org/abs/2606.06388)
**Source:** arxiv | **Authors:** Jiaju Chen; Yuxuan Lu; Jiayi Su; Chaoran Chen; Songlin Xiao; Zheng Zhang; Yun Wang; Yunyao Li; Jian ...
**Relevance:** 4/5 — Directly addresses LLM agent capabilities in human collaboration—specifically mental model reasoning, intent inference, and alignment, which are core agent competencies beyond task completion.
**Depth:** 3/5 — Provides a substantive dataset with theory-informed annotations and benchmarking methodology for evaluating collaborative reasoning, though the LLM evaluation results are reported as capability demonstration rather than architectural insight.

### [Rollout-Level Advantage-Prioritized Experience Replay for GRPO](https://arxiv.org/abs/2606.04560)
**Source:** arxiv | **Authors:** Gyeongtae Yoo; Sanghyeok Park; Soohyuk Jang; Ik-hwan Kim; Sungroh Yoon
**Relevance:** 4/5 — Directly addresses post-training efficiency for reasoning LLMs via GRPO, a frontier method for agent-like reasoning capabilities in language models.
**Depth:** 3/5 — Provides clear methodology (rollout-level replay with age eviction and advantage prioritization) and concrete benchmark results across scales, though the contribution is incremental optimization of existing GRPO rather than architectural novelty.


## Worth knowing (12 items)

_On-criterion but lower depth, or peripheral relevance._

### [Answer Presence Drives RAG Rewriting Gains](https://arxiv.org/abs/2606.05633)
**Source:** arxiv | **Authors:** Yuejie Li; Yueying Hua; Ke Yang; Li Zhang; Yueping He; Yueping He; Ruiqi Li; Bolin Chen; Tao Wang; B...
**Relevance:** 3/5 — The work analyzes RAG pipelines with LLM rewriters, which are tools used by agents, but focuses on QA evaluation methodology rather than agent reasoning, planning, or capabilities.
**Depth:** 4/5 — The paper provides rigorous controlled intervention methodology with concrete F1 measurements across multiple reader models and datasets, plus critical evaluation of existing probing techniques, demonstrating systematic experimental design.

### [A Pre-Registered Causal Partition of Self-Consistency Elicitation and Reward Design in RLVR](https://arxiv.org/abs/2606.05932)
**Source:** arxiv | **Authors:** Yuze Gao
**Relevance:** 3/5 — On-topic for agent training and RL-based reasoning improvement, but focuses on decomposing reward signal artifacts rather than core agent capabilities or frontier model properties.
**Depth:** 4/5 — Strong methodological contribution with rigorous causal decomposition, controlled experiments, pre-registration, and diagnostic tool for auditing alignment papers, though narrowly scoped to one RL training phenomenon.

### [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256)
**Source:** arxiv | **Authors:** Yang Liu; ZhaoKai Luo; HuaYi Jin; ZhiYong Wang; RuoZhou He; BoYu Wang; Guanjie Chen; Junhao Hu
**Relevance:** 3/5 — RedKnot addresses LLM serving infrastructure (KV cache management) that indirectly enables agent deployment at scale, but is not directly about agent reasoning, planning, or capabilities.
**Depth:** 4/5 — Presents a well-motivated architectural innovation (head-aware decomposition) with concrete methodology, systematic evaluation of KV cache utilization patterns, and practical improvements to serving efficiency without retraining.

### [From Symbolic to Geometric: Enabling Spatial Reasoning in Large Language Models](https://arxiv.org/abs/2606.04381)
**Source:** arxiv | **Authors:** Chen Chu; Bita Azarijoo; Li Xiong; Khurram Shafique; Cyrus Shahabi
**Relevance:** 3/5 — Directly addresses a frontier capability gap in LLMs (geometric spatial reasoning) that affects agent planning and environmental understanding, but is positioned as a perception/reasoning enhancement rather than an agent system.
**Depth:** 4/5 — Provides clear methodology (multimodal architecture treating location as first-class modality, geometric operations), a custom instruction dataset, new benchmark (SpatialEval), and comparative experimental results demonstrating concrete improvements over symbolic baselines.

### [SciVisAgentSkills: Design and Evaluation of Agent Skills for Scientific Data Analysis and Visualization](https://arxiv.org/abs/2606.05525)
**Source:** arxiv | **Authors:** Kuangshi Ai; Haichao Miao; Kaiyuan Tang; Shusen Liu; Chaoli Wang
**Relevance:** 3/5 — Directly addresses LLM-based agent capabilities for a specific domain (scientific visualization), with structured skill design and evaluation, but lacks frontier model capability insights or cross-domain agent reasoning advances.
**Depth:** 3/5 — Provides clear methodology for encoding domain expertise into reusable agent skills and offers concrete benchmark results (108 tasks, token-efficiency metrics), but the contribution is primarily domain-specific engineering rather than fundamental advancement in agent reasoning or capabilities.

### [SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations](https://arxiv.org/abs/2606.05563)
**Source:** arxiv | **Authors:** Taewon Yun; Hyeonseong Park; Jeonghwan Choi; Hayoon Park; Yeeun Choi; Hwanjun Song
**Relevance:** 3/5 — Directly addresses evaluation methodology for LLM-based agents in a specific domain (mediation), which is relevant to agent capability assessment, but mediation is not a frontier capability driver for general LLM agents.
**Depth:** 3/5 — Provides solid methodology (agentic pipeline, topic-localized evaluation, socio-cognitive axes) and concrete benchmarking results across eight frontier LLMs with measurable evaluation alignment (0.82), but contribution is primarily in evaluation design rather than advancing agent architecture or model capabilities.

### [Self-Commitment Latency: A Reward-Free Probe for Prompted Implicit Hacking](https://arxiv.org/abs/2606.05625)
**Source:** arxiv | **Authors:** Bonan Shen; Youting Wang; Dingyan Shang; Tao Ning
**Relevance:** 3/5 — Addresses LLM reasoning integrity and implicit reward hacking detection, which is relevant to agent reliability and safety, but is primarily a diagnostic/evaluation paper rather than an advance in agent capabilities or core training methods.
**Depth:** 3/5 — Proposes a novel, reward-free probe methodology (self-commitment latency) with concrete AUROC results and controlled evaluation, demonstrating solid technical contribution, though the scope is narrowly focused on one detection mechanism rather than broader agent capability or training advances.

### [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875)
**Source:** arxiv | **Authors:** Jianxin Yan; Wangze Ni; Zhenxin Li; Jiabao Jin; Zhitao Shen; Haoyang Li; Jia Zhu; Peng Cheng; Xuemin...
**Relevance:** 3/5 — QCFuse addresses RAG serving efficiency, a supporting infrastructure for LLM agents, but is primarily an optimization technique rather than advancing core agent reasoning or frontier model capabilities.
**Depth:** 3/5 — The paper provides solid methodology (compressed-view query-aware selection, chunk-anchor probing, critical-layer profiling) and concrete benchmark results (1.7x speedup, 1.5x over ProphetKV), but focuses on serving optimization rather than agent capability emergence or novel reasoning mechanisms.

### [Self-Distilled Policy Gradient](https://arxiv.org/abs/2606.04036)
**Source:** arxiv | **Authors:** Yifeng Liu; Shiyuan Zhang; Yifan Zhang; Quanquan Gu
**Relevance:** 3/5 — Self-distillation and policy gradient methods are relevant to LLM agent training, but this work focuses on RL optimization techniques rather than agent reasoning, planning, or tool use capabilities.
**Depth:** 3/5 — The paper presents a concrete methodology combining self-distillation with policy gradient optimization and reports empirical improvements, but the contribution is primarily technical refinement of existing RL training approaches rather than revealing new agent capabilities or frontier model insights.

### [Sparse Mixture-of-Experts Reward Models Learn Interpretable and Specialized Experts for Personalized Preference Modeling](https://arxiv.org/abs/2606.04284)
**Source:** arxiv | **Authors:** Yifan Wang; Jinyi Mu; Mayank Jobanputra; Yu Wang; Ji-Ung Lee; Soyoung Oh; Isabel Valera; Vera Dember...
**Relevance:** 3/5 — Directly addresses RLHF and reward modeling for LLM alignment, a key capability that enables agent instruction-following, but focuses on preference heterogeneity rather than agent reasoning, planning, or tool use.
**Depth:** 3/5 — Presents clear methodology (sparse MoE for expert specialization) and concrete experimental results on interpretability and personalization, but is narrowly scoped to reward modeling rather than broader agent capabilities.

### [A Motivational Architecture for Conversational AGI](https://arxiv.org/abs/2606.05411)
**Source:** arxiv | **Authors:** Anna Mikeda; Ben Goertzel
**Relevance:** 3/5 — Proposes an agent architecture for conversational systems with explicit methodology for motivation and affect, directly addressing LLM-agent design, but operates at an abstract/theoretical level without concrete benchmark evaluation.
**Depth:** 2/5 — Offers architectural concepts and a processing pipeline with two example sketches, but lacks empirical validation, specific implementation details, or quantitative results demonstrating that the motivational framework improves agent capabilities or performance.

### [Entropy-Based Evaluation of AI Agents: A Lightweight Framework for Measuring Behavioral Patterns](https://arxiv.org/abs/2606.05872)
**Source:** arxiv | **Authors:** Olasimbo Ayodeji Arigbabu
**Relevance:** 3/5 — Directly addresses evaluation of LLM-based agents, a frontier concern for agent research, but focuses on behavioral measurement rather than agent capability, reasoning, or planning mechanisms.
**Depth:** 2/5 — Proposes a set of entropy-based metrics with practical implementation, but lacks empirical validation, comparative results, or theoretical justification for why these metrics capture meaningful agent properties beyond intuition.

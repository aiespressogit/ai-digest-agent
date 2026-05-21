# AI digest — 2026-05-21

Rolling 7-day window. Generated automatically.

---

## Read deeply (74 items)

_High relevance and substantial depth — worth full attention._

### [Agentic Systems as Boosting Weak Reasoning Models](https://arxiv.org/abs/2605.14163)
**Source:** arxiv | **Authors:** Varun Sunkaraneni; Pierfrancesco Beneventano; Riccardo Neumarker; Tomaso Poggio; Tomer Galanti
**Relevance:** 5/5 — Directly addresses LLM-based agent orchestration (committee search, critic-comparator systems) and reasoning model capabilities that enable agentic behavior at inference time.
**Depth:** 5/5 — Provides formal theoretical analysis (coverage amplification, local identifiability, soundness conditions, rank-based bounds) combined with concrete empirical results on SWE-bench Verified showing weak-model committee strategies matching frontier models.

### [EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents](https://arxiv.org/abs/2605.13941)
**Source:** arxiv | **Authors:** Jiaqi Liu; Xinyu Ye; Peng Xia; Zeyu Zheng; Cihang Xie; Mingyu Ding; Huaxiu Yao
**Relevance:** 5/5 — Directly addresses LLM-based agent memory systems with a novel self-evolving architecture that improves core agent capabilities (long-term reasoning, retrieval) through autonomous optimization.
**Depth:** 4/5 — Provides clear methodology (closed-loop self-evolution via LLM diagnosis module with safeguards), concrete benchmark results (25.7% and 18.9% improvements on LoCoMo and MemBench), and demonstrates transfer learning insights across benchmarks.

### [Test-Time Learning with an Evolving Library](https://arxiv.org/abs/2605.14477)
**Source:** arxiv | **Authors:** Weijia Xu; Alessandro Sordoni; Chandan Singh; Zelalem Gero; Michel Galley; Xingdi Yuan; Jianfeng Gao
**Relevance:** 5/5 — Directly addresses LLM-based agent capabilities through test-time learning, knowledge accumulation, and multi-turn agentic reasoning without parameter updates.
**Depth:** 4/5 — Presents concrete methodology (weighting/consolidation mechanisms for evolving knowledge libraries) and benchmarked results across mathematical reasoning, code generation, and multi-turn agentic tasks.

### [Resolving Action Bottleneck: Agentic Reinforcement Learning Informed by Token-Level Energy](https://arxiv.org/abs/2605.14558)
**Source:** arxiv | **Authors:** Langzhou He; Junyou Zhu; Yue Zhou; Zhengyao Gu; Junhua Liu; Wei-Chieh Huang; Henry Peng Zou; David W...
**Relevance:** 5/5 — Directly addresses training methods for LLM-based agents via reinforcement learning, focusing on credit assignment mechanisms that materially affect agent policy optimization.
**Depth:** 4/5 — Provides clear methodology (token reweighting via energy-based modeling), concrete empirical results (65.2 pp gains over PPO/GRPO), and identifies a specific limitation of uniform credit assignment in multi-turn agentic trajectories.

### [Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155)
**Source:** arxiv | **Authors:** Zhengxi Lu; Zhiyuan Yao; Zhuowen Han; Zi-Han Wang; Jinyang Wu; Qi Gu; Xunliang Cai; Weiming Lu; Jun ...
**Relevance:** 5/5 — Directly addresses post-training of LLM-based agents via RL, with novel methodology for improving trajectory-level supervision in multi-turn agentic interaction.
**Depth:** 4/5 — Presents clear technical methodology (gated auxiliary objective combining OPSD and RL) with concrete empirical results across three benchmarks showing substantial improvements over baselines.

### [Auditing Agent Harness Safety](https://arxiv.org/abs/2605.14271)
**Source:** arxiv | **Authors:** Chengzhi Liu; Yichen Guo; Yepeng Liu; Yuzhe Yang; Qianqi Yan; Xuandong Zhao; Wenyue Hua; Sheng Liu; ...
**Relevance:** 5/5 — Directly addresses safety and evaluation of LLM-based agent execution harnesses, a critical infrastructure component for multi-agent systems that materially affects what agents can safely do.
**Depth:** 4/5 — Provides concrete methodology (HarnessAudit framework for trajectory auditing), a substantial benchmark (210 tasks across 8 domains in single/multi-agent configurations), and empirical results revealing misalignment between task completion and safe execution across frontier models.

### [Invisible Orchestrators Suppress Protective Behavior and Dissociate Power-Holders: Safety Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2605.13851)
**Source:** arxiv | **Authors:** Hiroki Fukui
**Relevance:** 5/5 — Directly addresses safety and behavioral risks in multi-agent LLM systems—a frontier concern for deployed agent orchestration architectures.
**Depth:** 4/5 — Rigorous preregistered experimental methodology (3×2 design, 365 runs) with concrete metrics (effect sizes, behavioral heterogeneity, alignment suppression) revealing mechanistic failures in multi-agent coordination that output-based evaluation misses.

### [PREPING: Building Agent Memory without Tasks](https://arxiv.org/abs/2605.13880)
**Source:** arxiv | **Authors:** Yumin Choi; Sangwoo Park; Minki Kang; Jinheon Baek; Sung Ju Hwang
**Relevance:** 5/5 — Directly addresses LLM-based agent memory construction, a core capability enabling agent reasoning and planning across diverse environments.
**Depth:** 4/5 — Presents a structured methodology (proposer-guided framework with proposer, solver, validator components) and comprehensive empirical results across three benchmarks showing both competitive performance and substantial deployment cost reduction.

### [Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use](https://arxiv.org/abs/2605.14038)
**Source:** arxiv | **Authors:** Yize Cheng; Chenrui Fan; Mahdi JafariRaviz; Keivan Rezaei; Soheil Feiz
**Relevance:** 5/5 — Directly addresses a core LLM-agent capability—adaptive tool use decision-making—with model-specific analysis of when and why agents fail to invoke necessary tools.
**Depth:** 4/5 — Provides rigorous methodology (model-adaptive definitions, hidden-state probing, two-stage decomposition) and concrete quantitative results (26.5–54% mismatch rates) that diagnose the cognition-to-action gap underlying tool-use failures.

### [SkillFlow: Flow-Driven Recursive Skill Evolution for Agentic Orchestration](https://arxiv.org/abs/2605.14089)
**Source:** arxiv | **Authors:** Mingda Zhang; Tiesunlong Shen; Haoran Luo; Wenjin Liu; Zikai Xiao; Erik Cambria; Xiaoying Tang
**Relevance:** 5/5 — Directly addresses LLM-based agent orchestration with novel training methodology (flow-matching), skill evolution mechanisms, and credit assignment—core frontier capabilities for agent reasoning and planning.
**Depth:** 4/5 — Presents substantial methodological contribution (Tempered Trajectory Balance, recursive skill evolution) with concrete experimental validation across 14 datasets and transparent credit assignment mechanism.

### [LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning](https://arxiv.org/abs/2605.14483)
**Source:** arxiv | **Authors:** Xudong Chen; Yixin Liu; Hua Wei; Kaize Ding
**Relevance:** 5/5 — Directly addresses orchestration, coordination, and training of LLM-based multi-agent systems, which is central to frontier agent capabilities.
**Depth:** 4/5 — Presents concrete methodology (counterfactual RL with localized credit assignment via span editing) and comprehensive empirical results across six benchmarks with state-of-the-art performance claims.

### [Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction](https://arxiv.org/abs/2605.13950)
**Source:** arxiv | **Authors:** Darius A. Faroughy; Sofia Palacios Schweitzer; Ian Pang; Siddharth Mishra-Sharma; David Shih
**Relevance:** 4/5 — Directly evaluates LLM-based agents on long-horizon tool-use tasks with methodology for benchmarking agent capabilities, reasoning, and error detection.
**Depth:** 4/5 — Provides concrete evaluation framework with continuous fidelity metrics, computational cost tracking, LLM-based qualitative failure detection, and empirical results across agent capability levels.

### [Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility](https://arxiv.org/abs/2605.14037)
**Source:** arxiv | **Authors:** Gergely Szilvasy (Meta FAIR); Manuel Faysse (Meta FAIR; MICS; CentraleSup\'elec); Maria Lomeli (Meta...
**Relevance:** 4/5 — Directly addresses a frontier capability constraint (KV-cache efficiency) that materially affects what LLM agents can do—enabling longer context and faster inference for agentic use cases.
**Depth:** 4/5 — Presents clear methodology (lightweight utility predictor, joint end-to-end training, dynamic sparsification), concrete results (3-10× KV cache reduction with minimal performance loss), and reveals structured sparsity patterns for architectural guidance.

### [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](https://arxiv.org/abs/2605.14126)
**Source:** arxiv | **Authors:** Marius S. Knorr; Robert M\"uller; Jan P. Bremer; Nils Schweingruber
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and tool use through reinforcement learning post-training on structured graph reasoning tasks, a frontier capability for agent improvement.
**Depth:** 4/5 — Provides concrete methodology (RL harness, LLM Judge rewards, CodeAct agent design) and empirical results (50% → 77% accuracy improvement on FHIR-AgentBench) with explicit problem formulation addressing tool-selection and constraint-violation failures in prior agents.

### [LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling](https://arxiv.org/abs/2605.14186)
**Source:** arxiv | **Authors:** Qi Cao; Yufan Wang; Peijia Qin; Shuhao Zhang; Pengtao Xie
**Relevance:** 4/5 — Directly addresses LLM agent reasoning and control through metacognitive mechanisms that enable adaptive test-time scaling, a frontier capability for improving agent decision-making.
**Depth:** 4/5 — Provides explicit methodology (separating monitoring from reasoning, FOK/JOL control harness) with concrete benchmark results (48.3→56.9 accuracy improvement, leaderboard positions) and demonstrates how latent model capabilities can be operationalized for agent control.

### [How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization](https://arxiv.org/abs/2605.14200)
**Source:** arxiv | **Authors:** Leena Chennuru Vankadara; Moritz Haas; Luke Hayward; Sebastian Bordt; Alessandro Breccia
**Relevance:** 4/5 — MoE architectures are central to frontier LLMs that power modern agents; principled scaling theory directly affects what model capabilities emerge and thus what agents can accomplish.
**Depth:** 4/5 — Rigorous theoretical framework (DMFT) with novel parameterization (MSSP), systematic analysis across three scaling regimes, and experimental validation of learning-rate transfer and monotonic improvement at scale.

### [Diagnosing Training Inference Mismatch in LLM Reinforcement Learning](https://arxiv.org/abs/2605.14220)
**Source:** arxiv | **Authors:** Tianle Zhong; Neiwen Ling; Yifan Pi; Zijun Wei; Tianshu Yu; Geoffrey Fox; Peng Wu; Xiao Yu
**Relevance:** 4/5 — Directly addresses a systems-level challenge in LLM RL training that affects agent policy optimization stability, which is core to frontier agent capabilities.
**Depth:** 4/5 — Provides rigorous methodology (VeXact diagnostic framework) to isolate TIM from confounding factors, quantifies its impact on training collapse, and identifies concrete remedies with theoretical grounding.

### [Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents](https://arxiv.org/abs/2605.14241)
**Source:** arxiv | **Authors:** Kexin Chu; Dawei Xiang; Wei Zhang
**Relevance:** 4/5 — Directly addresses a core agent infrastructure problem—routing tool calls to functionally equivalent providers—with methodology and concrete benchmark improvements.
**Depth:** 4/5 — Presents a novel contextual bandit approach (latency-quality matching) with clear design rationale, online adaptation mechanism, and substantial empirical gains (+2–18 pp across three benchmarks).

### [Beyond Binary: Reframing GUI Critique as Continuous Semantic Alignment](https://arxiv.org/abs/2605.14311)
**Source:** arxiv | **Authors:** Yuchen Sun; Pei Fu; Shaojie Zhang; Anan Du; Xiuwen Xi; Ruoceng Zhang; Zhenbo Luo; Jian Luan; Chongya...
**Relevance:** 4/5 — Directly addresses critic model design for GUI agents within the test-time scaling paradigm, a core capability enabler for LLM-based agents.
**Depth:** 4/5 — Provides clear methodology (two-stage contrastive learning, affordance space alignment), identifies structural defects in prior work, and demonstrates concrete experimental improvements with zero-shot transferability analysis.

### [FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale](https://arxiv.org/abs/2605.14445)
**Source:** arxiv | **Authors:** Runyuan He; Qiuyang Mang; Shang Zhou; Kaiyuan Liu; Hanchen Li; Huanzhi Mao; Qizheng Zhang; Zerui Li;...
**Relevance:** 4/5 — Directly addresses training methodology for LLM-based agents to improve their reasoning and planning on complex, open-ended problems—a frontier capability that enables better agent performance.
**Depth:** 4/5 — Provides concrete methodology (problem synthesis pipeline with divergence metrics, test case generation) and substantial empirical results (8-12 point improvements on benchmarks) with clear ablation on agent behavior (turn count, token use).

### [LiSA: Lifelong Safety Adaptation via Conservative Policy Induction](https://arxiv.org/abs/2605.14454)
**Source:** arxiv | **Authors:** Minbeom Kim; Lesly Miculicich; Bhavana Dalvi Mishra; Mihir Parmar; Phillip Wallis; Bharath Chandrase...
**Relevance:** 4/5 — Directly addresses safety and guardrails for LLM-based agents in real-world deployment scenarios with tool use and multi-step workflows, a frontier capability concern.
**Depth:** 4/5 — Provides concrete methodology (conservative policy induction, conflict-aware rules, evidence-aware confidence gating) with evaluation across three benchmarks showing robustness under sparse and noisy feedback.

### [Silent Collapse in Recursive Learning Systems](https://arxiv.org/abs/2605.14588)
**Source:** arxiv | **Authors:** Zhipeng Zhang
**Relevance:** 4/5 — Directly addresses a critical failure mode in recursive LLM training pipelines used by autonomous agents and self-improving systems, with clear implications for agent reliability and deployment.
**Depth:** 4/5 — Provides concrete methodology (three measurable precursor signals), a novel framework (MTR) with mechanistic explanation, and trajectory-level analysis of internal model degradation across multiple generations.

### [Learning from Language Feedback via Variational Policy Distillation](https://arxiv.org/abs/2605.15113)
**Source:** arxiv | **Authors:** Yang Li; Erik Nijkamp; Semih Yavuz; Shafiq Rayhan Joty
**Relevance:** 4/5 — Directly addresses a core agent capability—learning from language feedback to improve reasoning and planning—using RL methods that enhance how agents extract actionable signals from natural language critique.
**Depth:** 4/5 — Proposes a novel Variational EM framework with explicit methodology (adaptive teacher refinement, M/E-step mechanics) and concrete evaluation across scientific reasoning and code generation with comparative baselines and stress tests.

### [FutureSim: Replaying World Events to Evaluate Adaptive Agents](https://arxiv.org/abs/2605.15188)
**Source:** arxiv | **Authors:** Shashwat Goel; Nikhil Chandak; Arvindh Arun; Ameya Prabhu; Steffen Staab; Moritz Hardt; Maksym Andri...
**Relevance:** 4/5 — Directly addresses evaluation of LLM-based agents' adaptive reasoning and planning capabilities in realistic, long-horizon scenarios with concrete methodology and results.
**Depth:** 4/5 — Provides systematic benchmark design with ablations studying adaptation mechanisms (memory, reasoning, search), frontier model evaluations with specific accuracy metrics, and identifies clear capability gaps motivating future research.

### [Distribution Corrected Offline Data Distillation for Large Language Models](https://arxiv.org/abs/2605.14071)
**Source:** arxiv | **Authors:** Yumeng Zhang; Zhengbang Yang; Yevin Nikhel Goonatilake; Zhuangdi Zhu
**Relevance:** 4/5 — Directly addresses a frontier capability problem—training smaller LLMs via distillation—that materially affects what resource-constrained agents can do, with explicit methodology solving distributional drift in reasoning tasks.
**Depth:** 4/5 — Presents a principled offline distillation framework with clear technical contribution (distribution correction via adaptive weighting), concrete benchmarks (GSM8K, MATH, AMC, AIME, OlympiadBench), and explicit comparison against prior offline methods.

### [Why Retrieval-Augmented Generation Fails: A Graph Perspective](https://arxiv.org/abs/2605.14192)
**Source:** arxiv | **Authors:** Kai Guo; Xinnan Dai; Zhibo Zhang; Nuohan Lin; Shenglai Zeng; Jie Ren; Haoyu Han; Jiliang Tang
**Relevance:** 4/5 — RAG is a critical capability for LLM-based agents, and this work directly addresses how agents integrate external evidence—a fundamental mechanism for grounded reasoning and tool use.
**Depth:** 4/5 — The paper provides substantial mechanistic insight via circuit tracing and attribution graphs, identifies structural differences between correct and failed reasoning paths, and proposes both a detection framework and targeted interventions with concrete results.

### [Agentic Recommender System with Hierarchical Belief-State Memory](https://arxiv.org/abs/2605.14401)
**Source:** arxiv | **Authors:** Xiang Shen; Yuhang Zhou; Yifan Wu; Zhuokai Zhao; Siyu Lin; Lei Huang; Qianqian Zhong; Lizhu Zhang; B...
**Relevance:** 4/5 — Directly addresses LLM-based agent memory architecture and planning mechanisms for a concrete application (recommendation), with clear methodology for belief-state management and agentic scheduling.
**Depth:** 4/5 — Provides substantial methodological contribution with hierarchical memory tiers, a complete six-operation lifecycle explicitly scheduled by LLM planning, and demonstrates concrete improvements (26.4% HR@1, 10.3% NDCG@10) on benchmark evaluation.

### [Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict](https://arxiv.org/abs/2605.14473)
**Source:** arxiv | **Authors:** Yihang Chen; Pin Qian; Su Wang; Sipeng Zhang; Huan Xu; Shuhuai Lin; Xinpeng Wei
**Relevance:** 4/5 — RAG is a critical capability for LLM agents; this work directly addresses how agents misuse retrieved context when it conflicts with parametric knowledge, a core reliability issue for agent deployment.
**Depth:** 4/5 — The paper introduces Context-Driven Decomposition as a principled intervention mechanism with extensive empirical validation across multiple model families and stress-test regimes, revealing structural patterns in context compliance that distinguish it from prior robustness work.

### [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498)
**Source:** arxiv | **Authors:** Jingbo Yang; Kwei-Herng Lai; Xiaowen Wang; Shiyu Chang; Yaar Harari; Evgeniy Gabrilovich
**Relevance:** 4/5 — Directly addresses LLM-agent memory systems, a core capability enabling deployment as multi-user assistants, with methodology for benchmarking and concrete performance measurements.
**Depth:** 4/5 — Provides substantial methodological contribution (graph-grounded synthesis pipeline, adversarial query generation) and concrete benchmark results exposing critical failures in current memory systems (46% accuracy, 27.1% on knowledge update).

### [Learning from Failures: Correction-Oriented Policy Optimization with Verifiable Rewards](https://arxiv.org/abs/2605.14539)
**Source:** arxiv | **Authors:** Mengjie Ren; Jie Lou; Boxi Cao; Xueru Wen; Hongyu Lin; Xianpei Han; Le Sun; Xing Yu; Yaojie Lu
**Relevance:** 4/5 — Directly addresses LLM reasoning and tool-use capability improvement through a verifiable reward training method, which is central to frontier LLM-based agent capabilities.
**Depth:** 4/5 — Provides clear methodology (correction-oriented supervision from failed trajectories), concrete experimental results across 11 benchmarks with pass@K metrics, and addresses a specific limitation of sparse credit assignment in RLVR.

### [EndPrompt: Efficient Long-Context Extension via Terminal Anchoring](https://arxiv.org/abs/2605.14589)
**Source:** arxiv | **Authors:** Han Tian; Luxuan Chen; Xinran Chen; Rui Kong; Fang Wang; Jiamin Chen; Jinman Zhao; Yuchen Li; Jiashu...
**Relevance:** 4/5 — Context window extension is a frontier capability directly enabling agent reasoning, planning, and memory—core LLM agent competencies.
**Depth:** 4/5 — Strong methodology with theoretical grounding (RoPE analysis, Bernstein inequality), comprehensive benchmarks (RULER, LongBench), and concrete efficiency gains over prior work.

### [Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining](https://arxiv.org/abs/2605.14747)
**Source:** arxiv | **Authors:** Weimin Xiong; Shuhao Gu; Bowen Ye; Zihao Yue; Lei Li; Feifan Song; Sujian Li; Hao Tian
**Relevance:** 4/5 — Directly addresses LLM-based GUI agents through large-scale pretraining data synthesis and multimodal model capability improvements for agent generalization.
**Depth:** 4/5 — Provides clear methodology (coarse-to-fine filtering pipeline, video-to-trajectory extraction) and concrete results (12M trajectories, 5-20% benchmark improvements across grounding/action tasks).

### [GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration](https://arxiv.org/abs/2605.13848)
**Source:** arxiv | **Authors:** Yeahia Sarker; Md Rahmat Ullah; Musa Molla; Shafiq Joty
**Relevance:** 4/5 — GraphBit directly addresses core LLM agent orchestration challenges—routing, state management, tool invocation, and reproducibility—with explicit methodology and comprehensive benchmarking.
**Depth:** 4/5 — The paper presents substantive technical contributions (DAG-based deterministic routing, three-tier memory architecture, error recovery mechanisms) with concrete ablation studies and performance metrics across multiple agent workflow types.

### [ClawForge: Generating Executable Interactive Benchmarks for Command-Line Agents](https://arxiv.org/abs/2605.14133)
**Source:** arxiv | **Authors:** Yuxiang Lai; Peng Xia; Haonian Ji; Kaiwen Xiong; Kaide Zeng; Jiaqi Liu; Fang Wu; Jike Zhong; Zeyu Zh...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation methodology with focus on realistic, stateful interactions—a key capability frontier for agents.
**Depth:** 4/5 — Provides concrete benchmark framework with systematic methodology, detailed evaluation results across seven frontier models, and explicit analysis of failure modes under state conflict.

### [Distribution-Aware Algorithm Design with LLM Agents](https://arxiv.org/abs/2605.14141)
**Source:** arxiv | **Authors:** Saharsh Koganti; Priyadarsi Mishra; Pierfrancesco Beneventano; Tomer Galanti
**Relevance:** 4/5 — Directly addresses LLM-based agents for code synthesis and algorithmic problem-solving, with methodology on how LLMs generate specialized solver code and concrete empirical results on combinatorial optimization.
**Depth:** 4/5 — Provides theoretical analysis of generalization guarantees, clear methodology for solver hint extraction and compilation, and substantial empirical validation across 21 distributions with detailed performance comparisons showing 336.9× speedup gains.

### [Grounded Continuation: A Linear-Time Runtime Verifier for LLM Conversations](https://arxiv.org/abs/2605.14175)
**Source:** arxiv | **Authors:** Qisong He; Yi Dong; Xiaowei Huang
**Relevance:** 4/5 — Directly addresses a critical agent failure mode (context degradation in long conversations) with runtime verification that enables safer deployment of LLM-based conversational agents.
**Depth:** 4/5 — Contributes explicit methodology (dependency graph formalism combining four symbolic systems) with formal guarantees (conflict-free retraction), concrete benchmarks (78-item oracle + multi-agent scenarios), and empirical measurement of LLM extraction faithfulness across model families.

### [SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/abs/2605.14205)
**Source:** arxiv | **Authors:** Zahra Zanjani Foumani; Alberto Castelo; Shuang Xie; Ted Chaiwachirasak; Han Li; Lingyun Wang
**Relevance:** 4/5 — Directly addresses how LLM-based agents can be personalized and scaled to handle heterogeneous user populations in e-commerce, a core capability requirement for practical agent deployment.
**Depth:** 4/5 — Presents novel methodology combining VQ-VAE-induced discrete persona spaces with LLM fine-tuning and persona tokens, includes substantial evaluation on 8.37M real buyers across 42 storefronts with concrete metrics (78% conversion-rate alignment), and releases an open-source pipeline.

### [MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning](https://arxiv.org/abs/2605.14212)
**Source:** arxiv | **Authors:** Yaolun Zhang; Yujie Zhao; Nan Wang; Yiran Wu; Jiayu Chang; Yizhao Chen; Qingyun Wu; Jishen Zhao; Hua...
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent system design and execution through end-to-end reinforcement learning, covering agent orchestration, planning, and self-optimization—core frontier capabilities for autonomous agent systems.
**Depth:** 4/5 — Provides clear methodology (Executor Designer Hierarchical Rollout, Stagewise Co-evolution), concrete benchmark results (21.7% gains over baselines), ablation studies demonstrating designer-executor co-evolution dynamics, and identifies a prior limitation (frozen-executor ceiling) that motivates the contribution.

### [Are Agents Ready to Teach? A Multi-Stage Benchmark for Real-World Teaching Workflows](https://arxiv.org/abs/2605.14322)
**Source:** arxiv | **Authors:** Zixin Chen; Peng Liu; Rui Sheng; Haobo Li; Jianhong Tu; Xiaodong Deng; Kashun Shum; Dayiheng Liu; Hu...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation in a complex real-world workflow (tutoring), with focus on agent capabilities like reasoning, planning, and situated decision-making that are central to frontier agent research.
**Depth:** 4/5 — Provides substantive benchmark methodology with theory-grounded task construction, multiple evaluation signals, human verification, and comprehensive frontier model evaluation revealing specific capability gaps (pedagogical judgment vs. situated tutoring vs. workflow execution).

### [Herculean: An Agentic Benchmark for Financial Intelligence](https://arxiv.org/abs/2605.14355)
**Source:** arxiv | **Authors:** Xueqing Peng; Zhuohan Xie; Yupeng Cao; Haohang Li; Lingfei Qian; Yan Wang; Vincent Jim Zhang; Huan H...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation through a structured benchmark that measures agent capabilities across realistic financial workflows, identifying specific gaps in long-horizon reasoning and execution.
**Depth:** 4/5 — Provides concrete methodology (MCP-based skill environments, standardized workflows) and comparative results across frontier agents with explicit failure analysis (struggles on Hedging/Auditing due to coordination and state consistency), revealing material limitations in current agent systems.

### [Uncovering the Representation Geometry of Minimal Cores in Overcomplete Reasoning Traces](https://arxiv.org/abs/2605.14358)
**Source:** arxiv | **Authors:** Sanjoy Chowdhury; Dinesh Manocha
**Relevance:** 4/5 — Directly addresses how LLM reasoning traces work and what reasoning mechanisms are necessary for agent decision-making, with implications for agent efficiency and interpretability.
**Depth:** 4/5 — Provides rigorous methodology (minimal core extraction, compression metrics, theoretical guarantees), concrete quantitative results across six benchmarks, and geometric analysis that clarifies the representation structure underlying reasoning traces.

### [Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis](https://arxiv.org/abs/2605.14392)
**Source:** arxiv | **Authors:** Yucheng Shi; Zhenwen Liang; Kishan Panaganti; Dian Yu; Wenhao Yu; Haitao Mi
**Relevance:** 4/5 — Directly addresses self-improving LLM reasoning through RL and environment synthesis, with explicit focus on training mechanisms that enable frontier models to improve beyond fixed data.
**Depth:** 4/5 — Presents novel methodology (solve-verify asymmetry, staged validation, difficulty calibration) with concrete results (3.3% relative improvement on Qwen3-4B-Thinking) and clear articulation of why prior approaches fail.

### [Prompting Policies for Multi-step Reasoning and Tool-Use in Black-box LLMs with Iterative Distillation of Experience](https://arxiv.org/abs/2605.14443)
**Source:** arxiv | **Authors:** Krishna Sayana; Ketan Todi; Ambarish Jash
**Relevance:** 4/5 — Directly addresses optimization of prompting policies for LLM-based agents performing multi-step reasoning and tool-use, a core frontier capability for agent systems.
**Depth:** 4/5 — Presents concrete RL methodology with iterative distillation mechanism, demonstrates substantial empirical gains (55%→90% on logic tasks, 74%→91% on tool-use), and provides mechanistic analysis of prompt evolution against established baselines.

### [Stateful Reasoning via Insight Replay](https://arxiv.org/abs/2605.14457)
**Source:** arxiv | **Authors:** Bin Lei; Caiwen Ding; Jiachen Yang; Ang Li; Xin Eric Wang
**Relevance:** 4/5 — InsightReplay directly addresses a core LLM agent capability—scaling reasoning depth without degradation—by proposing a mechanism to maintain access to critical intermediate insights during long reasoning traces.
**Depth:** 4/5 — The work identifies a specific mechanistic failure mode (attention weakening to early insights), proposes a concrete stateful solution with clear methodology, and provides extensive empirical validation across 24 settings with consistent gains.

### [From Table to Cell: Attention for Better Reasoning with TABALIGN](https://arxiv.org/abs/2605.14465)
**Source:** arxiv | **Authors:** Tung Sum Thomas Kwok; Zeyong Zhang; Xinyu Wang; Chunhe Wang; Xiaofeng Lin; Hanwei Wu; Lei Ding; Guan...
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning over structured data through novel planning and grounding mechanisms that improve multi-step reasoning capabilities.
**Depth:** 4/5 — Provides clear methodology (DLM planner + attention verifier architecture), empirical analysis of DLM vs. autoregressive trade-offs, and substantial quantitative results (15.76pp improvement, ablation studies) across multiple benchmarks.

### [Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining](https://arxiv.org/abs/2605.14537)
**Source:** arxiv | **Authors:** Robert M\"uller; Clemens M\"uller
**Relevance:** 4/5 — Directly evaluates LLM-based agents in multi-agent strategic reasoning with tool use (bidding, trading), opponent modeling, and resource planning—core agent capabilities.
**Depth:** 4/5 — Provides systematic evaluation methodology across 242 games, concrete behavioral analysis of failure modes (overbidding, poor adaptation), and comparative results between LLMs and baselines that reveal strategic coherence as a key factor beyond isolated skills.

### [SliceGraph: Mapping Process Isomers in Multi-Run Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.14619)
**Source:** arxiv | **Authors:** Kang Chen; Junjie Nian; Yixin Cao; Yugang Jiang
**Relevance:** 4/5 — Directly addresses LLM reasoning mechanisms and chain-of-thought evaluation through novel analysis of multi-run sampling behavior, a core technique for improving agent decision-making and planning.
**Depth:** 4/5 — Provides rigorous methodology (SliceGraph construction via activation-key Jaccard similarity, biconnected component analysis) with concrete empirical results (85.5% divergence rate, 76.6% cross-family splits) demonstrating structured process geometry overlooked by standard aggregation.

### [Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning](https://arxiv.org/abs/2605.14636)
**Source:** arxiv | **Authors:** Chenlu Ding; Jiancan Wu; Yanchen Luo; Zheyuan Liu; Yancheng Yuan; Xiang Wang
**Relevance:** 4/5 — Directly addresses a critical reasoning limitation in LLMs—temporal reasoning and knowledge cutoff awareness—which is foundational for agent reliability in time-sensitive decision-making and planning.
**Depth:** 4/5 — Provides systematic methodology (prompt analysis, TCFT fine-tuning framework with critique training), concrete benchmark results (41.89% and 37.79% leakage reduction), and identifies a fundamental gap between prompting and model capability that motivated the approach.

### [Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model](https://arxiv.org/abs/2605.14723)
**Source:** arxiv | **Authors:** Minghao Wu; Yuting Yan; Zhenyang Cai; Ke Ji; Chuangsen Fang; Ziying Sheng; Xidong Wang; Rongsheng Wa...
**Relevance:** 4/5 — This paper directly addresses LLM-based agent design with explicit methodology for grounding reasoning in action-conditioned dynamics through world models and multi-stage training.
**Depth:** 4/5 — The work provides concrete methodology (propose-simulate-refine workflow, three-stage curriculum learning), detailed results on MIMIC-IV benchmarks with multiple evaluation metrics, and principled investigation of why world-model access alone fails.

### [XDomainBench: Diagnosing Reasoning Collapse in High-Dimensional Scientific Knowledge Composition](https://arxiv.org/abs/2605.14754)
**Source:** arxiv | **Authors:** Gong Zhiren; Tiantong Wu; Jiaming Zhang; Fuyao Zhang; Che Wang; Yurong Hao; Yikun Hou; Foo Ping; Yil...
**Relevance:** 4/5 — Directly addresses LLM reasoning capabilities and failure modes in compositional scientific tasks, which materially affects what agent systems can accomplish in complex multi-domain reasoning scenarios.
**Depth:** 4/5 — Provides systematic methodology for stress-testing compositional generalization, identifies concrete root causes of reasoning collapse (difficulty increases and interaction-amplified failures), and includes large-scale evaluation across 8,598 sessions revealing failure patterns.

### [Holistic Evaluation and Failure Diagnosis of AI Agents](https://arxiv.org/abs/2605.14865)
**Source:** arxiv | **Authors:** Netta Madvil; Gilad Dym; Alon Mecilati; Edo Dekel; Jonatan Liberman; Rotem Brazilay; Liron Schliesse...
**Relevance:** 4/5 — Directly addresses evaluation and failure diagnosis of LLM-based agents, a frontier capability enabling better agent development and understanding.
**Depth:** 4/5 — Presents concrete methodology (top-down diagnosis paired with bottom-up span-level evaluation) with substantial empirical results (3.5x localization accuracy gains, state-of-the-art on GAIA/SWE-Bench) and explicit limitation diagnosis showing evaluation methodology as the bottleneck.

### [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040)
**Source:** arxiv | **Authors:** Baolin Peng; Wenlin Yao; Qianhui Wu; Hao Cheng; Xiao Yu; Rui Yang; Tao Ge; Alessandrio Sordoni; Xing...
**Relevance:** 4/5 — Directly addresses LLM-based agent development infrastructure, training methods (SFT, RL, distillation), and evaluation across multiple agent domains with concrete benchmarks.
**Depth:** 4/5 — Presents substantive methodology including credit-assignment SFT, Balanced Adaptive Rollout, lightweight environment primitives, and demonstrates results across three distinct agent types with detailed performance metrics.

### [Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use](https://arxiv.org/abs/2605.15041)
**Source:** arxiv | **Authors:** Renning Pang; Tian Lan; Leyuan Liu; Piao Tong; Sheng Cao; Xiaosong Zhang
**Relevance:** 4/5 — Directly addresses LLM-based tool use through a structured framework for adaptive reasoning and execution, which is core to agent capability.
**Depth:** 4/5 — Presents clear methodology (case extraction, complexity/failure profiles, reward design, RL fine-tuning) with concrete benchmark results (5.85pp accuracy gain, 26% reduction in reasoning length) on established tooling evaluations.

### [Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG](https://arxiv.org/abs/2605.15109)
**Source:** arxiv | **Authors:** Riccardo Terrenzi; Maximilian von Zastrow; Serkan Ayvaz
**Relevance:** 4/5 — Directly addresses agentic systems using knowledge graphs with RAG, focusing on how agent reasoning and traversal affect answer quality and citation faithfulness.
**Depth:** 4/5 — Provides methodology (ablation experiments isolating/removing/masking entities) and concrete results showing cited vs. uncited context effects, with explicit limitations of prior citation evaluation approaches.

### [APWA: A Distributed Architecture for Parallelizable Agentic Workflows](https://arxiv.org/abs/2605.15132)
**Source:** arxiv | **Authors:** Evan Rose; Tushin Mallick; Matthew D. Laws; Cristina Nita-Rotaru; Alina Oprea
**Relevance:** 4/5 — Directly addresses multi-agent LLM system architecture, parallelization, and coordination—core frontier challenges for scaling agentic workflows.
**Depth:** 4/5 — Presents concrete architectural design (APWA) with methodology for workflow decomposition and parallel execution, supported by evaluation on complex tasks where prior systems fail.

### [OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation](https://arxiv.org/abs/2605.15177)
**Source:** arxiv | **Authors:** Shang Zhou; Wenhao Chai; Kaiyuan Liu; Huanzhi Mao; Qiuyang Mang; Jingbo Shang
**Relevance:** 4/5 — Directly addresses test-time compute scaling for LLM reasoning via a novel population-based selection mechanism, a frontier capability that materially affects what agents can accomplish.
**Depth:** 4/5 — Presents clear methodology (Bradley-Terry pairwise aggregation with mutation loop), concrete results (+405 Codeforces Elo points), and identifies a real limitation of prior depth-scaling approaches (breadth selection bottleneck).

### [Long Context Pre-Training with Lighthouse Attention](https://huggingface.co/papers/2605.06554)
**Source:** hf_papers | **Authors:** Bowen Peng; Subho Ghosh; Jeffrey Quesnelle
**Relevance:** 4/5 — Long-context capability is a frontier model capacity that directly enables agent reasoning, planning, and tool use across extended interactions and memory windows.
**Depth:** 4/5 — The paper provides clear methodology (hierarchical selection mechanism, symmetrical compression, two-stage training) and concrete experimental results showing training speedup and loss improvements over full attention baseline.

### [Minimal-Intervention KV Retention: A Design-Space Study and a Diversity-Penalty Survivor](https://arxiv.org/abs/2605.14292)
**Source:** arxiv | **Authors:** Libo Sun; Po-wei Harn; Peixiong He; Xiao Qin
**Relevance:** 4/5 — KV-cache compression directly enables longer-context reasoning in LLM agents and affects what long-horizon tasks they can perform; this work systematically studies the design space and proposes a novel scoring mechanism with rigorous evaluation.
**Depth:** 3/5 — The paper provides clear methodology (matched-memory comparison, pre-registered protocol, held-out evaluation) and concrete results (Bonferroni-corrected significance on specific model-budget cells), but the contribution is a localized scoring function improvement rather than a fundamental advance in agent reasoning or capability emergence.

### [InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting](https://arxiv.org/abs/2605.14967)
**Source:** arxiv | **Authors:** Mahdi Sabbaghi; George Pappas; Adel Javanmard; Hamed Hassani
**Relevance:** 4/5 — SFT and instruction-following are foundational to agent capability development, and this work directly addresses how to train models to learn new behaviors while preserving prior knowledge—both critical for capable agents.
**Depth:** 3/5 — The paper presents a principled methodology (information-aware token weighting) with concrete benchmarks across math, code, and reasoning tasks, but the contribution is a focused loss-weighting improvement rather than a breakthrough in agent architectures or capabilities.

### [Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected Few-Shot Guidance](https://arxiv.org/abs/2605.15012)
**Source:** arxiv | **Authors:** Kai Yan; Alexander G. Schwing; Yu-Xiong Wang
**Relevance:** 4/5 — Directly addresses training methods for LLM-based agents performing reasoning tasks (math, coding) via reinforcement learning with verifiable rewards, a frontier capability for agent reasoning.
**Depth:** 3/5 — Proposes FEST with clear methodology (combining supervised, on-policy, and regularization signals) and provides concrete benchmark results demonstrating sample efficiency gains, though the contribution is somewhat incremental over prior demonstration-guided RL work.

### [BOOKMARKS: Efficient Active Storyline Memory for Role-playing](https://arxiv.org/abs/2605.14169)
**Source:** arxiv | **Authors:** Letian Peng; Ziche Liu; Yiming Huang; Longfei Yun; Kun Zhou; Yupeng Hou; Jingbo Shang
**Relevance:** 4/5 — Directly addresses memory systems for LLM-based role-playing agents, a core capability that enables long-horizon consistency and agent reasoning.
**Depth:** 3/5 — Presents a concrete methodology (search-based bookmark framework with synchronization mechanisms) and demonstrates results on 85 characters across 16 artifacts, though focused on a specific application domain rather than frontier model capabilities.

### [A Two-Dimensional Framework for AI Agent Design Patterns: Cognitive Function and Execution Topology](https://arxiv.org/abs/2605.13850)
**Source:** arxiv | **Authors:** Jia Huang; Joey Tianyi Zhou
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture design patterns, cognitive functions, and execution topologies—core to understanding how agents are built and what enables their capabilities.
**Depth:** 3/5 — Provides systematic methodology (2D framework with 7×6 matrix, 27 named patterns, orthogonality analysis) and empirical validation across domains, but lacks mechanistic insights into why patterns work or concrete capability benchmarks.

### [PolitNuggets: Benchmarking Agentic Discovery of Long-Tail Political Facts](https://arxiv.org/abs/2605.14002)
**Source:** arxiv | **Authors:** Yifei Zhu
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation through a benchmark that tests core agent capabilities (planning, tool use, information synthesis) on a realistic task.
**Depth:** 3/5 — Provides concrete methodology (FactNet protocol, multi-agent evaluation system) and empirical results across models, but focuses primarily on benchmarking rather than novel agent mechanisms or frontier capabilities.

### [SPIN: Structural LLM Planning via Iterative Navigation for Industrial Tasks](https://arxiv.org/abs/2605.14051)
**Source:** arxiv | **Authors:** Yusuke Ozaki; Dhaval Patel
**Relevance:** 4/5 — Directly addresses a core LLM-agent problem—planning quality and execution efficiency—with a methodology that enforces structural validity and reduces unnecessary tool calls.
**Depth:** 3/5 — Presents a concrete planning wrapper combining DAG validation with prefix-based execution control, supported by quantitative results on two benchmarks, though the technical novelty is moderate (applying established validation and control patterns).

### [ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation](https://arxiv.org/abs/2605.14102)
**Source:** arxiv | **Authors:** Tarun Mittal
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation methodology, tool orchestration, and operational failure modes that constrain agent capabilities.
**Depth:** 3/5 — Provides concrete evaluation results on GAIA tasks and explicit analysis of why additional orchestration overhead fails to improve performance, yielding actionable design insights for agent systems.

### [Good to Go: The LOOP Skill Engine That Hits 99% Success and Slashes Token Usage by 99% via One-Shot Recording and Deterministic Replay](https://arxiv.org/abs/2605.14237)
**Source:** arxiv | **Authors:** Xiaohua Wang; Kai Yu; XuXiao Liang; Liang Wang; Chao Han
**Relevance:** 4/5 — Directly addresses LLM-based agent deployment, focusing on practical token efficiency and reliability for repetitive task automation through deterministic replay mechanisms.
**Depth:** 3/5 — Provides clear methodology (one-shot recording, template extraction algorithm, deterministic replay) and concrete empirical results (93–99% token reduction, 8.7x latency improvement, 99% success rate) with formal guarantees on replay determinism and write safety.

### [Hypergraph Enterprise Agentic Reasoner over Heterogeneous Business Systems](https://arxiv.org/abs/2605.14259)
**Source:** arxiv | **Authors:** Ling Wang; Songnan Liu; Jianan Wang; Cheng Cheng; Xin Liu; Yihan Zhu; Enyu Li; Yu Xiao; Jiangyong Xi...
**Relevance:** 4/5 — HEAR is an LLM-based agent system addressing core agent challenges (hallucinations, multi-hop reasoning, tool orchestration) with explicit methodology for structured reasoning over enterprise systems.
**Depth:** 3/5 — The paper provides solid methodological contribution (stratified hypergraph ontology, evidence-driven reasoning loop, tool orchestration) and concrete benchmark results (94.7% accuracy on RCA tasks), though lacks deeper investigation into why the approach works or frontier capability implications.

### [Nexus : An Agentic Framework for Time Series Forecasting](https://arxiv.org/abs/2605.14389)
**Source:** arxiv | **Authors:** Sarkar Snigdha Sarathi Das; Palash Goyal; Mihir Parmar; Nanyun Peng; Vishy Tirumalashetty; Chun-Lian...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for reasoning with structured and unstructured data, demonstrating multi-agent decomposition strategies that enhance frontier model capabilities.
**Depth:** 3/5 — Provides clear methodology on how agents decompose forecasting into specialized stages and concrete empirical results on benchmark datasets, though the contribution is somewhat domain-specific (time series) rather than broadly architecturally novel.

### [Coding Agent Is Good As World Simulator](https://arxiv.org/abs/2605.14398)
**Source:** arxiv | **Authors:** Hongyu Wang; Jingquan Wang; Bocheng Zou; Radu Serban; Dan Negrut
**Relevance:** 4/5 — Directly addresses LLM-based agent systems (planning, code generation, visual review, physics analysis agents) coordinating to build world models, a capability that materially affects what agents can do.
**Depth:** 3/5 — Presents explicit methodology (agent framework with specialized roles and iterative refinement) and concrete experimental results comparing physical accuracy and instruction fidelity against video-based baselines.

### [$\pi$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](https://arxiv.org/abs/2605.14678)
**Source:** arxiv | **Authors:** Haoran Zhang; Luxin Xu; Zhilin Wang; Runquan Gui; Shunkai Zhang; Haodi Lei; Zihao He; Bingsu He; Chi...
**Relevance:** 4/5 — Directly evaluates LLM-based personal assistant agents on a frontier capability (proactive intent recognition) that materially affects agent effectiveness in real-world deployments.
**Depth:** 3/5 — Provides concrete benchmark design with 100 multi-turn tasks, explicit evaluation methodology for proactivity vs. task completion, and empirical results showing capability gaps, though limited in mechanistic insights into how agents should achieve proactivity.

### [A Heterogeneous Temporal Memory Governance Framework for Long-Term LLM Persona Consistency](https://arxiv.org/abs/2605.14802)
**Source:** arxiv | **Authors:** Zhao Yang; Wang Huan; Li Yingshuo; Tu Haomiao; Lin Hujite
**Relevance:** 4/5 — Directly addresses memory and consistency challenges in long-term LLM agent interactions, a frontier capability problem for deploying agents in extended dialogue scenarios.
**Depth:** 3/5 — Provides clear methodology (temporal memory separation, fusion strategies, evidence verification protocol) and concrete empirical results (recall accuracy under noise conditions, ablation studies), though the evaluation is limited to engineering logs rather than standardized benchmarks.

### [Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.14892)
**Source:** arxiv | **Authors:** Shihao Qi; Jie Ma; Rui Xing; Wei Guo; Xiao Huang; Zhitao Gao; Jianhao Deng; Jun Liu; Lingling Zhang;...
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent systems covering collaboration, failure attribution, and self-evolution—core frontier topics for agent capability and deployment.
**Depth:** 3/5 — Survey work that provides systematic taxonomies and formally characterizes dependencies across four stages (LIFE progression), but lacks novel empirical results or detailed methodology for individual contributions.

### [Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling](https://arxiv.org/abs/2605.15100)
**Source:** arxiv | **Authors:** Rongman Xu; Yifei Li; Tianzhe Zhao; Yanrui Wu; Bo Li; Hang Yan
**Relevance:** 4/5 — Directly addresses inference-time scaling for LLMs, a frontier capability that materially affects agent reasoning quality and cost—core to enabling practical LLM agents.
**Depth:** 3/5 — Presents concrete methodology (Confidence-Weighted Bayesian protocol + Trend-Aware Stratified Pruning) with quantified results (10x token reduction) across benchmarks, though the contribution is primarily algorithmic optimization rather than paradigm-shifting.

### [Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected Few-Shot Guidance](https://huggingface.co/papers/2605.15012)
**Source:** hf_papers | **Authors:** Kai Yan; Alexander G. Schwing; Yu-Xiong Wang
**Relevance:** 4/5 — Directly addresses training methods for LLM-based agents doing reasoning tasks (math, coding) via reinforcement learning with verifiable rewards, a frontier capability-enabling approach.
**Depth:** 3/5 — Provides clear methodology (combination of supervised, on-policy, and weight-decay signals) and concrete results (sample efficiency gains with 128 demonstrations across benchmarks), though the contribution is primarily an engineering improvement rather than a fundamental advance.


## Worth knowing (22 items)

_On-criterion but lower depth, or peripheral relevance._

### [PreFT: Prefill-only finetuning for efficient inference](https://arxiv.org/abs/2605.14217)
**Source:** arxiv | **Authors:** Andrew Lanpouthakoun; Aryaman Arora; Zhengxuan Wu; Dhruv Pai; Ben Keigwin; Dan Jurafsky; Christopher...
**Relevance:** 3/5 — On-topic as an inference optimization for personalized LLM serving, but tangential to core agent capabilities—focuses on deployment efficiency rather than agent reasoning, planning, or tool use.
**Depth:** 4/5 — Solid methodology with clear technical motivation (prefill vs. decode mismatch), concrete empirical results (1.9× throughput improvement, performance tradeoffs), and an efficient implementation released on vLLM.

### [Dynamics of the Transformer Residual Stream: Coupling Spectral Geometry to Network Topology](https://arxiv.org/abs/2605.14258)
**Source:** arxiv | **Authors:** Jesseba Fernando; Grigori Guitchounts
**Relevance:** 3/5 — Provides mechanistic understanding of how LLM internals process information through depth, which is foundational for predicting agent reasoning capabilities, but is not directly about agent construction or deployment.
**Depth:** 4/5 — Rigorous methodology (full Jacobian eigendecomposition across production-scale models) with concrete empirical results (spectral gradients, low-rank bottlenecks, topological coupling) that reveal learned structure and offer mechanistic insight into LLM computation.

### [Exemplar Partitioning for Mechanistic Interpretability](https://arxiv.org/abs/2605.14347)
**Source:** arxiv | **Authors:** Jessica Rumbelow
**Relevance:** 3/5 — Mechanistic interpretability of LLM activations is adjacent to agent capabilities but not directly about agent reasoning, planning, tool use, or deployment.
**Depth:** 4/5 — The work presents novel methodology (Exemplar Partitioning via leader-clustering), concrete benchmarks (0.881 AUROC on AxBench, 97% probe accuracy), and explicit comparisons to SAE baselines with significant computational efficiency gains.

### [When Answers Stray from Questions: Hallucination Detection via Question-Answer Orthogonal Decomposition](https://arxiv.org/abs/2605.14449)
**Source:** arxiv | **Authors:** Siyang Yao; Erhu Feng; Yubin Xia
**Relevance:** 3/5 — Hallucination detection is a critical safety and reliability concern for LLM agents, but this work addresses detection methodology rather than agent-specific architectures, planning, or tool use.
**Depth:** 4/5 — QAOD presents a clear methodology (orthogonal decomposition with layer/neuron selection) and strong empirical results (up to 21% OOD improvement), addressing both in-domain and cross-domain generalization.

### [XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference](https://arxiv.org/abs/2605.14844)
**Source:** arxiv | **Authors:** Thomas Witt
**Relevance:** 3/5 — LLM inference optimization is adjacent to agent deployment but not central to agent reasoning, planning, or tool use—it affects throughput/cost for running agents rather than agent capabilities themselves.
**Depth:** 4/5 — Solid technical contribution with clear methodology (quality-targeted quantization, H-Process search, sparse outlier separation), concrete benchmarks (tok/s, GSM8K accuracy across model scales), and explicit constraints driving the design.

### [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051)
**Source:** arxiv | **Authors:** Linghao Kong; Megan Flynn; Michael Peng; Nir Shavit; Mark Kurtz; Alexandre Marques
**Relevance:** 3/5 — Speculative decoding is a frontier inference optimization that materially affects LLM agent deployment efficiency, but the work is primarily about serving systems and latency modeling rather than agent capabilities or reasoning mechanisms.
**Depth:** 4/5 — The paper provides rigorous methodology (Little's Law decomposition, latency component analysis) and extensive empirical validation across vLLM with clear characterization of how SD parameters affect performance under load.

### [TFGN: Task-Free, Replay-Free Continual Pre-Training Without Catastrophic Forgetting at LLM Scale](https://arxiv.org/abs/2605.15053)
**Source:** arxiv | **Authors:** Anurup Ganguli
**Relevance:** 3/5 — Continual pre-training architecture for LLMs improves model robustness and capability retention, relevant to agent deployment and capability stability, but not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Rigorous architectural contribution with clear methodology (Read/Write decomposition), comprehensive multi-scale evaluation across six domains and three model sizes, and explicit measurements of backward/forward transfer and gradient orthogonality.

### [Polar probe linearly decodes semantic structures from LLMs](https://arxiv.org/abs/2605.14125)
**Source:** arxiv | **Authors:** Pablo J. Diego-Sim\'on; Pierre Orhan; Yair Lakretz; Jean-R\'emi King
**Relevance:** 3/5 — Directly addresses how LLMs internally represent and structure semantic knowledge, which is foundational to understanding model capabilities that enable agent reasoning, but does not focus on agent behaviors, tool use, or deployment.
**Depth:** 4/5 — Provides concrete methodology (Polar Probe technique), systematic evaluation across five domains with quantitative results (linear recoverability, layer emergence patterns, generalization bounds), and mechanistic insights into semantic binding via geometric principles.

### [Uncertainty Quantification for Large Language Diffusion Models](https://arxiv.org/abs/2605.14570)
**Source:** arxiv | **Authors:** Artem Vazhentsev; Vladislav Smirnov; David Li; Maxim Panov; Timothy Baldwin; Artem Shelmanov
**Relevance:** 3/5 — Uncertainty quantification for LLMs directly supports safer agent deployment and reliable reasoning, but the work focuses on diffusion-based LLMs rather than the dominant autoregressive architectures that power frontier agents.
**Depth:** 4/5 — The paper provides solid methodology (zero-shot UQ signals from denoising dynamics, theoretical bounds on trajectory dissimilarity) and comprehensive experimental validation across multiple tasks and models with concrete efficiency gains.

### [Conditional Attribute Estimation with Autoregressive Sequence Models](https://arxiv.org/abs/2605.14004)
**Source:** arxiv | **Authors:** Erica Stutz; Giacomo Marino; Daniella Meeker; Qiao Liu; Andrew J. Loza
**Relevance:** 3/5 — The work addresses control and steering of autoregressive language models through attribute conditioning, which is relevant to agent decision-making and constrained generation, but is not fundamentally about agent architecture, reasoning, planning, or tool use.
**Depth:** 4/5 — The paper presents concrete methodology (Conditional Attribute Transformers) with multiple capabilities (credit assignment, counterfactual analysis, steerable generation) and demonstrates state-of-the-art results on sparse reward tasks and language benchmarks.

### [Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection](https://arxiv.org/abs/2605.14062)
**Source:** arxiv | **Authors:** Anjir Ahmed Chowdhury; Syed Zawad; Feng Yan
**Relevance:** 3/5 — Directly addresses synthetic data generation efficiency for LLM post-training, which is foundational infrastructure for agent training, but focuses on token optimization rather than agent capabilities themselves.
**Depth:** 4/5 — Provides formal methodology (sequential decision process, martingale argument for unbiased rejection), concrete multi-stage validation approach, and comprehensive empirical results (11-78.2% token savings across 5 models and 7 benchmarks) with clear technical insight into why early rejection is effective.

### [The Evaluation Trap: Benchmark Design as Theoretical Commitment](https://arxiv.org/abs/2605.14167)
**Source:** arxiv | **Authors:** Theodore J Kalaitzidis
**Relevance:** 3/5 — This paper addresses evaluation methodology for AI capabilities, which is foundational to assessing agent capabilities, but is primarily meta-evaluative rather than directly about agent design or frontier model capabilities.
**Depth:** 4/5 — The work introduces a systematic methodology (Epistematics) with a failure-mode taxonomy and audit procedures for benchmarking, grounded in concrete theoretical analysis and a worked case study demonstrating structural evaluation gaps.

### [BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE](https://arxiv.org/abs/2605.14438)
**Source:** arxiv | **Authors:** Juntong Wu; Jialiang Cheng; Qishen Yin; Yue Dai; Yuliang Yan; Fuyu Lv; Ou Dan; Li Yuan
**Relevance:** 3/5 — MoE efficiency improvements affect LLM inference performance, which is relevant to agent deployment, but the work is primarily an optimization technique rather than directly addressing agent reasoning, planning, or capabilities.
**Depth:** 4/5 — The paper presents clear methodology (binary mask learning with straight-through estimators, auxiliary regularization), concrete results (98% performance retention, 85% FLOP reduction, 2.5× speedup), and addresses a real limitation (train-inference mismatch in sparse routing).

### [Efficient Multi-objective Prompt Optimization via Pure-exploration Bandits](https://arxiv.org/abs/2605.14553)
**Source:** arxiv | **Authors:** Donghao Li; Chengshuai Shi; Weijuan Ou; Cong Shen; Jing Yang
**Relevance:** 3/5 — Prompt optimization is foundational to agent capability, but this work focuses on engineering methodology rather than agent systems, reasoning, planning, or model capabilities that enable agents.
**Depth:** 3/5 — Solid methodological contribution (adapting multi-objective bandits theory with novel structured identification) and experimental validation across LLMs, but lacks agent-specific insights or capability emergence insights.

### [Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/abs/2605.15164)
**Source:** arxiv | **Authors:** Pratinav Seth; Vinay Kumar Sankarapu
**Relevance:** 3/5 — Addresses safety evaluation and governance of LLM-based systems with agentic behaviors, but is primarily a position paper on assurance limitations rather than advancing agent capabilities or core model methodology.
**Depth:** 3/5 — Formalizes the audit gap concept and proposes mechanistic-evidence approaches (linear probes, activation patching), but lacks empirical validation, concrete case studies, or benchmark results demonstrating the proposed technical pivots.

### [Derivation Prompting: A Logic-Based Method for Improving Retrieval-Augmented Generation](https://arxiv.org/abs/2605.14053)
**Source:** arxiv | **Authors:** Ignacio Sastre; Guillermo Moncecchi; Aiala Ros\'a
**Relevance:** 3/5 — Derivation Prompting addresses reasoning and control in RAG systems, which is relevant to agent capabilities, but focuses on a specific prompting technique rather than core agent architecture or frontier model capabilities.
**Depth:** 3/5 — The paper provides methodology (derivation trees with rule-based constraints) and case study results showing improvement over baseline RAG, but the contribution is narrowly scoped to a prompting variant rather than a fundamental advance in reasoning or agent design.

### [GradShield: Alignment Preserving Finetuning](https://arxiv.org/abs/2605.14194)
**Source:** arxiv | **Authors:** Zhanhao Hu; Xiao Huang; Patrick Mendoza; Emad A. Alghamdi; Basel Alomair; Raluca Ada Popa; David Wag...
**Relevance:** 3/5 — Alignment and safety during finetuning is relevant to frontier model capabilities and safety thresholds, but this work focuses on filtering harmful data rather than agent-specific capabilities or mechanisms that directly enable agent reasoning/planning.
**Depth:** 3/5 — The paper presents a principled methodology (FIHS scoring + adaptive thresholding) with empirical evaluation across multiple tasks and metrics, demonstrating solid technical contribution, though it is narrowly scoped to data filtering rather than broader alignment or capability emergence questions.

### [Fusion-fission forecasts when AI will shift to undesirable behavior](https://arxiv.org/abs/2605.14218)
**Source:** arxiv | **Authors:** Neil F. Johnson; Frank Yingjie Huo
**Relevance:** 3/5 — Directly addresses model safety and behavioral shift prediction relevant to reliable agent deployment, but focuses on forecasting undesirable behavior rather than enabling agent capabilities.
**Depth:** 3/5 — Presents a mathematical framework with cross-model validation and real-world corpus confirmation, but the theoretical foundation (fusion-fission group dynamics) and its necessity over alternative safety approaches lacks detailed methodological exposition.

### [Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in Indian Judicial AI](https://arxiv.org/abs/2605.14665)
**Source:** arxiv | **Authors:** Joy Bose
**Relevance:** 3/5 — Graph-constrained generation and verification mechanisms are methodologically relevant to LLM agent reliability and reasoning, but the application is domain-specific legal reasoning rather than frontier agent capabilities.
**Depth:** 3/5 — The work presents solid methodology (IRAC graph grounding, Verifier Agent architecture) and proposes domain-appropriate evaluation metrics, but evaluation is limited to proof-of-concept scale (51 judgments) without comparison to vector RAG baselines.

### [GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation](https://arxiv.org/abs/2605.14968)
**Source:** arxiv | **Authors:** Drewry H. Morris V (MedFlow; Inc.); Luis Valles (MedFlow; Inc.); Reza Hosseini Ghomi (MedFlow; Inc.)
**Relevance:** 3/5 — Directly addresses reliability and formal verification of LLM-based agent workflows in multi-step processes, but focuses on system architecture and execution guarantees rather than frontier agent capabilities or training methods.
**Depth:** 3/5 — Presents concrete methodology (formal semantics, proof-checked contracts, swimlane trust boundaries) and real-world results (8,728 workflow runs, 97.08% completion), but the verified core subsystem—the novel technical contribution—is explicitly unfinished and not yet evaluated.

### [From Descriptive to Prescriptive: Uncover the Social Value Alignment of LLM-based Agents](https://arxiv.org/abs/2605.14034)
**Source:** arxiv | **Authors:** Jinxian Qu; Qingqing Gu; Teng Chen; Luo Ji
**Relevance:** 3/5 — Directly addresses LLM-based agent behavior alignment and decision-making, but focuses on social values and emotions rather than core agent capabilities like reasoning, planning, or tool use.
**Depth:** 2/5 — Proposes a GraphRAG-based framework with evaluation on DAILYDILEMMAS, but lacks sufficient methodological detail on the alignment mechanism and provides incremental improvements over prompt-based baselines without deeper architectural insights.

### [Emotion-Attended Stateful Memory (EASM):The Architecture for Hyper-Personalization at Scale](https://arxiv.org/abs/2605.14833)
**Source:** arxiv | **Authors:** Vineet Kotecha; Vansh Gupta
**Relevance:** 3/5 — Stateful memory and context management are relevant to LLM agent capabilities, but this work focuses on conversational personalization rather than reasoning, planning, or tool use that define frontier agent research.
**Depth:** 2/5 — The paper presents an A/B study with concrete improvements but lacks detailed methodology on the memory architecture, emotional signal extraction mechanisms, or how the approach generalizes beyond conversational personalization.

# AI digest — 2026-05-11

Rolling 7-day window. Generated automatically.

---

## Read deeply (119 items)

_High relevance and substantial depth — worth full attention._

### [SciResearcher: Scaling Deep Research Agents for Frontier Scientific Reasoning](https://arxiv.org/abs/2605.01489)
**Source:** arxiv | **Authors:** Tianshi Zheng; Rui Wang; Xiyun Li; Yangqiu Song; Tianqing Fang
**Relevance:** 5/5 — Directly addresses LLM-based agents for frontier scientific reasoning with explicit methodology for data construction, agent training via SFT and reinforcement learning, and concrete benchmark results.
**Depth:** 4/5 — Provides substantial methodology for automated agentic data construction, describes post-training approaches (SFT + RL), reports specific benchmark improvements (19.46% HLE-Bio/Chem-Gold, 13-15% gains on others), and articulates limitations of prior knowledge-graph/web-browsing approaches that motivate the contribution.

### [Evaluating Agentic AI in the Wild: Failure Modes, Drift Patterns, and a Production Evaluation Framework](https://arxiv.org/abs/2605.01604)
**Source:** arxiv | **Authors:** Mukund Pandey
**Relevance:** 5/5 — Directly addresses evaluation and deployment of LLM-based agentic systems in production, a frontier challenge for agent capabilities and reliability.
**Depth:** 4/5 — Provides concrete taxonomy of seven failure modes grounded in billion-event scale observations, empirical demonstration of metric failures, and a novel five-dimension evaluation framework with reference implementation.

### [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/abs/2605.02269)
**Source:** arxiv | **Authors:** Kei Nishimura-Gasparian; Robert McCarthy; David Lindner
**Relevance:** 5/5 — Directly addresses a critical failure mode of LLM agents (specification gaming), with systematic study of when it arises and what drives it, including the role of RL reasoning training.
**Depth:** 4/5 — Provides concrete methodology (diverse evaluation suite with eight settings), specific empirical results (exploit rates across models, effects of RL budget), and actionable findings about what drives specification gaming in reasoning models.

### [Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning](https://arxiv.org/abs/2605.02913)
**Source:** arxiv | **Authors:** Rohan Surana; Gagan Mundada; Xunyi Jiang; Chuhan Wang; Zhenwei Tang; Difan Jiao; Zihan Huang; Yuxin ...
**Relevance:** 5/5 — Directly addresses RL-based post-training and reasoning for LLMs with comprehensive methodology covering rollout design—a core capability enabler for agent performance.
**Depth:** 4/5 — Provides unified formal framework (GFCR taxonomy), criterion characterization (reliability/coverage/cost), synthesis of diverse methods, and grounded case studies across math, code, tools, and agentic benchmarks.

### [When Safety Geometry Collapses: Fine-Tuning Vulnerabilities in Agentic Guard Models](https://arxiv.org/abs/2605.02914)
**Source:** arxiv | **Authors:** Ismail Hossain; Sai Puppala; Jannatul Ferdaus; Md Jahangir Alam; Yoonpyo Lee; Syed Bahauddin Alam; S...
**Relevance:** 5/5 — Directly addresses safety and robustness of guard models deployed in agentic AI pipelines, a critical frontier concern for LLM-based agent deployment.
**Depth:** 4/5 — Provides detailed mechanistic analysis (safety geometry via SVD, CKA, Fisher information), concrete empirical results across three models, and a principled mitigation method (FW-SSR) with quantified improvements.

### [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964)
**Source:** arxiv | **Authors:** Kunvar Thaman
**Relevance:** 5/5 — Directly addresses a critical safety and capability limitation of LLM-based agents with tool use—reward hacking—across frontier models with systematic evaluation and methodology.
**Depth:** 4/5 — Provides concrete benchmark design, quantified results across 13 frontier models with detailed exploit categorization, identifies post-training trade-offs (RL vs. alignment), and tests mitigation strategies with measurable outcomes.

### [CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment](https://arxiv.org/abs/2605.06702)
**Source:** arxiv | **Authors:** Siyuan Guo; Yali Du; Hechang Chen; Yi Chang; Jun Wang
**Relevance:** 5/5 — Directly addresses LLM-based agent learning and adaptation during deployment, a core frontier capability for enabling agents to improve through interaction.
**Depth:** 4/5 — Provides principled methodology (contextual bandit formulation with no-regret guarantees), explicit memory mechanisms, and comprehensive empirical evaluation across 16 diverse tasks with concrete improvement metrics (20.9% over baselines).

### [Weblica: Scalable and Reproducible Training Environments for Visual Web Agents](https://arxiv.org/abs/2605.06761)
**Source:** arxiv | **Authors:** O\u{g}uzhan Fatih Kar; Roman Bachmann; Yuanzheng Gong; Anders Boesen Lindbo Larsen; Afshin Dehghan
**Relevance:** 5/5 — Directly addresses LLM-based agent training at scale with methodology for reproducible web navigation environments and concrete benchmark results.
**Depth:** 4/5 — Substantial technical contribution with novel HTTP-level caching and LLM-based environment synthesis mechanisms, plus comprehensive evaluation across multiple benchmarks showing competitive performance.

### [Self-Programmed Execution for Language-Model Agents](https://arxiv.org/abs/2605.06898)
**Source:** arxiv | **Authors:** Luke J. O'Connor
**Relevance:** 5/5 — Directly addresses LLM agent architecture design by introducing a novel orchestration paradigm where the model itself controls state transitions without fixed turn-to-turn policies.
**Depth:** 4/5 — Provides formal framework (agentic machines), concrete methodology (Spell language with self-editing programs and memoized effects), and empirical validation showing frontier models can operate in this regime on challenging agentic tasks.

### [The Context Gathering Decision Process: A POMDP Framework for Agentic Search](https://arxiv.org/abs/2605.07042)
**Source:** arxiv | **Authors:** Chinmaya Kausik; Adith Swaminathan; Nathan Kallus
**Relevance:** 5/5 — Directly addresses core LLM agent capability—adaptive information retrieval and context management in constrained windows—with formal theoretical framing and practical interventions.
**Depth:** 4/5 — Provides explicit methodology (POMDP formalization, predicate-based belief state, programmatic exhaustion detection) and validates with concrete benchmarks (11.4% improvement, 39% token savings) across multiple domains.

### [EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation](https://arxiv.org/abs/2605.07247)
**Source:** arxiv | **Authors:** Yi Liu; TingFeng Hui; Wei Zhang; Li Sun; Ningxin Su; Jian Wang; Sen Su
**Relevance:** 5/5 — Directly addresses LLM-based agent training by identifying and solving a critical capability gap in environment simulation—a foundational infrastructure problem for scalable agent development.
**Depth:** 4/5 — Provides formal definition of Environment Simulation Ability, rigorous benchmark with 400 samples across 167 environments, systematic evaluation revealing the state-change cliff failure mode, and a constraint-driven pipeline with concrete improvements (6.8% yield boost, 90% cost reduction).

### [Tools as Continuous Flow for Evolving Agentic Reasoning](https://arxiv.org/abs/2605.07339)
**Source:** arxiv | **Authors:** Tairan Huang; Siyu Shang; Qiang Chen; Xiu Su; Yi Chen
**Relevance:** 5/5 — Directly addresses LLM-based agent reasoning through a novel tool-chaining architecture with theoretical guarantees and a new benchmark for plan-level agentic reasoning.
**Depth:** 4/5 — Presents concrete methodology (conditional flow matching for continuous trajectory generation), formal theoretical bounds on utility convergence, and empirical evaluation on long-horizon reasoning tasks with explicit handling of generalization and error attenuation.

### [Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators](https://arxiv.org/abs/2605.06997)
**Source:** arxiv | **Authors:** Anupama Sridhar; Alexander Johansen
**Relevance:** 5/5 — Directly addresses a critical bottleneck for long-horizon LLM agents: memory-efficient context retention for tool-calling traces and chain-of-thought reasoning, with concrete architectural methodology.
**Depth:** 4/5 — Presents novel Spectral Koopman Attention mechanism with rigorous mathematical grounding (kernel ridge regression, power-iteration filtering), comprehensive benchmarking across five transfer tasks including agent-relevant evaluations (tool-trace, multi-hop retrieval), and systematic ablations isolating the source of gains.

### [When Less is Enough: Efficient Inference via Collaborative Reasoning](https://arxiv.org/abs/2605.01111)
**Source:** arxiv | **Authors:** Yilei Chen; Sharut Gupta; Yannis Paschalidis; Ayush Sekhari; Aldo Pacchiano
**Relevance:** 4/5 — Directly addresses inference efficiency for LLM-based reasoning systems through a collaborative two-stage framework, which materially affects what agents can do in practice by reducing computational cost.
**Depth:** 4/5 — Presents concrete methodology (length-penalized joint training objective), specific architectural design (dual-model collaboration), and quantified results (60% token reduction on AIME/GPQA), with clear motivation rooted in limitations of end-to-end inference.

### [S^3-R1: Learning to Retrieve and Answer Step-by-Step with Synthetic Data](https://arxiv.org/abs/2605.01248)
**Source:** arxiv | **Authors:** Harsh Goel; Akhil Udathu; Susmija Jabireddy; Pradnesh Kalkar; Atharva Parulekar
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities (tool-use, search, reasoning) with a concrete training methodology for improving agentic behavior.
**Depth:** 4/5 — Presents clear methodology (synthetic data curation pipeline with retrieval-based verification, dense reward structure for credit assignment) and quantitative results (10% improvement on out-of-domain evaluation).

### [AI Alignment via Incentives and Correction](https://arxiv.org/abs/2605.01643)
**Source:** arxiv | **Authors:** Rohit Agarwal; Joshua Lin; Mark Braverman; Elad Hazan
**Relevance:** 4/5 — Directly addresses alignment and oversight mechanisms in LLM-based agent pipelines, with explicit focus on solver-auditor interactions and how reward design shapes agent behavior.
**Depth:** 4/5 — Provides formal game-theoretic modeling of the solver-auditor interaction, proposes a bandit-based bilevel optimization procedure for reward design, and demonstrates experimental results on LLM coding tasks showing improved alignment outcomes.

### [RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs](https://arxiv.org/abs/2605.01913)
**Source:** arxiv | **Authors:** Sadia Asif; Mohammad Mohammadi Amiri
**Relevance:** 4/5 — Directly addresses a frontier model capability concern—safety alignment stability—that materially affects what LLM agents can reliably do in deployment, with clear methodology on representation-level mechanisms.
**Depth:** 4/5 — Provides concrete mechanistic analysis of alignment degradation through representation drift, introduces a novel geometry-preserving fine-tuning framework, and demonstrates results across multiple model families and safety benchmarks.

### [TRAP: Tail-aware Ranking Attack for World-Model Planning](https://arxiv.org/abs/2605.01950)
**Source:** arxiv | **Authors:** Siyuan Duan; Ke Zhang; Xizhao Luo
**Relevance:** 4/5 — Directly addresses security and robustness of world-model-based agents, a frontier capability that materially affects what LLM and learned-model agents can safely do.
**Depth:** 4/5 — Provides clear methodology (tail-aware ranking loss with dual gating mechanisms) and concrete experimental results on DreamerV3 and TD-MPC2 demonstrating vulnerability exploitation and performance degradation.

### [Break the Block: Dynamic-size Reasoning Blocks for Diffusion Large Language Models via Monotonic Entropy Descent with Reinforcement Learning](https://arxiv.org/abs/2605.02263)
**Source:** arxiv | **Authors:** Yan Jiang; Ruihong Qiu; Zi Huang
**Relevance:** 4/5 — Directly addresses reasoning capabilities in diffusion LLMs through a novel post-training framework that enhances coherence in semi-autoregressive generation, a frontier approach to scaling reasoning.
**Depth:** 4/5 — Provides clear methodology (monotonic entropy descent with RL for dynamic block sizing), empirical observations motivating the approach (entropy trends in correct vs. incorrect reasoning), and systematic evaluation across reasoning benchmarks.

### [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375)
**Source:** arxiv | **Authors:** Marc Dymetman
**Relevance:** 4/5 — Directly addresses a fundamental problem in RLVR (reinforcement learning from verifiable rewards), a core training method for improving LLM reasoning and agent capabilities.
**Depth:** 4/5 — Provides rigorous theoretical analysis of diversity collapse with explicit mathematical formulas, identifies the structural failure mode under model misspecification, and proposes alternative divergences as solutions.

### [Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent](https://arxiv.org/abs/2605.02469)
**Source:** arxiv | **Authors:** Yao Shu; Chenxing Wei; Hongbin Lin; Shuang Qiu; Hui Xiong
**Relevance:** 4/5 — Directly addresses training methods for LLM agents via reinforcement learning with verifiable rewards (RLVR), a frontier approach to aligning agent behavior with checkable outcomes.
**Depth:** 4/5 — Provides rigorous methodology for weighted SFT objectives with finite-sample analysis, explicit error decomposition, and empirical validation on Qwen, addressing concrete limitations of prior RL training approaches.

### [StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k](https://arxiv.org/abs/2605.02568)
**Source:** arxiv | **Authors:** Jaber Jaber; Osama Jaber
**Relevance:** 4/5 — Compressed Sparse Attention is a frontier mechanism that directly enables longer-context reasoning in LLM agents by improving model capabilities through efficient scaling.
**Depth:** 4/5 — The paper provides detailed methodology for memory-efficient streaming top-k computation, concrete memory/performance results across design-space sweeps, and identifies a critical bottleneck (materialize path) that prior work failed to address.

### [Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models](https://arxiv.org/abs/2605.02626)
**Source:** arxiv | **Authors:** Inoussa Mouiche
**Relevance:** 4/5 — DPO and preference optimization are frontier training methods that directly affect LLM capability and behavior, making models suitable for agentic tasks, though not directly about agent architecture.
**Depth:** 4/5 — Paper provides clear methodology (gradient-gating mechanism), diagnosis of optimization pathology (squeezing effect), and concrete experimental results across architectures showing improved training stability and chosen-response likelihood.

### [Towards Multi-Agent Autonomous Reasoning in Hydrodynamics](https://arxiv.org/abs/2605.01102)
**Source:** arxiv | **Authors:** Jinpai Zhao; Albert Cerrone; Joannes Westerink; Clint Dawson
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent orchestration, planning, tool use, and context management—core frontier agent capabilities—with explicit methodology for coordinating specialized agents through structured execution graphs.
**Depth:** 4/5 — Provides concrete architectural design (Layer Execution Graph, planner/specialist/consolidator roles), detailed ablations and stress tests (37 queries, 6 complexity categories, parallel degradation analysis), and systematic evaluation of a key bottleneck (context saturation) in single-agent systems.

### [Faithful Mobile GUI Agents with Guided Advantage Estimator](https://arxiv.org/abs/2605.01208)
**Source:** arxiv | **Authors:** Haowen Hu; Pengzhou Cheng; Zheng Wu; Lingzhong Dong; Gongshen Liu; Zhuosheng Zhang
**Relevance:** 4/5 — Directly addresses LLM-based GUI agents' core capability limitation (faithfulness and grounding), with explicit methodology for improving agent reasoning and action consistency.
**Depth:** 4/5 — Substantial contribution with two-stage training pipeline (SFT + RFT), novel guided advantage estimator mechanism (GuAE) built on GRPO, concrete benchmark results (Trap SR 13.88% → 80.21%), and systematic diagnosis of agent failure modes.

### [Agentic AI Systems Should Be Designed as Marginal Token Allocators](https://arxiv.org/abs/2605.01214)
**Source:** arxiv | **Authors:** Siqi Zhu
**Relevance:** 4/5 — Directly addresses LLM-based agent design and resource allocation across reasoning, planning, verification, and execution layers—core agent system architecture.
**Depth:** 4/5 — Provides explicit methodology (marginal token allocation framework) that unifies four design layers and predicts failure modes, offering concrete research agenda with mechanistic insight into agent system behavior.

### [EO-Gym: A Multimodal, Interactive Environment for Earth Observation Agents](https://arxiv.org/abs/2605.01250)
**Source:** arxiv | **Authors:** Sai Ma; Zhuang Li; Sichao Li; Xinyue Xu; Ruibiao Zhu; Tony Boston; John A. Taylor
**Relevance:** 4/5 — Directly addresses LLM-based agents with tool use, planning, and multi-step reasoning in a structured interactive environment with clear methodology and benchmark evaluation.
**Depth:** 4/5 — Provides concrete methodology (Gymnasium-style framework with 35 specialized tools, 9,078 trajectory benchmark), explicit evaluation results (Pass@3 improvements from 0.49 to 0.74), and identifies limitations of general VLMs on temporal/cross-modal agent reasoning.

### [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2605.01293)
**Source:** arxiv | **Authors:** Jie-Jing Shao; Haiyan Yin; Yueming Lyu; Xingrui Yu; Lan-Zhe Guo; Ivor Tsang; James Kwok; Yu-Feng Li
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities for long-horizon planning through skill induction, a core frontier problem in agentic reasoning.
**Depth:** 4/5 — Proposes a neuro-symbolic methodology that explicitly synthesizes control flows and variable binding from traces, with experimental validation on agentic tasks demonstrating improvements over baselines.

### [Segment-Aligned Policy Optimization for Multi-Modal Reasoning](https://arxiv.org/abs/2605.01327)
**Source:** arxiv | **Authors:** Lei Gao; Zhuoming Li; Mengxi Jia; Jiakang Yuan; Hongbo Sun; Hao Sun; Xuelong Li
**Relevance:** 4/5 — Directly addresses RL-based training methods for LLM reasoning and agent decision-making, a frontier capability that materially affects what agents can accomplish.
**Depth:** 4/5 — Presents novel methodology (segment-aligned MDP abstraction with step-wise value estimation) and demonstrates concrete improvements on reasoning benchmarks with analysis of training stability and credit assignment.

### [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/abs/2605.01566)
**Source:** arxiv | **Authors:** Florian Valentin Wunderlich; Lars Benedikt Kaesberg; Jan Philip Wahle; Terry Ruas; Bela Gipp
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent inference methods (debate, mixture-of-agents) and their computational tradeoffs, which is core to understanding agent capability scaling.
**Depth:** 4/5 — Provides systematic methodology comparing multiple inference strategies across configurations with concrete Pareto-optimality analysis, benchmark results, and design guidelines for multi-agent efficiency.

### [NeuroState-Bench: A Human-Calibrated Benchmark for Commitment Integrity in LLM Agent Profiles](https://arxiv.org/abs/2605.01847)
**Source:** arxiv | **Authors:** Jia Xiao
**Relevance:** 4/5 — Directly addresses a frontier agent capability—commitment integrity across multi-turn reasoning—through a novel evaluation methodology that exposes failures in LLM agent profiles.
**Depth:** 4/5 — Contributes substantial methodology (human-calibrated benchmarking with 0.977 inter-rater agreement, deterministic task construction, side-query probes) and concrete diagnostic results (0.8469 AUC for commitment failure detection) that reveal misalignment between task success and state coherence.

### [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087)
**Source:** arxiv | **Authors:** Chloe Li; Sara Price; Samuel Marks; Jon Kutasov
**Relevance:** 4/5 — Directly addresses alignment training methodology and generalization for frontier LLMs, with clear implications for agent behavior and safety—a core capability frontier.
**Depth:** 4/5 — Provides explicit methodology (midtraining on synthetic spec documents), concrete empirical results (54% to 7% agentic misalignment reduction), and systematic study of what spec properties improve generalization.

### [NORA: A Harness-Engineered Autonomous Research Agent for End-to-End Spatial Data Science](https://arxiv.org/abs/2605.02092)
**Source:** arxiv | **Authors:** Bing Zhou; Xiao Huang; Huan Ning; Qiusheng Wu; Diya Li; Ziyi Zhang
**Relevance:** 4/5 — NORA is a concrete LLM-based agent system with specialized reasoning, planning, and tool-use capabilities for autonomous research workflows, directly addressing agent architecture and deployment challenges.
**Depth:** 4/5 — The paper provides substantial methodology on harness engineering (lifecycle hooks, safety gates, generator-evaluator separation, state persistence) and domain-specialized skill design, with evaluation across multiple dimensions by experts.

### [Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/abs/2605.02168)
**Source:** arxiv | **Authors:** Wenyi Wu; Sibo Zhu; Kun Zhou; Biwei Huang
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for long-horizon planning with a multi-agent decomposition framework and systematic analysis of compute allocation across planner, actor, and memory components.
**Depth:** 4/5 — Provides concrete methodology (compute-allocation analysis, planner-centric RL optimization with VLM-as-judge rewards) and empirical results across multiple benchmarks (web navigation, OS control, tool use) with publicly released code.

### [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178)
**Source:** arxiv | **Authors:** Haixin Wang; Hejie Cui; Chenwei Zhang; Xin Liu; Shuowei Jin; Shijie Geng; Xinyang Zhang; Nasser Zalm...
**Relevance:** 4/5 — Directly addresses training stability and exploration efficiency for LLM-based agents in multi-turn RL, a frontier capability problem that materially affects agent reasoning and task performance.
**Depth:** 4/5 — Proposes explicit uncertainty-guided methodology with token-level and turn-level mechanisms, demonstrates concrete results across multiple environments (WebShop, ALFWorld, SearchQA), and identifies and addresses root causes of training instability.

### [MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing](https://arxiv.org/abs/2605.02199)
**Source:** arxiv | **Authors:** Nishant Bhargava; Rodrigo Sobral Barrento
**Relevance:** 4/5 — Directly addresses memory mechanisms for long-term LLM agents, a core capability enabling agent persistence and reasoning over extended interactions.
**Depth:** 4/5 — Provides rigorous methodology (exact package-oracle protocol with MILP certification) and concrete evaluation framework separating memory writing from retrieval effects, enabling precise localization of agent memory quality.

### [Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates](https://arxiv.org/abs/2605.02236)
**Source:** arxiv | **Authors:** Pawel Kaplanski (Kaplanski AI Lab)
**Relevance:** 4/5 — Directly addresses LLM agent behavior in recursive loops—a fundamental mechanism for agents that iteratively refine reasoning, plan, and interact with their own outputs; context-update rules are agent-architecture design choices.
**Depth:** 4/5 — Rigorous empirical methodology (30-step loops, falsification battery, multiple context-update protocols, within-vendor replication) with concrete quantitative results (persistence/escape rates, dose-response curves, confidence intervals) that reveal design-relevant trade-offs in recursive agent architectures.

### [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://arxiv.org/abs/2605.02240)
**Source:** arxiv | **Authors:** Ruoqi Liu; Imran Q. Mohiuddin; Austin J. Schoeffler; Kavita Renduchintala; Ashwin Nayak; Prasantha L...
**Relevance:** 4/5 — Directly evaluates LLM-based agents on long-horizon planning and tool use in a realistic environment with execution-grounded verification, a frontier capability for autonomous agents.
**Depth:** 4/5 — Provides substantial methodology (real EHR APIs, structured checkpoints, execution-grounded verification across 670 tasks) and concrete results (46% best performance, 19% for open-source) revealing systematic capability gaps.

### [EngiAgent: Fully Connected Coordination of LLM Agents for Solving Open-ended Engineering Problems with Feasible Solutions](https://arxiv.org/abs/2605.02289)
**Source:** arxiv | **Authors:** Xiyuan Zhou; Ruixi Zou; Xinlei Wang; Yuheng Cheng; Yan Xu; Junhua Zhao; Jinjin Gu
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent coordination for complex problem-solving with explicit methodology on agent specialization, feedback routing, and feasibility constraints.
**Depth:** 4/5 — Provides detailed architectural design (fully connected coordinator, specialized agents, flexible feedback mechanisms), empirical validation across four domains, and identifies concrete limitations of prior pipeline-based approaches.

### [Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding](https://arxiv.org/abs/2605.02290)
**Source:** arxiv | **Authors:** Taewon Yun; Jisu Shin; Jeonghwan Choi; Seunghwan Bang; Hwanjun Song
**Relevance:** 4/5 — Directly addresses frontier capability enabling LLM agents: making long-chain-of-thought reasoning practical through distillation, a critical bottleneck for deploying reasoning-capable agents.
**Depth:** 4/5 — Presents concrete methodology (collaborative multi-teacher decoding with perplexity-based scoring and beam search) and empirical results showing near-teacher performance with reduced supervision, addressing a real limitation of prior curation approaches.

### [Controllable and Verifiable Process Data Synthesis for Process Reward Models](https://arxiv.org/abs/2605.02395)
**Source:** arxiv | **Authors:** Yinghui Chi; Lucien Wang
**Relevance:** 4/5 — Process reward models are a frontier capability directly enabling LLM-based reasoning agents to improve through fine-grained step-level supervision, which materially affects agent reasoning quality.
**Depth:** 4/5 — The paper presents concrete methodology (template-aware error injection, symbolic recomputation, prefix-validity verification) with experimental results showing improvements on logical and mathematical reasoning benchmarks and detailed step-level evaluation.

### [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)
**Source:** arxiv | **Authors:** Jianing Wang; Linsen Guo; Zhengyu Chen; Qi Guo; Hongyu Zang; Wenjie Shi; Haoxiang Ma; Xiangyu Xi; Xi...
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning mechanisms and orchestration frameworks, with focus on scaling thinking as an internalized skill within agents.
**Depth:** 4/5 — Provides systematic empirical methodology for understanding heavy thinking as a two-stage pipeline, compares against baselines, and demonstrates RL-based scaling with concrete results across domains.

### [FitText: Evolving Agent Tool Ecologies via Memetic Retrieval](https://arxiv.org/abs/2605.02411)
**Source:** arxiv | **Authors:** Kyle Zheng; Han Zhang; Renliang Sun; Chenchen Ye; Wei Wang
**Relevance:** 4/5 — Directly addresses tool use in LLM agents through dynamic retrieval mechanisms that evolve during execution, a core capability for agent reasoning and planning.
**Depth:** 4/5 — Presents clear methodology (memetic retrieval with iterative refinement and evolutionary selection) and concrete benchmark results (43k and 16k tool settings with significant improvements) that illuminate why and how dynamic tool discovery works.

### [The Model Knows, the Decoder Finds: Future Value Guided Particle Power Sampling](https://arxiv.org/abs/2605.02427)
**Source:** arxiv | **Authors:** Tu Nguyen; Rasul Tutunov; Xiaotong Ji; Matthieu Zimmer
**Relevance:** 4/5 — Directly addresses inference-time decoding for LLM reasoning and solution discovery, a frontier capability that materially affects what base models can accomplish without retraining.
**Depth:** 4/5 — Presents novel methodology (APPS algorithm with future-value-guided particle reweighting) grounded in power sampling theory, includes empirical evaluation across reasoning benchmarks with concrete accuracy-runtime trade-offs, and identifies the core bottleneck (mode location) that motivates the approach.

### [DataClaw: A Process-Oriented Agent Benchmark for Exploratory Real-World Data Analysis](https://arxiv.org/abs/2605.02503)
**Source:** arxiv | **Authors:** Qiaohong Zhang; Weihao Ye; Jialong Chen; Yi Luo; BoYuan Li; Bowen Deng; Zibin Zheng; Jianhao Lin; We...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation through a comprehensive benchmark for autonomous data analysis agents, falling squarely within frontier agent research.
**Depth:** 4/5 — Provides substantial methodology (process-oriented evaluation design, intermediate milestone annotations) and concrete results (2.06M records, 492 tasks, detailed performance metrics across eight LLMs with process-level analysis revealing partial progress and exploration strategies).

### [On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length](https://arxiv.org/abs/2605.02572)
**Source:** arxiv | **Authors:** Sunghwan Kim; Junhee Cho; Beong-woo Kwak; Taeyoon Kwon; Liang Wang; Nan Yang; Xingxing Zhang; Furu W...
**Relevance:** 4/5 — Directly addresses how to train LLM-based agents for long-horizon sequential decision-making, a core capability bottleneck for agent reasoning and planning.
**Depth:** 4/5 — Provides systematic empirical methodology with controlled task construction, identifies specific training failure modes (exploration, credit assignment), and proposes horizon reduction as a principle with generalization results.

### [eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization](https://arxiv.org/abs/2605.02905)
**Source:** arxiv | **Authors:** Pei-Chun Su
**Relevance:** 4/5 — KV cache compression directly enables longer context and more efficient deployment of LLM-based agents by reducing memory bottlenecks during inference.
**Depth:** 4/5 — Strong theoretical grounding in random matrix theory with rigorous guarantees (BBP phase transition, bias bounds, quantization distortion), plus comprehensive experimental validation across model scales and downstream tasks including retrieval-heavy agent scenarios.

### [Delay, Plateau, or Collapse: Evaluating the Impact of Systematic Verification Error on RLVR](https://arxiv.org/abs/2605.02909)
**Source:** arxiv | **Authors:** Kazuki Egashira; Mark Vero; Jasper Dekoninck; Florian E. Dorner; Robin Staab; Martin Vechev
**Relevance:** 4/5 — Directly addresses a critical training methodology (RLVR) for improving LLM reasoning capabilities, which is core frontier work on enabling agent behavior.
**Depth:** 4/5 — Provides controlled experimental methodology, identifies systematic error patterns (false positives vs. negatives), and challenges prior assumptions about verifier robustness with concrete results showing when performance plateaus or collapses.

### [Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943)
**Source:** arxiv | **Authors:** Minbyul Jeong
**Relevance:** 4/5 — Directly addresses LLM-based agent training through multi-turn agentic RL in a clinical domain, with focus on tool use, reasoning, and training methodology for agents.
**Depth:** 4/5 — Provides concrete empirical analysis of agent training failure modes (verbosity collapse, tool-use degradation), identifies root causes (reward misalignment), and proposes TT-OPD with measurable improvements (+3.9pp average) and detailed ablations.

### [Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation](https://arxiv.org/abs/2605.02944)
**Source:** arxiv | **Authors:** Xin-Ye Li; Ren-Biao Liu; Yun-Ji Zhang; Hui Sun; Zheng Xie; Ming Li
**Relevance:** 4/5 — Post-training RL methods for LLM code generation directly affect agent capability for tool use and autonomous problem-solving, a frontier training technique that materially impacts what LLM-based agents can accomplish.
**Depth:** 4/5 — The paper provides rigorous methodology (controlled experiments across models/algorithms), concrete empirical results (pass-rate vs. binary reward comparison), and mechanistic analysis (gradient direction study) that explains why a common approach fails and motivates better reward design.

### [DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment](https://arxiv.org/abs/2605.03327)
**Source:** arxiv | **Authors:** Hongbo Jin; Rongpeng Zhu; Zhongjing Du; Xu Jiang; Jingqi Tian; Qiaoman Zhang; Jiayu Ding
**Relevance:** 4/5 — Directly addresses RL training methods for LLM reasoning and agent alignment, a frontier capability that enables complex agent behavior.
**Depth:** 4/5 — Presents novel methodology (distribution-guided framework) with explicit motivation (fine-grained credit assignment, gradient stability) and addresses concrete limitations of prior work (GRPO's coarse-grained assignment).

### [More Thinking, More Bias: Length-Driven Position Bias in Reasoning Models](https://arxiv.org/abs/2605.06672)
**Source:** arxiv | **Authors:** Xiao Wang
**Relevance:** 4/5 — Directly addresses a critical capability and limitation of reasoning-tuned models (DeepSeek-R1 and CoT-enabled systems) that materially affects their reliability in agent deployment and evaluation contexts.
**Depth:** 4/5 — Provides rigorous methodology (causal truncation intervention, partial correlations across 13 configurations, diagnostic toolkit), concrete quantitative results (PBS scores, effect sizes p<0.05), and explicit mechanistic insights into how reasoning length interacts with bias in frontier models.

### [When Does a Language Model Commit? A Finite-Answer Theory of Pre-Verbalization Commitment](https://arxiv.org/abs/2605.06723)
**Source:** arxiv | **Authors:** Long Zhang; Wei-neng Chen; Feng-feng Wei; Zi-bo Qin
**Relevance:** 4/5 — Directly addresses agent decision-making internals by studying when and how LLMs stabilize answer preferences during reasoning, which is foundational to understanding agent planning and commitment.
**Depth:** 4/5 — Provides concrete methodology (finite-answer projection, log-odds metrics) with systematic empirical results (17-31 token lead measurements, linearity recovery from hidden states) and explicit diagnostic separation from confounds.

### [When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR: Structured Critic--Actor Loop for Agentic Reasoning](https://arxiv.org/abs/2605.06772)
**Source:** arxiv | **Authors:** Vasilis Niarchos; Constantinos Papageorgakis; Alexander G. Stapleton; Sokratis Trifinopoulos
**Relevance:** 4/5 — Directly addresses LLM-based agent design through an Actor-Critic-Judge framework for iterative reasoning, studying how agent-human interaction structures affect performance on complex tasks.
**Depth:** 4/5 — Provides systematic methodology with controlled ablations across actor personas, critic strategies, and model scales, plus concrete results showing how interaction structures and model pairings affect performance on frontier reasoning tasks.

### [Towards Security-Auditable LLM Agents: A Unified Graph Representation](https://arxiv.org/abs/2605.06812)
**Source:** arxiv | **Authors:** Chaofan Li; Lyuye Zhang; Jintao Zhai; Siyue Feng; Xichun Yang; Huahao Wang; Shihan Dou; Yu Ji; Yutao...
**Relevance:** 4/5 — Directly addresses security auditing and safety of LLM-based agents through a novel graph representation framework that captures agent execution semantics and enables risk assessment.
**Depth:** 4/5 — Presents a well-motivated methodology (Agent-BOM graph model with static/dynamic layers and semantic edges) with concrete evaluation against real-world attack scenarios including memory poisoning, tool misuse, and supply-chain hijacking.

### [Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning](https://arxiv.org/abs/2605.06840)
**Source:** arxiv | **Authors:** Sixing Chen; Ji-An Li; Saner Cakir; Sinan Akcali; Kayla Lee; Marcelo G. Mattar
**Relevance:** 4/5 — Directly addresses frontier LLM agent capability (planning and reasoning) with methodology for understanding how reasoning models structure deliberation.
**Depth:** 4/5 — Introduces novel interpretability method (search tree extraction), provides concrete empirical results on planning structure, and offers causal interventions revealing fundamental differences between LLM and human planning.

### [Agentick: A Unified Benchmark for General Sequential Decision-Making Agents](https://arxiv.org/abs/2605.06869)
**Source:** arxiv | **Authors:** Roger Creus Castanyer; Pablo Samuel Castro; Glen Berseth
**Relevance:** 4/5 — Directly addresses evaluation of LLM-based agents and hybrid agents across sequential decision-making, with concrete methodology and benchmark design enabling fair comparison.
**Depth:** 4/5 — Provides substantial empirical infrastructure with 37 tasks, multiple agent modalities, detailed evaluation across 90K+ episodes revealing performance patterns, and identifies key insights (reasoning harness multiplies LLM performance 3-10x, ASCII outperforms natural language).

### [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
**Source:** arxiv | **Authors:** Hariom Tatsat; Ariye Shater
**Relevance:** 4/5 — Directly addresses interpretability and failure diagnosis of LLM-based agents' tool-use decisions, a core capability that enables reliable agent deployment.
**Depth:** 4/5 — Presents concrete mechanistic-interpretability methodology using SAEs and linear probes with feature ablation, evaluated on multi-step trajectories across multiple models (Nemotron, GPT-OSS, Gemma).

### [Mitigating Cognitive Bias in RLHF by Altering Rationality](https://arxiv.org/abs/2605.06895)
**Source:** arxiv | **Authors:** Tiffany Horter; Andrew Markham; Niki Trigoni; Serena Booth
**Relevance:** 4/5 — RLHF is a critical training method for frontier LLMs that directly affects model capabilities and agent behavior; improving robustness to human feedback bias materially impacts model quality for agent deployment.
**Depth:** 4/5 — The work presents clear methodology (dynamic rationality parameter adjustment via LLM-as-judge), concrete empirical results on bias mitigation, and identifies a real limitation of prior fixed-beta approaches.

### [Learning and Reusing Policy Decompositions for Hierarchical Generalized Planning with LLM Agents](https://arxiv.org/abs/2605.06957)
**Source:** arxiv | **Authors:** Shirin Sohrabi; Haritha Ananthakrishnan; Harsha Kokel; Kavitha Srinivas; Michael Katz
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and planning through hierarchical task decomposition and policy learning, with concrete methodology for improving agent capability.
**Depth:** 4/5 — Presents a substantive approach combining generalized planning with component extraction, includes methodology for decomposition and semantic retrieval, and provides quantified benchmark results with ablation evidence (62.5% vs near-zero reuse).

### [Behavior Cue Reasoning: Monitorable Reasoning Improves Efficiency and Safety through Oversight](https://arxiv.org/abs/2605.07021)
**Source:** arxiv | **Authors:** Christopher Z. Cui; Taylor W. Killian; Prithviraj Ammanabrolu
**Relevance:** 4/5 — Directly addresses LLM agent safety, controllability, and oversight through a novel mechanism (Behavior Cues) that enables monitoring of reasoning processes—core to safe agent deployment.
**Depth:** 4/5 — Introduces clear methodology (training models to emit interpretable token sequences, RL-based monitor fine-tuning), provides concrete results (50% token pruning efficiency, 96% safe action recovery), and demonstrates evaluation across multiple domains.

### [2.5-D Decomposition for LLM-Based Spatial Construction](https://arxiv.org/abs/2605.07066)
**Source:** arxiv | **Authors:** Paul Whitten; Li-Jen Chen; Sharath Baddam
**Relevance:** 4/5 — Directly addresses LLM-based agent capability (spatial reasoning for autonomous construction) with a neuro-symbolic method that materially improves agent performance on structured tasks.
**Depth:** 4/5 — Provides clear methodology (2.5-D decomposition principle), concrete benchmarks (94.6% vs 90.3% GPT-4o baseline, ablation showing 50.7pp contribution), and demonstrates transfer across hardware and domains (IGLU tasks).

### [TeamBench: Evaluating Agent Coordination under Enforced Role Separation](https://arxiv.org/abs/2605.07073)
**Source:** arxiv | **Authors:** Yubin Kim; Chanwoo Park; Taehan Kim; Eugene Park; Samuel Schmidgall; Salman Rahman; Chunjong Park; C...
**Relevance:** 4/5 — Directly addresses LLM-based agent coordination and evaluation, a frontier capability for multi-agent systems, with methodology for enforcing role separation.
**Depth:** 4/5 — Provides concrete benchmark design (851 templates, 931 instances), systematic evaluation methodology comparing prompt-only vs. enforced separation, quantitative results (3.6× code-edit cases, 49% false approvals), and human study validation exposing coordination patterns.

### [SREGym: A Live Benchmark for AI SRE Agents with High-Fidelity Failure Scenarios](https://arxiv.org/abs/2605.07161)
**Source:** arxiv | **Authors:** Jackson Clark; Yiming Su; Saad Mohammad Rafid Pial; Yifang Tian; Lily Gniedziejko; Hans-Arno Jacobse...
**Relevance:** 4/5 — SREGym is a benchmark designed specifically to evaluate LLM-based agents in production system diagnosis and mitigation, directly addressing agent evaluation methodology and capability assessment.
**Depth:** 4/5 — The work provides substantial methodology (modular, extensible benchmark architecture with fault/noise injectors simulating realistic failure modes) and concrete results (evaluation of frontier agents showing 40% performance variance across failure types).

### [HMACE: Heterogeneous Multi-Agent Collaborative Evolution for Combinatorial Optimization](https://arxiv.org/abs/2605.07214)
**Source:** arxiv | **Authors:** Yuping Yan; Jirui Han; Fei Ming; Yuanshuai Li; Yaochu Jin
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for optimization, featuring multi-agent reasoning, planning, and memory—core agent capabilities—applied to a well-defined problem domain.
**Depth:** 4/5 — Provides explicit methodology (role-specialized agents, behavior-aware retrieval, archive updates) and concrete quantitative results (token efficiency, quality gaps) on multiple benchmarks with clear comparison to baselines.

### [MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory](https://arxiv.org/abs/2605.07242)
**Source:** arxiv | **Authors:** Yang Zhao; Chengxiao Dai; Mengying Kou; Yue Xiu
**Relevance:** 4/5 — Directly addresses a core infrastructure problem in LLM-based agent memory management—cascade failures when source artifacts are invalidated—which is essential for reliable long-horizon agentic systems.
**Depth:** 4/5 — Provides formal problem definition, a principled repair contract with algorithmic solution (s-t min-cut reduction), and quantitative experiments on ToolBench and MemoryArena demonstrating substantial improvements (0% invalidated exposure vs. 69.8-94.3% baseline).

### [Can Agents Price a Reaction? Evaluating LLMs on Chemical Cost Reasoning](https://arxiv.org/abs/2605.07251)
**Source:** arxiv | **Authors:** Yuyang Wu; Yue Huang; Shuaike Shen; Xujian Wang; Shuhao Zhang; Qiyao Xue; Weichen Liu; Runtian Gao; ...
**Relevance:** 4/5 — Directly evaluates LLM-based agents on tool use and reasoning tasks with rigorous methodology, addressing a gap in scientific agent evaluation.
**Depth:** 4/5 — Provides substantial empirical methodology (1,427-reaction benchmark with ground truth evaluation, stage-level diagnostics, noise-injection analysis) and concrete results revealing specific failure modes in agent reasoning and tool use.

### [Signal Reshaping for GRPO in Weak-Feedback Agentic Code Repair](https://arxiv.org/abs/2605.07276)
**Source:** arxiv | **Authors:** Jia Li; Yuxin Su; Ting Peng; Hailiang Huang; Yuetang Deng; Michael R. Lyu
**Relevance:** 4/5 — Directly addresses LLM-agent RL training methodology (GRPO signal design) for code-repair agents with explicit focus on weak feedback challenges and agentic tool use.
**Depth:** 4/5 — Provides concrete methodology (layered rewards, process-score weighting, rollout governance), controlled ablations with quantified results (0.385→0.535 accuracy, 23.50→17.02 steps), and clear analysis of what signal properties enable meaningful RL in agent settings.

### [SOM: Structured Opponent Modeling for LLM-based Agents via Structural Causal Model](https://arxiv.org/abs/2605.07301)
**Source:** arxiv | **Authors:** Shiyue Cao; Pei Xu; Likun Yang; Lei Cui; Xiaotang Chen; Kaiqi Huang
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and decision-making in multi-agent environments through structured opponent modeling, a core capability for strategic agent behavior.
**Depth:** 4/5 — Proposes explicit methodology (Structural Causal Models) for separating opponent model construction from prediction, with evaluation on multiple benchmarks demonstrating improvements over baselines.

### [When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory](https://arxiv.org/abs/2605.07313)
**Source:** arxiv | **Authors:** Jiaqi Shao; Yiyi Lu; Yunzhen Zhang; Bing Luo
**Relevance:** 4/5 — Directly addresses a core agent capability—memory retrieval and usability under scale—with rigorous evaluation methodology for LLM-based agents.
**Depth:** 4/5 — Presents a novel evaluation protocol with multiple diagnostic metrics, concrete empirical results across different memory architectures and models, and identifies failure modes that challenge prior fixed-snapshot evaluation approaches.

### [Implicit Compression Regularization: Concise Reasoning via Internal Shorter Distributions in RL Post-Training](https://arxiv.org/abs/2605.07316)
**Source:** arxiv | **Authors:** Chen Wang; Hexuan Deng; Yining Zhang; Yuchen Zhang; Jionghao Bai; Zhaochun Li; Ge Lan; Yue Wang
**Relevance:** 4/5 — Directly addresses a frontier capability problem in LLM reasoning agents—controlling reasoning trace length while maintaining correctness—using RL post-training, a core technique for agent ability development.
**Depth:** 4/5 — Provides clear methodology (implicit compression signal from shortest correct responses, formalized via length-accuracy correlation dynamics) and concrete experimental results across multiple benchmarks showing Pareto frontier improvements.

### [Confidence-Aware Alignment Makes Reasoning LLMs More Reliable](https://arxiv.org/abs/2605.07353)
**Source:** arxiv | **Authors:** Kejia Chen; Jiawen Zhang; Yihong Wu; Kewei Gao; Jian Lou; Zunlei Feng; Mingli Song; Ruoxi Jia
**Relevance:** 4/5 — Directly addresses frontier reasoning LLM capabilities through confidence calibration and inference-time pruning—core mechanisms for reliable agent reasoning and planning.
**Depth:** 4/5 — Introduces novel methodology (token-level confidence alignment via DPO, dynamic branch pruning with CaT), concrete benchmarks across ten datasets (AIME'24/25, others), and releases annotated dataset for fine-grained analysis.

### [GraphReAct: Reasoning and Acting for Multi-step Graph Inference](https://arxiv.org/abs/2605.07357)
**Source:** arxiv | **Authors:** Xingtong Yu; Zhongwei Kuai; Chang Zhou; Xuanting Xie; Renhe Jiang; Xikun Zhang; Hong Cheng; Xinming ...
**Relevance:** 4/5 — Directly addresses reasoning-acting frameworks for LLMs extended to graph-structured data, with explicit methodology for multi-step inference through interleaved retrieval and refinement actions.
**Depth:** 4/5 — Provides concrete architectural contributions (topological vs. semantic retrieval actions, context refinement mechanism) with systematic evaluation across six benchmarks demonstrating consistent improvements.

### [LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning](https://arxiv.org/abs/2605.07505)
**Source:** arxiv | **Authors:** Yubin Wu; Zicheng Cai; Liping Ning; Hua Wang; Zhi Chen; Yaohua Tang; Hao Chen
**Relevance:** 4/5 — Directly addresses LLM-based GUI agents through training methodology (knowledge distillation, RL) that materially improves agent capability and on-device deployment.
**Depth:** 4/5 — Contributes novel methodology (Guided On-policy Distillation, Multi-solution Dual-level GRPO) with clear mechanisms, systematic benchmarking across datasets, and ablation studies demonstrating capability gains for 2B/3B models.

### [AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents](https://arxiv.org/abs/2605.07926)
**Source:** arxiv | **Authors:** Zhengkang Guo; Yiyang Li; Lin Qiu; Xiaohua Wang; Jingwen Xv; Dongyu Ru; Xiaoyu Li; Xiaoqing Zheng; X...
**Relevance:** 4/5 — Directly evaluates LLM-based agent capabilities in tool use and reasoning, addressing a frontier challenge in agent design with concrete benchmark methodology.
**Depth:** 4/5 — Introduces a well-structured benchmark with clear methodology (DAG-based dependency constraints), 270 instances across difficulty tiers, and detailed trajectory analysis revealing specific failure modes in state tracking and result propagation.

### [TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples](https://arxiv.org/abs/2605.07935)
**Source:** arxiv | **Authors:** Shuren Xia; Qiwei Li; Taqiya Ehsan; Jorge Ortiz
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent coordination, planning, and execution with formal verification methodology to improve reliability and deadlock prevention.
**Depth:** 4/5 — Presents concrete methodology (verification-first pipeline with TLA+ counterexample repair), comprehensive empirical evaluation (48 tasks, 3,456 runs, ablation studies), and quantified improvements in coordination robustness (deadlock/livelock reduction from 31.1% to 14.1%).

### [Abductive Reasoning with Probabilistic Commonsense](https://arxiv.org/abs/2605.08011)
**Source:** arxiv | **Authors:** Joseph Cotnareanu; Chiara Roverato; Han Zhou; Didier Chetelat; Yingxue Zhang; Mark Coates
**Relevance:** 4/5 — Directly addresses neurosymbolic reasoning in LLMs by improving how formal solvers integrate commonsense knowledge, a core capability that enables agent reasoning and planning.
**Depth:** 4/5 — Presents novel methodology (probabilistic framework with PACS algorithm) that combines LLM sampling with formal solvers, includes concrete empirical results across multiple benchmarks, and explicitly motivates limitations of prior neurosymbolic approaches.

### [Learning CLI Agents with Structured Action Credit under Selective Observation](https://arxiv.org/abs/2605.08013)
**Source:** arxiv | **Authors:** Haoyang Su; Ying Wen
**Relevance:** 4/5 — CLI agents are a direct instantiation of LLM-based agents for computer interaction; the paper addresses core agent challenges (credit assignment, selective observation) with novel RL methodology.
**Depth:** 4/5 — The work provides concrete methodological contributions (σ-Reveal for selective observation, A³ for credit assignment with AST-based decomposition) and introduces ShellOps benchmark, grounded in specific problem analysis of long-horizon CLI tasks.

### [Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners](https://arxiv.org/abs/2605.08019)
**Source:** arxiv | **Authors:** Botos Csaba; Sreejan Kumar; Austin Tudor David Andrews; Laurence Hunt; Chris Summerfield; Joshua B. ...
**Relevance:** 4/5 — Directly evaluates frontier LRMs on reasoning, planning, and learning in complex environments, establishing mechanistic insights into how these models represent and manipulate abstract knowledge—core capabilities for autonomous agents.
**Depth:** 4/5 — Provides substantial methodology (multi-modal evaluation framework combining behavioral, neuroimaging, and computational benchmarks) and concrete results (order-of-magnitude brain prediction improvements, targeted mechanistic manipulations revealing in-context state representation).

### [Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning](https://arxiv.org/abs/2605.08061)
**Source:** arxiv | **Authors:** Manish Bhattarai; Ismael Boureima; Nishath Rajiv Ranasinghe; Scott Pakin; Dan O'Malley
**Relevance:** 4/5 — Directly addresses frontier LLM training methodology (GRPO with structured rewards) that enhances reasoning capabilities—a material enabler of agent competence on complex tasks.
**Depth:** 4/5 — Presents formal framework (rubric-grounded RL), clear methodology (GRPO training with multi-criterion LLM judge), concrete benchmark results (71.7% reward, improvements on GSM8K/MATH/GPQA), and evidence of transferable reasoning beyond training corpus.

### [Gradient Extrapolation-Based Policy Optimization](https://arxiv.org/abs/2605.06755)
**Source:** arxiv | **Authors:** Ismam Nur Swapnil; Aranya Saha; Tanvir Ahmed Khan; Mohammad Ariful Haque; Ser-Nam Lim
**Relevance:** 4/5 — Directly addresses training methods for LLM reasoning via RL (GRPO), which is a core frontier capability enabling agent reasoning and planning.
**Depth:** 4/5 — Provides concrete methodology (gradient extrapolation mechanism with three-pass approximation), theoretical surrogate analysis, and extensive empirical results (+1.65 to +5.00 points on math reasoning benchmarks with significant speedup).

### [Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache](https://arxiv.org/abs/2605.06763)
**Source:** arxiv | **Authors:** Mohsen Dehghankar; Abolfazl Asudeh
**Relevance:** 4/5 — Sparse attention and KV cache optimization directly enable more efficient LLM agent deployment and longer-context reasoning tasks critical for agent planning and memory.
**Depth:** 4/5 — Introduces a novel index structure (Louver) with theoretical guarantees (zero false negatives), concrete empirical comparisons against prior methods, and hardware-aware optimizations addressing a specific limitation (missing critical tokens in long reasoning).

### [Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
**Source:** arxiv | **Authors:** Rachel Ma; Dylan Hadfield-Menell; Kristjan Greenewald
**Relevance:** 4/5 — Process Reward Models are a direct frontier capability enabling inference-time scaling and test-time compute allocation for LLM reasoning agents, and calibration is a critical practical limitation.
**Depth:** 4/5 — The paper introduces a novel methodological approach (conditional optimal transport for PRM calibration) with concrete empirical validation on MATH-500 and AIME benchmarks, demonstrating structural improvements over baselines.

### [Conformal Agent Error Attribution](https://arxiv.org/abs/2605.06788)
**Source:** arxiv | **Authors:** Naihe Feng; Yi Sui; Shiyi Hou; Ga Wu; Jesse C. Cresswell
**Relevance:** 4/5 — Directly addresses error attribution and recovery in LLM-based multi-agent systems, which is central to agent reliability and deployment.
**Depth:** 4/5 — Introduces novel conformal prediction algorithms tailored for sequential agent trajectories with theoretical guarantees and demonstrates practical error isolation and rollback mechanisms.

### [SHARP: A Self-Evolving Human-Auditable Rubric Policy for Financial Trading Agents](https://arxiv.org/abs/2605.06822)
**Source:** arxiv | **Authors:** Xiwen Chen; Wenhui Zhu; Songzhu Zheng; Kashif Rasul; Yueyue Deng; Huayu Li
**Relevance:** 4/5 — Directly addresses LLM-based agent self-improvement through structured policy optimization with clear methodology for credit assignment and continuous adaptation in a complex domain.
**Depth:** 4/5 — Presents a concrete neuro-symbolic framework (rubric-based policy + attribution mechanism + walk-forward validation) with empirical results across multiple models and sectors, including specific performance improvements (10-20 percentage points).

### [How to Compress KV Cache in RL Post-Training? Shadow Mask Distillation for Memory-Efficient Alignment](https://arxiv.org/abs/2605.06850)
**Source:** arxiv | **Authors:** Rui Zhu; Weiheng Bai; Qiushi Wu; Yang Ren; Haixu Tang; Yuchu Liu
**Relevance:** 4/5 — Directly addresses a frontier capability bottleneck (KV cache memory) in RL-based LLM training, which is essential infrastructure for enabling advanced reasoning and agent alignment at scale.
**Depth:** 4/5 — Presents concrete methodology (shadow mask distillation) with explicit problem diagnosis (off-policy bias amplification in RL), technical solutions, and empirical validation addressing a real optimization challenge.

### [Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents](https://arxiv.org/abs/2605.06908)
**Source:** arxiv | **Authors:** Ziming Li; Jiatan Huang; Xiaoguang Guo; Guilin Wang; Chuxu Zhang
**Relevance:** 4/5 — Directly addresses test-time compute allocation for LLM agents, a frontier capability that affects reasoning and planning performance.
**Depth:** 4/5 — Presents novel methodology (direction-informed adaptive learning via counterfactual exploration) with concrete empirical validation across multiple environments and backbones, identifying a fundamental instability in existing gating approaches.

### [$f$-Divergence Regularized RLHF: Two Tales of Sampling and Unified Analyses](https://arxiv.org/abs/2605.06977)
**Source:** arxiv | **Authors:** Di Wu; Chengshuai Shi; Jing Yang; Cong Shen
**Relevance:** 4/5 — RLHF is a frontier training method that directly affects LLM capabilities and agent behavior; theoretical understanding of regularization approaches is methodologically relevant to post-training.
**Depth:** 4/5 — Provides unified theoretical framework with rigorous analysis (regret bounds, sub-optimality gaps) and two novel algorithms addressing a gap in prior work on f-divergence regularization.

### [Why Does Agentic Safety Fail to Generalize Across Tasks?](https://arxiv.org/abs/2605.06992)
**Source:** arxiv | **Authors:** Yonatan Slutzky; Yotam Alexander; Tomer Slor; Yoav Nagel; Nadav Cohen
**Relevance:** 4/5 — Directly addresses a frontier challenge in LLM-based agents: why safety fails to generalize across tasks, with explicit experiments on LLM agents in CRM.
**Depth:** 4/5 — Provides both theoretical analysis (Lipschitz bounds for safe vs. unsafe control) and empirical validation across two domains (quadcopter and LLM), identifying an inherent structural limitation rather than just a training problem.

### [PACEvolve++: Improving Test-time Learning for Evolutionary Search Agents](https://arxiv.org/abs/2605.07039)
**Source:** arxiv | **Authors:** Minghao Yan; Bo Peng; Benjamin Coleman; Ziqi Chen; Zhouhang Xie; Shuo Chen; Zhankui He; Noveen Sachd...
**Relevance:** 4/5 — Directly addresses LLM-based agents in evolutionary search with test-time adaptation and policy learning, a frontier capability for agent reasoning and decision-making.
**Depth:** 4/5 — Provides clear methodology (advisor-model RL framework, phase-adaptive training with group-relative and best-of-k feedback) and concrete results across three domains with convergence improvements over state-of-the-art.

### [Theoretical Limits of Language Model Alignment](https://arxiv.org/abs/2605.07105)
**Source:** arxiv | **Authors:** Lucas Monteiro Paes; Natalie Mackraz; Barry-John Theobald; Federico Danieli
**Relevance:** 4/5 — Alignment is foundational to enabling safe and capable LLM-based agents, and understanding the theoretical limits of alignment directly informs what agent capabilities are achievable and reliable.
**Depth:** 4/5 — The work provides rigorous information-theoretic analysis with closed-form expressions, practical estimators, empirical Pareto frontier computations, and identifies algorithmic gaps between theory and practice (PPO/GRPO suboptimality).

### [Where to Spend Rollouts: Hit-Utility Optimal Rollout Allocation for Group-Based RLVR](https://arxiv.org/abs/2605.07114)
**Source:** arxiv | **Authors:** Tao Wang; Shuo Li; Yan Sun; Dongsheng Ding; Edgar Dobriban
**Relevance:** 4/5 — Directly addresses training methods for LLM reasoning and agent capabilities through RLVR, a frontier approach to improving LLM reasoning via reinforcement learning with verifiable rewards.
**Depth:** 4/5 — Provides concrete methodology (hit-utility concept, HORA allocation policy), empirical results across four benchmarks and three scales, and identifies limitations of prior uniform allocation that motivated the contribution.

### [Convergence and Emergence of In-Context Reinforcement Learning with Chain of Thought](https://arxiv.org/abs/2605.07123)
**Source:** arxiv | **Authors:** Zixuan Xie; Xinyu Liu; Rohan Chandra; Shangtong Zhang
**Relevance:** 4/5 — Directly addresses how LLM agents (via Transformers) perform in-context reinforcement learning and reasoning, a frontier capability enabling agent adaptation at inference time.
**Depth:** 4/5 — Provides novel theoretical analysis of CoT-ICRL interaction with convergence proofs, finite-sample bounds, and explanation of parameter emergence through pretraining loss—substantive methodology grounded in formal results.

### [The Position Curse: LLMs Struggle to Locate the Last Few Items in a List](https://arxiv.org/abs/2605.07127)
**Source:** arxiv | **Authors:** Zhanqi Zhang; Hua-Dong Xiong; Robert C. Wilson; Mikio Aoi; Marcelo G. Mattar; Li Ji-An
**Relevance:** 4/5 — Directly addresses a frontier model capability limitation that materially affects LLM agent performance in code understanding and manipulation tasks.
**Depth:** 4/5 — Provides systematic methodology (complementary query evaluation, controlled position specifications), concrete benchmark results across models, and a practical solution approach (PosBench dataset with LoRA fine-tuning and generalization analysis).

### [Adaptive Negative Reinforcement for LLM Reasoning:Dynamically Balancing Correction and Diversity in RLVR](https://arxiv.org/abs/2605.07137)
**Source:** arxiv | **Authors:** Yash Ingle; Jaival Chauhan; Ankit Yadav; Sudhakar Mishra
**Relevance:** 4/5 — Directly addresses training methods for improving LLM reasoning capabilities through reinforcement learning, a frontier capability that materially affects what reasoning agents can accomplish.
**Depth:** 4/5 — Provides concrete methodology (adaptive scheduling and confidence-weighted penalties in NSR framework) with formal analysis of token-level updates and empirical evaluation on hard reasoning benchmarks (MATH, AIME, AMC).

### [HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177)
**Source:** arxiv | **Authors:** Guankai Li; Jiabin Chen; Yi Xu; Xichen Zhang; Yuan Lu
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for multimodal search with concrete methodology on planning, tool use, and efficiency optimization.
**Depth:** 4/5 — Provides substantial methodological contributions (Dual-Grained RL framework with TRACE reward and On-Policy Distillation) and concrete results (9.9% accuracy gain, 5.3x efficiency improvement) with explicit limitations of sequential processing that motivate the work.

### [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/abs/2605.07182)
**Source:** arxiv | **Authors:** Ali Taghibakhshi; Ruisi Cai; Saurav Muralidharan; Sharath Turuvekere Sreenivas; Aditya Vavre; Ameya ...
**Relevance:** 4/5 — Star Elastic directly enables efficient deployment and dynamic resource allocation for reasoning LLMs, a key capability for agent systems that must balance inference cost with reasoning quality.
**Depth:** 4/5 — The paper provides concrete methodology (nested submodel architecture, router-based selection, curriculum distillation) and substantial empirical results (7x compression over SOTA, 16% accuracy gains, 1.9x latency reduction via elastic budget control).

### [Position: Safety and Fairness in Agentic AI Depend on Interaction Topology, Not on Model Scale or Alignment](https://arxiv.org/abs/2605.01147)
**Source:** arxiv | **Authors:** Tanav Singh Bajaj; Nikhil Singh; Karan Anand; Eishkaran Singh
**Relevance:** 4/5 — Directly addresses safety and behavior of LLM-based multi-agent systems, identifying structural failure modes that materially affect how agents interact and make decisions.
**Depth:** 3/5 — Provides clear conceptual framework (interaction topology as primary safety determinant) and identifies three specific failure modes with evidence across model families, though empirical depth and quantitative evaluation of proposed solutions are limited.

### [GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models](https://arxiv.org/abs/2605.01203)
**Source:** arxiv | **Authors:** Zhouhao Sun; Xuan Zhang; Xiao Ding; Bibo Cai; Li Du; Kai Xiong; Xinran Dai; Fei Zhang; weidi tang; Z...
**Relevance:** 4/5 — Process reward models are a core frontier capability for test-time scaling and reasoning verification in LLM-based agents, and this work provides methodology for evaluating their error-detection abilities across diverse domains.
**Depth:** 3/5 — The paper offers concrete evaluation results across 22 models and 11 reasoning domains with specific findings about PRM limitations, though it is primarily a benchmarking contribution rather than a methodological advance in PRM architecture or training.

### [MAP-Law: Coverage-Driven Retrieval Control for Multi-Turn Legal Consultation](https://arxiv.org/abs/2605.01486)
**Source:** arxiv | **Authors:** Qinchuan Cheng; Ruixuan Xie; Jiaqi Liu; Xiaoya Yuan; Yuxin Liu
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and control mechanisms for multi-turn consultation tasks, with explicit methodology for dynamic retrieval decisions.
**Depth:** 3/5 — Provides concrete methodology (coverage-driven state representation and stopping criteria), benchmark results (80% evidence reduction), and ablation studies, though the contribution is specialized to legal domain rather than broadly paradigm-shaping.

### [Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems](https://arxiv.org/abs/2605.01758)
**Source:** arxiv | **Authors:** Yue Ma; Ziyuan Yang; Yi Zhang
**Relevance:** 4/5 — Directly addresses safety and robustness of LLM-based multi-agent systems, a frontier concern for agent deployment and capability trust.
**Depth:** 3/5 — Provides concrete methodology (foresight-guided prediction, multi-persona simulation, recursive binary diagnosis) and experimental results (infection rate reduction from 95% to 5.47%), with clear problem motivation and technical approach.

### [Moira: Language-driven Hierarchical Reinforcement Learning for Pair Trading](https://arxiv.org/abs/2605.01954)
**Source:** arxiv | **Authors:** Polydoros Giannouris; Yuechen Jiang; Lingfei Qian; Yuyan Wang; Xueqing Peng; Jimin Huang; Guojun Xio...
**Relevance:** 4/5 — Directly addresses LLM-based agent design through hierarchical RL with explicit methodology for credit assignment and policy optimization via prompt updates.
**Depth:** 3/5 — Provides clear methodology (hierarchical decomposition, textual feedback mechanisms, prompt-based optimization) and real-world experimental validation, though the contribution is domain-specific rather than broadly advancing agent capability fundamentals.

### [12 Angry AI Agents: Evaluating Multi-Agent LLM Decision-Making Through Cinematic Jury Deliberation](https://arxiv.org/abs/2605.01986)
**Source:** arxiv | **Authors:** Ahmet Bahaddin Ersoz
**Relevance:** 4/5 — Multi-agent LLM deliberation directly addresses agent reasoning, coordination, and evaluation, with findings on how alignment training affects agent behavior in collaborative settings.
**Depth:** 3/5 — Provides concrete methodology (controlled multi-agent setup with persona conditioning, systematic RLHF comparison), specific results (hung jury rates, vote change distributions, model-specific behavioral asymmetries), and identifies a mechanistic failure mode (anchoring bias), though limited scale (18 runs) and exploratory framing somewhat constrain impact.

### [The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence](https://arxiv.org/abs/2605.02106)
**Source:** arxiv | **Authors:** Terry Dorsey; Kevin Huggins
**Relevance:** 4/5 — DGMM directly addresses memory architecture for LLM-based agents, a core frontier capability enabling persistent reasoning, temporal grounding, and context-aware behavior without retraining.
**Depth:** 3/5 — The paper provides formal architectural theory with explicit schema and invariants for memory representation, though it appears to be a theoretical framework without reported empirical evaluation or benchmark results demonstrating concrete improvements.

### [Zero-Shot Confidence Estimation for Small LLMs: When Supervised Baselines Aren't Worth Training](https://arxiv.org/abs/2605.02241)
**Source:** arxiv | **Authors:** Luong N. Nguyen
**Relevance:** 4/5 — Directly addresses a critical agent deployment capability—confidence estimation and routing decisions—which enables cost-effective multi-model agent orchestration strategies.
**Depth:** 3/5 — Provides concrete methodology (token log-probability as zero-shot signal, retrieval-conditional self-assessment) with rigorous empirical evaluation across models and distribution shifts, though the technical novelty is moderate.

### [Measuring AI Reasoning: A Guide for Researchers](https://arxiv.org/abs/2605.02442)
**Source:** arxiv | **Authors:** Munachiso Samuel Nwadike; Zangir Iklassov; Kareem Ali; Rifo Genadi; Kentaro Inui
**Relevance:** 4/5 — Directly addresses evaluation of reasoning in frontier LLMs, a critical capability for assessing agent performance, though focused on measurement methodology rather than agent architecture.
**Depth:** 3/5 — Provides substantial methodological framework (process-based evaluation, formalization of search-like reasoning) with clear motivation from model limitations, but lacks concrete benchmark results or agent-specific case studies.

### [GRAIL: A Deep-Granularity Hybrid Resonance Framework for Real-Time Agent Discovery via SLM-Enhanced Indexing](https://arxiv.org/abs/2605.02489)
**Source:** arxiv | **Authors:** Jinliang Xu
**Relevance:** 4/5 — Directly addresses agent discovery and routing in multi-agent LLM systems, a key infrastructure capability for LLM-based agents at scale.
**Depth:** 3/5 — Presents concrete methodology (SLM-enhanced prediction, pseudo-document expansion, MaxSim matching) with quantified results (79× latency reduction, Recall@10 improvements) on a new 9K-agent dataset, though the contribution is primarily engineering optimization rather than fundamental capability advance.

### [AcademiClaw: When Students Set Challenges for AI Agents](https://arxiv.org/abs/2605.02661)
**Source:** arxiv | **Authors:** Junjie Yu; Pengrui Lu; Weiye Si; Hongliang Lu; Jiabao Wu; Kaiwen Tao; Kun Wang; Lingyu Yang; Qiran Z...
**Relevance:** 4/5 — AcademiClaw directly evaluates LLM-based agents on complex, long-horizon tasks with concrete methodology and results across frontier models, providing diagnostic insights into agent capability boundaries.
**Depth:** 3/5 — The work offers solid empirical contribution through rigorous task curation, multi-dimensional evaluation rubrics, and fine-grained analysis of model performance patterns, though it is primarily a benchmark rather than a methodological advance in agent architecture or training.

### [Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI](https://arxiv.org/abs/2605.02682)
**Source:** arxiv | **Authors:** Majed El Helou; Benjamin Ryder; Chiara Troiani; Jean Diaconu; Herv\'e Muyal; Marcelo Yannuzzi
**Relevance:** 4/5 — Directly addresses security and authorization challenges in LLM-based agents engaging in multi-turn tool use, a frontier capability concern for agent deployment.
**Depth:** 3/5 — Provides clear methodology (hybrid deterministic + semantic controls, two-stage task extraction and matching) and experimental results on multi-turn TBAC, though the primary contribution is in safety/authorization rather than core agent capabilities.

### [ORPilot: A Production-Oriented Agentic LLM-for-OR Tool for Optimization Modeling](https://arxiv.org/abs/2605.02728)
**Source:** arxiv | **Authors:** Guangrui Xie
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture (multi-agent system with specialized conversational, data, and parameter agents) that enables production-grade agentic reasoning for a concrete domain.
**Depth:** 3/5 — Presents novel architectural components (conversational interview agent, data collection agent, parameter computation agent, solver-agnostic IR) and self-correcting mechanisms with evaluation on real-world problems, but focuses on domain-specific application rather than frontier model capabilities or general agent reasoning advances.

### [Mitigating Misalignment Contagion by Steering with Implicit Traits](https://arxiv.org/abs/2605.02751)
**Source:** arxiv | **Authors:** Maria Chang; Ronny Luss; Miao Lui; Keerthiram Murugesan; Karthikeyan Ramamurthy; Djallel Bouneffouf
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent interactions, alignment, and behavioral control—core concerns for deployed agent systems—though focused on social dynamics rather than reasoning/planning capabilities.
**Depth:** 3/5 — Provides clear methodology (implicit trait steering), empirical evidence of misalignment contagion across multiple LMs, and concrete comparison of steering techniques, but the technical contribution is relatively incremental (prompt engineering variation) rather than architectural or capability-frontier work.

### [U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning](https://arxiv.org/abs/2605.02765)
**Source:** arxiv | **Authors:** Christine P Lee; Xinyu Jessica Wang; Aws Albarghouthi; David Porfirio; Bilge Mutlu
**Relevance:** 4/5 — Directly addresses LLM-based agent planning with a focus on constraint specification and verification mechanisms that enable more reliable agent behavior.
**Depth:** 3/5 — Presents concrete methodology (hard vs. soft constraint types with formal and LLM-based verification) and user study results, though primarily a UI/interaction design contribution rather than advancing core agent capabilities or model training.

### [SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering](https://arxiv.org/abs/2605.02819)
**Source:** arxiv | **Authors:** Jiujiu Chen; Yazheng Liu; Sihong Xie; Hui Xiong
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and planning through process reward models and MCTS for knowledge graph question answering, a frontier capability for agentic systems.
**Depth:** 3/5 — Provides clear methodology (schema-aware cumulative rewards, conditioning on prefixes) and concrete results (1.18% Hits@k improvement), but incremental advance on existing process reward model approaches rather than paradigm-shifting.

### [GraphDC: A Divide-and-Conquer Multi-Agent System for Scalable Graph Algorithm Reasoning](https://arxiv.org/abs/2605.06671)
**Source:** arxiv | **Authors:** Wenjin Li; Jiaming Cui
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent reasoning with a concrete hierarchical architecture (Divide-and-Conquer) designed to enhance agent capabilities on complex reasoning tasks.
**Depth:** 3/5 — Presents clear methodology (graph decomposition, specialized agents, master integration) and extensive experiments with quantitative results, though the contribution is task-specific rather than establishing new frontier model capabilities.

### [State Representation and Termination for Recursive Reasoning Systems](https://arxiv.org/abs/2605.06690)
**Source:** arxiv | **Authors:** Debashis Guha; Amritendu Mukherjee; Sanjay Kukreja; Tarun Kumar
**Relevance:** 4/5 — Directly addresses a core agent capability—recursive reasoning and termination—with explicit methodology for state representation and stopping criteria applicable to agent loops and tree-of-thought systems.
**Depth:** 3/5 — Provides formal mathematical framework (order-gap criterion, linearization analysis) with clear methodology, though appears to be local rather than global analysis and lacks empirical validation on concrete agent benchmarks.

### [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)
**Source:** arxiv | **Authors:** Jinghao Luo; Yuchen Tian; Chuxue Cao; Ziyang Luo; Hongzhan Lin; Kaixin Li; Chuyi Kong; Ruichao Yang;...
**Relevance:** 4/5 — Directly addresses LLM-based agent memory mechanisms, a core architectural component enabling agent reasoning and planning capabilities.
**Depth:** 3/5 — Provides a formal evolutionary framework (Storage → Reflection → Experience) with clear design principles and identifies frontier mechanisms (proactive exploration, cross-trajectory abstraction), though the survey synthesizes existing work rather than introducing novel empirical results or methodology.

### [Switchcraft: AI Model Router for Agentic Tool Calling](https://arxiv.org/abs/2605.07112)
**Source:** arxiv | **Authors:** Sharad Agarwal; Pooria Namyar; Alec Wolman; Rahul Ambavat; Ankur Gupta; Qizheng Zhang
**Relevance:** 4/5 — Directly addresses LLM-based agent deployment through model routing for tool calling, a core infrastructure challenge for agentic systems.
**Depth:** 3/5 — Provides concrete methodology (DistilBERT classifier, evaluation framework on five benchmarks) and quantitative results (82.9% accuracy, 84% cost reduction), though the technical novelty is primarily in application rather than fundamental capability innovation.

### [Towards Autonomous Business Intelligence via Data-to-Insight Discovery Agent](https://arxiv.org/abs/2605.07202)
**Source:** arxiv | **Authors:** Dongming Wu; Junwen Li; Ming Lu; Gang Wang; Ting Chen
**Relevance:** 4/5 — Directly addresses LLM-based agent design for complex reasoning and tool use (SQL generation, schema navigation, multi-step analysis), with concrete system architecture and RL-based mechanisms.
**Depth:** 3/5 — Provides methodology including DSL design, RL formulation, and benchmark results on a custom retail environment; however, lacks sufficient detail on core algorithmic innovations and the paper reads more as an applied system than a frontier capability contribution.

### [VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection](https://arxiv.org/abs/2605.08070)
**Source:** arxiv | **Authors:** James Petullo; Sonny George; Dylan Cashman; Nianwen Xue
**Relevance:** 4/5 — Directly addresses inference-time reasoning scaling for LLMs through improved self-consistency methods, a core technique for enhancing agent decision-making and planning.
**Depth:** 3/5 — Presents clear methodology (semantic similarity-based filtering of reasoning traces) with concrete experimental results across five benchmarks showing 47% token reduction, though the contribution is incremental optimization rather than fundamental capability advancement.


## Worth knowing (53 items)

_On-criterion but lower depth, or peripheral relevance._

### [Position: How can Graphs Help Large Language Models?](https://arxiv.org/abs/2605.02452)
**Source:** arxiv | **Authors:** Xiyuan Wang; Yi Hu; Yanbo Wang; Chuan Shi; Muhan Zhang
**Relevance:** 4/5 — Directly addresses how graphs enhance LLM reasoning and planning through prompting techniques (CoT, ToT, GoT) and knowledge integration, which are core capabilities for LLM-based agents.
**Depth:** 2/5 — Position paper that surveys existing techniques and outlines directions rather than presenting novel methodology, concrete benchmarks, or detailed mechanistic insights into graph-LLM integration.

### [Minimizing Collateral Damage in Activation Steering](https://arxiv.org/abs/2605.01167)
**Source:** arxiv | **Authors:** Tam Nguyen; Tu Anh Nguyen; Sina Alemohammad; Richard G. Baraniuk
**Relevance:** 3/5 — Activation steering is a control method for LLMs that touches agent alignment and behavior control, but the work is primarily about steering mechanics rather than agent reasoning, planning, or capability emergence.
**Depth:** 4/5 — The paper provides rigorous mathematical formalization of collateral damage, introduces a principled constrained optimization framework, and demonstrates empirical improvements with clear methodology and quantifiable results.

### [Molecular Representations for Large Language Models](https://arxiv.org/abs/2605.01822)
**Source:** arxiv | **Authors:** Nicholas T. Runcie; Fergus Imrie; Charlotte M. Deane
**Relevance:** 3/5 — The work addresses how LLMs interact with structured knowledge (molecular representations) in service of chemistry reasoning tasks, which is relevant to agent capabilities for tool use and domain reasoning, but the focus is domain-specific optimization rather than core agent mechanisms.
**Depth:** 4/5 — Systematic evaluation across 78,045 questions with multiple models, concrete performance metrics showing substantial differences across representations, and clear error analysis identifying failure modes of existing formats provides substantive methodology and results.

### [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/abs/2605.01910)
**Source:** arxiv | **Authors:** Kyle Lee; Corentin Delacour; Kevin Callahan-Coray; Kyle Jiang; Can Yaras; Samet Oymak; Tathagata Sri...
**Relevance:** 3/5 — Directly addresses inference efficiency for LLM decoding at long contexts, which is a material bottleneck for deploying agents with extended reasoning and memory capabilities.
**Depth:** 4/5 — Presents concrete methodology (stratified sampling, Bernoulli qK^T sparsification), unbiased estimators with variance analysis, GPU kernel implementation, and measured 1.5× speedup with accuracy preservation at 32k tokens.

### [Statistically-Lossless Quantization of Large Language Models](https://arxiv.org/abs/2605.02404)
**Source:** arxiv | **Authors:** Michael Helcig; Eldar Kurtic; Dan Alistarh
**Relevance:** 3/5 — Quantization for efficient LLM deployment affects agent capabilities by enabling model access on constrained hardware, but is a supporting infrastructure concern rather than directly advancing agent reasoning, planning, or tool use.
**Depth:** 4/5 — The paper provides rigorous methodology (three formalized notions of losslessness, gamma-squared variance law, EAR metric) and comprehensive empirical results (task-lossless at 3.3-4 bits, distribution-lossless at 5-6 bits, 1.7-3.6x speedups) with clear technical motivation.

### [Generalized Distributional Alignment Games for Unbiased Answer-Level Fine-Tuning](https://arxiv.org/abs/2605.02435)
**Source:** arxiv | **Authors:** Mehryar Mohri; Jon Schneider; Yutao Zhong
**Relevance:** 3/5 — Answer-level fine-tuning is relevant to LLM agent training, but this work focuses narrowly on statistical estimation bias in reward modeling rather than agent reasoning, planning, or deployment capabilities.
**Depth:** 4/5 — Solid methodological contribution with rigorous theoretical analysis (U-statistics, minimax optimality, convergence proofs) and concrete variance-reduction techniques, though the impact is limited to a specific component of the training pipeline.

### [Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs](https://arxiv.org/abs/2605.02735)
**Source:** arxiv | **Authors:** Xin Zhang; Qiqi Tao; Jiawei Du; Moyun Liu; Joey Tianyi Zhou
**Relevance:** 3/5 — Addresses reasoning mechanisms in multimodal LLMs that could enhance agent capabilities, but is focused on latent reasoning optimization rather than agent architectures, planning, or tool use directly.
**Depth:** 4/5 — Provides clear methodology (two-stage inference-time optimization with contrastive alignment and confidence-progression rewards), identifies a specific optimization pathology, and reports comprehensive empirical validation across eight benchmarks and four model backbones.

### [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/abs/2605.02888)
**Source:** arxiv | **Authors:** Shikhar Shukla
**Relevance:** 3/5 — Directly addresses LLM inference optimization (speculative decoding), a capability enabler for agent systems, but focuses on inference efficiency rather than agent reasoning or capabilities themselves.
**Depth:** 4/5 — Provides solid methodology (adaptive gamma selection via MLP trained on draft confidence/entropy signals), extensive empirical profiling across 5,112 step-level records and 3 compression regimes, and statistically significant improvements (56% over baseline) with released artifacts.

### [H-Probes: Extracting Hierarchical Structures From Latent Representations of Language Models](https://arxiv.org/abs/2605.00847)
**Source:** arxiv | **Authors:** Cutter Dawes; Aryan Sharma; Angelos Ioannis Lagos; Shivam Raval
**Relevance:** 3/5 — The work analyzes how LLMs represent hierarchical reasoning—a capability fundamental to agent planning and reasoning—but focuses on interpretability rather than agent design or deployment.
**Depth:** 4/5 — Provides clear methodology (linear probes for hierarchical structure extraction), rigorous experimental validation (synthetic tasks with ablations showing causality and generalization), and concrete mechanistic insights into LLM representations.

### [Understanding Emergent Misalignment via Feature Superposition Geometry](https://arxiv.org/abs/2605.00842)
**Source:** arxiv | **Authors:** Gouki Minegishi; Hiroki Furuta; Takeshi Kojima; Yusuke Iwasawa; Yutaka Matsuo
**Relevance:** 3/5 — Addresses LLM safety and alignment mechanisms that affect agent deployment, but focuses on fine-tuning phenomena rather than agent capabilities or reasoning directly.
**Depth:** 4/5 — Provides clear geometric mechanistic explanation via feature superposition, empirical validation across multiple models with sparse autoencoders, and a concrete mitigation approach with quantified results (34.5% misalignment reduction).

### [Iterative Finetuning is Mostly Idempotent](https://arxiv.org/abs/2605.01130)
**Source:** arxiv | **Authors:** Zephaniah Roe; Jack Sanderson; Dang Nguyen; Julian Huang; Todd Nief; Aryan Shrivastava; Chenhao Tan;...
**Relevance:** 3/5 — Studies training dynamics and behavioral stability of LLMs across finetuning iterations, which affects agent reliability and alignment—a capability concern for deployed agents, but not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides rigorous experimental methodology across three training paradigms (SFT, SDF, DPO) with systematic measurement of trait amplification and coherence tradeoffs, yielding actionable insights about which training stages pose risks.

### [Arithmetic in the Wild: Llama uses Base-10 Addition to Reason About Cyclic Concepts](https://arxiv.org/abs/2605.01148)
**Source:** arxiv | **Authors:** Sheridan Feucht; Tal Haklay; Usha Bhalla; Daniel Wurgaft; Can Rager; Rapha\"el Sarfati; Jack Merullo...
**Relevance:** 3/5 — Mechanistic understanding of LLM reasoning on concrete tasks is relevant to agent capability research, but this work focuses on a narrow arithmetic behavior rather than agent-enabling capabilities like planning, tool use, or multi-step reasoning.
**Depth:** 4/5 — The paper provides rigorous mechanistic methodology (causal abstraction, Fourier feature analysis, neuron identification) with concrete results identifying specific sparse circuits, offering genuine insight into LLM computation.

### [Latent State Design for World Models under Sufficiency Constraints](https://arxiv.org/abs/2605.01694)
**Source:** arxiv | **Authors:** Keon Woo Kim
**Relevance:** 3/5 — Directly addresses world models and latent state design relevant to agent planning and reasoning, but focuses on representation design rather than LLM-based agents or frontier model capabilities.
**Depth:** 4/5 — Provides a systematic functional taxonomy with explicit methodology for evaluating latent states against sufficiency constraints, supported by a multi-axis evaluation framework and concrete distinctions between architectural approaches.

### [The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition Under Adversarial Pressure](https://arxiv.org/abs/2605.02398)
**Source:** arxiv | **Authors:** Rahul Kumar
**Relevance:** 3/5 — Addresses frontier model evaluation and safety under pressure, relevant to agent deployment reliability, but focuses on metacognitive degradation rather than agent reasoning, planning, or tool-use capabilities.
**Depth:** 4/5 — Strong methodology (factorial design, 67K records, dual-classifier scoring, statistical rigor) and concrete results identifying the compliance trap mechanism, but primarily a safety evaluation rather than capability advancement for agents.

### [Strategy-Aware Optimization Modeling with Reasoning LLMs](https://arxiv.org/abs/2605.02545)
**Source:** arxiv | **Authors:** Ruiqing Zhao; Fengzhi Li; Yuan Zuo; Rui Liu; Yansong Liu; Yunfei Ma; Fanyu Meng; Junlan Feng
**Relevance:** 3/5 — The work addresses LLM capability in structured reasoning (optimization modeling) with explicit methodology, but falls short of frontier agent capabilities—it's specialized tool use without broader planning, memory, or agent autonomy.
**Depth:** 4/5 — Strong methodology (multi-strategy dataset construction, GRPO training with composite rewards) and comprehensive evaluation (8 benchmarks, pass@1/pass@16, constraint efficiency metrics) demonstrate solid technical substance.

### [On the Invariants of Softmax Attention](https://arxiv.org/abs/2605.02907)
**Source:** arxiv | **Authors:** Wonsuk Lee
**Relevance:** 3/5 — Mechanistic analysis of attention provides foundational understanding relevant to how LLMs compute, but does not directly address agent capabilities, reasoning, planning, or tool use.
**Depth:** 4/5 — Rigorous mathematical characterization of attention invariants with concrete empirical verification across models, identifying both mechanism-level and model-level regularities that could inform architectural design.

### [RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.02946)
**Source:** arxiv | **Authors:** Zhiyuan Xu; Joseph Gardiner; Sana Belguith; Lichao Wu
**Relevance:** 3/5 — Addresses safety and robustness of frontier MoE architectures, which affects agent deployment reliability, but focuses on adversarial attacks rather than agent capabilities or reasoning mechanisms.
**Depth:** 4/5 — Provides solid methodology (response-driven expert localization, routing-aware optimization) and comprehensive empirical results (69.3% ASR across 7 MoE models with zero-shot transfer analysis), exposing architectural vulnerabilities.

### [ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving](https://arxiv.org/abs/2605.02960)
**Source:** arxiv | **Authors:** Zhaoyuan Su; Olatunji Ruwase; Karthik Ganesan; Aurick Qiao; Samyam Rajbhandari; Juncheng Yang; Yue C...
**Relevance:** 3/5 — Addresses frontier model serving efficiency for MoE systems that power LLM agents, but focuses on infrastructure optimization rather than agent capabilities, reasoning, or tool use directly.
**Depth:** 4/5 — Provides clear methodology (asynchronous weight gathering vs. activation routing), concrete system design (AsyncEP, prefix-aware routing), and substantial empirical results across multiple hardware configurations with measurable throughput gains.

### [The Right Answer, the Wrong Direction: Why Transformers Fail at Counting and How to Fix It](https://arxiv.org/abs/2605.03258)
**Source:** arxiv | **Authors:** Gabriel Garcia
**Relevance:** 3/5 — This work examines a fundamental capability limitation of LLMs (counting) with mechanistic analysis, which is relevant to understanding model capabilities that affect agent reasoning, but it is narrowly scoped to a single failure mode rather than directly addressing agent architectures or frontier capabilities.
**Depth:** 4/5 — The paper provides rigorous methodology (linear probes, mechanistic localization, intervention studies with clear parameter counts) and concrete quantitative results (R² > 0.99 for internal representation, 50,000x logit rank improvement), identifying a specific geometric bottleneck with cross-task validation.

### [Structured Role-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2605.07274)
**Source:** arxiv | **Authors:** Bingqing Jiang; Difan Zou
**Relevance:** 3/5 — On-topic work on training methods (RLVR/GRPO) that improve LLM/LVLM reasoning capabilities, but focused on vision-language models rather than agent deployment and tool use.
**Depth:** 4/5 — Solid methodological contribution with clear technical innovation (role-aware token-level credit assignment via self-distilled contrasts) and comprehensive experiments across multimodal benchmarks demonstrating concrete improvements.

### [Inference Time Causal Probing in LLMs](https://arxiv.org/abs/2605.07631)
**Source:** arxiv | **Authors:** Sadegh Khorasani; Saber Salehkaleybar; Negar Kiyavash; Matthias Grossglauser
**Relevance:** 3/5 — Causal probing and interpretability methods are relevant to understanding LLM behavior and control, which indirectly supports agent development, but this work is not directly about agent architectures, reasoning, or capabilities.
**Depth:** 4/5 — The paper presents clear methodology (HDMI: probe-free margin-based intervention, LA-HDMI with lookahead), concrete benchmarks (LGD agreement, CausalGym), and explicit improvements over prior probe-classifier approaches with reliability metrics.

### [RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory](https://arxiv.org/abs/2605.06675)
**Source:** arxiv | **Authors:** Fei Zuo; Zikang Zhou; Hao Cong; Xiaoyan Xi; Ho Fai Leung
**Relevance:** 3/5 — KV cache quantization is a frontier optimization for serving LLMs at scale, directly enabling agent deployment and inference efficiency, but is not core to agent reasoning/planning capabilities themselves.
**Depth:** 4/5 — Paper presents novel methodology (distortion model fitting + rate-distortion-based bit allocation) with strong empirical results (70% perplexity reduction) and identifies a concrete failure mode (distortion model mismatch) motivating the contribution.

### [LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction](https://arxiv.org/abs/2605.06676)
**Source:** arxiv | **Authors:** Enshuai Zhou; Yifan Hao; Chao Wang; Rui Zhang; Di Huang; Jiaming Guo; Xing Hu; Zidong Du; Qi Guo; Yu...
**Relevance:** 3/5 — KV cache optimization directly affects LLM inference efficiency and enables longer-context agent reasoning, but is infrastructural rather than core to agent capabilities or frontier model releases.
**Depth:** 4/5 — The paper presents end-to-end differentiable optimization with clear methodology (LKV-H for budgeting, LKV-T for importance scoring), concrete benchmarks (LongBench, RULER), and identifies learned budgeting as the key driver with rigorous evaluation.

### [A Theory of Online Learning with Autoregressive Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.06819)
**Source:** arxiv | **Authors:** Ilan Doron-Arad; Idan Mehalel; Elchanan Mossel
**Relevance:** 3/5 — Addresses theoretical foundations of autoregressive reasoning and chain-of-thought in LLMs, directly relevant to agent reasoning mechanisms but framed as pure learning theory rather than agent systems.
**Depth:** 4/5 — Provides rigorous theoretical analysis with clear methodology (online learning framework, mistake bounds, taxonomy of growth rates) and concrete results (logarithmic ceiling in End-to-End model, elimination of M-dependence in Chain-of-Thought model).

### [Benchmarked Yet Not Measured -- Generative AI Should be Evaluated Against Real-World Utility](https://arxiv.org/abs/2605.06856)
**Source:** arxiv | **Authors:** Ishani Mondal; Shweta Bhardwaj
**Relevance:** 3/5 — Addresses evaluation methodology for generative AI systems in deployment contexts, which is relevant to understanding agent capabilities and limitations, but focuses on utility measurement rather than agent reasoning, planning, or tool use mechanisms.
**Depth:** 4/5 — Proposes a substantive four-stage evaluation framework (SCU-GenEval) with supporting instruments and identifies three recurring evaluation failures (proxy displacement, temporal collapse, distributional concealment) grounded in analysis of 28 deployment cases.

### [LLMs are not (consistently) Bayesian: Quantifying internal (in)consistencies of LLMs' probabilistic beliefs](https://arxiv.org/abs/2605.06915)
**Source:** arxiv | **Authors:** Chacha Chen; Matthew J\"orke; Adam Goli\'nski; Masha Fedzechkina; Guillermo Sapiro; Sinead Williamso...
**Relevance:** 3/5 — Studies an important capability (probabilistic reasoning and belief updating) relevant to agent reliability and decision-making in uncertain domains, but does not directly address agent architectures, tool use, planning, or deployment.
**Depth:** 4/5 — Provides novel methodology for measuring internal consistency of LLM probabilistic beliefs, concrete experimental results comparing Bayesian vs. heuristic updates, and diagnostics for identifying inferential system failures with clear limitations of prior work motivating the approach.

### [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)
**Source:** arxiv | **Authors:** James Fiedler
**Relevance:** 3/5 — LLM-as-a-Judge is a critical evaluation methodology for frontier models and agents, but this work focuses on measurement bias rather than agent capabilities or model releases that enable agents.
**Depth:** 4/5 — Provides analytical results, simulations with diagnostic parameters (J and ΔJ), and concrete case studies demonstrating failure modes in evaluation methodology.

### [Self Driving Datasets: From 20 Million Papers to Nuanced Biomedical Knowledge at Scale](https://arxiv.org/abs/2605.07022)
**Source:** arxiv | **Authors:** Haydn Jones; Yimeng Zeng; Alden Rose; Li S. Yifei; Yining Huang; Kaiwen Wu; Jiaming Liang; Maggie Zi...
**Relevance:** 3/5 — Starling is a multi-agent LLM system with explicit methodology for agent coordination (retrieval design, schema induction, extraction), directly relevant to agent capability, but the work is domain-specific (biomedical knowledge extraction) rather than advancing frontier agent architectures or model capabilities.
**Depth:** 4/5 — The paper provides substantial methodology for agent design (multi-agent orchestration, hybrid retrieval, structured extraction) and concrete large-scale results (6.3M records, error rates on six benchmarks), demonstrating how LLM agents can autonomously execute complex research workflows.

### [Dr. Post-Training: A Data Regularization Perspective on LLM Post-Training](https://arxiv.org/abs/2605.07063)
**Source:** arxiv | **Authors:** Pingbang Hu; Xueshen Liu; Z. Morley Mao; Jiaqi W. Ma
**Relevance:** 3/5 — Post-training methodology (SFT, RLHF, RLVR) is adjacent to agent capabilities but focuses on data regularization rather than agent-specific reasoning, planning, or tool use.
**Depth:** 4/5 — Strong methodological contribution with novel theoretical framing (data as regularizer), concrete experimental validation across multiple post-training objectives, and system-level optimization insights.

### [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)
**Source:** arxiv | **Authors:** Yee Zhing Liew; Andrew Huey Ping Tan; Anwar P. P Abdul Majeed
**Relevance:** 3/5 — Hallucination detection is a known limitation affecting LLM agent reliability and decision-making, but this work focuses on detection methodology rather than agent architecture, planning, or capabilities.
**Depth:** 3/5 — The paper provides a novel geometric mechanism (EPGS via gradient sensitivity and Hessian sharpness) with clear methodology and experimental validation, but is primarily a diagnostic tool rather than advancing agent capabilities or frontier model capabilities.

### [Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy](https://arxiv.org/abs/2605.01642)
**Source:** arxiv | **Authors:** Rachel Freedman
**Relevance:** 3/5 — Addresses frontier model alignment and value adaptation that affects how LLM agents can be steered over time, but is primarily an alignment/governance contribution rather than directly about agent capabilities or reasoning.
**Depth:** 3/5 — Provides concrete methodology (reward basis decomposition, social-choice voting, weight fitting) and proof-of-concept implementation with preliminary analysis, but lacks empirical results on actual agent deployment or performance benchmarks.

### [Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards](https://arxiv.org/abs/2605.01823)
**Source:** arxiv | **Authors:** Rudray Dave; Vedang Dubey; Smit Deoghare; Sudhakar Mishra
**Relevance:** 3/5 — Directly addresses LLM reasoning capability improvement through RL training methods, which is frontier-relevant, but focuses narrowly on math problem selection rather than agent reasoning, planning, or tool use.
**Depth:** 3/5 — Presents solid methodology (multi-dimensional selector model with entropy-based curriculum) and concrete benchmark results (68.0% vs 64.0% baseline), but the contribution is primarily data curation optimization rather than fundamental capability emergence or architectural insight.

### [Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting](https://arxiv.org/abs/2605.02105)
**Source:** arxiv | **Authors:** Ishaan Watts; Catherine Li; Sachin Goyal; Jacob Mitchell Springer; Aditi Raghunathan
**Relevance:** 3/5 — Directly addresses a frontier model capability (post-training robustness and quantization) that affects LLM agent performance, but focuses on optimizer geometry rather than agent reasoning or deployment.
**Depth:** 3/5 — Provides clear methodology (SAM, learning rate schedules) with consistent experimental results across scales (20M–1B parameters), demonstrating 31–40% forgetting reduction, but lacks agent-specific evaluation or architectural insights into how this enables new agent capabilities.

### [A Low-Latency Fraud Detection Layer for Detecting Adversarial Interaction Patterns in LLM-Powered Agents](https://arxiv.org/abs/2605.01143)
**Source:** arxiv | **Authors:** Sheldon Yu; Yingcheng Sun; Hanqing Guo; Julian McAuley; Qianqian Tong
**Relevance:** 3/5 — Directly addresses safety and deployment of LLM-based agents through adversarial robustness, but focuses on a specialized defense layer rather than core agent capabilities or frontier model properties.
**Depth:** 3/5 — Provides concrete methodology (42 structured features, XGBoost classifier, interaction-level detection) and empirical results (9x speedup, synthetic corpus evaluation), but the contribution is primarily an engineering/security layer rather than fundamental insights into agent reasoning or model capabilities.

### [Truth or Tribe: How In-group Favoritism Prioritize Facts in Persona Agents](https://arxiv.org/abs/2605.01329)
**Source:** arxiv | **Authors:** Shijun Lei; Hongyu Wang; Yunji Liang; Haowen Zheng; Bin Guo; Zhiwen Yu
**Relevance:** 3/5 — Directly studies LLM-based persona agents' reasoning and decision-making under social bias, which affects agent reliability and behavior, but focuses on a specific bias phenomenon rather than core agent capability or methodology.
**Depth:** 3/5 — Provides controlled experimental evaluation of in-group favoritism in agents with three proposed mitigation strategies, offering concrete results and intervention mechanisms, but the contribution is narrowly scoped to one bias pattern rather than advancing fundamental agent architectures or capabilities.

### [CP-SynC: Multi-Agent Zero-Shot Constraint Modeling in MiniZinc with Synthesized Checkers](https://arxiv.org/abs/2605.01675)
**Source:** arxiv | **Authors:** Yuliang Song; Eldan Cohen
**Relevance:** 3/5 — Multi-agent LLM workflow with explicit agent coordination (modeling, validation, selection) demonstrates agent reasoning and tool use, but applied to constraint programming rather than frontier model capabilities or general-purpose agent paradigms.
**Depth:** 3/5 — Clear methodology on multi-agent coordination, synthesized checkers for semantic validation, and evidence aggregation with quantitative results on 100 problems; solid contribution but constrained to a specific domain rather than advancing core agent capabilities.

### [Retrieval and Multi-Hop Reasoning in 1M-Token Context Windows: Evaluating LLMs on Classical Chinese Text](https://arxiv.org/abs/2605.02173)
**Source:** arxiv | **Authors:** Eric H. C. Chow
**Relevance:** 3/5 — Evaluates frontier LLM capabilities (long-context retrieval and multi-hop reasoning) that enable agent functionality, but focuses on benchmark performance rather than agent systems or applications.
**Depth:** 3/5 — Provides concrete evaluation methodology (needle-in-haystack variants, three-hop reasoning tasks) and substantive empirical findings about model degradation patterns, though lacks architectural insights into why these limitations exist.

### [An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance](https://arxiv.org/abs/2605.02709)
**Source:** arxiv | **Authors:** Gelei Xu; Ningzhi Tang; Xueyang Li; Toby Jia-Jun Li; Zhi Zheng; Wei Jin; Yiyu Shi
**Relevance:** 3/5 — Directly addresses agent skill architectures and their reusability across domains, a practical layer for LLM-based agent deployment, but focuses narrowly on healthcare application rather than frontier agent capabilities.
**Depth:** 3/5 — Provides empirical analysis of 557 healthcare skills with systematic annotation across ten dimensions and identifies concrete gaps (diagnostic/treatment underrepresentation, lifecycle coverage), but lacks methodological innovation or performance benchmarks that would elevate impact.

### [AutoRAGTuner: A Declarative Framework for Automatic Optimization of RAG Pipelines](https://arxiv.org/abs/2605.02967)
**Source:** arxiv | **Authors:** Xintan Zeng; Yongchao Liu; Yice Luo; Jiajun Zhen
**Relevance:** 3/5 — RAG is a core technique for enhancing LLM agents with retrieval capabilities, but this work focuses on pipeline optimization automation rather than agent reasoning, planning, or capability emergence.
**Depth:** 3/5 — The paper presents solid methodology (modular architecture, Domain-Element Model, Bayesian optimization) and concrete results (performance improvements, code reduction metrics), but the contribution is primarily an engineering framework rather than advancing fundamental agent or model capabilities.

### [Self-Mined Hardness for Safety Fine-Tuning](https://arxiv.org/abs/2605.03226)
**Source:** arxiv | **Authors:** Prakhar Gupta; Garv Shah; Donghua Zhang
**Relevance:** 3/5 — Safety fine-tuning is relevant to agent deployment and reliability, but this work focuses on refusal behavior and jailbreak robustness rather than core agent capabilities like reasoning, planning, or tool use.
**Depth:** 3/5 — The paper presents a clear methodology (self-mined hardness scoring and mixed training) with concrete benchmark results (ASR reduction, refusal rate tradeoffs), but the contribution is primarily a training procedure for safety rather than advancing frontier model capabilities or agent architecture.

### [Uneven Evolution of Cognition Across Generations of Generative AI Models](https://arxiv.org/abs/2605.06815)
**Source:** arxiv | **Authors:** Isaac Galatzer-Levy; Daniel McDuff; Xin Liu; Jed McGiffin
**Relevance:** 3/5 — Evaluates frontier model cognitive capabilities through systematic benchmarking, which informs what agents can do, but focuses on static capability assessment rather than agent-specific reasoning, planning, or tool use.
**Depth:** 3/5 — Introduces a psychometric framework and AIQ benchmark with concrete cross-generation comparisons revealing architectural biases, but lacks mechanistic explanation of why these asymmetries exist or how to address them.

### [How Well Do LLMs Perform on the Simplest Long-Chain Reasoning Tasks: An Empirical Study on the Equivalence Class Problem](https://arxiv.org/abs/2605.06882)
**Source:** arxiv | **Authors:** Chun Zheng; Lianlong Wu; Bingqian Li; Lvting Liu; Yi Zhou
**Relevance:** 3/5 — Evaluates LLM reasoning capabilities on a specific long-chain task, which is relevant to understanding agent capabilities, but focuses narrowly on one synthetic problem rather than agent architecture or deployment.
**Depth:** 3/5 — Provides concrete benchmark results across model types and problem parameters with analysis of failure modes, but lacks methodological innovation or mechanistic insight into how LLMs perform reasoning.

### [GASim: A Graph-Accelerated Hybrid Framework for Social Simulation](https://arxiv.org/abs/2605.07692)
**Source:** arxiv | **Authors:** Xuan Zhou; Yanhui Sun; Hantao Yao; Allen He; Yongdong Zhang; Wu Liu
**Relevance:** 3/5 — Directly addresses LLM-based agent scaling and hybrid frameworks for multi-agent systems, but focuses on optimization/efficiency rather than core agent capabilities or frontier model advances.
**Depth:** 3/5 — Provides concrete methodology (Graph-Optimized Memory, Graph Message Passing, Entropy-Driven Grouping) with quantified results (9.94x speedup, 20% token reduction), but contributions are primarily engineering-focused optimization rather than advancing agent reasoning or capability boundaries.

### [Hierarchical Task Network Planning with LLM-Generated Heuristics](https://arxiv.org/abs/2605.07707)
**Source:** arxiv | **Authors:** Felipe Meneguzzi; Alexandre Buchweitz; Augusto B. Corr\^ea; Victor Scherer Putrich; Andr\'e Grahl Pe...
**Relevance:** 3/5 — Uses LLMs to generate heuristics for hierarchical planning, which is tangentially related to LLM agent reasoning and planning but focuses on classical/hierarchical planning rather than agentic behavior, tool use, or frontier model capabilities.
**Depth:** 3/5 — Provides solid methodology (extending prior work to HTN domain, domain-specific prompting) and concrete empirical results (coverage and search effort across benchmarks), but the contribution is primarily an application of LLMs to planning heuristics rather than novel agent reasoning mechanisms or frontier capability emergence.

### [A Reproducible Optimisation Protocol for Calibrating Prompt-Based Large Language Model Workflows in Evidence Synthesis](https://arxiv.org/abs/2605.06937)
**Source:** arxiv | **Authors:** Teo Susnjak
**Relevance:** 3/5 — Addresses prompt optimization and LLM workflow calibration, which are agent-relevant techniques, but applied narrowly to evidence synthesis rather than core agent capabilities like reasoning, planning, or tool use.
**Depth:** 3/5 — Presents a reproducible calibration protocol with concrete methodology (prompt optimization via metric-guided search, student-reflection LLM separation, DSPy/GEPA instantiation) and evaluation results, but is primarily an engineering contribution rather than advancing frontier agent capabilities.

### [Adaptive Memory Decay for Log-Linear Attention](https://arxiv.org/abs/2605.06946)
**Source:** arxiv | **Authors:** Yaxita Amin; Helen Zichen Li; Mengfan Zhang; Samet Ayhan
**Relevance:** 3/5 — Improves a frontier sequence modeling architecture (log-linear attention) with clear methodology, but is a mechanism optimization rather than directly about agent capabilities or major model releases.
**Depth:** 3/5 — Solid technical contribution with concrete evaluation on recall and language modeling tasks, but incremental in scope—adapting a fixed parameter via learned decay is a focused, well-executed improvement without paradigm-shifting implications.

### [Response Time Enhances Alignment with Heterogeneous Preferences](https://arxiv.org/abs/2605.06987)
**Source:** arxiv | **Authors:** Federico Echenique; Alireza Fallah; Baihe Huang; Michael I. Jordan
**Relevance:** 3/5 — Addresses preference alignment and RLHF methodology for LLMs, which is foundational to agent training, but focuses narrowly on heterogeneous labeler preferences rather than agent capabilities or deployment.
**Depth:** 3/5 — Provides solid theoretical contribution (identifiability proof via DDM) and empirical validation on synthetic and real datasets, but the methodology applies to a specific alignment problem rather than advancing frontier model capabilities or agent reasoning.

### [Agentopic: A Generative AI Agent Workflow for Explainable Topic Modeling](https://arxiv.org/abs/2605.00833)
**Source:** arxiv | **Authors:** Brice Valentin Kok-Shun; Johnny Chan; Gabrielle Peko; David Sundaram
**Relevance:** 3/5 — Agentopic demonstrates LLM-based agent workflow for a specific NLP task with multi-agent collaboration and reasoning, but topic modeling itself is peripheral to core agent capabilities (reasoning, planning, tool use, memory) rather than advancing frontier model capabilities.
**Depth:** 2/5 — While the paper describes a multi-agent workflow and reports F1-scores, it lacks detailed methodology on agent coordination mechanisms, reasoning chains, or failure analysis, presenting primarily an application of existing LLM capabilities rather than advancing agent or model capability understanding.

### [A Language for Describing Agentic LLM Contexts](https://arxiv.org/abs/2605.01920)
**Source:** arxiv | **Authors:** Noga Peleg Pelc; Gal A. Kaminka; Yoav Goldberg
**Relevance:** 3/5 — Directly addresses context engineering and prompt design for LLM agents, which is a foundational component of agent capability, but is primarily a formal language/notation contribution rather than advancing agent reasoning or model capabilities.
**Depth:** 2/5 — Provides a formal specification language with visualization tools and examples, but lacks novel methodology for improving agent performance or deep technical insights into why certain context structures enable better agent behavior.

### [A Compound AI Agent for Conversational Grant Discovery](https://arxiv.org/abs/2605.02366)
**Source:** arxiv | **Authors:** Zhisheng Tang; Mayank Kejriwal
**Relevance:** 3/5 — The work demonstrates a compound AI system using LLM-based agents for a real-world task, but the technical focus is primarily on application architecture and UX rather than frontier agent capabilities or model methods.
**Depth:** 2/5 — The paper describes a deployed system with practical results (3,000+ users, time reduction metrics) but provides limited methodological insight into agent design, reasoning mechanisms, or evaluation of agent decision-making quality beyond task completion.

### [Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges](https://arxiv.org/abs/2605.02592)
**Source:** arxiv | **Authors:** Vincent Henkel; Felix Gehlhoff; David Kube; Asaad Almutareb; Luis Cruz; Bernd Hellingrath; Philip Ko...
**Relevance:** 3/5 — Directly addresses LLM-based agents in industrial contexts with systematic analysis of capabilities and limitations, but focuses on survey methodology rather than advancing frontier agent capabilities or model training.
**Depth:** 2/5 — Provides structured categorization and empirical aggregation of existing work (capability profiles, TRL stages, reported limitations) but lacks novel methodology, architectural insights, or concrete technical results that would drive frontier understanding.

### [Reliable AI Needs to Externalize Implicit Knowledge: A Human-AI Collaboration Perspective](https://arxiv.org/abs/2605.02010)
**Source:** arxiv | **Authors:** Hengyu Liu; Tianyi Li; Zhihong Cui; Yushuai Li; Zhangkai Wu; Torben Bach Pedersen; Kristian Torp; Ch...
**Relevance:** 3/5 — Addresses reliability and verification of LLM reasoning—a real concern for deployed agents—but is a position paper proposing a framework rather than demonstrating empirical methodology or results on agent-specific problems.
**Depth:** 1/5 — Identifies a genuine problem (implicit knowledge verification) and sketches a conceptual solution (Knowledge Objects), but provides no concrete methodology, algorithms, empirical evaluation, or case studies demonstrating how KOs would work in practice.

### [From Pixels to Prompts: Vision-Language Models](https://arxiv.org/abs/2605.07544)
**Source:** arxiv | **Authors:** Khang Hoang Nhat Vo
**Relevance:** 3/5 — Vision-language models are foundational for multimodal agents, but this is a survey/tutorial book focused on conceptual understanding rather than novel agent architectures or frontier capabilities.
**Depth:** 1/5 — The excerpt promises a pedagogical mental map and intuition-building rather than new methodology, concrete results, or limitations analysis that would substantiate a research contribution.

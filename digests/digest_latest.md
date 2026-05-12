# AI digest — 2026-05-12

Rolling 7-day window. Generated automatically.

---

## Read deeply (187 items)

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

### [MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs](https://arxiv.org/abs/2605.08374)
**Source:** arxiv | **Authors:** Junwei Liao; Haoting Shi; Ruiwen Zhou; Jiaqian Wang; Shengtao Zhang; Wei Zhang; Weinan Zhang; Ying W...
**Relevance:** 5/5 — Directly addresses episodic memory mechanisms in LLM agents, a core capability for reasoning and planning over experience.
**Depth:** 4/5 — Provides formal methodology (Exogenous-Context MDP, TD(λ) eligibility traces on provenance DAGs) with concrete empirical results across six diverse benchmarks and principled parameter guidance.

### [CoCoDA: Co-evolving Compositional DAG for Tool-Augmented Agents](https://arxiv.org/abs/2605.08399)
**Source:** arxiv | **Authors:** Ziyang Yu; Qiyue Li; Liang Zhao
**Relevance:** 5/5 — Directly addresses tool use, planning, and library management in LLM-based agents with novel methodology for scaling tool composition.
**Depth:** 4/5 — Provides substantial technical contribution: compositional DAG structure with typed retrieval mechanisms, theoretical analysis of cost reduction, and empirical validation across multiple benchmarks showing concrete improvements.

### [Human-Inspired Memory Architecture for LLM Agents](https://arxiv.org/abs/2605.08538)
**Source:** arxiv | **Authors:** Doga Kerestecioglu; Alexei Robsky; Clemens Vasters; Anshul Sharma; Yitzhak Kesselman
**Relevance:** 5/5 — Directly addresses memory management for LLM agents across long interaction horizons, a core frontier challenge in enabling agent reasoning and planning.
**Depth:** 4/5 — Presents six concrete cognitive mechanisms with explicit methodology (synthetic calibration, deduplication-based consolidation), rigorous evaluation on two benchmarks with quantified results (97.2% retention precision, +13.3 pp improvement), and identifies failure modes motivating each component.

### [SkillMaster: Toward Autonomous Skill Mastery in LLM Agents](https://arxiv.org/abs/2605.08693)
**Source:** arxiv | **Authors:** Min Yang; Jinghua Piao; Xu Xia; Xiaochong Lan; Jiaju Chen; Yongshun Gong; Yong Li
**Relevance:** 5/5 — Directly addresses core LLM-agent capability: autonomous skill creation, refinement, and selection during task solving—a frontier problem in agent self-improvement.
**Depth:** 4/5 — Presents three key methodological innovations (trajectory-informed skill review, counterfactual utility evaluation, DualAdv-GRPO training) with concrete benchmark improvements (8.8–9.3%) and analysis of learned agent behaviors.

### [EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems](https://arxiv.org/abs/2605.08769)
**Source:** arxiv | **Authors:** Chengdong Xu; Kaiqiang Ke; Ziheng Liu; Jiaqi Wei; Zibo Shao; Weile Guo; Chao Yu
**Relevance:** 5/5 — Directly addresses LLM-based multi-agent systems with focus on agent coordination, workflow planning, and execution-time adaptation—core frontier capabilities for agents.
**Depth:** 4/5 — Provides clear methodology (Planner-Evaluator-Updater pipeline, learned Workflow Adapter, policy gradient training), concrete experimental results across three benchmarks, and explicit limitations of static workflows that motivate the contribution.

### [Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://arxiv.org/abs/2605.08978)
**Source:** arxiv | **Authors:** Xingyuan Hua; Sheng Yue; Ju Ren
**Relevance:** 5/5 — Directly addresses LLM-based agent reasoning and planning through test-time scaling and adaptive exploration strategies, which are core frontier capabilities for agents.
**Depth:** 4/5 — Provides clear methodology (variational inference for reward functions, exploration-aware grouping mechanism) and empirical validation across multiple benchmarks with reproducible artifacts.

### [FORTIS: Benchmarking Over-Privilege in Agent Skills](https://arxiv.org/abs/2605.09163)
**Source:** arxiv | **Authors:** Shawn Li; Chenxiao Yu; Han Wang; Wei Yang; Ryan Rossi; Franck Dernoncourt; Xiyang Hu; Philip Yu; Cha...
**Relevance:** 5/5 — Directly addresses a critical safety and capability limitation in LLM-based agents—over-privilege in skill selection and execution—which is fundamental to understanding what enables and constrains agent behavior.
**Depth:** 4/5 — Presents a systematic benchmark (FORTIS) with concrete evaluation methodology across frontier models and domains, identifies specific failure patterns under realistic conditions, and provides actionable insight into privilege escalation as a primary agent vulnerability.

### [Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation](https://arxiv.org/abs/2605.09315)
**Source:** arxiv | **Authors:** Ye Yu; Xiaopeng Yuan; Haibo Jin; Heming Liu; Yaoning Yu; Haohan Wang
**Relevance:** 5/5 — Directly addresses a critical frontier challenge in LLM-based agents—capability degradation during lifelong adaptation—across multiple evolution dimensions (workflow, skill, model, memory).
**Depth:** 4/5 — Proposes a general stabilization principle (CPE) with concrete methodology and quantitative results (e.g., 41.8%→52.8% retained performance improvement) across multiple agent evolution channels.

### [Workspace Optimization: How to Train Your Agent](https://arxiv.org/abs/2605.09650)
**Source:** arxiv | **Authors:** Elad Sarafian; Gal Kaplun; Ron Banner; Daniel Soudry; Boris Ginsburg
**Relevance:** 5/5 — Directly addresses how to train and adapt LLM-based agents when model weights are frozen, proposing workspace optimization as a core mechanism for agent learning in multi-turn reasoning tasks.
**Depth:** 4/5 — Presents a principled methodology that mirrors weight-space training (artifacts→parameters, evidence→data, counterexamples→losses, feedback→gradients) with concrete instantiation in DreamTeam and measured improvements on ARC-AGI-3 benchmark.

### [M2A: Synergizing Mathematical and Agentic Reasoning in Large Language Models](https://arxiv.org/abs/2605.09879)
**Source:** arxiv | **Authors:** Junjian Wang; Xin Zhou; Qiran Xu; Kun Zhan
**Relevance:** 5/5 — Directly addresses LLM-based agent reasoning capabilities through a novel model merging paradigm that synergizes mathematical and agentic reasoning patterns.
**Depth:** 4/5 — Provides explicit methodology (parameter-space merging via null space identification), concrete results (SWE-Bench improvements from 44.0% to 51.2%), and articulates the limitation of prior multi-task learning approaches that motivates the contribution.

### [MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs](https://arxiv.org/abs/2605.10064)
**Source:** arxiv | **Authors:** Ruiyi Yang; Zechen Li; Hao Xue; Imran Razzak; Flora D. Salim
**Relevance:** 5/5 — Directly addresses LLM-based agent self-improvement through structured knowledge externalization, with explicit methodology for cross-iteration learning and frozen-backbone inference.
**Depth:** 4/5 — Provides detailed technical approach (co-evolutionary knowledge graphs, bandit-based routing, append-only memory constraints) with comprehensive evaluation across nine benchmarks and ablations isolating complementary memory contributions.

### [Verifiable Process Rewards for Agentic Reasoning](https://arxiv.org/abs/2605.10325)
**Source:** arxiv | **Authors:** Huining Yuan; Zelai Xu; Huaijie Wang; Xiangmin Yi; Jiaxuan Gao; Xiao-Ping Zhang; Yu Wang; Chao Yu; Y...
**Relevance:** 5/5 — Directly addresses a core challenge in LLM-based agent training: credit assignment in long-horizon reasoning via dense process rewards, with methodology and empirical validation across multiple reasoning domains.
**Depth:** 4/5 — Provides theoretical analysis of credit assignment improvement, concrete methodology (three instantiations of VPR with different verification approaches), and empirical results showing transfer to general reasoning benchmarks.

### [TMAS: Scaling Test-Time Compute via Multi-Agent Synergy](https://arxiv.org/abs/2605.10344)
**Source:** arxiv | **Authors:** George Wu; Nan Jing; Qing Yi; Chuan Hao; Ming Yang; Feng Chang; Yuan Wei; Jian Yang; Ran Tao; Bryan ...
**Relevance:** 5/5 — Directly addresses LLM-based agent coordination and test-time scaling through multi-agent collaboration with structured information flow and memory mechanisms.
**Depth:** 4/5 — Provides clear methodology (hierarchical memories, hybrid reward RL scheme) and empirical results on reasoning benchmarks demonstrating stronger iterative scaling than baselines.

### [How LLMs Are Persuaded: A Few Attention Heads, Rerouted](https://arxiv.org/abs/2605.09314)
**Source:** arxiv | **Authors:** Xiangkun Sun; Lingkai Kong; Aoqi Zhang; Liang Zeng; Tonghan Wang
**Relevance:** 4/5 — This work directly addresses frontier model capabilities and safety—specifically how LLMs can be manipulated via attention mechanisms—which materially affects what agents can reliably do and how to build trustworthy ones.
**Depth:** 5/5 — The paper provides rigorous causal mechanistic analysis (via intervention and circuit isolation), concrete methodology for tracing persuasion pathways, and validates findings across multiple models and realistic scenarios.

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

### [On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective](https://arxiv.org/abs/2605.08368)
**Source:** arxiv | **Authors:** Yuhao Li; Shengchao Liu
**Relevance:** 4/5 — Directly addresses frontier model capabilities and post-training methods (SFT vs RL) that materially affect what LLM agents can do, particularly their ability to reach new behavioral capabilities through interaction and tool use.
**Depth:** 4/5 — Provides a rigorous free-energy framework with operational definitions (accessible support) that distinguish capability elicitation from creation, offering methodological clarity on how post-training actually changes model capabilities rather than just reweighting existing ones.

### [SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost-Efficient LLM Agents](https://arxiv.org/abs/2605.08386)
**Source:** arxiv | **Authors:** Yongliang Miao; Ziyang Yu; Liang Zhao; Bowen Zhu; Hasibul Haque
**Relevance:** 4/5 — Directly addresses LLM agent capability through skill reuse and retrieval mechanisms, a core methodology for enabling agent reasoning and planning across tasks.
**Depth:** 4/5 — Presents concrete hierarchical architecture (four-layer skill graph), theoretical analysis of cost complexity under sparse mismatch, verifier-based routing mechanism, and quantified results (up to 6.31pp improvement) across two benchmarks.

### [Belief or Circuitry? Causal Evidence for In-Context Graph Learning](https://arxiv.org/abs/2605.08405)
**Source:** arxiv | **Authors:** Katharine Kowalyshyn; Timothy Duggan; Daniel Little; Michael C Hughes
**Relevance:** 4/5 — Mechanistic understanding of in-context learning directly illuminates a core capability that enables LLM agents to adapt and reason over new information without retraining.
**Depth:** 4/5 — The paper combines multiple rigorous methodologies (PCA reconstruction, activation patching, causal steering with controls) to establish a dual-mechanism account of how models learn graph structure in-context, moving beyond surface-level capability observation.

### [Mid-Training with Self-Generated Data Improves Reinforcement Learning in Language Models](https://arxiv.org/abs/2605.08472)
**Source:** arxiv | **Authors:** Aswin RRV; Jacob Dineen; Divij Handa; Mihir Parmar; Ben Zhou; Swaroop Mishra; Chitta Baral
**Relevance:** 4/5 — Directly addresses RL training methods for LLMs to improve reasoning and problem-solving capabilities, which is core to enabling agent behavior like planning and multi-step reasoning.
**Depth:** 4/5 — Provides theoretical perspective on policy-gradient incentives, a specific bootstrapped data-generation framework grounded in problem-solving heuristics, and empirical validation across multiple reasoning benchmarks.

### [Log analysis is necessary for credible evaluation of AI agents](https://arxiv.org/abs/2605.08545)
**Source:** arxiv | **Authors:** Peter Kirgis; Sayash Kapoor; Stephan Rabanser; Nitya Nadgir; Cozmin Ududec; Magda Dubois; JJ Allaire...
**Relevance:** 4/5 — Directly addresses evaluation methodology for LLM-based agents, a critical frontier concern for understanding what agents can actually do and their real-world limitations.
**Depth:** 4/5 — Provides a systematic taxonomy of evaluation threats, principled framework for log analysis, and concrete empirical evidence (50% performance re-elicitation on tau-Bench) demonstrating methodology and results.

### [Why Retrying Fails: Context Contamination in LLM Agent Pipelines](https://arxiv.org/abs/2605.08563)
**Source:** arxiv | **Authors:** Zhanfu Yang
**Relevance:** 4/5 — Directly addresses a failure mode in LLM agent tool-use pipelines (multi-step reasoning with retries), providing formal methodology for understanding and optimizing agent performance.
**Depth:** 4/5 — Rigorous theoretical framework with five closed-form results, information-theoretic bounds, and validation on real SWE-bench data demonstrating concrete modeling of agent behavior degradation.

### [The Echo Amplifies the Knowledge: Somatic Marker Analogues in Language Models via Emotion Vector Re-Injection](https://arxiv.org/abs/2605.08611)
**Source:** arxiv | **Authors:** Jared Glover
**Relevance:** 4/5 — Directly addresses LLM agent capability through memory and emotional decision-making systems, which are foundational to agent reasoning and planning.
**Depth:** 4/5 — Provides concrete methodology (sparse autoencoder feature identification, emotion vector re-injection at specific layers), rigorous empirical results (statistical tests, four-condition design replicating neuroscience framework), and mechanistic insights into how emotional markers affect model decision-making.

### [MIND-Skill: Quality-Guaranteed Skill Generation via Multi-Agent Induction and Deduction](https://arxiv.org/abs/2605.08670)
**Source:** arxiv | **Authors:** Yixuan Li; Mingshu Cai; Ziyang Xiao; Wanyuan Wang; Yanchen Deng; Bo An
**Relevance:** 4/5 — Directly addresses skill generation and reuse for LLM-based agents, a core capability that enables agents to perform complex multi-step tasks more effectively.
**Depth:** 4/5 — Presents clear methodology (induction-deduction framework with three complementary losses optimized via TextGrad) and empirical validation on two benchmarks (AppWorld, BFCL-v3) with comparison to concurrent methods.

### [Iterative Critique-and-Routing Controller for Multi-Agent Systems with Heterogeneous LLMs](https://arxiv.org/abs/2605.08686)
**Source:** arxiv | **Authors:** Wenzhi Fang; Liangqi Yuan; Guangchen Lan; Dong-Jun Han; Christopher G. Brinton
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent coordination and control, a core agent capability with methodology for iterative refinement and routing decisions.
**Depth:** 4/5 — Provides explicit methodology (MDP formulation, policy gradient optimization, composite reward design) and comprehensive experimental results across seven benchmarks showing substantial efficiency gains.

### [AgentPSO: Evolving Agent Reasoning Skill via Multi-agent Particle Swarm Optimization](https://arxiv.org/abs/2605.08704)
**Source:** arxiv | **Authors:** Hyunmin Hwang; Jaemin Kim; Choonghan Kim; Hangeol Chang; Jong Chul Ye
**Relevance:** 4/5 — Directly addresses multi-agent LLM reasoning and evolves agent skills without parameter updates, core to frontier agent capabilities.
**Depth:** 4/5 — Presents novel methodology (PSO-inspired skill evolution with semantic updates and self-reflection) with experimental validation across benchmarks and transfer learning results.

### [AHD Agent: Agentic Reinforcement Learning for Automatic Heuristic Design](https://arxiv.org/abs/2605.08756)
**Source:** arxiv | **Authors:** Haoze Lv; Ning Lu; Ziang Zhou; Shengcai Liu
**Relevance:** 4/5 — Directly addresses LLM-based agents with tool use, dynamic decision-making, and agentic RL training—core to agent capability frontier.
**Depth:** 4/5 — Provides substantial methodology (tool-integrated multi-turn framework, environment synthesis pipeline, agentic RL system) and concrete results (8 domains, 4B model matching larger baselines).

### [Reasoning Compression with Mixed-Policy Distillation](https://arxiv.org/abs/2605.08776)
**Source:** arxiv | **Authors:** Han Yang; Mingyan Wu; Bailan He; Zeyu Cao; Sikuan Yan; Kevin Qinghong Lin; Zifeng Ding
**Relevance:** 4/5 — Directly addresses efficiency and deployment of reasoning-based LLMs through a novel distillation method that improves agent capability in resource-constrained settings.
**Depth:** 4/5 — Provides clear methodology (Mixed-Policy Distillation combining on-policy and off-policy approaches), concrete quantitative results (27.1% token reduction with performance gains), and explicit motivation addressing prior distillation limitations.

### [How You Begin is How You Reason: Driving Exploration in RLVR via Prefix-Tuned Priors](https://arxiv.org/abs/2605.08817)
**Source:** arxiv | **Authors:** Yifan Xu; Junren Chen; Yifan Chen
**Relevance:** 4/5 — Directly addresses LLM agent reasoning through reinforcement learning with verifiable rewards, a frontier approach to improving planning and exploration in language model-based agents.
**Depth:** 4/5 — Provides clear methodology (prefix-tuning with information maximization reward), concrete results (11.60% improvement in Pass@4), and identifies a specific failure mode (entropy collapse) in prior RLVR approaches.

### [When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents](https://arxiv.org/abs/2605.08828)
**Source:** arxiv | **Authors:** Strick Sheng; Ziyue Wang; Liyi Zhou
**Relevance:** 4/5 — Directly addresses a core LLM agent failure mode—evidence grounding and reliability in agent-environment interaction—with systematic methodology for evaluating and benchmarking this defect across multiple architectures.
**Depth:** 4/5 — Provides concrete methodology (EnvTrustBench framework with workspace generation, oracle validation, and feedback-guided case expansion) and empirical results across 55 cases, 6 LLM backbones, and 5 scaffolds, identifying a systematic failure pattern with security implications.

### [Ace-Skill: Bootstrapping Multimodal Agents with Prioritized and Clustered Evolution](https://arxiv.org/abs/2605.08887)
**Source:** arxiv | **Authors:** Feng Xiong; Zengbin Wang; Yong Wang; Xuecai Hu; Jinghan He; Liang Lin; Yuan Liu; Xiangxiang Chu
**Relevance:** 4/5 — Directly addresses self-evolving multimodal LLM-based agents with concrete methodology for improving rollout efficiency and knowledge organization in tool-use scenarios.
**Depth:** 4/5 — Provides explicit mechanisms (prioritized sampling with proficiency tracking, semantic knowledge clustering) with substantial empirical results (+35.46% improvement) and knowledge transfer analysis across model scales.

### [OPT-BENCH: Evaluating the Iterative Self-Optimization of LLM Agents in Large-Scale Search Spaces](https://arxiv.org/abs/2605.08904)
**Source:** arxiv | **Authors:** Xiaozhe Li; Jixuan Chen; Xinyu Fang; Shengyuan Ding; Haodong Duan; Qingwen Liu; Kai Chen
**Relevance:** 4/5 — Directly addresses LLM-based agent self-improvement through iterative feedback, combining benchmark design with agent framework for evaluating core reasoning and adaptation capabilities.
**Depth:** 4/5 — Proposes OPT-Agent framework with explicit perception-memory-reasoning loop, conducts systematic evaluation across 19 LLMs with concrete results on performance gaps versus human experts, and identifies capacity constraints as fundamental limitations.

### [Forge: Quality-Aware Reinforcement Learning for NP-Hard Optimization in LLMs](https://arxiv.org/abs/2605.08905)
**Source:** arxiv | **Authors:** Xiaozhe Li; Xinyu Fang; Shengyuan Ding; Yang Li; Linyang Li; Haodong Duan; Qingwen Liu; Kai Chen
**Relevance:** 4/5 — Directly addresses frontier LLM capabilities for reasoning and optimization through reinforcement learning with verifiable rewards, a key training method that enables agent performance on complex tasks.
**Depth:** 4/5 — Provides substantial methodology (quality-aware RLVR framework, reward design, training infrastructure), concrete benchmarks (10 NP-hard tasks, 1,000 instances), and rigorous results (93.1% SR vs GPT-4o's 29.6%, transfer learning gains) with analysis of scaling factors.

### [Self-ReSET: Learning to Self-Recover from Unsafe Reasoning Trajectories](https://arxiv.org/abs/2605.08936)
**Source:** arxiv | **Authors:** Dongcheng Zhang; Yi Zhang; Yuxin Chen; An Zhang; Xiang Wang; Chaochao Lu
**Relevance:** 4/5 — Directly addresses safety and robustness of Large Reasoning Models (LRMs) through a reinforcement learning approach to improve self-correction capabilities, which is central to agent reliability.
**Depth:** 4/5 — Presents a novel RL framework (Self-ReSET) with clear methodology for on-policy recovery from unsafe trajectories, empirical validation across multiple benchmarks, and analysis of learned self-recovery patterns.

### [MDGYM: Benchmarking AI Agents on Molecular Simulations](https://arxiv.org/abs/2605.08941)
**Source:** arxiv | **Authors:** Vinay Kumar; Satyendra Rajput; Mausam; N. M. Anoop Krishnan
**Relevance:** 4/5 — Directly evaluates LLM-based agent capabilities on a grounded reasoning task, revealing failure modes and limitations that constrain what agents can accomplish beyond pure code generation.
**Depth:** 4/5 — Provides concrete benchmark results (21% on easy tasks, <10% on hard), systematic failure analysis (trajectory instability, fabricated outputs, premature abandonment), and identifies a qualitative gap between code fluency and physical reasoning that motivates future agent research.

### [Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery](https://arxiv.org/abs/2605.08956)
**Source:** arxiv | **Authors:** Harshit Bisht; Vinay Kumar; Kevin Maik Jablonka; Mausam; N. M. Anoop Krishnan
**Relevance:** 4/5 — Directly addresses LLM-based agent design and deployment for scientific discovery, identifying fundamental architectural and training limitations that constrain agent capabilities.
**Depth:** 4/5 — Provides substantive methodological critique of agent construction (LLM training gaps, preference optimization effects, benchmark design) and proposes concrete design recommendations (scientific simulations as verifiers, persistent world models, preregistration systems).

### [SearchSkill: Teaching LLMs to Use Search Tools with Evolving Skill Banks](https://arxiv.org/abs/2605.09038)
**Source:** arxiv | **Authors:** Jinchao Hu; Meizhi Zhong; Kehai Chen; Min Zhang
**Relevance:** 4/5 — Directly addresses LLM agent tool use (search) through explicit skill-based query planning, a core capability for reasoning and planning in agents.
**Depth:** 4/5 — Provides clear methodology (skill selection + skill-grounded execution, evolving SkillBank with failure-pattern reconstruction) and concrete benchmark results showing improved exact match and retrieval efficiency.

### [Containment Verification: AI Safety Guarantees Independent of Alignment](https://arxiv.org/abs/2605.09045)
**Source:** arxiv | **Authors:** Royce Moon; Lav R. Varshney
**Relevance:** 4/5 — Directly addresses agentic framework safety and containment verification for LLM-based agents, a frontier concern for deployed agent systems.
**Depth:** 4/5 — Presents novel methodology (havoc oracle semantics, formal verification via refinement in Dafny) with concrete instantiation (PocketFlow) and mechanized proofs, demonstrating substantial technical contribution to agent safety guarantees.

### [Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas](https://arxiv.org/abs/2605.09159)
**Source:** arxiv | **Authors:** Nils A. Herrmann; Leander Girrbach; Kirill Bykov; Zeynep Akata
**Relevance:** 4/5 — Directly addresses LLM reasoning mechanisms and introduces a novel methodology (polylogue monitoring) for reasoning-time control and steering, which are core capabilities for agent planning and decision-making.
**Depth:** 4/5 — Presents concrete methodology (persona vectors as dynamic signals), systematic experiments across four models with interpretability analysis, and demonstrates practical steering improvements with mechanistic insight into reasoning stages.

### [CIVeX: Causal Intervention Verification for Language Agents](https://arxiv.org/abs/2605.09168)
**Source:** arxiv | **Authors:** Fabio Rovai
**Relevance:** 4/5 — Directly addresses a critical safety and reliability problem in tool-using LLM agents—verifying that actions have causal effects, not just valid schemas.
**Depth:** 4/5 — Introduces a principled causal intervention verification framework with identifiability checking, structured verdicts, and extensive empirical validation on both synthetic benchmarks and production logs.

### [Agentic MIP Research: Accelerated Constraint Handler Generation](https://arxiv.org/abs/2605.09186)
**Source:** arxiv | **Authors:** Liding Xu; Yugeng Zhou; Sebastian Pokutta
**Relevance:** 4/5 — Directly demonstrates LLM agents autonomously performing complex reasoning, planning, and code generation within a solver harness—a concrete frontier application of agent capabilities to algorithmic research.
**Depth:** 4/5 — Provides clear methodology (solver-aware harness, in-context learning, sandboxed debugging loop), concrete results (5 novel instances solved, executable constraint handlers generated), and explicit limitations of prior work (manual feedback loop overhead) that motivate the agentic approach.

### [The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations](https://arxiv.org/abs/2605.09195)
**Source:** arxiv | **Authors:** Rania Elbadry; Ahmed Heakl; Fan Zhang; Dani Bouch; Yuxia Wang; Preslav Nakov; Zhuohan Xie
**Relevance:** 4/5 — Directly addresses a critical frontier capability limitation—temporal knowledge drift detection in LLMs—that materially affects what agents can reliably do and how they can be deployed safely.
**Depth:** 4/5 — Provides rigorous mechanistic methodology (geometric analysis, linear probes, null-space projections, MLP circuit tracing) with concrete quantitative results (AUROC 0.83–0.95, orthogonality metrics, cross-cutoff validation) that reveal why existing uncertainty methods fail by construction.

### [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](https://arxiv.org/abs/2605.09278)
**Source:** arxiv | **Authors:** Yuqiao Meng; Sakshi Sunil Narvekar; Luoxi Tang; Rupali Rajendra Vaje; Yingxue Zhang; Muchao Ye; Zhao...
**Relevance:** 4/5 — Directly addresses a critical problem in multi-agent LLM systems (memory corruption in debate-based reasoning), proposing a game-theoretic calibration mechanism to improve agent reliability.
**Depth:** 4/5 — Presents novel methodology (zero-trust memory game formulation, equilibrium-guided calibration) with concrete algorithmic instantiation for both embedding and graph-based memory, plus empirical validation across benchmarks and architectures.

### [PiCA: Pivot-Based Credit Assignment for Search Agentic Reinforcement Learning](https://arxiv.org/abs/2605.09287)
**Source:** arxiv | **Authors:** Dongyi Liu; Yifan Niu; Qinwen Wang; Han Xiao; Jia Li
**Relevance:** 4/5 — Directly addresses RL training of LLM-based search agents with novel credit assignment methodology that materially affects agent reasoning and long-horizon planning capabilities.
**Depth:** 4/5 — Provides clear methodology (PBRS-based pivot identification), identifies concrete limitations of prior work (reward sparsity, isolated credit, distributional shift), and demonstrates substantial empirical gains (15.2% improvement for 3B models across seven QA benchmarks).

### [Towards a Virtual Neuroscientist: Autonomous Neuroimaging Analysis via Multi-Agent Collaboration](https://arxiv.org/abs/2605.09366)
**Source:** arxiv | **Authors:** Keqi Han; Songlin Zhao; Yao Su; Lifang He; Carl Yang
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent systems with reasoning, planning, and adaptive tool use for complex workflow construction, core agent capabilities.
**Depth:** 4/5 — Presents concrete methodology (code-centric execution, hierarchical verification framework, specialist agent collaboration) and empirical validation on real datasets (ADHD-200, ADNI) with measured improvements over baselines.

### [NEXUS: Continual Learning of Symbolic Constraints for Safe and Robust Embodied Planning](https://arxiv.org/abs/2605.09387)
**Source:** arxiv | **Authors:** Tiehan Cui; Peipei Liu; Yanxu Mao; Congying Liu; Mingzhe Xing; Datao You
**Relevance:** 4/5 — Directly addresses LLM-based embodied agents with explicit focus on safety constraints, planning, and continual learning—core agent capabilities.
**Depth:** 4/5 — Presents methodology for decoupling feasibility from safety, symbolic grounding mechanisms, and concrete experimental evaluation on SafeAgentBench with multiple success metrics.

### [SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning](https://arxiv.org/abs/2605.09423)
**Source:** arxiv | **Authors:** Haoqiang Kang; Xiaokang Ye; Yuhan Liu; Siddhant Hitesh Mantri; Lingjun Mao; James Fleming; Drishti R...
**Relevance:** 4/5 — SimCoder is an LLM-based coding agent with tool use, self-evolution via feedback, and verifier mechanisms—core agent capabilities—applied to environment generation for embodied learning.
**Depth:** 4/5 — The paper provides clear methodology (tool-augmented coding agent with verifier feedback loops, self-evolution mechanism, co-evolution curriculum), concrete results (18-point and 40-point performance gains, generalization to unseen benchmarks), and explicit limitations of prior work (static scene generation, lack of diverse training grounds).

### [Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/abs/2605.09497)
**Source:** arxiv | **Authors:** Yilin Zhang; Yingkai Hua; Chunyu Wei; Xin Wang; Yueguo Chen
**Relevance:** 4/5 — Directly addresses a frontier capability problem for LLM/VLM-based web agents—robustness to adversarial interfaces—with methodology and evaluation.
**Depth:** 4/5 — Proposes a concrete two-stage defense framework (hybrid-reward learning + experience summarization), introduces a new benchmark (RUC with 1,407 scenarios), and reports quantified improvements (53.8% reduction in susceptibility).

### [LLM-Guided Monte Carlo Tree Search over Knowledge Graphs: Composing Mechanistic Explanations for Drug-Disease Pairs](https://arxiv.org/abs/2605.09542)
**Source:** arxiv | **Authors:** Rishabh Jakhar; Michel Dumontier; Remzi Celebi
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and planning through a neuro-symbolic framework combining LLMs with structured search (MCTS) for multi-step decision-making over knowledge graphs.
**Depth:** 4/5 — Provides clear methodology (TESSERA framework with dual LLM roles as policy prior and state evaluator, MCTS for credit assignment) and concrete evaluation with ablations demonstrating component contributions on drug-disease mechanism tasks.

### [TIDE-Bench: Task-Aware and Diagnostic Evaluation of Tool-Integrated Reasoning](https://arxiv.org/abs/2605.09544)
**Source:** arxiv | **Authors:** Yize Li; Junzhi Li; Jason Song; Chuxiong Sun; Rui Wang; Changwen Zheng
**Relevance:** 4/5 — Directly addresses evaluation of tool-integrated reasoning in LLMs, a core capability enabling agent behavior, with concrete benchmark design and multi-task methodology.
**Depth:** 4/5 — Provides substantial methodological contribution through task-aware evaluation protocol, four task categories (including novel tool-grounding and interactive tasks), and diagnostic evaluation metrics across process reliability, tool efficiency, and inference cost.

### [CodeClinic: Evaluating Automation of Coding Skills for Clinical Reasoning Agents](https://arxiv.org/abs/2605.09675)
**Source:** arxiv | **Authors:** Timothy Ossowski; Xinchi Liu; Danyal Maqbool; Vaibhav Dhanuka; Sheng Zhang; Hoifung Poon; Majid Afsh...
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities for clinical reasoning, tool synthesis, and compositional skill composition—core to agent methodology and deployment.
**Depth:** 4/5 — Contributes concrete methodology (autoformalization pipeline with iterative refinement), substantial benchmark design (two complementary tasks, stratified complexity), and measured results (40% token reduction, consistency gains).

### [Unpredictability dissociates from structured control in language agents](https://arxiv.org/abs/2605.09692)
**Source:** arxiv | **Authors:** Jia Xiao
**Relevance:** 4/5 — Directly investigates control mechanisms in language agents—specifically how structured reasoning, memory, and inhibition couple to action selection—which is core to understanding what makes agents effective.
**Depth:** 4/5 — Substantial empirical methodology with 74K+ API calls across 7 datasets, systematic lesion ablations, matched controls, multi-model validation, and blinded annotation, establishing that stochasticity alone cannot reproduce structured agent control.

### [Ambig-DS: A Benchmark for Task-Framing Ambiguity in Data-Science Agents](https://arxiv.org/abs/2605.09698)
**Source:** arxiv | **Authors:** Josefa Lia Stoisser; Marc Boubnovski Martell; Sidsel Boldsen; Kaspar M\"artens; Robert Kitchen
**Relevance:** 4/5 — Directly addresses evaluation and failure modes of LLM-based data-science agents, a key frontier in agent capabilities and deployment.
**Depth:** 4/5 — Provides systematic benchmark methodology with controlled task variants, human-LLM verification pipeline, and empirical analysis across five frontier models revealing specific failure modes and recovery mechanisms.

### [EnactToM: An Evolving Benchmark for Functional Theory of Mind in Embodied Agents](https://arxiv.org/abs/2605.09826)
**Source:** arxiv | **Authors:** Gurusha Juneja; Dylan Lu; Saaket Agashe; Parth Diwane; Edward Gunn; Jayanth Srinivasa; Gaowen Liu; W...
**Relevance:** 4/5 — Directly addresses a critical frontier capability for LLM-based agents—theory of mind and multi-agent coordination—with a rigorous benchmark that exposes failure modes in state-of-the-art models.
**Depth:** 4/5 — Provides substantial methodology (formal verification of task solvability, epistemic depth control, evolving difficulty), concrete results (0% Pass@3 on hard split across frontier models), and systematic analysis of failure modes (93% traced to epistemic coordination breakdowns).

### [When to Re-Commit: Temporal Abstraction Discovery for Long-Horizon Vision-Language Reasoning](https://arxiv.org/abs/2605.09860)
**Source:** arxiv | **Authors:** Chen Li; Zhantao Yang; Fangyi Chen; Han Zhang; Anudeepsekhar Bolimera; Marios Savvides
**Relevance:** 4/5 — Directly addresses long-horizon reasoning and planning in vision-language agents, with methodology for adaptive commitment depth that improves agent decision-making under uncertainty.
**Depth:** 4/5 — Provides clear methodology (learnable state-conditioned commitment depth), theoretical analysis of why it works, and concrete benchmark results showing Pareto improvements and outperformance of GPT-5.5/Claude.

### [Cross-Family Universality of Behavioral Axes via Anchor-Projected Representations](https://arxiv.org/abs/2605.09875)
**Source:** arxiv | **Authors:** Su-Hyeon Kim; Yo-Sub Han
**Relevance:** 4/5 — Cross-model behavioral steering and representation transfer directly enable agent control and interpretability across model families, a frontier capability for deploying aligned agents.
**Depth:** 4/5 — Introduces a novel anchor-projection framework with concrete methodology, evaluates five model families across ten behavioral axes with quantified transfer accuracy (0.83 ten-way detection, 0.95 AUROC), and provides sensitivity analysis on anchor pool requirements.

### [expo: Exploration-prioritized policy optimization via adaptive kl regulation and gaussian curriculum sampling](https://arxiv.org/abs/2605.09923)
**Source:** arxiv | **Authors:** Mingxiong Lin; Zhangquan Gong; Maowen Tang; Qian Li; Chuangchuang Wang; Jian Ma; Sutian Huang; Kai T...
**Relevance:** 4/5 — Directly addresses training methods for LLM-based reasoning agents through policy optimization improvements, which materially affects agent capabilities on mathematical reasoning tasks.
**Depth:** 4/5 — Provides clear methodology (adaptive KL regulation and curriculum sampling mechanisms) with concrete benchmark results showing substantial improvements (13.34 absolute gain on AIME 2025).

### [HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution](https://arxiv.org/abs/2605.09942)
**Source:** arxiv | **Authors:** Dongming Jiang; Yi Li; Guanpeng Li; Qiannan Li; Bingzhe Li
**Relevance:** 4/5 — Directly addresses memory architectures for LLM-based agents through a novel retrieval mechanism with concrete methodology and RL-based optimization.
**Depth:** 4/5 — Provides substantial technical methodology (weighted graph evolution, query-conditioned traversal, RL training framework) and empirical results on long-horizon reasoning tasks.

### [TimeClaw: A Time-Series AI Agent with Exploratory Execution Learning](https://arxiv.org/abs/2605.10038)
**Source:** arxiv | **Authors:** Hangchen Liu; Dongyuan Li; Renhe Jiang; Jiewen Deng; Weiwei Ye; Yoshihide Sekimoto
**Relevance:** 4/5 — Directly addresses LLM-based agent learning through exploratory execution, tool use, and experience distillation—core agent capabilities that affect frontier model reasoning.
**Depth:** 4/5 — Presents a clear four-stage methodology (Explore, Compare, Distill, Reinject) with concrete evaluation on 17 tasks and identifies a specific bottleneck (how exploratory experience is reused) that prior agent systems don't address.

### [Route by State, Recover from Trace: STAR with Failure-Aware Markov Routing for Multi-Agent Spatiotemporal Reasoning](https://arxiv.org/abs/2605.10057)
**Source:** arxiv | **Authors:** Ruiyi Yang; Lihuan Li; Hao Xue; Flora D. Salim
**Relevance:** 4/5 — Directly addresses LLM-based agent systems' core challenge: routing and recovery among multiple specialized agents with typed failure handling, a key frontier capability for agent robustness.
**Depth:** 4/5 — Presents explicit methodology (failure-aware Markov routing matrix, state-conditioned transitions learned from execution traces) with concrete empirical results across three benchmarks and eight LLMs, including ablations proving typed failure routing's necessity.

### [TRACE: Distilling Where It Matters via Token-Routed Self On-Policy Alignment](https://arxiv.org/abs/2605.10194)
**Source:** arxiv | **Authors:** Jiaxuan Wang; Xuan Ouyang; Zhiyu Chen; Yulan Hu; Zheng Pan; Xin Li; Lan-Zhe Guo
**Relevance:** 4/5 — TRACE directly addresses LLM agent training through on-policy self-distillation and reasoning alignment, core capabilities for agentic behavior in math and reasoning tasks.
**Depth:** 4/5 — The paper provides detailed methodology (token-routed KL strategies, span masking, annealing schedules), concrete empirical results across multiple benchmarks with ablation analysis, and explicit diagnosis of prior approach failure (gradient waste, entropy rise, OOD degradation).

### [Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution](https://arxiv.org/abs/2605.10223)
**Source:** arxiv | **Authors:** Kai Pan; Rong Hou
**Relevance:** 4/5 — Directly addresses LLM-based agent deployment with focus on governance, safety mechanisms, and architectural patterns essential for enterprise agent systems.
**Depth:** 4/5 — Provides concrete methodology (risk-adaptive tiering, separation of powers, verifier-recovery loops) and formalizes tier selection, distilled from production SaaS platform experience.

### [SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems](https://arxiv.org/abs/2605.10246)
**Source:** arxiv | **Authors:** Zonglin Yang; Xingtong Liu; Xinyan Xu
**Relevance:** 4/5 — Directly evaluates LLM-based AI scientist agents' ability to reason about task feasibility and honesty, a frontier capability concern for autonomous research systems.
**Depth:** 4/5 — Provides systematic benchmark design (33 scenarios, 11 trap categories), concrete evaluation results across 7 models (34.2% integrity problem rate), and mechanistic insights from ablation revealing completion bias as root cause.

### [EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents](https://arxiv.org/abs/2605.10332)
**Source:** arxiv | **Authors:** Ruofei Ju; Xinrui Wang; Xin Ding; Yifan Yang; Hao Wu; Shiqi Jiang; Qianxi Zhang; Hao Wen; Xiangyu Li...
**Relevance:** 4/5 — Directly addresses LLM-based embodied agent self-improvement through skill learning and reflection, a frontier capability for autonomous agent deployment.
**Depth:** 4/5 — Provides clear methodology for skill-aware trajectory reflection with distinction between skill errors and execution lapses, plus concrete benchmarks (93.28% on ALFWorld, 31.58% improvement over GPT-4) demonstrating practical impact.

### [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347)
**Source:** arxiv | **Authors:** Weikai Xu; Kun Huang; Yunren Feng; Jiaxing Li; Yuhan Chen; Yuxuan Liu; Zhizheng Jiang; Heng Qu; Peng...
**Relevance:** 4/5 — Directly addresses LLM-based mobile GUI agents, world models for action prediction, and agent guidance mechanisms—core frontier capabilities for planning and environment interaction.
**Depth:** 4/5 — Provides solid methodology (four modality comparisons, rigorous benchmarking across three downstream tasks) and concrete empirical findings on world-model utility, data transfer, and agent verification—addressing practical limitations in prior work.

### [Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values](https://arxiv.org/abs/2605.10365)
**Source:** arxiv | **Authors:** Haonan Dong; Qiguan Feng; Kehan Jiang; Haoran Ye; Xin Zhang; Guojie Song
**Relevance:** 4/5 — Directly addresses evaluation and safety of LLM-based agents, a frontier capability concern, with comprehensive empirical methodology across multiple agent harnesses and models.
**Depth:** 4/5 — Substantial contribution with 394 executable environments, 4,335 tasks, professional curation, trajectory-level evaluation rubrics, and concrete findings about value alignment mechanisms in agentic systems.

### [EGL-SCA: Structural Credit Assignment for Co-Evolving Instructions and Tools in Graph Reasoning Agents](https://arxiv.org/abs/2605.10366)
**Source:** arxiv | **Authors:** Zike Yuan; Yukun Cao; Han Zhang; Jianzhi Yan; Le Liu; Cai ke; Yue Yu; Hui Wang; Ming Liu; Bing Qin
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and tool use with a novel framework for credit assignment that jointly optimizes instructions and tools.
**Depth:** 4/5 — Presents clear methodology (structural credit assignment mapping trajectory evidence to conditional updates, dual-space co-evolution) with concrete benchmark results (92.0% success rate on graph reasoning tasks) and explicit comparison against baselines.

### [Can Agent Benchmarks Support Their Scores? Evidence-Supported Bounds for Interactive-Agent Evaluation](https://arxiv.org/abs/2605.10448)
**Source:** arxiv | **Authors:** Shanshan Gao; Liyi Zhou
**Relevance:** 4/5 — Directly addresses evaluation and benchmarking of LLM-based agents, a core concern for understanding agent capabilities and limitations.
**Depth:** 4/5 — Introduces a concrete methodological framework (outcome evidence reporting layer) with empirical validation across five established agent benchmarks, revealing distinct failure modes in current evaluation practices.

### [SkillEvolver: Skill Learning as a Meta-Skill](https://arxiv.org/abs/2605.10500)
**Source:** arxiv | **Authors:** Genrui Zhang; Erle Zhu; Jinfeng Zhou; Caiyan Jia; Hongning Wang
**Relevance:** 4/5 — Directly addresses LLM-based agent skill learning and improvement—a core agent capability—with a concrete system that enables agents to iteratively refine their own skills in deployment.
**Depth:** 4/5 — Provides clear methodology (meta-skill architecture, deployment-driven refinement, overfitting audits) and substantive empirical results across 83 tasks with quantified improvements (56.8% vs 43.6% baseline).

### [Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability](https://arxiv.org/abs/2605.10516)
**Source:** arxiv | **Authors:** Harsh Raj; Niranjan Orkat; Suvrorup Mukherjee; Aritra Guha; Cheryl Flynn; Subhabrata Majumdar
**Relevance:** 4/5 — Directly addresses evaluation and reliability of LLM-based agents, a core capability that impacts agent deployment and robustness.
**Depth:** 4/5 — Provides rigorous mathematical methodology (U-statistics, kernel-based metrics) with extensive validation across agentic benchmarks, demonstrating diagnostic insights beyond standard metrics.

### [Agent-First Tool API: A Semantic Interface Paradigm for Enterprise AI Agent Systems](https://arxiv.org/abs/2605.10555)
**Source:** arxiv | **Authors:** Kai Pan
**Relevance:** 4/5 — Directly addresses a core infrastructure challenge for LLM-based agents in production—tool API design—with explicit methodology and quantified results on agent task success.
**Depth:** 4/5 — Proposes concrete mechanisms (Six-Verb Protocol, Normalized Tool Contract, dual-layer governance) with production validation across 85 tools and comparative benchmarks showing substantial performance gains over baselines.

### [PRISM: Generation-Time Detection and Mitigation of Secret Leakage in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.10614)
**Source:** arxiv | **Authors:** Riya Tapwal; Abhishek Kumar; Carsten Maple
**Relevance:** 4/5 — Directly addresses a critical safety and operational challenge in multi-agent LLM systems, which is central to frontier agent research and deployment.
**Depth:** 4/5 — Provides detailed methodology combining 16 signals with generation-time monitoring, concrete quantitative results on a 2,000-task benchmark, and explicit analysis of why existing defenses fail for this setting.

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

### [Behavioral Determinants of Deployed AI Agents in Social Networks: A Multi-Factor Study of Personality, Model, and Guardrail Specification](https://arxiv.org/abs/2605.08463)
**Source:** arxiv | **Authors:** Sarah Wilson; Diem Linh Dang; Usman Ali Moazzam; Shan Ye; Gail Kaiser
**Relevance:** 4/5 — Directly studies deployed LLM-based agents in social environments with systematic variation of agent configuration (personality, model, guardrails) as determinants of emergent behavior.
**Depth:** 3/5 — Provides concrete empirical results from controlled multi-factor study with quantified behavioral metrics across 13 agents over 400 sessions, though focuses more on observational findings than novel methodology or architectural insights.

### [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](https://arxiv.org/abs/2605.09104)
**Source:** arxiv | **Authors:** Yuxi Chen; Junming Chen; Chenyu He; Yiwei Li; Yicheng Ji; Yifan Wu; Dingyu Yang; Lansong Diao; Lidan...
**Relevance:** 4/5 — Directly addresses a core constraint of LLM-based agents (token consumption and efficiency) through a systematic framework that spans agent optimization, multi-agent systems, and ecosystems.
**Depth:** 3/5 — Provides a unified conceptual taxonomy grounded in economic theory (neoclassical firm theory, transaction costs, mechanism design) rather than algorithmic methodology, synthesizing existing literature without presenting novel empirical results or mechanisms.

### [MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments](https://arxiv.org/abs/2605.09131)
**Source:** arxiv | **Authors:** Giridhar Ganapavarapu; Dhaval Patel
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture by integrating world models into the MCP ecosystem to improve planning and execution capabilities.
**Depth:** 3/5 — Presents methodology for combining world models with agents and MCP, includes experimental evaluation across 20+ tasks with new metrics, but the core contribution is primarily engineering integration rather than novel frontier capability or mechanism.

### [The Metacognitive Probe: Five Behavioural Calibration Diagnostics for LLMs](https://arxiv.org/abs/2605.09844)
**Source:** arxiv | **Authors:** Rafael C. T. Oliveira
**Relevance:** 4/5 — Directly addresses a frontier model capability—confidence calibration and metacognitive alignment—that materially affects agent reliability, planning, and deployment decisions.
**Depth:** 3/5 — Provides concrete diagnostic methodology with specific quantitative results (47-point dissociation, calibration scores) and surfaces a real limitation of prior benchmarks, but the instrument is exploratory rather than establishing new mechanisms.

### [RADAR: Redundancy-Aware Diffusion for Multi-Agent Communication Structure Generation](https://arxiv.org/abs/2605.09907)
**Source:** arxiv | **Authors:** Zhen Zhang; Wanjing Zhou; Juncheng Li; Hao Fei; Jun Wen; Wei Ji
**Relevance:** 4/5 — Directly addresses multi-agent LLM system design with focus on communication topology optimization, a key structural problem in agent coordination and efficiency.
**Depth:** 3/5 — Provides concrete methodology using conditional discrete graph diffusion for adaptive communication structure generation, with comprehensive experimental validation across six benchmarks showing accuracy, token, and robustness improvements.

### [FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models](https://arxiv.org/abs/2605.10141)
**Source:** arxiv | **Authors:** Zeynel A. Ulu\c{s}an; Burak S. Akbudak; Can S. Erer; G\"ozde G\"ul \c{S}ahin
**Relevance:** 4/5 — Directly addresses reward modeling for LLM-based agents in formal theorem proving, a frontier capability that enables agent reasoning and planning in structured domains.
**Depth:** 3/5 — Provides concrete benchmark methodology with error injection strategies and empirical results across multiple model classes, though the contribution is primarily evaluative rather than proposing new agent architectures or training mechanisms.

### [Agent-X: Full Pipeline Acceleration of On-device AI Agents](https://arxiv.org/abs/2605.10380)
**Source:** arxiv | **Authors:** Jinha Chung; Byeongjun Shin; Jiin Kim; Minsoo Rhu
**Relevance:** 4/5 — Directly addresses on-device LLM-based agent deployment and latency reduction through agent-specific optimization techniques (prefix caching and speculative decoding).
**Depth:** 3/5 — Provides concrete methodology (prompt rewriting, LLM-free speculative decoding) and measurable results (1.61x speedup with no accuracy loss), but focuses on systems optimization rather than advancing agent reasoning or capabilities.

### [Agentic Performance at the Edge: Insights from Benchmarking](https://arxiv.org/abs/2605.10384)
**Source:** arxiv | **Authors:** Shiqiang Wang; Herbert Woisetschl\"ager
**Relevance:** 4/5 — Directly addresses LLM-based agent deployment and performance under realistic constraints, examining how model size, tool integration, and domain affect agentic task quality.
**Depth:** 3/5 — Provides concrete empirical methodology (domain-conditioned evaluation, Pareto analysis) and actionable results on model-tool interactions and failure modes, though focused on benchmarking rather than architectural innovation.


## Worth knowing (59 items)

_On-criterion but lower depth, or peripheral relevance._

### [Position: How can Graphs Help Large Language Models?](https://arxiv.org/abs/2605.02452)
**Source:** arxiv | **Authors:** Xiyuan Wang; Yi Hu; Yanbo Wang; Chuan Shi; Muhan Zhang
**Relevance:** 4/5 — Directly addresses how graphs enhance LLM reasoning and planning through prompting techniques (CoT, ToT, GoT) and knowledge integration, which are core capabilities for LLM-based agents.
**Depth:** 2/5 — Position paper that surveys existing techniques and outlines directions rather than presenting novel methodology, concrete benchmarks, or detailed mechanistic insights into graph-LLM integration.

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

### [The Attacker in the Mirror: Breaking Self-Consistency in Safety via Anchored Bipolicy Self-Play](https://arxiv.org/abs/2605.08427)
**Source:** arxiv | **Authors:** Gabriele La Malfa; Emanuele La Malfa; Saar Cohen; Jie M. Zhang; Michael Luck; Michael Wooldridge; El...
**Relevance:** 3/5 — Directly addresses LLM safety and robustness via self-play methods, which is foundational to safe agent deployment, but is primarily a safety technique rather than core agent capability advancement.
**Depth:** 4/5 — Provides clear methodology (Anchored Bipolicy Self-Play with role-specific LoRAs), identifies theoretical limitations of prior work, and reports concrete empirical results (100x parameter efficiency, safety improvements across benchmarks).

### [Mirror, Mirror on the Wall: Can VLM Agents Tell Who They Are at All?](https://arxiv.org/abs/2605.08816)
**Source:** arxiv | **Authors:** Filippo Ziliotto; Ciro Beneduce; Bruno Lepri; Luciano Serafini; Massimiliano Luca; Tommaso Campari
**Relevance:** 3/5 — Directly evaluates a frontier VLM agent capability (embodied self-recognition and grounding) with rigorous methodology, but assesses perception/cognition rather than core agent functions like reasoning, planning, or tool use.
**Depth:** 4/5 — Strong methodology with controlled 3D benchmark, systematic ablations (mirror removal, misleading cues, occluded reflections), and decision-process evaluation (seeking, temporal ordering, attribution, consistency checks) that isolate causal mechanisms from confounds.

### [Internalizing Safety Understanding in Large Reasoning Models via Verification](https://arxiv.org/abs/2605.08930)
**Source:** arxiv | **Authors:** Yi Zhang; Yuxin Chen; Leheng Sheng; Dongcheng Zhang; Chaochao Lu; Xiang Wang; An Zhang
**Relevance:** 3/5 — Addresses safety alignment of large reasoning models, which is relevant to agent capability and deployment, but focuses on response verification rather than core agent mechanisms like planning, tool use, or reasoning architectures.
**Depth:** 4/5 — Provides clear methodology (training LRMs on safety verification tasks), concrete empirical analysis of alignment failures, and demonstrates generalization results against jailbreaks, with ablations showing benefits of internalized versus behavioral alignment.

### [CauSim: Scaling Causal Reasoning with Increasingly Complex Causal Simulators](https://arxiv.org/abs/2605.09079)
**Source:** arxiv | **Authors:** Nicol\'as Astorga; Anita Kriz; Mihaela van der Schaar
**Relevance:** 3/5 — Causal reasoning is a frontier capability relevant to agent reasoning and planning, but this work focuses on scaling causal understanding in LLMs rather than on LLM-based agents or agent deployment.
**Depth:** 4/5 — The paper presents solid methodology for constructing executable causal simulators, systematic empirical studies on curriculum scaling and data augmentation, and concrete results on generalization across representations.

### [Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning](https://arxiv.org/abs/2605.09292)
**Source:** arxiv | **Authors:** Xia Yang; Xuanyi Zhang; Hao Hu; Feng Ji
**Relevance:** 3/5 — Evaluates a frontier model capability (mathematical reasoning flexibility) with concrete methodology and results, but focuses on benchmarking rather than agent architecture, planning, or tool use.
**Depth:** 4/5 — Introduces a rigorous strategy-level evaluation framework with dual-AI annotation, human adjudication, and systematic analysis across frontier models revealing a meaningful decoupling between accuracy and reasoning flexibility.

### [Benchmarking Safety Risks of Knowledge-Intensive Reasoning under Malicious Knowledge Editing](https://arxiv.org/abs/2605.10146)
**Source:** arxiv | **Authors:** Qinghua Mao; Xi Lin; Jinze Gu; Jun Wu; Siyuan Li; Yuliang Chen
**Relevance:** 3/5 — Safety evaluation of knowledge editing in LLMs is adjacent to agent capabilities, but focuses on a specific vulnerability rather than core agent reasoning, planning, or tool-use mechanisms.
**Depth:** 4/5 — The work provides systematic methodology (unified benchmark framework with multi-level reasoning tasks), concrete evaluation results across models, and identifies key factors (edit scale, knowledge characteristics, reasoning complexity) that influence safety risks.

### [Budget-Efficient Automatic Algorithm Design via Code Graph](https://arxiv.org/abs/2605.10598)
**Source:** arxiv | **Authors:** Maxime Bouscary; Manxi Wu; Saurabh Amin
**Relevance:** 3/5 — Uses LLMs for automatic algorithm design with structured reasoning, but is not fundamentally about LLM-based agents or frontier model capabilities—it treats LLMs as a tool for a downstream optimization task rather than studying agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides substantial methodology (DAG representation, correction-level credit assignment, budget-depth-breadth tradeoffs) and empirical validation on concrete problems, with clear insights about when context helps or hinders LLM performance.

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

### [Measuring What Matters: Benchmarking Generative, Multimodal, and Agentic AI in Healthcare](https://arxiv.org/abs/2605.08445)
**Source:** arxiv | **Authors:** Prasanna Desikan; Harshit Rajgarhia; Shivali Dalmia; Ananya Mantravadi
**Relevance:** 3/5 — Benchmarking framework for agentic AI in healthcare is on-topic for agent evaluation, but the work is domain-specific (healthcare) rather than frontier agent research itself.
**Depth:** 3/5 — The paper provides concrete performance gaps (0.53–0.85 across tasks) and identifies a methodological problem (ad hoc benchmarks fail to measure real-world reliability), but appears to be a position/framework paper rather than delivering new agent capabilities or training methods.

### [Results and Retrospective Analysis of the CODS 2025 AssetOpsBench Challenge](https://arxiv.org/abs/2605.08518)
**Source:** arxiv | **Authors:** Dhaval Patel; Chathurangi Shyalika; Suryanarayana Reddy Yarrabothula; Ling Yue; Shuxin Lin; Nianjun ...
**Relevance:** 3/5 — Directly analyzes multi-agent orchestration benchmarking and evaluation methodology, but focuses on competition retrospective and leaderboard analysis rather than advancing agent capabilities or training methods.
**Depth:** 3/5 — Provides concrete empirical findings about evaluation design (leaderboard saturation, public-private correlation, guardrail importance) and methodological insights about competition structure, but lacks novel agent architecture or capability contributions.

### [DiagnosticIQ: A Benchmark for LLM-Based Industrial Maintenance Action Recommendation from Symbolic Rules](https://arxiv.org/abs/2605.08614)
**Source:** arxiv | **Authors:** Devin Yasith De Silva; Dhaval Patel; Christodoulos Constantinides; Shuxin Lin; Nianjun Zhou; Paul J ...
**Relevance:** 3/5 — Evaluates LLM decision-making under real-world constraints (rule interpretation, robustness), directly relevant to agent deployment but narrowly focused on a specific industrial task rather than core agent reasoning or capability advancement.
**Depth:** 3/5 — Provides solid benchmark methodology (symbolic-to-MCQA pipeline, five failure-mode variants, 29-model evaluation) and reveals concrete brittleness patterns (13–60% accuracy drops, 49–63% pattern-matching bias), but findings are incremental limitations rather than methodological breakthroughs in agent design or model capability.

### [Re$^2$Math: Benchmarking Theorem Retrieval in Research-Level Mathematics](https://arxiv.org/abs/2605.09012)
**Source:** arxiv | **Authors:** Zicheng Lyu; Wenjie Yang; Shengzhong Zhang; Zengfeng Huang
**Relevance:** 3/5 — Directly addresses tool use and retrieval for LLM-based mathematical reasoning agents, but focuses on a narrow domain-specific task rather than frontier agent capabilities or model training.
**Depth:** 3/5 — Provides a well-structured benchmark with clear methodology for evaluating source-grounded retrieval and diagnostic evaluation, but lacks novel architectural insights or training methods that would shape agent capabilities.

### [From Passive Reuse to Active Reasoning: Grounding Large Language Models for Neuro-Symbolic Experience Replay](https://arxiv.org/abs/2605.09419)
**Source:** arxiv | **Authors:** Yanan Xiao; Yixiang Tang; Zechen Feng; Lu Jiang; Minghao Yin; Pengyang Wang
**Relevance:** 3/5 — Uses LLMs for reasoning about RL experience replay, but the core contribution is RL-specific optimization rather than LLM-based agent capabilities or frontier model properties.
**Depth:** 3/5 — Presents a concrete neuro-symbolic methodology grounding LLM reasoning into differentiable logic with empirical results, but the LLM component is instrumental rather than exploring frontier agent capabilities or emergent model behaviors.

### [EpiGraph: A Knowledge Graph and Benchmark for Evidence-Intensive Reasoning in Epilepsy](https://arxiv.org/abs/2605.09505)
**Source:** arxiv | **Authors:** Yuyang Dai; Zheng Chen; Jathurshan Pradeepkumar; Yasuko Matsubara; Jimeng Sun; Yasushi Sakurai; Yush...
**Relevance:** 3/5 — The work evaluates LLMs with Graph-RAG for clinical reasoning tasks, which relates to agent-like augmentation patterns, but is domain-specific (epilepsy) without advancing frontier LLM capabilities or core agent methodologies.
**Depth:** 3/5 — Provides concrete benchmark results (+30–41% gains with Graph-RAG) and methodology (knowledge graph integration with five clinical tasks), but the contribution is primarily in domain knowledge engineering rather than novel agent mechanisms or model capabilities.

### [PDEAgent-Bench: A Multi-Metric, Multi-Library Benchmark for PDE Solver Generation](https://arxiv.org/abs/2605.09636)
**Source:** arxiv | **Authors:** Zhen Hang; Yushan Yashengjiang; Junhui Li; Huanshuo Dong; Yang Wei; Zhezheng Hao; Jiangtao Ma; Songl...
**Relevance:** 3/5 — Directly evaluates LLM agent capability on a specialized code generation task, but the domain (numerical PDE solving) is narrowly specialized rather than central to frontier agent capabilities.
**Depth:** 3/5 — Introduces a well-structured multi-metric benchmark with concrete evaluation results showing agent limitations, but lacks methodological contributions to agent architecture or training.

### [Absurd World: A Simple Yet Powerful Method to Absurdify the Real-world for Probing LLM Reasoning Capabilities](https://arxiv.org/abs/2605.09678)
**Source:** arxiv | **Authors:** Ryan Albright; Golam Md Muktadir; Zarif Ikram; S M Jubaer; Mehrab Hossain; Dianbo Liu
**Relevance:** 3/5 — Directly evaluates LLM reasoning capabilities through systematic benchmarking, which is relevant to understanding frontier model capabilities, but does not address agent-specific mechanisms (planning, tool use, memory) or training methods that enable agents.
**Depth:** 3/5 — Provides a methodology for probing reasoning robustness through symbolic manipulation and altered realism scenarios with evaluation across multiple models and prompting techniques, offering solid methodological contribution but lacks novel architectural insights or breakthrough-level results on agent capabilities.

### [AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks](https://arxiv.org/abs/2605.10286)
**Source:** arxiv | **Authors:** Baraa Al Jorf; Farah E. Shamout
**Relevance:** 3/5 — Directly evaluates LLM-based agents on multimodal clinical tasks, but the application domain (healthcare) and lack of novel agent methodology limits centrality to frontier LLM agent research.
**Depth:** 3/5 — Provides systematic evaluation with concrete benchmark results and comparative analysis (single vs. multi-agent systems), but focuses on application benchmarking rather than advancing agent architecture or reasoning mechanisms.

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

### [AI-Care: A Conversational Agentic System for Task Coordination in Alzheimer's Disease Care](https://arxiv.org/abs/2605.08480)
**Source:** arxiv | **Authors:** Preyash Yadav; Michelle Cohn; Priyanka Koppolu; Hritvik Agarwal; Amey Gohil; Tejas Patil; Sasha Pime...
**Relevance:** 3/5 — Describes an LLM-based conversational agent system with multi-turn reasoning and tool use, but focuses on a specific healthcare application rather than frontier agent capabilities or methodology.
**Depth:** 2/5 — Provides system architecture and design rationale (LangGraph orchestration, safety controls, clarification loops) but lacks detailed methodology, benchmark evaluations, or concrete capability insights that would advance understanding of LLM agents.

### [Shaping Schema via Language Representation as the Next Frontier for LLM Intelligence Expanding](https://arxiv.org/abs/2605.09271)
**Source:** arxiv | **Authors:** Zhiqin Yang; Yuhan Liu; Jingwen Fu; Pei Fu anf Bo Han; Masashi Sugiyama; Nanning Zheng
**Relevance:** 3/5 — Language representation design is relevant to LLM agent capabilities but addresses prompt/representation engineering rather than core agent architectures, reasoning mechanisms, or model capabilities that enable agents.
**Depth:** 2/5 — The paper claims formalization and controlled experiments but reads primarily as a position paper reviewing existing practices without presenting novel methodologies, detailed experimental results, or mechanistic insights into how representation shapes reasoning.

### [A Prompt-Aware Structuring Framework for Reliable Reuse of AI-Generated Content in the Agentic Web](https://arxiv.org/abs/2605.09283)
**Source:** arxiv | **Authors:** Shusaku Egami; Masahiro Hamasaki
**Relevance:** 3/5 — Directly addresses LLM-agent reliability and reuse in agentic systems, but focuses on metadata/provenance rather than agent reasoning or core model capabilities.
**Depth:** 2/5 — Proposes a framework for AIGC metadata attachment with structured components, but lacks concrete methodology details, evaluation results, or comparative analysis of the approach.

### [Reliable AI Needs to Externalize Implicit Knowledge: A Human-AI Collaboration Perspective](https://arxiv.org/abs/2605.02010)
**Source:** arxiv | **Authors:** Hengyu Liu; Tianyi Li; Zhihong Cui; Yushuai Li; Zhangkai Wu; Torben Bach Pedersen; Kristian Torp; Ch...
**Relevance:** 3/5 — Addresses reliability and verification of LLM reasoning—a real concern for deployed agents—but is a position paper proposing a framework rather than demonstrating empirical methodology or results on agent-specific problems.
**Depth:** 1/5 — Identifies a genuine problem (implicit knowledge verification) and sketches a conceptual solution (Knowledge Objects), but provides no concrete methodology, algorithms, empirical evaluation, or case studies demonstrating how KOs would work in practice.

### [From Pixels to Prompts: Vision-Language Models](https://arxiv.org/abs/2605.07544)
**Source:** arxiv | **Authors:** Khang Hoang Nhat Vo
**Relevance:** 3/5 — Vision-language models are foundational for multimodal agents, but this is a survey/tutorial book focused on conceptual understanding rather than novel agent architectures or frontier capabilities.
**Depth:** 1/5 — The excerpt promises a pedagogical mental map and intuition-building rather than new methodology, concrete results, or limitations analysis that would substantiate a research contribution.

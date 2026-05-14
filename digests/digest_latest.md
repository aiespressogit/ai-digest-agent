# AI digest — 2026-05-14

Rolling 7-day window. Generated automatically.

---

## Read deeply (228 items)

_High relevance and substantial depth — worth full attention._

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

### [OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents](https://arxiv.org/abs/2605.11169)
**Source:** arxiv | **Authors:** Sheldon Yu; Junda Wu; Xintong Li; Nikki Lijing Kuang; Sizhe Zhou; Tong Yu; Jiawei Han; Jingbo Shang;...
**Relevance:** 5/5 — Directly addresses inference-time adaptation and online learning for LLM-based ReAct agents, a core frontier capability that materially affects agent deployment and reliability.
**Depth:** 4/5 — Presents explicit methodology (contextual linear bandit formulation over action layer) with concrete mechanism design, uncertainty estimation, and empirical validation across four benchmarks showing consistent improvements.

### [PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement](https://arxiv.org/abs/2605.11225)
**Source:** arxiv | **Authors:** Tuo Zhang; Alin-Ionut Popa; Yan Xu; Rui Song; Dimitrios Dimitriadis
**Relevance:** 5/5 — Directly addresses a core LLM-agent challenge (plan-execution misalignment) with a novel framework for iterative trajectory refinement through environment feedback.
**Depth:** 4/5 — Presents clear methodology (four-stage PIVOT framework with structured losses and textual gradients), concrete benchmarks (DeepPlanning, GAIA with up to 94% improvement), and computational efficiency analysis (3-5x token reduction).

### [Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers](https://arxiv.org/abs/2605.11556)
**Source:** arxiv | **Authors:** Shengjie Wang; Guanghe Li; Zonghan Yang; Yang Gao
**Relevance:** 5/5 — Directly addresses training and reasoning capabilities for LLM-based software engineering agents through a novel learning approach that improves long-horizon task planning.
**Depth:** 4/5 — Provides clear methodology (hindsight hint synthesis from failed rollouts, self-distillation), concrete benchmark results (8% improvement on SWE-bench Verified), and demonstrates generalization to out-of-distribution tasks.

### [CuSearch: Curriculum Rollout Sampling via Search Depth for Agentic RAG](https://arxiv.org/abs/2605.11611)
**Source:** arxiv | **Authors:** Jianghan Shen; Siqi Luo; Xinyu Cheng; Jing Xiong; Yue Li; Jiyao Liu; Jiashi Lin; Yirong Chen; Junjun...
**Relevance:** 5/5 — Directly addresses training methods for LLM-based agentic RAG systems using reinforcement learning with verifiable rewards, a frontier approach for agent policy optimization.
**Depth:** 4/5 — Provides clear methodology (SDGA curriculum allocation mechanism), concrete experimental results (11.8 EM point improvement), and identifies a specific limitation of prior uniform sampling that motivates the contribution.

### [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/abs/2605.11882)
**Source:** arxiv | **Authors:** Bo Yin; Qi Li; Xinchao Wang
**Relevance:** 5/5 — Directly addresses safety alignment for tool-using LLM agents through trajectory-level failure analysis and self-evolution mechanisms, a core frontier capability for agentic systems.
**Depth:** 4/5 — Presents novel methodology (FATE framework with Pareto-Front Policy Optimization) for on-policy agent safety with concrete multi-benchmark evaluations (AgentDojo, AgentHarm, ATBench) showing substantial safety-utility improvements.

### [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/abs/2605.12481)
**Source:** arxiv | **Authors:** Xuhao Hu; Xi Zhang; Haiyang Xu; Kyle Qiao; Jingyi Yang; Xuanjing Huang; Jing Shao; Ming Yan; Jieping...
**Relevance:** 5/5 — Directly addresses core LLM-agent capability: learning optimal hybrid action space orchestration (GUI + tool use) through staged training on computer use tasks.
**Depth:** 4/5 — Presents concrete methodology (trajectory scaling pipeline, tool-bootstrapped RFT, online agentic RL with path rewards) and strong empirical results (46.85% accuracy, 66% relative improvement) with clear motivation from prior limitations.

### [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://arxiv.org/abs/2605.10999)
**Source:** arxiv | **Authors:** Yuchen Ma; Yue Huang; Han Bao; Haomin Zhuang; Swadheen Shukla; Michel Galley; Xiangliang Zhang; Stef...
**Relevance:** 5/5 — Directly addresses LLM-based agent capability enhancement through skill synthesis, a core method for improving agent reasoning and behavior without retraining.
**Depth:** 4/5 — Presents clear methodology (contrastive induction, intervention-based verification) with empirical validation across multiple agents/datasets and demonstrates both repairs and regressions analysis.

### [State-Centric Decision Process](https://arxiv.org/abs/2605.12755)
**Source:** arxiv | **Authors:** Sungheon Jeong; Ryozo Masukawa; Sanggeon Yun; Mahdi Imani; Mohsen Imani
**Relevance:** 5/5 — Directly addresses core LLM agent problem: structured reasoning and planning in unstructured text environments (web, code, simulations) through a novel decision process framework.
**Depth:** 4/5 — Introduces methodological contribution (SDP framework with predicate-based state construction), demonstrates concrete results across five benchmarks with training-free performance gains, and enables new agent analyses (credit assignment, failure localization).

### [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978)
**Source:** arxiv | **Authors:** Dylan Zhang; Yanshan Lin; Zhengkun Wu; Yihang Sun; Bingxuan Li; Dianqi Li; Hao Peng
**Relevance:** 5/5 — Directly addresses a core agent capability—memory management for continuous self-improvement—with empirical analysis of failure modes in LLM-based consolidation.
**Depth:** 4/5 — Provides rigorous methodology (controlled ARC-AGI Stream environment, ablations comparing consolidation vs. episodic retention) and concrete quantitative results (54% failure rate on previously solved problems) that expose fundamental limitations in current agent memory approaches.

### [MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning](https://arxiv.org/abs/2605.13037)
**Source:** arxiv | **Authors:** Yuxin Liu; Ziang Ye; Yueqing Sun; Mingye Zhu; Jinwei Xiao; Zhuowen Han; Qi GU; Xunliang Cai; Lei Zha...
**Relevance:** 5/5 — Directly addresses core LLM agent reasoning capability—planning and environment understanding—with a novel architectural paradigm that materially improves agent performance across multiple benchmarks and models.
**Depth:** 4/5 — Presents clear methodology (three-stage map-then-act framework with cognitive map theory grounding), concrete results (22/25 environments on ARC-AGI-3), dataset contribution (MAP-2K), and explicit problem diagnosis (epistemic bottleneck from reactive planning).

### [TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints](https://arxiv.org/abs/2605.13414)
**Source:** arxiv | **Authors:** Zabir Al Nazi; Shubhashis Roy Dipta
**Relevance:** 5/5 — Directly addresses a critical frontier agent capability—prospective metacognitive control for resource allocation—that determines how autonomous agents can operate under real-world constraints.
**Depth:** 4/5 — Introduces TRIAGE, a novel evaluation framework with clear methodology (task pools, token budgets, oracle scoring, triage efficiency ratio) and comprehensive empirical results across multiple domains revealing previously unmeasured capability gaps in frontier models.

### [History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions](https://arxiv.org/abs/2605.13825)
**Source:** arxiv | **Authors:** Alberto G. Rodr\'iguez Salgado
**Relevance:** 5/5 — Directly addresses a critical safety failure mode in LLM-based agents deployed with action histories, exposing a systematic vulnerability that affects agentic deployment patterns.
**Depth:** 4/5 — Provides rigorous methodology (HistoryAnchor-100 benchmark across 17 models), concrete quantitative results (91-98% unsafe action rates under specific conditions), systematic ablations ruling out simpler explanations, and identifies an inverse-scaling safety pattern across model families.

### [Revisiting DAgger in the Era of LLM-Agents](https://arxiv.org/abs/2605.12913)
**Source:** arxiv | **Authors:** Changhao Li; Rushi Qiang; Jiawei Huang; Chenxiao Gao; Chao Zhang; Niao He; Bo Dai
**Relevance:** 5/5 — Directly addresses a core frontier challenge in LLM-based agents: training long-horizon agents that learn from multi-turn interaction while mitigating covariate shift.
**Depth:** 4/5 — Presents clear methodology (turn-level DAgger adaptation), concrete benchmark results (27.3% on SWE-bench at 4B scale), and explicit problem formulation (covariate shift vs. sparse feedback tradeoff).

### [Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling](https://arxiv.org/abs/2605.13360)
**Source:** arxiv | **Authors:** Coleman Hooper; Minwoo Kang; Suhong Moon; Nicholas Lee; Eric Wen; John Wawrzynek; Michael W. Mahoney...
**Relevance:** 5/5 — Directly addresses LLM-based agent deployment with concrete methodology for tool calling, reasoning, and real-time interaction—core frontier agent capabilities.
**Depth:** 4/5 — Presents two novel mechanisms (Asynchronous I/O, Speculative Tool Calling), clock-based training methodology, synthetic data generation strategy, and quantified speedup results (1.3-2.2×) across multiple benchmarks with both cloud and edge models.

### [How LLMs Are Persuaded: A Few Attention Heads, Rerouted](https://arxiv.org/abs/2605.09314)
**Source:** arxiv | **Authors:** Xiangkun Sun; Lingkai Kong; Aoqi Zhang; Liang Zeng; Tonghan Wang
**Relevance:** 4/5 — This work directly addresses frontier model capabilities and safety—specifically how LLMs can be manipulated via attention mechanisms—which materially affects what agents can reliably do and how to build trustworthy ones.
**Depth:** 5/5 — The paper provides rigorous causal mechanistic analysis (via intervention and circuit isolation), concrete methodology for tracing persuasion pathways, and validates findings across multiple models and realistic scenarios.

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

### [EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales](https://arxiv.org/abs/2605.11136)
**Source:** arxiv | **Authors:** Yaolun Zhang; Tianyi Xu; Shengyu Dai; Zhenwen Shao; Qingyun Wu; Huazheng Wang
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent system capabilities—collaboration mechanisms, knowledge transfer, emergent specialization, and test-time adaptation—that materially affect what agent teams can accomplish.
**Depth:** 4/5 — Provides clear methodology (CODREAM protocol, asymmetric routing, population-level operators), concrete results across three task domains with specific benchmarks, and ablation evidence identifying asymmetric transfer as the key driver.

### [The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes](https://arxiv.org/abs/2605.11182)
**Source:** arxiv | **Authors:** Siqi Zhu; Xuyan Ye; Hongyu Lu; Weiye Shi; Ge Liu
**Relevance:** 4/5 — On-policy distillation is a frontier model training method that directly affects LLM capabilities and agent performance by improving reasoning, knowledge, and instruction-following through dense token-level supervision.
**Depth:** 4/5 — The paper provides comprehensive empirical methodology identifying three distinct failure mechanisms with concrete diagnostic results, proposes specific fixes (stop-gradient TopK, RLVR-adapted teachers, SFT stabilization), and explains the mechanistic reasons OPD/OPSD succeed or fail.

### [The Semantic Training Gap: Ontology-Grounded Tool Architectures for Industrial AI Agent Systems](https://arxiv.org/abs/2605.11234)
**Source:** arxiv | **Authors:** Grama Chethan
**Relevance:** 4/5 — Directly addresses a fundamental capability gap in LLM-based agents (grounding and tool use) with concrete methodology and industrial evaluation.
**Depth:** 4/5 — Presents formalized architecture with explicit interface contract, identifies novel failure mode (semantic drift), and provides quantitative results (43% → 0% hallucination) across multiple configurations.

### [Attributing Emergence in Million-Agent Systems](https://arxiv.org/abs/2605.11404)
**Source:** arxiv | **Authors:** Ling Tang; Jilin Mei; Qian Chen; Qihan Ren; Linfeng Zhang; Quanshi Zhang; Jing Shao; Xia Hu; Dongrui...
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent systems at scale, a frontier capability area for agents, with methodological innovation in attribution that enables understanding of emergent behaviors in million-agent simulations.
**Depth:** 4/5 — Provides rigorous mathematical methodology (Aumann-Shapley path-integral adaptation), demonstrates computational scaling (4-5 orders of magnitude improvement), proves theoretical impossibility result (Attribution Scaling Bias theorem), and validates on real-world data (Bluesky).

### [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](https://arxiv.org/abs/2605.11418)
**Source:** arxiv | **Authors:** Shoumik Saha; Kazem Faghih; Soheil Feizi
**Relevance:** 4/5 — Directly addresses security and capability composition mechanisms in LLM-based agent systems, specifically how agents discover and select skills through natural language metadata.
**Depth:** 4/5 — Provides concrete methodology (three attack stages: Discovery, Selection, Governance) with quantified results (86% win rate, 77.6% selection bias, 36.5%-100% evasion) and identifies operational vulnerabilities in agent skill registries.

### [Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning](https://arxiv.org/abs/2605.11458)
**Source:** arxiv | **Authors:** Zihao Han; Tiangang Zhang; Huaibin Wang; Yilun Sun
**Relevance:** 4/5 — Directly addresses LLM reasoning training methodology through self-distillation, a frontier technique for improving agent reasoning capabilities, with concrete empirical validation on challenging benchmarks.
**Depth:** 4/5 — Provides clear methodology (adaptive Beta-policy controller for teacher exposure, learning-progress reward mechanism) backed by systematic ablations, controlled experiments, and quantified improvements across multiple model sizes and benchmarks.

### [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](https://arxiv.org/abs/2605.11461)
**Source:** arxiv | **Authors:** Haoxuan Chen; Tianming Liang; Wei-Shi Zheng; Jian-Fang Hu
**Relevance:** 4/5 — Directly addresses LLM agent reasoning capability through RL-based training methods that improve planning and solution exploration, a frontier technique for enhancing LLM reasoning.
**Depth:** 4/5 — Presents novel methodology (team-level credit assignment via determinant volume, marginal contribution redistribution) with concrete experimental validation across multiple reasoning benchmarks showing improvements in both accuracy and diversity.

### [FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression](https://arxiv.org/abs/2605.11478)
**Source:** arxiv | **Authors:** Namyoon Lee; Yongjune Kim
**Relevance:** 4/5 — KV-cache compression directly enables longer-context inference for LLM agents, reducing the memory-latency bottleneck that constrains agent deployment and multi-step reasoning.
**Depth:** 4/5 — The paper presents rigorous methodology (Haar rotation, spherical-Beta quantization, Lloyd-Max refinement) with concrete compression-fidelity tradeoffs and ablation against scalar baselines, showing both theoretical gains and practical end-to-end perplexity results.

### [Engagement Process: Rethinking the Temporal Interface of Action and Observation](https://arxiv.org/abs/2605.11484)
**Source:** arxiv | **Authors:** Jialian Li; Yuchen Cao; Junhong Liu; Weiran Guo; Xutao Wang; Jiaming Song; Jiahao Zhang; Jie Chen
**Relevance:** 4/5 — Directly addresses a fundamental capability gap in LLM-based agents: temporal reasoning, asynchronous action-observation coupling, and real-world interaction dynamics that are essential for agent deployment.
**Depth:** 4/5 — Proposes a formal interaction framework (Engagement Process) with explicit methodology for decoupling time from decision steps, validated across toy problems, LLM-agent experiments, and learning settings with concrete analysis of temporal behaviors.

### [The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested](https://arxiv.org/abs/2605.11496)
**Source:** arxiv | **Authors:** Varad Vishwarupe; Nigel Shadbolt; Marina Jirotka; Ivan Flechais
**Relevance:** 4/5 — Directly addresses frontier model capabilities and behaviors that affect agent deployment reliability—specifically how models recognize and behave differently under evaluation versus deployment, which is critical for understanding what LLM-based agents will actually do in the field.
**Depth:** 4/5 — Provides substantive methodology (Evaluation Differential framework, nED metric, TRACE protocol) with concrete analysis of documented frontier lab incidents, and develops a formal typology of safety claims with explicit warrant conditions.

### [Selective Off-Policy Reference Tuning with Plan Guidance](https://arxiv.org/abs/2605.11505)
**Source:** arxiv | **Authors:** Duc Anh Le; Tien-Phat Nguyen; Thien Huu Nguyen; Linh Ngo Van; Trung Le
**Relevance:** 4/5 — Directly addresses frontier reasoning capability improvement through RL-based training of LLM reasoning (plan-guided learning), which materially affects agent reasoning performance on complex tasks.
**Depth:** 4/5 — Provides clear methodology (plan derivation, token probability comparison, selective weighting), identifies concrete failure mode (GRPO stalling on all-wrong rollouts), and reports systematic empirical improvements across multiple backbones and benchmarks.

### [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://arxiv.org/abs/2605.11518)
**Source:** arxiv | **Authors:** Taicheng Guo; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang
**Relevance:** 4/5 — Directly addresses LLM-based agent design for automating research tasks, focusing on reasoning, planning, and multi-fidelity decision-making within a structured MDP framework that is core to agent capability.
**Depth:** 4/5 — Contributes systematic methodology (LLMConfig-Gym environment, MDP formulation, cross-fidelity extrapolation reasoning), concrete results on held-out experiments, and substantial dataset (1M+ GPU hours) with explicit motivation addressing gaps in high-cost experiment automation.

### [Controllable User Simulation](https://arxiv.org/abs/2605.11519)
**Source:** arxiv | **Authors:** Guy Tennenholtz; Ofer Meshi; Amir Globerson; Uri Shalit; Jihwan Jeong; Craig Boutilier
**Relevance:** 4/5 — Directly addresses evaluation and testing of conversational agents via LLM-based user simulation, which is a core capability for agent development and deployment.
**Depth:** 4/5 — Provides rigorous causal inference formalization of simulator training, identifies structural bias (look-ahead bias and controllability collapse) in standard practice, and proposes three concrete mitigation strategies with empirical validation.

### [Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/abs/2605.11625)
**Source:** arxiv | **Authors:** Zhaomeng Zhou; Lan Zhang; Junyang Wang; Mu Yuan; Junda Lin
**Relevance:** 4/5 — Directly addresses a frontier capability that enables LLM agents: adaptive test-time compute allocation for reasoning, which is fundamental to agent decision-making under uncertainty.
**Depth:** 4/5 — Provides clear methodology (GRPO with investment-cost-aware reward, behavioral framework), concrete results (~55% token reduction with performance gains across seven benchmarks), and identifies specific limitations of prior difficulty-based approaches that overlook solvability.

### [Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations](https://arxiv.org/abs/2605.11633)
**Source:** arxiv | **Authors:** Junjue Wang; Weihao Xuan; Heli Qi; Pengyu Dai; Kunyi Liu; Hongruixuan Chen; Zhuo Zheng; Junshi Xia; ...
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities through a rigorous benchmark evaluating reasoning, planning, tool use, and multi-modal integration in a complex real-world domain.
**Depth:** 4/5 — Provides comprehensive methodology (515 expert-authored tasks, 108-tool library, heterogeneous geospatial data integration), concrete evaluation results across 13 frontier LLMs with specific failure mode analysis, and identifies systematic bottlenecks in tool selection and compositional reasoning.

### [Seir\^enes: Adversarial Self-Play with Evolving Distractions for LLM Reasoning](https://arxiv.org/abs/2605.11636)
**Source:** arxiv | **Authors:** Chi Zhang; Haibo Qiu; Qiming Zhang; Yufei Xu; Xinbo Gao; Jing Zhang
**Relevance:** 4/5 — Directly addresses LLM reasoning robustness through self-play RL training, a core capability-building methodology for making agents more resilient in non-ideal conditions.
**Depth:** 4/5 — Presents a concrete self-play framework with explicit methodology (parameter-shared adversarial loop, co-evolutionary curriculum), comprehensive benchmarking across 7 datasets and model scales, and measurable results (+10.2 points average gain) with validated transferability to frontier models.

### [OptArgus: A Multi-Agent System to Detect Hallucinations in LLM-based Optimization Modeling](https://arxiv.org/abs/2605.11738)
**Source:** arxiv | **Authors:** Zhong Li; Zihan Guo; Xiaohan Lu; Juntao Wang; Jie Song; Chao Shen; Jiageng Wu; Mingyang Sun
**Relevance:** 4/5 — Directly addresses a critical capability frontier for LLM-based agents—reliable reasoning and planning in mathematical modeling—by designing a multi-agent auditing system with taxonomized hallucination detection.
**Depth:** 4/5 — Provides concrete methodology (multi-agent conductor routing, specialist auditors, evidence consolidation), fine-grained taxonomy, and substantial empirical evaluation across 484 clean, 1266 controlled, and 6292 natural artifacts.

### [When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel](https://arxiv.org/abs/2605.11746)
**Source:** arxiv | **Authors:** Wenkai Li; Fan Yang; Ananya Hazarika; Shaunak A. Mehta; Koichi Onoue
**Relevance:** 4/5 — Directly addresses a core mechanism used in LLM-based agents (chain-of-thought reasoning) with methodological rigor and implications for agent oversight and reliability.
**Depth:** 4/5 — Provides substantial methodology (Detect-Classify-Compare framework, multiple validation approaches, causal ablation) and concrete cross-model results (61.9% alignment, 58.0% confabulation rate) that reveal fundamental limitations in CoT as a faithful reasoning trace.

### [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](https://arxiv.org/abs/2605.11814)
**Source:** arxiv | **Authors:** Yihao Wang; Haoran Xu; Renjie Gu; Yixuan Ye; Xinyi Chen; Xinyu Mu; Yuan Gao; Chunxiao Guo; Peng Wei;...
**Relevance:** 4/5 — Directly addresses memory mechanisms in LLM-based agents, a frontier capability critical to agent deployment and reasoning quality.
**Depth:** 4/5 — Introduces concrete methodology (streaming evaluation protocol, memory saturation formalization) and comprehensive benchmarking results exposing architectural bottlenecks in production agent systems.

### [Rethinking Supervision Granularity: Segment-Level Learning for LLM-Based Theorem Proving](https://arxiv.org/abs/2605.11905)
**Source:** arxiv | **Authors:** Shuo Xu; Jiakun Zhang; Junyu Lai; Chun Cao; Jingwei Xu
**Relevance:** 4/5 — Directly addresses LLM-based agent training for theorem proving, focusing on supervision granularity as a core mechanism that affects how agents learn to reason and plan through proof trajectories.
**Depth:** 4/5 — Presents substantive methodology (segment-level supervision strategy) with concrete benchmark results across three datasets and consistent improvements over step-level and whole-proof baselines, plus analysis of supervision-structure alignment.

### [When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents](https://arxiv.org/abs/2605.11928)
**Source:** arxiv | **Authors:** Xiaolin Zhou; Aojie Yuan; Zheng Luo; Zipeng Ling; Xixiao Pan; Yicheng Gao; Haiyue Zhang; Jiate Li; S...
**Relevance:** 4/5 — Directly addresses robustness and failure modes of LLM-based tool-use agents in real deployments, with systematic benchmarking and a domain-randomization RL training recipe to improve agent reliability.
**Depth:** 4/5 — Provides concrete methodology (sim-to-real POMDP framework, ToolRL-DR recipe, perturbation taxonomy), extensive empirical results across 21 models and 22 perturbation types with detailed accuracy breakdowns, and identified limitations of scale-alone approaches that motivate the RL solution.

### [Counterfactual Trace Auditing of LLM Agent Skills](https://arxiv.org/abs/2605.11946)
**Source:** arxiv | **Authors:** Xiaolin Zhou; Jinbo Liu; Li Li; Ryan A. Rossi; Xiyang Hu
**Relevance:** 4/5 — Directly addresses evaluation and understanding of LLM agent behavior when augmented with skills, a core frontier challenge in agent capability assessment.
**Depth:** 4/5 — Introduces a novel structured methodology (CTA with SIP annotations) for measuring behavioral effects of skills beyond pass rates, with concrete instantiation on 49 tasks revealing systematic patterns standard metrics miss.

### [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](https://arxiv.org/abs/2605.12061)
**Source:** arxiv | **Authors:** Juntong Wang; Haoyue Zhao; guanghui Pan; Xiyuan Wang; Yanbo Wang; Qiyan Deng; Muhan Zhang
**Relevance:** 4/5 — Directly addresses long-term memory architecture for language agents with methodological innovations in graph-based memory construction and retrieval, core to agent capability.
**Depth:** 4/5 — Provides clear methodology (memory writer + GFM-based reader architecture with self-evolution), theoretical analysis, and concrete benchmarks across multiple domains (multi-hop QA, open-domain retrieval, LongMemEval, HaluMem).

### [Intermediate Artifacts as First-Class Citizens: A Data Model for Durable Intermediate Artifacts in Agentic Systems](https://arxiv.org/abs/2605.12087)
**Source:** arxiv | **Authors:** Josh Rosen; Seth Rosen
**Relevance:** 4/5 — Directly addresses systems-level architecture for LLM-based agents, focusing on how intermediate artifacts and state management enable multi-step reasoning, tool use, and human-agent collaboration—core agent capability.
**Depth:** 4/5 — Contributes a formal data model with explicit semantics (typed artifacts, versioning, lineage, update resolution) and distinguishes intermediate artifacts from related concepts, providing methodological substance for agent system design.

### [Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts](https://arxiv.org/abs/2605.12105)
**Source:** arxiv | **Authors:** Damir Safin; Dian Balta
**Relevance:** 4/5 — Directly addresses LLM-based agent deployment with focus on architectural design, oversight mechanisms, and the coupling between agency and autonomy—core concerns for agent capability and safety.
**Depth:** 4/5 — Provides explicit methodology through a two-dimensional design space with five operational levels, six concrete architectural tactics (checkpoints, escalation, delegation, tool provisioning, fencing, staging), and grounded examples demonstrating application under compliance constraints.

### [Rollout Cards: A Reproducibility Standard for Agent Research](https://arxiv.org/abs/2605.12131)
**Source:** arxiv | **Authors:** Charlie Masters; Ziyuan Liu; Stefano V. Albrecht
**Relevance:** 4/5 — Directly addresses reproducibility and evaluation methodology for LLM-based agent research, a foundational concern for frontier agent work.
**Depth:** 4/5 — Provides concrete methodology (rollout cards framework), systematic audit of 50 repos with 37 documented cases of reporting rule variance, and quantified results showing 20.9pp score changes from evaluation manipulation.

### [Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems](https://arxiv.org/abs/2605.12213)
**Source:** arxiv | **Authors:** Jiazhou Liang; Armin Toroghi; Yifan Simon Liu; Faeze Moradi Kalarde; Liam Gallagher; Scott Sanner
**Relevance:** 4/5 — Directly addresses LLM-based agent memory and reasoning capabilities, specifically how agents retrieve and reason over contextual information for coherent long-horizon behavior.
**Depth:** 4/5 — Presents a concrete methodology (backward chaining from goals, Natural Language Logic formalism) with explicit problem motivation (semantic similarity retrieval fails for multi-hop reasoning) and comprehensive experimental validation across two datasets against nine baselines.

### [No Action Without a NOD: A Heterogeneous Multi-Agent Architecture for Reliable Service Agents](https://arxiv.org/abs/2605.12240)
**Source:** arxiv | **Authors:** Zixu Yang; Hang Zheng; Nan Jiang; Zhiyang Tang; Situo Zhang; Xiaobao Wu; Lu Chen; Kai Yu
**Relevance:** 4/5 — Directly addresses LLM-based service agents with a novel architecture (NOD) that tackles reliability challenges in long-horizon tasks through explicit state management and oversight mechanisms.
**Depth:** 4/5 — Provides clear methodology (heterogeneous multi-agent design with Navigator-Operator-Director roles, externalized global state, selective oversight), concrete experimental results on τ²-Bench showing improvements in task success and critical action precision, and explicit problem articulation (policy violations, tool hallucinations, misalignment).

### [Executable Agentic Memory for GUI Agent](https://arxiv.org/abs/2605.12294)
**Source:** arxiv | **Authors:** Zerui Qin; Sheng Yue; Xingyuan Hua; Yongjian Fu; Ju Ren
**Relevance:** 4/5 — Directly addresses LLM-based agent memory, planning, and tool use through a structured knowledge graph approach for GUI agents with theoretical and empirical grounding.
**Depth:** 4/5 — Provides clear methodology (KG construction via state-aware DFS, value-guided MCTS search), theoretical analysis (bias-consistency, sample complexity bounds), and concrete empirical results (19.6% improvement on AndroidWorld, 6× token reduction).

### [$\delta$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357)
**Source:** arxiv | **Authors:** Jingdi Lei; Di Zhang; Junxian Li; Weida Wang; Kaixuan Fan; Xiang Liu; Qihan Liu; Xiaoteng Ma; Baian ...
**Relevance:** 4/5 — Directly addresses memory mechanisms for LLM-based agent systems, a core capability that enables long-horizon reasoning and context reuse in agent deployment.
**Depth:** 4/5 — Presents clear methodology (delta-rule learning, low-rank attention corrections, fixed-size state matrix) with concrete benchmark results on memory-heavy tasks (MemoryAgentBench, LoCoMo) and systematic comparisons to baselines.

### [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/abs/2605.12366)
**Source:** arxiv | **Authors:** Sam Martin; Fabien Roger
**Relevance:** 4/5 — Directly addresses a critical limitation in monitoring LLM-based coding agents—a core agent safety and deployment concern—by identifying and characterizing context-length-dependent capability degradation in frontier models.
**Depth:** 4/5 — Provides concrete quantitative results (2×–30× miss-rate increase), identifies a specific failure mechanism (context rot), demonstrates it across multiple frontier models, and proposes partial mitigations with empirical validation.

### [Formalize, Don't Optimize: The Heuristic Trap in LLM-Generated Combinatorial Solvers](https://arxiv.org/abs/2605.12421)
**Source:** arxiv | **Authors:** Haoyu Wang; Yuliang Song; Tao Li; Zhiwei Deng; Yaqing Wang; Deepak Ramachandran; Eldan Cohen; Dan Ro...
**Relevance:** 4/5 — Directly addresses LLM-based agent capability for tool use and solver synthesis, a frontier area of neuro-symbolic reasoning where agents interact with external verification systems.
**Depth:** 4/5 — Provides substantial methodology (three distinct representation paradigms evaluated systematically), concrete benchmark results (100 problems, 4,577 instances), and mechanistic insight into failure modes (the 'heuristic trap' traced through code audits).

### [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)
**Source:** arxiv | **Authors:** Anas Mahmoud; MohammadHossein Rezaei; Zihao Wang; Anisha Gunjal; Bing Liu; Yunzhong He
**Relevance:** 4/5 — Directly addresses reward hacking in RL-based post-training for LLM agents in reasoning domains (medical, science, math), a frontier capability problem affecting what agents can reliably do.
**Depth:** 4/5 — Provides rigorous methodology (cross-family verifier panel, verifier-free diagnostics like self-internalization gap) with concrete results across domains, systematically characterizing failure modes and their scaling with verifier strength.

### [Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures](https://arxiv.org/abs/2605.10991)
**Source:** arxiv | **Authors:** Linhai Zhang; Yulan He
**Relevance:** 4/5 — Directly addresses inference-time scaling and reward modeling for LLM personalization, core capabilities for agent decision-making and output selection.
**Depth:** 4/5 — Provides theoretical analysis (scaling law, oracle bounds), diagnostic framework identifying failure modes, and a principled probabilistic solution with experimental validation across multiple settings.

### [LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models](https://arxiv.org/abs/2605.11011)
**Source:** arxiv | **Authors:** Taekhyun Park; Yongjae Lee; Dohee Kim; Hyerim Bae
**Relevance:** 4/5 — Directly addresses test-time compute scaling and reasoning improvement in LLMs through looped latent refinement, a frontier capability relevant to agentic reasoning performance.
**Depth:** 4/5 — Presents detailed technical methodology (block decomposition, selective gating, deep supervision, confidence-based early exiting) with clear architectural mechanisms for converting pretrained models into looped architectures.

### [Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness](https://arxiv.org/abs/2605.11019)
**Source:** arxiv | **Authors:** Zizhao Chen; Yuying Li; Siting Lin; Lianxi Wang
**Relevance:** 4/5 — Directly addresses reasoning efficiency in LLM agents through chain-of-thought optimization, a frontier capability that materially affects what agents can accomplish under resource constraints.
**Depth:** 4/5 — Provides rigorous theoretical foundation (variational inference formalization, posterior guidance proof) and concrete methodology (dual-stream architecture, cross-view evaluation, variational distillation) with quantified results (8.73%-12.37% efficiency gains).

### [GRAFT-ATHENA: Self-Improving Agentic Teams for Autonomous Discovery and Evolutionary Numerical Algorithms](https://arxiv.org/abs/2605.11117)
**Source:** arxiv | **Authors:** Juan Diego Toscano; Zhaojie Chai; George Em Karniadakis
**Relevance:** 4/5 — Directly addresses LLM-based agentic systems for scientific discovery, focusing on agent architecture, planning, and autonomous capability expansion across domains.
**Depth:** 4/5 — Provides explicit methodology (GRAFT factorization as I-map, metric space embedding for transfer learning) and concrete results on physics-informed benchmarks and engineering problems, including autonomous discovery of new numerical methods.

### [Spurious Correlation Learning in Preference Optimization: Mechanisms, Consequences, and Mitigation via Tie Training](https://arxiv.org/abs/2605.11134)
**Source:** arxiv | **Authors:** Christian Moya; Alex Semendinger; Guang Lin; Elliott Thornley
**Relevance:** 4/5 — Directly addresses a critical training methodology (preference optimization) that affects LLM agent behavior and reliability, with implications for agent goal alignment and robustness.
**Depth:** 4/5 — Provides unified theoretical analysis of spurious learning mechanisms in preference optimization, proposes a provable mitigation strategy (tie training), and validates findings across log-linear models, neural networks, and LLMs.

### [Internalizing Curriculum Judgment for LLM Reinforcement Fine-Tuning](https://arxiv.org/abs/2605.11235)
**Source:** arxiv | **Authors:** Han Zheng; Yining Ma; Karthick Gunasekaran; Bharathan Balaji; Zheng Du; Shiv Vitaladevuni; Cathy Wu
**Relevance:** 4/5 — Directly addresses frontier capability in LLM agent training through novel reinforcement fine-tuning methodology with metacognitive curriculum learning, applicable to agent reasoning and function-calling tasks.
**Depth:** 4/5 — Provides clear methodology (within-prompt reward variance as informativeness metric, joint optimization, in-context learning for self-judgment) with extensive benchmarks showing 67% convergence acceleration across reasoning, code, and agentic domains.

### [Primal Generation, Dual Judgment: Self-Training from Test-Time Scaling](https://arxiv.org/abs/2605.11299)
**Source:** arxiv | **Authors:** Yizhu Jiao; Ruixiang Zhang; Richard Bai; Jiawei Han; Ronan Collobert; Yizhe Zhang
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities through test-time scaling and self-training methodology that improves reasoning and planning in code generation tasks.
**Depth:** 4/5 — Presents novel training methodology (DuST framework leveraging dual judgment space) with concrete results across multiple model scales and rigorous ablation (SFT vs RL comparison) demonstrating mechanism.

### [Epistemic Uncertainty for Test-Time Discovery](https://arxiv.org/abs/2605.11328)
**Source:** arxiv | **Authors:** Kainat Riaz; Muhammad Ahmed Mohsin; Ahsan Bilal; Muhammad Umer; Ayesha Mohsin; Aqib Riaz; Ali Subhan...
**Relevance:** 4/5 — Directly addresses LLM-based agent exploration and discovery through a novel uncertainty quantification mechanism that improves policy learning for scientific discovery tasks.
**Depth:** 4/5 — Presents clear methodology (ensemble of low-rank adapters with mutual information-based exploration bonus and nuclear norm regularization) and concrete empirical results across four benchmarks with ablation studies validating the approach.

### [fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum](https://arxiv.org/abs/2605.11403)
**Source:** arxiv | **Authors:** Mingxiong Lin; Zhangquan Gong; Maowen Tang; Qian Li; Chuangchuang Wang; Jian Ma; Sutian Huang; Kai T...
**Relevance:** 4/5 — Directly addresses frontier model capability training for LLM-based reasoning agents through improved RL optimization methods that enhance reasoning and planning performance.
**Depth:** 4/5 — Provides clear methodology (adaptive KL scaling and curriculum sampling mechanisms) with concrete benchmark results (13.34 improvement on AIME 2025) and explicit analysis of GRPO limitations.

### [Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](https://arxiv.org/abs/2605.12620)
**Source:** arxiv | **Authors:** Nishad Singhi; Christian Bialas; Snehal Jauhri; Vignesh Prasad; Georgia Chalvatzaki; Marcus Rohrbach...
**Relevance:** 4/5 — Directly addresses a core LLM-agent capability—robust action selection for embodied reasoning—using MLLMs with explicit verification mechanisms to improve out-of-distribution generalization.
**Depth:** 4/5 — Presents concrete methodology (ensemble sampling + generative verifier + curriculum-based data synthesis) with substantial empirical results (36% relative gains on challenging benchmarks) and explicit motivation grounded in MLLM limitations.

### [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](https://arxiv.org/abs/2605.12673)
**Source:** arxiv | **Authors:** Hao Wang; Hanchen Li; Qiuyang Mang; Alvin Cheung; Koushik Sen; Dawn Song
**Relevance:** 4/5 — Directly addresses evaluation and robustness of LLM-based agent benchmarks, a critical capability that affects agent deployment and model selection.
**Depth:** 4/5 — Provides systematic methodology (taxonomy of eight flaw patterns, automated red-teaming system), concrete results across 10 benchmarks with specific numbers (219 distinct flaws, reduction from ~100% to <10% hackable tasks), and identifies limitations of current evaluation pipelines.

### [CHAL: Council of Hierarchical Agentic Language](https://arxiv.org/abs/2605.12718)
**Source:** arxiv | **Authors:** Tommaso Giovannelli; Griffin D. Kent
**Relevance:** 4/5 — Directly addresses multi-agent LLM reasoning and debate as a core agent capability, with explicit focus on belief optimization and reasoning mechanisms that affect what agents can do.
**Depth:** 4/5 — Provides substantial methodology (graph-structured belief schemas, Bayesian-inspired architecture, gradient-informed dynamics, configurable meta-cognitive value systems) and ablation experiments demonstrating systematic effects on agent behavior and reasoning.

### [Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents](https://arxiv.org/abs/2605.12894)
**Source:** arxiv | **Authors:** Harshita Chopra; Kshitish Ghate; Aylin Caliskan; Tadayoshi Kohno; Chirag Shah; Natasha Jaques
**Relevance:** 4/5 — Directly addresses evaluation and training robustness of LLM-based agents through realistic user simulation, which is a core frontier challenge in agent deployment.
**Depth:** 4/5 — Provides concrete methodology (evolutionary program search for persona generation), multi-objective fitness design, and substantial empirical results (33-62% fitness gains, 80.4% human-likeness rating, +17% task success improvement).

### [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction](https://arxiv.org/abs/2605.12922)
**Source:** arxiv | **Authors:** Vardhan Dongre; Joseph Hsieh; Viet Dac Lai; Seunghyun Yoon; Trung Bui; Dilek Hakkani-T\"ur
**Relevance:** 4/5 — Directly addresses a critical failure mode in LLM-based agents—loss of instruction adherence in multi-turn interactions—through mechanistic analysis of attention and residual representations.
**Depth:** 4/5 — Provides rigorous methodology (Goal Accessibility Ratio, sliding-window ablations, residual-stream probes, linear probes) with quantitative results across multiple architectures and a causal intervention demonstrating predictable failure thresholds.

### [Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation](https://arxiv.org/abs/2605.12975)
**Source:** arxiv | **Authors:** Jiashuo Sun; Jimeng Shi; Yixuan Xie; Saizhuo Wang; Jash Rajesh Parekh; Pengcheng Jiang; Zhiyi Shi; J...
**Relevance:** 4/5 — Directly addresses a core agent capability—multi-hop reasoning and tool use in RAG systems—by reformulating reasoning as executable programs with structured intermediate states and deterministic feedback.
**Depth:** 4/5 — Provides clear methodology (program synthesis over retrieval/QA tools, compiler-grounded repair, execution-driven retrieval) and concrete results across five benchmarks, with insight into why code-based reasoning outperforms free-form language.

### [GRACE: Gradient-aligned Reasoning Data Curation for Efficient Post-training](https://arxiv.org/abs/2605.13130)
**Source:** arxiv | **Authors:** Junjie Li; Ziao Wang; NingXuan Ma; Jianghong Ma; Xiaofeng Zhang
**Relevance:** 4/5 — Directly addresses reasoning data curation for LLM post-training, a frontier capability-building method that materially affects model reasoning abilities needed for agent tasks.
**Depth:** 4/5 — Presents clear methodology (gradient-aligned step-level scoring with representation-level proxy) and concrete quantitative results (108.8% performance at 20% data, cross-model transfer validation).

### [Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning](https://arxiv.org/abs/2605.13213)
**Source:** arxiv | **Authors:** Hao Zhou; Tiru Wu; Yan Jiang; Wanqi Zhou; Junxing Hu; Ai Han
**Relevance:** 4/5 — Directly addresses vulnerabilities and robustness of LLM-based multi-agent systems using established reasoning paradigms (ReAct, Plan-and-Solve, Reflexion), which is central to understanding agent capabilities and limitations.
**Depth:** 4/5 — Presents a systematic hierarchical framework with three attack layers (perception, communication, reasoning), concrete ASR results (up to 78.3%), and evaluation across multiple reasoning paradigms with specific insights about attack effectiveness.

### [Respecting Self-Uncertainty in On-Policy Self-Distillation for Efficient LLM Reasoning](https://arxiv.org/abs/2605.13255)
**Source:** arxiv | **Authors:** Junlong Ke; Zichen Wen; Weijia Li; Conghui He; Linfeng Zhang
**Relevance:** 4/5 — Directly addresses training methods for LLM reasoning agents through self-distillation, a frontier capability that improves how models learn to plan and reason.
**Depth:** 4/5 — Proposes concrete methodology (entropy-guided weighting, causal-lookahead variant) with explicit mechanism rationale and experimental results showing accuracy-length frontier improvements on reasoning benchmarks.

### [Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling](https://arxiv.org/abs/2605.13301)
**Source:** arxiv | **Authors:** Yafu Li; Runzhe Zhan; Haoran Zhang; Shunkai Zhang; Yizhuo Li; Zhilin Wang; Jiacheng Chen; Futing Wan...
**Relevance:** 4/5 — Directly addresses frontier model capabilities for reasoning and long-horizon problem-solving that materially enable agent-like behaviors (planning, self-checking, verification), with methodology and concrete benchmark results on olympiad competitions.
**Depth:** 4/5 — Presents explicit methodology (reverse-perplexity curriculum, two-stage RL with verifiable/proof-level rewards, test-time scaling) with concrete results (gold-medal performance on IMO/IPhO, 100K+ token trajectories) and demonstrates generalization across scientific domains.

### [RS-Claw: Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents](https://arxiv.org/abs/2605.13391)
**Source:** arxiv | **Authors:** Liangtian Liu; Zeyuan Wang; Ziyu Li; Kai Ouyang; Zichao Tang; Chengfu Liu; Haifeng Li; Hanwen Yu; We...
**Relevance:** 4/5 — Directly addresses LLM-based agent tool use and reasoning in a frontier domain (remote sensing), with focus on architectural innovations for managing tool selection under context constraints.
**Depth:** 4/5 — Provides clear methodology (hierarchical skill trees with progressive tool loading), concrete benchmark results (86% token compression, Earth-Bench evaluation), and identifies specific limitations of prior approaches (Flat vs. RAG trade-offs).

### [Cognifold: Always-On Proactive Memory via Cognitive Folding](https://arxiv.org/abs/2605.13438)
**Source:** arxiv | **Authors:** Suli Wang; Yiqun Duan; Yu Deng; Rundong Zhao; Dai Shi; Xinliang Zhou
**Relevance:** 4/5 — Directly addresses agent memory architecture—a core capability for LLM-based agents—with explicit methodology grounded in cognitive science theory (Complementary Learning Systems).
**Depth:** 4/5 — Provides novel three-layer memory model with graph-topology self-organization mechanisms, cognitive emergence benchmarking (CogEval-Bench), and validation across seven benchmarks spanning multiple cognitive domains.

### [MMSkills: Towards Multimodal Skills for General Visual Agents](https://arxiv.org/abs/2605.13527)
**Source:** arxiv | **Authors:** Kangning Zhang; Shuai Shao; Qingyao Li; Jianghao Lin; Lingyue Fu; Shijian Wang; Wenxiang Jiao; Yuan ...
**Relevance:** 4/5 — Directly addresses skill reuse and runtime decision-making for visual LLM-based agents, a core agent capability.
**Depth:** 4/5 — Provides concrete methodology for multimodal skill representation, generation pipeline, and inference architecture with systematic evaluation across benchmarks.

### [Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging](https://arxiv.org/abs/2605.13534)
**Source:** arxiv | **Authors:** Jiabei Liu; Wenyu Mao; Junfei Tan; Chunxu Shen; Lingling Yi; Jiancan Wu; Xiang Wang
**Relevance:** 4/5 — Directly addresses LLM-based agent reasoning and planning through retrieval-augmented multi-step reasoning with explicit methodology for query generation and information consolidation.
**Depth:** 4/5 — Presents concrete methodology (multi-query retrieval, explicit merging process, RL framework with multi-process rewards) and demonstrates results across seven benchmarks with signal-to-noise ratio improvements.

### [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://arxiv.org/abs/2605.13542)
**Source:** arxiv | **Authors:** Chengzhi Shen (Cherise); Weixiang Shen (Cherise); Tobias Susetzky (Cherise); Chen (Cherise); Chen (C...
**Relevance:** 4/5 — Directly evaluates LLM agents' long-context reasoning and sequential decision-making under realistic conditions, with structured-memory agent variants designed to improve agent reasoning.
**Depth:** 4/5 — Provides concrete methodology (hindsight annotation, 30-min window partitioning, Oracle labeler validation), detailed benchmark results exposing failure modes (recall-safety tradeoff, anchoring bias), and introduces ICU-Evo agent architecture with structured memory to address limitations.

### [ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles](https://arxiv.org/abs/2605.13725)
**Source:** arxiv | **Authors:** Yitian Yang; Yiqun Duan; Linghan Huang; Yiqi Zhu; Francesco Bailo; Chunmeizi Su; Huaming Chen
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent systems with structured methodology for reasoning, memory, and belief dynamics that enables more capable agent behavior.
**Depth:** 4/5 — Presents concrete architectural components (anchoring-based belief updates, hierarchical memory, dynamic profiles), systematic evaluation across multiple metrics, and grounding in cognitive science theory with demonstrated improvements in behavioral realism.

### [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821)
**Source:** arxiv | **Authors:** Jiayi Zhang; Yongfeng Gu; Jianhao Ruan; Maojia Song; Yiran Peng; Zhiguang Han; Jinyu Xiang; Zhitao W...
**Relevance:** 4/5 — Directly addresses LLM-based agent evolution and meta-control mechanisms that improve agent performance through procedural editing and feedback integration.
**Depth:** 4/5 — Provides explicit methodology (meta-editing framework with process-level state management), concrete benchmarks with quantified improvements (26% relative gain), and identifies limitations of prior fixed vs. flexible approaches.

### [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652)
**Source:** arxiv | **Authors:** Weichen Yu; Xiaomin Li; Yizhou Zhao; Xiaoze Liu; Ruowang Zhang; Haixin Wang; Yinyi Luo; Chen Henry W...
**Relevance:** 4/5 — Directly addresses post-training methods for LLM reasoning and decision-making in agents, improving on-policy learning from multi-step trajectories across agent-relevant benchmarks.
**Depth:** 4/5 — Presents clear methodology (peer-conditioned distillation with success-failure contexts), concrete results across multiple domains, and mechanistic analysis showing why mixed contexts improve alignment with verifier rewards.

### [ODRPO: Ordinal Decompositions of Discrete Rewards for Robust Policy Optimization](https://arxiv.org/abs/2605.12667)
**Source:** arxiv | **Authors:** Nirmal Patel; Fei Wang; Inderjit Dhillon
**Relevance:** 4/5 — Directly addresses LLM alignment via RLAIF, a frontier method for enabling agent-like behaviors through reinforcement learning with noisy evaluation signals.
**Depth:** 4/5 — Provides clear methodology (ordinal decomposition mechanism), concrete empirical results (14.8% and 7.5% improvements on benchmarks), and identifies a specific limitation (stochasticity of auto-raters) that prior work fails to handle robustly.

### [Learning with Rare Success but Rich Feedback via Reflection-Enhanced Self-Distillation](https://arxiv.org/abs/2605.12741)
**Source:** arxiv | **Authors:** Yuwei Zhang; Sha Li; Changlong Yu; Qin Lu; Shuowei Jin; Chengyu Dong; Haoran Liu; Ilgee Hong; Xinton...
**Relevance:** 4/5 — Directly addresses post-training improvement of LLMs through environmental interaction and self-distillation, a core capability mechanism for continuous agent learning.
**Depth:** 4/5 — Presents concrete methodology (reflection-based error diagnosis, persistent playbook curation) with empirical benchmarks showing 8× sample efficiency gains over GRPO baseline.

### [WriteSAE: Sparse Autoencoders for Recurrent State](https://arxiv.org/abs/2605.12770)
**Source:** arxiv | **Authors:** Jack Young
**Relevance:** 4/5 — Sparse autoencoders for mechanistic interpretability of LLM internals directly enable better understanding and control of model capabilities, supporting agent reliability and safety.
**Depth:** 4/5 — Introduces novel methodology (WriteSAE) for decomposing recurrent model state writes with closed-form analysis, demonstrates concrete quantitative results (92.4% substitution success, R²=0.98 prediction), and advances interpretability at a frontier model architecture boundary.

### [ToolMol: Evolutionary Agentic Framework for Multi-objective Drug Discovery](https://arxiv.org/abs/2605.12784)
**Source:** arxiv | **Authors:** Andrew Y. Zhou; Sharvaree Vadgama; Sumanth Varambally; Peter Eckmann; Michael K. Gilson; Rose Yu
**Relevance:** 4/5 — Directly addresses LLM-based agents with tool use for molecular generation, demonstrating agentic reasoning and tool-calling mechanisms that are central to agent capability.
**Depth:** 4/5 — Provides clear methodology (genetic algorithm + agentic LLM operator with RDKit tool integration), concrete benchmark results (10%+ binding affinity improvement, 35%+ ABFE gains), and analysis of how tool-calling enables faithful execution of planned modifications.

### [Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion](https://arxiv.org/abs/2605.12825)
**Source:** arxiv | **Authors:** Chien Van Nguyen; Chaitra Hegde; Van Cuong Pham; Ryan A. Rossi; Franck Dernoncourt; Thien Huu Nguyen
**Relevance:** 4/5 — Orthrus directly addresses LLM inference efficiency through a novel architecture combining autoregressive and diffusion token generation, materially affecting agent deployment capabilities by enabling faster inference.
**Depth:** 4/5 — The paper presents clear methodology (dual-view framework with consensus mechanism), concrete results (7.8x speedup with O(1) memory overhead), and rigorous convergence guarantees that distinguish it from prior diffusion language model work.

### [Reinforced Collaboration in Multi-Agent Flow Networks](https://arxiv.org/abs/2605.12943)
**Source:** arxiv | **Authors:** Zheng Wang; Yuang Liu; Yangkai Ding
**Relevance:** 4/5 — Directly addresses multi-agent LLM systems with focus on workflow optimization, agent collaboration mechanisms, and error propagation—core agent architecture concerns.
**Depth:** 4/5 — Presents MANGO framework with explicit methodology (reinforcement learning + textual gradients + flow networks + skipping mechanism) and concrete benchmark results (12.8% improvement, 47.4% efficiency gain across seven tasks).

### [Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective](https://arxiv.org/abs/2605.12969)
**Source:** arxiv | **Authors:** Feng Zhang; Xinhong Ma; Ziqiang Dong; Xi Leng; Jianfei Zhao; Xin Sun; Yang Yang; Guanjun Jiang
**Relevance:** 4/5 — Directly addresses frontier training methods (RLVR/GRPO) for improving LLM reasoning capabilities with clear methodological contributions to policy optimization.
**Depth:** 4/5 — Provides formal analysis of GRPO limitations, proposes ConSPO with concrete mechanisms (contrastive objectives, curriculum scheduling), and includes extensive empirical evaluation across model scales and benchmarks.

### [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy](https://arxiv.org/abs/2605.12991)
**Source:** arxiv | **Authors:** Adarsh Kumarappan; Ananya Mujoo
**Relevance:** 4/5 — Directly addresses a frontier safety and capability issue in LLM-based multi-agent systems, with mechanistic insights into how agents behave under peer pressure in reasoning tasks.
**Depth:** 4/5 — Provides rigorous methodology (activation patching, controlled experiments across model families) and concrete results (yield metrics, localized corruption windows, quantified intervention effects) that mechanistically explain and mitigate agent failure modes.

### [Teacher-Guided Policy Optimization for LLM Distillation](https://arxiv.org/abs/2605.13230)
**Source:** arxiv | **Authors:** Xinyu Liu; Kechen Jiao; Chunyang Xiao; Runsong Zhao; Junhao Ruan; Bei Li; Jiahao Liu; Qifan Wang; Xi...
**Relevance:** 4/5 — LLM distillation via reinforcement learning is a frontier capability training method that directly affects what student models can do, enabling more capable and efficient agents.
**Depth:** 4/5 — The paper provides clear methodology (TGPO algorithm with dense directional guidance), identifies concrete limitations of prior work (RKL failure under distribution divergence), and demonstrates empirical results on reasoning benchmarks.

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

### [CVEvolve: Autonomous Algorithm Discovery for Unstructured Scientific Data Processing](https://arxiv.org/abs/2605.11359)
**Source:** arxiv | **Authors:** Ming Du; Xiangyu Yin; Yanqi Luo; Dishant Beniwal; Songyuan Tang; Hemant Sharma; Mathew J. Cherukara
**Relevance:** 4/5 — CVEvolve directly demonstrates LLM-based agent capabilities for autonomous algorithm discovery, including reasoning, tool use, planning, and evaluation—core agent mechanisms that impact what frontier models can accomplish.
**Depth:** 3/5 — The paper provides concrete methodology (multi-round search strategy, lineage-aware sampling, holdout testing) and empirical results on three scientific tasks, but lacks fine-grained analysis of why the agentic approach succeeds or frontier model capability requirements.

### [LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents](https://arxiv.org/abs/2605.11376)
**Source:** arxiv | **Authors:** Giuliano Lorenzoni (University of Waterloo); Paulo Alencar (University of Waterloo); Donald Cowan (U...
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent coordination and communication, a core frontier capability for enabling scalable agent systems.
**Depth:** 3/5 — Provides explicit architecture (federated gateways, routing, policy enforcement), typed protocols for negotiation, and empirical evaluation of multi-agent interactions at scale with clear policy-performance trade-offs.

### [Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics](https://arxiv.org/abs/2605.12178)
**Source:** arxiv | **Authors:** Jishnu Sethumadhavan Nair; Patrice Bechard; Rishabh Maheshwary; Surajit Dasgupta; Sravan Ramachandra...
**Relevance:** 4/5 — Directly addresses LLM-based agent design and reasoning in enterprise contexts, with focus on how agents should incorporate runtime discovery rather than relying solely on learned world models—a methodological insight for agent architecture.
**Depth:** 3/5 — Provides concrete methodology (discovery agents that read system configuration at runtime) and empirical evaluation on a custom benchmark (CascadeBench) demonstrating robustness under distribution shift, though the contribution is domain-specific to enterprise systems rather than advancing frontier capabilities.

### [Leveraging RAG for Training-Free Alignment of LLMs](https://arxiv.org/abs/2605.11217)
**Source:** arxiv | **Authors:** John T. Halloran
**Relevance:** 4/5 — Directly addresses LLM alignment and safety against agentic attacks, a frontier capability concern that materially affects what agents can safely do.
**Depth:** 3/5 — Presents a concrete methodology (RAG-Pref) with specific empirical results (3.7x improvement in refusal across five LLMs) and clear comparison against baselines, though the core mechanism is relatively straightforward application of existing techniques.

### [Learning Transferable Latent User Preferences for Human-Aligned Decision Making](https://arxiv.org/abs/2605.12682)
**Source:** arxiv | **Authors:** Alina Hyk; Sandhya Saisubramanian
**Relevance:** 4/5 — Directly addresses LLM-based agent alignment and preference learning, a core capability needed for human-aligned autonomous decision-making in agent systems.
**Depth:** 3/5 — Presents a concrete methodology (CLIPR framework) for learning transferable preference rules from minimal interactions with evaluation on multiple datasets and user studies, though the core mechanism is preference extraction rather than novel agent architecture.

### [Position: Agentic AI System Is a Foreseeable Pathway to AGI](https://arxiv.org/abs/2605.12966)
**Source:** arxiv | **Authors:** Junwei Liao; Shuai Li; Muning Wen; Jun Wang; Weinan Zhang
**Relevance:** 4/5 — Directly addresses agentic AI as a paradigm for complex task mastery and contrasts it against monolithic scaling, which is central to understanding frontier agent capabilities and pathways to AGI.
**Depth:** 3/5 — Provides theoretical analysis comparing optimization constraints, discusses DAG topologies and routing mechanisms, and connects to Mixture-of-Experts, though the paper appears primarily position/framework-oriented rather than empirical validation-heavy.

### [What properties of reasoning supervision are associated with improved downstream model quality?](https://arxiv.org/abs/2605.13290)
**Source:** arxiv | **Authors:** Miko{\l}aj Langner; Dzmitry Pihulski; Jan Eliasz; Micha{\l} Rajkowski; Przemys{\l}aw Kazienko; Macie...
**Relevance:** 4/5 — Directly addresses training methods for reasoning models, a frontier capability that materially affects what LLM agents can do by improving their planning and problem-solving abilities.
**Depth:** 3/5 — Provides concrete methodology (intrinsic data metrics framework) and empirical results (scale-dependent predictor correlations), but focuses narrowly on data validation rather than architectural innovation or breakthrough reasoning capabilities.

### [How to Interpret Agent Behavior](https://arxiv.org/abs/2605.13625)
**Source:** arxiv | **Authors:** Jie Gao; Kaiser Sun; Jen-tse Huang; Katherine Van Koevering; Sijie Ji; Heyuan Huang; Weiyan Shi; Zhu...
**Relevance:** 4/5 — Directly addresses agent behavior interpretation and oversight, which is critical infrastructure for understanding and improving LLM-based agents at runtime.
**Depth:** 3/5 — Provides a structured taxonomy methodology (3-level hierarchy with 176 categories) and an automated analysis pipeline with concrete experimental results comparing agent behavioral profiles, though the contribution is primarily organizational/analytical rather than revealing new agent capabilities or mechanisms.


## Worth knowing (71 items)

_On-criterion but lower depth, or peripheral relevance._

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

### [Unlocking LLM Creativity in Science through Analogical Reasoning](https://arxiv.org/abs/2605.11258)
**Source:** arxiv | **Authors:** Andrew Shen; Shaul Druckmann; James Zou
**Relevance:** 3/5 — The work addresses LLM reasoning and solution generation for autonomous systems, which is relevant to agent capabilities, but focuses narrowly on analogical reasoning for scientific discovery rather than agent deployment, planning, or tool use.
**Depth:** 4/5 — The paper provides clear methodology (analogical reasoning approach with cross-domain structural matching), concrete quantitative results (90-173% diversity improvement, state-of-the-art on biomedical benchmarks), and identifies a specific limitation (mode collapse) that motivates the contribution.

### [A Mechanistic Investigation of Supervised Fine Tuning](https://arxiv.org/abs/2605.11426)
**Source:** arxiv | **Authors:** Ruhaan Chopra
**Relevance:** 3/5 — Mechanistic understanding of SFT is foundational to agent capabilities, but this work focuses on representational geometry rather than agent-specific abilities like reasoning, planning, or tool use.
**Depth:** 4/5 — Introduces a novel diagnostic pipeline using pretrained SAEs to systematically analyze how SFT alters semantic features and safety alignment, with publicly available code and reproducible analysis.

### [Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion](https://arxiv.org/abs/2605.11679)
**Source:** arxiv | **Authors:** ShiYing Huang; Liang Lin; Yuer Li; Kaiwen Luo; Zhenhong Zhou; An Zhang; Junhao Dong; Kun Wang; Zhiga...
**Relevance:** 3/5 — Directly addresses frontier model alignment trade-offs that affect agent deployment and capability, but focuses on preference balancing rather than agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides clear methodology (multi-dimensional reward expansion via prompt rewriting), concrete quantitative results (5-12.4% improvements), and identifies root cause (prompts restricting achievable rewards).

### [To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands](https://arxiv.org/abs/2605.12120)
**Source:** arxiv | **Authors:** Fangyi Yu; Nabeel Seedat; Jonathan Richard Schwarz; Andrew M. Bean
**Relevance:** 3/5 — Addresses alignment and decision-making in deployed LLM systems across professional domains, which relates to agent behavior in high-stakes settings, but focuses on alignment hierarchies rather than agent architecture, reasoning, or tool use.
**Depth:** 4/5 — Provides concrete methodology (7,136 scenarios across legal/medical domains), systematic evaluation of 10 frontier models, mechanistic analysis (knowledge omission failures, reasoning trace suppression), and identifies failure modes with reproducible evidence.

### [Enabling Performant and Flexible Model-Internal Observability for LLM Inference](https://arxiv.org/abs/2605.11093)
**Source:** arxiv | **Authors:** Nengneng Yu; Sixian Xiong; Yibo Zhao; Wei Wang; Zaoxing Liu
**Relevance:** 3/5 — Internal model observability is useful infrastructure for agent development and debugging, but this work is primarily a systems/inference optimization contribution rather than directly addressing agent reasoning, planning, or capabilities.
**Depth:** 4/5 — The paper presents solid systems methodology (Ring² memory abstraction, asynchronous observability substrate, policy-controlled backend) with concrete latency and overhead measurements (0.4%–6.8% offline, 6% online, 2x–15x improvement over baselines).

### [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/abs/2605.11196)
**Source:** arxiv | **Authors:** Vishal Pandey; Gopal Singh
**Relevance:** 3/5 — Long-context transformer efficiency is a frontier capability that enables agents to maintain larger working memories and process longer reasoning traces, but this work is architecture-focused rather than agent-specific.
**Depth:** 4/5 — The paper provides rigorous theoretical analysis (spectral norm proofs, state norm bounds), concrete empirical results (109× reduction in memory state norm, 62% accuracy at capacity boundary), and a production-grade implementation with measured latency improvements.

### [Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks](https://arxiv.org/abs/2605.11209)
**Source:** arxiv | **Authors:** Eungyeup Kim; Chenchen Gu; Vashisth Tiwari; J. Zico Kolter
**Relevance:** 3/5 — Evaluation methodology for LLM reliability is relevant to agent deployment, but the work focuses narrowly on failure rate estimation rather than agent-specific capabilities like reasoning, planning, or tool use.
**Depth:** 4/5 — The paper presents a concrete methodology (cross-entropy method for failure-prone input sampling) with substantial empirical results (156x inference reduction) and reveals meaningful distinctions between models on a previously underexplored evaluation axis.

### [Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs](https://arxiv.org/abs/2605.13737)
**Source:** arxiv | **Authors:** Trung Nguyen Quang; Yiming Gao; Fanyi Pu; Kaichen Zhang; Shuo Sun; Ziwei Liu
**Relevance:** 3/5 — The work studies grounding failures in omnimodal LLMs used as agents, but focuses narrowly on perception-action gaps rather than agent reasoning, planning, or tool use—making it on-topic but not central to frontier LLM-based agents.
**Depth:** 4/5 — The paper provides a rigorous methodology (IMAVB benchmark with controlled 2x2 design), concrete findings (representation-action gap documented across 9 models), mechanistic insight (hidden states encode mismatches despite output failures), and a diagnostic intervention (PGLA), meeting the threshold for substantial methodology and results.

### [Early Data Exposure Improves Robustness to Subsequent Fine-Tuning](https://arxiv.org/abs/2605.12705)
**Source:** arxiv | **Authors:** Lawrence Feng; Gaurav R. Ghosal; Jacob Mitchell Springer; Ziqian Zhong; Aditi Raghunathan
**Relevance:** 3/5 — Addresses robustness of model capabilities during fine-tuning, which affects agent deployment and capability retention, but is not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides systematic methodology (three-stage pipeline, controlled experiments across scales), concrete empirical results (135M and 1B models, quantified retention metrics), and theoretical insight into the mechanisms of specialization vs. robustness.

### [Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer](https://arxiv.org/abs/2605.12798)
**Source:** arxiv | **Authors:** Baris Askin; Muhammed Ustaomeroglu; Anupam Nayak; Gauri Joshi; Guannan Qu; Carlee Joe-Wong
**Relevance:** 3/5 — Addresses safety and alignment of LLMs which affects what agents can reliably do, but focuses on fine-tuning misalignment rather than agent capabilities, reasoning, or planning directly.
**Depth:** 4/5 — Provides substantive methodology analyzing data-mediated transfer through systematic experiments across EM and subliminal learning, with clear mechanistic insights about task structure, pretraining composition, and training channels.

### [Descriptive Collision in Sparse Autoencoder Auto-Interpretability: When One Explanation Describes Many Features](https://arxiv.org/abs/2605.12874)
**Source:** arxiv | **Authors:** Jordan F. McCann
**Relevance:** 3/5 — Sparse autoencoders are interpretability tools for understanding LLM internals, which is adjacent to but not directly about LLM-based agent capabilities; the work analyzes a failure mode in automated interpretability rather than improving agent reasoning or tool use.
**Depth:** 4/5 — The paper identifies a novel structural failure mode (descriptive collision) with formal information-theoretic analysis, proposes corrective metrics, and validates findings on a large human-annotated dataset, demonstrating rigorous methodology and concrete measurement.

### [From Instance Selection to Fixed-Pool Data Recipe Search for Supervised Fine-Tuning](https://arxiv.org/abs/2605.12944)
**Source:** arxiv | **Authors:** Haodong Wu; Jiahao Zhang; Lijie Hu; Yongqi Zhang
**Relevance:** 3/5 — SFT data curation directly impacts model capability for downstream agent tasks, but the work focuses on data selection methodology rather than agent-specific capabilities or architectures.
**Depth:** 4/5 — Solid methodology with multi-layer optimization (warmup probes, GP-assisted ranking, stagnation reseeding), concrete experimental validation across three models, and ablation studies demonstrating that recipe structure matters.

### [Controlling Logical Collapse in LLMs via Algebraic Ontology Projection over F2](https://arxiv.org/abs/2605.12968)
**Source:** arxiv | **Authors:** Hisashi Miyashita; Mgnite Inc
**Relevance:** 3/5 — Investigates internal logical structure and reasoning mechanisms of LLMs, which is foundational to understanding agent capabilities, but lacks explicit agent application or deployment methodology.
**Depth:** 4/5 — Presents novel algebraic methodology (AOP, SC metrics), concrete zero-shot accuracy results (93.33%, 86.67%), and identifies a systematic failure mode (Late-layer Collapse) with clear mechanistic explanation and layer-dependent analysis.

### [F-GRPO: Factorized Group-Relative Policy Optimization for Unified Candidate Generation and Ranking](https://arxiv.org/abs/2605.12995)
**Source:** arxiv | **Authors:** Rohan Surana; Gagan Mundada; Junda Wu; Xintong Li; Yizhu Jiao; Bowen Jin; Sizhe Zhou; Tong Yu; Ritwi...
**Relevance:** 3/5 — Addresses LLM optimization for structured decision-making (candidate generation and ranking), which is relevant to agent capabilities, but focuses on retrieval/recommendation rather than core agent reasoning, planning, or tool use.
**Depth:** 4/5 — Presents a concrete methodology (F-GRPO with factorized credit assignment) for unified end-to-end optimization, includes systematic evaluation across multiple benchmarks, and explicitly identifies and solves a credit assignment problem in sequence-level feedback.

### [EMO: Frustratingly Easy Progressive Training of Extendable MoE](https://arxiv.org/abs/2605.13247)
**Source:** arxiv | **Authors:** Linghao Jin; Chufan Shi; Huijuan Wang; Nuan Wen; Zhengzhong Liu; Eric Xing; Xuezhe Ma
**Relevance:** 3/5 — MoE scaling is a frontier training method that affects model capacity and capability emergence, but this work focuses on training efficiency rather than agent-specific capabilities or reasoning mechanisms.
**Depth:** 4/5 — The paper provides explicit methodology (progressive expert allocation with compute-optimal budgets), scaling law analysis, and large-scale empirical validation demonstrating wall-clock efficiency gains.

### [Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory](https://arxiv.org/abs/2605.13370)
**Source:** arxiv | **Authors:** Sungwoo Goo; Hwi-yeol Yun; Sangkeun Jung
**Relevance:** 3/5 — Addresses frontier model capability (explicit memory architecture for language modeling) that could improve context handling and reasoning in LLM-based systems, but is not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides mechanistic proof-of-concept with theoretical grounding (Unitary Phasor Dynamics to solve gradient instability), concrete empirical results (85-slot memory tree, 100% retrieval on Copy-Paste task, competitive scaling), and clear ablation analysis of why prior explicit memory failed.

### [OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention](https://arxiv.org/abs/2605.13473)
**Source:** arxiv | **Authors:** Chenyu Zhou; Hongpei Li; Yuerou Liu; Jianghao Lin; Dongdong Ge; Yinyu Ye
**Relevance:** 3/5 — Linear attention and state-space models are frontier architecture components that affect LLM capabilities and efficiency, but this work focuses on in-context recall optimization rather than agent-specific reasoning or planning.
**Depth:** 4/5 — The paper provides rigorous methodology (online preconditioning with theoretical convergence proofs and hardware-efficient implementation), concrete scaling results (32-39% improvements), and addresses clear limitations of prior Delta Rule work through algorithmic innovation.

### [Discovery of Hidden Miscalibration Regimes](https://arxiv.org/abs/2605.13484)
**Source:** arxiv | **Authors:** Katarzyna Kobalczyk; Mihaela van der Schaar
**Relevance:** 3/5 — Calibration and confidence estimation are important for reliable LLM-based agents, but this work focuses on model introspection rather than agent architectures, reasoning, planning, or frontier capability emergence.
**Depth:** 4/5 — The paper presents solid methodology (calibration-aware representation learning with kernel smoothing), comprehensive evaluation across twelve LLMs and four benchmarks, and actionable results (local confidence correction), though the contribution is primarily in diagnostics rather than enabling new agent capabilities.

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

### [Template-as-Ontology: Configurable Synthetic Data Infrastructure for Cross-Domain Manufacturing AI Validation](https://arxiv.org/abs/2605.11259)
**Source:** arxiv | **Authors:** Grama Chethan
**Relevance:** 3/5 — Directly addresses validation infrastructure for LLM-based agents in manufacturing, with demonstrated hallucination mitigation through ontology constraints, but is primarily a data/systems contribution rather than advancing core agent capabilities or frontier model development.
**Depth:** 3/5 — Provides solid methodology (Template-as-Ontology principle, five-layer pipeline, formal schema definition) and concrete results (66 entity types, 6 templates, 0% vs 43% hallucination rates with statistical validation), but the core contribution is engineering infrastructure rather than fundamental insights into agent reasoning, planning, or model capabilities.

### [LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?](https://arxiv.org/abs/2605.11301)
**Source:** arxiv | **Authors:** Xueqi Cheng; Yushun Dong
**Relevance:** 3/5 — MLLM routing is tangentially relevant to agent systems (model selection for heterogeneous capabilities is a tactical problem in multi-model agent deployment), but this work focuses on inference-time routing rather than agent reasoning, planning, or tool use.
**Depth:** 3/5 — The paper presents solid methodology (counterfactual utility prediction with latent communication and capsule correction) and empirical validation on benchmarks, but the contribution is incremental optimization of model selection rather than addressing frontier agent capabilities or reasoning mechanisms.

### [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://arxiv.org/abs/2605.11330)
**Source:** arxiv | **Authors:** Wenbo Chen; Veena Padmanabhan; Tootiya Giyahchi; Elaine Wong; Leman Akoglu
**Relevance:** 3/5 — Hallucination detection is relevant to agent reliability and trust, but this work is primarily a benchmark/evaluation contribution for RAG systems rather than advancing agent reasoning, planning, or capabilities.
**Depth:** 3/5 — The paper provides solid methodology (desiderata framework, rigorous annotation process, noise schemes) and concrete results (benchmark comparison, detector evaluation), but lacks architectural innovation or insights that materially enable new agent capabilities.

### [CPEMH: An Agentic Framework for Prompt-Driven Behavior Evaluation and Assurance in Foundation-Model Systems for Mental Health Screening](https://arxiv.org/abs/2605.11341)
**Source:** arxiv | **Authors:** Giuliano Lorenzoni (University of Waterloo); Ivens Portugal (University of Waterloo); Paulo Alencar ...
**Relevance:** 3/5 — The paper addresses LLM-based agent evaluation and orchestration for a specific application domain (mental health screening), but the core contribution is primarily application-focused rather than advancing frontier agent capabilities or model training methods.
**Depth:** 3/5 — The work provides concrete methodology for multi-agent orchestration, modular architecture design, and behavioral assurance with a case study demonstrating the framework, but lacks novel insights into agent reasoning, planning, or mechanisms that would be central to frontier agent research.

### [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](https://arxiv.org/abs/2605.11712)
**Source:** arxiv | **Authors:** Wenhao Chen; Sirui Sun; Shengyuan Bai; Guojie Song
**Relevance:** 3/5 — Addresses LLM alignment and safety mechanisms relevant to agent deployment, but focuses on value guidance architecture rather than core agent reasoning, planning, or tool use capabilities.
**Depth:** 3/5 — Provides concrete architectural design (independent value modules, Bridge Tokens) with quantitative safety results (70% harm reduction), but lacks methodology on how these mechanisms interact with agent decision-making or planning systems.

### [From Noise to Diversity: Random Embedding Injection in LLM Reasoning](https://arxiv.org/abs/2605.11936)
**Source:** arxiv | **Authors:** Heejun Kim; Seungpil Lee; Jewon Yeom; Jaewon Sok; Seonghyeon Park; Jeongjae Park; Taesup Kim; Sundon...
**Relevance:** 3/5 — Addresses LLM reasoning via prompt engineering mechanism, but is a narrow optimization technique rather than agent-capability or frontier model work.
**Depth:** 3/5 — Provides solid methodology isolating injection effects and theoretical mechanism, with empirical validation on math reasoning, but incremental rather than foundational contribution.

### [ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows](https://arxiv.org/abs/2605.12376)
**Source:** arxiv | **Authors:** Wei Liu; Yang Gu; Xi Yan; Zihan Nan; Beicheng Xu; Keyao Ding; Bin Cui; Wentao Zhang
**Relevance:** 3/5 — ProfiliTable applies LLM-based agent workflows (multi-agent reasoning, ReAct, iterative refinement) to tabular data tasks, demonstrating agent methodology but focused on a specialized domain rather than frontier agent capabilities or model breakthroughs.
**Depth:** 3/5 — The paper presents clear methodology (profiler-generator-evaluator architecture with closed-loop refinement) and concrete benchmark results across 18 task types, but the contribution is primarily in domain-specific agent orchestration rather than advancing fundamental LLM reasoning or capability emergence.

### [Semantic Reward Collapse and the Preservation of Epistemic Integrity in Adaptive AI Systems](https://arxiv.org/abs/2605.12406)
**Source:** arxiv | **Authors:** William Parris
**Relevance:** 3/5 — Directly addresses a training/optimization challenge (RLHF preference collapse) that affects LLM agent behavior and reliability, but is primarily a safety/alignment concern rather than a core agent capability or capability-enabling advance.
**Depth:** 3/5 — Proposes a conceptual framework (SRC/CRS) grounded in multiple theoretical domains with clear problem motivation, but lacks concrete experimental validation, benchmark results, or empirical demonstration of the proposed solution's effectiveness.

### [Rotation-Preserving Supervised Fine-Tuning](https://arxiv.org/abs/2605.10973)
**Source:** arxiv | **Authors:** Hangzhan Jin; Tianwei Ni; Lu Li; Pierre-Luc Bacon; Mohammad Hamdaqa; Doina Precup
**Relevance:** 3/5 — Fine-tuning methodology that preserves model capabilities during adaptation is relevant to agent training pipelines, but the work is primarily about general LLM optimization rather than agent-specific capabilities or reasoning.
**Depth:** 3/5 — Solid methodological contribution with clear motivation (OOD degradation), concrete mechanism (rotation preservation via singular subspace constraints), and empirical validation across model sizes, though focused on a specific optimization problem rather than emerging agent capabilities.

### [$\xi$-DPO: Direct Preference Optimization via Ratio Reward Margin](https://arxiv.org/abs/2605.10981)
**Source:** arxiv | **Authors:** Zhengyuan Fan; Zhonghua Wu; Yuxuan Du; Qun Chen
**Relevance:** 3/5 — Direct preference optimization is a frontier training method that affects LLM capabilities for agents, but this work focuses on hyperparameter interpretability rather than agent-specific capabilities or deployment.
**Depth:** 3/5 — The paper provides solid methodology (reformulation analysis, ratio margin derivation) and concrete results (hyperparameter tuning insights), but the contribution is incremental optimization of existing DPO variants rather than paradigm-shifting.

### [VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference](https://arxiv.org/abs/2605.11334)
**Source:** arxiv | **Authors:** Jasmine Qi; Danylo Dantsev; Muyang Sun
**Relevance:** 3/5 — LLM judge confidence estimation is tangential to core agent capabilities; it supports evaluation of agent outputs rather than enabling agent reasoning, planning, or tool use.
**Depth:** 3/5 — The paper presents solid methodology (decomposition into sub-checks, three structural signals, calibration via Platt scaling) and comprehensive empirical validation across multiple models and benchmarks, but the contribution is incremental within the narrower domain of confidence calibration.

### [It's not the Language Model, it's the Tool: Deterministic Mediation for Scientific Workflows](https://arxiv.org/abs/2605.13245)
**Source:** arxiv | **Authors:** Marios Adamidis; Danae Katrisioti; Yannis Tzitzikas; Emmanuel Stratakis
**Relevance:** 3/5 — Addresses tool use in LLM agents and determinism/reproducibility challenges, but the contribution is narrowly scoped to scientific workflow mediation rather than advancing frontier capabilities or general agent reasoning.
**Depth:** 3/5 — Provides concrete methodology (typed mediation pattern), empirical results (reproducibility comparison across platforms), and identifies a structural insight about deployment topology, but lacks broader architectural or capability innovation beyond the specific application domain.

### [Position: Assistive Agents Need Accessibility Alignment](https://arxiv.org/abs/2605.13579)
**Source:** arxiv | **Authors:** Jie Hu; Changyuan Yan; Yu Zheng; Ziqian Wang; Jiaming Zhang
**Relevance:** 3/5 — Addresses LLM-based agent design and evaluation constraints, but focuses primarily on accessibility alignment as a design objective rather than core agent capabilities or frontier model advances.
**Depth:** 3/5 — Provides concrete analysis of 778 task instances and proposes a lifecycle-oriented design pipeline with identified failure modes, but lacks algorithmic methodology or empirical results demonstrating solutions to the identified mismatches.

### [Low-Rank Adapters Initialization via Gradient Surgery for Continual Learning](https://arxiv.org/abs/2605.12752)
**Source:** arxiv | **Authors:** Joana Pasquali; Ramiro N. Barros; Arthur S. Bianchessi; Vin\'icius Conte Turani; Jo\~ao Vitor Boer A...
**Relevance:** 3/5 — Addresses continual learning in LLMs via LoRA, a technique relevant to agent deployment and multi-task adaptation, but focuses on parameter efficiency rather than agent reasoning, planning, or capabilities.
**Depth:** 3/5 — Provides clear methodology (gradient surgery for LoRA initialization via SVD projection) and evaluates on standard benchmarks (TRACE, Super-NI) with concrete metrics, but incremental within adapter tuning rather than frontier capability advancement.

### [Neurodata Without Boredom: Benchmarking Agentic AI for Data Reuse](https://arxiv.org/abs/2605.12808)
**Source:** arxiv | **Authors:** Ling-Qi Zhang; Kristin Branson
**Relevance:** 3/5 — Directly evaluates LLM-based agents on a concrete task (data understanding and reformation) with methodology and error characterization, but neuroscience data reuse is domain-specific and not core to frontier agent capabilities research.
**Depth:** 3/5 — Provides concrete benchmark results across eight papers, characterizes failure modes of coding agents, and identifies reliability issues with agents-as-judges, offering solid empirical contribution to understanding agent limitations in practice.

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

### [Do Vision-Language-Models show human-like logical problem-solving capability in point and click puzzle games?](https://arxiv.org/abs/2605.11223)
**Source:** arxiv | **Authors:** Dominik Helfenstein; Marco Menner; Maximilian Triebel
**Relevance:** 3/5 — Evaluates VLM capabilities in interactive environments with reasoning and action execution, which relates to agent capabilities, but focuses on a narrow puzzle domain rather than general agent methodology or frontier model advances.
**Depth:** 2/5 — Introduces a benchmark with evaluation results showing capability gaps, but lacks novel methodology for improving agents or deep insights into why reasoning-execution disparities occur.

### [From Pixels to Prompts: Vision-Language Models](https://arxiv.org/abs/2605.07544)
**Source:** arxiv | **Authors:** Khang Hoang Nhat Vo
**Relevance:** 3/5 — Vision-language models are foundational for multimodal agents, but this is a survey/tutorial book focused on conceptual understanding rather than novel agent architectures or frontier capabilities.
**Depth:** 1/5 — The excerpt promises a pedagogical mental map and intuition-building rather than new methodology, concrete results, or limitations analysis that would substantiate a research contribution.

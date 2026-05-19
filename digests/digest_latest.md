# AI digest — 2026-05-19

Rolling 7-day window. Generated automatically.

---

## Read deeply (165 items)

_High relevance and substantial depth — worth full attention._

### [Agentic Systems as Boosting Weak Reasoning Models](https://arxiv.org/abs/2605.14163)
**Source:** arxiv | **Authors:** Varun Sunkaraneni; Pierfrancesco Beneventano; Riccardo Neumarker; Tomaso Poggio; Tomer Galanti
**Relevance:** 5/5 — Directly addresses LLM-based agent orchestration (committee search, critic-comparator systems) and reasoning model capabilities that enable agentic behavior at inference time.
**Depth:** 5/5 — Provides formal theoretical analysis (coverage amplification, local identifiability, soundness conditions, rank-based bounds) combined with concrete empirical results on SWE-bench Verified showing weak-model committee strategies matching frontier models.

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


## Worth knowing (56 items)

_On-criterion but lower depth, or peripheral relevance._

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

### [Do Vision-Language-Models show human-like logical problem-solving capability in point and click puzzle games?](https://arxiv.org/abs/2605.11223)
**Source:** arxiv | **Authors:** Dominik Helfenstein; Marco Menner; Maximilian Triebel
**Relevance:** 3/5 — Evaluates VLM capabilities in interactive environments with reasoning and action execution, which relates to agent capabilities, but focuses on a narrow puzzle domain rather than general agent methodology or frontier model advances.
**Depth:** 2/5 — Introduces a benchmark with evaluation results showing capability gaps, but lacks novel methodology for improving agents or deep insights into why reasoning-execution disparities occur.

### [From Descriptive to Prescriptive: Uncover the Social Value Alignment of LLM-based Agents](https://arxiv.org/abs/2605.14034)
**Source:** arxiv | **Authors:** Jinxian Qu; Qingqing Gu; Teng Chen; Luo Ji
**Relevance:** 3/5 — Directly addresses LLM-based agent behavior alignment and decision-making, but focuses on social values and emotions rather than core agent capabilities like reasoning, planning, or tool use.
**Depth:** 2/5 — Proposes a GraphRAG-based framework with evaluation on DAILYDILEMMAS, but lacks sufficient methodological detail on the alignment mechanism and provides incremental improvements over prompt-based baselines without deeper architectural insights.

### [Emotion-Attended Stateful Memory (EASM):The Architecture for Hyper-Personalization at Scale](https://arxiv.org/abs/2605.14833)
**Source:** arxiv | **Authors:** Vineet Kotecha; Vansh Gupta
**Relevance:** 3/5 — Stateful memory and context management are relevant to LLM agent capabilities, but this work focuses on conversational personalization rather than reasoning, planning, or tool use that define frontier agent research.
**Depth:** 2/5 — The paper presents an A/B study with concrete improvements but lacks detailed methodology on the memory architecture, emotional signal extraction mechanisms, or how the approach generalizes beyond conversational personalization.

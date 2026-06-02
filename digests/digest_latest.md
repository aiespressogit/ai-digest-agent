# AI digest — 2026-06-02

Rolling 7-day window. Generated automatically.

---

## Read deeply (105 items)

_High relevance and substantial depth — worth full attention._

### [The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary](https://arxiv.org/abs/2606.00376)
**Source:** arxiv | **Authors:** Dongxin Guo; Jikun Wu; Siu Ming Yiu
**Relevance:** 5/5 — Directly addresses when LLM agents should delegate to tools vs. rely on reasoning, establishing theoretical and empirical foundations for hybrid agent design.
**Depth:** 5/5 — Provides rigorous information-theoretic analysis (Attention Bottleneck Theorem), principled metrics (State-Space Jaccard), concrete deterministic horizon bounds, and extensive empirical validation across 12 models and 8 domains with significant performance gaps (86-94% vs 24-42%).

### [Agentic Transformers Provably Learn to Search via Reinforcement Learning](https://arxiv.org/abs/2606.00183)
**Source:** arxiv | **Authors:** Tong Yang; Yu Huang; Yingbin Liang; Yuejie Chi
**Relevance:** 5/5 — Directly addresses how transformer-based agents acquire search and reasoning capabilities through RL training—a core frontier capability for LLM-based agents.
**Depth:** 5/5 — Provides rigorous mechanistic analysis of how attention heads specialize to implement tree search, with formal RL training dynamics and concrete generalization results.

### [MAVEN: Improving Generalization in Agentic Tool Calling](https://arxiv.org/abs/2605.30738)
**Source:** arxiv | **Authors:** Omkar Ghugarkar; Vishvesh Bhat; Muhammad Ahmed Mohsin; Asad Aali
**Relevance:** 5/5 — Directly addresses core LLM agent challenge: generalization in tool calling through reasoning, planning, and intermediate state preservation with explicit methodology and comprehensive benchmarking.
**Depth:** 4/5 — Presents concrete architectural contribution (modular verification scaffold), introduces stress-test benchmark exposing reasoning gaps, and provides quantitative results (48→71% on MAVEN-Bench) with cost-efficiency analysis.

### [Learning Agent-Compatible Context Management for Long-Horizon Tasks](https://arxiv.org/abs/2605.30785)
**Source:** arxiv | **Authors:** Lu Yi; Runlin Lei; Liuyi Yao; Yuexiang Xie; Yuyang Li; Wenhao Zhang; Zhewei Wei; Yaliang Li; Jian-Yu...
**Relevance:** 5/5 — Directly addresses a core agent capability—context management for long-horizon reasoning—with methodology and concrete benchmark results on agent performance.
**Depth:** 4/5 — Provides clear methodology (external LLM trained via RL to manage frozen agent context), empirical results across benchmarks, and reveals actionable trade-offs (Fidelity-Reliability) with transfer analysis.

### [Distilling LLM Feedback for Lean Theorem Proving](https://arxiv.org/abs/2605.30861)
**Source:** arxiv | **Authors:** Gaetan Narozniak; G\'erard Biau; R\'emi Munos; Ahmad Rammal; Pierre Marion
**Relevance:** 5/5 — Directly addresses post-training methods for reasoning models on verifiable tasks, tackling concrete limitations of GRPO and proposing a novel training methodology that affects agent capability emergence.
**Depth:** 4/5 — Provides clear methodology (token-level feedback distillation), concrete evaluation metrics (policy entropy, pass@k scaling), and demonstrates complementarity with existing approaches through empirical results.

### [VeriGate: Verifier-Gated Step-Level Supervision for GRPO](https://arxiv.org/abs/2605.30451)
**Source:** arxiv | **Authors:** Aakriti Agrawal; Minghui Liu; Furong Huang
**Relevance:** 5/5 — Directly addresses training methods for reasoning-focused LLM agents using verifier-based supervision and process reward models, core to frontier agent capability development.
**Depth:** 4/5 — Presents concrete methodology (verifier gating, future-cumulated rewards, token-level advantages) with substantial empirical results (20%/12% improvements across reasoning benchmarks) and clear analysis of prior limitations.

### [Counterfactual Evaluation Reveals Hidden Capability Profiles in Clinical LLMs and Agents](https://arxiv.org/abs/2605.30590)
**Source:** arxiv | **Authors:** Matt Turk
**Relevance:** 5/5 — Directly addresses evaluation methodology for LLM-based agents in clinical domains, introducing an interventional metric (CSS) that reveals hidden capability gaps in reasoning and responsiveness that standard metrics miss.
**Depth:** 4/5 — Presents rigorous pre-registered methodology with counterfactual perturbations across five clinically meaningful dimensions, concrete benchmark results showing frontier models rank oppositely under CSS vs. CMS, explicit structural failures in tool-using agents, and clinical validation from multiple raters.

### [Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults](https://arxiv.org/abs/2606.00914)
**Source:** arxiv | **Authors:** Rana Muhammad Usman
**Relevance:** 5/5 — Directly addresses a critical frontier agent safety concern: how external information ranking and composition causally steer LLM agent decisions, with methodology isolating this control surface.
**Depth:** 4/5 — Provides rigorous controlled protocol, 2,785 rollouts across four models with statistical significance testing, identifies three behavioral regimes, dose-response characterization, and proposes defenses.

### [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/abs/2606.01139)
**Source:** arxiv | **Authors:** Yuxuan Liu; Zhaochen Su; Lingyun Xie; Yuhao Zhang; Qing Zong; Jiahe Guo; Zhongwei Xie; Yiyan Ji; Yau...
**Relevance:** 5/5 — Directly addresses LLM agent skill development—a core capability that enables agents to execute workflows, recover from failures, and improve through iterative refinement.
**Depth:** 4/5 — Presents clear methodology (trace-conditioned diagnosis, principle retrieval, execution-anchored edits) with substantial empirical results (36.05% → 61.63% on SkillsBench) across multiple models and benchmarks, plus cross-model transferability analysis.

### [SkillSmith: Co-Evolving Skills and Tools for Self-Improving Agent Systems](https://arxiv.org/abs/2606.01314)
**Source:** arxiv | **Authors:** Yangbo Wei; Zhen Huang; Shaoqiang Lu; Junhong Qian; Qifan Wang; Chen Wu; Lei He
**Relevance:** 5/5 — Directly addresses LLM-based agent capability through skill discovery, tool evolution, and multi-skill reasoning—core mechanisms for self-improving agent systems.
**Depth:** 4/5 — Presents substantial methodology (unified proposal space, Lotka-Volterra dynamics for skill-tool interactions, anti-pattern recording) with concrete experimental results across three benchmarks and multiple model scales.

### [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416)
**Source:** arxiv | **Authors:** Rahul Suresh Babu; Adarsh Agrawal
**Relevance:** 5/5 — Directly addresses orchestration and reliability mechanisms for tool-augmented LLM agents, a core frontier capability for agentic systems.
**Depth:** 4/5 — Presents explicit methodology (failure mapping, bounded recovery budgets, verification) with concrete benchmark results (98.8% success, systematic comparisons across baselines) and identifies real orchestration-level failure modes motivating the approach.

### [ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL](https://arxiv.org/abs/2606.01619)
**Source:** arxiv | **Authors:** Zelin He; Haotian Lin; Boran Han; Wei Zhu; Haoyang Fang; Bernie Wang; Xuan Zhu; Runze Li; Matthew Re...
**Relevance:** 5/5 — Directly addresses LLM agent capability through RL-based skill learning and policy optimization, a frontier method for enabling agents to accumulate and reuse strategies across tasks.
**Depth:** 4/5 — Presents concrete methodology (assertion-driven skill creator, within-group rollout sampling, Thompson Sampling with adaptive discounting) integrated with GRPO, supported by empirical results showing skill lifecycle dynamics and generalization gains on unseen tasks.

### [CAPF: Guiding Search-Agent Rollouts with Credit-Attenuated Privileged Feedback](https://arxiv.org/abs/2606.01830)
**Source:** arxiv | **Authors:** Bin Chen; Xinye Liao; Yiming Liu; Xin Liao; Chonghan Liu
**Relevance:** 5/5 — Directly addresses LLM-based agent training via reinforcement learning with verifiable rewards, a core frontier capability for enabling reasoning and planning in search agents.
**Depth:** 4/5 — Presents concrete methodology (CAPF mechanism with credit attenuation) that solves a specific training bottleneck, includes empirical results showing 3.8pp improvement on seven QA benchmarks, and identifies a clear limitation of prior outcome-only RLVR approaches.

### [POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems](https://arxiv.org/abs/2606.02282)
**Source:** arxiv | **Authors:** I\~naki Dellibarda Varela; R. Sendra-Arranz; Pablo Romero-Sorozabal; J. M. Valverde-Garc\'ia; Annema...
**Relevance:** 5/5 — Directly addresses failure detection, safety evaluation, and deployment of LLM-based multi-agent systems—core concerns for frontier agent research.
**Depth:** 4/5 — Presents a novel protocol (POIROT) with clear methodology for leveraging agent epistemic diversity, includes quantitative results with statistical significance testing, and releases benchmarking infrastructure (BLAME) for reproducible evaluation.

### [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](https://arxiv.org/abs/2606.02355)
**Source:** arxiv | **Authors:** Zhongyu He; Yuanfan Li; Fei Huang; Tianyu Chen; Siyuan Chen; Xingyang Li; Meng Hsuan Yu; Xiangrong L...
**Relevance:** 5/5 — Directly addresses LLM-based agent training through skill discovery and internalization, a core capability for long-horizon reasoning and planning.
**Depth:** 4/5 — Presents a concrete three-phase framework with explicit methodology (warm-up, self-skill mining, distillation), validated through quantified benchmark improvements on ALFWorld and WebShop tasks.

### [COMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/abs/2606.02372)
**Source:** arxiv | **Authors:** Youwei Liu; Jian Wang; Hanlin Wang; Wenjie Li
**Relevance:** 5/5 — Directly addresses LLM-based agent capabilities through a novel framework that improves planning and decision-making via co-evolving world models and policies.
**Depth:** 4/5 — Presents clear methodology (self-distillation loop, future-aware reflection, on-policy trajectory adaptation) with concrete experimental results across multiple benchmarks and analyses of improvement mechanisms.

### [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/abs/2606.00135)
**Source:** arxiv | **Authors:** Tong Liu; Cheng Qian; Matej Cief; Yuan He; Daniele Dan; Nikolaos Aletras; Gabriella Kazai
**Relevance:** 5/5 — Directly addresses tool-calling methodology in LLM agents, covering both evaluation rigor and training efficiency—core frontier capabilities for agent deployment.
**Depth:** 4/5 — Provides systematic analysis of evaluation sensitivity with concrete implementation factors, identifies specific sources of computational waste in RL training, and proposes techniques with wall-clock speedup validation.

### [Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621)
**Source:** arxiv | **Authors:** Minhua Lin; Juncheng Wu; Zijun Wang; Zhan Shi; Yisi Sang; Bing He; Zewen Liu; Tianxin Wei; Zongyu Wu...
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities, specifically how agents self-evolve their external harnesses (prompts, skills, tools) and which model capabilities enable effective harness updating and benefit.
**Depth:** 4/5 — Provides systematic empirical analysis distinguishing two separate capabilities (harness-updating vs. harness-benefit), identifies concrete failure modes (activation and instruction following), and derives actionable training insights backed by cross-model comparisons.

### [Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward](https://arxiv.org/abs/2605.30824)
**Source:** arxiv | **Authors:** Mustafa Anis Hussain; Xinle Wu; Yao Lu
**Relevance:** 4/5 — Directly addresses LLM-based agent planning and reasoning for complex multi-step tasks, with explicit methodology for structuring and training planning capabilities.
**Depth:** 4/5 — Provides concrete methodology (DAG-based plan representation, two-stage RL training, structured reward assignment) and empirical results (5.1-8.0 point improvements on benchmarks) with clear motivation addressing credit assignment in planning.

### [SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning](https://arxiv.org/abs/2605.30832)
**Source:** arxiv | **Authors:** Jian Yao; Xiongcai Luo; Ran Cheng; Kay Chen Tan
**Relevance:** 4/5 — Directly addresses chain-of-thought reasoning efficiency in LLMs through an RL-based optimization framework, a core capability enabling agent planning and reasoning.
**Depth:** 4/5 — Provides theoretical characterization of segment suboptimality, proposes a novel RL framework (SLAT) with segment-level granularity, and demonstrates 50% length reduction with maintained accuracy on standard benchmarks.

### [COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents](https://arxiv.org/abs/2605.30838)
**Source:** arxiv | **Authors:** Wenkai Shen; Pengyang Zhou; Jiahe Xu; Jiaming Qian; Haozhe He; Zhihao Huang; Chaochao Chen; Xiaolin ...
**Relevance:** 4/5 — Directly addresses safety alignment for LLM-based search agents during multi-step reasoning and tool use, a core frontier capability challenge.
**Depth:** 4/5 — Presents concrete methodology (cognitive tree exploration + introspective step-wise alignment) with empirical evaluation on safety-utility tradeoffs and training efficiency.

### [TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories](https://arxiv.org/abs/2605.31308)
**Source:** arxiv | **Authors:** Junjie Nian; Kang Chen; Ge Zhang; Yixin Cao; Yugang Jiang
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation and improvement through trajectory analysis, with concrete methodology for understanding agent behavior and failure modes across benchmarks.
**Depth:** 4/5 — Presents a substantive graph-based framework with explicit methodology (TraceGraph construction, trap detection, recovery pipelines) and concrete results showing improvements on SWE-bench (40.4% → 43.5% on fired subset).

### [Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents](https://arxiv.org/abs/2605.31354)
**Source:** arxiv | **Authors:** Yunpeng Zhou
**Relevance:** 4/5 — Directly addresses LLM-based agent failure modes in multi-step collaborative reasoning with shared memory, a core capability for agent systems.
**Depth:** 4/5 — Provides systematic failure mode diagnosis (Noise Reinforcement, Policy Collapse) with mechanistic analysis of information flow and cost-accuracy trade-offs across multiple benchmarks.

### [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468)
**Source:** arxiv | **Authors:** Weitong Qian; Beicheng Xu; Zhongao Xie; Bowen Fan; Guozheng Tang; Jiale Chen; Xinzhe Wu; Mingtian Ya...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture with explicit focus on memory systems, multi-agent coordination, and autonomous research execution across the full scientific lifecycle.
**Depth:** 4/5 — Provides concrete methodology across four core modules (SciMem schema design, SciFlow lifecycle orchestration, SciDAG multi-agent templates, SciEvolve feedback loops) with architectural mechanisms for persistent memory and skill evolution.

### [LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories](https://arxiv.org/abs/2605.31492)
**Source:** arxiv | **Authors:** Liwei Kang; Yee Whye Teh; Wee Sun Lee
**Relevance:** 4/5 — Directly addresses LLM reasoning and planning mechanisms for agents through structured search, a core capability enabling agent behavior.
**Depth:** 4/5 — Provides clear methodology (explicit tree structure via parent pointers), controlled experimental evaluation across three environments, and actionable insight into why search history alone fails without structure.

### [LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis](https://arxiv.org/abs/2605.30434)
**Source:** arxiv | **Authors:** Kewei Xu; Xiaoben Lu; Shuofei Qiao; Zihan Ding; Haoming Xu; Lei Liang; Ningyu Zhang
**Relevance:** 4/5 — Directly evaluates LLM-based agents on long-horizon reasoning and state management, a core capability bottleneck for agentic systems, with concrete methodology and results identifying failure modes.
**Depth:** 4/5 — Provides substantial empirical evaluation across five frontier models with detailed analysis of state-maintenance failures, dependency patterns, and architectural insights into why additional steps don't help—going beyond capability demo to identify mechanisms.

### [Representation Collapse in Sequential Post-Training of Large Language Models](https://arxiv.org/abs/2605.30524)
**Source:** arxiv | **Authors:** Yichen Liu; Mingyu Chen; Hao Wang; Xiaoran Xu; Chenxi Lin; Rui Zhang; Yutong Zhou; Yuxin Yang; Jiaru...
**Relevance:** 4/5 — Directly addresses frontier model capability and training methodology by studying how sequential post-training affects LLM representational properties, which materially impacts agent reasoning and adaptation capacity.
**Depth:** 4/5 — Provides systematic measurement methodology for analyzing representation collapse across multiple post-training stages, concrete empirical results on five specialization types, and evaluates lightweight interventions to preserve learnability with quantified outcomes.

### [LARK: Learnability-Grounded Trajectory Selection for Efficient Reasoning Distillation](https://arxiv.org/abs/2605.30651)
**Source:** arxiv | **Authors:** Tianrun Yu; Kaixiang Zhao; Chih-Chun Chen; Amanda Hughes; Taylor W. Killian; Fenglong Ma; Weitong Zh...
**Relevance:** 4/5 — Reasoning trajectory selection directly impacts distillation efficiency for LLM-based reasoning and agent capabilities, addressing a core methodological challenge in training reasoning models.
**Depth:** 4/5 — The paper contributes novel theoretical analysis (learnability factor ρ, χ²-regularized selection policy with estimation error guarantees) and demonstrates consistent empirical improvements across multiple models and tasks with diagnostic validation.

### [When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?](https://arxiv.org/abs/2605.30719)
**Source:** arxiv | **Authors:** Stephane Hatgis-Kessell; Emma Brunskill
**Relevance:** 4/5 — Directly studies LLM-based agents as policy optimizers with systematic methodology and concrete RL task results, addressing a frontier capability question about when LLMs can replace classical algorithms.
**Depth:** 4/5 — Presents Prompted Policy Optimization with clear methodology, benchmark results across multiple domains (exploration, robotics, real-world control), analysis of what policies emerge, and explicit discussion of failure modes and limitations.

### [Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation](https://arxiv.org/abs/2605.30757)
**Source:** arxiv | **Authors:** Haozhou Zhang
**Relevance:** 4/5 — Directly addresses test-time reasoning mechanisms (chain-of-thought vs. looped transformers) that are central to how LLM-based agents perform reasoning and planning.
**Depth:** 4/5 — Provides rigorous theoretical analysis with complexity-theoretic separation results and controlled empirical sweeps demonstrating how memory architecture fundamentally constrains reasoning capability.

### [Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO](https://arxiv.org/abs/2605.30789)
**Source:** arxiv | **Authors:** Yiming Ren; Yiran Xu; Zicheng Lin; Chufan Shi; Yukang Chen; Dingdong Wang; Tianhe Wu; Junjie Wang; Y...
**Relevance:** 4/5 — Directly addresses frontier LLM training methodology (GRPO) and policy optimization techniques that materially affect model capabilities for reasoning and planning tasks.
**Depth:** 4/5 — Provides concrete methodology (S2L-PO framework with progressive annealing strategy), clear mechanistic insight (policy-level vs token-level diversity), and substantial empirical results (+8.8% on AIME 24 with reduced compute).

### [CoMem: Context Management with A Decoupled Long-Context Model](https://arxiv.org/abs/2605.30842)
**Source:** arxiv | **Authors:** Yuwei Zhang; Chengyu Dong; Shuowei Jin; Changlong Yu; Hejie Cui; Hongye Jin; Xinyang Zhang; Hamed Bo...
**Relevance:** 4/5 — Directly addresses memory management and context handling in LLM-based agents, a core capability that enables long-horizon task solving.
**Depth:** 4/5 — Provides concrete methodology (k-step-off asynchronous pipeline, reward-driven training), theoretical analysis, and empirical results (1.4x latency improvement on SWE-Bench-Verified) with clear engineering insights.

### [ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory](https://arxiv.org/abs/2605.30858)
**Source:** arxiv | **Authors:** Yurui Chang; Yongkang Du; Yuanpu Cao; Jinghui Chen; Lu Lin
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities for forecasting, with explicit focus on memory mechanisms, reasoning, and calibration that enable better agentic decision-making.
**Depth:** 4/5 — Presents concrete methodology (hierarchical taxonomy, factor + reasoning memory, memory-revision procedure) and empirical results on benchmark datasets (Prophet Arena, FutureX) with quantified improvements in accuracy and calibration.

### [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](https://arxiv.org/abs/2605.30859)
**Source:** arxiv | **Authors:** Yujie Wang; Siwei Chen; Longzan Luo; Xinyi Liu; Xupeng Miao; Fangcheng Fu; Bin Cui
**Relevance:** 4/5 — Directly addresses RL training efficiency for LLMs, a frontier capability-enabling methodology that materially affects agent training feasibility and performance.
**Depth:** 4/5 — Provides concrete methodology (distribution-aware trajectory sampling, adaptive redundancy allocation) with quantified results (1.77x acceleration) and characterizes root inefficiencies (intra-prompt long tails) rather than surface-level optimization.

### [Automating Formal Verification with Reinforcement Learning and Recursive Inference](https://arxiv.org/abs/2605.30914)
**Source:** arxiv | **Authors:** Max Tan
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities for formal verification through reinforcement learning from verifiable rewards and verifier-guided inference-time search, which are frontier techniques for improving agent reasoning and decision-making.
**Depth:** 4/5 — Provides substantial methodology (RLVR with GRPO, verifier-guided scaffolding with proof revision), concrete results (verified pass rates: 2.2%→58.1% on Dafny, 46.2%→69.2% on Lean), and explicit limitations (specification hacking, weak progress on repository-scale tasks).

### [Retriever Portfolios: A Principled Approach to Adaptive RAG](https://arxiv.org/abs/2605.31176)
**Source:** arxiv | **Authors:** Miltiadis Stouras; Vincent Cohen-Addad; Silvio Lattanzi; Ola Svensson
**Relevance:** 4/5 — Directly addresses a core LLM-agent capability (adaptive retrieval and tool selection) with principled methodology for portfolio construction and routing.
**Depth:** 4/5 — Provides formal problem formulation (expected best-of-k objective), algorithmic solution with theoretical guarantees, and comprehensive empirical validation across multiple benchmarks with latency/cost analysis.

### [EchoRL: Reinforcement Learning via Rollout Echoing](https://arxiv.org/abs/2605.31228)
**Source:** arxiv | **Authors:** Jinhe Bi; Aniri; Minglai Yang; Xingcheng Zhou; Wenke Huang; Sikuan Yan; Yujun Wang; Zixuan Cao; Mich...
**Relevance:** 4/5 — Directly addresses post-training of LLMs for reasoning via reinforcement learning with verifiable rewards, a frontier capability-enablement method for agent reasoning.
**Depth:** 4/5 — Provides clear methodology (entropy-based EchoClip identification and auxiliary supervision), identifies concrete limitations of prior RLVR methods (advantage degeneracy), and reports extensive experimental validation across 10 benchmarks and 5 LLM backbones.

### [DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization](https://arxiv.org/abs/2605.31455)
**Source:** arxiv | **Authors:** Jian Mu; Tianyi Lin; Chengwei Qin; Zhongxiang Dai; Yao Shu
**Relevance:** 4/5 — DRIFT directly addresses a frontier challenge in LLM agent training: efficient multi-turn optimization that balances online RL's effectiveness with offline SFT's efficiency, a core capability enabler for deployed interactive agents.
**Depth:** 4/5 — The paper provides clear methodology (decoupled rollouts with importance-weighted SFT grounded in KL-regularized RL theory), concrete empirical comparisons against RL baselines, and explicit motivation addressing distribution shift and behavioral collapse limitations.

### [Skill Reuse as Compression in Agentic RL](https://arxiv.org/abs/2605.31509)
**Source:** arxiv | **Authors:** Zhikun Xu; Yu Feng; Jacob Dineen; Taiwei Shi; Jieyu Zhao; Ben Zhou
**Relevance:** 4/5 — Directly addresses LLM-based agent training and generalization through RL, with methodology grounded in information-theoretic principles and evaluation across multiple agent benchmarks.
**Depth:** 4/5 — Provides formal methodology (MDL-based objective, segmentation cost, PAC-Bayes bound), concrete empirical results across three benchmarks showing improvements in in- and out-of-distribution performance, and mechanistic insight into skill reuse as compression.

### [MindGames Arena Generalization Track: In2AI Solution with Delayed Per-Step Reward Attribution](https://arxiv.org/abs/2606.00017)
**Source:** arxiv | **Authors:** Aliaksei Korshuk; Alexander Buyantuev; Ilya Makarov
**Relevance:** 4/5 — Directly addresses RL training methodology for LLM-based agents in multi-agent strategic interaction, a core capability gap for agent deployment.
**Depth:** 4/5 — Presents concrete technical contributions (delayed reward attribution with eligibility gating, curriculum sampling, stratified batching) with empirical validation on a competitive benchmark showing frontier-scale results.

### [Grokers: Bottom-Up Inductive Comprehension and Write-Time Intelligence over Typed Knowledge Graphs](https://arxiv.org/abs/2606.00050)
**Source:** arxiv | **Authors:** Gregory Magarshak
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for knowledge graph comprehension with formal methodology and structured agent reasoning patterns.
**Depth:** 4/5 — Provides formal theorems, deterministic algorithms, and a reference implementation; establishes clear methodology for push-to-write-time intelligence and KV-cache optimization in autonomous agents.

### [Evaluating Interactive Reasoning in Large Language Models: A Hierarchical Benchmark with Executable Games](https://arxiv.org/abs/2606.00103)
**Source:** arxiv | **Authors:** Mingyuan Fan; Weiguang Han; Daixin Wang; Cen Chen; Zhiqiang Zhang; Jun Zhou
**Relevance:** 4/5 — Directly evaluates LLM reasoning and decision-making capabilities through interactive agent-like environments with query generation, observation integration, and adaptive behavior—core competencies for LLM-based agents.
**Depth:** 4/5 — Introduces a structured multi-turn evaluation framework with concrete methodology (executable games, perturbation analysis, metacognitive metrics) and empirical results across frontier models revealing differential performance on interaction efficiency and robustness.

### [CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO](https://arxiv.org/abs/2606.00172)
**Source:** arxiv | **Authors:** Yang Li; Gongle Xue; Yijia Guo; Yuheng Yuan; Liwen Hu; Lei Ma
**Relevance:** 4/5 — Directly addresses frontier LLM agent capability—reasoning via reinforcement learning with verifiable rewards—by improving GRPO training methodology for mathematical reasoning in large language models.
**Depth:** 4/5 — Provides detailed methodology (advantage flipping, self-teacher mechanisms, handling zero-variance groups) with empirical diagnostics of failure modes and concrete improvements on mathematical reasoning benchmarks.

### [MindZero: Learning Online Mental Reasoning With Zero Annotations](https://arxiv.org/abs/2606.00240)
**Source:** arxiv | **Authors:** Shunchi Zhang; Jin Lu; Chuanyang Jin; Yichao Zhou; Zhining Zhang; Tianmin Shu
**Relevance:** 4/5 — Directly addresses core LLM-based agent capability (Theory of Mind reasoning) essential for real-world assistance, with explicit methodology for training MLLMs to perform robust online mental state inference.
**Depth:** 4/5 — Presents concrete training framework (self-supervised RL with model-based reward signal), comparative benchmarks across gridworld and household domains, and clear analysis of why LLMs alone fail and how internalized reasoning improves both accuracy and efficiency.

### [Capability Self-Assessment: Teaching LLMs to Know Their Limits](https://arxiv.org/abs/2606.00251)
**Source:** arxiv | **Authors:** Haoyan Yang; Reza Shirkavand; Yukai Jin; Jiawei Zhou; Shangqian Gao; Heng Huang
**Relevance:** 4/5 — Directly addresses a critical agent capability—self-assessment and deciding when to delegate—which is fundamental to reliable autonomous decision-making in LLM-based systems.
**Depth:** 4/5 — Provides clear methodology (RL vs. SFT comparison), concrete empirical results across model families/scales, demonstrates generalization, and identifies practical applications (local-cloud inference decisions, training data selection).

### [From "Weak" Signals to Strong Models: Preference Delta Aggregation with LoRA Merging](https://arxiv.org/abs/2606.00357)
**Source:** arxiv | **Authors:** Qi Sun; Siyue Zhang; Yulin Chen; Yuxiang Xue; Ru Peng; Chen Zhao
**Relevance:** 4/5 — Directly addresses frontier model capability improvement through preference optimization and adapter merging, with explicit evaluation on agentic search benchmarks.
**Depth:** 4/5 — Presents novel methodology (PDA framework with geometric alignment merging), concrete benchmark results (6.8-7.3 point improvements on knowledge reasoning and agentic search), and analysis of complementary capability composition.

### [VESTA: Visual Exploration with Statistical Tool Agents](https://arxiv.org/abs/2606.00384)
**Source:** arxiv | **Authors:** William Rudman; Abhishek Divekar; Kanishk Jain; Sebastian Joseph; Stella S. R. Offner; Matthew Lease...
**Relevance:** 4/5 — VESTA directly addresses LLM-based agent capabilities through tool use, planning, and iterative refinement—core mechanisms for agent reasoning—with explicit methodology for dynamic tool creation and context management.
**Depth:** 4/5 — The paper provides concrete methodology (dynamic toolkit generation, diagnostic tool selection, context accumulation), introduces a new benchmark (DAWN) with quantified results, and demonstrates performance gains over baselines with analysis of tool sophistication.

### [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](https://arxiv.org/abs/2606.00424)
**Source:** arxiv | **Authors:** Can Jin; Jiakang Li; Rui Wu; Eddy Zhang; Dimitris N. Metaxas
**Relevance:** 4/5 — Directly addresses scalable oversight and weak supervision for strong models, a frontier capability challenge for LLM-based agents and autonomous systems.
**Depth:** 4/5 — Proposes concrete methodology (OPCD with on-policy critique distillation and adaptive self-teacher signals) with experimental results on reasoning and alignment benchmarks demonstrating measurable improvements.

### [TAPS: Target-Aware Prefix Tree Selection for Diffusion-Drafted Speculative Decoding](https://arxiv.org/abs/2606.00487)
**Source:** arxiv | **Authors:** Zhuoyu Wang; Junnan Huang; Xinyu Chen
**Relevance:** 4/5 — Speculative decoding with diffusion drafters directly optimizes inference efficiency for LLM-based systems, materially affecting what agents can deploy efficiently in production.
**Depth:** 4/5 — Proposes a principled target-aware mechanism (TAPS) that reframes draft-tree selection via prefix-conditioned acceptance estimates, with comprehensive benchmarking showing 1.36-1.74x improvements over prior art.

### [Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design](https://arxiv.org/abs/2606.00555)
**Source:** arxiv | **Authors:** Zaifei Yang; Weiyu Chen; Yaqing Wang; James Kwok
**Relevance:** 4/5 — Directly addresses LLM-based agents in a complex reasoning task (drug design), with focus on agent planning, evaluation failures, and multi-agent coordination mechanisms.
**Depth:** 4/5 — Provides explicit diagnostic metrics for failure modes, detailed methodology (site mapping, edit-response probing, multi-agent orchestration), and benchmark results showing state-of-the-art performance with clear mitigation of identified problems.

### [TRACE: Trajectory Risk-Aware Compression for Long-Horizon Agent Safety](https://arxiv.org/abs/2606.00611)
**Source:** arxiv | **Authors:** Zhepei Hong; Lin Wang; Liting Li; Haokai Ma; Junfeng Fang; Fei Shen; Dan Zhang; Xiang Wang
**Relevance:** 4/5 — Directly addresses safety detection and risk assessment for long-horizon LLM agents, a frontier capability challenge for agent deployment.
**Depth:** 4/5 — Proposes a concrete Compressor-Reader architecture with trajectory-level supervision, demonstrates significant improvements (up to 12.6pp) across multiple benchmarks, and provides mechanistic insights via attention visualization.

### [ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment](https://arxiv.org/abs/2606.00644)
**Source:** arxiv | **Authors:** Qiuyu Tian; Zequn Liu; Yingce Xia; Haojie Yin; Youyong Kong
**Relevance:** 4/5 — Directly evaluates LLM agents on research judgment and decision-making with explicit methodology for temporal control and evidence organization, a frontier capability relevant to agent deployment.
**Depth:** 4/5 — Provides concrete benchmark design with 500 tasks, diagnostic analysis revealing evidence-decision decoupling failure modes, and systematic evaluation across multiple agent architectures and backbones.

### [MOSAIC: Modular Orchestration for Structured Agentic Intelligence and Composition](https://arxiv.org/abs/2606.00708)
**Source:** arxiv | **Authors:** Yifan Bao; Xinyu Xi; Xinyu Liu; Wen Ge; Lei Jiang; Kevin Zhang; Raad Khraishi; Yihao Ang; Anthony K....
**Relevance:** 4/5 — MOSAIC directly addresses LLM-based agent architecture for structured reasoning, planning, and code generation with concrete execution feedback mechanisms and reinforcement learning refinement.
**Depth:** 4/5 — The work provides explicit methodology (blueprint intermediate representation, staged search, failure-aware RL policy) and concrete results on financial time-series tasks, comparing against AutoML and agentic baselines with improvements in performance and traceability.

### [Latent Reward Steering: An Adaptive Inference-Time Framework that Implicitly Promotes Cognitive Behaviors in Reasoning LLMs](https://arxiv.org/abs/2606.00726)
**Source:** arxiv | **Authors:** Jiakang Li; Guanyu Zhu; Can Jin; Chenxi Huang; Dexu Yu; Ronghao Chen; Yang Zhou; Hongwu Peng; Xuanqi...
**Relevance:** 4/5 — Directly addresses inference-time steering of reasoning LLMs using latent representations and reward optimization, a core capability mechanism for LLM-based agents.
**Depth:** 4/5 — Presents novel methodology combining sparse autoencoders with latent reward models for adaptive cognitive behavior promotion, includes empirical validation across multiple benchmarks with mechanistic analysis.

### [CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems](https://arxiv.org/abs/2606.00756)
**Source:** arxiv | **Authors:** Yannan Wang; Longli Yang; Zhen Liu; Abhishek Kumar; Carsten Maple
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities in long-horizon tasks through a novel cloud-edge architecture for memory management and reflection.
**Depth:** 4/5 — Provides clear methodology (Centralized Reflection, Decentralized Execution design with hierarchical memory and semantic subgoal tracking) and evaluates across five long-horizon tasks with concrete success-rate improvements.

### [FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search](https://arxiv.org/abs/2606.00765)
**Source:** arxiv | **Authors:** Md Nakhla Rafi; Md Ahasanuzzaman; Dong Jae Kim; Zhijie Wang; Tse-Hsun Chen
**Relevance:** 4/5 — Directly addresses failure diagnosis and attribution in LLM-based multi-agent systems, a key capability for reliable agent deployment and reasoning.
**Depth:** 4/5 — Introduces dependency-guided search methodology to distinguish error-introducing steps from error-propagating ones, with concrete benchmark results showing improvements over baselines on algorithm-generated and hand-crafted failure trajectories.

### [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](https://arxiv.org/abs/2606.01062)
**Source:** arxiv | **Authors:** Jiarui Feng; Hanqing Zeng; Karish Grover; Ruizhong Qiu; Yinglong Xia; Qiang Zhang; Qifan Wang; Ren C...
**Relevance:** 4/5 — Directly addresses a frontier model capability (MoE scaling in LLMs) that affects agent reasoning capacity and computational efficiency at scale.
**Depth:** 4/5 — Provides theoretical analysis of aggregation mechanisms, proposes a novel structural approach (DAG-MoE), and includes extensive empirical validation on pretraining and fine-tuning tasks.

### [Expected Value Alignment for Generative Reward Modeling in Formal Mathematics Verification](https://arxiv.org/abs/2606.01160)
**Source:** arxiv | **Authors:** Shihao Ji; Haotao Tan; Zihui Song; Mingyu Li
**Relevance:** 4/5 — Directly addresses process reward modeling for LLM-based agents in formal verification, a frontier capability that enables agents to self-evaluate reasoning steps during search and RL training.
**Depth:** 4/5 — Presents novel methodology (EVA) that solves a concrete trade-off in reward model design with clear technical insight (logit-based expectation over discrete tokens), instantiated and evaluated in a real system (Leibniz/Lean 4).

### ["Skill issues'': data-centric optimization of lakehouse agents](https://arxiv.org/abs/2606.01185)
**Source:** arxiv | **Authors:** Nicole Rose Schneider; Davide Ghilardi; Giacomo Piccinini; Jacopo Tagliabue
**Relevance:** 4/5 — Directly addresses LLM-based agent optimization through data-centric skill engineering and evaluation methodology for coding agents operating on data infrastructure.
**Depth:** 4/5 — Presents concrete methodology for agent skill optimization including task-verifier generation, sandbox execution, and state-verification evaluation with quantified 31.9% accuracy improvement on 25 tasks.

### [Can LLM Agents Sustain Long-Horizon Organizational Dynamics?](https://arxiv.org/abs/2606.01199)
**Source:** arxiv | **Authors:** Xuancheng Zhu; Yang Yue; Shuaibing Wan; Zihan Dou; Xiaohan Zhang; Yongrui Liu; Guoshun Nan
**Relevance:** 4/5 — Directly addresses LLM-based agent coordination, memory management, and long-horizon planning—core agent capabilities—through a hierarchical framework tested on sustained organizational simulation.
**Depth:** 4/5 — Introduces TaskWeave with explicit mechanism (Formulate-Partition-Diagnose-Align cycle and dependency-aware trace memory), evaluates against baselines on multiple coherence/grounding metrics, and identifies structured memory as a key enabler for reliable agent behavior.

### [The Shape of Wisdom: Decision Trajectories in Language Models](https://arxiv.org/abs/2606.01202)
**Source:** arxiv | **Authors:** Shailesh Rana
**Relevance:** 4/5 — Directly addresses frontier model capabilities and reasoning mechanisms that affect what LLM-based agents can reliably do, with concrete methodology for understanding decision-making in language models.
**Depth:** 4/5 — Provides reproducible empirical methodology (trajectory analysis across three models, 9,000 examples) with mechanistic insights into how attention and MLP layers move decision margins, enabling better understanding of model reliability and robustness.

### [HomeFlow: A Data Flywheel for Smart Home Agent Training with Verifiable Simulation](https://arxiv.org/abs/2606.01230)
**Source:** arxiv | **Authors:** Yi Gu; Huacan Wang; Shuo Zhang; Yuqing Hou; Lei Xue; Weipeng Ming; Chen Liu; Fangzhou Yu; Kuan Li; R...
**Relevance:** 4/5 — Directly addresses LLM-based agent training for physical-world control with methodology for data generation, trajectory synthesis, and iterative improvement through environment interaction.
**Depth:** 4/5 — Substantial methodological contributions including simulation environment design, procedural generation, MCTS-based trajectory synthesis, RLVE optimization, and comprehensive benchmark evaluation with concrete results.

### [ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment](https://arxiv.org/abs/2606.01279)
**Source:** arxiv | **Authors:** Zhengyang Zhao; Shengjie Ye; Lu Ma; Hao Liang; Hengyi Feng; Wentao Zhang
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities for autonomous instruction alignment and post-training, a frontier challenge in agent deployment and model improvement.
**Depth:** 4/5 — Presents methodological contributions (World Tree routing mechanism, diagnostic feedback loops) and concrete results on PostTrainBench with cross-task generalization, plus identifies and solves a specific agent limitation (context overflow in long-horizon data curation).

### [Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems](https://arxiv.org/abs/2606.01351)
**Source:** arxiv | **Authors:** Junze Zhu; Weihao Chen; Xuanwang Zhang; Zhen Wu; Xinyu Dai
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent systems, their orchestration architectures, and failure modes that materially affect agent capability.
**Depth:** 4/5 — Provides explicit methodology (Mean-Field Entropy Dynamics framework), introduces a validation pipeline (IWG), identifies a concrete failure mechanism (Reasoning Trap with context squeezing), and offers physically interpretable parameters for system analysis.

### [Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution](https://arxiv.org/abs/2606.01435)
**Source:** arxiv | **Authors:** Vikas Reddy; Sumanth Challaram
**Relevance:** 4/5 — Directly addresses a critical capability gap in LLM-based agent memory systems—conflict resolution during fact consolidation—with concrete methodology and benchmark results on a frontier evaluation framework.
**Depth:** 4/5 — Provides clear mechanistic insight (deterministic aggregation vs. LLM judgment), rigorous matched-setup comparisons isolating the resolver component, and substantial empirical gains (+28 points over prior SOTA on single-hop, +20 on multi-hop).

### [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](https://arxiv.org/abs/2606.01462)
**Source:** arxiv | **Authors:** Mingzhong Sun; Teresa Yeo; Armando Solar-Lezama; Tan Zhi-Xuan
**Relevance:** 4/5 — Directly investigates a frontier capability limitation in LLM-based reasoning models—a core constraint on agent reasoning—through systematic evaluation methodology.
**Depth:** 4/5 — Provides concrete methodology (VAIR dataset design), quantitative results (48% vs near-perfect production), mechanistic analysis (CoT inspection, linear probes, causal patching), and identifies a specific training-induced bias limiting reasoning robustness.

### [Joint Agent Memory and Exploration Learning via Novelty Signals](https://arxiv.org/abs/2606.01528)
**Source:** arxiv | **Authors:** Shizuo Tian; Xiaohong Weng; Rui Kong; Yuxuan Chen; Guohong Liu; Yuebing Song; Jiacheng Liu; Yuchen L...
**Relevance:** 4/5 — Directly addresses memory and exploration mechanisms for LLM-based agents in open-ended environments, which are core capabilities enabling agentic behavior.
**Depth:** 4/5 — Presents a novel framework (JAMEL) with clear methodology: joint training of memory and exploration via novelty signals, concrete empirical evaluations showing performance gains, and identified limitation (expensive raw history retention) that motivates the latent memory approach.

### [RoleCDE:Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents](https://arxiv.org/abs/2606.01552)
**Source:** arxiv | **Authors:** Huayi Lai; Shichao Song; Simin Niu; Hanyu Wang; Jiawei Yang; Zhouxing Wang; Zhiqiang Yin; Xun Liang
**Relevance:** 4/5 — Directly addresses LLM-based agents (role-playing agents) and their decision-making under conflicting constraints, a frontier capability concern for agent alignment and behavior control.
**Depth:** 4/5 — Provides structured benchmark methodology (8k role profiles, 24k dilemmas), identifies a concrete phenomenon (Role Value Decoupling), demonstrates evaluation results across LLMs, and offers a fine-tuning mitigation with preservation metrics.

### [S-SPPO: Semantic-Calibrated Self-Play Preference Optimization](https://arxiv.org/abs/2606.01561)
**Source:** arxiv | **Authors:** Xiwen Chen; Wenhui Zhu; Jingjing Wang; Peijie Qiu; Zhipeng Wang; Huayu Li; ZhengXiao He; Xuanzhao Do...
**Relevance:** 4/5 — Directly addresses LLM preference alignment and training methodology that materially affects agent capability and policy quality, core to frontier model development.
**Depth:** 4/5 — Provides clear methodology (semantic calibration via gating and latent repulsion), theoretical analysis (Nash Equilibrium convergence), and concrete empirical results (52.19% win rate on AlpacaEval 2.0) addressing a real instability in prior SPPO work.

### [Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation](https://arxiv.org/abs/2606.01725)
**Source:** arxiv | **Authors:** Donghwan Kim; Prakhar Singh; Younghoon Min; Jongryool Kim; Jongse Park; Kiwan Maeng
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation, system behavior characterization, and architecture design choices across multiple state-of-the-art agentic systems.
**Depth:** 4/5 — Provides both concrete methodology (trace-driven simulation framework, token-level dataset) and empirical characterization of agent system behaviors across diverse task types with reproducible evaluation infrastructure.

### [Token Predictors Are Not Planners: Building Physically Grounded Causal Reasoners](https://arxiv.org/abs/2606.01810)
**Source:** arxiv | **Authors:** Zheng Lu; Mingqi Gao; Qinlei Xie; Wanqi Zhong; Hanwen Cui; Heng Cao; Zirui Song; Yifan Yang; Chong L...
**Relevance:** 4/5 — Directly addresses a core capability gap in LLM-based embodied agents: the shift from shallow token prediction to physically grounded causal reasoning for planning and decision-making.
**Depth:** 4/5 — Provides concrete methodology (four-stage annotation pipeline, training recipe for Causal Planner), a diagnostic benchmark (Causal-Plan-Bench with four causal dimensions), empirical results (38.18% → 45.28% gain with scaling law), and identifies specific failure modes in frontier models.

### [Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886)
**Source:** arxiv | **Authors:** Ailiya Borjigin; Igor Stadnyk; Ben Bilski; Maksym Chikita; Dmytro Kyrylenko; Sofiia Pidturkina; Juli...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture design, specifically memory, context management, and tool integration mechanisms that materially affect agent capability and reliability in a financial domain.
**Depth:** 4/5 — Provides detailed methodology (passive knowledge injection, temporal graph memory, invalidation mechanisms) and concrete quantitative evaluation (46,080 baseline-conditioned evaluations with specific latency, token cost, and quality metrics).

### [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961)
**Source:** arxiv | **Authors:** Junqi Liu; Salena Song; Yuhan Wang; Jiawei Mao; Hardy Chen; Xiaoke Huang; Tianhao Qi; Pengfei Guo; Y...
**Relevance:** 4/5 — Directly evaluates LLM-based agent behavior across long-horizon medical research workflows with detailed stage-level analysis, revealing critical limitations in verification and validation—core agent capability gaps.
**Depth:** 4/5 — Provides structured methodology (five-stage workflow framework), concrete quantitative results (48% score drop with single error, stage-level performance breakdown), and systematic error analysis identifying where agents fail, enabling targeted improvement insights.

### [SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning](https://arxiv.org/abs/2606.01991)
**Source:** arxiv | **Authors:** Lichao Wang; Zhaoxing Ren; Tianzhuo Yang; Jiaming Ji; Chi Harold Liu; Yaodong Yang; Juntao Dai
**Relevance:** 4/5 — Directly addresses LLM agent safety and control through tool-use constraints, a core frontier concern for deployed LLM-based agents.
**Depth:** 4/5 — Provides explicit methodology (three-stage training pipeline with world models, dual verifiable rewards, two-tier defense) and concrete benchmark evaluations across three datasets demonstrating quantified safety-utility tradeoffs.

### [Extreme Low-Bit Inference in Reasoning Models: Failure Modes and Targeted Recovery](https://arxiv.org/abs/2606.02011)
**Source:** arxiv | **Authors:** Ekaterina Alimaskina; Darya Rudas; Denis Shveykin; Gleb Molodtsov; Pavel Vasiliev; Aleksandr Beznosi...
**Relevance:** 4/5 — Directly addresses inference efficiency and reliability of reasoning models, a frontier capability that materially affects what LLM-based agents can deploy and sustain.
**Depth:** 4/5 — Provides detailed methodology (FP16 planning, loop rescue detection), concrete quantitative results across benchmarks, and explicit analysis of failure modes in reasoning traces.

### [eMoT: evolving Memory-of-Thought via Symbolic Anchoring and Memory Corrosion](https://arxiv.org/abs/2606.02054)
**Source:** arxiv | **Authors:** Xiang Li; Jiwei Wei; Ke Liu; Yitong Qin; Jinyu Guo; Malu Zhang; Peng Wang; Yang Yang
**Relevance:** 4/5 — Directly addresses core LLM agent reasoning challenges (hallucination, numerical computation, consistency) through a framework that improves multi-step reasoning, a frontier capability requirement for capable agents.
**Depth:** 4/5 — Presents clear methodology (memory corrosion mechanism, symbolic anchoring with Python, consistency refinement) with concrete benchmark results showing substantial improvements over baselines on reasoning tasks.

### [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/abs/2606.02060)
**Source:** arxiv | **Authors:** Jiaming Wang; Ziteng Feng; Jiangtao Wu; Ruihao Li; Qianqian Xie; Yuxiang Ren; He Zhu; Xueming Han; F...
**Relevance:** 4/5 — Directly addresses evaluation and reliability of LLM-based agents through trajectory analysis, methodology for error localization, and benchmarking framework.
**Depth:** 4/5 — Contributes concrete methodology (DRIFT framework for claim-centric auditing), large-scale annotation dataset (TELBench with 2,790 trajectories), and systematic evaluation with quantified improvements up to 30 percentage points.

### [Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning](https://arxiv.org/abs/2606.02132)
**Source:** arxiv | **Authors:** Liuji Chen; Dianxing Tang; Xing Shi; Dingshuo Chen; Qiang Liu; Shu Wu; Liang Wang
**Relevance:** 4/5 — Directly addresses tool use in LLM-based agents, a frontier capability for agentic systems, with clear methodology for learning selective tool deployment.
**Depth:** 4/5 — Presents concrete methodology (EAPO framework with difficulty-aware reward shaping and confidence-aware reweighting) and detailed empirical results across multiple models and benchmarks showing significant accuracy-efficiency trade-offs.

### [Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses](https://arxiv.org/abs/2606.02373)
**Source:** arxiv | **Authors:** Pengcheng Jiang; Zhiyi Shi; Kelly Hong; Xueqiang Xu; Jiashuo Sun; Jimeng Sun; Hammad Bashir; Jiawei ...
**Relevance:** 4/5 — Directly addresses LLM-based agent design by proposing an architecture that separates semantic policy decisions from state management in retrieval agents, with explicit RL training methodology.
**Depth:** 4/5 — Provides concrete architectural innovations (stateful harness components), rigorous RL training approach, and comprehensive benchmarking across eight retrieval tasks with quantified gains (+11.4 points) and transfer generalization analysis.

### [HLL: Can Agents Cross Humanity's Last Line of Verification?](https://arxiv.org/abs/2606.02449)
**Source:** arxiv | **Authors:** Xinhao Song; Su Su; Sirui Song; Hongliang Wu; Wen Shen; Zhihua Wei; Gongshen Liu; Linfeng Zhang; Don...
**Relevance:** 4/5 — Directly evaluates multimodal LLM-based agents' capability to perform real-world tasks through grounded interaction and tool use, exposing limitations in localization, action calibration, and state tracking that constrain agent deployment.
**Depth:** 4/5 — Introduces a controlled benchmark methodology with multiple stressor conditions, evaluates eight frontier multimodal models in closed-loop environments, and provides concrete failure analysis across interaction types that exposes mechanistic gaps in current agent architectures.

### [Beyond One-shot: AI Agents for Learning in Field Experiments](https://arxiv.org/abs/2606.02458)
**Source:** arxiv | **Authors:** Junjie Luo; Ritu Agarwal; Gordon Gao
**Relevance:** 4/5 — Directly addresses tool-augmented LLM-based agents learning from experimental data to autonomously generate interventions, with explicit methodology (DIKW reasoning agents, structured evidence chains) and concrete field-experiment results.
**Depth:** 4/5 — Provides substantial methodological detail on agent architecture (tool augmentation, reasoning framework, evidence chains), comparative evaluation (Human+Chatbot vs. Agentic AI across 693K patient visits), and critical finding that frontier LLMs fail without domain-specific experimental data.

### [AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents](https://arxiv.org/abs/2606.02461)
**Source:** arxiv | **Authors:** Yiheng Shu; Bernal Jim\'enez Guti\'errez; Saisri Padmaja Jonnalagedda; Yuguang Yao; Huan Sun; Yu Su
**Relevance:** 4/5 — Directly addresses continual learning and memory mechanisms in LLM-based agents, a frontier capability gap that affects agent performance and reusability across task streams.
**Depth:** 4/5 — Presents rigorous evaluation methodology (AgentCL framework with controlled compositional task streams), a concrete probing technique (MemProbe), and empirical analysis across multiple domains revealing how memory design affects agent plasticity and transfer.

### [Iteris: Agentic Research Loops for Computational Mathematics](https://arxiv.org/abs/2606.02484)
**Source:** arxiv | **Authors:** Leheng Chen; Zihao Liu; Wanyi He; Bin Dong
**Relevance:** 4/5 — Directly addresses LLM-based agentic systems applied to research tasks, demonstrating agent reasoning, planning, and iterative problem-solving capabilities on frontier computational problems.
**Depth:** 4/5 — Provides concrete methodology for agentic research loops (numerical experimentation, adversarial construction, proof drafting) with verified case study results on open mathematical problems, showing both capabilities and human-validation requirements.

### [ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents](https://arxiv.org/abs/2606.02568)
**Source:** arxiv | **Authors:** Yuxing Lu; Yushuhong Lin; Wenqi Shi; J. Ben Tamo; Xukai Zhao; Jinzhuo Wang; May Dongmei Wang
**Relevance:** 4/5 — Directly evaluates LLM-based agents in a complex, sequential decision-making task with explicit methodology for probing information-gathering behavior and reasoning under uncertainty.
**Depth:** 4/5 — Provides concrete evaluation framework with specific metrics (decision F1, process vs. outcome quality), real-world EHR data, multi-stage reasoning pipeline, and empirical results across seven models revealing failure modes (information-acquisition gaps, redundant queries).

### [World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](https://arxiv.org/abs/2606.00133)
**Source:** arxiv | **Authors:** Arif Hassan Zidan; Yi Pan; Hanqi Jiang; Ruiyu Yan; Wei Ruan; Zihao Wu; Lifeng Chen; Weihang You; Xin...
**Relevance:** 4/5 — World models are a foundational architecture for LLM-based agents' planning and reasoning capabilities, and the survey explicitly covers language-augmented multimodal systems and chain-of-thought reasoning integration.
**Depth:** 4/5 — This is a comprehensive taxonomy paper covering multiple architectural families, reasoning mechanisms, methodologies, and applications with concrete references to milestone systems (PlaNet, Dreamer, MuZero, Sora, Genie) and identified technical challenges.

### [BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding](https://arxiv.org/abs/2606.00144)
**Source:** arxiv | **Authors:** Liang He; Jingbo Wen; Qishi Zhan; Yixiong Chen; Kangning Cui; Qizhen Lan; Xilu Wang
**Relevance:** 4/5 — Speculative decoding is a frontier inference optimization that directly impacts LLM agent deployment efficiency and latency, enabling practical agent deployment in resource-constrained settings.
**Depth:** 4/5 — The paper presents concrete methodology (multi-view sparse training with acceptance-aware loss) and substantial experimental results (6.55x speedup at 4K context) addressing a real sparse/full mismatch problem in production inference.

### [Learning to Construct Practical Agentic Systems](https://arxiv.org/abs/2606.00189)
**Source:** arxiv | **Authors:** Aditya Kumar; Zhihan Lei; Jerry Yan; Joshua W. Momo; Lauhitya Reddy; Rafael Enrique Cabrera Jimenez;...
**Relevance:** 4/5 — Directly addresses LLM-based agent design and optimization with concrete methodology for practical agentic systems, including pseudo-tools, workflow construction, and learning methods.
**Depth:** 4/5 — Provides substantial methodology (modular framework with pseudo-tools, fixed workflow optimization, multi-objective learning) and concrete results (comparison of hand-engineered vs. dynamically-planned systems, cost-quality tradeoffs).

### [BAGEN: Are LLM Agents Budget-Aware?](https://arxiv.org/abs/2606.00198)
**Source:** arxiv | **Authors:** Yuxiang Lin; Zihan Wang; Mengyang Liu; Yuxuan Shan; Longju Bai; Junyao Zhang; Xing Jin; Boshan Chen;...
**Relevance:** 4/5 — Directly addresses a frontier agent capability gap (budget awareness) with systematic evaluation and training methods across multiple frontier models.
**Depth:** 4/5 — Provides formal definitions of budget-awareness, comprehensive empirical evaluation across five frontier agents, concrete failure patterns, and demonstrates trainable improvements via SFT+RL with token savings of 28-64%.

### [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/abs/2606.00206)
**Source:** arxiv | **Authors:** Sanae Lotfi; Polina Kirichenko; Steven Li; Zechun Liu
**Relevance:** 4/5 — Directly addresses reasoning model behavior under quantization, a deployment constraint affecting agent capabilities, with concrete methodology for diagnosing and fixing reasoning failures.
**Depth:** 4/5 — Provides mechanistic analysis via token-level KL divergence and entropy correlation, identifies a specific failure mode (overthinking), and demonstrates a validated training-free intervention across multiple model scales and quantization methods.

### [ARCA: Adapter-Residual Credit Assignment When Token Signals Degenerate](https://arxiv.org/abs/2606.00257)
**Source:** arxiv | **Authors:** Rodney Lafuente-Mercado
**Relevance:** 4/5 — Directly addresses a frontier problem in LLM agent training: token-level credit assignment for RL-based LLM fine-tuning, which is foundational for agent learning and policy optimization.
**Depth:** 4/5 — Provides rigorous methodology (formalization of degeneracy under LoRA, concentration diagnostics), concrete mechanism (adapter-residual measurement), empirical validation (MATH/Qwen experiments), and identifies a structural failure mode in existing approaches.

### [COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://arxiv.org/abs/2605.31264)
**Source:** arxiv | **Authors:** Tianyi Zhou; Dongrui Liu; Leitao Yuan; Jing Shao; Xia Hu
**Relevance:** 4/5 — Directly addresses LLM agent capabilities through a system for encoding expertise, memory, and behavioral constraints—core infrastructure for person-grounded agents.
**Depth:** 3/5 — Presents a concrete end-to-end workflow with artifact contracts, correction lifecycles, and deployment surfaces, though the paper emphasizes system design and adoption metrics over algorithmic methodology or rigorous evaluation.

### [Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation](https://arxiv.org/abs/2605.31278)
**Source:** arxiv | **Authors:** Gr\'egoire Martinon; Ibrahim Merad; Mohammed Raki
**Relevance:** 4/5 — Directly addresses evaluation methodology for agentic systems, a frontier capability question for LLM-based agents, with concrete methodology and empirical validation.
**Depth:** 3/5 — Solid methodological contribution unifying prediction-powered inference techniques with practical implementation and decision framework, though primarily an engineering/tooling contribution rather than advancing core agent or model capabilities.

### [Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration](https://arxiv.org/abs/2605.31365)
**Source:** arxiv | **Authors:** Weile Chen; Bingchen Miao; Qifan Yu; Wendong Bu; Guoming Wang; Wenqiao Zhang; Shengyu Zhang; Junchen...
**Relevance:** 4/5 — Directly addresses LLM-based web agents with focus on autonomous learning, adaptation mechanisms, and self-improvement through exploration—core frontier topics in agent capability research.
**Depth:** 3/5 — Provides concrete methodology (adversarial roles framework, SCALE-Hop strategy) and evaluates on large-scale dataset with generalization results, though the core mechanisms are somewhat incremental extensions of existing MLLM agent architectures.

### [OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning](https://arxiv.org/abs/2605.30736)
**Source:** arxiv | **Authors:** Zhenghua Bao; Fengya Tian; Chris Zhang; Zhenjun Chen; Xile Ma; Yi Shi
**Relevance:** 4/5 — OrcaRouter directly addresses a key operational challenge for LLM-based agent systems: efficient model selection and routing at inference time, which materially affects what multi-model agent systems can achieve.
**Depth:** 3/5 — The work presents a concrete methodology combining contextual bandits with hybrid offline-online learning, includes production results (RouterArena leaderboard ranking, cost-accuracy tradeoff), and identifies a practical problem, but the core innovation is primarily algorithmic application rather than foundational capability advancement.

### [Model-Native Computing Architecture: Envisioning Future System Architecture Through the Lens of Computer Architecture](https://arxiv.org/abs/2606.00288)
**Source:** arxiv | **Authors:** Hai Lin
**Relevance:** 4/5 — Directly addresses LLM-based agent system architecture, frameworks, memory management, and multi-agent coordination—core frontier concerns for how agents are built and deployed.
**Depth:** 3/5 — Proposes a conceptual framework (ICAM) with explicit design principles and laws grounded in computer architecture analogy, validated against published system-level data, though acknowledged as a survey without new experiments.

### [Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents](https://arxiv.org/abs/2606.00476)
**Source:** arxiv | **Authors:** Yufeng Wang
**Relevance:** 4/5 — Directly addresses agent faithfulness—whether LLM agents act on their stated reasoning—a core capability concern for reliable agent deployment.
**Depth:** 3/5 — Provides controlled methodology (Texas Poker simulator with verifiable reference actions) and systematic decomposition of faithfulness gaps into reasoning-conclusion and conclusion-action steps with empirical findings on their opposite behaviors.

### [Before the Model Learns the Bug:Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066)
**Source:** arxiv | **Authors:** Jaideep Ray
**Relevance:** 4/5 — Directly addresses a frontier capability challenge for LLM-based agents: verifier robustness in RLVR systems, which enables reliable reward signals for agentic reasoning and tool use.
**Depth:** 3/5 — Provides concrete methodology (verifier-fuzzing framework with specific metrics) and identifies a real failure mode in agent training, but focuses on testing/validation rather than advancing core agent capabilities or model architectures.

### [CAREAgent: Clinical Agent with Structured Reasoning and Tool-Integrated for Order Generation](https://arxiv.org/abs/2606.01094)
**Source:** arxiv | **Authors:** Ruihui Hou; Ziyue Huai; Chennuo Zhang; Ziyan Liu; Siran Zhao; Yao Yu; Jie Zhai; Tong Ruan
**Relevance:** 4/5 — Directly addresses LLM-based agent design for a specialized domain (clinical), including structured reasoning, tool integration, and agentic training methodology.
**Depth:** 3/5 — Provides concrete methodology (two-stage data construction, SFT + RL with multi-dimensional rewards) and benchmark results (5.05% F1 improvement), though the contribution is domain-specific rather than advancing frontier agent capabilities.

### [Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery](https://arxiv.org/abs/2606.01316)
**Source:** arxiv | **Authors:** Zhe Zhao; Haibin Wen; Yingcheng Wu; Jiaming Ma; Yifan Wen; Jinglin Jian; Jiacheng Ge; Xiangru Tang; ...
**Relevance:** 4/5 — Directly addresses multi-agent coordination and reasoning for scientific discovery, core to frontier LLM-agent capabilities like negotiation, task allocation, and collaborative problem-solving.
**Depth:** 3/5 — Presents concrete EACN protocol methodology and empirical validation across two structurally distinct scientific tasks, though the cases serve as proof-of-concept rather than comprehensive benchmark evaluation.

### [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/abs/2606.01365)
**Source:** arxiv | **Authors:** Xianyou Li; Weiran Yan; Yichao Wu; Penghao Liang; Mengwei Yuan; Jianan Liu; Jing Yang
**Relevance:** 4/5 — Directly addresses multi-agent LLM system reliability and efficiency—core operational concerns for deployed agents—through a failure diagnostics framework with concrete methodology and empirical evaluation.
**Depth:** 3/5 — Solid contribution with systematic failure-mode mapping, online signal identification, and evaluation on 165 traces with quantified results; methodology is clear but framework is primarily diagnostic rather than introducing new agent capabilities or training methods.

### [SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes](https://arxiv.org/abs/2606.01912)
**Source:** arxiv | **Authors:** Kuan Li; Shuo Zhang; Huacan Wang; Fangzhou Yu; Zecheng Sheng; Yi Gu; Weipeng Ming; Lei Xue; Chen Liu...
**Relevance:** 4/5 — Directly evaluates LLM-based agents on reasoning, planning, and tool use in a realistic environment with concrete methodology and benchmarking across multiple task categories and complexity levels.
**Depth:** 3/5 — Provides solid empirical contribution through a comprehensive benchmark with 1,100 tasks and clear findings on frontier model weaknesses (automation scheduling, ambiguity handling, personalization), but lacks novel methodology for improving agent capabilities.

### [BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning](https://arxiv.org/abs/2606.02109)
**Source:** arxiv | **Authors:** Shannon Serrao; Soumitra Chatterjee; Dorina Strori; Abhishek Sharma; Nathan Miller
**Relevance:** 4/5 — Directly addresses evaluation and deployment of LLM-based agentic reasoning pipelines in enterprise settings, with concrete methodology for assessing agent behavior alongside task execution.
**Depth:** 3/5 — Provides concrete evaluation metrics (Hybrid-EX, agent behavior suite) with validation results (Cohen's kappa, balanced accuracy), though contributions are primarily engineering and refinement of existing assessment frameworks rather than foundational architectural insights.

### [MOC: Multi-Order Communication in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2606.02359)
**Source:** arxiv | **Authors:** Yao Guan; Lin Wang; Zhihu Lu; Ziyi Wang; Wenzhu Yan; Qiang Duan
**Relevance:** 4/5 — Directly addresses a core LLM-based multi-agent challenge: inter-agent communication mechanisms and message optimization, which materially affect agent coordination and task performance.
**Depth:** 3/5 — Provides clear methodology (multi-order evidence construction, semantic-topological merging algorithm) and concrete experimental results across six datasets with multiple LLM backbones, demonstrating consistent performance gains and communication cost reduction.

### [MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation](https://arxiv.org/abs/2606.02470)
**Source:** arxiv | **Authors:** Wenhao Wang; Peizhi Niu; Gongyi Zou; Xiyuan Yang; Jingxing Wang; Haoting Shi; Yaxin Du; Jingyi Chai;...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation on tool use and personalized applications, a core frontier capability that affects real-world deployment of agent systems.
**Depth:** 3/5 — Provides concrete benchmark results showing SOTA agent limitations on personalized MCP tools, though the contribution is primarily empirical benchmarking rather than new agent methodology or mechanisms.

### [Bridging the Last Mile of Time Series Forecasting with LLM Agents](https://arxiv.org/abs/2606.02497)
**Source:** arxiv | **Authors:** Yuhua Liao; Zetian Wang; Qiangqiang Nie; Zhenhua Zhang
**Relevance:** 4/5 — Directly addresses LLM-based agent design for a real-world task, demonstrating tool use, memory, reasoning trajectories, and safety constraints—all core agent capabilities.
**Depth:** 3/5 — Presents concrete methodology (unified workspace, tool invocation, map-reduce decomposition, memory bank, structural constraints) and real-world case studies, though lacks quantitative benchmark results or formal evaluation metrics.


## Worth knowing (28 items)

_On-criterion but lower depth, or peripheral relevance._

### [PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges](https://arxiv.org/abs/2605.30803)
**Source:** arxiv | **Authors:** Swastik Roy; Rajkumar Pujari; Tharindu Kumarage; Charith Peris; Rahul Gupta; Anna Rumshisky; Pradeep...
**Relevance:** 3/5 — Work on LLM evaluation methodology is adjacent to agent development but not central to agent reasoning, planning, tool use, or capability emergence that directly enables agents.
**Depth:** 4/5 — Solid methodology with concrete audit framework, repair operations, and quantified results (68.6% accuracy, 46.4%→36.0% exploit reduction) addressing real measurement problems in LLM evaluation.

### [CSULoRA: Closest Safe Update Low-Rank Adaptation](https://arxiv.org/abs/2605.30640)
**Source:** arxiv | **Authors:** Oleksandr Marchenko Breneur; Adelaide Danilov; Aria Nourbakhsh; Salima Lamsiyah
**Relevance:** 3/5 — Addresses safety alignment of LLMs during fine-tuning, which matters for reliable agent deployment, but is not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Presents a concrete closed-form method for safety-preserving adaptation with clear methodology (subspace decomposition and penalized optimization) and adversarial fine-tuning experiments showing substantial attack reduction.

### [Eigenvectors of Experts are Training-free Non-collapsing Routers](https://arxiv.org/abs/2605.30992)
**Source:** arxiv | **Authors:** Giang Do; Hung Le; Truyen Tran
**Relevance:** 3/5 — SMoE routing improvements affect LLM capabilities and efficiency, relevant to agent model infrastructure, but not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides clear methodology (SVD-based routing using spectral properties), theoretical analysis of expert collapse, and extensive empirical evaluation across language and vision tasks with public implementation.

### [Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing](https://arxiv.org/abs/2605.31367)
**Source:** arxiv | **Authors:** Erwan Fagnou; Paul Caillon; Blaise Delattre; Alexandre Allauzen
**Relevance:** 3/5 — Work on token mixing architectures affects frontier model capabilities and efficiency, relevant to agent deployment and reasoning scale, but is not directly about agent systems or major capability emergence.
**Depth:** 4/5 — Provides unified theoretical framework with principled expressivity-complexity trade-offs, structured recurrence patterns with provable guarantees, and empirical validation on language modeling tasks.

### [Assign and Add: A Mechanistic Study of Compositional Arithmetic](https://arxiv.org/abs/2605.31497)
**Source:** arxiv | **Authors:** Brady Exoo; Alberto Bietti; John Sous
**Relevance:** 3/5 — Mechanistic understanding of compositional generalization in transformers is foundational for agent reasoning and planning capabilities, but this work uses toy arithmetic tasks rather than directly studying agent behaviors.
**Depth:** 4/5 — Strong mechanistic analysis with three-phase learning dynamics, theoretical framework explaining compositionality emergence, and empirical investigation of how internal MLP modules are reused across compositions.

### [Threshold-Based Exclusive Batching for LLM Inference](https://arxiv.org/abs/2606.00516)
**Source:** arxiv | **Authors:** Weifang Zhang; Yuzhou Nie; Bowen Pang; Guangrui Ma; Shining Wu
**Relevance:** 3/5 — LLM inference optimization is infrastructure for agents but not directly about agent reasoning, planning, or capabilities; it's a scheduling mechanism that enables deployment efficiency.
**Depth:** 4/5 — Provides closed-form analytical conditions, concrete throughput measurements across hardware configurations, and a working hybrid scheduler with clear methodology and empirical validation.

### [KACE: Knowledge-Adaptive Context Engineering for Mathematical Reasoning](https://arxiv.org/abs/2606.00532)
**Source:** arxiv | **Authors:** Jayant Parashar; Suchendra M. Bhandarkar
**Relevance:** 3/5 — KACE addresses context/memory management for LLM reasoning, a capability-enabling technique relevant to agent performance, but focuses narrowly on mathematical reasoning without explicit agent architecture or deployment.
**Depth:** 4/5 — The work provides clear methodology (epistemic tree construction, tiered self-consistency, difficulty-domain stratification) with concrete empirical results (62.2% on AIME 2025, 10.4-point gains) and identifies real limitations of prior context approaches.

### [AXIOM: A Trust-First Neuro-Symbolic Execution Architecture for Verifiable Mathematical Reasoning](https://arxiv.org/abs/2606.00671)
**Source:** arxiv | **Authors:** Alessio Bruno
**Relevance:** 3/5 — Neuro-symbolic reasoning is tangentially relevant to LLM-agent capabilities (tool use, verification), but the work centers on a narrow domain (mathematical reasoning with symbolic backends) rather than general agent reasoning, planning, or deployment.
**Depth:** 4/5 — The paper presents substantive methodology (trust-first architecture, routing discipline, regression prevention via LOST_CORRECT scan) and concrete production results (94.36% correctness, 100% trust on parseable inputs, ~30k queries deployed), with clear transferable operational principles.

### [Mitigating Hallucinations in Large Language Models Via Decoder Layer Skipping](https://arxiv.org/abs/2606.00819)
**Source:** arxiv | **Authors:** Hanze Li; Jinhao You; Yichen Guo; Kai Tang; Shuangyang Xie; Xiande Huang
**Relevance:** 3/5 — Hallucination mitigation is foundational to agent reliability, but this work focuses on decoding-layer mechanics rather than agent-specific reasoning, planning, or tool use.
**Depth:** 4/5 — The paper provides clear methodology (layer-wise analysis, driftance metric based on gradient direction reversal, partial aggregation), theoretical grounding (gradient descent equivalence), and extensive empirical validation across models and benchmarks.

### [Subliminal Learning is a LoRA Artifact](https://arxiv.org/abs/2606.00831)
**Source:** arxiv | **Authors:** Todd Nief; Harvey Yiyun Fu; Mark Muchane; Ari Holtzman
**Relevance:** 3/5 — Addresses model behavior and finetuning mechanisms relevant to agent training and capability transmission, but focuses on a narrow artifact rather than core agent capabilities or frontier model releases.
**Depth:** 4/5 — Provides rigorous methodology (LoRA rank experiments, context ablations, localization analysis) and concrete results explaining an unexpected phenomenon, with clear limitations of prior work motivating the investigation.

### [Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995)
**Source:** arxiv | **Authors:** Camila Blank; Agam Bhatia; Senthooran Rajamanoharan; Arthur Conmy; Neel Nanda
**Relevance:** 3/5 — The work investigates mechanistic aspects of how models acquire behavioral traits through fine-tuning, which relates to model capability understanding and control relevant to agent behavior, but does not directly address agent reasoning, planning, or tool use.
**Depth:** 4/5 — The paper provides substantive mechanistic methodology (steering vector identification, adaptive optimizer analysis) and concrete experimental results across models demonstrating how subliminal learning operates, with clear explanations of why prior observations occur.

### [SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment](https://arxiv.org/abs/2606.02530)
**Source:** arxiv | **Authors:** Hao Li; Jingkun An; Zijun Song; Pengyu Zhu; Rui Li; Hao Wang; Wendi Feng; Yesheng Liu; Lijun Li; Jin...
**Relevance:** 3/5 — Safety alignment is relevant to agent deployment, but this paper focuses on capability-safety trade-offs in base model training rather than agent reasoning, planning, or tool use.
**Depth:** 4/5 — The work presents concrete methodology (activation steering, safety token selection, localized KL penalty) with thorough experimental validation across multiple benchmarks and models.

### [RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning with Alleviated Forgetting](https://arxiv.org/abs/2606.00147)
**Source:** arxiv | **Authors:** Yuduo Li; Xiaofeng Shi; Qian Kou; Longbin Yu; Hua Zhou
**Relevance:** 3/5 — Fine-tuning methodology that preserves general capabilities is relevant to agent robustness, but the work is primarily about SFT/distillation technique rather than agent capabilities or frontier model development.
**Depth:** 4/5 — The paper provides clear methodology (self-conditioned rewriting, on-policy distillation, adaptive loss balancing) with concrete benchmark results across multiple domains and backbones, demonstrating solid technical contribution.

### [A Pre-Training Analogue of Grokking in Language Models: Tracing Delayed Grammatical Generalization](https://arxiv.org/abs/2606.00230)
**Source:** arxiv | **Authors:** Sherin Muckatira; Namrata Shivagunde; Vijeta Deshpande; Anna Rumshisky
**Relevance:** 3/5 — Studies a frontier capability phenomenon (grokking/delayed generalization) in LLM pre-training with methodological rigor, but focuses on grammatical understanding rather than agent-relevant capabilities like reasoning, planning, or tool use.
**Depth:** 4/5 — Proposes a novel exposure-based framework for studying grokking during pre-training, provides concrete analysis across five grammatical phenomena with mechanistic insights (concept vectors, attention concentration), and identifies limitations of prior supervised grokking studies.

### [EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs](https://arxiv.org/abs/2605.30637)
**Source:** arxiv | **Authors:** Yuzhang Xie; Keqi Han; Yunpeng Xiao; Hejie Cui; Guanchen Wu; Ziyang Zhang; Kai Shu; Jiaying Lu; Xiao...
**Relevance:** 3/5 — Evaluates LLM capabilities on clinical decision-making tasks (diagnosis, treatment, prognosis), which is relevant to understanding frontier model capabilities, but focuses on benchmark construction and evaluation rather than agent reasoning, planning, or tool use mechanisms.
**Depth:** 3/5 — Provides solid methodology (EHR-LLM-KB pipeline, template instantiation, KB verification) and substantial empirical results (1M QA items, 30+ model benchmarks with detailed analysis), but the contribution is primarily in benchmark design and evaluation rather than advancing agent architectures or frontier model capabilities.

### [HypoAgent: An Agentic Framework for Interactive Abductive Hypothesis Generation over Knowledge Graphs](https://arxiv.org/abs/2605.31370)
**Source:** arxiv | **Authors:** Yisen Gao; Yixi Cai; Tianshi Zheng; Jiaxin Bai; Yangqiu Song
**Relevance:** 3/5 — HypoAgent is an LLM-based agent framework addressing interactive reasoning and dialogue grounding over knowledge graphs, which touches agent capabilities (multi-turn dialogue, intent recognition, tool use via KG probing) but operates in a specialized domain (abductive reasoning) rather than advancing frontier model capabilities or general agent paradigms.
**Depth:** 3/5 — The work presents clear methodology (three-agent decomposition: intent recognition, hypothesis generation, root cause analysis) and experimental evaluation on domain-specific KGs, but the contribution is primarily architectural application of existing LLM capabilities rather than novel mechanisms or fundamental insights into agent reasoning.

### [Federated Variational Preference Alignment with Gumbel-Softmax Prior for Personalized User Preferences](https://arxiv.org/abs/2605.30873)
**Source:** arxiv | **Authors:** Jabin Koo; Hoyoung Kim; Minwoo Jang; Jungseul Ok
**Relevance:** 3/5 — Addresses LLM alignment and preference modeling with federated learning, which is relevant to agent training and safety, but federated preference personalization is not central to frontier agent capabilities or reasoning.
**Depth:** 3/5 — Presents solid technical methodology (Gumbel-Softmax prior, orthogonal loss, federated mixture prior) and experimental validation on HH-RLHF, but focuses on a specific alignment problem rather than core agent reasoning or capability emergence.

### [Annealed Softmax Greedy in Many-Armed Bayesian Bandits](https://arxiv.org/abs/2605.31034)
**Source:** arxiv | **Authors:** William Overman; Mohsen Bayati
**Relevance:** 3/5 — The paper analyzes policy update mechanisms (softmax greedy with annealing) used in RLVR and GRPO, which are training methods for LLM agents, but the theoretical contribution is narrow (many-armed bandits) rather than directly addressing agent capabilities or frontier model training.
**Depth:** 3/5 — The work provides rigorous theoretical analysis with concrete regret bounds and identifies a structural analogy to RLVR, but the insights are limited to a stylized bandit setting and do not yield new methodologies or empirical results for agent training at scale.

### [Emergent Collaborative Deliberation in Multi-Model AI Systems: A BFT-Derived Protocol for Epistemic Synthesis](https://arxiv.org/abs/2606.00005)
**Source:** arxiv | **Authors:** VD Doske
**Relevance:** 3/5 — Multi-model deliberation is a coordination mechanism for LLM-based systems with agent-like reasoning properties, but the work emphasizes epistemic analysis and bias measurement rather than agent capabilities, planning, or tool use that would make it central to frontier agent research.
**Depth:** 3/5 — The paper provides a structured protocol with clear methodology (BFT-derived framework, persona engineering, validation approach), concrete quantitative results across 1,478 sessions with reproducibility metrics, and identifies specific limitations of RLHF alignment, but lacks focus on how these insights enable or constrain agent decision-making or deployment.

### [Deliberative Curation: A Protocol for Multi-Agent Knowledge Bases](https://arxiv.org/abs/2606.00007)
**Source:** arxiv | **Authors:** Steven Johnson
**Relevance:** 3/5 — Addresses multi-agent coordination and governance in shared knowledge systems, relevant to agent deployment and evaluation, but focused on curation protocol rather than core agent reasoning or frontier model capabilities.
**Depth:** 3/5 — Presents a formal protocol with three governance layers and empirical validation through agent-based simulation with clear ablation analysis, but the contribution is primarily in governance mechanism design rather than advancing fundamental agent capabilities or methodology.

### [A Multi-AI-agent Framework Enabling End-to-end Finite Element Analysis for Solid Mechanics Problems](https://arxiv.org/abs/2606.00138)
**Source:** arxiv | **Authors:** Titu Ranjan Sarker; Muhammed Jawaad Zulqernine; Ling Yue; Shaowu Pan; Chenxi Wang; Shiyao Lin
**Relevance:** 3/5 — Multi-agent LLM system directly relevant to agent architecture and tool use, but domain-specific application (FEA) with limited insight into frontier agent capabilities or training methods.
**Depth:** 3/5 — Solid engineering contribution with clear multi-agent orchestration methodology and quantitative results (86% success on 50 problems), but limited novelty in agent reasoning/planning mechanisms or analysis of failure modes.

### [Efficient Test-time Inference for Generative Planning Models](https://arxiv.org/abs/2606.00618)
**Source:** arxiv | **Authors:** Robert Gieselmann; Mihai Samson; Federico Pecora; Jeremy L. Wyatt
**Relevance:** 3/5 — Work on planning and inference optimization is adjacent to agent capabilities but focuses on classical search integration rather than LLM-based reasoning or frontier model capabilities.
**Depth:** 3/5 — Solid methodological contribution with concrete algorithmic innovations (OCL framework integration, exploration control) and empirical results across planning domains, though not addressing core LLM agent mechanisms.

### [Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs](https://arxiv.org/abs/2606.00642)
**Source:** arxiv | **Authors:** Yu-An Lu; Ci-Yang Tsai; Yu-Lin Tsai; Raluca Ada Popa; Chia-Mu Yu
**Relevance:** 3/5 — Directly addresses reasoning traces and their distillation in LLMs, which is relevant to agent capability transfer, but focuses on a security/privacy analysis rather than agent architecture or deployment.
**Depth:** 3/5 — Presents a concrete methodology (Reasoning Exposure Prompting) with empirical validation across models and datasets, demonstrating both mechanism and quantitative results on reasoning signal preservation.

### [TriLens: Per-Layer Logit-Lens Entropy for White-Box Hallucination Detection](https://arxiv.org/abs/2606.01033)
**Source:** arxiv | **Authors:** Bohan Yang; Yijun Gong; Zhi Zhang; Ge Zhang; Wenpeng Xing; Meng Han
**Relevance:** 3/5 — Hallucination detection is a frontier capability concern for LLM agents, but this work focuses on detection methodology rather than enabling agent capabilities or model training advances.
**Depth:** 3/5 — Solid methodology with concrete mechanism (per-layer logit-lens entropy trajectories) and evaluation across benchmarks, but represents an incremental detector rather than advancing agent reasoning or model capabilities.

### [TravelEval: A Comprehensive Benchmarking Framework for Evaluating LLM-Powered Travel Planning Agents](https://arxiv.org/abs/2606.01046)
**Source:** arxiv | **Authors:** Weiyi Chen; Shuaixiong Wang; Ziyun Gao; Kaichun Hu; Wangze Ni; Shimin Di; Chen Jason Zhang; Lei Chen
**Relevance:** 3/5 — TravelEval is a benchmarking framework for LLM-based agents (travel planning), which is on-topic for agent evaluation, but lacks frontier methodology or capability insights beyond domain-specific evaluation design.
**Depth:** 3/5 — The work provides solid concrete methodology (six-dimensional evaluation framework, simulation-based testing with realistic data) and empirical findings (LLMs struggle with spatio-temporal reasoning, agentic strategies show inconsistent gains), but these insights are specific to travel planning rather than advancing general agent architecture or model capabilities.

### [Diagnosing LLM Arbitration Behavior over Pre-evidence Epistemic States in RAG-based Fact-Checking](https://arxiv.org/abs/2606.01120)
**Source:** arxiv | **Authors:** Yuxi Sun; Wenbo Shang; Wei Gao; Xin Huang; Jing Ma
**Relevance:** 3/5 — Addresses LLM verifier behavior in RAG-based fact-checking (agent capability), but diagnostic evaluation rather than core agent reasoning/planning/tool-use.
**Depth:** 3/5 — Introduces PAVE testbed with clear methodology for stratifying epistemic states and proposes JSD-based test-time arbitration with experimental validation across models, but contribution is evaluation framework rather than novel capability or training method.

### [Algorithmic algorithm development with LLMs: A Case Study on LLM-Usage for Contraction Order Optimization in Tensor Networks](https://arxiv.org/abs/2606.01975)
**Source:** arxiv | **Authors:** Fabian Hoppe; Melven R\"ohrig-Z\"ollner; Philipp Knechtges
**Relevance:** 3/5 — This work studies LLM-based agents for algorithm development with verifier-guided evolutionary coding, which touches on agent reasoning and tool use, but the application domain (tensor network optimization) is domain-specific rather than representative of frontier agent capabilities.
**Depth:** 3/5 — The paper provides concrete methodology (evolutionary coding agents with verifier guidance) and evaluation results, but the contribution is largely a case study application rather than advancing frontier LLM capabilities or fundamental agent reasoning mechanisms.

### [RASER: Recoverability-Aware Selective Escalation Router for Multi-Hop Question Answering](https://arxiv.org/abs/2606.02488)
**Source:** arxiv | **Authors:** Yuyang Li; Zihe Yan; Tobias K\"afer
**Relevance:** 3/5 — RASER addresses routing and decision-making in LLM-based multi-hop QA systems, which is relevant to agent planning and resource efficiency, but is narrowly scoped to QA rather than general agent capabilities.
**Depth:** 3/5 — The paper provides clear methodology (router design based on six features, cost-accuracy trade-offs) and concrete results across benchmarks, but the contribution is primarily an optimization technique rather than advancing fundamental agent capabilities or model understanding.

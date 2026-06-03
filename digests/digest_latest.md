# AI digest — 2026-06-03

Rolling 7-day window. Generated automatically.

---

## Read deeply (160 items)

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

### [Inducing Reasoning Primitives from Agent Traces](https://arxiv.org/abs/2606.02994)
**Source:** arxiv | **Authors:** Zhihan Lei; Jiarui Yan; Joshua Momo; William W. Cohen
**Relevance:** 5/5 — Directly addresses LLM agent reasoning and tool use by introducing a method to extract and formalize recurring reasoning patterns from agent traces into reusable primitives.
**Depth:** 4/5 — Presents clear methodology (clustering ReAct traces, converting moves to pseudo-tools with natural-language specs), concrete quantitative results (+44pp, +30pp, +22pp improvements), and explicit comparison against baselines including expert decompositions and prior methods.

### [SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale](https://arxiv.org/abs/2606.03056)
**Source:** arxiv | **Authors:** Tong Bai; Zhenglin Wan; Pengfei Zhou; Xingrui Yu; Wangbo Zhao; Yang You; Ivor W. Tsang
**Relevance:** 5/5 — Directly addresses LLM agent skill selection and tool use at scale through a novel structural retrieval mechanism, a core frontier challenge for deploying capable agents.
**Depth:** 4/5 — Provides clear methodology (typed DAG modeling with propose-then-commit protocol), concrete benchmark results (+12.8/+8.6 points over baselines on ALFWorld/SkillsBench), and isolable mechanisms explaining robustness gains.

### [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108)
**Source:** arxiv | **Authors:** Guhong Chen; Yingcheng Shi; Yongbin Li; Binhua Li; Xander Xu; Hu Wei; Shiwen Ni; Min Yang; Jieping Y...
**Relevance:** 5/5 — Directly addresses autonomous LLM agent training through co-evolution of policies and training harnesses, a frontier methodology for improving agentic RL systems across reasoning, code generation, and software engineering tasks.
**Depth:** 4/5 — Presents novel methodology (joint policy-harness co-evolution with diagnostic feedback loops), concrete results across three domains with comparisons to human-engineered baselines, and trajectory analysis revealing mechanistic insights about strategy retention and invalid branch prevention.

### [LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks](https://arxiv.org/abs/2606.03303)
**Source:** arxiv | **Authors:** Po-Nien Kung; Linfeng Song; Dawsen Hwang; Jinsung Yoon; Chun-Liang Li; Simone Severini; Mirek Ol\v{s...
**Relevance:** 5/5 — LEAP is a core LLM-based agent framework for formal theorem proving that directly addresses how foundation models can be enhanced with agentic mechanisms (iterative refinement, tool interaction, decomposition) to tackle complex reasoning tasks.
**Depth:** 4/5 — The paper provides detailed methodology on bridging informal and formal reasoning through continuous compiler interaction, introduces a rigorous new benchmark (Lean-IMO-Bench), and demonstrates substantial empirical gains (70% solve rate vs <10% baseline) plus research-level autonomous formalization.

### [What Makes Interaction Trajectories Effective for Training Terminal Agents?](https://arxiv.org/abs/2606.03461)
**Source:** arxiv | **Authors:** Sidi Yang; Chaofan Tao; Jierun Chen; Tiezheng Yu; Ruoyu Wang; Yuxin Jiang; Yiming Du; Wendong Xu; Ji...
**Relevance:** 5/5 — Directly addresses LLM-based agent training through post-training methodology, focusing on how interaction trajectories and environment-grounded supervision enable agent capability emergence.
**Depth:** 4/5 — Provides clear methodology (Environment-Grounded Supervision, Harness Engineering framework), concrete empirical results (24.3% score with 15.3k trajectories vs 30x prior data), and identifies a pedagogical paradox that challenges assumptions about teacher agent quality.

### [EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)
**Source:** arxiv | **Authors:** Zherui Yang; Fan Liu; Yansong Ning; Hao Liu
**Relevance:** 5/5 — Directly addresses LLM-based agent architecture with skill learning, context management, and multi-agent training—core frontier capabilities for autonomous data science agents.
**Depth:** 4/5 — Provides explicit methodology (ASA and ACC mechanisms, two-stage training scheme), theoretical justification (hierarchical design reducing tool-selection error, information bottleneck alignment), and concrete benchmark results (28.9% improvement across four datasets).

### [Multi$^2$: Hierarchical Multi-Agent Decision-Making with LLM-Based Agents in Interactive Environments](https://arxiv.org/abs/2606.03698)
**Source:** arxiv | **Authors:** Sangeun Park; Minhae Kwon
**Relevance:** 5/5 — Directly addresses core LLM agent challenges (long-horizon planning, objective drift, hierarchical decision-making) with a novel architectural decomposition and training methodology.
**Depth:** 4/5 — Provides explicit methodology (hierarchical role separation with SFT for planning and offline-to-online RL for execution), concrete benchmarking against baselines, and releases three new hierarchical datasets to advance the field.

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

### [Thinking Past the Answer: Evaluating Harmful Overthinking in Large Reasoning Models](https://arxiv.org/abs/2606.02835)
**Source:** arxiv | **Authors:** Simone Caldarella; Davide Talon; Rahaf Aljundi; Elisa Ricci; Massimiliano Mancini
**Relevance:** 4/5 — Directly addresses frontier model capabilities (test-time reasoning scaling) and their limitations in LLM-based reasoning systems, which materially affect agent planning and reliability.
**Depth:** 4/5 — Introduces a novel prefix-level trajectory evaluation protocol with concrete benchmark results (21% accuracy improvement, 50% efficiency gains) and failure analysis revealing specific mechanisms (logical drift, visual reinterpretation) behind harmful overthinking.

### [Don't Gamble, GAMBLe: An Analytical Framework for AI-Driven Research Systems](https://arxiv.org/abs/2606.02863)
**Source:** arxiv | **Authors:** Marquita Ellis; Paul Castro
**Relevance:** 4/5 — Directly addresses LLM-based agent systems (ADRS) that use LLMs with automated evaluation for discovery, analyzing how component interactions (generator, assessor, mechanism) affect agent performance.
**Depth:** 4/5 — Provides substantial methodology (GAMBLe framework decomposing ADRS behavior, effective landscape formalization) and concrete empirical results (760+ runs, 13-67% performance improvements) revealing non-obvious findings about generator-assessor interactions and mechanism trade-offs.

### [When Helping Hurts and How to Fix It: Multi-Agent Debate for Data Cleaning](https://arxiv.org/abs/2606.02866)
**Source:** arxiv | **Authors:** Chirag Parmar; Akshat Mehta; Henglin Wu; Jagadish Ramamurthy; Shweta Medhekar
**Relevance:** 4/5 — Directly addresses multi-agent LLM reasoning and debate mechanisms for task performance, a core agent capability, with rigorous empirical analysis across multiple models and domains.
**Depth:** 4/5 — Provides concrete methodology (adversarial separation requirements, code-execution grounding, evidence-gating), quantified results across 6,000+ conditions, mechanistic insights (critique-induced confusion), and a generalizable predictive condition validated across 19 published comparisons.

### [Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks](https://arxiv.org/abs/2606.02875)
**Source:** arxiv | **Authors:** Dipesh KC; Anjila Budathoki
**Relevance:** 4/5 — Directly addresses LLM-based coding agents' real-world deployment constraints through a systematic evaluation of task resumption, context management, and agent coordination—core agent capability and evaluation challenges.
**Depth:** 4/5 — Introduces a rigorous handoff protocol with 181 tasks and 724 runs, provides quantified methodology (four handoff views), concrete efficiency results (20–59% reduction in agent events, 42–63% in tokens), and identifies an important evaluation gap in agent benchmarks.

### [What Benchmarks Don't Measure: The Case for Evaluating Abstention Competence in Autonomous Agents](https://arxiv.org/abs/2606.02965)
**Source:** arxiv | **Authors:** Victor Ojewale; Suresh Venkatasubramanian
**Relevance:** 4/5 — Directly addresses a critical evaluation and safety challenge in LLM-based autonomous agents, specifically how benchmarks and reward structures fail to measure abstention competence—a frontier capability gap in agent deployment.
**Depth:** 4/5 — Provides substantive methodology (three-gap taxonomy, abstention evaluation protocols with specific metrics) and concrete empirical results (89.2% hazardous-action blocking across 144 scenarios and five model families) with clear diagnosis of the root cause (reward hacking and compliance bias).

### [AUDITFLOW: Executable Symbolic Environments for Structured Financial Reporting Verification](https://arxiv.org/abs/2606.03031)
**Source:** arxiv | **Authors:** Yan Wang; Xuguang Ai; Jaisal Patel; Xueqing Peng; Fengran Mo; Yupeng Cao; Haohang Li; Mingyu Cao; Li...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for structured reasoning tasks, with explicit methodology for tool design and multi-agent coordination that enables reliable verification beyond model capabilities.
**Depth:** 4/5 — Provides concrete methodology (symbolic environment construction, typed tool interfaces, multi-agent disagreement resolution), quantified results (82.09% accuracy, 14.93pt improvement), and explicit ablation (17.91% drop without symbolic checks) demonstrating what agents require to solve structured tasks.

### [DELTAMEM: Incremental Experience Memory for LLM Agents via Residual Trees](https://arxiv.org/abs/2606.03083)
**Source:** arxiv | **Authors:** Haoran Tan; Zeyu Zhang; Zhicheng Cao; Rui Li; Xu Chen
**Relevance:** 4/5 — Directly addresses memory architecture for LLM-based agents, a core capability that enables continual learning and improved performance in interactive environments.
**Depth:** 4/5 — Presents novel methodology (residual trees with delta nodes, failure-penalized retrieval, autonomous consolidation) with empirical validation across diverse environments and concrete architectural insights into reducing redundancy and retrieval conflicts.

### [The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs](https://arxiv.org/abs/2606.03092)
**Source:** arxiv | **Authors:** Xu Wan; Speed Zhu; Jianwei Cai; Guang Chen; XiMing Huang; Wiggin Zhou; Mingyang Sun
**Relevance:** 4/5 — Directly addresses inference-time budget allocation for LLM reasoning, a frontier capability that materially affects agent performance under real-world deployment constraints.
**Depth:** 4/5 — Provides explicit optimization methodology (shadow price equilibrium, rational abandonment policy) with concrete experimental results (3x accuracy improvement) and clear articulation of prior limitations in uniform allocation.

### [DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration](https://arxiv.org/abs/2606.03103)
**Source:** arxiv | **Authors:** Wenkai Wang; Tao Xiong; Jingchen Ni; Yunpeng Bao; Xiyun Li; Tianqi Liu; Hongcan Guo; Zilong Huang; S...
**Relevance:** 4/5 — DeskCraft directly evaluates LLM-based desktop agents on long-horizon professional workflows and introduces a formal protocol for human-in-the-loop agent collaboration, squarely addressing agent reasoning, planning, and interaction capabilities.
**Depth:** 4/5 — The work provides substantial methodology (multilevel taxonomy, interaction protocol formalizing mid-turn and post-turn exchanges) and concrete results (18 agents evaluated on 538 tasks with detailed failure analysis on long-horizon and proactive clarification challenges).

### [Uncertainty-Aware Clarification in LLM Agents with Information Gain](https://arxiv.org/abs/2606.03135)
**Source:** arxiv | **Authors:** Mengyi Deng; Zhiwei Li; Xin Li; Tingyu Zhu; Ying Zhao; Zhijiang Guo; Wei Wang
**Relevance:** 4/5 — Directly addresses a core LLM-agent challenge (handling underspecified user instructions) with a principled clarification mechanism that improves agent-tool-user interactions.
**Depth:** 4/5 — Introduces Information Gain Reward as a concrete methodology for training clarification behavior, includes cross-backbone empirical validation on τ-Bench, and demonstrates measurable improvements (3.7% success rate gain) with quantified interaction overhead.

### [MedCUA-Bench: A Screenshot-Only Benchmark for Clinical Computer-Use Agents](https://arxiv.org/abs/2606.03203)
**Source:** arxiv | **Authors:** Jia Yu; Zilong Wang; Xinyang Jiang; Dongsheng Li; Shuo Wang
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation in a specialized domain, providing methodology for assessing agent capabilities on real-world UI tasks with safety constraints that materially affect agent deployment.
**Depth:** 4/5 — Presents concrete benchmark design (18 scenarios, 10 domains, dual-level goals), systematic evaluation across 23 agents with specific metrics, and quantified limitations (54.2% best closed-source vs 2.5% open-source average) that expose capability gaps.

### [InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain](https://arxiv.org/abs/2606.03329)
**Source:** arxiv | **Authors:** Tiancheng Han; Yong Li; Wuzhou Yu; Qiaosheng Zhang; Wenqi Shao
**Relevance:** 4/5 — Directly addresses training mechanisms for LLM-based chunk-wise memory agents on long-context tasks, a core agent capability.
**Depth:** 4/5 — Provides concrete methodology (answer-conditioned information gain reward design with normalization and trajectory filtering) and empirical results showing improvements over RL baselines under controlled conditions.

### [DMF: A Deterministic Memory Framework for Conversational AI Agents](https://arxiv.org/abs/2606.03463)
**Source:** arxiv | **Authors:** Matteo Stabile; Enrico Zimuel
**Relevance:** 4/5 — Directly addresses memory systems for LLM-based conversational agents, a core component of agent architecture that materially affects agent capabilities.
**Depth:** 4/5 — Presents clear mathematical methodology (Survival Score Ω, decay law formulation, structured recall pipeline), concrete experimental results (5x–242x token reduction vs. Mem0), and explicitly identifies limitations of LLM-based memory compression that motivate the contribution.

### [ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning](https://arxiv.org/abs/2606.03503)
**Source:** arxiv | **Authors:** Ziyan Liu; Xueda Shen; Yuzhe Gu; Songyang Gao; Kuikun Liu; Guangran Cheng; Chengqi Lyu; Dahua Lin; W...
**Relevance:** 4/5 — Directly addresses frontier capability in LLM-based reasoning systems by improving chain-of-thought efficiency through preference learning, a core methodology for agent reasoning.
**Depth:** 4/5 — Presents concrete methodology (introspective preference optimization with masked learning objective) and substantial empirical results (56% token reduction on DeepSeek-R1 while maintaining accuracy).

### [Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI](https://arxiv.org/abs/2606.03518)
**Source:** arxiv | **Authors:** Amjad Ibrahim; Yong Li
**Relevance:** 4/5 — Directly addresses authorization and governance mechanisms essential for deploying autonomous LLM-based agents that can delegate tasks, act with bounded permissions, and coordinate—a critical capability frontier for agentic AI systems.
**Depth:** 4/5 — Proposes formal compositional framework with relational definitions, recursive delegation primitives, scope attenuation mechanisms, and includes formal proofs plus empirical validation showing practical operationalization of agentic authorization semantics.

### [SAGE: A Quantitative Evaluation of Socialized Evolution in Agent Ecosystems](https://arxiv.org/abs/2606.03544)
**Source:** arxiv | **Authors:** Linyue Pan; Yaoming Zhu; Lin Qiu; Xuezhi Cao; Xunliang Cai
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation and learning dynamics, specifically how multi-agent interaction affects self-improvement capabilities—a frontier question for agent design and deployment.
**Depth:** 4/5 — Provides rigorous comparative methodology (SocialEvo vs. SelfEvo), concrete results across three diverse arenas with multiple evolutionary rounds, and mechanistic insights into when peer history helps agents break through plateaus.

### [Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition](https://arxiv.org/abs/2606.03657)
**Source:** arxiv | **Authors:** Jinnuo Liu; Yue Peng; Jinhan Niu; Hongyi Wen
**Relevance:** 4/5 — Directly addresses a core frontier capability for LLM-based agents: tool use and API acquisition, which is essential for agent autonomy and generalization.
**Depth:** 4/5 — Provides rigorous methodology (automated dynamic benchmarking with diagnostic categorization), concrete empirical results across 1.9K tasks and multiple models, and actionable insights into how retrieval and parametric adaptation serve complementary roles in API knowledge integration.

### [From Answers to States: Verifiable Process-Level Evaluation of Chemical Reasoning in Large Language Models](https://arxiv.org/abs/2606.03660)
**Source:** arxiv | **Authors:** Hongyu Guo; Hao Li; He Cao; Gongbo Zhang; Li Yuan
**Relevance:** 4/5 — Directly addresses evaluation and reasoning verification for LLM-based agents in a specialized domain, focusing on process-level assessment rather than final answers—critical for agent reliability.
**Depth:** 4/5 — Provides concrete methodology (rule-verifiable templates, deterministic chemistry verifiers, state constraints) and empirical results across 5,620 samples revealing systematic gaps between final correctness and reasoning consistency.

### [SkillPyramid: A Hierarchical Skill Consolidation Framework for Self-Evolving Agents](https://arxiv.org/abs/2606.03692)
**Source:** arxiv | **Authors:** Yuan Xiong; Ziqi Miao; Qian Chen; Lijun Li; Yequan Wang; Shizhu He; Jun Zhao; Kang Liu
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for skill management, composition, and generalization—core enabling capability for multi-task agents.
**Depth:** 4/5 — Proposes explicit hierarchical framework with self-evolution mechanism for skill consolidation, demonstrates substantial empirical gains (38% reward increase, 27.7% step reduction) across multiple environments and model backbones.

### [Code-on-Graph: Iterative Programmatic Reasoning via Large Language Models on Knowledge Graphs](https://arxiv.org/abs/2606.03705)
**Source:** arxiv | **Authors:** Weiwei Ding; Zixuan Li; Long Bai; Zhuo Chen; Kun Su; Fei Wang; Xiaolong Jin; Jin Zhang; Jiafeng Guo;...
**Relevance:** 4/5 — Directly addresses LLM agent reasoning and tool use via programmatic interfaces to knowledge graphs, improving compositional reasoning capabilities that enable more complex agent tasks.
**Depth:** 4/5 — Presents clear methodology (schema-to-class abstraction, code generation grounding) with concrete experimental results (up to 10.5% improvement on standard benchmarks) and explicitly identifies and addresses limitations of prior KG-LLM integration approaches.

### [LAP: An Agent-to-Instrument Protocol for Autonomous Science](https://arxiv.org/abs/2606.03755)
**Source:** arxiv | **Authors:** Linwu Zhu; Liqiang Gao; Yan Chen; Dan Zhu; Jian Huang
**Relevance:** 4/5 — Directly addresses the agent-to-instrument interface in LLM-based autonomous science systems, a critical infrastructure gap for deploying agents in physical-world tasks.
**Depth:** 4/5 — Provides detailed protocol specification with four physical-world primitives (InstrumentCard, reservation, safety-fence, MeasurementResult), six-layer architecture, and state machines—substantial methodology enabling agent interoperability.

### [BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents](https://arxiv.org/abs/2606.03829)
**Source:** arxiv | **Authors:** Alex Wang; Georg Meinhardt; Jacob Katz; Joseph H. Kim; Pratyush K. Chaudhary; Chase Blagden; Eric Xu
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation in a complex reasoning domain, with methodology for measuring derivation quality and concrete results across frontier models.
**Depth:** 4/5 — Provides substantial methodology (workflow-grounded rubric framework with 36k points), concrete evaluation results across 10 agents showing 58.8% best performance, and systematic analysis of capability variation across workflows.

### [Reasoning Structure of Large Language Models](https://arxiv.org/abs/2606.03883)
**Source:** arxiv | **Authors:** Fr\'ed\'eric Berdoz; Luca A. Lanzend\"orfer; Fabian Farestam; Roger Wattenhofer
**Relevance:** 4/5 — Directly addresses reasoning structure and evaluation methodology for LLMs, which is central to understanding agent capabilities and failure modes.
**Depth:** 4/5 — Introduces a scalable benchmark, a concrete pipeline for converting reasoning traces into verifiable graphs, and a novel efficiency metric with quantitative analysis on open-source models.

### [Entropy Is Not Enough: Unlocking Effective Reinforcement Learning for Visual Reasoning via Vision-Anchored Token Selection](https://arxiv.org/abs/2606.03937)
**Source:** arxiv | **Authors:** Senjie Jin; Peixin Wang; Boyang Liu; Xiaoran Fan; Shuo Li; Zhiheng Xi; Jiazheng Zhang; Yuhao Zhou; T...
**Relevance:** 4/5 — Directly addresses reinforcement learning for multimodal reasoning in LLM-based agents, improving credit assignment mechanisms that affect how agents learn from visual and semantic information.
**Depth:** 4/5 — Provides clear methodology (vision-entropy coupling via multiplicative interaction), identifies a specific failure mode of prior work (entropy collapse in visual reasoning), and reports substantial empirical gains (2.28-3.15 point improvements across model scales).

### [Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation](https://arxiv.org/abs/2606.02684)
**Source:** arxiv | **Authors:** Yuying Li; Leqi Zheng; Yongzi Yu; Wenrui Zhou; Xuchang Zhong; Xing Hu; Jing Jin; Huangjie Yuan; Tao ...
**Relevance:** 4/5 — On-policy distillation is a frontier training method that directly improves model capabilities for reasoning and planning, materially affecting what LLM-based agents can accomplish.
**Depth:** 4/5 — The paper presents concrete methodology (trajectory filtering + token-level soft reweighting) with substantial empirical results (+6.25 AIME, +18.81 Miner) and addresses specific limitations of prior hard token selection approaches.

### [MOSAIC: Efficient Mixture-of-Agent Scheduling via Adaptive Aggregation and Inference Concurrency](https://arxiv.org/abs/2606.03014)
**Source:** arxiv | **Authors:** Saptarshi Mitra; Yifan Zhang; Rachid Karami; Phyo Pyae Moe Aung; Nazmul Takbir; Sreetama Sarkar; Sou...
**Relevance:** 4/5 — Directly addresses efficient deployment and execution of multi-agent LLM systems (Mixture-of-Agents), a frontier capability that materially affects agent scalability and practical deployment.
**Depth:** 4/5 — Provides concrete methodology (ILP-based scheduling, confidence-aware adaptive aggregation) with substantial empirical results (2.5x–4.23x speedups) and explicit problem formulation addressing load imbalance in multi-agent inference.

### [ASymPO: Asymmetric-Scale Policy Optimization for Asynchronous LLM Post-Training Without Behavior Information](https://arxiv.org/abs/2606.03070)
**Source:** arxiv | **Authors:** Zehua Liu; Yuxuan Yao; Xiaojin Fu; Tao Zhong; Mingxuan Yuan
**Relevance:** 4/5 — Directly addresses LLM post-training through asynchronous RL, a frontier training method that materially affects agent capability and deployment efficiency.
**Depth:** 4/5 — Provides clear methodology (identifies scale-imbalance failure mode, proposes ASymPO normalization mechanism) and concrete evaluation on mathematical reasoning post-training with explicit limitations of prior behavior-corrected approaches.

### [Libra: Efficient Resource Management for Agentic RL Post-Training](https://arxiv.org/abs/2606.03077)
**Source:** arxiv | **Authors:** Kaiwen Chen; Xin Tan; Jingzong Li; Hong Xu
**Relevance:** 4/5 — Directly addresses efficient post-training and deployment of LLM-based agents through RL, tackling infrastructure challenges that materially affect agent capability scaling.
**Depth:** 4/5 — Provides concrete methodology (global resource planner, causality-driven MLFQ scheduler) with quantified results (3.0× throughput, 2.5× convergence speedup) and identifies non-obvious technical challenges in agentic RL workloads.

### [Learning to Solve, Forgetting to Retain: Correct-Set Turnover in RLVR](https://arxiv.org/abs/2606.03087)
**Source:** arxiv | **Authors:** Chuanyu Qin; Chenxu Yang; Qingyi Si; Naibin Gu; Peng Fu; Zheng Lin
**Relevance:** 4/5 — RLVR is a frontier training method that materially affects LLM agent capabilities by improving reasoning and tool-use performance through verifiable rewards.
**Depth:** 4/5 — The paper provides explicit methodology (repair-window principle, retention-aware review mechanism), analytical grounding, and comprehensive empirical results across 20 benchmarks demonstrating a systematic improvement to RLVR training pipelines.

### [Constitutional On-Policy Safe Distillation](https://arxiv.org/abs/2606.03089)
**Source:** arxiv | **Authors:** Ming Wen; Yuxuan Liu; Kun Yang; Yunhao Feng; Zhuoer Xu; Yuhao Sun; Shiwen Cui; Xiang Zheng; Xingjun ...
**Relevance:** 4/5 — Safety alignment and training efficiency directly affect what frontier LLMs can reliably do, and OPSD is a frontier post-training method that shapes model capabilities for deployment.
**Depth:** 4/5 — The paper provides formal analysis of failure modes (geometric leakage in semantic space), proposes a concrete mitigation mechanism (Cross-SFT cold-start), and reports systematic evaluation across 12 benchmarks with quantified safety-helpfulness trade-offs.

### [HARVE: Hacking-Aware Reward-Head Vector Editing for Robust Reward Models](https://arxiv.org/abs/2606.03131)
**Source:** arxiv | **Authors:** Shuang Liu; Yuxuan Bo; Qiuyang Zhao; Caiyue Huang; Xiaorong Chen; Yanguang Liu; Mengnan Du
**Relevance:** 4/5 — Reward models are foundational to LLM alignment and agent training; this work directly addresses robustness against reward hacking, a critical failure mode for deployed agents relying on learned reward signals.
**Depth:** 4/5 — The paper provides explicit methodology (residual-space editing via contrastive examples), comprehensive evaluation across eight models with a new benchmark (RewardHackBench), concrete empirical results, and mechanistic insights about multidimensional hacking structures.

### [FederatedSkill: Federated Learning for Agentic Skill Evolution](https://arxiv.org/abs/2606.03143)
**Source:** arxiv | **Authors:** Jingbo Yang; Guanyu Yao; Yang Zhang; Ramana Rao Kompella; Gaowen Liu; Shiyu Chang
**Relevance:** 4/5 — Directly addresses LLM agent self-improvement through skill library evolution and collaborative learning, which is core to agent capability development.
**Depth:** 4/5 — Presents clear methodology (semantic skill diffs, federated aggregation with client-specific boundaries) and concrete empirical results (44.4% success rate improvement, 37.5% cost reduction across 20 task families).

### [Right Makes Might: Aligning Verified Hidden States Empowers RL Reasoning](https://arxiv.org/abs/2606.03234)
**Source:** arxiv | **Authors:** Ziyue Wang; Aomufei Yuan; Yongfu Zhu; Shuai Dong; Wenpu Liu; Yiran Yao; Weichu Xie; Yuqi Xu; Caoyuan...
**Relevance:** 4/5 — Directly addresses frontier model capability for reasoning via RL training methodology that improves mathematical problem-solving in LLMs, a core capability for agentic reasoning.
**Depth:** 4/5 — Provides concrete methodology (Hidden-Align auxiliary loss with geometric analysis of hidden state structure), detailed ablations across model scales, and quantified improvements on eight benchmarks with mechanistic insight into why alignment works.

### [When RLHF Fails: A Mechanistic Taxonomy of Reward Hacking, Collapse, and Evaluator Gaming](https://arxiv.org/abs/2606.03238)
**Source:** arxiv | **Authors:** Zelalem Abahana
**Relevance:** 4/5 — RLHF is a frontier training method that directly determines what capabilities and behaviors emerge in LLMs, materially affecting agent performance; this work provides mechanistic insight into failure modes during training.
**Depth:** 4/5 — The paper offers concrete methodology (taxonomy of failure modes, logistic prediction model), empirical results across 1920 transitions with quantified metrics (14.45% reward-hacking rate, ROC-AUC 0.821), and reveals that failures occur during training dynamics, not just at convergence.

### [Mitigating False Credit Propagation: Probabilistic Graphical Reward Aggregation for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.03361)
**Source:** arxiv | **Authors:** Can Lv; Mingju Chen; Heng Chang; Shiji Zhou
**Relevance:** 4/5 — Directly addresses reward aggregation for LLM post-training via rubric-based RL, a frontier technique for steering agent behavior and enabling complex reasoning tasks.
**Depth:** 4/5 — Proposes a concrete probabilistic graphical framework with clear methodology, provides systematic evaluation across three benchmarks with quantified improvements (15.5% relative gain), and includes diagnostic analysis of failure modes (96.5% leakage reduction).

### [KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks](https://arxiv.org/abs/2606.03458)
**Source:** arxiv | **Authors:** Lorenz K. Muller; Philippe Bich; Chiara Boretti; Hyun-Min Chang; Jiawei Zhuang; Lukas Cavigelli
**Relevance:** 4/5 — Directly addresses KV-cache optimization for long-horizon LLM reasoning tasks, a critical bottleneck for agent deployment and test-time scaling.
**Depth:** 4/5 — Provides clear methodology (Hadamard rotation + variance normalization), identifies root cause of error accumulation, and demonstrates concrete improvements on reasoning benchmarks (MATH500, AIME24, HumanEval) with production implementation.

### [When Should the Teacher Move? Temporal Coupling and Stability in Self On-Policy Distillation](https://arxiv.org/abs/2606.03532)
**Source:** arxiv | **Authors:** Haowei Guo; Baolong Bi; Ruicheng Zhang; Bingqian Sun; Wentao Zhang
**Relevance:** 4/5 — Self on-policy distillation directly enables frontier LLM agent training by improving student policy stability and performance on reasoning tasks (Chemistry, Biology, Physics, ToolUse), addressing a core training methodology for agentic models.
**Depth:** 4/5 — The paper provides systematic methodology (temporal coupling analysis, diagnostic framework of KL structure and refresh shock) and concrete results (CGTR achieving zero collapse across all four tasks), with mechanistic insight into failure modes like state-oblivious collapse that distinguish it from prior work.

### [Exploiting Verification-Generation Gap: Test-Time Reinforcement Learning with Confidence-Conditioned Verification](https://arxiv.org/abs/2606.03608)
**Source:** arxiv | **Authors:** Jiahui Li; Jianfeng Shan; Wenpei Chen; Shunyu Wu; Jian Lou; Wenjie Feng; Dan Li; See-Kiong Ng
**Relevance:** 4/5 — Directly addresses test-time reinforcement learning for LLM reasoning—a frontier capability-enhancement method that materially affects what language model agents can accomplish in complex reasoning tasks.
**Depth:** 4/5 — Provides detailed methodology (confidence-conditioned verification mechanism, verifier-guided pseudo-label selection, exploration rewards), concrete empirical results across 6 benchmarks (+9.8% Pass@1, +18.7% Pass@16 gains), and clear problem analysis identifying root causes of prior failures.

### [Physics-Guided Policy Optimization with Self-Distillation](https://arxiv.org/abs/2606.03620)
**Source:** arxiv | **Authors:** Ke Wang; Yuning Wu; Haoran Liu; Chaoqun Jia; Devin Chen; Kai Wei
**Relevance:** 4/5 — Directly addresses LLM post-training methodology (self-distillation) with a novel optimization approach that improves training stability and agent capability, falling squarely within frontier model training methods that affect what agents can do.
**Depth:** 4/5 — Provides clear methodology (physics-inspired information modulation with SDE-level formalization), theoretical guarantees (order-1 weak-approximation), and concrete experimental results (+4.5 point gains on Science-QA with improved stability).

### [A Close Look At World Model Recovery In Supervised Fine-Tuned LLM Planners](https://arxiv.org/abs/2606.03685)
**Source:** arxiv | **Authors:** Patrick Emami; Nan Qiang; Peter Graf
**Relevance:** 4/5 — Directly addresses how LLM-based planners learn world models and internal representations for classical planning, a core capability for agent reasoning and planning.
**Depth:** 4/5 — Provides systematic interpretability methodology (probing internal representations, examining generative capabilities) with concrete empirical findings about what models learn from different training data distributions.

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

### [ToolGate: Token-Efficient Pre-Call Control for Tool-Augmented Vision-Language Agents](https://arxiv.org/abs/2606.03054)
**Source:** arxiv | **Authors:** Anjie Liu; Yan Song; Zhixun Chen; Ziqin Gong; Zhongwei Yu; Jun Wang
**Relevance:** 4/5 — Directly addresses a core LLM-agent capability (tool use and planning efficiency) with concrete methodology for controlling when tool calls execute in ReAct-style agents.
**Depth:** 3/5 — Provides clear problem formulation, a lightweight controller mechanism with concrete architectural design, and quantitative results across five benchmarks showing both efficiency gains (64-69% token cost) and accuracy preservation/improvement.

### [Perceive Before Reasoning: A Pre-Reasoning Perception Framework for Efficient and Reliable Proactive Mobile Agents](https://arxiv.org/abs/2606.03236)
**Source:** arxiv | **Authors:** Zhijie Ding (HyperAI Team; Xiaomi Corporation; Zhongnan University of Economics and Law); Weinan Hon...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for mobile assistance, focusing on decision-making mechanisms (intervention gating and reasoning) that materially affect agent capabilities.
**Depth:** 3/5 — Presents a concrete two-stage framework with explicit methodology (lightweight perceptor for gating, conditional reasoner activation) and benchmark results (FTR/SR improvements), though the contribution is architecturally incremental rather than paradigm-shifting.

### [StepFinder: A Temporal Semantic Framework for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2606.03467)
**Source:** arxiv | **Authors:** Taiyu Zhu; Yifan Wu; Weilin Jin; Ying Li; Gang Huang
**Relevance:** 4/5 — Directly addresses failure diagnosis and reliability in LLM-based multi-agent systems, a core capability needed for robust agent deployment.
**Depth:** 3/5 — Provides concrete methodology (temporal semantic encoding + lightweight neural modules for root cause identification) with quantitative results (79% latency reduction), though the technical novelty is primarily in engineering efficiency rather than fundamental agent reasoning.

### [Bridging Auxiliary Constraints to Resolve Instruction Following in Large Reasoning Models](https://arxiv.org/abs/2606.03624)
**Source:** arxiv | **Authors:** Zhengyi Zhao; Shubo Zhang; Huimin Wang; Zezhong Wang; Yutian Zhao; Yefeng Zheng; Binyang Li; Yulan H...
**Relevance:** 4/5 — Directly addresses instruction following and constraint satisfaction in LLMs—a core capability gap for agent reliability—using structured reasoning about constraint relationships.
**Depth:** 3/5 — Introduces explicit methodology (constraint knowledge graphs, bridge constraint discovery) and provides concrete results (39% reduction in constraint violations across three datasets), though the mechanism is narrow in scope rather than broadly paradigm-shifting.

### [Enhancing Operational Safety via Agentic Dialogue Hazard Identification Analysis](https://arxiv.org/abs/2606.03812)
**Source:** arxiv | **Authors:** Sanjay Das; Ran Elgedawy; Ethan Seefried; Ryan Burchfield; Tirthankar Ghosal
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent reasoning and agentic dialogue as a mechanism to improve task performance, squarely within frontier agent capabilities.
**Depth:** 3/5 — Provides systematic methodology comparing dialogue modalities (adversarial vs. constructive) and introduces algorithm-based optimization, with empirical evaluation on a curated dataset, though application domain (hazard identification) is narrower than core agent reasoning.

### [Hedge-Bench: Benchmarking Agents on Hard, Realistic Tasks Pertaining to Financial Reasoning](https://arxiv.org/abs/2606.03918)
**Source:** arxiv | **Authors:** Eric Cho; Shawn Huang; Alice Lu; Andy Lyu
**Relevance:** 4/5 — Directly evaluates LLM-based agent performance on realistic reasoning tasks with concrete methodology and deterministic grading, addressing a gap in agent benchmarking.
**Depth:** 3/5 — Provides solid contribution through expert-grounded benchmark design with verified reasoning traces and deterministic evaluation, though lacks novel agent architecture or training methodology.

### [Efficient Hyperparameter Optimization for LLM Reinforcement Learning](https://arxiv.org/abs/2606.03073)
**Source:** arxiv | **Authors:** Minping Chen; Bowen Xiao; Du Liang; Chuxuan Zeng; Zeyi Wen
**Relevance:** 4/5 — LLM RL training is a core frontier capability and agent-training method; efficient HPO directly impacts what models agents can be trained on and their performance.
**Depth:** 3/5 — Paper presents concrete methodology (dual fidelity adaptation, early-stopping, checkpointing) with quantified efficiency gains (14.9× speedup) and performance results (5.8–111.6% improvement), though HPO is a supporting technique rather than a breakthrough in agent reasoning itself.

### [FGRPO: Federated GRPO with Adaptive Aggregation on Non-IID Data](https://arxiv.org/abs/2606.03094)
**Source:** arxiv | **Authors:** Pengyu Chen; Shaowei Li; Kai Wang; Yunsheng Yuan; Kai Han; Jun Luo; Feng Li
**Relevance:** 4/5 — Directly addresses training frontier LLM reasoning models via GRPO (a key agent training method), with novel methodology for federated deployment that affects model capability development.
**Depth:** 3/5 — Presents concrete methodology (adaptive aggregation mechanism) and convergence analysis for federated RL training, though the core contribution is a training system design rather than advancing reasoning capability itself.


## Worth knowing (43 items)

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

### [Decomposing how prompting steers behavior](https://arxiv.org/abs/2606.03093)
**Source:** arxiv | **Authors:** Fan L. Cheng; Nikolaus Kriegeskorte
**Relevance:** 3/5 — Mechanistic understanding of how prompts steer LLM/VLM behavior is relevant to agent design and control, but focuses on representation geometry rather than agent reasoning, planning, or tool use capabilities directly.
**Depth:** 4/5 — Introduces a rigorous nested geometric decomposition framework with causal interventions across multiple model families and datasets, revealing that affine transformation is key to prompt-induced behavioral change—solid methodology with concrete experimental results.

### [Proof-Refactor: Refactoring Generated Formal Proofs into Modular Artifacts](https://arxiv.org/abs/2606.03743)
**Source:** arxiv | **Authors:** Yiming Fu; Peixuan Liu; Zichen Wang; Kun yuan
**Relevance:** 3/5 — The work is on LLM-based agents for formal proof generation and refactoring, which touches agent reasoning and planning, but is specialized to formal mathematics rather than the broader frontier of general-purpose LLM agents.
**Depth:** 4/5 — The paper presents a concrete agentic framework with clear methodology (four-phase decomposition), evaluates on real benchmarks (PutnamBench, Putnam2025), and identifies limitations of prior length-based optimization that motivate the process-guided approach.

### [Hallucination Is Linearly Decodable from Mid-Layer Hidden States in Quantized LLMs](https://arxiv.org/abs/2606.02628)
**Source:** arxiv | **Authors:** Aizierjiang Aiersilan
**Relevance:** 3/5 — Hallucination detection in LLMs is tangentially relevant to agent reliability and grounding, but this work focuses on mechanistic analysis of truthfulness signals rather than agent-specific capabilities like planning, tool use, or reasoning.
**Depth:** 4/5 — The paper provides solid methodology (systematic probing across layers and models), concrete quantitative results (0.904-1.000 AUROC), and mechanistic insights into where truthfulness is encoded, with reproducible code on limited hardware.

### [Locality Does Not Imply Reachability: Boundary Repair in Block-Sparse Causal Attention](https://arxiv.org/abs/2606.02680)
**Source:** arxiv | **Authors:** Zhibo Yang
**Relevance:** 3/5 — Block-sparse causal attention mechanisms are infrastructure for efficient LLM inference, which indirectly affects agent capability at scale, but the paper is primarily a theoretical analysis of attention structure rather than agent design or frontier model capability.
**Depth:** 4/5 — Strong methodology: formalizes locality-reachability mismatch through structural dependency sets and phase-conditioned coverage functions with concrete failure mode predictions and a minimal constructive repair (Boundary Bridge Attention) validated on both synthetic and Qwen2.5 checkpoints.

### [GRZO: Group-Relative Zeroth-Order Optimization for Large Language Model Fine-Tuning](https://arxiv.org/abs/2606.02857)
**Source:** arxiv | **Authors:** Liyan Tan; Yequan Zhao; Yifan Yang; Ruijie Zhang; Xinling Yu; Zheng Zhang
**Relevance:** 3/5 — Addresses memory-efficient fine-tuning of frontier LLMs (Llama3-8B, OPT-13B), a capability that enables broader agent deployment, but optimization methods are not directly about agent reasoning, planning, or tool use.
**Depth:** 4/5 — Provides clear methodology (group-relative normalization, per-example perturbations), theoretical analysis (directional unbiasedness, convergence bounds), and concrete results (3.0 accuracy gain, 23% memory reduction) across multiple models.

### [How Quantization Changes Interpretable Features: A Sparse Autoencoder Analysis of Language Models](https://arxiv.org/abs/2606.03002)
**Source:** arxiv | **Authors:** Evan Duan
**Relevance:** 3/5 — Interpretability and mechanistic understanding of LLMs is adjacent to agent capabilities, but this work focuses on quantization artifacts rather than agent reasoning, planning, or tool use directly.
**Depth:** 4/5 — Rigorous methodology with systematic empirical evaluation across models and bit-widths, quantitative metrics (Pearson correlation, AUC, Spearman correlation), and actionable findings about feature survival under compression.

### [Multi-component Causal Tracing in Large Language Models](https://arxiv.org/abs/2606.03085)
**Source:** arxiv | **Authors:** Zirui Yan; Dennis Wei; Dmitriy A. Katz; Prasanna Sattigeri; Ali Tajer
**Relevance:** 3/5 — Causal tracing provides interpretability into LLM internals relevant to understanding model behavior, but is foundational work for agent capability analysis rather than directly advancing agent reasoning, planning, or tool use.
**Depth:** 4/5 — The paper presents a unified methodology with algorithmic innovation (soft interventions, metric transformation, efficient search) and experimental validation, advancing prior single-component work with concrete technical contributions.

### [When Model Merging Breaks Routing: Training-Free Calibration for MoE](https://arxiv.org/abs/2606.03391)
**Source:** arxiv | **Authors:** Canbin Huang; Tianyuan Shi; Xiaojun Quan; Jingang Wang; Jianfei Zhang; Qifan Wang
**Relevance:** 3/5 — MoE routing and model merging are infrastructure concerns for scaling agent capabilities, but this work focuses on a specific technical problem in model consolidation rather than agent reasoning, planning, or tool use.
**Depth:** 4/5 — The paper identifies a concrete failure mode (routing breakdown), provides theoretical grounding via Hessian-based analysis, proposes a training-free solution with closed-form guarantees, and demonstrates empirical improvements on reasoning and code generation benchmarks.

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

### [Visual Graph Scaffolds for Structural Reasoning in Large Language Models](https://arxiv.org/abs/2606.02673)
**Source:** arxiv | **Authors:** Runlin Lei; Xiaokui Xiao; Zhewei Wei
**Relevance:** 3/5 — Directly addresses reasoning enhancement for LLMs through structured scaffolds, which is relevant to agent reasoning capabilities, but does not focus on agent autonomy, planning, or tool use.
**Depth:** 3/5 — Provides solid methodology (graph vs. text scaffolds, supervised fine-tuning, KL distillation) and concrete experimental results (modality gap findings, reasoning efficiency metrics) with clear limitations of prior text-only approaches.

### [Think-Before-Speak: From Internal Evaluation to Public Expression in Multi-Agent Social Simulation](https://arxiv.org/abs/2606.03137)
**Source:** arxiv | **Authors:** Kaiqi Yang; Tai-Quan Peng; Sanguk Lee; Hui Liu
**Relevance:** 3/5 — LLM-based multi-agent simulation with structured internal reasoning and planning mechanisms is relevant to agent architecture, but the application (social simulation/opinion dynamics) is peripheral to frontier agent capabilities rather than central.
**Depth:** 3/5 — The work presents solid methodology (interval-based framework separating internal evaluation from public expression) with structured results (systematic variation across conditions, appraisal effects), but lacks frontier model insights or capabilities advancement.

### [Cross-Lingual Token Arbitrage: Optimizing Code Agent Context Windows via Local LLM Preprocessing](https://arxiv.org/abs/2606.03618)
**Source:** arxiv | **Authors:** Mehmet Utku Colak
**Relevance:** 3/5 — Directly addresses a real bottleneck in LLM-based code agents (token efficiency), but is primarily an engineering/optimization contribution rather than advancing agent reasoning or frontier model capabilities.
**Depth:** 3/5 — Provides concrete methodology (local preprocessing pipeline with cross-lingual translation and structural rewriting) and comprehensive evaluation across multilingual benchmarks with ablation studies, but the core contribution is prompt optimization rather than novel agent architectures or capabilities.

### [When to Re-Plan: Subgoal Persistence in Hierarchical Latent Reasoning](https://arxiv.org/abs/2606.03741)
**Source:** arxiv | **Authors:** Ayushi Chadha
**Relevance:** 3/5 — Addresses latent reasoning and hierarchical planning in LLM-style architectures, relevant to agent reasoning capabilities, but operates on synthetic tasks (ARC) rather than frontier language models or deployed agents.
**Depth:** 3/5 — Provides clear methodology (feudal manager-worker architecture with subgoal persistence) and controlled empirical results (loss curves, ablations, hyperparameter optima), but is incremental within latent reasoning literature rather than establishing new paradigms.

### [PyraMathBench: Evaluating and Improving Mathematical Capability in Large Language Models](https://arxiv.org/abs/2606.03858)
**Source:** arxiv | **Authors:** Zetian Ouyang; Linlin Wang; Gerard de Melo; Liang He
**Relevance:** 3/5 — Addresses LLM mathematical reasoning capability—relevant to agent problem-solving—but focuses on benchmark construction and numerical computation rather than agent architecture or deployment.
**Depth:** 3/5 — Provides clear methodology (hierarchical benchmark design, SOLVE module with tool-use mechanisms, IRPO training) and quantitative results (5.0 score improvement), offering interpretable insights into LLM math failures.

### [$\Psi$-Bench: Evaluating Persona-Sensitive Influencing in Persuasive Dialogues](https://arxiv.org/abs/2606.02754)
**Source:** arxiv | **Authors:** Peixuan Han; Hongyi Du; Jiayu Liu; Yihang Sun; Yutong Liu; Jiaxuan You
**Relevance:** 3/5 — Evaluates LLM agent capabilities (proactive personalization, persuasion in dialogue) but focuses on benchmark design and performance measurement rather than agent architecture, reasoning mechanisms, or training methods that advance frontier capabilities.
**Depth:** 3/5 — Provides systematic evaluation methodology with concrete results (18.24% performance gain from user profiles, 10 frontier models tested) and identifies limitations in state-of-the-art persuasion, but lacks architectural or mechanistic insights into how agents achieve persona-sensitive influencing.

### [Toward a Modular Architecture for Embedded AI Agent Systems at the Edge](https://arxiv.org/abs/2606.02862)
**Source:** arxiv | **Authors:** Marcus R\"ub; Michael Gerhards
**Relevance:** 3/5 — Directly addresses LLM-based agent deployment and architecture, but focuses on embedded systems constraints rather than frontier agent capabilities or model advances.
**Depth:** 2/5 — Proposes architectural principles and design trade-offs for resource-constrained agents, but explicitly avoids empirical benchmarks and lacks concrete methodology or experimental validation of the proposed modular design.

# AI digest — 2026-06-01

Rolling 7-day window. Generated automatically.

---

## Read deeply (31 items)

_High relevance and substantial depth — worth full attention._

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


## Worth knowing (9 items)

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

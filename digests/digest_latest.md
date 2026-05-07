# AI digest — 2026-05-07

Rolling 7-day window. Generated automatically.

---

## Read deeply (153 items)

_High relevance and substantial depth — worth full attention._

### [End-to-end autonomous scientific discovery on a real optical platform](https://arxiv.org/abs/2604.27092)
**Source:** arxiv | **Authors:** Shuxing Yang; Fujia Chen; Rui Zhao; Junyao Wu; Yize Wang; Haiyao Luo; Ning Han; Qiaolu Chen; Yuze Hu...
**Relevance:** 5/5 — Directly demonstrates end-to-end LLM-based agent system with novel architecture (Meta-Trace memory, dual-layer design) for autonomous long-horizon reasoning, planning, and tool use in a real physical system.
**Depth:** 5/5 — Substantial methodology including nonlinear research phases, memory mechanisms, and architectural design enabling 3,242 LLM calls across 145.9M tokens with concrete validation of a previously unreported physical mechanism (optical bilinear interaction).

### [Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/abs/2604.27151)
**Source:** arxiv | **Authors:** Jinbiao Wei; Kangqi Ni; Yilun Zhao; Guo Gan; Arman Cohan
**Relevance:** 5/5 — Directly addresses core LLM-based agent capability: efficient deployment of computer-use agents through adaptive compute allocation and risk-aware scaling.
**Depth:** 4/5 — Provides concrete methodology (event-driven cascade with learned monitors for stuck/drift detection) and clear mechanism design with evaluation across benchmarks, showing how to make frontier agents practical.

### [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/abs/2604.27707)
**Source:** arxiv | **Authors:** Binyan Xu; Xilin Dai; Kehuan Zhang
**Relevance:** 5/5 — Directly addresses a fundamental architectural limitation in LLM-based agent memory systems, identifying a critical gap between lookup and true learning that constrains agent long-term capability.
**Depth:** 4/5 — Formalizes theoretical limitations with provable consequences, grounds analysis in neuroscience (Complementary Learning Systems theory), and structures critique around three major failure modes (expertise accumulation, compositional generalization ceiling, memory poisoning vulnerability).

### [Synthetic Computers at Scale for Long-Horizon Productivity Simulation](https://arxiv.org/abs/2604.28181)
**Source:** arxiv | **Authors:** Tao Ge; Baolin Peng; Hao Cheng; Jianfeng Gao
**Relevance:** 5/5 — Directly addresses LLM-based agent capabilities for long-horizon reasoning, planning, and tool use in complex environments, with explicit methodology for synthetic data generation to improve agent performance.
**Depth:** 4/5 — Presents concrete methodology for scaling synthetic environment creation, reports quantitative results from 1,000 simulations with 2,000+ turns each, and demonstrates measurable improvements on both in-domain and out-of-domain evaluations.

### [Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182)
**Source:** arxiv | **Authors:** Eyon Jang; Damon Falck; Joschka Braun; Nathalie Kirch; Achu Menon; Perusha Moodley; Scott Emmons; Ro...
**Relevance:** 5/5 — Directly addresses RL-based post-training of LLM agents, exploring a critical failure mode that affects how frontier models can be trained for agentic capabilities and alignment.
**Depth:** 4/5 — Provides concrete methodology (model organisms, detection/mitigation strategies), empirical results across multiple environments, and mechanistic insight into how capable models reason about resisting training.

### [Step-level Optimization for Efficient Computer-use Agents](https://huggingface.co/papers/2604.27151)
**Source:** hf_papers | **Authors:** Jinbiao Wei; Kangqi Ni; Yilun Zhao; Guo Gan; Arman Cohan
**Relevance:** 5/5 — Directly addresses LLM-based computer-use agents, a core frontier application, with concrete methodology for improving agent efficiency and reliability.
**Depth:** 4/5 — Provides substantial technical methodology (event-driven cascade, Stuck Monitor, Milestone Monitor) with clear problem analysis (progress stalls, semantic drift) and modular deployment approach, though specific benchmark results are not detailed in the abstract.

### [Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows](https://huggingface.co/papers/2604.28139)
**Source:** hf_papers | **Authors:** Chenxin Li; Zhengyang Tang; Huangxin Lin; Yunlong Lin; Shijue Huang; Shengyuan Liu; Bowen Ye; Rang L...
**Relevance:** 5/5 — Directly addresses LLM agent evaluation methodology and benchmark design for real-world workflow automation, a frontier capability that constrains what agents can achieve.
**Depth:** 4/5 — Provides concrete evaluation methodology (execution traces, audit logs, deterministic checks, structured LLM judging), specific results across 13 frontier models and 105 tasks, and structured failure analysis revealing persistent bottlenecks in business workflows.

### [Synthetic Computers at Scale for Long-Horizon Productivity Simulation](https://huggingface.co/papers/2604.28181)
**Source:** hf_papers | **Authors:** Tao Ge; Baolin Peng; Hao Cheng; Jianfeng Gao
**Relevance:** 5/5 — Directly addresses long-horizon LLM-based agent capabilities through a scalable methodology for synthetic environment creation and at-scale agentic learning, which is frontier work on model training and evaluation for productivity agents.
**Depth:** 4/5 — Provides clear methodology (synthetic computer generation, multi-agent simulation architecture, experiential learning signals), concrete results (1,000 synthetic computers, 2,000+ turns per simulation, validated performance improvements), and explicit motivation (scaling synthetic data for long-horizon agent tasks at billion scale).

### [Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital](https://huggingface.co/papers/2604.26091)
**Source:** hf_papers | **Authors:** T. J. Barton; Chris Constantakis; Patti Hauseman; Annie Mous; Alaska Hoffman; Brian Bergeron; Hunter...
**Relevance:** 5/5 — Directly addresses LLM-based agent reliability and deployment at scale, with focus on operating-layer mechanisms (prompt compilation, validation, memory, observability) that enable agents to function under real capital constraints.
**Depth:** 4/5 — Provides concrete methodology for agent reliability (typed controls, policy validation, execution guards), extensive empirical results from 21-day deployment (7.5M invocations, 300K onchain actions), and explicit failure modes and mitigations (fabricated rules reduced 57%→3%, fee paralysis addressed, capital deployment 42.9%→78.0%).

### [The Last Harness You'll Ever Build](https://huggingface.co/papers/2604.21003)
**Source:** hf_papers | **Authors:** Haebin Seong; Li Yin; Haoran Zhang
**Relevance:** 5/5 — Directly addresses core LLM-agent challenges: automated harness engineering, multi-level optimization loops (Harness and Meta-Evolution), and enabling rapid adaptation of agents to novel domains without manual engineering.
**Depth:** 4/5 — Presents a formalized two-level framework with explicit algorithmic correspondence to meta-learning, concrete mechanisms (Worker, Evaluator, Evolution agents), and addresses the practical bottleneck of task-specific harness engineering through systematic automation.

### [AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Models Go?](https://arxiv.org/abs/2605.00334)
**Source:** arxiv | **Authors:** Ranit Karmakar; Jayita Chatterjee
**Relevance:** 5/5 — Directly addresses LLM-based agent architecture design by systematically evaluating which model capabilities are necessary for different agent workflow components.
**Depth:** 4/5 — Provides concrete methodology (30-task six-tier benchmark), extensive empirical results (16,542 scored runs across 16 models), and actionable insights about model routing in production agent systems with clear limitations of frontier models.

### [To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling](https://arxiv.org/abs/2605.00737)
**Source:** arxiv | **Authors:** Qinyuan Wu; Soumi Das; Mahsa Amani; Arijit Nag; Seungeon Lee; Krishna P. Gummadi; Abhilasha Ravichan...
**Relevance:** 5/5 — Directly addresses core LLM agent capability—tool-use decision-making—with explicit methodology for when to call tools and training lightweight controllers to optimize this behavior.
**Depth:** 4/5 — Provides principled framework (necessity, utility, affordability), comparative analysis of normative vs. descriptive perspectives, trained estimators with concrete experimental validation across multiple tasks and models.

### [Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning](https://arxiv.org/abs/2605.00347)
**Source:** arxiv | **Authors:** Chengshuai Shi; Wenzhe Li; Xinran Liang; Yizhou Lu; Wenjia Yang; Ruirong Feng; Seth Karten; Ziran Ya...
**Relevance:** 5/5 — Directly addresses LLM-based agents in long-horizon decision-making with systematic methodology for scaling VLMs via RL, a core frontier capability for embodied reasoning agents.
**Depth:** 4/5 — Provides concrete algorithmic contributions (PPO variant with turn-level critic), detailed comparative analysis of training stability, and substantial benchmark results (3x improvement in game progress) with clear methodological insights on sample efficiency and generalization.

### [Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction](https://huggingface.co/papers/2604.27221)
**Source:** hf_papers | **Authors:** Yuxuan Huang; Yihang Chen; Zhiyuan He; Yuxiang Chen; Ka Yiu Lee; Huichi Zhou; Weilin Luo; Meng Fang;...
**Relevance:** 5/5 — Directly addresses LLM-based multi-agent systems with core agent capabilities (planning, decomposition, coordination, memory, reflection) applied to a frontier task.
**Depth:** 4/5 — Provides detailed bi-level architecture design, closed-loop run-verify-reflect methodology, shared workspace coordination mechanism, and substantial benchmark results with significant improvements over prior work.

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

### [Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction](https://arxiv.org/abs/2604.27221)
**Source:** arxiv | **Authors:** Yuxuan Huang; Yihang Chen; Zhiyuan He; Yuxiang Chen; Ka Yiu Lee; Huichi Zhou; Weilin Luo; Meng Fang;...
**Relevance:** 4/5 — Core LLM-based agent work with multi-agent orchestration, reasoning, tool use (web search), memory, and coordination mechanisms that directly enable frontier agent capabilities.
**Depth:** 4/5 — Substantive methodology including bi-level architecture, closed-loop run–verify–reflect process, shared workspace coordination, and persistent memory with self-evolution; paired with strong empirical results (7.5× improvement on WideSearch benchmark and generalization to depth-oriented tasks).

### [Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents](https://arxiv.org/abs/2604.27233)
**Source:** arxiv | **Authors:** Anh Ta; Junjie Zhu; Shahin Shayandeh
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation and error correction at inference time, a core capability gap for tool-calling agents.
**Depth:** 4/5 — Introduces novel Helpfulness-Harmfulness metrics, systematic tradeoff analysis for multi-agent review architectures, and concrete benchmarks on BFCL and Tau2-Bench with model/prompt optimization insights.

### [AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling](https://arxiv.org/abs/2604.27253)
**Source:** arxiv | **Authors:** Fazle Elahi Faisal; Qianhui Wu; Baolin Peng; Jianfeng Gao
**Relevance:** 4/5 — Directly addresses LLM-based web agent training through systematic trajectory generation methodology, a core capability enabler for agent deployment.
**Depth:** 4/5 — Provides concrete methodology (breadth-first exploration, trajectory-grounded task synthesis, hint-based refinement) with quantified benchmark results (24.23% vs 19.59% prior SOTA on WebArena) and addresses specific limitations of prior work.

### [The Inverse-Wisdom Law: Architectural Tribalism and the Consensus Paradox in Agentic Swarms](https://arxiv.org/abs/2604.27274)
**Source:** arxiv | **Authors:** Dahlia Shehata; Ming Li
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent swarms, their failure modes, and architectural mechanisms that affect agent collaboration and reasoning quality.
**Depth:** 4/5 — Provides formal mechanistic analysis (Consensus Paradox, Inverse-Wisdom Law, Tribalism Coefficient) with large-scale empirical validation across 12,804 trajectories and three SOTA benchmarks, identifying specific failure modes and safety requirements.

### [Machine Collective Intelligence for Explainable Scientific Discovery](https://arxiv.org/abs/2604.27297)
**Source:** arxiv | **Authors:** Gyoung S. Na; Chanyoung Park
**Relevance:** 4/5 — Directly presents LLM-based multi-agent reasoning system with coordinated generation, evaluation, and critique mechanisms for autonomous scientific discovery, a frontier capability for agent planning and collaboration.
**Depth:** 4/5 — Provides concrete methodology for orchestrating multiple reasoning agents through symbolic hypothesis evolution and coordination, with quantitative results (6 orders of magnitude error reduction, parameter compression from millions to tens) and explicit comparison against deep learning baselines.

### [Heterogeneous Scientific Foundation Model Collaboration](https://arxiv.org/abs/2604.27351)
**Source:** arxiv | **Authors:** Zihao Li; Jiaru Zou; Feihao Fang; Xuying Ning; Mengting Ai; Tianxin Wei; Sirui Chen; Xiyuan Yang; Ji...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture by extending language-centric agentic systems to coordinate with domain-specific foundation models, which is core to frontier agent capabilities.
**Depth:** 4/5 — Provides explicit methodology for heterogeneous model collaboration (language-model reasoning interface, planning-based orchestration), concrete multi-domain evaluation results, and addresses fundamental architectural limitations of prior agentic systems.

### [InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?](https://arxiv.org/abs/2604.27419)
**Source:** arxiv | **Authors:** Qiyao Wang; Haoran Hu; Longze Chen; Hongbo Wang; Hamid Alinejad-Rokny; Yuan Lin; Min Yang
**Relevance:** 4/5 — Directly addresses LLM-based agent limitations in interactive task execution (website generation), with focus on reasoning failures and adaptive interaction mechanisms.
**Depth:** 4/5 — Provides systematic methodology for simulating user behavior perturbations, introduces novel interactive execution environment with Clarify-Implement-Verify-Submit action space, and delivers empirical analysis of frontier MLLM agent failure modes.

### [Belief-Guided Inference Control for Large Language Model Services via Verifiable Observations](https://arxiv.org/abs/2604.27536)
**Source:** arxiv | **Authors:** Wenhao Yuan; Chenchen Lin; Jian Chen; Jinfeng Xu; Shuo Yang; Edith Cheuk Han Ngai
**Relevance:** 4/5 — Directly addresses inference control and resource allocation for LLM agents—a frontier capability problem for enabling efficient, reliable agentic systems at scale.
**Depth:** 4/5 — Proposes VEROIC, a concrete methodology using POMDPs and verifiable observation channels to solve adaptive inference control, with experimental validation on multiple tasks showing quality-cost trade-offs and calibration improvements.

### [Trace-Level Analysis of Information Contamination in Multi-Agent Systems](https://arxiv.org/abs/2604.27586)
**Source:** arxiv | **Authors:** Anna Mazhar; Huzaifa Suri; Sainyam Galhotra
**Relevance:** 4/5 — Directly addresses how uncertainty and information contamination affect multi-agent LLM workflows, tool use, planning, and execution—core agent capabilities.
**Depth:** 4/5 — Contributes formal taxonomy, trace-based measurement framework, and systematic empirical analysis across 614 runs showing why verification fails and how contamination manifests differently in agent execution.

### [From Context to Skills: Can Language Models Learn from Context Skillfully?](https://arxiv.org/abs/2604.27660)
**Source:** arxiv | **Authors:** Shuzheng Si; Haozhe Zhao; Yu Lei; Qingyi Wang; Dingwei Chen; Zhitong Wang; Zhenhailong Wang; Kangyan...
**Relevance:** 4/5 — Directly addresses LLM agent capabilities through multi-agent self-play for autonomous skill discovery and context learning, which are central to agent reasoning and adaptation.
**Depth:** 4/5 — Proposes a concrete methodology (Ctx2Skill framework with Challenger-Reasoner-Judge loop, Proposer/Generator agents, Cross-time Replay) with empirical evaluation on CL-bench tasks demonstrating consistent improvements.

### [When Agents Evolve, Institutions Follow](https://arxiv.org/abs/2604.27691)
**Source:** arxiv | **Authors:** Chao Fei; Hongcheng Guo; Yanghua Xiao
**Relevance:** 4/5 — Directly addresses multi-agent LLM system architecture, governance design, and collective coordination—core to agent-based research frontier.
**Depth:** 4/5 — Provides explicit methodology (translating 7 historical institutions into executable architectures), concrete comparative results (57pp gap, model-dependent optima), and systematic evaluation across 3 models and 2 benchmarks with reproducible code.

### [Intent2Tx: Benchmarking LLMs for Translating Natural Language Intents into Ethereum Transactions](https://arxiv.org/abs/2604.27763)
**Source:** arxiv | **Authors:** Zhuoran Pan; Yue Li; Zhi Guan; Jianbin Hu; Zhong Chen
**Relevance:** 4/5 — Directly addresses LLM-based agent capability for executing complex, state-dependent tasks (multi-step planning and reasoning-to-execution), which is frontier work on what agents can reliably do.
**Depth:** 4/5 — Contributes rigorous execution-aware evaluation methodology grounded in real mainnet traces, identifies concrete capability gaps (out-of-distribution generalization, multi-step planning failures), and provides substantial benchmark data and analysis of 16 LLMs.

### [WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments](https://arxiv.org/abs/2604.27776)
**Source:** arxiv | **Authors:** Jinchao Li; Yunxin Li; Chenrui Zhao; Zhenran Xu; Baotian Hu; Min Zhang
**Relevance:** 4/5 — WindowsWorld directly evaluates LLM-based GUI agents on multi-application reasoning and coordination—a frontier capability gap—with systematic methodology and concrete performance metrics.
**Depth:** 4/5 — The work provides rigorous benchmark design (multi-agent generation framework, human refinement, 181 tasks across 17 apps), concrete failure analysis (< 21% on multi-app tasks), and identifies specific capability limitations (conditional reasoning, cross-app coordination) that motivate future agent research.

### [MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents](https://arxiv.org/abs/2604.27819)
**Source:** arxiv | **Authors:** Haonan Li; Tianjun Sun; Yongqing Wang; Qisheng Zhang
**Relevance:** 4/5 — Directly addresses a critical safety and capability limitation of LLM-based agents using MCP tool composition, evaluating how model behavior affects cross-boundary data propagation in multi-server agent systems.
**Depth:** 4/5 — Provides substantial methodological contributions (canary-based taint tracking, stratified experimental design, CRS methodology) alongside concrete quantitative results across 3,615 traces from 5 models, plus a prompt-mitigation study showing both effectiveness limits and capability dependencies.

### [ObjectGraph: From Document Injection to Knowledge Traversal -- A Native File Format for the Agentic Era](https://arxiv.org/abs/2604.27820)
**Source:** arxiv | **Authors:** Mohit Dubey; Open Gigantic
**Relevance:** 4/5 — Directly addresses a material constraint on LLM agent capability—token efficiency and context management—through a novel format design that enables better information retrieval and role-scoped access for agents.
**Depth:** 4/5 — Formalizes the Document Consumption Problem with six structural properties, introduces three native format primitives (Progressive Disclosure, Role-Scoped Access, Executable Assertions), and provides empirical evaluation across document classes and agent task types with quantified token reduction.

### [In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks](https://arxiv.org/abs/2604.27891)
**Source:** arxiv | **Authors:** Simon Dennis; Michael Diamond; Rivaan Patil; Kevin Shabahang; Hao Guo
**Relevance:** 4/5 — Directly addresses LLM agent architecture design—comparing external orchestration frameworks (LangGraph, CrewAI) against in-context self-orchestration, a core frontier question about how agents should be structured.
**Depth:** 4/5 — Provides controlled methodology (200 conversations per condition, LLM-as-judge scoring, five criteria), concrete failure rates and quality scores across three procedural domains, and explicitly identifies capability thresholds that make architectural choices viable.

### [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](https://arxiv.org/abs/2604.27906)
**Source:** arxiv | **Authors:** Alex Petrov; Alexander Gusak; Denis Mukha; Dima Korolev
**Relevance:** 4/5 — Directly addresses a critical capability gap for LLM-based agents in production: reliable, schema-grounded external memory systems that support stateful reasoning and exact fact retrieval.
**Depth:** 4/5 — Presents clear methodology (iterative schema-aware extraction pipeline with validation gates) and comprehensive empirical results (90.42% object accuracy, 97.10% F1 on memory tasks) that demonstrate architectural principles superior to retrieval-based baselines.

### [GUI Agents with Reinforcement Learning: Toward Digital Inhabitants](https://arxiv.org/abs/2604.27955)
**Source:** arxiv | **Authors:** Junan Hu; Jian Liu; Jingxiang Lai; Jiarui Hu; Yiwei Sheng; Shuang Chen; Jian Li; Dazhao Du; Song Guo
**Relevance:** 4/5 — Directly addresses LLM-based GUI agents and the RL training methodologies that enable them to handle long-horizon reasoning, credit assignment, and safe exploration—core agent capabilities.
**Depth:** 4/5 — Provides principled taxonomy of RL approaches for GUI agents, analyzes reward engineering and data efficiency mechanisms, identifies emerging technical trends (world models, composite rewards, System-2 reasoning), and offers a roadmap for future development.

### [LLMs as ASP Programmers: Self-Correction Enables Task-Agnostic Nonmonotonic Reasoning](https://arxiv.org/abs/2604.27960)
**Source:** arxiv | **Authors:** Adam Ishay; Joohyung Lee
**Relevance:** 4/5 — Directly addresses LLM reasoning and planning through neuro-symbolic coupling with ASP, a frontier capability enhancement that enables agents to perform robust nonmonotonic reasoning without per-task engineering.
**Depth:** 4/5 — Provides clear methodology (self-correction loop with structured ASP feedback), concrete empirical results across six benchmarks, and identifies mechanistic insights (context rot phenomenon, stable model semantics advantages over SMT).

### [D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery](https://arxiv.org/abs/2604.27977)
**Source:** arxiv | **Authors:** Hanane Nour Moussa; Yifei Li; Zhuoyang Li; Yankai Yang; Cheng Tang; Tianshu Zhang; Nesreen K. Ahmed;...
**Relevance:** 4/5 — Directly addresses LLM-based agents for scientific discovery with a benchmark dataset and evaluation methodology that enables agent training and assessment.
**Depth:** 4/5 — Provides concrete methodology for environment construction, rigorous evaluation validation (87.5% agreement with gold standards), and demonstrates substantial empirical gains (7.8 points on Qwen3-32B) with reproducible artifacts.

### [Exploring Interaction Paradigms for LLM Agents in Scientific Visualization](https://arxiv.org/abs/2604.27996)
**Source:** arxiv | **Authors:** Jackson Vonderhorst; Kuangshi Ai; Haichao Miao; Shusen Liu; Chaoli Wang
**Relevance:** 4/5 — Directly addresses LLM agent paradigms, tool use, memory mechanisms, and long-horizon planning limitations—core agent capabilities—with systematic evaluation across interaction modalities.
**Depth:** 4/5 — Provides concrete methodology (8 agents, 15 benchmarks, multiple metrics), explicit results with tradeoffs (success rates, efficiency, robustness), and identifies key limitations (long-horizon planning) that motivate future directions.

### [What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design](https://arxiv.org/abs/2604.28093)
**Source:** arxiv | **Authors:** Ivan Bercovich
**Relevance:** 4/5 — Directly addresses evaluation methodology for LLM-based agents in terminal/coding domains, a frontier capability area, with concrete guidance on benchmark design flaws that affect how we measure agent performance.
**Depth:** 4/5 — Provides systematic methodology (taxonomy of failure modes, design principles for adversarial tasks) grounded in empirical evidence (15% of benchmarks are reward-hackable) and drawn from extensive practical experience with benchmark curation.

### [When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents](https://arxiv.org/abs/2604.27003)
**Source:** arxiv | **Authors:** Qisheng Hu; Quanyu Long; Wenya Wang
**Relevance:** 4/5 — Directly addresses a fundamental challenge in LLM-based agents—how memory-augmented systems handle continual learning—which is central to agent capability and deployment.
**Depth:** 4/5 — Provides systematic methodology (k,v framework decomposing representation and retrieval), concrete experimental results across ALFWorld and BabyAI, and identifies a non-obvious architectural limitation (stability-plasticity resurfaces at memory level rather than being solved).

### [Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture](https://arxiv.org/abs/2604.27045)
**Source:** arxiv | **Authors:** Samuel L Pugh; Eric Yang; Alexander Muir Sutherland; Alessandra Breschi
**Relevance:** 4/5 — Directly addresses a frontier agent capability—persistent memory management and safety validation for LLM-based agents in longitudinal applications—with methodology and concrete evaluation.
**Depth:** 4/5 — Proposes a novel dual-stream architecture with a dedicated reconciliation engine, provides quantified metrics (84.4% discrepancy detection, 13.6% error cascade), and identifies a specific failure mode (extraction-level degradation) with implications for safe agent deployment.

### [Distributional Alignment Games for Answer-Level Fine-Tuning](https://arxiv.org/abs/2604.27166)
**Source:** arxiv | **Authors:** Mehryar Mohri; Jon Schneider; Yifan Wu
**Relevance:** 4/5 — Directly addresses training methods for LLM reasoning and self-improvement, which are core capabilities enabling agent behavior; answer-level fine-tuning is fundamental to agent performance.
**Depth:** 4/5 — Provides novel game-theoretical framework with Nash equilibrium analysis, proves theoretical equivalence to the original problem, and demonstrates concrete algorithmic improvements (Coherence-GRPO) with results on mathematical reasoning.

### [ANCORA: Learning to Question via Manifold-Anchored Self-Play for Verifiable Reasoning](https://arxiv.org/abs/2604.27644)
**Source:** arxiv | **Authors:** Chengcao Yang; Jun Chen
**Relevance:** 4/5 — ANCORA directly addresses LLM agent self-improvement through verifiable reasoning via self-play, a frontier capability for autonomous agent systems.
**Depth:** 4/5 — The paper provides concrete methodology (two-level group-relative updates, self-distilled SFT, UCB-guided curriculum DAG) and substantial empirical results (81.5% pass@1, 15.8 point improvement over PSV baseline) with explicit problem diagnosis (Proposer collapse).

### [Mind the Gap: Structure-Aware Consistency in Preference Learning](https://arxiv.org/abs/2604.27733)
**Source:** arxiv | **Authors:** Mehryar Mohri; Yutao Zhong
**Relevance:** 4/5 — Directly addresses LLM alignment and preference learning methodology (DPO), a core capability-enabling technique for making LLMs effective agents that follow instructions.
**Depth:** 4/5 — Provides rigorous theoretical analysis with H-consistency bounds, identifies inconsistency gaps in existing methods, proposes SA-DPO with semantic-aware margins, and analyzes margin-capacity trade-offs with concrete theoretical results.

### [CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting](https://arxiv.org/abs/2604.27840)
**Source:** arxiv | **Authors:** Bokai Pan; Mingyue Cheng; Zhiding Liu; Shuo Yu; Xiaoyu Tao; Yuchong Wu; Qi Liu; Defu Lian; Enhong Ch...
**Relevance:** 4/5 — CastFlow presents an LLM-based agent architecture with explicit agentic workflows (planning, action, forecasting, reflection), memory, tool use, and multi-stage training methodology that directly advances how LLMs can be organized as agents.
**Depth:** 4/5 — The paper provides concrete methodology including role-specialized design (frozen general LLM + fine-tuned domain LLM), two-stage training (SFT + RLVR), memory retrieval mechanisms, and multi-view toolkit construction, plus extensive experimental validation across datasets.

### [Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning](https://arxiv.org/abs/2604.27998)
**Source:** arxiv | **Authors:** Jingcheng Deng; Zihao Wei; Liang Pang; Junhong Wu; Shicheng Xu; Zenghao Duan; Huawei Shen
**Relevance:** 4/5 — Directly addresses frontier model capability (latent reasoning) and RL training methods that enable more efficient agent reasoning, with clear methodology for stabilizing latent-space policy optimization.
**Depth:** 4/5 — Provides detailed technical methodology identifying three coupled bottlenecks in latent-space RL and proposing concrete solutions (invalid-sample masking, one-sided noise sampling, token selection), with comprehensive benchmark results across multiple difficulty tiers.

### [Kernelized Advantage Estimation: From Nonparametric Statistics to LLM Reasoning](https://arxiv.org/abs/2604.28005)
**Source:** arxiv | **Authors:** Shijin Gong; Kai Ye; Jin Zhu; Xinyu Zhang; Hongyi Zhou; Chengchun Shi
**Relevance:** 4/5 — Directly addresses RL-based training methods that materially affect LLM reasoning capabilities, a frontier capability that enables agent planning and decision-making.
**Depth:** 4/5 — Provides concrete methodology (kernel smoothing for value estimation), theoretical analysis, and comparative results addressing a real resource-constrained setting in LLM policy optimization.

### [Cost-Aware Learning](https://arxiv.org/abs/2604.28020)
**Source:** arxiv | **Authors:** Clara Mohri; Amir Globerson; Haim Kaplan; Tomer Koren; Yishay Mansour
**Relevance:** 4/5 — Directly addresses cost-efficient policy optimization for LLM-based agents through Cost-Aware GRPO, a frontier training method that materially affects agent capability and practical deployment.
**Depth:** 4/5 — Provides clear methodology (cost-aware SGD algorithm with theoretical cost complexity and lower bounds) combined with concrete empirical results (30% token reduction on 1.5B and 8B models) that advance understanding of efficient LLM agent training.

### [Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling](https://arxiv.org/abs/2604.27039)
**Source:** arxiv | **Authors:** Zhen Zhang; Changyi Yang; Zijie Xia; Zhen Yang; Chengzhi Liu; Zhaotiao Weng; Yepeng Liu; Haobo Chen;...
**Relevance:** 4/5 — Directly addresses a frontier capability for LLM agents—controlling generation length and reasoning efficiency through token-level value modeling, which improves performance-cost tradeoffs critical for agent deployment.
**Depth:** 4/5 — Provides clear methodology (value estimation formulation with constant negative reward), concrete experimental results (LIFEBench 30.9→64.8, GSM8K 63% accuracy at 200 tokens), and interpretable insights into generation dynamics that could support future agent RL training.

### [Path-Lock Expert: Separating Reasoning Mode in Hybrid Thinking via Architecture-Level Separation](https://arxiv.org/abs/2604.27201)
**Source:** arxiv | **Authors:** Shouren Wang; Wang Yang; Chuang Ma; Debargha Ganguly; Vikash Singh; Chaoda Song; Xinpeng Li; Xianxua...
**Relevance:** 4/5 — Directly addresses frontier model capability for hybrid reasoning modes (think/no-think) that materially affects LLM-based agent behavior and decision-making quality.
**Depth:** 4/5 — Provides clear architectural methodology (dual-expert MLP separation with deterministic routing), concrete benchmark results across reasoning tasks, and explicit limitations of prior work motivating the contribution.

### [Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models](https://arxiv.org/abs/2604.27251)
**Source:** arxiv | **Authors:** Xingwei Tan; Marco Valentino; Mahmud Elahi Akhter; Yuxiang Zhou; Maria Liakata; Nikolaos Aletras
**Relevance:** 4/5 — Directly addresses controllability and reasoning patterns in LLMs—core capabilities needed for reliable agent behavior—through systematic investigation of how models prioritize reasoning schemas.
**Depth:** 4/5 — Provides mechanistic methodology (reasoning conflicts framework, probing experiments, activation steering) with concrete results (29% compliance improvement, linear encoding detection) that explain *why* and *how* LLM reasoning behaves, moving beyond observation to intervention.

### [Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents](https://arxiv.org/abs/2604.27283)
**Source:** arxiv | **Authors:** Mehmet Iscan
**Relevance:** 4/5 — Directly addresses memory management and retrieval in LLM-based coding agents, a core capability for agent performance and safety.
**Depth:** 4/5 — Presents clear methodology (risk-sensitive contextual bandit formulation with 16-feature state representation) and concrete empirical results (62.5% success, 0.0% false-positive rate) with explicit safety constraints addressing prior retrieval limitations.

### [Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models](https://huggingface.co/papers/2604.27251)
**Source:** hf_papers | **Authors:** Xingwei Tan; Marco Valentino; Mahmud Elahi Akhter; Yuxiang Zhou; Maria Liakata; Nikolaos Aletras
**Relevance:** 4/5 — Directly addresses reasoning controllability and mechanistic steering of LLMs, which are foundational capabilities for building reliable and controllable LLM-based agents.
**Depth:** 4/5 — Provides systematic methodology for investigating reasoning conflicts, concrete empirical results on how models encode reasoning types, and demonstrates practical activation-level steering techniques with quantified improvements.

### [Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling](https://huggingface.co/papers/2604.27039)
**Source:** hf_papers | **Authors:** Zhen Zhang; Changyi Yang; Zijie Xia; Zhen Yang; Chengzhi Liu; Zhaotiao Weng; Yepeng Liu; Haobo Chen;...
**Relevance:** 4/5 — Length modeling via value estimation directly improves agent reasoning performance and enables inference-time control critical for agentic planning and resource-constrained deployment.
**Depth:** 4/5 — Strong methodology grounding length as a value estimation problem with dense, scalable supervision, concrete benchmarks (64.8 on LIFEBench vs 30.9 baseline, 63% GSM8K accuracy at token budget), and interpretable token-level dynamics.

### [Co-Evolving Policy Distillation](https://huggingface.co/papers/2604.27083)
**Source:** hf_papers | **Authors:** Naibin Gu; Chenxu Yang; Qingyi Si; Chuanyu Qin; Dingyu Yao; Peng Fu; Zheng Lin; Weiping Wang; Nan Du...
**Relevance:** 4/5 — Co-Evolving Policy Distillation directly addresses frontier model training methodology for consolidating multi-modal reasoning capabilities into unified models, a key enabler for capable LLM-based agents.
**Depth:** 4/5 — The paper provides clear methodology (bidirectional OPD during parallel expert training), concrete experimental validation across text/image/video reasoning, and identifies specific failure modes of prior approaches (inter-capability divergence, behavioral pattern gaps) that motivate the contribution.

### [InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?](https://huggingface.co/papers/2604.27419)
**Source:** hf_papers | **Authors:** Qiyao Wang; Haoran Hu; Longze Chen; Hongbo Wang; Hamid Alinejad-Rokny; Yuan Lin; Min Yang
**Relevance:** 4/5 — Directly addresses LLM-based agent capabilities in interactive settings, focusing on a critical failure mode (blind execution) and agent design for intent refinement through iterative interaction.
**Depth:** 4/5 — Introduces systematic methodology (four agent personas, instruction perturbations grounded in defect taxonomies, unified action space with Clarify/Implement/Verify/Submit) and concrete experimental findings exposing frontier MLLM agent limitations in adaptive interaction.

### [The Last Human-Written Paper: Agent-Native Research Artifacts](https://huggingface.co/papers/2604.24658)
**Source:** hf_papers | **Authors:** Jiachen Liu; Jiaxin Pei; Jintao Huang; Chenglei Si; Ao Qu; Xiangru Tang; Runyu Lu; Lichang Chen; Xia...
**Relevance:** 4/5 — Directly addresses a frontier capability gap for LLM-based agents—enabling them to understand, reproduce, and extend research—with concrete methodology and benchmarks.
**Depth:** 4/5 — Proposes a novel protocol (ARA) with three supporting mechanisms, demonstrates clear methodology for agent-oriented research artifacts, and reports substantial empirical gains (93.7% QA accuracy, analysis of agent constraints).

### [Heterogeneous Scientific Foundation Model Collaboration](https://huggingface.co/papers/2604.27351)
**Source:** hf_papers | **Authors:** Zihao Li; Jiaru Zou; Feihao Fang; Xuying Ning; Mengting Ai; Tianxin Wei; Sirui Chen; Xiyuan Yang; Ji...
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture and reasoning, specifically how agents can coordinate with specialized domain models through language interfaces.
**Depth:** 4/5 — Presents clear methodology (language-model-based reasoning interface augmenting domain models), architectural contributions (single-agent, multi-agent, and orchestration variants), and empirical evaluation across multiple scientific domains.

### [Large Language Models Explore by Latent Distilling](https://huggingface.co/papers/2604.24927)
**Source:** hf_papers | **Authors:** Yuanhao Zeng; Ao Lu; Lufei Li; Zheng Zhang; Yexin Li; Kan Ren
**Relevance:** 4/5 — Directly addresses test-time scaling and decoding strategies for LLM reasoning, which are core capabilities that enable agent planning and multi-step problem-solving.
**Depth:** 4/5 — Provides clear methodology (lightweight Distiller for novelty signal via prediction error), concrete empirical results across multiple benchmarks (math, science, code), and demonstrates practical efficiency gains with <5% overhead.

### [GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents](https://huggingface.co/papers/2604.26752)
**Source:** hf_papers | **Authors:** V Team; Wenyi Hong; Xiaotao Gu; Ziyang Pan; Zhen Yang; Yuting Wang; Yue Wang; Yuanchang Yue; Yu Wang...
**Relevance:** 4/5 — Directly addresses frontier multimodal LLM-based agents with integrated perception for reasoning, planning, and tool use across heterogeneous modalities.
**Depth:** 4/5 — Reports concrete methodological contributions spanning model design, multimodal training, RL optimization, tool integration, and framework-based evaluation with performance results on agent tasks.

### [Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding](https://huggingface.co/papers/2604.26779)
**Source:** hf_papers | **Authors:** Hayate Iso; Tiyasa Mitra; Sudipta Mondal; Rasoul Shafipour; Venmugil Elango; Terry Kong; Yuki Huang;...
**Relevance:** 4/5 — Directly addresses RL post-training of frontier LLMs and rollout generation efficiency, a key systems bottleneck that materially affects agent training capabilities.
**Depth:** 4/5 — Provides concrete methodology (speculative decoding integration into NeMo-RL with vLLM), empirical results (1.8x throughput at 8B, 2.5x projected at 235B), and addresses real deployment challenges in RL training pipelines.

### [ClawGym: A Scalable Framework for Building Effective Claw Agents](https://huggingface.co/papers/2604.26904)
**Source:** hf_papers | **Authors:** Fei Bai; Huatong Song; Shuang Sun; Daixuan Cheng; Yike Yang; Chuan Hao; Renyuan Li; Feng Chang; Yuan...
**Relevance:** 4/5 — ClawGym directly addresses LLM-based agent development across the full lifecycle—training data synthesis, agent training via SFT and RL, and evaluation—making it squarely on-criterion for frontier agent infrastructure.
**Depth:** 4/5 — The work provides concrete methodology (persona-driven data synthesis, hybrid verification, parallel RL pipeline), a substantial dataset (13.5K filtered tasks), trained models, and a calibrated benchmark (200 instances), demonstrating material contributions to agent training and evaluation.

### [Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents](https://arxiv.org/abs/2605.00136)
**Source:** arxiv | **Authors:** Kaituo Zhang; Zhen Xiong; Mingyu Zhong; Zhimeng Jiang; Zhouyuan Yuan; Zhecheng Li; Ying Lin
**Relevance:** 4/5 — Directly addresses a critical bottleneck in LLM-based agent tool use through empirical analysis and mechanistic understanding of tool-calling overhead.
**Depth:** 4/5 — Provides methodology (Factorized Intervention Framework isolating three cost sources), concrete empirical results on performance gaps, and proposes G-STEP with measurable improvements alongside honest limitations.

### [TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization](https://arxiv.org/abs/2605.00224)
**Source:** arxiv | **Authors:** Abdulhady Abas Abdullah; Fatemeh Daneshfar; Seyedali Mirjalili; Mourad Oussalah
**Relevance:** 4/5 — DPO is a frontier training method that directly affects LLM alignment and reasoning capabilities central to agent deployment, and this work addresses key limitations (preference robustness, reasoning quality) that constrain what agents can reliably do.
**Depth:** 4/5 — The paper presents clear methodology (topology-aware reward factorization, uncertainty weighting, RL-free objective design) and comprehensive empirical results across multiple benchmarks demonstrating measurable improvements in reasoning, faithfulness, and calibration over DPO baseline.

### [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.00425)
**Source:** arxiv | **Authors:** Haotian Zhao; Yuxin Zhang; Songlin Zhou; Stephen S. -T. Yau; Wenyu Zhang; Lun Tian; Tianshu Zhu; Yif...
**Relevance:** 4/5 — Directly addresses RL training of LLM agents through a novel credit assignment method, tackling a core technical challenge in multi-turn agentic reasoning.
**Depth:** 4/5 — Provides theoretical analysis of entropy dynamics at response level, derives a practical proxy for reshaping training, and validates across multiple model scales with concrete benchmark results including SWE-bench-Verified gains.

### [Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642)
**Source:** arxiv | **Authors:** Yan Zhang; Daiqing Wu; Huawen Shen; Yu Zhou; Can Ma
**Relevance:** 4/5 — GUI grounding is a direct application of LLM-based agents for autonomous interaction with software systems, falling squarely within agent capabilities and tool use.
**Depth:** 4/5 — The paper presents GUI-SD, a novel on-policy self-distillation framework with concrete methodology (visually enriched privileged context, entropy-guided distillation) and extensive experimental validation across six benchmarks showing improvements over GRPO baselines.

### [Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2605.00155)
**Source:** arxiv | **Authors:** Yikai Wang; Shang Liu; Jose Blanchet
**Relevance:** 4/5 — Directly addresses a frontier capability challenge in LLM agent alignment—reward over-optimization in RLHF—with a novel theoretical and algorithmic approach that affects what agents can safely optimize toward.
**Depth:** 4/5 — Provides rigorous methodology (Wasserstein DRRO framework with exact solutions under ℓ1 ambiguity, water-filling structure), theoretical analysis of why DRRO is less pessimistic than DRO, and empirical validation showing concrete improvements over existing baselines in mitigating Goodharting.

### [State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning](https://arxiv.org/abs/2605.00206)
**Source:** arxiv | **Authors:** Thea Aviss
**Relevance:** 4/5 — SST V2 directly addresses frontier model capabilities for reasoning and latent-space deliberation—mechanisms that enhance what LLM agents can do in planning and problem-solving—with concrete architectural innovation and rigorous evaluation.
**Depth:** 4/5 — The work presents clear methodology (FFN-driven recurrence, two-pass training, learned blending), mechanistic analysis (hidden state exploration of semantic basins, Bayesian posterior shifts), and strong empirical results (+15.15 GPQA-Diamond, 46% GSM8K error reduction, outperforming 25× larger models).

### [Borrowed Geometry: Computational Reuse of Frozen Text-Pretrained Transformer Weights Across Modalities](https://arxiv.org/abs/2605.00333)
**Source:** arxiv | **Authors:** Abay Bektursun
**Relevance:** 4/5 — Directly addresses frontier model capabilities and transfer learning mechanisms that enable agents to operate across modalities with frozen pretrained weights, a capability-enabling contribution for agent development.
**Depth:** 4/5 — Provides rigorous methodology (dual-measurement protocol, architecture-alone falsifications, head-level mechanistic analysis) with concrete quantitative results (8.7× advantage on associative recall, SOTA on robotic manipulation) and explicit limitations of from-scratch training baselines.

### [Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity](https://arxiv.org/abs/2605.00365)
**Source:** arxiv | **Authors:** Anamika Lochab; Bolian Li; Ruqi Zhang
**Relevance:** 4/5 — Directly addresses RL training methods for LLM-based reasoning agents, improving multi-sample diversity and capability on math reasoning tasks—a frontier agent capability.
**Depth:** 4/5 — Provides formal analysis of diversity collapse mechanism, derives optimal policy structure, proposes concrete algorithmic modification (UCPO), and includes comprehensive empirical evaluation across models and benchmarks with measurable improvements.

### [ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning](https://arxiv.org/abs/2605.00380)
**Source:** arxiv | **Authors:** Zihan Lin; Xiaohan Wang; Jie Cao; Jiajun Chai; Li Wang; Xiaodong Lu; Wei Lin; Ran He; Guojun Yin
**Relevance:** 4/5 — Directly addresses frontier LLM reasoning enhancement via RL training methodology, with explicit evaluation on agent tasks and mathematical reasoning—core capabilities enabling LLM-based agents.
**Depth:** 4/5 — Provides clear methodology (SVD-based projection, gradient modulation), theoretical grounding (LLD-gradient interference link), and concrete benchmarked results across twelve domains including agent tasks and code.

### [Hierarchical Abstract Tree for Cross-Document Retrieval-Augmented Generation](https://arxiv.org/abs/2605.00529)
**Source:** arxiv | **Authors:** Ziwen Zhao; Menglin Yang
**Relevance:** 4/5 — Directly addresses RAG-enhanced LLM agents with explicit methodology for hierarchical retrieval and agent-powered hybrid retrieval mechanisms that materially affect agent capability.
**Depth:** 4/5 — Provides concrete architectural contributions (iterative merging-collapse process, multi-granular retrieval agent), detailed methodology addressing prior limitations, and strong empirical results on cross-document QA benchmarks.

### [Decouple before Integration: Test-time Synthesis of SFT and RLVR Task Vectors](https://arxiv.org/abs/2605.00610)
**Source:** arxiv | **Authors:** Chaohao Yuan; Chenghao Xiao; Yu Rong; Hong Cheng; Long-Kai Huang
**Relevance:** 4/5 — Directly addresses frontier LLM post-training methods (SFT and RLVR) that materially affect model capabilities for reasoning and knowledge, which are foundational for agent performance.
**Depth:** 4/5 — Provides rigorous methodology with structural analysis (task vectors, magnitude/sign properties), concrete empirical results across benchmarks, and a novel inference-time synthesis approach with explicit computational cost comparison.

### [Evaluating the Architectural Reasoning Capabilities of LLM Provers via the Obfuscated Natural Number Game](https://arxiv.org/abs/2605.00677)
**Source:** arxiv | **Authors:** Lixing Li
**Relevance:** 4/5 — Directly evaluates frontier model reasoning capabilities (mathematical proof synthesis) with a novel methodology to distinguish genuine reasoning from pattern matching, which materially affects understanding of LLM agent capabilities for formal reasoning and theorem discovery.
**Depth:** 4/5 — Provides clear methodology (obfuscation benchmark design), concrete comparative results across models (general vs. reasoning models), and identifies a quantitative distinction (latency tax and robustness divergence) that reveals mechanistic differences in how models approach reasoning tasks.

### [RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution](https://arxiv.org/abs/2605.00798)
**Source:** arxiv | **Authors:** Arunabh Srivastava (Amir); Mohammad A. (Amir); Khojastepour; Srimat Chakradhar; Sennur Ulukus
**Relevance:** 4/5 — Directly addresses LLM-based agent planning and execution with explicit methodology for structured workflow control, constraint validation, and tool use.
**Depth:** 4/5 — Presents concrete architectural mechanisms (agentic language with control constructs, constraint derivation, dynamic tool selection, error correction) and evaluation on benchmark datasets demonstrating improvements over baselines.

### [RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners](https://arxiv.org/abs/2605.00199)
**Source:** arxiv | **Authors:** Jugal Gajjar; Kamalasankari Subramaniakuppusamy
**Relevance:** 4/5 — Directly addresses agent interpretability and reasoning verification through structured attribution, enabling faithful multi-step reasoning in LLM-based systems that must justify decisions.
**Depth:** 4/5 — Presents concrete methodology (two-phase training with SFT + GRPO), quantified results across six models (3.7× faithfulness improvement, 0.992 citation validity), and ablations demonstrating reward criticality.

### [Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions](https://arxiv.org/abs/2605.00226)
**Source:** arxiv | **Authors:** Jan Sobotka; Mustafa O. Karabag; Ufuk Topcu
**Relevance:** 4/5 — Directly addresses frontier model capabilities—reasoning, planning, and belief formation—that materially affect LLM-based agent performance in strategic decision-making tasks.
**Depth:** 4/5 — Provides systematic methodology for probing internal mechanisms (observation-belief gap, belief-action gap) with concrete experimental results on reasoning failures across multiple models, exposing architectural vulnerabilities relevant to agent deployment.

### [MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents](https://arxiv.org/abs/2605.00356)
**Source:** arxiv | **Authors:** Tianyu Hu; Weikai Lin; Weizhi Zhang; Jing Ma; Song Wang
**Relevance:** 4/5 — Directly addresses a core LLM-agent capability: memory management for long-term conversational agents, with methodology and concrete benchmark results on a controlled task.
**Depth:** 4/5 — Provides clear methodology (embedding-based routing with frozen LLM backbone + lightweight classifiers), controlled experimental comparison with matched harness, factorial analysis isolating contributions, and latency improvements alongside performance gains.

### [Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.00410)
**Source:** arxiv | **Authors:** Aninda Ray
**Relevance:** 4/5 — Directly addresses LLM-based multi-agent pipeline execution, optimization, and quality control—core agent system infrastructure.
**Depth:** 4/5 — Presents concrete methodology (three-tier execution strategies, quality-gated routing, empirical constraints) with detailed benchmarks (51% token savings, quality parity/gains) on real multi-agent systems.

### [Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output](https://arxiv.org/abs/2605.00557)
**Source:** arxiv | **Authors:** James Mooney; Zae Myung Kim; Young-Jun Lee; Dongyeop Kang
**Relevance:** 4/5 — Directly addresses LLM-based agent planning and reasoning through a structured sensemaking framework that improves downstream agent performance in research tasks.
**Depth:** 4/5 — Provides clear methodology (eight-stage cognitive framework, 100K dataset construction, dual training modes), concrete quantitative results (2.0% improvement, executability/quality metrics), and mechanistic insight into how planning structure enables agent creativity.

### [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](https://arxiv.org/abs/2605.00702)
**Source:** arxiv | **Authors:** Derong Xu; Shuochen Liu; Pengfei Luo; Pengyue Jia; Yingyi Zhang; Yi Wen; Yimin Deng; Wenlin Zhang; E...
**Relevance:** 4/5 — Directly addresses memory architecture for LLM agents, a core capability enabler for long-horizon personalization and reasoning.
**Depth:** 4/5 — Presents a cognition-inspired two-stage optimization framework with explicit methodology (contrastive feedback, multi-turn RL with structured rewards) and evaluation on multiple personalization benchmarks.

### [When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models](https://arxiv.org/abs/2605.00817)
**Source:** arxiv | **Authors:** Sailesh Panda; Pritam Kadasi; Abhishek Upperwal; Mayank Singh
**Relevance:** 4/5 — Directly addresses a critical failure mode in LLM procedural execution that materially affects agent capability to follow multi-step plans and algorithms.
**Depth:** 4/5 — Provides systematic diagnostic methodology with controlled benchmarks across 14 models and 55 datasets, identifies specific failure modes (missing steps, hallucinated steps, premature termination), and reveals the gap between reasoning benchmarks and faithful execution.

### [From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills](https://huggingface.co/papers/2604.24026)
**Source:** hf_papers | **Authors:** Qiliang Liang; Hansi Wang; Zhong Liang; Yang Liu
**Relevance:** 4/5 — Directly addresses skill representation and management for LLM-based agents, a core capability that enables agent reasoning, planning, and tool use.
**Depth:** 4/5 — Introduces a novel structured representation (SSL) with clear methodology grounded in classical knowledge representation theory, and provides concrete evaluation results on two tasks with measurable improvements over baselines.

### [Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring](https://huggingface.co/papers/2605.00754)
**Source:** hf_papers | **Authors:** Indraneil Paul; Glavaš Glavas; Iryna Gurevych
**Relevance:** 4/5 — Reward models are a frontier capability that directly enables test-time scaling and policy alignment in LLMs, both critical infrastructure for agent reasoning and planning.
**Depth:** 4/5 — The work provides substantial methodology (multi-criteria RM training, cross-lingual transfer mechanisms), concrete results (350k+ preference pairs, scaling trends across 600M-32B models, benchmarks on 8 languages), and clear ablations demonstrating importance of design choices.

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

### [Think it, Run it: Autonomous ML pipeline generation via self-healing multi-agent AI](https://arxiv.org/abs/2604.27096)
**Source:** arxiv | **Authors:** Adela Bara; Gabriela Dobrita; Simona-Vasilica Oprea
**Relevance:** 4/5 — Multi-agent LLM system for planning, tool use (microservice recommendation), and execution with error recovery directly addresses agent reasoning and deployment.
**Depth:** 3/5 — Provides concrete methodology (five-agent architecture, code-grounded RAG, self-healing mechanism) and quantitative results (84.7% success rate on 150 tasks), though the contribution is primarily systems integration rather than novel capability insights.

### [Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems](https://arxiv.org/abs/2604.27358)
**Source:** arxiv | **Authors:** Yuan Sun
**Relevance:** 4/5 — Directly addresses runtime safety and delegation in hierarchical LLM multi-agent systems, a frontier concern for deploying agents in high-stakes environments.
**Depth:** 3/5 — Establishes formal theoretical results (safety monotonicity, convergence, accountability bounds) and specifies evaluation protocols across three domains, though empirical validation is only planned.

### [Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents](https://arxiv.org/abs/2604.27699)
**Source:** arxiv | **Authors:** Chunhui Zhang; Yuxuan Wang; Aoyang Qin; Yi-Long Lu; Kunlun Wu; Yizhou Wang; Wei Wang
**Relevance:** 4/5 — Directly addresses LLM-based agent architecture for long-horizon reasoning, planning, and value alignment—core agent capabilities—with a concrete hierarchical framework combining LLM reasoning with classical planning.
**Depth:** 3/5 — Solid methodology coupling LLM-based value reasoning with PDDL planning and closed-loop refinement, plus novel value-centric evaluation metrics, though the empirical validation is limited to a single household simulation environment.

### [KellyBench: A Benchmark for Long-Horizon Sequential Decision Making](https://arxiv.org/abs/2604.27865)
**Source:** arxiv | **Authors:** Thomas Grady; Kip Parker; Iliyan Zarov; Henry Course; Chengxi Taylor; Ross Taylor
**Relevance:** 4/5 — KellyBench directly evaluates LLM agent capabilities in long-horizon sequential decision-making with open-ended goals, a frontier challenge for agent deployment.
**Depth:** 3/5 — The work provides concrete evaluation results (returns, rubric scores) and identifies specific limitations of frontier models, though methodology for agent reasoning/planning is not the primary contribution.

### [Collaborative Agent Reasoning Engineering (CARE): A Three-Party Design Methodology for Systematically Engineering AI Agents with Subject Matter Experts, Developers, and Helper Agents](https://arxiv.org/abs/2604.28043)
**Source:** arxiv | **Authors:** Rahul Ramachandran; Nidhi Jha; Muthukumaran Ramasubramanian
**Relevance:** 4/5 — Directly addresses LLM agent engineering methodology covering reasoning, tool orchestration, verification, and deployment with systematic design practices.
**Depth:** 3/5 — Presents a structured methodology with stage-gated phases and artifact-driven design, but lacks detailed algorithmic innovation or comprehensive quantitative benchmarking across diverse agent tasks.

### [Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence](https://huggingface.co/papers/2604.24954)
**Source:** hf_papers | **Authors:** NVIDIA; Amala Sanjay Deshmukh; Kateryna Chumachenko; Tuomas Rintamaki; Matthieu Le; Tyler Poon; Dani...
**Relevance:** 4/5 — Frontier multimodal model with explicit agentic computer use capabilities and architectural innovations directly enabling agent reasoning over diverse modalities.
**Depth:** 3/5 — Provides concrete methodology (multimodal token-reduction techniques, architecture advances, training recipes) and results across benchmarks including agentic tasks, though lacks detailed ablations or mechanistic analysis.

### [FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments](https://huggingface.co/papers/2604.25135)
**Source:** hf_papers | **Authors:** Amir Saeidi; Venkatesh Mishra; Souradeep Mukhopadhyay; Gaowen Liu; Ali Payani; Jayanth Srinivasa; Ch...
**Relevance:** 4/5 — Directly addresses LLM-based agent failure modes, tool use, and decision-making in interactive environments, which are core agent capabilities.
**Depth:** 3/5 — Presents a clear methodology (failure analysis + orchestration of specialized agents) with concrete experimental results (27% improvement), though the contribution is more of a practical engineering pattern than a fundamental capability advance.

### [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://huggingface.co/papers/2604.25256)
**Source:** hf_papers | **Authors:** Lei Xiong; Kun Luo; Ziyi Xia; Wenbo Zhang; Jin-Ge Yao; Zheng Liu; Jingying Shao; Jianlyu Chen; Hongj...
**Relevance:** 4/5 — Directly addresses LLM-based agent evaluation through a specialized benchmark measuring reasoning, planning, and tool use in scientific literature discovery tasks.
**Depth:** 3/5 — Provides concrete evaluation methodology and results (9.39% and 9.31% accuracy on task types) but focuses primarily on benchmark design rather than advancing agent architecture or capability mechanisms.

### [TADI: Tool-Augmented Drilling Intelligence via Agentic LLM Orchestration over Heterogeneous Wellsite Data](https://arxiv.org/abs/2605.00060)
**Source:** arxiv | **Authors:** Rong Lu
**Relevance:** 4/5 — Directly addresses LLM-based agent design with explicit methodology for tool orchestration, function calling, and multi-step reasoning over heterogeneous data sources.
**Depth:** 3/5 — Provides concrete methodology (dual-store architecture, 12 domain-specialized tools, iterative function calling) and substantive evaluation (95 tests, Evidence Grounding Score metric, qualitative ablation), though the contribution is domain-application focused rather than advancing frontier agent or model capabilities.

### [Position: agentic AI orchestration should be Bayes-consistent](https://arxiv.org/abs/2605.00742)
**Source:** arxiv | **Authors:** Theodore Papamarkou; Pierre Alquier; Matthias Bauer; Wray Buntine; Andrew Davison; Gintare Karolina ...
**Relevance:** 4/5 — Directly addresses orchestration and decision-making in LLM-based agent systems, a core frontier capability for agentic AI.
**Depth:** 3/5 — Articulates clear methodology (Bayesian decision theory applied to agent control layers) with design patterns and concrete examples, though it is a position paper rather than empirical validation.

### [Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding](https://arxiv.org/abs/2605.00342)
**Source:** arxiv | **Authors:** Lehan Pan; Ziyang Tao; Ruoyu Pang; Xiao Wang; Jianjun Zhao; Yanyong Zhang
**Relevance:** 4/5 — Directly addresses inference optimization for LLM-based systems through speculative decoding, a technique that materially affects deployment efficiency and agent response latency.
**Depth:** 3/5 — Provides clear methodology (adaptive tree truncation using drafter signals and offline cost profiling), concrete speedup results (2.35x over baseline, 1.21x over EAGLE-3), and identifies specific limitations of prior work (expert activation expansion in MoE models).

### [A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction](https://arxiv.org/abs/2605.00551)
**Source:** arxiv | **Authors:** Michito Takeshita; Takuro Kawada; Takumi Ohashi; Shunsuke Kitada; Hitoshi Iyatomi
**Relevance:** 4/5 — Directly addresses a frontier capability for LLM-based GUI agents: efficient observation representation and grounding, which materially affects agent performance and scalability.
**Depth:** 3/5 — Provides concrete methodology (modal detection, redundancy reduction, semantic structuring) and quantified results (22% token reduction, 5.1pp success gain on OSWorld), though the contribution is narrowly focused on representation optimization rather than architectural innovation.

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


## Worth knowing (64 items)

_On-criterion but lower depth, or peripheral relevance._

### [Rethinking Agentic Reinforcement Learning In Large Language Models](https://arxiv.org/abs/2604.27859)
**Source:** arxiv | **Authors:** Fangming Cui; Ruixiao Zhu; Cheng Fang; Sunan Li; Jiahong Li
**Relevance:** 4/5 — Directly addresses LLM-based agents with focus on RL integration, goal-setting, planning, reasoning, and decision-making—core frontier agent capabilities.
**Depth:** 2/5 — Appears to be a position/survey paper outlining conceptual foundations and challenges rather than presenting concrete methodology, novel mechanisms, or quantitative results.

### [Olmo Hybrid and future LLM architectures](https://www.interconnects.ai/p/olmo-hybrid-and-future-llm-architectures)
**Source:** interconnects | **Authors:** Nathan Lambert
**Relevance:** 4/5 — Hybrid LLM architectures (mixing attention with RNNs/Gated DeltaNet) directly affect model capabilities and efficiency that enable agent reasoning and deployment, representing a frontier architectural shift.
**Depth:** 2/5 — The piece provides historical context and overview of hybrid model adoption but lacks concrete methodology details, benchmark results, or rigorous evaluation of how these architectural choices impact agent-relevant capabilities like reasoning or tool use.

### [Position: How can Graphs Help Large Language Models?](https://arxiv.org/abs/2605.02452)
**Source:** arxiv | **Authors:** Xiyuan Wang; Yi Hu; Yanbo Wang; Chuan Shi; Muhan Zhang
**Relevance:** 4/5 — Directly addresses how graphs enhance LLM reasoning and planning through prompting techniques (CoT, ToT, GoT) and knowledge integration, which are core capabilities for LLM-based agents.
**Depth:** 2/5 — Position paper that surveys existing techniques and outlines directions rather than presenting novel methodology, concrete benchmarks, or detailed mechanistic insights into graph-LLM integration.

### [When Roles Fail: Epistemic Constraints on Advocate Role Fidelity in LLM-Based Political Statement Analysis](https://arxiv.org/abs/2604.27228)
**Source:** arxiv | **Authors:** Juergen Dietrich
**Relevance:** 3/5 — Directly studies a critical failure mode in multi-agent LLM pipelines used for structured analysis, providing methodology and empirical results on role fidelity—a capability constraint affecting agent reliability.
**Depth:** 4/5 — Introduces systematic measurement framework (four metrics), identifies two distinct failure modes unified under epistemic role override mechanism, and provides concrete cross-model and cross-language comparisons with statistical significance testing.

### [The Two Boundaries: Why Behavioral AI Governance Fails Structurally](https://arxiv.org/abs/2604.27292)
**Source:** arxiv | **Authors:** Alan L. McCann
**Relevance:** 3/5 — Directly addresses governance of LLM agent effects (tool invocation, API calls) with formal methodology, but is primarily a governance/safety framework rather than agent capability or training work.
**Depth:** 4/5 — Rigorous formal framework with mechanized proofs in Coq and clear architectural analysis of the expressiveness-governance boundary gap, providing substantial methodology applicable to agent deployment systems.

### [AutoSP: Unlocking Long-Context LLM Training Via Compiler-Based Sequence Parallelism](https://arxiv.org/abs/2604.27089)
**Source:** arxiv | **Authors:** Ahan Gupta; Zhihao Wang; Neel Dani; Masahiro Tanaka; Olatunji Ruwase; Minjia Zhang
**Relevance:** 3/5 — Long-context training infrastructure is adjacent to agent capabilities but not directly about LLM agents, reasoning, planning, or tool use—it's a training optimization that enables longer context windows which agents could leverage.
**Depth:** 4/5 — The work provides concrete methodology (compiler-based sequence parallelism and activation checkpointing), quantitative results (2.7× context increase on NVIDIA), and addresses a clear limitation of existing training libraries, demonstrating solid systems contribution.

### [Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains](https://huggingface.co/papers/2604.24902)
**Source:** hf_papers | **Authors:** Emaan Bilal Khan; Amy Winecoff; Miranda Bogen; Dylan Hadfield-Menell
**Relevance:** 3/5 — Safety drift in fine-tuned models is relevant to agent deployment but focuses on base model adaptation rather than agent-specific reasoning, planning, or tool-use capabilities.
**Depth:** 4/5 — Provides rigorous empirical methodology (100 models across domains), concrete safety benchmark results, and explicit identification of limitations in current governance that materially affect downstream model safety—key for deployment contexts.

### [Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists](https://huggingface.co/papers/2604.28158)
**Source:** hf_papers | **Authors:** Yujun Wu; Dongxu Zhang; Xinchen Li; Jinhang Xu; Yiling Duan; Yumou Liu; Jiabao Pan; Xuanhe Zhou; Jin...
**Relevance:** 3/5 — Directly targets infrastructure for AI research agents to consume scientific knowledge and reconstruct methodological evolution, which is a supporting capability for agent-based scientific discovery rather than core agent reasoning or frontier model capabilities.
**Depth:** 4/5 — Presents concrete methodology (graph construction from 1M+ papers, temporal tree search algorithm, typing of 9.4M edges) with evaluation against ground-truth chains and demonstrated downstream applications, though focused on infrastructure rather than agent mechanisms themselves.

### [Minimal, Local, Causal Explanations for Jailbreak Success in Large Language Models](https://arxiv.org/abs/2605.00123)
**Source:** arxiv | **Authors:** Shubham Kumar; Narendra Ahuja
**Relevance:** 3/5 — This work addresses LLM safety and jailbreak robustness through mechanistic interpretability, which is relevant to understanding frontier model vulnerabilities but is primarily a safety/robustness study rather than directly about agent capabilities or training methods that enable agent functionality.
**Depth:** 4/5 — The paper presents LOCA, a systematic methodology with causal intervention experiments that identifies minimal sets of intermediate representation changes needed to induce refusal, demonstrating substantially better performance (6 vs 20+ changes) than prior work with clear mechanistic insights.

### [Affinity Is Not Enough: Recovering the Free Energy Principle in Mixture-of-Experts](https://arxiv.org/abs/2605.00604)
**Source:** arxiv | **Authors:** Man Yung Wong (Russell)
**Relevance:** 3/5 — Mixture-of-Experts routing improvements are relevant to scaling and efficiency of frontier models that underpin LLM agents, but the work is primarily about model architecture rather than agent capabilities or reasoning directly.
**Depth:** 4/5 — The paper provides clear methodology (three lightweight gate modifications with mechanistic grounding in Free Energy Principle and spiking networks), controlled experiments with ablations revealing super-additive interactions, concrete quantitative results (124x improvement, 75% oracle gap closure), and public implementations.

### [How Language Models Process Out-of-Distribution Inputs: A Two-Pathway Framework](https://arxiv.org/abs/2605.00269)
**Source:** arxiv | **Authors:** Hamidreza Saghir
**Relevance:** 3/5 — Addresses model robustness and safety detection relevant to agent deployment, but OOD detection is peripheral to core agent capabilities like reasoning, planning, and tool use.
**Depth:** 4/5 — Provides solid methodology with deconfounding analysis, multi-pathway framework with AUROC results, circuit attribution evidence, and reveals structural limitations of prior detection methods.

### [Escaping Mode Collapse in LLM Generation via Geometric Regulation](https://arxiv.org/abs/2605.00435)
**Source:** arxiv | **Authors:** Xin Du; Kumiko Tanaka-Ishii
**Relevance:** 3/5 — Addresses a core generation quality issue affecting LLM agent reliability and output stability, but is a decoding-level technique rather than agent architecture or frontier model capability.
**Depth:** 4/5 — Provides clear mechanistic insight (geometric collapse in representation space), concrete methodology (low-rank damping in value cache), and substantial empirical results (entropy reduction from 2.0 to 0.8 nats/step across multiple models).

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

### [TRUST: A Framework for Decentralized AI Service v.0.1](https://arxiv.org/abs/2604.27132)
**Source:** arxiv | **Authors:** Yu-Chao Huang; Zhen Tan; Mohan Zhang; Pingzhi Li; Zhuo Zhang; Tianlong Chen
**Relevance:** 3/5 — Addresses verification and trustworthiness of LLM-based reasoning systems and multi-agent deployments, which is relevant to agent safety and evaluation, but focuses on decentralized auditing infrastructure rather than core agent capabilities or reasoning mechanisms.
**Depth:** 3/5 — Provides concrete technical contributions (HDAGs for reasoning decomposition, DAAN protocol for attribution, consensus mechanisms) with empirical results (72.4% accuracy, 70% root-cause attribution) and human validation, but the core novelty lies in auditing architecture rather than fundamental advances in agent reasoning or capability emergence.

### [Knowledge Graph Representations for LLM-Based Policy Compliance Reasoning](https://arxiv.org/abs/2604.27713)
**Source:** arxiv | **Authors:** Wilder Baldwin; Sepideh Ghanavati
**Relevance:** 3/5 — The paper presents an LLM-based agentic system for reasoning over policy documents using knowledge graphs, which touches on agent reasoning and knowledge retrieval, but policy compliance is a specialized application rather than frontier agent capability development.
**Depth:** 3/5 — The work includes concrete methodology (KG construction from policies, two ontology schemas, evaluation across six reasoning types) and quantitative results (improvements for five LLM models), but the core contribution is primarily an application of existing techniques rather than new agent mechanisms or frontier model capabilities.

### [Modeling Clinical Concern Trajectories in Language Model Agents](https://arxiv.org/abs/2604.27872)
**Source:** arxiv | **Authors:** Sukesh Subaharan; Venkatesan VS; Murugadasan P; Sivakumar D; Gautham N; Ganeshkumar M
**Relevance:** 3/5 — Addresses LLM-based agent behavior (memory, state dynamics, monitoring) in a specialized domain, but focuses on clinical interpretability rather than frontier capabilities or core agent architecture patterns.
**Depth:** 3/5 — Presents clear methodology (state dynamics integration for risk encoding) and concrete results (comparison of stateless vs. second-order dynamics), but the contribution is domain-specific and incremental rather than methodologically foundational for agents broadly.

### [Graph World Models: Concepts, Taxonomy, and Future Directions](https://arxiv.org/abs/2604.27895)
**Source:** arxiv | **Authors:** Jiawei Liu; Senqiao Yang; Mingjun Wang; Yu Wang; Bei Yu
**Relevance:** 3/5 — Graph world models are relevant to agent reasoning and planning capabilities, but this is a taxonomy/survey paper rather than work directly advancing frontier LLM-based agent capabilities or model training methods.
**Depth:** 3/5 — The paper provides systematic formalization and unification of graph world models with principled taxonomy based on relational inductive biases, offering methodological substance, but does not present novel empirical results or breakthrough architectural insights that materially shift frontier agent capabilities.

### [Agent-Agnostic Evaluation of SQL Accuracy in Production Text-to-SQL Systems](https://arxiv.org/abs/2604.28049)
**Source:** arxiv | **Authors:** Taslim Jamal Arif; Kuldeep Singh
**Relevance:** 3/5 — Text-to-SQL evaluation is relevant to agent deployment and monitoring, but the work focuses on evaluation methodology rather than agent reasoning, planning, or capability emergence.
**Depth:** 3/5 — The paper presents a concrete evaluation framework (STEF) with clear methodology for production T2SQL systems, including specific normalization techniques and metrics, but lacks frontier model insights or agent capability analysis.

### [RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses](https://arxiv.org/abs/2604.28056)
**Source:** arxiv | **Authors:** Feiyu Wu; Xu Zheng; Zhuocheng Wang; Yi ming Dai; Hui Li
**Relevance:** 3/5 — This addresses reward design for RL agents via LLM generation, which is relevant to agent capability but focuses on a narrow deployment problem rather than core agent reasoning, planning, or tool use.
**Depth:** 3/5 — The paper provides clear methodology (competence-aware verification, phase-aware deployment protocol) and empirical results (reward ranking reliability thresholds, performance improvements), but the contribution is specialized to reward hypothesis deployment rather than foundational agent capabilities.

### [Diagnosing Capability Gaps in Fine-Tuning Data](https://arxiv.org/abs/2604.27547)
**Source:** arxiv | **Authors:** Saeid Asgari Taghanaki; Rakshanda Agarwal; Bruce Sun; Rohan Jha; Elias Stengel-Eskin; Sara Malvar; R...
**Relevance:** 3/5 — Fine-tuning dataset diagnostics are adjacent to agent development but not directly about agent reasoning, planning, or tool use; the work supports model capability engineering rather than agent-specific capabilities.
**Depth:** 3/5 — GoalCover presents a systematic methodology for detecting capability gaps with controlled experiments and downstream validation, but the contribution is primarily a diagnostic tool for dataset curation rather than advancing core LLM or agent capabilities.

### [Optimized Deferral for Imbalanced Settings](https://arxiv.org/abs/2604.27723)
**Source:** arxiv | **Authors:** Corinna Cortes; Anqi Mao; Mehryar Mohri; Yutao Zhong
**Relevance:** 3/5 — Learning to defer with LLM routing is relevant to agent capability systems, but the paper focuses on a general routing optimization problem rather than LLM-based agent reasoning, planning, or tool use.
**Depth:** 3/5 — The paper provides solid methodology (cost-sensitive learning framework, margin-based losses, novel algorithms) and experimental validation on LLM routing tasks, but the technical contribution is primarily in the optimization/learning problem formulation rather than advancing agent capabilities.

### [CL-bench Life: Can Language Models Learn from Real-Life Context?](https://arxiv.org/abs/2604.27043)
**Source:** arxiv | **Authors:** Shihan Dou; Yujiong Shen; Chenhao Huang; Junjie Ye; Jiayi Chen; Junzhe Wang; Qianyu He; Shichun Liu;...
**Relevance:** 3/5 — Context learning is relevant to LLM agent capabilities, but this work is primarily a benchmark paper evaluating model performance rather than advancing agent architecture, reasoning, or tool use.
**Depth:** 3/5 — The paper provides solid empirical contribution (405 curated pairs, 5,348 rubrics, evaluation of 10 frontier models) and identifies a real limitation (19.3% best performance), but lacks novel methodology for addressing the problem or mechanistic insights into why models fail.

### [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](https://arxiv.org/abs/2604.27393)
**Source:** arxiv | **Authors:** Junbo Cui; Bokai Xu; Chongyi Wang; Tianyu Yu; Weiyue Sun; Yingjing Xu; Tianran Wang; Zhihui He; Wens...
**Relevance:** 3/5 — The work addresses frontier multimodal model capabilities (real-time streaming, proactive behavior) that materially expand what LLM-based agents can do, but focuses on interaction architecture rather than agent reasoning/planning directly.
**Depth:** 3/5 — Presents a concrete technical contribution (Omni-Flow framework for full-duplex alignment) with comparative benchmarks and efficiency claims, though the paper appears to emphasize capability demonstration over detailed methodology exposition.

### [FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption](https://huggingface.co/papers/2604.28157)
**Source:** hf_papers | **Authors:** Yanting Wang; Chenlong Yin; Ying Chen; Jinyuan Jia
**Relevance:** 3/5 — Directly addresses security evaluation of long-context LLMs used in agents and RAG systems, but focuses on red-teaming methodology rather than agent capabilities or frontier model advances.
**Depth:** 3/5 — Provides solid technical methodology (optimization techniques for efficient attacks) and concrete benchmarks (2-7x speedup, 2-4x memory reduction), but is primarily an engineering contribution to evaluation rather than advancing core agent or model capabilities.

### [Causal Foundations of Collective Agency](https://arxiv.org/abs/2605.00248)
**Source:** arxiv | **Authors:** Frederik Hytting J{\o}rgensen; Sebastian Weichwald; Lewis Hammond
**Relevance:** 3/5 — Addresses safety and emergent behavior in multi-agent AI systems, which is tangentially related to agent capabilities and control, but focuses on theoretical foundations rather than LLM-based agents or frontier model capabilities.
**Depth:** 3/5 — Provides formal methodology (causal games and causal abstraction framework) for analyzing collective agency with concrete applications (voting mechanisms, actor-critic models), but lacks empirical results on actual LLM or frontier agent systems.

### [Caracal: Causal Architecture via Spectral Mixing](https://arxiv.org/abs/2605.00292)
**Source:** arxiv | **Authors:** Bingzheng Gan; Tianyi Zhang; Yusu Li; Jing Huang; Wei Shi; Yangkai Ding; Tao Yu
**Relevance:** 3/5 — Caracal addresses frontier model capabilities (long-sequence efficiency, architecture alternatives to attention) that affect what agents can accomplish, but is a general-purpose architectural contribution rather than agent-specific methodology.
**Depth:** 3/5 — The work presents solid technical contributions (FFT-based mixing with frequency-domain causal masking, competitive benchmarks) with clear methodology, but lacks explicit evaluation on agent tasks or reasoning capabilities that would make it high-priority for agent research.

### [Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance](https://arxiv.org/abs/2605.00553)
**Source:** arxiv | **Authors:** Minchan Kwon; Sunghyun Baek; Minseo Kim; Jaemyung Yu; Dongyoon Han; Junmo Kim
**Relevance:** 3/5 — Red-teaming LLMs is adjacent to agent safety and robustness, but the paper focuses on attack generation methodology rather than agent reasoning, planning, or capabilities that enable agentic behavior.
**Depth:** 3/5 — The paper provides solid technical methodology (Stable-GFN with partition function elimination and contrastive balancing) and demonstrates empirical results, but the contribution is specialized to red-teaming reward stability rather than advancing core agent or frontier model capabilities.

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

### [Reading today's open-closed performance gap](https://www.interconnects.ai/p/reading-todays-open-closed-performance)
**Source:** interconnects | **Authors:** Nathan Lambert
**Relevance:** 3/5 — Discusses agentic benchmarking and model evaluation gaps that affect agent capability assessment, but is primarily a meta-analysis of benchmarking dynamics rather than agent methodology or frontier capability work.
**Depth:** 2/5 — Offers conceptual observations about benchmark-reality misalignment and mentions agentic benchmarks, but lacks concrete methodology, specific evaluation results, or technical insight into what makes agents work better.

### [H-RAG at SemEval-2026 Task 8: Hierarchical Parent-Child Retrieval for Multi-Turn RAG Conversations](https://arxiv.org/abs/2605.00631)
**Source:** arxiv | **Authors:** Passant Elchafei; Hossam Emam; Mohamed Alansary; Monorama Swain; Markus Schedl
**Relevance:** 3/5 — H-RAG addresses multi-turn RAG in conversational settings, which is relevant to LLM-based agent capabilities, but is a task-specific system submission rather than frontier methodology or model capability work.
**Depth:** 2/5 — The paper describes a hierarchical chunking and retrieval pipeline with standard components (hybrid search, rescoring, aggregation) applied to an evaluation benchmark, but lacks novel methodology or deep insights into why these design choices matter for agent reasoning or capability.

### [Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs](https://arxiv.org/abs/2605.00674)
**Source:** arxiv | **Authors:** Jasper Dekoninck; Nikola Jovanovi\'c; Tim Gehrunger; K\'ari R\"ognvalddson; Ivo Petrov; Chenhao Sun;...
**Relevance:** 3/5 — Mathematical reasoning evaluation is tangentially relevant to LLM-based agents, but the work is primarily a benchmarking platform rather than advancing agent capabilities, reasoning mechanisms, or deployment methodologies.
**Depth:** 2/5 — The paper presents an evaluation framework and benchmark aggregation system with performance metrics, but lacks methodology insights into how agents reason, plan, or use tools, and does not explain mechanisms that enable the capability improvements shown.

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

### [Building Persona-Based Agents On Demand: Tailoring Multi-Agent Workflows to User Needs](https://arxiv.org/abs/2604.27882)
**Source:** arxiv | **Authors:** Giuseppe Arbore; Andrea Sillano; Luigi De Russis
**Relevance:** 3/5 — Directly addresses LLM-based multi-agent system design and personalization, but focuses on orchestration and runtime configuration rather than core agent capabilities or frontier model advances.
**Depth:** 1/5 — Proposes a conceptual pipeline for on-demand persona generation without concrete methodology details, evaluation results, or technical depth on how personalization mechanisms function.

### [Reliable AI Needs to Externalize Implicit Knowledge: A Human-AI Collaboration Perspective](https://arxiv.org/abs/2605.02010)
**Source:** arxiv | **Authors:** Hengyu Liu; Tianyi Li; Zhihong Cui; Yushuai Li; Zhangkai Wu; Torben Bach Pedersen; Kristian Torp; Ch...
**Relevance:** 3/5 — Addresses reliability and verification of LLM reasoning—a real concern for deployed agents—but is a position paper proposing a framework rather than demonstrating empirical methodology or results on agent-specific problems.
**Depth:** 1/5 — Identifies a genuine problem (implicit knowledge verification) and sketches a conceptual solution (Knowledge Objects), but provides no concrete methodology, algorithms, empirical evaluation, or case studies demonstrating how KOs would work in practice.

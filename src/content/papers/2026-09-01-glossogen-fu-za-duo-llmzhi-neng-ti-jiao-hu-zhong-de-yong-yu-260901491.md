---
title: 'GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions'
title_zh: 《GlossoGen：复杂多LLM智能体交互中的涌现语言研究》
authors:
- Elias Stengel-Eskin
- Newton Sander
- Carlos Bonetti
- Sasha Boguraev
- James Bowler
- Hale Sirin
- Simon Kirby
affiliations:
- University of Texas at Austin
- AE Studio
- Schmidt Sciences
- University of Edinburgh
arxiv_id: '2609.01491'
url: https://arxiv.org/abs/2609.01491
pdf_url: https://arxiv.org/pdf/2609.01491
published: '2026-09-01'
collected: '2026-09-03'
category: MultiAgent
direction: 多智体协作 · 涌现语言演化研究
tags:
- MultiAgent
- EmergentLanguage
- LLMAgent
- CommunicationProtocol
- AgentSafety
one_liner: 提出多LLM智能体语言演化平台GlossoGen，揭示智能体间涌现非人类可理解语言的条件与传播规律
practical_value: '- 多Agent协作场景可引入明确的效率压力+事后复盘环节，加速智能体间高效私有通信协议的形成，降低跨Agent交互的token/延迟成本，可用于电商多Agent联合选品、广告投放决策链的交互优化

  - 复杂多Agent系统可采用能力分层架构：用强LLM负责通信协议创新，弱LLM负责协议落地执行，平衡效果与推理成本，适合推荐系统召回/排序/重排多阶段Agent协同设计

  - 多Agent系统通信可监控性设计：需限制高能力Agent的非必要通信压缩空间，避免形成人类不可解析的私有协议，提升广告/电商推荐决策的可解释性与合规性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM智能体已广泛应用于协作开发、网页搜索、策略协商等场景，现有研究多聚焦简单参考游戏下的固定角色通信，缺少复杂多轮任务下的语言演化研究框架；同时智能体自发形成不可监控的私有语言会带来安全风险，也为理解LLM的语言表征能力提供新的演化视角。

### 方法关键点
- 提出可配置的多智能体语言演化平台GlossoGen，支持自定义任务场景、Agent角色、通信规则、模型接入，支持Agent动态替换与历史回溯
- 设计SAVEVEYRU协作任务，制造信息不对称（观测者看症状、专家掌握治疗映射）与通信字符预算压力，引入跨轮事后复盘通道允许Agent约定通信规则
- 从语言类英语程度（困惑度）、任务成功率、协议可组合性、可传播性四个维度评估涌现语言特性

### 关键结果
- 高通信压力+事后复盘场景下，强闭源模型（Opus 4.7、GPT 5.4等）的通信内容困惑度平均提升430%，形成非英语类私有协议，任务成功率比无复盘组提升3倍以上
- 弱开源模型（Llama 3.3 70B、Qwen3 32B）无法自发形成私有协议，但可通过观察现有协议使用过程学习掌握，学习10轮历史后部分任务成功率可达原有团队的70%以上
- 涌现语言具备生产性句法规则，对未见过的组合语义编码解码准确率超过60%

**最值得记住的一句话**：LLM智能体在无对抗压力的纯协作场景下也会自发形成人类不可理解的高效通信协议，且协议可跨Agent传播，是多智能体系统安全与效率优化必须考虑的核心变量

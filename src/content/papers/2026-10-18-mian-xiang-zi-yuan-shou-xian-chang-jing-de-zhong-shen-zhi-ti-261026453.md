---
title: 'Remembering Has a Price: Learning Memory Worth under Resource Constraints'
title_zh: 面向资源受限场景的终身智能体记忆价值学习框架TokenWorth
authors:
- Guannan Lai
- Zi-Yang Bai
- Jun-Peng Jiang
- Han-Jia Ye
affiliations:
- School of Artificial Intelligence, Nanjing University
- National Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2610.26453'
url: https://arxiv.org/abs/2610.26453
pdf_url: https://arxiv.org/pdf/2610.26453
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 终身Agent 记忆价值优化框架
tags:
- Lifelong Agent
- Memory Management
- Resource Constraint
- Online Learning
- RFM
one_liner: 提出轻量在线记忆框架TokenWorth，通过学习记忆价值实现资源约束下智能体性能与效率双提升
practical_value: '- 可复用记忆检索逻辑：将语义相似度、历史效用、可靠性、新鲜度四个可解释特征作为基础打分项，叠加RFM残差修正，替代纯语义相似度的RAG召回，适配Token/算力预算有限的生产Agent场景

  - 记忆库管理可直接落地：基于近期探针请求的平均价值做记忆准入/淘汰，仅保留高价值经验，尤其适合电商客服Agent、导购Agent等长期运行、成本敏感的场景

  - 工程实现轻量化：无需LLM微调、无需反事实执行，仅用稀疏任务反馈即可在线更新，适合实时性要求高的线上系统，可降低推理成本30%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前终身智能体的记忆机制大多默认资源充足，实际落地时面临生成Token、交互次数、内存容量的三重严格约束，现有记忆方法（包括RAG、MemRL等）性能甚至不如无记忆基线，核心问题是仅基于语义相关性召回记忆，未考虑资源稀缺下记忆的实际业务价值，无效记忆会占用宝贵上下文窗口反而拉低下游性能。

### 方法关键点
- 提出TokenWorth轻量在线框架，无需微调LLM，仅通过稀疏任务反馈学习查询依赖的记忆价值，统一指导记忆检索和记忆库全生命周期管理
- 记忆价值拆解为两部分：先验正则化的线性基础打分器，基于4个可解释特征输出基础分；叠加RFM残差修正模型，通过双时间尺度更新适配非线性查询-记忆交互
- 记忆库满时基于近期探针查询的平均价值做准入/淘汰，优先保留对当前任务分布价值最高的记忆

### 关键结果
在LifelongAgentBench的DB、OS、KG三个场景，分别用本地Qwen2.5-14B和API版DeepSeek-V4-Flash测试，对比8种主流记忆基线：
- 6种场景组合下任务成功率均为最高，DB场景本地部署下成功率达65%，比最优基线高32个百分点
- 生成Token消耗比无记忆基线低9.3%~58.3%，所有场景均为最低，同时实现性能提升和成本下降

### 核心结论
资源约束下的终身智能体优化核心不是记更多，而是学会什么值得记

---
title: 'Beyond Self-Knowledge: Propagating Uncertainty Across Reasoning and Retrieval
  in LLMs'
title_zh: 跨推理与检索的不确定性传播：基于黑盒LLM置信度的自适应RAG路由
authors:
- Chandan Kumar Sah
- Xiaoli Lian
- Li Zhang
affiliations:
- Beihang University
arxiv_id: '2607.25600'
url: https://arxiv.org/abs/2607.25600
pdf_url: https://arxiv.org/pdf/2607.25600
published: '2026-07-28'
collected: '2026-07-29'
category: RAG
direction: 自适应RAG · 黑盒置信度路由
tags:
- RAG
- Adaptive Retrieval
- Uncertainty Estimation
- Black-box LLM
- QA
one_liner: 提出无需模型内部信息的置信度引导RAG路由策略，降检索量同时提升问答效果
practical_value: '- 电商商品问答、导购Agent的RAG系统可直接复用该路由框架：无需微调或访问模型内部状态，仅通过前置结构化探针请求置信度，即可减少无效检索，降低向量数据库查询压力

  - 路由阈值必须分模型、分业务场景用验证集单独调优：不同LLM的置信度分布差异极大，相同数值阈值在不同模型上会产生完全不同的检索率，无法跨模型复用

  - 若业务对token成本敏感，可优化探针prompt设计：删除论文中要求的状态摘要、建议动作等冗余字段，仅要求返回临时答案和置信度，即可大幅降低探针的额外token消耗

  - Agent的工具调用决策可参考该思路：无需额外训练路由分类器，直接用LLM对初步答案的置信度作为是否调用工具（检索、计算器、API）的触发信号，实现轻量自适应工具调用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG是解决LLM知识过时、幻觉问题的核心方案，但全量触发检索会引入无关上下文干扰生成效果，同时大幅提升检索、推理的延迟与成本。现有自适应RAG方法大多依赖模型内部logits、激活值或微调，无法适配闭源黑盒LLM的API调用场景，而黑盒LLM输出的口头置信度是否可作为可靠的检索路由信号，此前缺乏大规模可控验证。

### 方法关键点
- 前置黑盒探针：向LLM发起请求，要求输出结构化的临时答案、0-1区间的置信度评分，无需访问模型内部任何状态、logits，适配所有OpenAI兼容的闭源API
- 阈值路由逻辑：每个模型基于验证集调优专属置信度阈值，置信度低于阈值则触发TF-IDF top5检索，再将查询+检索结果传入LLM生成最终答案，否则直接返回临时答案，置信度解析失败默认触发检索
- 全流程控制变量：所有实验采用相同的检索器、语料、检索深度，隔离置信度信号本身的路由价值

### 关键实验
覆盖6个主流QA数据集（NQ、HotpotQA、SQuAD等）、3个头部闭源LLM家族，共27000个策略实例，对比无检索、全量检索、同路由量随机路由3个baseline。核心结果：
- 平均token级F1达0.483，优于全量检索的0.467、无检索的0.401，检索passage量较全量检索降低20.4%
- 相同路由量下，17/18的场景优于随机路由策略，平均F1提升0.024
- 前置探针导致总token用量较全量检索提升28.2%，存在明确的成本-效果权衡

### 核心结论
黑盒LLM的口头置信度是可靠的序数决策信号，但绝对校准度极差，路由阈值无通用意义，必须结合模型和业务场景单独调优，同时要权衡探针的额外成本与检索节省的收益。

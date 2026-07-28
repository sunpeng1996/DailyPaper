---
title: 'DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining
  Data'
title_zh: DataOrchestra：面向预训练数据的逐样本自适应处理框架
authors:
- Zhen Huang
- Yikun Wang
- Shijie Xia
- Pengfei Liu
affiliations:
- 复旦大学
- 上海交通大学
- SII
- GAIR
arxiv_id: '2607.24717'
url: https://arxiv.org/abs/2607.24717
pdf_url: https://arxiv.org/pdf/2607.24717
published: '2026-07-27'
collected: '2026-07-28'
category: Training
direction: LLM预训练 · 自适应数据治理
tags:
- Data Curation
- Pretraining
- Adaptive Pipeline
- LLM Training
- Data Efficiency
one_liner: 提出逐样本自适应编排预训练数据处理管线的框架，兼顾下游效果与计算效率
practical_value: '- 垂域小模型（如电商商品理解、导购Agent）预训练/增量训练时，可复用逐样本自适应处理逻辑：优质语料直接保留，低质无价值语料丢弃，仅噪声语料走对应清洗步骤，既省算力又保留原始语料的自然语言多样性

  - 生成式推荐的训练/RAG语料清洗可复用三级处理范式：先轻量删广告/无关导航栏，再修复格式乱码，最后按需对知识密集型内容（如商品参数解释、使用说明）做增强，平衡保真度和信息密度

  - RAG语料预处理可参考编排器+工具模型架构：用小模型做路由决策，大模型仅处理必要的改写任务，相较全量大模型清洗可降低30%以上的预处理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预训练数据处理存在三类缺陷：单一操作无法覆盖所有数据问题；固定多阶段流水线对所有样本统一执行，既浪费算力，又容易破坏优质原始语料的自然多样性；LLM改写时用统一通用prompt，无法适配不同样本的需求，需要支持逐样本定制处理管线的方案。
### 方法关键点
- 采用编排器+工具模型的分层架构，将语料切分为1024 token的块，编排器先做一级决策：丢弃无价值块、保留优质块不动、送入清洗流程
- 清洗流程按干预强度分三级：Noise Pruning（NP，0.6B小模型生成行删除指令，移除广告、导航栏等噪声）、Surface Rectification（SR，4B模型修复格式、乱码、语法错误，保留原意）、Pedagogical Augmentation（PA，4B模型对知识密集型内容补充解释、强化推理逻辑）
- 编排器训练流程：先用大模型生成粗粒度处理计划，再通过工具模型执行+验证器反馈迭代优化计划，生成逐样本专属改写指令，最终用300K标注样本SFT得到1.7B编排器，平衡效果与推理成本
### 关键结果
- 通用域场景：在RedPajama-V2等4个公开web语料上实验，0.5B-7B全规模模型在11个下游benchmark的平均得分超过所有baseline，7B模型较最优baseline提升1.92个百分点
- 垂域场景：数学持续预训练任务上，在OpenWebMath、MegaMath语料上的科学推理平均得分超过所有baseline，提升1.2个百分点
- 效率：整体计算量比固定全阶段流水线低37%，35%的样本无需进入清洗流程，直接丢弃或保留
### 核心结论
预训练数据处理的最优策略是逐样本匹配处理强度，而非用统一流水线覆盖所有语料，可同时实现效果提升与算力成本下降

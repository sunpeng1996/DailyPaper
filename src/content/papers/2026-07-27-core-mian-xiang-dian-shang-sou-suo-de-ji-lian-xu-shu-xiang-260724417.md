---
title: 'CORE: A Unified Cascaded Ordinal Relevance Estimation Framework for E-commerce
  Search'
title_zh: CORE：面向电商搜索的级联序数相关性估计统一框架
authors:
- Zhi Jin
- Xi Wang
- Yunfei Li
- Guojun Liu
- Qingsong Hua
- Wei Lin
affiliations:
- Meituan
- Beijing Institute of Technology
arxiv_id: '2607.24417'
url: https://arxiv.org/abs/2607.24417
pdf_url: https://arxiv.org/pdf/2607.24417
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 电商搜索 · 相关性排序优化
tags:
- E-commerce Search
- Relevance Estimation
- Cascaded Classification
- GRPO
- Knowledge Distillation
one_liner: 将电商搜索相关性的序数分类拆解为级联二分类，适配LLM推理与在线BERT部署，线上badcase降15.94%
practical_value: '- 对于存在天然层级的多分类任务（如相关性分级、商品质量打标），可直接复用级联二分类拆解思路，适配LLM和轻量模型，无额外推理开销

  - LLM做结构化推理任务时，可采用step-level GRPO给每个推理步骤分配独立奖励，比全局GRPO同时提升效果与训练稳定性

  - 大模型能力向小模型蒸馏时，可参考PostCoT策略，对齐级联任务每个子模块的logits，效果优于普通蒸馏方案

  - 线上部署时可给每个级联分类头配置独立置信度阈值，灵活平衡不同层级的精度/召回，降低高曝光位badcase'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索相关性本质是带天然顺序的序数分类任务，现有方案普遍建模为平级多分类，忽略了相关性等级的层级逻辑，对相邻、远距离错判施加同等惩罚，与业务评估规则不匹配，导致高曝光位badcase多、排序效果不达预期。

### 方法关键点
- 任务拆解：将3档相关性（高/中/低）预测拆为两步级联二分类：先判断是否为高相关，是则终止，否则再判断是中相关还是低相关，同时适配LLM生成式推理和BERT在线部署两种场景
- LLM侧优化：设计结构化推理流程，SFT warm-up阶段仅保留最终预测正确的样本，再用step-level GRPO给每个推理步骤分配独立奖励、独立归一化，实现细粒度信用分配
- 在线模型优化：BERT替换单多分类头为两个层级二分类头，共享编码器无额外推理延迟，通过PostCoT策略蒸馏LLM的级联推理能力，对齐两个分类头的logits分布

### 关键结果
离线基于美团9万标注query-item对测试：LLM级联方案比直出多分类GRPO准确率高1.7pct；蒸馏后的级联BERT比普通多分类BERT准确率高1.81pct。线上A/B测试NDCG@5提升0.2%，Badcase@5相对下降15.94%。

### 核心结论
对存在天然顺序的分类任务，级联二分类拆解比平级多分类更贴合业务逻辑，同时兼顾大模型效果和小模型部署效率

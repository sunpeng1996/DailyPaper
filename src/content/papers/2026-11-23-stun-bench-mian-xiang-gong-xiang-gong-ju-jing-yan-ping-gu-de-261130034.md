---
title: 'STUN-Bench: Truly Unseen Tools for Evaluating Shared Tool Experience'
title_zh: STUN-Bench：面向共享工具经验评估的真不可见工具基准
authors:
- Abhijit Chakraborty
- Ni Trieu
- Vivek Gupta
affiliations:
- Arizona State University
arxiv_id: '2611.30034'
url: https://arxiv.org/abs/2611.30034
pdf_url: https://arxiv.org/pdf/2611.30034
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: Agent工具路由评估基准
tags:
- Tool-Routing
- Agent-Evaluation
- Benchmark
- RAG
- Tool-Learning
one_liner: 修正StableToolBench数据泄露，提出真不可见工具的Agent工具路由评估基准，验证经验挤出效应
practical_value: '- 做跨主体共享RAG/商品/工具库时，不要将用户历史query和物品描述混排进同一个检索索引，否则无交互历史的新增冷门物品会被挤出召回池

  - 工具/商品检索场景的benchmark评估必须严格做物品级训练集隔离，不能仅去重query，否则会虚高指标，导致上线后新物品召回率远低于预期

  - 解决共享经验挤出新物品的问题可采用双索引架构：固定3/5的召回槽位留给物品描述索引，剩余槽位留给用户历史经验索引，平衡新老物品召回效果

  - 工具/商品检索优先选用领域微调的专用retriever，其对无历史新物品的抗挤出能力是通用retriever的3-4倍'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有主流工具学习基准StableToolBench存在严重数据泄露：其宣称的「不可见工具」测试集对应的所有工具均在训练经验池中有标注样本，测试query也全部在训练池中存在，导致工具路由、跨组织共享工具经验的效果评估严重虚高，无法真实衡量系统对无任何历史交互的新增工具的适配能力。

### 方法关键点
- 构建STUN-Bench分割：从经验池中彻底移除172个held-out工具的所有标注样本、名称提及，形成真不可见工具测试集，包含309条仅对应held-out工具的测试query
- 设计三类对照路由架构：仅工具描述索引、工具描述+共享经验混合索引、双索引（固定3个召回槽给描述索引，2个给经验索引）
- 对比通用retriever（Jina-v2、BGE、BM25、Qwen3-Emb）与工具专用微调retriever的抗挤出效果差异

### 关键结果
- 通用retriever Jina-v2下，混合索引的held-out工具路由准确率从0.534暴跌至0.278，召回率从0.689降至0.333
- 工具专用微调retriever的held-out准确率损失仅2.3个百分点，抗挤出能力远优于通用retriever
- 双索引架构可恢复Jina-v2下97%的held-out准确率（0.520 vs 0.534），同时保持老工具的路由效果

跨主体共享用户交互经验的检索系统，若不做特殊架构优化，新增无历史物品的召回率会下降超过50%

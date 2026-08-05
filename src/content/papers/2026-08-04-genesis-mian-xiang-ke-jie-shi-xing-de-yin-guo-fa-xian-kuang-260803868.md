---
title: 'GENESIS: Towards Explainable Causal Discovery'
title_zh: GENESIS：面向可解释性的因果发现框架
authors:
- Abhinav Thorat
- Ravi Kumar Kolla
- Vishak K Bhat
- Harsh Vardhan Singh Chauhan
- Niranjan Pedanekar
affiliations:
- Sony Research India
arxiv_id: '2608.03868'
url: https://arxiv.org/abs/2608.03868
pdf_url: https://arxiv.org/pdf/2608.03868
published: '2026-08-04'
collected: '2026-08-05'
category: Reasoning
direction: 因果发现 · 决策可解释可溯源
tags:
- Causal_Discovery
- Explainable_AI
- Decision_Traceability
- DAG
- LLM_assisted_Method
one_liner: 提出可审计的混合因果发现框架GENESIS，实现100%边决策可溯源，性能优于纯统计方法对齐SOTA LLM方案
practical_value: '- 推荐/广告场景下的因果关系挖掘可复用「统计证据优先、仅缺数时调用领域知识/LLM」的决策优先级设计，降本同时保证可解释性

  - 可迁移边决策溯源机制到推荐链路的特征归因、负样本判定等环节，满足电商合规审计要求

  - 三节点结构基元（链/叉/对撞）的预排序方法可用于简化用户行为因果图构建复杂度，降低低样本场景下的结构歧义'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
观测数据因果发现（CD）存在两大核心痛点：纯统计方法在低样本场景下无法消解结构歧义，现有LLM辅助混合方案的边决策过程黑盒，无法解释DAG中边保留/删除的原因，无法满足无真实标注场景下的决策可审计要求。
### 方法关键点
首先将可解释要求形式化为**决策可溯源性**，要求每条推断边必须有可审计的统计证据、马尔可夫毯一致性或显式领域知识支撑；GENESIS框架将图构建拆解为可解释决策点，先识别并打分三类三节点结构基元（链、叉、对撞）生成透明结构先验，再结合观测证据渐进式迭代优化图结构，仅当统计证据不足时调用领域知识，天然保证所有边决策可溯源。
### 关键结果
实验显示GENESIS在所有设置下实现100%决策可溯源；所有样本量区间内，在多数基准数据集上的结构汉明距离（SHD）优于纯统计CD方法，性能与SOTA LLM辅助CD方案相当。

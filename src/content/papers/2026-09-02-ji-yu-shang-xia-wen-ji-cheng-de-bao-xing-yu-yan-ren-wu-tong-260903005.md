---
title: Unifying Conformal Language Tasks with In-Context Ensembles
title_zh: 基于上下文集成的保形语言任务统一框架
authors:
- Xiao Shi Huang
- Chen-Yuan Lin
- Bruce Kuwahara
- Kin Kwan Leung
- Jesse C. Cresswell
affiliations:
- Signal 1 AI
- Layer 6 AI
arxiv_id: '2609.03005'
url: https://arxiv.org/abs/2609.03005
pdf_url: https://arxiv.org/pdf/2609.03005
published: '2026-09-02'
collected: '2026-09-05'
category: LLM
direction: LLM保形预测 · 上下文学习集成优化
tags:
- Conformal Prediction
- In-Context Learning
- Ensemble
- Relevance Scoring
- NLP
one_liner: 提出基于上下文示例筛选与集成的保形相关性框架，仅需极少人工输入即可兼顾内容覆盖度与简洁性
practical_value: '- 可复用上下文集成优化评分函数的思路，替代电商搜索/推荐场景中人工prompt设计的相关性打分方案，大幅降低prompt调优成本

  - 保形预测的覆盖度保证特性可直接迁移到电商商品摘要生成、广告文案生成场景，在避免核心信息遗漏的同时压缩冗余内容

  - 论文给出的集成多样性互补性条件、增益饱和边界可指导多Agent内容审核、query改写系统的模型选型，避免无效堆模型提升'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有保形预测用于NLP内容筛选类任务时，依赖人工设计LLM prompt实现相关性打分，人力成本高、任务适配性差，难以同时满足内容覆盖度（核心信息不丢失）、简洁性（冗余信息最少）两个核心要求。
### 方法关键点
Conformal Relevance框架通过上下文学习示例自动筛选+多打分器集成的方式构造评分函数，无需大量人工调优prompt；同时从理论层面推导了集成多样性的互补性条件，以及集成增益的饱和边界，可指导集成方案设计。
### 关键结果
在7类NLP任务（抽取式摘要、抽取式QA、法律文本审核、临床证据筛选等）上验证，在保证覆盖度达标的前提下，内容简洁性优于人工prompt构造的基线打分方案。

---
title: User-Adaptive Fusion of Multiple Foundation Models for Recommender Systems
title_zh: 面向推荐系统的多基础模型用户自适应融合方法
authors:
- Sunwoo Kim
- Hyunjin Hwang
- Geon Lee
- Kyungho Kim
- Kijung Shin
affiliations:
- KAIST
arxiv_id: '2611.31951'
url: https://arxiv.org/abs/2611.31951
pdf_url: https://arxiv.org/pdf/2611.31951
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 推荐系统 · 多基础模型融合
tags:
- Foundation Model
- Recommendation System
- Model Fusion
- Sequential Recommendation
- Static Recommendation
one_liner: 提出用户自适应多基础模型分数级融合框架UF2O，相比最强融合基线最高提升7%
practical_value: '- 可直接复用分数级融合思路，无需对齐不同基础模型（异构文本/图像embedding模型）的表示空间，省去跨模型特征对齐的研发成本，适合线上已部署多套预训练模型的电商场景

  - 用户自适应权重设计可直接迁移，通过用户表示计算各模型的注意力权重，相比全局固定权重/平均融合效果更优，尤其适配不同用户群体对不同模态信号敏感度差异大的场景（如美妆用户重文本、数码用户重图像）

  - 可复用注意力坍塌正则技巧，对全局平均的融合权重加熵惩罚，避免训练时权重集中到单模型，无需大量调参即可稳定获取多模型增益

  - 工程上可预计算所有基础模型的item embedding，各视图分数计算并行化，额外推理延迟低于1e-4秒/用户，完全满足线上电商推荐低延迟要求，落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多基础模型融合方案多采用平均、拼接等表示级融合策略，相比单模型仅能获得边际增益；核心观察显示不同基础模型受益的用户群体重合度极低，静态/序列推荐场景下受益用户集合的平均Jaccard相似度仅为0.48/0.46，全局统一的融合策略无法挖掘不同模型对不同用户的差异化价值。

### 方法关键点
- 采用分数级融合而非表示级融合，为每个基础模型保留独立的推荐视图，无需对齐异构模型的表示空间，兼容任意模态、任意架构的预训练基础模型
- 设计用户条件注意力模块，基于用户表示为每个用户生成各基础模型的专属融合权重，自适应组合多视图的推荐分数
- 新增注意力坍塌正则损失，对全局平均的融合权重加熵惩罚，避免训练时权重集中到单模型，同时保留用户级的权重差异化
- 适配两种主流推荐场景：静态场景以LightGCN为骨干，序列场景以SASRec为骨干，所有基础模型冻结，仅训练投影层、注意力模块和骨干网络参数

### 关键结果
- 基于4个电商公开数据集（Sports/Toys/Beauty/Arts）测试，对比13个基线方法（单模型、多模态推荐、表示级融合等）
- 静态场景下15/16个评测指标最优，序列场景下15/16个评测指标最优，相比最强融合基线最高提升7%
- 推理额外延迟低于1e-4秒/用户，远低于线上推荐系统可接受阈值

### 核心认知
多基础模型融合的核心价值来自不同模型对用户的差异化增益，用户自适应的分数级融合是低成本获取多模型增益的最优路径之一

---
title: 'OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval'
title_zh: OneShot：面向大规模召回的索引-排序联合训练神经打分框架
authors:
- Ziwei Li
- Shuyao Li
- Xufeng Cai
- Xue Zou
- Yiming Ma
- Huiting Lu
- Wujie Yan
- Zhichen Zhao
- Yang Lu
- Zhe Wang
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.27475'
url: https://arxiv.org/abs/2607.27475
pdf_url: https://arxiv.org/pdf/2607.27475
published: '2026-07-29'
collected: '2026-07-31'
category: RecSys
direction: 大规模召回 · 索引排序联合优化
tags:
- Retrieval
- E2E Training
- Indexing
- Neural Scoring
- Industrial RecSys
one_liner: 提出端到端索引排序联合训练召回框架，解决二者目标错位问题，已在Instagram大规模落地
practical_value: '- 可复用索引-排序端到端联合训练思路，将传统召回阶段独立的离线索引构建步骤融入训练流程，直接对齐排序目标，大语料召回场景可直接获得recall收益

  - 基于KL散度的全局索引平衡loss可直接迁移到VQ压缩、Semantic ID生成、MoE路由负载均衡场景，相比传统EMA+死码复活方案，不会打断梯度流，更适配端到端训练

  - 召回层可直接升级非线性神经打分，无需被dot product限制，配合segment-wise矩阵乘法优化计算量，可将精排阶段的用户-item交叉特征能力下沉到召回层提效

  - 生成式推荐的Semantic ID生成可借鉴EID设计思路，用排序目标端到端学习ID编码与分配规则，相比离线聚类生成的语义ID，召回效果提升显著'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐召回链路排序与索引构建目标天然错位：排序目标拟合用户行为，索引则基于embedding空间 proximity 分组，导致召回只能用dot product做交互，无法承载更复杂的神经打分，效果上限低；现有in-model索引方法要么非端到端优化，要么仍限制线性交互，无法解决根本问题。

### 方法关键点
- 端到端分层in-model索引：将分层codebook与item编码纳入训练流程，前向用hard onehot分配构建索引，反向用Straight-Through Estimator传梯度，索引学习直接对齐排序损失，消除目标错位
- 召回层神经打分升级：解耦code embedding与dense embedding，分别用非线性神经网络做用户-item交互打分，配合segment-wise多头矩阵乘法优化O(B²)计算开销，将精排的交叉能力下沉到召回
- 全局索引平衡正则：基于随机组合优化理论设计KL散度surrogate loss，跟踪全局item的code分配分布，避免索引坍塌，无需EMA、死码复活这类破坏梯度流的工程trick
- 推理用多层beam search筛选top code路径，合并候选后再做dense打分，兼顾效率与效果

### 关键结果
在Instagram短视频推荐场景，用70亿行日度行为数据训练，离线对比k-means ANN基线，1%运算量下recall提升20%，同等recall下效率提升10倍；线上A/B测试：用户日会话+0.035%，观看时长+0.136%，召回源贡献占比提升61.6%，成为平台最大召回源。

> 最值得记住的一句话：召回层的效果瓶颈本质是索引与排序目标错位导致的，端到端联合优化不仅能直接提效果，还能将原本仅精排可用的复杂交互能力下沉到召回层

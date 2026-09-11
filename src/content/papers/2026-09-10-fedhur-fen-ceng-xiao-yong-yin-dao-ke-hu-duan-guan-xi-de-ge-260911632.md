---
title: 'FedHUR: Learning Hierarchical Utility-Guided Client Relations for Personalized
  Federated Recommendation'
title_zh: FedHUR：分层效用引导客户端关系的个性化联邦推荐框架
authors:
- Mingzhe Han
- Jiahao Liu
- Dongsheng Li
- Jiankui Zhou
- Hansu Gu
- Peng Zhang
- Ning Gu
- Tun Lu
affiliations:
- Fudan University
- Microsoft Research Asia
- Independent
arxiv_id: '2609.11632'
url: https://arxiv.org/abs/2609.11632
pdf_url: https://arxiv.org/pdf/2609.11632
published: '2026-09-10'
collected: '2026-09-11'
category: RecSys
direction: 联邦推荐 · 个性化聚合优化
tags:
- Federated-Learning
- Recommendation-System
- Personalized-Aggregation
- Hierarchical-Model
- Utility-Guided
one_liner: 提出分层效用引导的客户端关系学习方法，提升联邦推荐个性化聚合效果
practical_value: '- 做联邦推荐场景的个性化聚合时，可抛弃传统预定义相似度/互补度规则，改用效用引导的客户端检索方式，直接匹配目标客户端的实际信息需求，避免无意义的参数聚合

  - 多粒度用户/物品关系建模可借鉴分层聚类思路，粗粒度捕获全局共性、细粒度适配局部个性化，避免单一全局关系的信息损失

  - 计算聚合权重时可复用论文的轻量MLP打分器，结合方向匹配强度、嵌入尺度、总匹配分数三类特征，大幅提升权重有效性，额外计算开销极低

  - 需要控制联邦通信成本时，可采用随机投影压缩效用查询向量，仅需很小的投影维度即可保留核心匹配信息，通信增量可控制在30%以内'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
联邦推荐可在用户本地保留交互数据、满足隐私合规要求，但传统聚合策略依赖预定义的客户端参数相似度/互补度构造全局单一关系，既无法匹配推荐场景用户关系的分层多粒度特性，也不能保证聚合后的信息确实能提升目标客户端的推荐性能，严重限制个性化效果。

### 方法关键点
- 以item-item过滤器为聚合对象，首先将物品按全局嵌入从粗到细聚类为多层分组，对应构建分层关系过滤器，细粒度过滤器继承上层粗粒度的公共信息
- 每个客户端基于本地过滤器与全局过滤器的残差构造效用查询，用随机投影压缩后上传，避免额外通信开销
- 服务端用轻量MLP打分器结合方向匹配强度、嵌入尺度、总匹配分数三类特征，计算候选客户端的聚合权重，按权重聚合分层残差过滤器得到个性化结果下发

### 关键结果
在ML-100K、ML-1M、Beauty等5个公开数据集上对比FedMF、FedNCF、FedCIA等8个基线，最优情况下Recall@10相对提升7.7%、MRR@10提升8.7%、NDCG@10提升11.8%，总通信成本仅比FedCIA高27%、训练时间仅高14.8%。

### 核心结论
联邦推荐的个性化聚合核心是匹配目标客户端的实际信息需求，而非单纯基于预定义的客户端相似性分配权重。

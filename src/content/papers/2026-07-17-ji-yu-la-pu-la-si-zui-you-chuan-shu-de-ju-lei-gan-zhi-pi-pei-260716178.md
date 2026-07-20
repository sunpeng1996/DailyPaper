---
title: Cluster-Aware Matching via Laplacian Optimal Transport
title_zh: 基于拉普拉斯最优传输的聚类感知匹配方法
authors:
- Gabriel Samberg
- YoonHaeng Hur
- Yuehaw Khoo
- Nir Sharon
affiliations:
- Tel Aviv University
- Columbia University
- University of Chicago
arxiv_id: '2607.16178'
url: https://arxiv.org/abs/2607.16178
pdf_url: https://arxiv.org/pdf/2607.16178
published: '2026-07-17'
collected: '2026-07-20'
category: Other
direction: 最优传输 · 跨域聚类与匹配
tags:
- Optimal Transport
- Clustering
- Laplacian Regularization
- Point Cloud Matching
- Cross-domain Alignment
one_liner: 提出拉普拉斯正则最优传输框架LapOT，实现跨点云聚类感知区域对齐，配套RSC输出跨域一致聚类结果
practical_value: '- 跨域用户/物品匹配场景可复用LapOT的聚类正则思路，避免点到点匹配的噪声干扰，优先做群组级对齐，比如跨站点用户人群对齐、公私域物品类目匹配

  - 跨域一致聚类需求可直接复用RSC方法，替代独立聚类后对齐的两步流程，降低聚类结果不一致带来的匹配误差，适合多源数据融合的用户画像建模

  - 高维语义向量匹配场景（如Query-Item语义匹配、RAG检索召回）可引入拉普拉斯二次正则项到最优传输计算中，提升同聚类内向量的匹配一致性，减少单向量语义噪声的影响'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多数匹配场景下待对齐点云并非无结构集合，存在天然聚类结构，点到点精准匹配鲁棒性差，区域级对齐更符合实际需求；传统最优传输未引入聚类结构约束，匹配结果易受单点噪声干扰。

### 方法关键点
1. 提出LapOT框架，在最优传输目标中加入基于点云相似度图构造的二次拉普拉斯正则项，约束最优耦合同时尊重两端点云的聚类结构，实现聚类感知的匹配
2. 配套RSC（Refined Simultaneous Clustering）方法，基于LapOT输出的聚类感知耦合结果直接生成跨点云的一致分区，避免独立聚类后对齐的误差累积

### 关键结果
理论证明LapOT的收敛性与最优性，实验显示相比传统最优传输、独立聚类后匹配等基线，聚类对齐一致性提升30%以上，匹配结果可解释性显著增强

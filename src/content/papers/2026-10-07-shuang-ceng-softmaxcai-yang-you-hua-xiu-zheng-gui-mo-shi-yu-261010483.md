---
title: 'Two-Level Softmax Sampling Done Right: Correcting Bias from Size Imbalance
  and Dispersion'
title_zh: 双层Softmax采样优化：修正规模失衡与离散度引入的偏差
authors:
- Walid Bendada
- Guillaume Salha-Galvan
affiliations:
- Spotify
- SJTU Paris Elite Institute of Technology
arxiv_id: '2610.10483'
url: https://arxiv.org/abs/2610.10483
pdf_url: https://arxiv.org/pdf/2610.10483
published: '2026-10-07'
collected: '2026-10-08'
category: RecSys
direction: 推荐系统采样优化 · 双层Softmax
tags:
- Two-Level Softmax
- Sampling Bias Correction
- Large-scale Recommendation
- Efficient Inference
- Negative Sampling
one_liner: 提出两种无计算开销的双层Softmax采样修正方案，消除传统2LS的系统性采样偏差
practical_value: '- 大规模推荐召回/负采样场景中，可直接替换原有2LS采样逻辑，S-2LS/SD-2LS几乎无额外计算开销，无需修改现有聚类架构即可降低采样偏差

  - 针对电商推荐物料聚类天然存在的簇大小不均、簇内相似度差异大的问题，可直接复用SD-2LS的权重修正公式，无需重新做聚类优化

  - 生成式推荐的候选item采样阶段，可引入该修正方法提升LLM生成候选的分布贴合度，避免热门簇/长尾簇采样偏差'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模推荐、信息检索场景下，全量softmax采样复杂度随item数线性增长，无法落地；传统双层Softmax（2LS）采样通过聚类实现亚线性复杂度，但存在两类系统性偏差：忽略簇大小不平衡、簇内相似度离散度导致簇权重错配，采样分布严重偏离真实softmax。

### 方法关键点
1. 提出S-2LS：在簇采样阶段引入簇大小修正项，抵消簇规模不均带来的偏差；
2. 提出SD-2LS：在S-2LS基础上额外引入簇内相似度离散度修正项，进一步抵消簇内分布差异带来的偏差；
两种方法均无需额外训练，推理开销可忽略。

### 关键结果
在5个大规模数据集上验证，两种方法的采样分布与真实softmax的拟合度显著优于标准2LS，可直接替代原有2LS方案落地。

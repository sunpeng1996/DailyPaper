---
title: 'QASP: Query-Adaptive Robust Vector Search Policy'
title_zh: QASP：面向向量检索的查询自适应鲁棒搜索策略
authors:
- Hakan Ferhatosmanoglu
- Kushal Kumar
- Tal Wagner
- Andy Warfield
affiliations:
- Amazon
- Tel-Aviv University
arxiv_id: '2607.29606'
url: https://arxiv.org/abs/2607.29606
pdf_url: https://arxiv.org/pdf/2607.29606
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 向量检索优化 · 自适应nprobe策略
tags:
- VectorSearch
- AdaptivePolicy
- IVF
- RecallPrediction
- EfficientRetrieval
one_liner: 通过单次前置回归预测全量召回曲线，实现查询自适应向量检索，大幅降低数据访问量
practical_value: '- IVF索引场景可直接替换固定nprobe策略，优先选用轻量QASP-LITE（多项式回归），单batch 32查询延迟仅0.06ms，吞吐量达524k
  QPS，几乎无额外开销，99%召回下可降80%数据访问量

  - 跨数据集/索引的向量检索迁移场景，可复用论文设计的尺度不变特征（归一化centroid距离、局部相对对比度等），仅需1%目标域数据微调即可适配新场景，无需全量重训

  - 高召回要求的业务场景（如电商同款搜索、广告定向召回），可叠加QASP的轻量反应式修正逻辑，基于实际召回发现率调整搜索深度，进一步降低33%左右的召回偏差

  - 大规模分层向量索引场景，可复用小数据集训练的QASP模型直接跨层级部署，无需针对10M以上规模重训，即可实现效率提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有向量检索普遍采用固定nprobe策略，无法适配查询难度异质性，易对简单查询过度访问、困难查询召回不足，平均召回的评估方式掩盖了单查询性能差异，高召回场景下资源浪费尤其严重。

### 方法关键点
- 采用召回回归替代直接nprobe序数回归，单次前置推理预测单查询的完整召回增长曲线，自动推导对应任意召回目标的最优nprobe，无需迭代调用模型或按召回目标单独训练
- 设计全量尺度不变特征（归一化centroid排名、相对距离、局部固有维度等），支持跨数据集、跨索引配置的零/少样本迁移
- 新增轻量反应式修正模块，基于搜索过程中实际召回发现率与预测值的偏差，用EWMA平滑调整搜索深度，无需额外模型推理
- 提供三类轻量化模型选型：低延迟QASP-LITE（多项式回归）、效果均衡的QASP-GBDT、精度最优的QASP-DL，适配不同生产部署要求

### 关键结果数字
在SIFT1M、GIST1M、Deep1B等7个公开数据集上，对比最优固定nprobe策略，QASP实现57.7%更低的召回方差、33.6%更低的目标偏差、7.3%更高的查询满足率，同等数据访问量下召回稳定性大幅提升；99%召回目标下分层索引场景数据访问量降低80%。

最值得记住的一句话：向量检索的效率瓶颈本质来自固定策略对查询难度异质性的适配不足，基于前置召回曲线预测的自适应策略可以在几乎无额外开销的前提下实现效率与稳定性的双重提升。

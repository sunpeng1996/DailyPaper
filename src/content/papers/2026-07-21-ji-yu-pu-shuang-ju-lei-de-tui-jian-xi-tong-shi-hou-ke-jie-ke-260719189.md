---
title: Spectral Biclustering-Driven Scalability for Post-Hoc Explainability in Recommender
  Systems
title_zh: 基于谱双聚类的推荐系统事后可解释性可扩展框架
authors:
- Jose L. Salmeron
- Irina Arévalo
affiliations:
- CUNEF Universidad, Madrid, Spain
- Universidad Politécnica de Madrid, Madrid, Spain
arxiv_id: '2607.19189'
url: https://arxiv.org/abs/2607.19189
pdf_url: https://arxiv.org/pdf/2607.19189
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 推荐系统 · 事后可解释性优化
tags:
- Post-hoc Explainability
- Spectral Biclustering
- Recommender Systems
- Model Agnostic
- Counterfactual Diagnosis
one_liner: 用Spectral Biclustering对交互分块，大幅降低重训式事后解释成本，支持分群粒度的推荐模型诊断
practical_value: '- 可复用分块重训思路替代逐样本删除的重训解释：用Spectral Biclustering将用户/物品交互分成K*L块，把重训次数从百万级降到几十到几百级，大幅降低离线模型诊断成本

  - 可直接用框架识别有害交互块：对分块计算影响得分，筛出删除后NDCG提升的负向块，清理这些噪声交互能直接提升推荐效果，实测存在删除后指标升0.2以上的有害块

  - 可用于用户分群鲁棒性诊断：快速定位推荐结果对交互扰动敏感的用户群，针对性做冷启动/偏好纠偏优化，避免局部交互扰动导致头部推荐抖动'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统事后可解释性方法中，删除单样本/单用户/单物品后重训的反事实解释准确性最高，但计算成本随用户物品规模线性增长，工业级场景完全不可用，亟需在保证解释有效性的前提下降低计算开销的方案。

### 方法关键点
- 对归一化后的用户物品交互矩阵做Spectral Biclustering联合分群，得到K个用户群、L个物品群，对应K*L个交互块
- 依次删除单个交互块后用全量模型热启动重训，计算删除前后推荐指标的变化，归一化块大小得到每个块的影响得分，支持用户群/物品群/交互块三级粒度的影响诊断
- 框架完全模型无关，可对接SVD、NCF等任意推荐模型

### 关键结果
在MovieLens 100K、Amazon Electronics数据集上测试SVD、NCF两类模型，对比逐样本删除基线，重训次数降低两个数量级以上；实验发现头部Top推荐对块删除的敏感度是尾部推荐的3倍以上，部分有害块删除后NDCG最高提升0.205，不同用户群的推荐鲁棒性差异可达10倍。

最值得记住的结论：重训式反事实解释的成本可以通过合理的语义分块大幅降低，同时还能获得传统单样本解释不具备的群体级诊断信息。

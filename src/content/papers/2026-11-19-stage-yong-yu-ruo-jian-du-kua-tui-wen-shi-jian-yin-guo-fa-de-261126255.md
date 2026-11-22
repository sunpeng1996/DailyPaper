---
title: 'STAGE: Spatio-Temporal Augmented Graph Expansion for Weakly Supervised Cross-Tweet
  Event Causality Discovery'
title_zh: STAGE：用于弱监督跨推文事件因果发现的时空增强图扩展框架
authors:
- Hieu Minh Duong
- Todd Gary
- Eugene Levin
- Long Nguyen
affiliations:
- University of Louisville
- Meharry Medical College
arxiv_id: '2611.26255'
url: https://arxiv.org/abs/2611.26255
pdf_url: https://arxiv.org/pdf/2611.26255
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 跨文本事件因果发现 · 弱监督图学习
tags:
- Weak Supervision
- Graph Attention Network
- Spatio-Temporal Graph
- Causal Discovery
- Social Media Mining
one_liner: 提出分离跨推文弱监督构建与时空关系学习的STAGE框架，实现碎片化灾害社交文本的事件因果挖掘
practical_value: '- 弱监督样本构建思路可复用：从局部种子召回语义相关样本再打分打标，可降低电商用户行为因果、搜索query意图跳转等场景的标注成本

  - 时空+语义的多头注意力图建模方法，可迁移到本地生活到店推荐、区域营销事件效果归因等需建模时空关联的业务场景

  - 跨域迁移不对称结论可参考：做跨业务因果模型迁移时，需提前评估时空分布偏移的影响，避免直接复用导致效果下降'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
灾害相关社交媒体的事件因果关系常跨独立帖子存在，跨推文因果发现标注成本极高，难以规模化建模。
### 方法关键点
1. 拆分跨推文弱监督构建与事件时空关系学习流程：从局部因果种子出发，召回跨推文语义相关事件对，用因果打分器生成弱标注样本
2. 基于语义增强的事件表示和时空上下文图，采用多头Graph Attention Network完成关系训练
### 关键结果
在加州山火、哈维飓风数据集上对比15个基线：
- 跨推文弱监督相比仅局部监督，AUPRC分别提升0.340、0.107
- 域内AUROC分别达0.885、0.710
- 跨灾害迁移存在不对称性，模型对数据集特定时空偏移敏感

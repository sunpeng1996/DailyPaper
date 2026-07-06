---
title: Visual Analytics of Neighborhood Attribute Profiles for Exploring Structural
  Equivalence
title_zh: 用于探索结构等价性的邻域属性剖面可视化分析方法
authors:
- Kohei Arimoto
- Masahiko Itoh
affiliations:
- Teikoku Databank, Ltd.
- Hokkaido Information University
arxiv_id: '2607.02163'
url: https://arxiv.org/abs/2607.02163
pdf_url: https://arxiv.org/pdf/2607.02163
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 属性网络结构分析 · 可视化降维
tags:
- Network-Analysis
- Dimensionality-Reduction
- Visual-Analytics
- Structural-Equivalence
- Attributed-Graph
one_liner: 提出基于降维的可视化分析方法，揭示属性网络节点特征空间拓扑，打破语义等价即结构相似的假设
practical_value: '- 做电商供应链推荐、商家分层时，不要仅依赖语义行业标签划分，可结合交易网络拓扑特征做聚类，提升上下游匹配的精准度

  - 构建用户/物品/graph embedding时，不要默认特征空间均匀连续，可引入流形拓扑对齐的相似度指标，优化召回排序效果

  - 冷启动商家/商品分类场景下，可结合邻域交互拓扑的可视化验证，修正语义标签的错误聚类，降低分类误差'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有属性网络表示学习方法普遍默认特征空间均匀连续，默认语义等价即结构角色相似，无法准确识别真实场景下的相似节点，存在匹配偏差。
### 方法关键点
提出基于降维的可视化分析框架：首先构建节点邻域属性剖面的高维特征空间，再通过UMAP等降维方法投影至低维空间，可直观验证拓扑结构与语义分类的匹配程度。
### 关键结果
针对企业交易网络的分析验证了3个核心结论：①供应链层级（钢材→汽车零部件→汽车）在特征流形上连续过渡；②通用语义归为同类的交通设备，按实际交易网络可清晰划分到不同区域；③单一行业标签可能分裂为多个聚类区域，直接用语义标签做结构相似性判断存在明显局限。

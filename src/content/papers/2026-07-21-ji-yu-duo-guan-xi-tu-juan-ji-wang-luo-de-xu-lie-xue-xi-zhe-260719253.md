---
title: Sequential Learner Modeling Using Multi-Relational Graph Convolutional Networks
title_zh: 基于多关系图卷积网络的序列学习者建模
authors:
- Rawaa Alatrash
- Mohamed Amine Chatti
- Hong Yang
- Yumeng Wang
arxiv_id: '2607.19253'
url: https://arxiv.org/abs/2607.19253
pdf_url: https://arxiv.org/pdf/2607.19253
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 用户建模 · 多关系GCN序列建模
tags:
- GCN
- User Modeling
- Multi-Relational Graph
- Sequential Recommendation
- PKG
one_liner: 提出融合多关系GCN、PKG与SBERT的无监督序列用户建模方法，优化推荐系统用户体验
practical_value: '- 电商用户建模可参考将多关系GCN与用户行为序列结合，区分浏览/加购/下单等不同交互关系的语义，提升用户画像准确度

  - 可复用PKG+预训练语义模型（如SBERT）的组合方案，给商品/内容的图谱节点注入语义信息，优化召回排序的语义相关性

  - 无监督建模的思路可复用在冷启动用户/商品的表征学习场景，降低标注成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有基于GNN的用户建模方法大多将图中不同关系视为同质，无法捕捉丰富语义，且普遍忽略用户交互序列信息，多关系GNN在用户建模场景的应用尚未被探索。

### 方法关键点
提出无监督的MR-ConceptGCN方法，融合Personal Knowledge Graphs（PKG）、多关系GCN、预训练语言模型SBERT，学习PKG条目兼具关系感知与语义感知的增强表征；结合用户长短期交互，基于用户未掌握的知识概念的增强嵌入构建序列学习者模型。

### 关键结果
在线用户研究（n=31）验证，该方法在教育推荐场景下，准确率、有用性、多样性、用户满意度等多个用户中心指标均有显著提升。

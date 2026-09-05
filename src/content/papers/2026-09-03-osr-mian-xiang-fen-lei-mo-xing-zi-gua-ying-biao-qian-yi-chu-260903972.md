---
title: 'OSR: Output Space Redistribution for Adaptive Label Removal in Classification
  Models'
title_zh: OSR：面向分类模型自适应标签移除的输出空间重分配方法
authors:
- Minyi Peng
- Darian Gunamardi
- Ivan Tjuawinata
- Yongsen Zheng
- Kwok-Yan Lam
affiliations:
- Nanyang Technological University
arxiv_id: '2609.03972'
url: https://arxiv.org/abs/2609.03972
pdf_url: https://arxiv.org/pdf/2609.03972
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 分类模型自适应更新 · 无数据标签移除
tags:
- Output Space Redistribution
- Label Removal
- Classification Model
- Taxonomy Update
- Privacy Preserving
one_liner: 提出输出空间重分配的模块化标签移除方案，无需原数据无需重训，性能接近全量重训且保护隐私
practical_value: '- 电商类目迭代时，可直接把OSR作为现有分类模型的输出后处理模块，无需重训就能适配类目下线/合并需求，大幅节省算力和数据成本

  - 涉及敏感用户/商品数据的分类场景（如金融风控、用户属性预测），用OSR可规避重训需要原数据的隐私风险，满足合规要求

  - 推荐系统粗排/召回侧的标签类预训练模型迭代时，可复用输出空间重分配思路，避免全量重训带来的线上停服或版本对齐问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
分类系统（如电商类目、行业编码）随业务迭代经常需要移除/合并标签，现有方案要么全量重训，依赖原数据、算力成本高、隐私风险大；要么调整特征空间，效果不稳定、扩展性差。
### 方法关键点
提出OSR方案，作为模块化的输出过滤器，仅基于现有标签集合和模型原输出置信度做统计重分配，直接拟合全量重训后的输出置信度向量，无需调整模型参数、不需要原训练数据，也不用重新收敛损失函数。
### 关键结果
在多个分类任务上效果与全量重训相当，算力效率提升显著，同时完全规避原数据依赖带来的隐私问题。

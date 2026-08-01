---
title: Explaining Image Similarity with Automatically Extracted Concept Activation
  Vectors
title_zh: 基于自动提取的概念激活向量的图像相似性可解释方法
authors:
- Isaac Roberts
- Petra Bevandic
- Alexander Schulz
- Barbara Hammer
affiliations:
- Bielefeld University - Faculty of Technology
- University of Zagreb - Faculty of Electrical Engineering and Computing
arxiv_id: '2607.28386'
url: https://arxiv.org/abs/2607.28386
pdf_url: https://arxiv.org/pdf/2607.28386
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 图像相似性 · 可解释性
tags:
- CAV
- Sparse Autoencoder
- Image Similarity
- Explainable AI
- Embedding Interpretation
one_liner: 提出模型与度量无关的图像相似性解释框架，用稀疏自编码器提取CAV实现单对/集群图像相似性归因
practical_value: '- 电商多模态检索场景可复用该框架，基于SAE自动提取embedding空间的语义概念（如服饰纹理、颜色），解释召回/粗排阶段的物品相似性排序原因

  - 推荐系统的embedding可解释性优化可借鉴该思路，通过隐空间扰动而非像素/原始特征扰动，降低归因结果偏离真实数据分布的概率

  - 同款/相似款聚类场景可复用组级相似性归因能力，快速定位聚类簇的核心共性特征，降低人工标注成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像相似性解释方法多依赖梯度归因图，仅能提供局部解释，无法给出embedding空间中驱动相似性的全局语义特征（如纹理、形状、颜色），且像素空间扰动容易偏离真实数据分布。

### 方法关键点
提出模型与度量无关的通用框架，用稀疏自编码器（SAE）自动提取Concept Activation Vectors（CAVs）；对单对图像，沿CAV方向扰动embedding并度量相似度变化得到概念重要性，同时输出概念归因图；支持集群级相似性归因，新增样例检索能力挖掘具有相似归因逻辑的样本。

### 关键结果
隐空间扰动对真实数据分布的贴合度显著优于像素空间基线；概念重要性可线性还原真实相似度分数，定性实验验证了单样本与组级相似性判断的解释有效性。

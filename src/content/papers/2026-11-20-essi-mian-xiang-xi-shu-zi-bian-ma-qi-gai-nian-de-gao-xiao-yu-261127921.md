---
title: 'ESSI: Computationally Efficient Semantic Search for Sparse Autoencoder Concepts'
title_zh: ESSI：面向稀疏自编码器概念的高效语义搜索方法
authors:
- James Baker
affiliations:
- UMBC
arxiv_id: '2611.27921'
url: https://arxiv.org/abs/2611.27921
pdf_url: https://arxiv.org/pdf/2611.27921
published: '2026-11-20'
collected: '2026-11-23'
category: Multimodal
direction: 多模态可解释性 · SAE语义特征匹配
tags:
- Sparse Autoencoder
- Semantic Search
- Diffusion Model
- Interpretability
- Feature Selection
one_liner: 提出低成本ESSI方法，快速匹配SAE特征与语义概念，支持扩散模型概念插入与遗忘
practical_value: '- 语义特征匹配场景可复用ESSI的「特征排序+二分搜索最小有效特征集」框架，大幅降低特征筛选的计算成本

  - 电商商品图生成、营销素材生成等多模态业务的概念控制需求，可借鉴该方法快速定位SAE中对应语义的特征，实现精准的概念插入/删除

  - 特征重要性评估、特征选择场景可复用该方法的线性分类器性能阈值判断逻辑，兼顾特征集规模与下游效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Sparse Autoencoders (SAE) 可将扩散模型激活分解为可解释特征，但现有「语义概念到SAE特征匹配」方法依赖网格搜索或重复UNet前向，计算成本极高，无法高效支撑模型语义控制需求。
### 方法关键点
提出ESSI框架：1. 用分割掩码标注SDXL激活的概念/非概念样本，对SAE特征做重要性排序；2. 通过二分搜索筛选满足线性分类器性能阈值的最小特征子集；3. 复用训练好的线性分类器校准语义控制的转向强度，同一套特征可同时支持概念插入与对象遗忘任务。
### 关键结果
相比现有基线，ESSI计算成本相当或更低，在概念插入、对象遗忘两个任务上均达到优异性能。

---
title: 'Beyond Top Words: MonoTM for Topic Modeling with Interpretable Monosemantic
  Features'
title_zh: 超越高频词：基于可解释单语义特征的主题建模框架MonoTM
authors:
- Una Joh
- Bei Yu
affiliations:
- Syracuse University
- School of Information Studies, Syracuse University
arxiv_id: '2609.09575'
url: https://arxiv.org/abs/2609.09575
pdf_url: https://arxiv.org/pdf/2609.09575
published: '2026-09-09'
collected: '2026-09-11'
category: Other
direction: 可解释主题建模 · SAE特征解耦
tags:
- Topic Modeling
- Sparse Autoencoder
- Interpretability
- Semantic Feature
- Text Analysis
one_liner: 解耦主题估计与语义解释任务，基于SAE构建可解释性更强的主题建模框架
practical_value: '- 电商搜索Query聚类、用户评论主题挖掘场景可复用MonoTM的解耦设计，分别优化主题划分准确性和人工可读性，解决传统LDA主题语义模糊难落地问题

  - 做LLM可解释性相关任务时可参考「任务适配的SAE特征子集选择」思路，不同下游任务选择不同的稀疏激活特征组合，兼顾效果和可解释性

  - 生成式推荐的用户兴趣主题建模场景，可引入单语义特征替代单个关键词做兴趣标签，提升用户兴趣标签的可读性和覆盖度'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统主题模型依赖高频词表达主题语义，易出现语义模糊、可解释性差的问题；稀疏自编码器(SAE)可从稠密表征中提取可解释特征，但特征可解释性与主题推理质量的关联关系尚不明确。
### 方法关键点
MonoTM框架解耦文档-主题混合估计、主题语义解释两个任务：前者基于全量SAE特征袋表征计算，保证全局主题结构准确性；后者固定混合估计结果，基于语料对齐的独立语义特征词汇表学习主题描述符，提升可解释性。
### 关键结果
在3个基准语料库上验证，相比传统主题模型，MonoTM在保留全局主题结构效果的同时，主题语义单元的可读性显著优于单个词表达，更适配下游语料分析任务。

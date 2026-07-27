---
title: Unsupervised Multimodal Intent Discovery via MLLM-Guided Concept Generation
  and Semantic Propagation
title_zh: 基于MLLM引导概念生成与语义传播的无监督多模态意图发现
authors:
- Yunjin Gu
- Qianrui Zhou
- Hua Xu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Tsinghua University
arxiv_id: '2607.21908'
url: https://arxiv.org/abs/2607.21908
pdf_url: https://arxiv.org/pdf/2607.21908
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: 多模态意图理解 · 无监督聚类
tags:
- Multimodal Intent Discovery
- MLLM
- Unsupervised Clustering
- Concept Generation
- Semantic Propagation
one_liner: 提出MCSP无监督框架，通过MLLM概念生成与语义传播实现可解释多模态意图发现
practical_value: '- 无标注电商用户会话/搜索query意图挖掘可复用「簇代表样本筛选→MLLM相邻簇对比生成语义概念」的流程，大幅降低标注成本

  - 语义加权图+语义传播的伪标签生成方法可直接迁移到冷启动用户/物品的无监督聚类场景，同时提升聚类结果可解释性

  - 多模态意图聚类框架可复用在电商多模态搜索（图文混合query）的意图理解模块，优化搜索结果匹配精度'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
无监督多模态意图发现无需人工标注即可挖掘会话/搜索query的潜在意图，但现有方法仅依赖特征几何相似度优化，缺乏高阶语义指导，聚类结果可解释性差，无法满足业务场景对意图可解释性的要求。
### 方法关键点
1. 提出全无监督框架MCSP，首先为每个初始簇筛选高质量代表性样本；
2. 输入MLLM对相邻簇做对比推理，生成可解释的高阶语义概念作为聚类监督信号；
3. 基于语义加权图做语义传播，对齐概念信息与局部结构一致性，生成可靠伪标签优化表征。
### 关键结果
在3个公开多模态意图数据集上效果全面超越现有SOTA方法，同时输出具备明确语义概念支撑的可解释聚类结果。

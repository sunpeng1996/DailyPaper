---
title: Vision-Grounded Semantic Learning and Alignment for Scalable Multilingual Text-Based
  Person Retrieval
title_zh: 面向可扩展多语言文本行人检索的视觉语义学习与对齐
authors:
- Xinyu Zhou
- Fan Li
- Shasha Chen
- Min Cao
- Ahtamjan Ahmat
- Qiaoming Zhu
- Mang Ye
affiliations:
- Soochow University
- The Xinjiang Technical Institute of Physics & Chemistry, Chinese Academy of Sciences
- Wuhan University
arxiv_id: '2611.15328'
url: https://arxiv.org/abs/2611.15328
pdf_url: https://arxiv.org/pdf/2611.15328
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 多模态跨语言检索 · 语义对齐
tags:
- Multimodal Retrieval
- Cross-lingual Learning
- MoE
- Cross-modal Alignment
- Pre-training Dataset
one_liner: 发布10M级多语言行人图文预训练数据集，以及无 pivot 语言的跨模态对齐检索框架
practical_value: '- 多语言跨模态对齐可复用无 pivot 语言的语义探针设计，避免单一语言 bias，适配跨境电商多语种商品图文检索场景

  - MoE 路由语言不变语义到专属专家的设计，可迁移至多语言用户生成内容（UGC）的语义理解任务，降低不同语种特征干扰

  - 质量感知的多语言图文数据构造 pipeline 可直接复用，大幅降低多模态预训练数据集的构建成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多语言文本行人检索（TBPR）研究稀缺，仅有的落地方案缺乏大规模预训练数据集支撑，且共享编码器忽略语言异质性、依赖英语作为对齐 pivot 引入英语中心 bias，难以适配多语种实际场景。
### 方法关键点
1. 开源 MultiPedes 数据集，为该领域首个大规模预训练数据集，通过质量感知构造流程生成覆盖4语种的10M行人图文对；
2. ViSeLA 框架包含两大核心模块：一是基于 MoE 的语义感知多语言学习模块，路由语言不变语义到专属专家优化多语言特征学习；二是视觉 grounded 跨模态对齐模块，通过语义探针捕捉细粒度跨模态语义，无需 pivot 语言即可实现直接对齐。
### 关键结果
在多语言 TBPR 基准、英文单语种 TBPR 基准上均取得 SOTA 精度表现

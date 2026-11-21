---
title: 'Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language
  Models'
title_zh: 探查「意识」心智：视觉语言模型中的选择性访问与全局工作空间
authors:
- Jiahao Huang
- Jun Wang
affiliations:
- Imperial College London
- University College London
arxiv_id: '2611.26590'
url: https://arxiv.org/abs/2611.26590
pdf_url: https://arxiv.org/pdf/2611.26590
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 多模态大模型 · 内部机制探测
tags:
- VLM
- Global Workspace Theory
- Concept Probing
- Multimodal Alignment
- Model Interpretability
one_liner: 提出多模态概念探测框架MC-Lens，验证视觉语言模型符合全局工作空间理论的概念处理规律
practical_value: '- MC-Lens的J-space跨模态对齐度量方法可复用到多模态搜索/推荐的语义对齐效果评估，敏感度优于传统隐层余弦相似度

  - 选择性访问晚于概念对齐的训练规律可指导多模态推荐模型训练流程设计：优先完成跨模态对齐再做下游任务适配，提升训练效率

  - 概念干预实验方法可用于多模态Agent决策归因，定位多模态推荐、图文搜索结果出错的核心概念偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM内部概念表示黑盒化，缺乏量化工具探测跨模态概念处理规律，也无法验证其是否符合认知科学的全局工作空间理论（GWT）。
### 方法关键点
Multimodal Concept Lens（MC-Lens）为基于雅可比矩阵的多模态探测工具，可将视觉编码器、语言解码器的中间状态映射到解码器词汇表定义的共享语义空间，支持跨模态概念可及性对比与内部概念干预；将单token读出载体扩展为token集，提升概念信息捕捉精度。
### 关键结果
1. 配套J-space度量比传统隐层余弦相似度更清晰地追踪跨模态概念对齐过程；
2. VLM可靠的选择性访问能力的训练成熟阶段晚于概念可及性；
3. 不同架构、不同参数量的VLM均存在一致的概念可及性、查询依赖选择性、跨任务干预效应规律。

---
title: Rank-Aware Hyperbolic Alignment for Vision-Language Dataset Distillation
title_zh: 面向视觉语言数据集蒸馏的秩感知双曲对齐方法
authors:
- Jongoh Jeong
- Sun-Kyung Lee
- Kuk-Jin Yoon
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
- Electronics and Telecommunications Research Institute (ETRI)
arxiv_id: '2606.29464'
url: https://arxiv.org/abs/2606.29464
pdf_url: https://arxiv.org/pdf/2606.29464
published: '2026-06-27'
collected: '2026-07-03'
category: Multimodal
direction: 多模态训练 · 数据集蒸馏优化
tags:
- Dataset Distillation
- Vision-Language Model
- Hyperbolic Embedding
- Cross-Modal Alignment
- Low-Rank Optimization
one_liner: 提出秩感知双曲对齐框架RAHA，优化视觉语言数据集蒸馏效果与跨模态迁移鲁棒性
practical_value: '- 跨模态商品检索的特征对齐可借鉴秩感知非对称优化思路，对语义共享子空间做强对齐，模态私有空间保留多样性，提升泛化性

  - 小样本/低算力场景下训练多模态召回模型时，可尝试将特征映射到双曲空间做测地线对齐，替代传统欧氏对齐降低开销

  - 多模态Item Embedding蒸馏时，可复用残差子空间正则化方法，保留模态独有信息，提升跨域迁移鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉语言数据集蒸馏（VLDD）默认在欧氏空间做全维度跨模态对齐，受跨模态相关性秩缺失限制（共享语义集中在低维子空间，剩余维度为弱相关残差），约束过强效果不佳；低秩分解类对齐方法又缺乏对核心对齐结构的显式管控，迁移鲁棒性不足。
**方法关键点**：1. 提出秩感知双曲对齐（RAHA）框架，将多模态表示映射到层次结构适配的双曲空间；2. 设计非对称优化目标：共享语义子空间强制测地线对齐，残差子空间加正则保留模态私有多样性，显式控制对齐容量。
**关键结果**：固定数据与算力预算下，跨模态检索性能达到同期SOTA水平，迁移鲁棒性指标较基线方法有显著提升。

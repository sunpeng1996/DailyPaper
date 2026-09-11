---
title: On the Regularization Landscape for the Linear Recommendation Models
title_zh: 线性推荐模型的正则化机制统一分析与低秩闭式解优化
authors:
- Dong Li
- Zhenming Liu
- Ruoming Jin
- Hao Zhou
- Zhi Liu
- Jing Gao
- Bin Ren
affiliations:
- Kent State University
- College of William and Mary
- iLambda
arxiv_id: '2609.11876'
url: https://arxiv.org/abs/2609.11876
pdf_url: https://arxiv.org/pdf/2609.11876
published: '2026-09-10'
collected: '2026-09-11'
category: RecSys
direction: 线性推荐 · 正则化与低秩优化
tags:
- Linear_RecSys
- Regularization
- Nuclear_Norm
- Frobenius_Norm
- Closed_Form_Solution
- Low_Rank_Approximation
one_liner: 统一线性推荐模型正则化分类，提出兼具核范数与Frobenius范数优势的低秩闭式解
practical_value: '- 业务上线优先选择Frobenius范数类线性模型（如EASE/EDLAE），比核范数类模型（正则化PCA、VLAE等）nDCG@100高3~8个百分点，训练简单无需复杂调参

  - 大物料池场景可直接复用论文提出的LR-EDLAE-1/2低秩闭式解，无需调优ADMM超参，存储消耗降低70%以上的前提下效果与满秩EDLAE几乎持平

  - 核范数类正则化天生存在性能天花板，无需在基于核范数的MF/线性自编码器上做过多优化投入，性价比远低于Frobenius范数类模型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
近年大量深度学习推荐模型在基准测试中表现甚至不如简单线性推荐模型，且不同线性模型性能接近但技术路径差异大，缺乏统一理论框架解释性能差异来源，也缺少兼顾低部署成本与高效果的线性模型实现。

### 方法关键点
- 将现有SOTA线性推荐模型的正则化统一划分为两类：核范数（Nuclear Norm）类仅保留输入矩阵的奇异向量、按固定规则收缩奇异值，存在刚性结构限制表达能力；Frobenius范数类表达能力更强，但低秩版本需依赖难调参的ADMM算法。
- 证明线性变分自编码器（LVAE）、带dropout的MF本质都是核范数正则化的不同实现，其性能天花板由正则化结构决定，与技术路径无关。
- 提出两种低秩Frobenius范数正则化的闭式解LR-EDLAE-1、LR-EDLAE-2，同时保留核范数的低秩、闭式解优势和Frobenius范数的高表达能力。

### 关键实验
在ML-20M、Netflix、MSD三个公开基准数据集上对比12种基线模型，满秩Frobenius范数类模型EDLAE比核范数类最优模型nDCG@100高0.03~0.10；提出的低秩闭式解LR-EDLAE-1/2与ADMM实现的低秩EDLAE效果几乎持平，nDCG@100差距<0.002，训练速度提升10倍以上。

### 核心结论
线性推荐模型的性能天花板由正则化类型决定，而非所包装的深度学习技术，Frobenius范数类模型的效果与工程效率综合优势远高于核范数类。

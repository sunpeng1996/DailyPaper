---
title: Non--negative matrix factorization using the \textit{R} package \textsf{nnmf}
title_zh: 基于R包nnmf的非负矩阵分解实现与性能对比
authors:
- Volkan Sevinç
- Nikolas Kontemeniotis
- Theodoros Perdikis
- Michail Tsagris
affiliations:
- Mugla Sitki Kocman University
- University of Crete
- University of Piraeus
arxiv_id: '2607.20084'
url: https://arxiv.org/abs/2607.20084
pdf_url: https://arxiv.org/pdf/2607.20084
published: '2026-07-22'
collected: '2026-07-24'
category: Other
direction: 非负矩阵分解 · R工具包性能评估
tags:
- NMF
- R-package
- Dimensionality-Reduction
- Recommender-System
- Performance-Evaluation
one_liner: 推出新R语言NMF工具包nnmf，基于真实数据对主流NMF包做多维度性能对比
practical_value: '- 做推荐系统召回/用户建模采用NMF时，可参考本文的评估维度（效率、收敛性、重建精度、内存占用、稳定性）选择合适的NMF实现包

  - 自研NMF类矩阵分解算法时，可复用本文基于真实业务数据而非模拟数据的评估框架，更贴合业务实际表现

  - 电商场景用户/物品交互矩阵天然非负，可直接试用本次发布的nnmf包做隐语义挖掘，降低开发成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
NMF是成熟的非负数据降维、隐结构提取技术，在推荐系统、文本挖掘等领域应用广泛，但现有不同R语言NMF实现包缺乏真实场景下的系统性性能评估，从业者选型无客观参考依据。
### 方法关键点
1. 发布全新开源R语言NMF实现包nnmf
2. 搭建统一实验框架，全部采用真实数据而非模拟数据开展评测，覆盖真实场景下数据的复杂度、异构性、噪声特性
3. 从计算效率、收敛行为、重建精度、内存占用、分解结果稳定性5个核心维度，与2款市面主流NMF R包做横向对比
### 关键结果
输出各主流NMF包的多维度性能对标数据，可直接作为业务场景下NMF工具选型的客观参考，帮助开发者减少选型试错成本。

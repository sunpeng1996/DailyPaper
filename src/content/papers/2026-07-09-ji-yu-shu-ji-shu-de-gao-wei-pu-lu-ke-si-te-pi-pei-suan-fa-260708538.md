---
title: High-Dimensional Procrustes Matching via Tree Counts
title_zh: 基于树计数的高维普鲁克斯特匹配算法
authors:
- Xiaochun Niu
- Tselil Schramm
- Jiaming Xu
affiliations:
- Duke University
- Stanford University
arxiv_id: '2607.08538'
url: https://arxiv.org/abs/2607.08538
pdf_url: https://arxiv.org/pdf/2607.08538
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 高维向量匹配 · 统计学习理论
tags:
- Procrustes-Matching
- High-Dimensional-Statistics
- Tree-Counting
- Exact-Recovery
- Gaussian-Vectors
one_liner: 提出基于宽树加权计数的多项式时间算法，实现高维场景下常数相关度的Procrustes匹配精确恢复
practical_value: '- 跨平台用户/物品embedding对齐任务可借鉴宽树计数思路，替代传统余弦匹配，提升低相关度下的匹配准确率

  - 异构特征对齐（如多模态图文向量匹配、跨域特征映射）场景可参考该算法的常数相关度恢复阈值做基线调优

  - 高维向量匹配类任务可直接复用其给出的信息论下界作为性能天花板参考，避免无效的精度优化尝试'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统Procrustes匹配仅在d=O(log n)低维场景有成熟解法，高维d≫log n场景下现有方案要求相关度ρ接近1才能实现恢复，性能瓶颈明显，无法适配实际高维向量匹配需求。
### 方法关键点
设计基于自定义宽树家族加权计数的多项式时间匹配算法，通过计算两组高维高斯向量的宽树加权计数相似度做对齐，无需接近完美的相关度即可恢复未知排列。
### 关键结果数字
1. 当d≥polylog(n)、ρ²>√α（α≈0.338为Otter树计数常数）时，算法高概率实现精确恢复；
2. 信息论层面证明精确恢复的下界为ρ²≳max{log n/d, √(log n/n)}；
3. 低阶优势计算验证ρ²>√α是所有树计数类算法的必要适用条件。

---
title: Exponential Convex Calibration Dimension for the Multi-Label Jaccard Measure
title_zh: 多标签Jaccard度量的指数凸校准维度
authors:
- Mingyuan Zhang
affiliations:
- Independent Researcher
arxiv_id: '2608.13549'
url: https://arxiv.org/abs/2608.13549
pdf_url: https://arxiv.org/pdf/2608.13549
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 多标签分类损失校准理论研究
tags:
- Multi-label Classification
- Jaccard Loss
- Convex Calibration
- MinHash
- Surrogate Loss
one_liner: 证明Jaccard精确凸校准需指数维度，给出两类多项式维度近似方案及对应后悔上界
practical_value: '- 做多标签召回、多兴趣建模的Jaccard/IoU优化时，无需追求零后悔的精确校准，直接选用多项式维度近似方案降低计算开销

  - 可复用F1-to-Jaccard后悔转移方法，直接复用现有成熟F1代理损失优化目标，保证Jaccard后悔上限可控在约0.172

  - 多标签分类/匹配任务的近似度量优化可复用MinHash随机特征构造低维代理损失，灵活平衡精度要求与计算成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
Jaccard（IoU）是多标签分类、图像分割的核心度量，其非跨标签可分解的特性导致凸校准的维度边界长期不明确，工业界近似优化方案缺乏理论支撑。
### 方法关键点
结合有限MinHash Gram表示与布尔Möbius反演证明Jaccard损失矩阵非奇异性；推导精确校准的凸校准维度上下界；提出两类多项式维度近似方案：F1-to-Jaccard后悔转移、MinHash平方损失代理。
### 关键结果数字
- 精确校准所需维度为$2^{s-1} \sim 2^s-1$，随标签数$s$指数增长
- F1转移方案渐近Jaccard后悔上限为$3-2\sqrt{2} \approx 0.172$，仅需$O(s^2)$维度
- 带符号MinHash方案维度为$O((s+\log(1/\rho))/\alpha^2)$，可在任意$\alpha$后悔容忍下达到多项式维度

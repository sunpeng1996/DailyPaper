---
title: Nuclear Norm-Regularized Bayesian Matrix Completion
title_zh: 核范数正则化的贝叶斯矩阵补全方法
authors:
- Calvin Tolbert
affiliations:
- Cornell University
arxiv_id: '2609.30078'
url: https://arxiv.org/abs/2609.30078
pdf_url: https://arxiv.org/pdf/2609.30078
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: 推荐系统 · 矩阵补全 不确定性量化
tags:
- Matrix Completion
- Nuclear Norm
- Bayesian Learning
- Uncertainty Quantification
- Recommender System
one_liner: 提出首个带非渐近复杂度保证的未知噪声方差下核范数正则贝叶斯矩阵补全采样器
practical_value: '- 该方法为理论可行性证明，当前多项式复杂度暂不满足工业级大规模推荐场景的部署要求，仅可作为理论参考

  - 针对小体量推荐场景（如小众垂类冷启预估、小流量实验效果补全），可参考其将噪声精度离散化结合热力学积分构建后验分布的思路

  - 仅单变量导致的非对数凹采样问题均可参考本方法的离散化网格+热力学积分处理思路，不限于矩阵补全场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统核范数正则化矩阵补全仅输出点估计，无内置不确定性量化能力；现有贝叶斯矩阵补全方案需预先已知噪声方差，不符合实际业务真实情况。
### 方法关键点
将噪声精度分布离散到网格空间，通过热力学积分构建分类后验，是首个适配未知噪声方差场景的核范数正则贝叶斯矩阵补全采样器，思路可迁移至仅单变量导致非对数凹、其余变量联合分布非光滑的其他采样问题。
### 关键结果
采样器复杂度为矩阵维度、目标精度倒数的多项式级，仅为理论可行性证明，当前版本不适用于大规模工业场景部署。

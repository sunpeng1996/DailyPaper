---
title: 'Online Supervised Dimension Reduction with Random Features: Diagnostics and
  Computational Trade-offs'
title_zh: 带随机特征的在线监督降维：诊断分析与计算权衡
authors:
- Zhenlin Yao
- Wei Xiong
affiliations:
- School of Statistics, University of International Business and Economics
arxiv_id: '2609.20454'
url: https://arxiv.org/abs/2609.20454
pdf_url: https://arxiv.org/pdf/2609.20454
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 在线监督降维 · 计算效率权衡
tags:
- Online Dimension Reduction
- Random Features
- Supervised PCA
- Subspace Tracking
- Computational Tradeoff
one_liner: 量化诊断在线核监督PCA的子空间估计偏差、计算成本与下游效果的权衡规律
practical_value: '- 推荐系统召回/排序阶段的在线特征降维可参考选型策略：分类场景优先按需计算精确SVD降维，高维稠密回归场景可采用Adam式在线基更新替代全量SVD降低计算耗时

  - 做在线子空间更新时不要仅用终端优化精度评估效果，需额外验证子空间总体泛化能力与下游任务效果的相关性，避免几何偏差导致的预测损失

  - 在线降维缓存的中间状态需做几何偏差校验，不建议直接用于高稳定性要求的推荐推理链路，可降级用于非核心流量的预实验场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
工业流场景下在线监督降维普遍存在优化精度与下游预测效果、子空间泛化能力脱节的问题，在线核监督PCA（OKSPCA）的计算策略选型缺乏明确的量化权衡依据。
### 方法关键点
针对融合有限随机特征中心化交叉矩、Adam式正交基更新的OKSPCA框架，通过固定映射一致性、浓度与扰动分析拆解估计器与真实子空间的差异，设计同目标对比实验，覆盖6个预测基准与多类数值服务负载做评估。
### 关键结果
分类场景下按需计算精确降维比在线迭代更快，平均可捕获几乎全部终端目标能量；高维稠密回归场景下Adam式在线更新比全量thin-SVD耗时更低，但存在持续几何偏差；替换在线迭代器为精确经验目标后，两类回归任务的精度损失基本不变。

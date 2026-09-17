---
title: Probabilistic Linear Explanations
title_zh: 概率线性可解释性框架
authors:
- Frederic Koriche
- Jean-Marie Lagniez
- Chi Tran
affiliations:
- CRIL, UMR CNRS 8188, University of Artois
arxiv_id: '2609.19077'
url: https://arxiv.org/abs/2609.19077
pdf_url: https://arxiv.org/pdf/2609.19077
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 机器学习可解释性 · 概率线性解释
tags:
- XAI
- Probabilistic Explanation
- Sparse Linear Model
- MIP
- Iterative Hard Thresholding
one_liner: 提出适用于二分类与回归任务的稀疏锚定线性概率可解释框架，效果优于LIME等主流基线
practical_value: '- 电商推荐/广告排序模型的特征归因场景可直接复用该框架的k-sparse约束，生成符合用户认知上限的解释，降低合规风险与用户信任成本

  - 可直接替换现有LIME类解释方案，在不额外增加特征数的前提下获得更低的解释误差，提升归因结果可信度

  - 高stakes场景（如金融信贷推荐、电商合规校验）可采用MIP方案求最优解释，普通流量场景用IHT算法兼顾效果与推理效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有溯因解释涉及特征过多超出人类认知上限，且概率松弛类解释方案大多仅支持分类任务，无法覆盖回归等工业界常见场景。
### 方法关键点
1. 基于稀疏锚定线性模型搭建统一概率可解释框架，同时支持二分类与连续回归任务，将实例映射到布尔超立方体，可捕捉特征贡献的幅度与方向，严格遵循指定稀疏度k约束；
2. 将难解的相关性误差最小化目标转化为易解的保真度误差代理目标，给出k稀疏解释的相关性误差上界；
3. 提供两种互补求解方案：可输出最优解的MIP公式（多项式样本复杂度）、多项式时间的IHT近似算法（带近似保证）。
### 关键结果
对比LIME、MAPLE等SOTA基线，该方法天然满足锚定与稀疏约束，相关性误差显著低于同类方案。

---
title: Accelerating Conformal Prediction via Approximate Leave-One-Out
title_zh: 基于近似留一法的保形预测加速方法
authors:
- Jiachen Cong
- Jingbo Liu
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.31915'
url: https://arxiv.org/abs/2606.31915
pdf_url: https://arxiv.org/pdf/2606.31915
published: '2026-06-30'
collected: '2026-07-01'
category: Eval
direction: 不确定性量化 · 保形预测加速
tags:
- Conformal Prediction
- Approximate Leave-One-Out
- Uncertainty Quantification
- Computational Efficiency
- Jackknife+
one_liner: 引入近似留一估计器加速保形预测，在保障性能前提下大幅降低运行耗时
practical_value: '- 推荐/广告冷启动、新Item预估等不确定性量化场景，可替换高成本Jackknife+方案，用该ALO加速的保形预测方法降低计算开销

  - AB实验效果显著性校验场景可复用近似留一思路，避免全量留一交叉验证的高耗时，提升实验迭代效率

  - LLM生成式推荐结果的置信度校验场景，可低成本输出带覆盖性保障的置信区间，平衡性能与计算成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
保形预测是预测推理中不确定性量化的通用框架，具备无分布假设的覆盖性保障，但现有方案计算成本过高：Full Conformal Prediction需要遍历候选响应值，Jackknife+等优化方案仍需对所有训练样本执行留一重拟合，难以落地到大样本、高维的工业场景。
### 方法关键点
引入近似留一（ALO）估计器适配保形预测场景，对高维统计中原有ALO交叉验证风险估计的分析方法做适配修改，使其支持对新样本$x_{n+1}$的留$i$残差计算而非仅适配训练样本$x_i$，从理论上证明了该方法的渐近覆盖率与效率。
### 关键结果
仿真实验验证，基于ALO的保形预测方法覆盖率、预测效率与精确保形预测方法相当，运行耗时较现有方案大幅降低。

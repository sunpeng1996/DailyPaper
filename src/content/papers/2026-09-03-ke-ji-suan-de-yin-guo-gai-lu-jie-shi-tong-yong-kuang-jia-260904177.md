---
title: A Computationally Feasible Framework for Causal Probabilistic Explanation
title_zh: 可计算的因果概率解释通用框架
authors:
- Rafal Urbaniak
- Sam Witty
- Daniel Waxman
- Andy Zane
- Poorva Garg
- Emily Bunnapradist
- Sankaran Vaidyanathan
- Jack Feser
- Drew Lehe
- Eli Bingham
affiliations:
- Basis Research Institute
- Sorbus AI
- Massachusetts Institute of Technology
- University of Massachusetts Amherst
- University of California, Los Angeles
arxiv_id: '2609.04177'
url: https://arxiv.org/abs/2609.04177
pdf_url: https://arxiv.org/pdf/2609.04177
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 因果归因 · 模型可解释性
tags:
- Causal Explainability
- Feature Attribution
- Actual Causality
- Monte Carlo Estimation
- PCI
one_liner: 提出PCI因果归因框架，兼顾实际因果理论严谨性与大规模工业场景的可扩展性
practical_value: '- 推荐/广告排序模型的特征归因可替换SHAP，用PCI框架得到符合因果结构的归因结果，避免特征重要性误判影响迭代方向

  - 业务异动归因（如大促营收波动、推荐ctr异动）可复用PCI的蒙特卡洛近似思路，无需枚举全量反事实场景即可得到可解释的因果结论

  - 官方开源代码可直接二次开发，适配电商亿级样本的训练后模型归因场景，比传统实际因果方法计算成本低两个数量级以上'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有因果归因方案存在明显短板：实际因果（AC）理论严谨但需枚举反事实场景，仅能适配小体量模型；SHAP等可扩展归因方法忽略数据生成的因果结构，结果常与严谨因果分析冲突，工业级大规模场景缺乏兼顾因果严谨性与计算效率的归因方案。

### 方法关键点
提出概率因果影响（PCI）框架，基于AC理论与Pearl的必要性/充分性概率定义，将可解释性问题转化为概率因果模型上的估计问题，通过Monte Carlo方法即可快速近似；通过定义候选解释分布、反事实值分布、打分函数三类组件，输出兼具因果依据、可扩展、可分级的解释结果，可向下兼容AC与Pearl因果概率的退化场景。

### 关键结果
在合成数据、连续动力系统、基于百万级样本训练的工业部署因果模型上验证有效，与AC结果一致性达标，相比传统AC方法计算效率提升百倍级，可适配千万级样本规模的模型归因。

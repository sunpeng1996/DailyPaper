---
title: Statistical Efficiency and Inference of Quantile Distributional Reinforcement
  Learning
title_zh: 分位数分布强化学习的统计效率与推断
authors:
- Zijie Cheng
- Yang Peng
- Zhihua Zhang
affiliations:
- 北京大学数学科学学院
- 清华大学丘成桐数学科学中心
arxiv_id: '2607.08444'
url: https://arxiv.org/abs/2607.08444
pdf_url: https://arxiv.org/pdf/2607.08444
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 分布强化学习 · 统计效率与推断分析
tags:
- Distributional RL
- Quantile Regression
- Statistical Efficiency
- Asymptotic Inference
- Sample Complexity
one_liner: 推导分位数分布强化学习的非渐近误差界与渐近特性，证明样本效率最优并提供统计推断基础
practical_value: '- 若业务中用分布RL做风险敏感决策（如动态定价、营销预算分配），可参考其分位数数量m与样本量n的误差缩放关系$√(m/n)$，平衡估计精度与样本成本

  - 对RL策略收益做上线前显著性验证时，可复用其推导的渐近分布与Berry-Esseen定理构造统计置信区间，提升决策严谨性

  - 无分布RL相关需求的推荐/广告业务场景，可借鉴价值有限'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分位数分布强化学习的统计特性缺乏系统性理论证明，样本效率、推断有效性等核心问题无明确结论，限制其落地应用的可靠性。
### 方法关键点
聚焦分布策略评估问题，基于分位数投影的分布Bellman方程推导分位数不动点，构造基于经验MDP的估计器，分别在固定分位数数量、分位数数量发散两种场景下开展理论分析。
### 关键结果
1. 固定分位数数量m时，估计误差缩放为$Õ(√(m/n))$，达到最优参数收敛率$√n$；
2. 推导分位数参数的渐近分布，证明估计器达到半参数效率界；
3. 分位数数量发散时，估计器仍保持渐近效率，匹配非参数模型的半参数效率界；
4. 建立光滑泛函的Berry-Esseen定理，为收益分布泛函的统计推断提供理论支撑。

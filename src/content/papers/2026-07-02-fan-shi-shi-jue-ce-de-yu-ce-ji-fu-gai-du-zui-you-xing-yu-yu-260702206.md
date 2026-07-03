---
title: 'Prediction Sets for Counterfactual Decisions: Coverage, Optimality, and Conformal
  Prediction'
title_zh: 反事实决策的预测集：覆盖度、最优性与共形预测
authors:
- Yurui Zheng
- Ying Jin
affiliations:
- Peking University
- University of Pennsylvania
arxiv_id: '2607.02206'
url: https://arxiv.org/abs/2607.02206
pdf_url: https://arxiv.org/pdf/2607.02206
published: '2026-07-02'
collected: '2026-07-03'
category: Other
direction: 反事实决策 · 共形预测优化
tags:
- conformal-prediction
- counterfactual-inference
- uncertainty-quantification
- decision-theory
- risk-averse-optimization
one_liner: 提出策略耦合覆盖度框架与PC-RACP方法，实现反事实决策下共形覆盖与效用最优的统一
practical_value: '- 电商发券、营销触达等高风险决策场景可引入PC-RACP框架，在保证效果覆盖度的同时提升整体决策效用，避免反事实偏差导致的策略失效

  - 可复用策略耦合覆盖度思想，将不确定性量化模块与决策策略绑定优化，而非独立做预测后再做决策，减少中间环节的效用损耗

  - 风险敏感的推荐/广告冷启动场景可借鉴两阶段共形预测流程，用有限样本即可获得严格的覆盖保证，降低新策略试错成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有共形预测等不确定性量化方法仅能提供统计有效性保证，未关联反事实场景下决策与结果的耦合关系，无法直接支撑最优决策，忽略决策规则对不确定性的依赖会导致决策有效性和效用双下降。
### 方法关键点
1. 提出**policy-coupled coverage（策略耦合覆盖度）**概念，作为不确定性与决策的无损接口，要求覆盖预测集诱导的动作下的实际结果；
2. 证明该覆盖度约束下的预测集优化等价于风险厌恶的策略优化，可导出群体最优预测集的显式形式；
3. 提出两阶段算法PC-RACP，可在有限样本下近似最优预测集，具备严格的有限样本覆盖保证。
### 关键结果
仿真及真实邮件营销实验验证，PC-RACP在维持有效覆盖的前提下，效用显著优于现有基准方法；忽略决策问题的反事实结构，会导致决策有效性和效用双双次优

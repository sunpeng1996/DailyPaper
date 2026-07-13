---
title: A Statistical Test for the Benefits of Personalizing Interventions
title_zh: 个性化干预收益的统计检验方法
authors:
- Zhaoqi Li
- Emma Brunskill
affiliations:
- Stanford University
arxiv_id: '2607.08951'
url: https://arxiv.org/abs/2607.08951
pdf_url: https://arxiv.org/pdf/2607.08951
published: '2026-07-09'
collected: '2026-07-13'
category: Eval
direction: 个性化干预收益评估 · 统计检验
tags:
- Statistical Test
- Personalization
- Hypothesis Testing
- Treatment Effect
- RecSys Evaluation
one_liner: 提出严格控制Type-I error的统计检验方法，量化个性化干预相比最优单一干预的潜在收益
practical_value: '- 上线个性化推荐/广告干预策略前，可复用该检验方法基于历史数据量化收益，对比最优通用策略的ROI，避免盲目上个性化带来的额外成本浪费

  - 检验方法自带严格Type-I error控制，可直接用于AB实验前的预评估，降低策略上线的决策风险

  - 该检验的最小方差渐近正态特性可直接复用到个性化策略效果显著性计算模块，无需重新推导统计性质'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
跨医疗、营销、推荐等多领域的个性化干预虽理论收益明确，但落地成本高、鲁棒性差，缺乏可靠的量化工具判断个性化策略是否显著优于最优单一通用干预，难以支撑ROI决策。

### 方法关键点
针对性统计假设检验方法逻辑：基于历史干预数据验证个性化策略性能是否超过最优单一干预；严格控制Type-I error，指定条件下具备最小方差的渐近正态性，无需复杂调参即可适配多场景。

### 关键结果
在职业培训、抑郁症治疗、教育、推荐系统4类异质数据集上验证，相比现有同类检验方法性能更优，通用性更强，可直接支撑各领域干预决策。

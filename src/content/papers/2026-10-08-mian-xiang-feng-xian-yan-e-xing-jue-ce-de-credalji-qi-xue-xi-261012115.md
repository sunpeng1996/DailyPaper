---
title: Credal Machine Learning for Risk-Averse Decision Making
title_zh: 面向风险厌恶型决策的Credal机器学习方法
authors:
- Timo Löhr
- Paul Hofman
- Maximilian Muschalik
- Eyke Hüllermeier
affiliations:
- LMU Munich
- MCML
- DFKI
arxiv_id: '2610.12115'
url: https://arxiv.org/abs/2610.12115
pdf_url: https://arxiv.org/pdf/2610.12115
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 风险厌恶决策 · 认知不确定性建模
tags:
- Risk-Averse Decision
- Credal Set
- CVaR
- Epistemic Uncertainty
- Distribution Shift
one_liner: 基于credal集建模认知不确定性，结合新决策规则实现低性能损耗的可靠风险规避
practical_value: '- 电商大促、广告投放等高风险场景，可借鉴credal集建模损失分布的认知不确定性，替代单纯的CVaR优化，规避极端亏损决策

  - 推荐系统遭遇分布偏移（如新用户、新类目冷启动）时，可复用该方法的决策规则，在平均效果下降极小的前提下避免灾难性bad case

  - Agent在动态未知环境做序列决策时，可引入该风险规避框架，降低极端错误决策的出现概率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于CVaR的风险厌恶模型受限于对真实损失分布的认知不确定性，无法可靠规避最坏情况，在分布偏移、安全敏感场景极易出现灾难性决策。

### 方法关键点
1. 用credal集（概率分布集合）建模认知不确定性，开发高效学习器输出credal集形式的预测结果
2. 设计全新决策规则，将每个credal集映射为单一预测分布，实现CVaR最小化

### 关键结果
在分类任务、分布偏移场景、强化学习任务中均能可靠避免灾难性决策，且预期性能损失极低。

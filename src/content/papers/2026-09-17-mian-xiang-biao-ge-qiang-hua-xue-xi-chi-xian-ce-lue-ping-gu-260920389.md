---
title: Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement
  Learning
title_zh: 面向表格强化学习离线策略评估的基于模型Bootstrap方法
authors:
- Weiwei Wang
- Yuqiang Li
- Xianyi Wu
- Bingyi Jing
affiliations:
- Department of Statistics and Data Science, Southern University of Science and Technology
- School of Statistics & KLATASDS-MOE, East China Normal University
- School of Artificial Intelligence, The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2609.20389'
url: https://arxiv.org/abs/2609.20389
pdf_url: https://arxiv.org/pdf/2609.20389
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 离线强化学习 · 策略评估不确定性量化
tags:
- OPE
- Bootstrap
- MDP
- Uncertainty Quantification
- Offline RL
- Tabular RL
one_liner: 提出适配多类离线数据的模型驱动Bootstrap框架，实现表格RL离线策略评估的可靠不确定性量化
practical_value: '- 电商搜索/推荐的离线排序策略、流量分配策略评估时，可复用该框架处理不完整用户行为轨迹，无需完整会话即可做不确定性估计

  - 高风险场景（大促流量分配、广告投放策略）上线前，可用该方法生成策略收益置信区间，评估波动范围降低上线风险

  - 离线轨迹数据格式混杂的业务场景，无需额外清洗补全完整会话，直接基于该框架做OPE，节省数据预处理成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高风险RL场景下新策略上线前仅靠OPE点估计不足以支撑安全决策，现有方法依赖完整会话数据，鲁棒性、有限样本有效性不足，缺乏可靠的不确定性量化能力。
### 方法关键点
面向有限时域非齐次MDP，提出模型驱动Bootstrap框架：不依赖完整episode重采样，从估计的MDP中再生轨迹，可适配完整轨迹、单步转移观测、轨迹碎片等多类离线数据格式，提升有限样本统计效率。
### 关键结果
理论上证明了bootstrap分布一致性、置信区间渐近有效、目标策略价值方差估计一致；仿真实验显示，多数场景下可精准捕捉OPE估计量的采样分布，输出更紧的置信区间、更准确的方差估计结果。

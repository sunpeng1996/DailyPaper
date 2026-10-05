---
title: When May a Bandit Leave Its Anchor? E-Process-Authorized Thompson Sampling
  under Non-stationarity
title_zh: 非平稳环境下基于E过程授权的自适应汤普森采样算法
authors:
- Mayand Gulati
- Kerong Wang
- WeiChen Au
affiliations:
- UC Santa Barbara
- Purdue University
arxiv_id: '2610.03646'
url: https://arxiv.org/abs/2610.03646
pdf_url: https://arxiv.org/pdf/2610.03646
published: '2026-10-02'
collected: '2026-10-05'
category: RecSys
direction: 推荐系统在线学习 · 非平稳多臂老虎机
tags:
- Thompson Sampling
- Non-stationary Bandit
- E-process
- Online Learning
- A-B Testing
one_liner: 提出e-ATS自适应汤普森采样，用随时有效E过程管控非平稳老虎机的全历史锚点退出时机
practical_value: '- 电商动态场景（大促、季节更替）下的多臂老虎机选品/排序策略，可引入E过程授权机制管控历史数据遗忘时机，避免非平稳分布下历史数据误导，控制策略切换的假阳率

  - 做在线自适应策略时，可参考「锚点策略+授权触发+动态加权」的三段式架构，未触发变化检测时严格沿用高置信的静态最优策略，触发后平滑切换到折扣历史的策略，降低策略波动带来的业务损失

  - 非平稳环境的算法效果评估不要只看单一数据集，要同时覆盖构造的动态测试集和真实业务回放数据集，避免优化方向和实际业务收益背离'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
非平稳场景下多臂老虎机的全历史学习易被过时数据误导，现有固定折扣/滑动窗口的遗忘策略无严格统计边界，盲目切换策略会带来不必要的regret损失。
### 方法关键点
每个臂同时维护全历史Beta状态（锚点策略OTS）和折扣历史Beta状态；引入随时有效E过程作为变化检测器，仅当E过程超过阈值时才授权启用折扣状态，用可逆相关性分数控制折扣状态的权重，未授权时完全沿用OTS策略，无需人工拟合阈值。
### 关键结果
Beta-Bernoulli平稳假设下，e-ATS误退出OTS策略的概率不超过预设的α_E；对比无授权基线，注册测试集上平均归一化动态伪regret降低38.4%，文献回放集上regret升高7.5%，授权机制收益高度依赖场景非平稳特性。

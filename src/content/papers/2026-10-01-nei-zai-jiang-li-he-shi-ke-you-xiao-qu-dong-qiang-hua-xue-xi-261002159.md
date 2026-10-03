---
title: When Do Intrinsic Rewards Lead to Exploration?
title_zh: 内在奖励何时可有效驱动强化学习Agent探索
authors:
- Scott W. Viteri
- Laura Gomezjurado Gonzalez
- Clark Barrett
affiliations:
- Stanford University
arxiv_id: '2610.02159'
url: https://arxiv.org/abs/2610.02159
pdf_url: https://arxiv.org/pdf/2610.02159
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: Agent 强化学习探索机制优化
tags:
- Intrinsic Reward
- Reinforcement Learning
- Exploration
- Counterfactual Inference
- RL Agent
one_liner: 提出反事实信息探索评估标准，揭示现有内在奖励失效条件与优化方向
practical_value: '- 设计推荐冷启动、广告投放的探索策略时，不能仅追求单维度内在reward（如新奇度、预测误差），需额外引入反事实信息增益作为评估指标，避免陷入局部次优探索

  - 构建RL驱动的导购Agent、智能投放Agent的探索模块时，可参考文中四类主流内在reward的失效条件，提前加入边界约束规避无效探索

  - 业务场景需低成本最优探索策略时，可复用文中基于反事实信息匹配度的探索优先级排序逻辑，降低线上试错成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有强化学习内在 reward 仅基于智能体实际交互经验赋值，最大化这类 reward 不一定能获取最高信息量的探索结果，行业缺乏统一的探索效果度量标准。
### 方法关键点
1. 提出基于反事实信息获取量的探索正式评估准则，通过对比不同策略采集的历史数据对其他备选策略的经验替代效果，衡量策略探索效率；
2. 构造极简验证环境，验证count-based、prediction-error、empowerment、information-gain四类主流内在reward的最优策略，在反事实信息获取维度均存在帕累托次优问题；
3. 明确现有内在reward可实现最优探索的前置条件，同时构造新的优化目标，当探索效果满足评估标准时自动分配更高reward。
### 关键结果
在构造的标准测试环境中，四类主流内在reward的最优策略均存在探索失效问题，符合推导的失效条件场景下，新优化目标可实现探索效果与奖励赋值的严格对齐，无额外计算开销。

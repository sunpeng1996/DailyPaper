---
title: Analytic Planning under Uncertainty with Moment Closure
title_zh: 基于矩闭合的不确定环境下解析规划方法
authors:
- Shishir Sharma
- Doina Precup
affiliations:
- McGill University
- Mila – Quebec Artificial Intelligence Institute
arxiv_id: '2608.02519'
url: https://arxiv.org/abs/2608.02519
pdf_url: https://arxiv.org/pdf/2608.02519
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 不确定环境下规划优化
tags:
- Reinforcement Learning
- Model-based RL
- Planning under Uncertainty
- Moment Closure
- Distribution-aware Learning
one_liner: 提出转移分布与价值函数兼容性原则，实现无采样低方差的分布感知强化学习规划
practical_value: '- 电商搜索推荐的动态规划场景（如多步流量分配、促销ROI预估）可借鉴兼容性原则，用解析矩计算替代采样，降低预估方差

  - 不确定环境下的Agent决策（如智能选品、动态定价的多步序列优化）可复用高斯转移+径向基价值函数的闭式解结构，减少采样开销

  - 推荐系统不确定性校准场景可参考该方法的矩传播思路，提升冷启动、新流量场景下的预估置信度校准效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
基于模型的强化学习在随机环境中规划存在两难：全分布解析传播依赖严苛的策略/奖励结构难以泛化，随机采样会引入高额目标方差，确定性点估计则完全忽略预测协方差，无法有效校准不确定性。
### 方法关键点
1. 采用二次动作值参数化，将Bellman备份简化为仅针对状态值函数的期望运算；
2. 提出预测转移分布与价值函数类的兼容性原则，满足约束时期望可通过分布的矩直接解析计算；
3. 基于高斯转移模型+径向基价值函数实例化该原则，得到同时传播预测均值和协方差的闭式备份，无需采样。
### 关键结果
连续控制任务下目标方差较基线显著降低，随机观测场景下预测不确定性校准效果大幅提升，为分布模型规划提供了可落地的理论框架。

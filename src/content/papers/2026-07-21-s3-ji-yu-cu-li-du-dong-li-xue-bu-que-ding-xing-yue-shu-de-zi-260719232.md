---
title: 'S3: Stable Subgoal Selection by Constraining Uncertainty of Coarse Dynamics
  in Hierarchical Reinforcement Learning'
title_zh: S3：基于粗粒度动力学不确定性约束的分层RL稳定子目标选择方法
authors:
- Kshitij Kumar Srivastava
- Kshitij Jerath
affiliations:
- University of Massachusetts, Lowell
arxiv_id: '2607.19232'
url: https://arxiv.org/abs/2607.19232
pdf_url: https://arxiv.org/pdf/2607.19232
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: 分层强化学习 · 子目标选择优化
tags:
- Hierarchical RL
- Subgoal Selection
- Intrinsic Reward
- Mixture Density Network
- Uncertainty Estimation
one_liner: 提出基于粗粒度动力学不确定性约束的S3方法，优化分层RL高层子目标选择，提升长周期任务性能
practical_value: '- 电商长周期决策场景（如大促用户全路径留存优化、多节点 campaign 规划）可复用分层RL+粗粒度动力学建模思路，缓解高层策略反馈稀疏问题

  - 分层Agent架构的高层子目标选择模块可引入MDN建模的预测不确定性作为内在奖励，降低无效子目标占比，提升策略稳定性

  - 非平稳业务场景（如流量波动下的广告投放、大促实时流量调度）可借鉴风险规避的子目标筛选逻辑，降低策略波动带来的业务损失'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
分层强化学习（HRL）在长周期复杂任务上表现优于平层RL，但高层Agent面临环境反馈稀疏、延迟问题，性能高度依赖下层执行能力，子目标选择缺乏有效引导。
### 方法关键点
1. 采用高层Agent时间尺度下多步环境转移聚合得到的粗粒度动力学，规避原始转移动力学对状态-动作空间高覆盖度的要求；
2. 用混合密度网络（MDN）拟合粗粒度动力学的预测不确定性，以最小化该不确定性作为内在奖励引导高层策略学习；
3. 实现风险规避的子目标筛选，稳定高层策略输出。
### 关键结果
在非平稳长周期环境中，性能全面超越现有SOTA HRL方法。

---
title: Explore Beyond the Boundary Using Entropic Information
title_zh: 基于熵信息的强化学习边界外探索方法
authors:
- Bumgeun Park
- Donghwan Lee
affiliations:
- Korea Advanced Institute of Science and Technology
arxiv_id: '2607.29419'
url: https://arxiv.org/abs/2607.29419
pdf_url: https://arxiv.org/pdf/2607.29419
published: '2026-07-31'
collected: '2026-08-04'
category: Agent
direction: 强化学习Agent稀疏奖励场景探索优化
tags:
- Reinforcement Learning
- Exploration
- Intrinsic Reward
- Entropy
- Sparse Reward
one_liner: ENTINEX方法基于熵信息识别状态分布边界分配内在奖励，解决稀疏延迟奖励下的Agent探索问题
practical_value: '- 推荐系统冷启动场景可借鉴ENTINEX思路，给未探索的用户/物品特征空间边界分配虚拟奖励，引导策略快速覆盖小众长尾需求

  - 多轮对话导购Agent决策模块可复用熵信息识别状态边界的逻辑，降低稀疏转化信号下的探索效率损耗

  - 广告投放出价/定向策略优化中，可将内在奖励与业务外显奖励结合，提升冷启动阶段的跑量效率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
强化学习在稀疏、延迟奖励场景下反馈不足，传统奖励工程高度依赖领域知识、泛化性差，现有计数类内在奖励方法难以适配连续状态空间，探索效率低下。
### 方法关键点
1. ENTINEX探索框架基于熵信息精准识别状态分布的边界区域
2. 给边界区域的状态访问分配专属内在奖励，激励Agent突破已有分布边界探索未覆盖空间，无需手动设计领域相关奖励规则
### 关键结果
在多类稀疏、延迟奖励的测试环境中，探索表现一致优于现有基线方法，无额外领域知识依赖的前提下实现探索效率显著提升

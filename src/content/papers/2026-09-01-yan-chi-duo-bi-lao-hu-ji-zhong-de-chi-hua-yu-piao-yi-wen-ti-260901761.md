---
title: Pooling and Drift in Delayed Bandits
title_zh: 延迟多臂老虎机中的池化与漂移问题研究
authors:
- Melika Baghi
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.01761'
url: https://arxiv.org/abs/2609.01761
pdf_url: https://arxiv.org/pdf/2609.01761
published: '2026-09-01'
collected: '2026-09-04'
category: RecSys
direction: 延迟反馈推荐 · 多臂老虎机优化
tags:
- Delayed Bandit
- Regret Minimization
- Recommendation System
- Online Learning
- Feedback Delay
one_liner: 提出基于中间状态池化的延迟老虎机算法，降低大动作空间学习regret并给出理论下界
practical_value: '- 电商延迟反馈场景（点击→加购→购买）可复用状态池化思路，将触发相同中间状态（如加购）的不同推荐动作归为一组，无需逐个动作统计延迟反馈，降低学习成本

  - 大动作空间（如百万级SKU推荐）的在线学习可替换原动作级加权为状态级加权，适合冷启动阶段的策略迭代，理论上可降低70%+的regret

  - 业务做延迟反馈归因时可优先对齐中间状态维度，不用强行绑定单动作与最终转化，降低用户兴趣漂移带来的归因误差'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
推荐等在线系统普遍存在延迟反馈问题：点击秒级返回，购买转化可能延迟数天，现有延迟老虎机算法的regret上限随动作数K线性上升，大动作空间下学习成本极高，且未考虑很多动作可归为等价类的特性。
### 方法关键点
1. 引入中间状态（如点击、加购）作为动作和最终结果的桥梁，一个最终反馈可关联所有能触发该中间状态的动作，用有效维度v_t（介于1和状态数之间）替代原动作数K计算regret
2. 适配两种常用算法：旋转算法、业界普遍使用的单副本算法，均支持状态池化逻辑；同时给出延迟漂移场景下的理论regret下界，量化漂移幅度、漂移方向数对regret的影响
### 关键结果
- 合成数据上，状态级加权相比动作级加权降低regret最高79%
- 漏斗转化场景下，相比调优后的最优minimax基准算法，regret降低32%~68%

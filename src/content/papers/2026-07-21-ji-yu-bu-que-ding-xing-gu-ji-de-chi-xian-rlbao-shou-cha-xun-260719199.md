---
title: Conservative Query and Adaptive Regularization for Offline RL Under Uncertainty
  Estimation
title_zh: 基于不确定性估计的离线RL保守查询与自适应正则化方法
authors:
- Li-Rong Zhou
- Qin-Wen Luo
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
arxiv_id: '2607.19199'
url: https://arxiv.org/abs/2607.19199
pdf_url: https://arxiv.org/pdf/2607.19199
published: '2026-07-21'
collected: '2026-07-23'
category: Agent
direction: 离线强化学习 · 偏好查询与正则化优化
tags:
- Offline RL
- Uncertainty Estimation
- Conservative Query
- Adaptive Regularization
- CQL
one_liner: 基于不确定性估计优化离线RL偏好查询与利用，在D4RL基准任务上取得领先或可比性能
practical_value: '- 电商推荐/广告排序场景落地离线RL策略时，可复用Morse网络做动作不确定性估计，规避OOD动作导致的策略更新抖动问题

  - 引入专家反馈优化RL策略时，可参考保守查询机制优先选择接近历史分布的高价值动作咨询，降低专家标注成本同时保障收敛稳定性

  - 策略优化阶段可复用不确定性感知自适应正则，替代固定权重的正则项，根据动作置信度动态调整约束强度，提升策略收敛效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离线RL从静态数据集学习策略的效果受数据集覆盖度限制，现有基于专家动作偏好查询的优化方案仅按策略动作与数据集动作的距离选查询对象，搭配固定约束对齐偏好，易导致策略更新不稳定，也难以和值正则方法兼容。

### 方法关键点
1. 引入Morse网络量化策略动作相对于离线数据集的不确定性；
2. 设计不确定性驱动的保守查询策略，仅选择靠近数据集分布的动作请求专家反馈，保障贝尔曼更新稳定性；
3. 提出不确定性感知的自适应正则方案，根据动作不确定性动态调整策略优化的数据级约束强度，可直接集成到CQL等主流离线RL框架。

### 关键结果
在D4RL基准的全品类任务上测试，性能优于或持平现有SOTA离线RL方法。

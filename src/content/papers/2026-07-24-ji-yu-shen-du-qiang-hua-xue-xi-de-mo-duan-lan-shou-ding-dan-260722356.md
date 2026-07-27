---
title: Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement
  Learning
title_zh: 基于深度强化学习的末端揽收订单派单与路径集成优化框架
authors:
- Yida Xu
- Zhaofang Mao
- Yuheng Miao
- Jiaxin Zhang
- Yiting Sun
affiliations:
- 天津大学管理与经济学部
- 天津大学复杂管理系统计算与分析实验室(CACMS)
arxiv_id: '2607.22356'
url: https://arxiv.org/abs/2607.22356
pdf_url: https://arxiv.org/pdf/2607.22356
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 末端物流调度 · 深度强化学习优化
tags:
- Deep-Reinforcement-Learning
- Graph-Attention-Network
- Last-Mile-Logistics
- Order-Dispatching
- Vehicle-Routing
one_liner: 提出耦合学习型路径预言机与实时派单启发式的集成框架，解决末端揽收派单与路径协同优化难题
practical_value: '- 处理强耦合多子问题优化时，可复用「学习型预言机+实时启发式」架构，既保留优化效果又满足线上低延迟要求

  - 路径规划类问题可参考Dynamic-Residual GAT编码器+个性化前瞻解码器结构，适配骑手/配送员的个性化特征

  - 大规模调度场景可借鉴「预言机生成候选集+局部搜索调优」的两阶段策略，平衡优化效果与算力开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
末端揽收场景中派单、路径规划两个决策环节强耦合，分开求解会忽略二者的依赖关系，端到端学习在大规模可变实例上存在奖励稀疏、不稳定、计算成本高的问题。

### 方法关键点
1. 采用集成优化框架，耦合学习型路由预言机与实时派单启发式算法；2. 路径子问题使用Dynamic-Residual GAT编码器+骑手个性化前瞻解码器结构；3. 派单子问题由路由预言机输出近优解筛选候选骑手，结合局部搜索保证实时可扩展性。

### 关键结果数字
在菜鸟物流真实数据集的离线评估与在线滚动仿真中，方案在解质量与求解速度上均优于所有基准，可支撑实时大规模末端揽收决策。

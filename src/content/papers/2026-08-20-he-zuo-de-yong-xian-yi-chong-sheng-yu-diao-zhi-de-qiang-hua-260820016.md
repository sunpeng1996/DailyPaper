---
title: 'Emergence of cooperation: A reputation-modulated reinforcement learning'
title_zh: 合作的涌现：一种声誉调制的强化学习方法
authors:
- Chenyang Zhao
- Jiqiang Zhang
- Li Chen
- Yong Zou
affiliations:
- 华东师范大学物理学院
- 宁夏大学物理学院
- 陕西师范大学物理与信息技术学院
arxiv_id: '2608.20016'
url: https://arxiv.org/abs/2608.20016
pdf_url: https://arxiv.org/pdf/2608.20016
published: '2026-08-20'
collected: '2026-08-23'
category: MultiAgent
direction: 多智能体协作 · 声誉驱动演化
tags:
- MultiAgent
- Q-Learning
- ReinforcementLearning
- ReputationMechanism
- CooperationEvolution
one_liner: 提出融合局部声誉度量的Q-learning多智能体框架，揭示声誉驱动合作涌现的相变机制
practical_value: '- 多智能体协作场景（如多渠道广告投放调度、供应链协同）可将局部声誉作为Q-learning的输入特征，提升整体协作效率

  - 平台生态治理（如商家管控、UGC激励）可参考声誉作为信息输入的机制，替代单纯收益奖惩，降低运营管控成本

  - 多智能体系统稳定性调优可借鉴相变观测方法，定位策略调整临界阈值，避免系统从良性状态突变为崩溃状态'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有博弈论模型大多将声誉作为调节收益、交互结构的外部因子，忽略其作为信息输入影响个体决策判断的核心作用，无法准确解释真实社会场景下的合作涌现规律。
### 方法关键点
1. 基于空间囚徒困境博弈框架，为智能体装备Q-learning能力，定义局部声誉度量融合个体交互经验与周边社会信息指导决策
2. 仿真模拟不同背叛诱惑收益下的多智能体策略演化过程
### 关键结果
1. 声誉调制的学习机制可大幅提升合作行为涌现概率
2. 随背叛诱惑提升，系统会从全合作到全背叛发生不连续相变
3. 合作通过合作簇成核扩散，合作簇瓦解则会导致系统进入完全背叛的吸收态

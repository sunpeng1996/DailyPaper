---
title: 'Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon
  World-Model Failure'
title_zh: 世界模型长 horizon 推演失效诊断：仅拟合运动学而非动力学
authors:
- Finn Rasmus Schäfer
- Korbinian Moller
- Yuan Gao
- Christian Oefinger
- Sebastian Schmidt
- Johannes Betz
affiliations:
- Technical University of Munich
- Autonomous Vehicle Systems Lab
- Data Analytics and Machine Learning Group
arxiv_id: '2607.05966'
url: https://arxiv.org/abs/2607.05966
pdf_url: https://arxiv.org/pdf/2607.05966
published: '2026-07-06'
collected: '2026-07-11'
category: Agent
direction: Agent 世界模型长序列推演故障诊断
tags:
- World Model
- Long-Horizon Reasoning
- Embodied Agent
- Diagnostic Metric
- iKCE
one_liner: 提出iKCE诊断指标，揭示世界模型长horizon推演失效本质是仅拟合运动学未建模动力学
practical_value: '- 做长序列规划类Agent（如广告预算规划、用户长期兴趣演化模拟）的世界模型时，可引入iKCE类分层误差诊断，避免笼统将长序列失效归因为累积误差

  - 训练世界模型时，可针对性加入动力学/因果约束损失，而非仅拟合运动学轨迹特征，提升长horizon推演鲁棒性

  - 跨域泛化类世界模型任务（如不同客群兴趣推演），可借鉴扰动测试协议，验证模型是否学到核心规则而非表层分布'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
世界模型长horizon推演失效传统上被笼统归因为累积误差，无法明确误差类型，难以针对性优化模型，现有故障归因框架颗粒度过粗。
### 方法关键点
引入经典力学运动学/动力学二分框架，提出逐步诊断指标**iKCE（想象运动学一致性误差）**衡量推演和运动学先验的偏差，搭配扰动协议测试物理条件跨边界时iKCE的响应情况，区分模型是学到表层运动学特征还是底层动力学规则。
### 关键结果
- DMC walker-walk任务训练的DreamerV3上，模型推演iKCE比真实物理推演高约2个数量级
- 跨越步态崩溃边界的摩擦系数扫描实验中，策略奖励显著下降的同时模型iKCE无统计层面变化，验证了模型仅拟合运动学特征的本质

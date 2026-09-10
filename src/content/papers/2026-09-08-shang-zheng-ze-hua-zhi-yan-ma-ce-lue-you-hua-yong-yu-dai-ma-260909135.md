---
title: Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement
  Learning in Code Generation
title_zh: 熵正则化秩掩码策略优化用于代码生成的测试时强化学习
authors:
- Jiacheng Xu
- Feng Chen
- Xiuneng Xu
- Bo An
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2609.09135'
url: https://arxiv.org/abs/2609.09135
pdf_url: https://arxiv.org/pdf/2609.09135
published: '2026-09-08'
collected: '2026-09-10'
category: Training
direction: LLM训练 · 测试时强化学习优化
tags:
- Reinforcement Learning
- Test-Time Adaptation
- Code Generation
- Policy Optimization
- LLM Training
one_liner: 提出探针驱动测试时RL框架与ERPO算法，解决代码生成无标注测试时适配问题
practical_value: '- 针对无法通过表层形式匹配判优的生成任务（如推荐文案、Agent工具调用代码），可借鉴探针共识奖励（PCR）思路构造无标注训练信号，无需人工标注即可实现在线适配

  - ERPO的秩掩码+熵正则化策略可直接复用在推荐系统在线RL调优场景，避免奖励hack导致的策略漂移，提升低置信度负样本更新的保守性

  - 测试时RL的适配思路可迁移到电商大促等短时域流量突变场景，用实时无标注数据快速微调LLM驱动的推荐/Agent模块，降低推理延迟的同时提升效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有测试时强化学习（TTRL）依赖答案表层投票获得奖励信号，无法适配代码生成任务：不同代码实现表层差异大但功能可能一致，无法直接通过文本匹配得到有效训练信号，且现有伪奖励机制易出现奖励黑客问题。

### 方法关键点
1. 探针驱动TTRL框架：基于问题描述生成无输出探针输入，执行候选代码得到行为一致性结果，构造探针共识奖励（PCR），完全避开表层匹配的限制
2. 熵正则化秩掩码策略优化（ERPO）：通过秩掩码将低PCR样本转为保守负更新，用熵上限控制策略漂移，解决伪奖励不可靠的问题

### 关键结果
在主流代码生成基准上，域内适配、零样本迁移两种场景下的pass@1、pass@k指标均获得显著提升

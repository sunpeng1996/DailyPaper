---
title: 'METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning'
title_zh: 面向元强化学习的记忆增强测试时自适应框架METTA
authors:
- Ali Najar
- Hosein Hasani
- Amir Kooshan Fattah
- Yasamin Rajabi
- Mahdieh Soleymani Baghshah
affiliations:
- Sharif University of Technology
arxiv_id: '2610.31656'
url: https://arxiv.org/abs/2610.31656
pdf_url: https://arxiv.org/pdf/2610.31656
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: 元强化学习 · 长上下文自适应Agent
tags:
- Meta-RL
- Test-Time Adaptation
- Neural Memory
- Long Context
- Agent
one_liner: 提出双时间尺度记忆架构的元强化学习方法，兼顾长上下文效率与跨任务泛化
practical_value: '- 双时间尺度记忆设计可直接复用在电商用户行为建模场景：单会话细粒度行为用线性复杂度记忆模块处理，跨会话偏好用摘要聚合，避免Transformer二次方计算开销，适配高并发线上推理

  - 测试时记忆更新思路可迁移到冷启动场景：新用户/新物品场景下无需重新训练全局模型，仅在线更新记忆模块即可快速适配偏好，大幅降低冷启动成本

  - 稀疏奖励下的探索优化方法可复用在广告投放Agent：低转化稀疏反馈场景中，记忆模块留存历史探索有效信息，减少重复试错，提升投放ROI'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
元强化学习（Meta-RL）需要基于长交互历史快速适配未知任务，但传统循环模型压缩经验会丢失关键细粒度信息，Transformer类方法又受限于二次方计算与存储成本，难以落地长horizon、稀疏反馈的工业场景。

### 方法关键点
- 双时间尺度记忆架构：将快速适配拆分为两个层级，会话内用Test-Time Training（TTT）神经记忆模块做细粒度自适应，仅需线性序列复杂度；跨会话用episode级摘要聚合，支持长程跨任务推理无需遍历全量交互历史
- 跨会话聚合支持两种可选实现：轻量指数移动平均（EMA）适配低算力边缘场景，注意力检索适配需要精准回溯历史的场景，两种都可端到端训练
- 适配Meta-RL的PPO训练优化：按会话顺序处理轨迹片段，避免随机采样轨迹重复重构前缀的冗余计算，训练效率提升近1倍

### 关键实验
覆盖MuJoCo运动控制、Meta-World机械臂操作、稀疏奖励PointMaze导航三类基准，对比RL2、PEARL、TrMRL、ECET等主流Meta-RL基线：未见过的Meta-World ML10/45测试集上成功率超50%，比基线最高领先40个百分点；稀疏奖励PointMaze任务上探索覆盖率比Transformer基线高39%，到达目标步数少48%，无重复探索行为；训练GPU耗时仅为Transformer类基线的1/3，同时保持线性推理复杂度。

### 核心结论
工业级长上下文智能体不需要依赖全量注意力，通过分层记忆+测试时自适应即可同时兼顾效率、效果与OOD泛化能力。

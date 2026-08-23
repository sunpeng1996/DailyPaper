---
title: 'RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement
  Learning in Robotic Manipulation'
title_zh: RoMAN-Flow：面向机器人操作离线强化学习的自回归归一化流优化框架
authors:
- Shaoxuan Wang
- Guangting Zheng
- Rui Huang
- Zhipeng Tang
- Sha Zhang
- Jiajun Deng
- Yanyong Zhang
affiliations:
- University of Science and Technology of China
- The Chinese University of Hong Kong
arxiv_id: '2608.20208'
url: https://arxiv.org/abs/2608.20208
pdf_url: https://arxiv.org/pdf/2608.20208
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 离线强化学习 · 机器人策略优化
tags:
- Offline-RL
- Autoregressive-Normalizing-Flow
- Robotic-Manipulation
- Knowledge-Distillation
- Latency-Optimization
one_liner: 解决自回归归一化流采样瓶颈，实现低延迟高性能的机器人操作离线RL框架
practical_value: '- 生成式推荐/广告文案生成等自回归模型训练场景，可借鉴无采样的加权似然目标，规避自回归采样开销，显著提升训练效率

  - 对精度要求高但线上延迟约束严格的生成类任务，可复用「先训练高精度自回归模型再蒸馏为单步生成器」的范式，平衡效果与推理速度

  - Agent策略离线微调场景，可复用该框架的似然驱动优化思路，无需环境交互即可完成策略迭代，降低业务试错成本'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
离线强化学习可基于历史数据完成机器人策略优化无需环境交互，但主流扩散/流匹配策略无易处理的似然，限制了似然驱动的后训练效果；自回归归一化流（AR-NFs）虽同时具备强动作建模能力和精确似然计算能力，但串行采样开销大，无法直接用于训练和线上部署。
### 方法关键点
1. 训练阶段采用无采样的优势加权似然目标，直接对离线数据集内的高优势动作分配更高似然权重，无需从AR策略采样即可完成优化，消除训练侧采样开销；
2. 部署阶段将训练好的AR策略蒸馏为单步动作生成器，实现低延迟推理。
### 关键结果
在多模拟操作基准、真实机器人平台上，策略性能与现有SOTA方案持平，推理延迟较原生AR-NF方案大幅降低。

---
title: 'PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene
  Memory and Fine-Grained Motion Control'
title_zh: PhysStream：带结构化场景内存与细粒度运动控制的流式物理视频生成
authors:
- Chuhao Chen
- Peter Wonka
- Chaoyang Wang
- Chen Wang
- Qiao Feng
- Sergey Tulyakov
- Lingjie Liu
affiliations:
- University of Pennsylvania
- Snap Inc.
- KAUST
arxiv_id: '2609.17521'
url: https://arxiv.org/abs/2609.17521
pdf_url: https://arxiv.org/pdf/2609.17521
published: '2026-09-14'
collected: '2026-09-17'
category: Other
direction: 可控视频生成 · 物理驱动
tags:
- Video Generation
- Controllable Generation
- Autoregressive Model
- Scene Memory
- Physics-grounded Generation
one_liner: 提出带结构化场景内存的自回归物理驱动视频生成框架，支持生成中细粒度交互式运动控制
practical_value: '- 电商短视频生成场景可复用结构化场景内存设计，基于已生成帧在线提取物体跟踪/位置映射，提升生成内容物理一致性，避免穿模等问题

  - 互动广告/虚拟展示场景可参考稀疏速度增量控制机制，支持用户在生成过程中动态调整物体运动，降低交互控制门槛

  - 两阶段训练范式可迁移至时序生成类任务：先微调带控制条件的双向模型，再训练带记忆模块的因果自回归模型，兼顾控制精度与时序一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有可控视频生成方法要么需提前预设完整控制序列，要么仅基于像素级位置信号控制，无法支撑物理动态层面的生成中交互式细粒度控制。

### 方法关键点
提出PhysStream自回归物理驱动图生视频模型：
1. 加入结构化场景内存，在线从已生成帧提取位置映射、物体跟踪映射；
2. 通过编码物理量的稀疏速度增量信号实现细粒度运动控制，让模型学习底层动力学；
3. 两阶段训练：先微调带运动控制条件的双向模型，再训练加入结构化场景内存的因果自回归模型，提升物理一致性。

### 关键结果
在合成基准上，相比最优基线运动分布距离（FVMD）降低33%，轨迹误差降低12%；真实场景人类评估中85%以上的案例更受偏好。

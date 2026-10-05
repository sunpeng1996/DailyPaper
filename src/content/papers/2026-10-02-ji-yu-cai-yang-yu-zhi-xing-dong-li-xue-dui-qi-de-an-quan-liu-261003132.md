---
title: Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics
title_zh: 基于采样与执行动力学对齐的安全流式流规划方法
authors:
- Seunghwan Jang
- Jeongyong Yang
- Siddharth Ancha
- SooJean Han
affiliations:
- Nanyang Technological University
- University of Washington
- University of California, Berkeley
- KAIST
arxiv_id: '2610.03132'
url: https://arxiv.org/abs/2610.03132
pdf_url: https://arxiv.org/pdf/2610.03132
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 安全轨迹规划 · 流匹配
tags:
- Flow Matching
- Safe Planning
- Trajectory Generation
- Agent Planning
- Streaming Inference
one_liner: 提出对齐采样与执行动力学的流式流规划器，兼顾低延迟、高安全性与目标达成率
practical_value: '- 生成式序列推理可借鉴流式逐步生成+仅当前执行步加约束的思路，大幅降低实时推荐/广告投放序列规划的 latency，适配高吞吐线上场景

  - 采样动力学与执行动力学对齐的思路可复用解决推荐系统「离线训练-线上推理」分布偏移问题，例如LLM4Rec的采样逻辑要对齐线上真实展示逻辑

  - 全序列约束改为仅执行步校验的trick，可迁移到电商推荐/广告的合规校验场景，在满足内容/投放合规要求的同时降低计算开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于扩散/流匹配的生成式Agent规划器采用全轨迹一次性生成、逐中间状态扰动加安全约束的方案，不仅计算开销高无法适配高实时性部署要求，还因学习到的采样动力学与实际执行动力学不一致存在严重分布偏移，导致线上效果劣化。
### 方法关键点
提出SafeStreamingFlow目标条件规划器，通过将学习到的状态向量场与分层状态预测逐步融合，实现流采样动力学与执行动力学的精准对齐；仅对当前需要执行的步骤采用高阶控制屏障函数做安全约束校验，无需对全轨迹做约束校正。
### 关键结果
在导航、竞速、运动三类基准测试中，相比现有方法规划延迟大幅降低、安全表现显著提升，同时目标达成率保持SOTA级竞争力。

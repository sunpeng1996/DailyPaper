---
title: 'DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation
  in Few-Step Video World Models'
title_zh: DyMD：少步视频世界模型中基于分布匹配蒸馏的交互动态保留方法
authors:
- Haojun Xu
- Jie Huang
- Xin Lu
- Mingchen Zhong
- Zihao Fan
- Linjiang Huang
- Si Liu
affiliations:
- Beihang University
- JD Future Academy
arxiv_id: '2609.31349'
url: https://arxiv.org/abs/2609.31349
pdf_url: https://arxiv.org/pdf/2609.31349
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 视频世界模型 · 分布匹配蒸馏
tags:
- Diffusion Model
- Knowledge Distillation
- World Model
- Video Generation
- Embodied Agent
one_liner: 提出动态适配的分布匹配蒸馏框架DyMD，降低视频世界模型推理成本同时保留交互动态
practical_value: '- 大模型蒸馏时可借鉴动态重加权策略，对强交互/动态类困难样本提升损失权重，兼顾生成质量与动态一致性

  - 少步生成蒸馏的时间步自适应调度方法，可迁移到文生图/文生视频业务的轻量化推理优化，降低线上延迟

  - 交互动态定向蒸馏优化思路，可用于电商3D商品展示、虚拟试穿试戴等动态内容生成的小模型落地'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
大体积视频扩散模型多步采样推理成本高，难以支撑交互式下游任务；现有DMD少步生成蒸馏方法仅能保留视觉质量，会严重抑制机器人-物体等交互动态，核心是弱重噪导致教师后验集中在缺运动的生成序列，强运动样本拟合误差大阻碍动态学习。
### 方法关键点
1. 设计时间亲和性条件重噪采样，混合基础调度与基于局部后验变化的教师先验，适配每个生成序列的交互保真度，平衡运动恢复与外观优化
2. 引入动态引导的伪分数跟踪，用噪声条件预测器估计样本拟合难度，在判别器损失中对强运动困难样本加权
### 关键结果
将14B教师模型蒸馏为4步推理无辅助模块的1.3B学生模型，R-Bench任务依从性较基准DMD提升9.6个百分点，PAI-Bench-G领域得分提升5.1分，作为下游规划backbone在WorldArena任务上平均成功率从16%升至34%，视觉质量与基准持平

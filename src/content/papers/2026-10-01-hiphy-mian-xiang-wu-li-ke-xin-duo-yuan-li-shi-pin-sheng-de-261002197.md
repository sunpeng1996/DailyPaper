---
title: 'HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video
  Generation'
title_zh: HiPhy：面向物理可信多原理视频生成的层级对齐方法
authors:
- Tahira Kazimi
- Shubhankar Borse
- Munawar Hayat
- Fatih Porikli
- Pinar Yanardag
affiliations:
- Virginia Tech
- Qualcomm AI Research
arxiv_id: '2610.02197'
url: https://arxiv.org/abs/2610.02197
pdf_url: https://arxiv.org/pdf/2610.02197
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 多物理原理视频生成 · 层级RL优化
tags:
- Video Generation
- Reinforcement Learning
- Hierarchical Reward
- Physical Alignment
- Benchmark
one_liner: 提出层级物理对齐RL框架，解决多物理原理共存场景视频生成的合理性问题
practical_value: '- 多约束生成任务可复用分层对齐奖励设计：局部单独校验每个约束（如营销规则、合规要求、商品属性）的合理性，全局校验整体一致性，适配电商商品短视频、广告文案生成场景

  - 多规则共存的生成场景可借鉴独立子流跟踪机制：每个规则对应独立学习流，避免多规则间的互斥抵消，解决多要求叠加下生成效果骤降的问题

  - 业务效果评测可参考专项Benchmark构建思路：针对高频难点场景构造定向评测集，精准度量优化收益，避免通用评测覆盖度不足的问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频生成模型视觉保真度较高，但普遍无法遵循物理定律，在多物理原理共存的真实场景下易出现规则冲突、物理效果遗漏等问题，现有方法仅支持单原理单视频生成，无法适配复杂场景需求。
### 方法关键点
1. 提出HiPhy层级物理对齐RL框架，采用双层优化目标：局部层面单独约束每个物理原理的时序动态合理性，全局层面保障全场景物理与语义一致性
2. 构建含50K条prompt的多物理原理数据集，开源MultiPhyBench评测基准，覆盖多类共存物理事件场景
### 关键结果
在多类基准上物理常识、语义对齐效果显著优于现有基线，在多物理原理并发场景下收益最高，解决了现有方法在该场景下性能骤降的痛点

---
title: 'PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon
  Objectives'
title_zh: PlayWorld：基于智能体玩家的长序列目标世界模型评测基准
authors:
- Kaixin Ding
- Xi Chen
- Minghong Cai
- Zhiyuan Xu
- Yiyang Wang
- Yuxiang Lu
- Junyi Li
- Shuyang Chen
- Yuan Gao
- Xin Tao
affiliations:
- The University of Hong Kong
- Kling Team, Kuaishou Technology
- The Chinese University of Hong Kong
- Zhejiang University
arxiv_id: '2608.13552'
url: https://arxiv.org/abs/2608.13552
pdf_url: https://arxiv.org/pdf/2608.13552
published: '2026-08-12'
collected: '2026-08-14'
category: Eval
direction: 世界模型评测 · 多模态Agent交互
tags:
- World Model
- Benchmark
- Multi-modal Agent
- Long-horizon
- Interactive Evaluation
one_liner: 提出含171个场景的PlayWorld基准，通过多模态Agent Player交互评测世界模型长时序性能
practical_value: '- 电商3D逛店、数字人导购、虚拟试穿等交互生成场景的评测，可复用「目标驱动Agent替代固定动作序列」的范式，解决不同模型动作逻辑差异导致的横向对比难问题

  - 长时序交互系统的评测维度可参考本文分层设计：基础能力（质量/可控性）+ 核心维度（一致性/保真度/状态演化），全面覆盖用户核心感知点

  - 搭建电商类世界模型业务时，可优先攻坚几何一致性、非视野内状态持久化两大现有SOTA模型普遍存在的短板，快速提升用户体验'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型多采用固定动作序列做评测，但不同模型达成同一长时序目标的动作路径差异极大，固定动作的评测方案无法实现跨模型公平对比。
### 方法关键点
提出PlayWorld基准，内置171个带明确长时序目标的场景，采用多模态Agent Player与世界模型动态交互完成目标；从4个核心维度（几何一致性、交互保真度、非视野内演化、内在演化）+ 基础能力（视频质量、可控性）综合评估模型性能。
### 关键结果
对9个SOTA世界模型的评测显示，现有模型在长时序交互目标下表现普遍不可靠，其中空间一致性、持久化状态演化两类任务的缺陷最为突出。

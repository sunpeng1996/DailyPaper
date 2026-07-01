---
title: 'MemLearner: Learning to Query Context memory for Video World Models'
title_zh: MemLearner：面向视频世界模型的上下文记忆查询学习方法
authors:
- Jiwen Yu
- Jianxiong Gao
- Jianhong Bai
- Yiran Qin
- Kaiyi Huang
- Quande Liu
- Xintao Wang
- Pengfei Wan
- Kun Gai
- Xihui Liu
affiliations:
- The University of Hong Kong
- Fudan University
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2606.31734'
url: https://arxiv.org/abs/2606.31734
pdf_url: https://arxiv.org/pdf/2606.31734
published: '2026-06-29'
collected: '2026-07-01'
category: Multimodal
direction: 视频世界模型 · 长视频生成记忆优化
tags:
- VideoWorldModel
- ContextMemory
- LongVideoGeneration
- DiffusionModel
- SceneConsistency
one_liner: 提出学习式自适应上下文查询机制，解决视频世界模型长时生成场景不一致问题
practical_value: '- 电商动态营销素材、商品展示长视频生成业务可复用学习式上下文查询机制，替代传统规则检索方案，大幅提升长视频内容一致性

  - 多模态生成任务可借鉴混合训练策略，同时利用低成本标注合成数据、无标注真实数据，在不提升标注成本的前提下优化模型效果

  - 复用预训练模型能力实现新增功能的设计思路可迁移，无需额外引入独立模块，降低模型部署的计算与存储开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频世界模型长时生成存在严重的场景一致性退化问题，此前基于规则的上下文帧检索记忆方案，在存在遮挡、动态物体的场景下泛化能力不足，无法支撑长时序视频生成需求。

### 方法关键点
1. 设计MemLearner学习式自适应上下文查询方法，用query token桥接上下文与预测token，实现动态上下文召回；
2. 直接复用预训练视频生成模型的视觉先验完成查询逻辑，无需从零训练额外模块，配套优化了训练、推理效率；
3. 构建带相机位姿标注的遮挡/动态物体长视频数据集，采用标注渲染数据+无标注真实数据混合的多数据集训练策略。

### 关键结果
在遮挡、动态物体等复杂场景下，场景一致性与记忆能力显著优于现有SOTA视频世界模型。

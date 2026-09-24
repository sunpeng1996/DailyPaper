---
title: The Capability Manifold and ML Scaling Laws
title_zh: 能力流形与机器学习缩放定律
authors:
- Syed Ali Raza Zaidi
- Maryam Hafeez
affiliations:
- SPRINT Lab, University of Leeds
arxiv_id: '2609.27588'
url: https://arxiv.org/abs/2609.27588
pdf_url: https://arxiv.org/pdf/2609.27588
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: ML缩放定律 · 全生命周期资源能力映射
tags:
- Scaling-Laws
- Capability-Manifold
- LLM-Training
- Agent-Capability
- Resource-Optimization
one_liner: 提出多维能力流形框架，统一关联ML全生命周期资源与下游推理、规划等多维度能力
practical_value: '- Agent/LLM4Rec业务选型时可参考该框架，不止看预训练Loss，而是对齐推理/规划/检索等下游核心能力的资源投入配比，避免盲目堆参

  - 业务迭代时可复用雅可比灵敏度分析方法，量化预训练/微调/测试时计算资源调整对业务效果的边际收益，优化ROI

  - 多阶段资源分配优化时，可将Chinchilla等现有缩放定律作为流形上的已知轨迹，快速定位当前业务阶段的最优资源投入方案'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ML缩放定律仅将预测损失与计算、参数量、数据三类资源关联，但当前模型多通过Agent框架部署，相同损失的模型在推理、检索、规划、适配等下游能力上差异极大，缺乏统一框架关联全生命周期耦合资源与多维度能力。
### 方法关键点
提出多维能力流形框架，通过有界缩放函数将下游能力映射到预训练、训练后、测试时三个阶段的资源投入；引入解析雅可比矩阵量化不同能力对资源变化、资源间交互的灵敏度，可兼容现有各类缩放定律。
### 关键结果
成功将Kaplan型、Chinchilla型缩放定律及测试时计算规律嵌入该框架，证明现有不同场景的缩放关系可统一表示为通用能力流形上的轨迹，实现多维度能力-资源关系的统一建模。

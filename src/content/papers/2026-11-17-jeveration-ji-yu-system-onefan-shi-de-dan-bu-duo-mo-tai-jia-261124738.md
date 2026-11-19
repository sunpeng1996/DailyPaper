---
title: 'Jeveration: System One Models Now Generate'
title_zh: Jeveration：基于System One范式的单步多模态生成框架
authors:
- Yuhe Liu
- Qi Li
- Shihua Zhang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.24738'
url: https://arxiv.org/abs/2611.24738
pdf_url: https://arxiv.org/pdf/2611.24738
published: '2026-11-17'
collected: '2026-11-19'
category: Multimodal
direction: 多模态生成 · 单步并行推理
tags:
- Multimodal Generation
- Fast Inference
- Unified Model
- Text-to-Image
- Single Forward Pass
one_liner: 基于冻结多模态基座实现单步前向多任务生成，速度较现有统一模型最高提升122倍
practical_value: '- 全局共享随机态约束并行预测的方法，可迁移到生成式推荐的全序列一致性生成场景，大幅降低多token生成的KV cache开销

  - 冻结基座复用语义知识+轻量离散分布引导的训练范式，可用于低资源下多任务统一生成模型的快速迭代，适配电商商品文案/主图生成的多业务需求

  - 单checkpoint支持多任务单步推理的架构设计，可落地到推荐系统的实时内容生成链路，显著降低端到端推理延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态生成模型依赖多步迭代推理，延迟高难以适配实时业务场景，System One类快速并行决策模型此前未被拓展至生成任务。
### 方法关键点
1. 基于冻结视觉语言基座复用已有视觉语义知识，大幅降低训练成本；
2. 引入全局共享随机态约束所有位置的并行预测，解决单步生成的全局一致性问题；
3. 预学习离散图像码分布引导生成过程，避免模型忽略随机态约束；
4. 同一架构适配文生图、图生图、密集预测三类任务，单checkpoint支持全链路能力。
### 关键结果
单H200显卡上生成512×512图像仅需78ms，较现有统一模型最高提速122倍，图像质量与密集预测性能达到行业可比水平。

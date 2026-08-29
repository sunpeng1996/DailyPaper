---
title: Task-disentangled Low-Rank Adaptation for Versatile Audio-visual Multi-modal
  Learning Tasks within a Unified Framework
title_zh: 面向统一多模态视听学习框架的任务解耦低秩适配方法
authors:
- Hanyu Xuan
- Mengqi Zhang
- Junjun Mao
- Fei Wang
- Kun Li
- Guanghui Yue
- Zhiliang Wu
- Hehe Fan
arxiv_id: '2608.24209'
url: https://arxiv.org/abs/2608.24209
pdf_url: https://arxiv.org/pdf/2608.24209
published: '2026-08-25'
collected: '2026-08-29'
category: Multimodal
direction: 多模态学习 · 任务解耦LoRA
tags:
- LoRA
- Multi-modal Learning
- Multi-task Training
- Low-Rank Adaptation
- Audio-visual Learning
one_liner: 设计任务解耦LoRA机制实现多视听任务统一训练，效果优于现有统一及部分单任务模型
practical_value: '- 多目标训练场景（如推荐点击/转化/加购多任务）可复用任务解耦LoRA结构：拆分通用低秩矩阵+任务特定调制矩阵+跨任务专家，解决多任务互扰问题，提升整体效果

  - 电商跨模态（图文/音视频）多任务统一训练（如短视频分类/标签生成/召回预训练）可参考该架构，降低多任务重复开发成本

  - 大模型跨模态多任务微调时，用该改进LoRA替代普通LoRA，可在不增加过多算力开销的前提下，提升多任务整体表现'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视听多模态学习普遍采用单任务独立训练模式，与人类统一感知认知能力存在显著差距；朴素多任务联合训练受复杂任务间关系影响，容易出现任务互扰，效果下降。
### 方法关键点
基于LLM的强表征与泛化能力，设计任务解耦LoRA机制：包含3个核心组件，分别是任务通用低秩矩阵（捕获通用跨模态知识）、任务特定调制矩阵（解耦各任务独有模式）、跨任务协作专家（挖掘任务间固有相关性），从模型、任务两层实现显式协作。
### 关键结果
在多个视听多模态任务上表现超越现有统一架构视听模型，部分任务效果优于绝大多数定制化单任务模型

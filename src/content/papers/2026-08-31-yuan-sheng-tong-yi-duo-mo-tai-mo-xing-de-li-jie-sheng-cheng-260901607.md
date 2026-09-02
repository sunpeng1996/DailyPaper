---
title: 'Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models:
  From Representation, Task to System'
title_zh: 原生统一多模态模型的理解-生成协同机制研究：从表征、任务到系统
authors:
- Penghao Wu
- Haiwen Diao
- Weichen Fan
- Lewei Lu
- Dahua Lin
- Ziwei Liu
affiliations:
- S-Lab, Nanyang Technological University
- SenseTime Research
arxiv_id: '2609.01607'
url: https://arxiv.org/abs/2609.01607
pdf_url: https://arxiv.org/pdf/2609.01607
published: '2026-08-31'
collected: '2026-09-02'
category: Multimodal
direction: 统一多模态模型 · 理解生成协同优化
tags:
- Multimodal-LLM
- Unified-Model
- Vision-Language
- Task-Decoupling
- End-to-End-Optimization
one_liner: 从表征、任务、系统三层揭示统一多模态模型理解与生成的协同规律及优化方案
practical_value: '- 做包含商品图理解+定制化物料生成的多模态生成式推荐场景时，采用任务解耦架构：冲突的视觉计算分支单独优化，仅保留上层语义交互，可避免单任务性能退化

  - 跨模态商品召回、商品文案生成等依赖共享商品语义知识的多任务场景，可复用同一个统一多模态底座，双向正向迁移可同时提升两类任务效果

  - 搭建需要同时处理用户上传图像理解、定制化内容生成的电商Agent时，优先选型端到端统一多模态模型，性能优于 planner-executor 拼接管线'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
统一多模态模型（UMM）可同时实现视觉理解与生成，但功能统一不代表学习协同，两类目标可能互相增益、竞争容量或仅独立共存，现有研究缺乏对其协同机制的系统级拆解。
### 方法关键点
在无预训练视觉先验的原生受控环境下，从三层开展验证：
1. 表征层：对比共享计算路径、任务解耦架构（冲突视觉计算分支专用，保留语义交互层）的性能差异
2. 任务层：通过三类案例验证任务知识重叠度对双向迁移效果的影响
3. 系统层：对比端到端UMM与planner-executor拼接管线在复杂多步任务的表现
### 关键结果
- 理解与生成目标可互相提供有效训练信号：生成丰富理解任务的视觉特征，理解强化生成任务的多模态对齐能力
- 任务解耦架构可完全规避共享计算路径下的单任务主导、非对称性能退化问题
- 依赖共享知识的理解、生成任务可实现双向正向迁移；端到端UMM在同时需要两类能力的复杂任务上性能显著优于拼接管线

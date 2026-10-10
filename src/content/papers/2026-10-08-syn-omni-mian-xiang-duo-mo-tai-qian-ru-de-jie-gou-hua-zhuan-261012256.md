---
title: 'Syn-Omni: Structured Specialization and Progressive Collaboration for Omnimodal
  Embeddings'
title_zh: Syn-Omni：面向多模态嵌入的结构化专用与渐进式协作框架
authors:
- Youngtaek Oh
- Qiyu Wu
- Hiromi Wakaki
- Junmo Kim
- Yuki Mitsufuji
affiliations:
- KAIST
- Sony Group Corporation
arxiv_id: '2610.12256'
url: https://arxiv.org/abs/2610.12256
pdf_url: https://arxiv.org/pdf/2610.12256
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态表征 · 结构化适配优化
tags:
- Omnimodal Embedding
- LoRA
- Cross-modal Routing
- Multimodal Adaptation
one_liner: 提出带正交模态专家LoRA与渐进协同路由的多模态嵌入框架，跨81个任务优于基线
practical_value: '- 多模态召回/检索场景可复用OME-LoRA参数拆分思路：用共享LoRA学通用语义、模态专属LoRA学图文/短视频/音频等模态特有特征，大幅降低适配成本

  - 跨模态特征融合可借鉴PSR渐进路由策略：先固化单模态表征再做跨模态协同，避免模态噪声干扰，提升多模态搜索/推荐的召回准确率

  - 多模态大模型业务适配可直接复用该轻量微调方案：仅更新LoRA参数无需全量微调，快速落地多模态表征能力'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多模态嵌入方法依赖单一共享参数空间，无法有效分离通用语义与模态专属特征，表征性能受限，跨模态融合易受噪声干扰。
### 方法关键点
1. 设计Orthogonal Modality-Expert LoRA（OME-LoRA），将适配拆分为共享LoRA路径学习通用语义、模态专属LoRA路径学习各模态特有特征，两组参数正交避免相互干扰；
2. 提出Progressive Synergy Routing（PSR），先让各模态专家独立学习模态先验，再逐步开启跨模态交互实现协同，降低模态噪声影响。
### 关键结果
在覆盖图像、视频、音频、音视频的81个任务上全面优于基线，整体Hit@1提升1.7pp，音视频模态Hit@1提升3pp

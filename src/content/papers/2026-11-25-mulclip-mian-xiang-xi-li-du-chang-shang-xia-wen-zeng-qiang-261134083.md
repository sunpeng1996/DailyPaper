---
title: 'MulCLIP: A Multi-level Alignment Framework for Enhancing Fine-grained Long-context
  CLIP'
title_zh: MulCLIP：面向细粒度长上下文增强的多层次对齐CLIP框架
authors:
- Chau Truong
- Hieu Ta Quang
- Zhenzhen Liu
- Dung D. Le
affiliations:
- Vinmotion
- VinUniversity
- Cornell University
arxiv_id: '2611.34083'
url: https://arxiv.org/abs/2611.34083
pdf_url: https://arxiv.org/pdf/2611.34083
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态预训练 · 图文细粒度对齐
tags:
- CLIP
- Multimodal Alignment
- Long-context
- Fine-grained Matching
- Vision-Language
one_liner: 无需区域候选的端到端多层次对齐CLIP框架，提升长文本细粒度图文匹配性能
practical_value: '- 电商商品图与长详情/属性描述的对齐训练可复用三层对齐目标，无需额外标注视觉区域，大幅降低训练标注成本

  - 跨模态商品搜索召回场景可直接替换原CLIP backbone，长文本query匹配精度提升无需修改推理部署架构

  - 多粒度对齐信号的兼容设计思路可复用在其他多模态预训练任务，避免堆叠优化目标带来的信号冲突'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有CLIP基于短字幕训练，对长文本细粒度匹配效果差；基于区域候选的改进方案推理部署成本高，难以落地工业场景。

### 方法关键点
提出端到端多层次对齐框架MulCLIP，无需区域候选，利用三层兼容训练信号对齐不同文本粒度：1）全局对比对齐适配长字幕与短摘要；2）Word-Patch Reconstruction校准局部特征，捕捉样本内词与图像块的语义对应；3）Subcaption-Aggregated Patch对齐实现上下文丰富的子字幕grounding。

### 关键结果
在不同字幕长度的基准测试集上均获得稳定精度提升，消融实验验证三个对齐目标互补，可共同提升框架整体性能。

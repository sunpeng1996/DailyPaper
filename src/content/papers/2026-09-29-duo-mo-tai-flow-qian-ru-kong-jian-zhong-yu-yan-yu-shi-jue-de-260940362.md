---
title: 'Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding
  Spaces'
title_zh: 多模态Flow：嵌入空间中语言与视觉的统一流建模
authors:
- Hongyuan Tao
- Xinggang Wang
- Lianghui Zhu
- Yongkang Li
- Yunchao Wei
- Bin Feng
- Shaoyu Chen
- Qian Zhang
- Chang Huang
- Kai Yu
affiliations:
- Huazhong University of Science and Technology
- Beijing Jiaotong University
- Horizon Robotics
arxiv_id: '2609.40362'
url: https://arxiv.org/abs/2609.40362
pdf_url: https://arxiv.org/pdf/2609.40362
published: '2026-09-29'
collected: '2026-10-03'
category: Multimodal
direction: 多模态统一生成 · 连续流建模
tags:
- Multimodal Generative Model
- Flow Matching
- Vision-Language Pretraining
- Continuous Embedding
- Unified Architecture
one_liner: 提出全连续统一多模态生成架构Multimodal Flow，同等参数数据预算下性能优于现有离散/混合模型
practical_value: '- 可复用文本+图像统一连续超块建模方法，优化电商多模态召回/排序的跨模态特征对齐效率，避免量化瓶颈

  - 训练多块并行预测、推理块级顺序生成的范式，可迁移至多模态商品文案/配图生成场景，降低推理延迟

  - 同等参数数据下连续流模型性能优于离散方案，可作为多模态生成式推荐底座的备选架构'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态模型要么将语言与量化图像都建模为离散token，存在视觉量化瓶颈；要么混合离散语言预测+连续图像生成，需模态专属目标与采样流程，全连续统一多模态建模相关研究尚少。

### 方法关键点
1. 提出统一连续架构，将文本块、图像组织为有序连续超块，保留文本顺序与视觉空间结构；
2. 基于Flow Matching在超块上学习统一向量场，用联合注意力实现跨模态交互，搭配模态专属FFN处理单模态特征；
3. 训练阶段并行预测多目标块，推理阶段顺序生成超块，兼顾训练效率与生成可控性。

### 关键结果
仅用150B预训练token，1.6B参数的MF-1在GenEval+DPG-Bench平均得分82.8，VQAv2+MMBench+POPE平均得分75.3，同等数据、优化、参数预算下性能优于主流离散/混合多模态模型。

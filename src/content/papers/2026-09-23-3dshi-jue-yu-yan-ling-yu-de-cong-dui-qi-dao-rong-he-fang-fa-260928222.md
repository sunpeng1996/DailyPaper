---
title: From Alignment to Fusion in 3D Vision-Language
title_zh: 3D视觉-语言领域的从对齐到融合方法研究
authors:
- Xueqi Qiu
- Xingyu Miao
- Jingjing Deng
- Haoran Duan
- Yang Long
- Ling Shao
arxiv_id: '2609.28222'
url: https://arxiv.org/abs/2609.28222
pdf_url: https://arxiv.org/pdf/2609.28222
published: '2026-09-23'
collected: '2026-09-24'
category: Multimodal
direction: 3D多模态学习 · 跨模态对齐融合
tags:
- 3D-Vision-Language
- Multimodal-Alignment
- Multimodal-Fusion
- Orthogonal-Transformation
- Prompt-Guided-Decoder
one_liner: 提出先对齐后融合的3D视觉-语言框架，通过正交约束保几何结构实现多任务性能提升
practical_value: '- 多模态特征融合前先做两两cosine对齐，可迁移到商品图文/3D模型的多模态表征对齐场景，减少特征差异

  - 融合前采用特殊正交群约束的可学习映射变换特征，可在不破坏原始表征内在几何结构的前提下做适配，适合多源异构特征融合场景

  - 用prompt引导的query decoder提取任务条件特征，可复用在多任务统一的多模态理解系统中减少重复开发'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D视觉-语言系统独立处理点云、体素网格、多视图图像三类异构表征，直接融合存在特征差异大、无约束适配易破坏原始几何结构的问题，限制多任务性能。
### 方法关键点
1. 先执行三重两两cosine对齐，建立三类表征的片段级对应关系；
2. 采用prompt引导的query decoder检索任务相关特征，融合前对各表征特定query特征做特殊正交群约束的可学习映射，保留内积与欧氏距离避免几何失真；
3. 基于下游任务监督执行自适应特征融合。
### 关键结果
在8个数据集上验证，对比基线PQ3D：ScanNet200数据集AP提升3.2个点；ScanRefer/Nr3D/Sr3D/Multi3DRefer数据集grounding精度分别提升2.9/10.6/4.6/4.1个点；3D问答、密集字幕等任务性能均有稳定提升。

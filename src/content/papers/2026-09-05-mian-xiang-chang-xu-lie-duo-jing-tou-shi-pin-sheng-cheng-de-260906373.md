---
title: Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation
title_zh: 面向长序列多镜头视频生成的多网格后训练方法
authors:
- Jiawei Mao
- Haoqin Tu
- Hardy Chen
- Yuhan Wang
- Keyang Xu
- Jieru Mei
- Hongliang Fei
- Ruogu Fang
- Wei Shao
- Cihang Xie
affiliations:
- UC Santa Cruz
- University of Florida
- Vanderbilt University
- Google
arxiv_id: '2609.06373'
url: https://arxiv.org/abs/2609.06373
pdf_url: https://arxiv.org/pdf/2609.06373
published: '2026-09-05'
collected: '2026-09-10'
category: Multimodal
direction: 多模态 · 长视频生成优化
tags:
- VideoGeneration
- MultiGridTraining
- LongFormContent
- PostTraining
- Multimodal
one_liner: 提出多网格后训练范式MovieGrid，大幅提升长多镜头视频帧内/跨帧生成一致性
practical_value: '- 多网格分块联合建模思路可迁移到长序列用户行为建模、长文案/多片段短视频串生成场景，解决单时序轴长序列信息衰减问题

  - Noise-Free Random-Grid Training的干净上下文注入技巧，可复用在RAG长上下文生成、多模态内容一致性生成任务，提升全局连贯性

  - Grid Embedding+Grid Boundary Loss的结构约束方法，可用于电商商品展示短视频生成、推荐feed多内容块混排的风格一致性管控'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有长多镜头视频生成方案沿单时序轴打包全叙事内容，偏好连续运动但难以兼顾多镜头完整性与跨镜头叙事一致性。
### 方法关键点
1. 提出MovieGrid多网格后训练范式，将长视频拆解为时序有序短块，排列在空间网格联合建模，减少单时序轴处理的镜头数同时支持块间全局信息交互
2. 构建含54K配对角色感知story prompt的MGLV长视频数据集
3. 采用Noise-Free Random-Grid Training保留部分块作为干净上下文指导去噪，配合Grid Embedding、Grid Boundary Loss优化生成一致性
### 关键结果
相同token预算下，生成1616帧视频的镜头数是Temporal Packing方案的6.05倍；跨5类真实场景基准，intra-shot一致性达0.9131（优于SOTA HoloCine的0.8086），inter-shot一致性达0.5914（优于SOTA StoryMem的0.5384），可扩容视频长度且性能损失极小

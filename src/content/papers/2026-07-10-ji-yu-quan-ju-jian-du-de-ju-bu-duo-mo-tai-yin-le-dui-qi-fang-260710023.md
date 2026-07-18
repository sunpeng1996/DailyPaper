---
title: Local Multimodal Music Alignment from Global Supervision
title_zh: 基于全局监督的局部多模态音乐对齐方法
authors:
- Irmak Bukey
- Zachary Novack
- Jongmin Jung
- Dasaem Jeong
- Chris Donahue
affiliations:
- Carnegie Mellon University
- University of California San Diego
- Neutune
- Sogang University
arxiv_id: '2607.10023'
url: https://arxiv.org/abs/2607.10023
pdf_url: https://arxiv.org/pdf/2607.10023
published: '2026-07-10'
collected: '2026-07-18'
category: Multimodal
direction: 多模态理解 · 弱监督局部对齐
tags:
- Multimodal Alignment
- Contrastive Learning
- Weak Supervision
- Sinkhorn Distance
- Cross-Modal Retrieval
one_liner: 提出仅需全局监督的FuSiLi相似性度量，实现多模态音乐局部对齐且保留全局对比能力
practical_value: '- 弱监督局部对齐思路可直接复用在电商多模态内容匹配场景，比如商品视频片段和详情页图文的对应关系挖掘，仅需全局配对标注即可落地，大幅降低细粒度标注成本

  - FuSiLi基于Sinkhorn的软对齐对比损失可嵌入现有多模态召回/排序模型，在不损失全局检索效果的前提下，提升细粒度内容匹配精度

  - 全局+局部混合相似性的微调范式可迁移到通用图文/音视频多模态表征学习任务，适配预训练大模型的下游适配需求'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态理解任务（如音频与乐谱匹配）依赖细粒度局部对应关系，但逐帧/逐块的局部标注成本极高，工业界通常仅能获取粗粒度的全局配对监督信号，现有对比学习方法难以兼顾全局对齐能力和局部匹配精度。
### 方法关键点
1. 提出FuSiLi（Fused Sinkhorn-Localized Similarity）相似性度量，基于Sinkhorn软对齐直接计算局部特征（图像块、音频帧）的相似度，适配多模态对比学习流程
2. 设计混合对比学习目标，将FuSiLi局部相似性与传统全局相似性结合，仅需全局配对监督即可微调CLIP、CLAP等预训练多模态编码器
### 关键结果
在跨模态检索、帧级对齐任务上对比现有全局/局部基线，局部对齐效果最优，同时全局检索性能保持竞争力，无明显下降

---
title: 'Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative
  Transformers'
title_zh: 面向像素空间生成Transformer的角色耦合分词方法SpecSlot
authors:
- Jiongfan Yang
- Weichen Fan
- Haiwen Diao
- Zhongang Cai
- Ziwei Liu
affiliations:
- Peking University
- Nanyang Technological University
- SenseTime
arxiv_id: '2610.40647'
url: https://arxiv.org/abs/2610.40647
pdf_url: https://arxiv.org/pdf/2610.40647
published: '2026-10-28'
collected: '2026-10-31'
category: Multimodal
direction: 多模态生成 · 像素空间Transformer优化
tags:
- Generative Transformer
- Image Generation
- Tokenization
- Attention Routing
- DCT
- Efficient Computing
one_liner: 通过DCT频带拆分与注意力路由结合，降本同时提升像素空间生成Transformer效果
practical_value: '- 推荐系统长用户行为序列建模可借鉴频带拆分思路：高频低价值行为做局部交互、低频高价值行为做全局交互，大幅降低全局Attention算力开销

  - 多模态/生成式推荐的Token路由可参考「按信息重要性分配计算资源」的逻辑，降低冗余计算的同时保留核心信息的交互能力

  - 电商商品图、营销文案等AIGC场景可直接复用该算力优化方案，在不提升推理成本前提下提升生成内容的细节丰富度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
像素空间生成Transformer默认每个图像patch对应1个Token，提升生成细节需要增加Token数量，导致全局Attention算力成本指数级上升，且此前方案未利用不同频率信息的交互特性差异。

### 方法关键点
1. 提出SpecSlot整流流Transformer架构，将输出细节与全局注意力序列长度完全解耦
2. 每个空间锚点扩展为多个Slot，分别对应互不重叠的DCT系数频带，仅最低频Slot参与全局注意力，其余Slot仅做局部交互，无需扩大全局序列长度即可提升频谱细节
3. 新增空间头对频谱预测做局部校正，生成状态、目标、损失仍保留在像素空间，无需额外预训练自编码器

### 关键结果数字
- ImageNet-256上与同FLOPs的JiT基线FID相当，收敛速度更快
- ImageNet-512上FID比基线优2.84，FLOPs降低3.9%；仅比JiT-B/16 FID高0.69的同时成本低38.2%
- 文本生成图像任务DPG-Bench得分比JiT-B/8高1.06，推理成本低40.6%

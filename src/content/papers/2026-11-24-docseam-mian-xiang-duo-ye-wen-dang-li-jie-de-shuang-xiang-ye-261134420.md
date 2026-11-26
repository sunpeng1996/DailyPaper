---
title: 'DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding'
title_zh: DocSEAM：面向多页文档理解的双向跨页编码
authors:
- Hoang-Nhat Nguyen
- Chen Change Loy
affiliations:
- S-Lab, Nanyang Technological University
- Synvo AI
arxiv_id: '2611.34420'
url: https://arxiv.org/abs/2611.34420
pdf_url: https://arxiv.org/pdf/2611.34420
published: '2026-11-24'
collected: '2026-11-26'
category: Multimodal
direction: 多模态文档理解 · 跨页上下文融合
tags:
- Multimodal VLM
- Cross-Page Encoding
- Document Understanding
- VQA
- Lightweight Module
one_liner: 提出轻量跨页编码模块DocSEAM，解决多页文档VLM单页编码的特征断层问题
practical_value: '- 处理多页商品说明书/多页用户评价等图文混合长内容时，可复用DocSEAM的邻页三元组融合思路，在不改动现有视觉编码器、LLM主干结构的前提下插入轻量模块，提升跨页内容理解精度

  - 跨上下文特征融合场景可借鉴「中心锚定掩码注意力+方向显著性门控」设计，仅输出中心页增强特征，不增加下游模型token输入长度，规避序列过长带来的性能损失

  - 针对分块截断的长序列内容理解任务，可复用「局部邻块融合预热+模块冻结微调」的训练流程，在低算力成本下提升长内容的边界感知能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多页文档VLM默认单页独立编码，导致页边界存在特征断层，跨页段落、连续表格等内容的理解误差大，后续LLM补全上下文的推理成本高。

### 方法关键点
1. 在预训练视觉编码器与LLM之间插入轻量模块DocSEAM，无需改动原有主干结构；
2. 对每一页取前后相邻页组成局部三元组，采用中心锚定掩码自注意力+方向显著性门控融合邻页信息，仅输出增强后的中心页token，不改变原有token数量；
3. 训练流程为跨页监督预热后，冻结DocSEAM做下游多页任务微调。

### 关键结果
9B参数模型在5个多页文档VQA基准上，成为10B参数以内开源模型的SOTA；可降低分页位置敏感度，跨页内容定位精度显著提升。

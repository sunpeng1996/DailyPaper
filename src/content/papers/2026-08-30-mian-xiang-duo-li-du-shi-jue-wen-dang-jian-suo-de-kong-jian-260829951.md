---
title: Spatial Matryoshka Training for Multi-Granularity Visual Document Retrieval
title_zh: 面向多粒度视觉文档检索的空间套娃训练方法
authors:
- Trishan Singha Roy
- Arkadeep Acharya
- Vishwajeet Kumar
- Jaydeep Sen
- Sachindra Joshi
affiliations:
- IIT Delhi
- IBM
arxiv_id: '2608.29951'
url: https://arxiv.org/abs/2608.29951
pdf_url: https://arxiv.org/pdf/2608.29951
published: '2026-08-30'
collected: '2026-09-02'
category: Multimodal
direction: 多模态视觉文档检索 · 嵌套压缩训练优化
tags:
- Visual Document Retrieval
- Late-interaction Retriever
- Embedding Compression
- Multi-granularity Retrieval
- Lightweight Fine-tuning
one_liner: 提出ColSNAP空间嵌套平均池化训练法，单模型支持多压缩等级视觉文档检索，可灵活调节精度存储权衡
practical_value: '- 电商商品图文详情页检索、商家素材库、广告创意库检索场景，可直接复用ColSNAP嵌套池化训练思路，无需修改模型架构即可灵活适配不同存储预算的检索需求

  - 针对多模态召回embedding存储成本高的痛点，可套用单编码生成多粒度embedding的方案，索引阶段按需选择压缩等级，平衡召回精度与存储、查询耗时

  - 已上线的预训练多模态召回模型可通过轻量适配阶段接入ColSNAP，无需全量重训，落地成本低，适合快速迭代的业务场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
多模态late-interaction检索器基于分patch embedding做token级匹配，在视觉文档检索任务上精度表现优异，但patch级embedding存储成本极高；现有压缩方法在索引阶段固定单一压缩等级，无法灵活适配不同存储预算的业务需求。
### 方法关键点
提出ColSNAP空间嵌套平均池化训练范式，对backbone输出的patch网格做分层空间池化，生成由细到粗的多层嵌套embedding，所有层级同步训练，无需修改原有模型架构；单次编码即可生成全部压缩等级的embedding，精度-存储权衡可在索引阶段动态配置，无需在训练阶段固定。
### 关键结果
大幅压缩下仍保持接近全分辨率的检索性能，可无缝适配多种late-interaction backbone，仅需对预训练检索器做轻量适配即可获得绝大多数性能收益。

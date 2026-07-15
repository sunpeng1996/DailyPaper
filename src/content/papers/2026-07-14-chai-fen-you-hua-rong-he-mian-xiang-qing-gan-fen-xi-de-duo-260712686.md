---
title: 'Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment
  Analysis'
title_zh: 《拆分-优化-融合：面向情感分析的多模态融合解耦方案》
authors:
- Alexios Filippakopoulos
- Elias Kallioras
- Nikolaos Xiros
- Efthymios Georgiou
- Alexandros Potamianos
arxiv_id: '2607.12686'
url: https://arxiv.org/abs/2607.12686
pdf_url: https://arxiv.org/pdf/2607.12686
published: '2026-07-14'
collected: '2026-07-15'
category: Multimodal
direction: 多模态融合 · 情感分析
tags:
- Multimodal Fusion
- Sentiment Analysis
- Cross-modal Interaction
- Unimodal Representation
- SeRIn
one_liner: 提出分离单模态优化与跨模态交互的SeRIn多模态融合方案，在情感分析基准达SOTA
practical_value: '- 多模态特征融合可复用该解耦架构：电商商品/内容的图文评论多模态特征融合时，先单独优化各模态表征再做跨模态交互，避免单模态有效信息被污染

  - 延迟全量跨模态交互到预测层的设计，可大幅降低多模态召回/排序模块的推理开销，适合高QPS生产环境落地

  - 自发模态重加权特性可直接复用在模态缺失场景（如商品缺详情图、用户评价不足），无需额外标注即可适配'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多模态融合方法将单模态信号优化、跨模态交互两个存在竞争关系的目标耦合在同一操作中，容易导致单模态有效信息被污染，两类目标的优化相互干扰。

### 方法关键点
SeRIn为多模态大模型融合范式，从架构先验层面强制两类目标分离：设置三条独立通路，一是多条单模态专属通路，各自基于对应编码器上下文优化模态独有表征，互不干扰；二是专用跨模态通路，累积多模态联合演化信息，不反向污染单模态流；三是全量跨模态交互延迟到最终预测阶段才执行。

### 关键结果
在CH-SIMS、CMU-MOSEI两个多模态情感分析基准上达到SOTA，所有指标均实现提升；消融实验证明性能增益来自结构化交互而非参数量增加，在视觉模态损坏场景下可自发实现模态重加权，无需显式监督。

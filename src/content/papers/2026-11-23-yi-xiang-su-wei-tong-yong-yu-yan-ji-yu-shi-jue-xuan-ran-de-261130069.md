---
title: 'Pixel as the Common Language: Unified Multimodal Embedding via Visual Rendering'
title_zh: 《以像素为通用语言：基于视觉渲染的统一多模态嵌入方法》
authors:
- Xu Yuan
- Pangjing Wu
- Wenqi Fan
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.30069'
url: https://arxiv.org/abs/2611.30069
pdf_url: https://arxiv.org/pdf/2611.30069
published: '2026-11-23'
collected: '2026-11-24'
category: Multimodal
direction: 多模态嵌入 · 统一视觉编码
tags:
- Multimodal Embedding
- VLM
- Cross-Modal Retrieval
- Visual Rendering
- Representation Learning
one_liner: 将异构多模态输入转为统一视觉基底用VLM编码，实现更优的多模态检索性能与跨域泛化能力
practical_value: '- 多模态召回场景可复用「异构输入先统一转视觉基底再编码」的思路，统一文本、商品图、图文详情页的编码通路，减少多模态分支维护成本

  - 跨域检索任务可借鉴干预式渲染学习方案，通过语义、渲染双维度扰动训练，提升嵌入向量在不同场景下的稳定性，降低域适配成本

  - 多模态RAG场景可直接引入RenderEmbed预训练模型做向量召回，相比同规模SOTA在跨域任务上Precision@1有2.1个点的增益'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多模态嵌入模型对纯文本、纯图像、组合输入采用不同编码通路，异构任务无法共享端到端编码流程，跨输入配置的监督迁移效率低，限制模型泛化能力。
### 方法关键点
1. 提出RenderEmbed框架，编码前先通过视觉基底渲染将所有异构输入转为统一的视觉格式，复用单个VLM完成全类型输入编码
2. 采用分层渐进锚点编码，通过可学习锚点跨层融合视觉token特征，同时保留全局上下文与细粒度特征，生成紧凑检索向量
3. 引入干预式渲染学习，通过语义干预、渲染扰动互补训练，保证向量对内容变化敏感、对渲染差异稳定
### 关键结果
- 同参数规模下优于现有SOTA，MMEB数据集整体Precision@1比MetaEmbed高1.7个点
- 跨域任务上Precision@1增益达2.1个点，跨域泛化能力显著更优

---
title: 'Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence'
title_zh: Pix2Evidence：支持文本与视觉证据的多模态RAG系统
authors:
- Ziniu Liu
- Xiaoyang Chen
- Dezhi Ye
- Jie Liu
- Jin Ma
- Hao Deng
affiliations:
- 同济大学
- 腾讯元宝
arxiv_id: '2610.41335'
url: https://arxiv.org/abs/2610.41335
pdf_url: https://arxiv.org/pdf/2610.41335
published: '2026-10-30'
collected: '2026-11-02'
category: RAG
direction: 多模态RAG · 图文融合证据检索
tags:
- Multimodal RAG
- Visual Retrieval
- Contrastive Learning
- LoRA
- Evidence Alignment
one_liner: 提出融合图文编码+证据引导训练的多模态RAG，在多类QA基准上显著优于PixelRAG
practical_value: '- 电商商品详情页/活动页多模态检索可复用该方案：先对页面截图切片做OCR转录，联合图文编码构建索引，同时保留布局和文本信息，提升检索准确率

  - 训练阶段可引入大模型教师生成查询关联的证据描述，通过KL对齐损失让检索器更聚焦能支撑答案的关键片段，而非仅语义相关内容，可迁移到搜推召回排序优化

  - 工程上可对视觉输入做适度下采样（比如c=2时分辨率减半），实测精度损失极小，能显著降低存储和计算开销，适合大规模多模态知识库落地

  - 双检索分支融合场景下，RRF/z-score归一化融合效果优于直接取最高分，可复用在图文多路召回的结果融合环节'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有富视觉文档RAG存在两类缺陷：截图检索保留了页面布局、图像信息但文本语义匹配能力弱，纯文本检索丢失了视觉、结构信息；且常规相关性检索仅匹配语义，无法区分语义相关但不包含答案证据的片段，导致多模态问答准确率低。
### 方法关键点
- 数据层：对所有截图切片做OCR转录并缓存，训练阶段用大模型教师生成每个正样本切片对应的查询关联证据描述，作为监督信号
- 检索层：基于多模态Embedding模型用LoRA微调共享编码器，将查询、切片+转录文本映射到同一向量空间，用对比损失+KL对齐损失联合训练，让查询排序分布对齐证据描述的排序分布
- 推理层：先做融合向量检索召回TopN候选，再经多模态重排器筛选TopK输入生成模块输出答案
### 关键结果
在5个Wikipedia QA基准上测试，对比文本提取、PixelRAG等基线，非重排版本在4个基准上准确率领先，MMSearch数据集上准确率达26.0%，较PixelRAG高4.4个百分点；加重排后SimpleQA准确率达77.6%，较PixelRAG提升4.8个百分点。
### 核心结论
富文档RAG的核心不仅是保留多模态信息，更要优先将可支撑答案的证据输送到生成模块，而非仅检索语义相关内容

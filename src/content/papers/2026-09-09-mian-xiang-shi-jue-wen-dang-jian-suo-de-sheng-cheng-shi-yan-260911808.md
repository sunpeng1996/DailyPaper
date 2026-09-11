---
title: Generative Late-Interaction Embeddings For Visual Document Retrieval
title_zh: 面向视觉文档检索的生成式延迟交互嵌入方法
authors:
- Mohamed Eltahir
- Talal Aloushan
- Rose Khairoalsendi
- Jana Shata
- Mohammed Alhassan
- Leen Alrehaili
- Tanveer Hussain
- Naeemullah Khan
affiliations:
- King Abdullah University of Science and Technology (KAUST)
- Edge Hill University
arxiv_id: '2609.11808'
url: https://arxiv.org/abs/2609.11808
pdf_url: https://arxiv.org/pdf/2609.11808
published: '2026-09-09'
collected: '2026-09-11'
category: RecSys
direction: 多向量检索 · 存储效率优化
tags:
- Late-Interaction
- Embedding Compression
- MaxSim
- Multi-Vector Retrieval
- Visual Retrieval
one_liner: 提出冻结编码器下的生成式多向量压缩方案GLIE，解决延迟交互检索存储成本过高问题
practical_value: '- 所有采用MaxSim的多向量检索场景（电商多模态商品检索、RAG检索层、广告召回），k-means聚类压缩后必须做质心单位球投影，零成本可提nDCG@5最高0.093，可直接上线

  - 已上线预训练嵌入模型的业务无需重训编码器，仅需训一个415K参的后处理编解码器，千级训练样本、3分钟GPU时间即可实现250倍压缩下精度保留79%，避免全量重推索引的成本

  - 两级检索架构可直接复用：第一阶段用压缩后的少量向量做粗排，仅对top L候选恢复全量向量做精排，大幅降低存储成本和查询延迟，适配大规模高吞吐检索场景

  - 优化多向量检索前可先分析嵌入的几何特性（分布、本征维度），针对性设计压缩方案，远好于盲目试错调参'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
延迟交互检索（如ColPali）是当前视觉文档、多模态内容检索的SOTA方案，核心是用MaxSim算子匹配query与单样本近千个patch嵌入，精度远高于单向量检索，但单样本存储成本达258KB/页，百万样本存储成本超250GB，现有压缩方案要么低预算下精度暴跌，要么需要重训编码器导致存量索引全部失效，没有兼顾冻结编码器、低存储、高精度的落地方案。
### 方法关键点
- 几何先验挖掘：实测3种主流延迟交互编码器的输出均严格落在单位球面上，且单样本近千个嵌入的本征流形维度仅5-6，远低于嵌入的环境维度，为极低资源压缩提供了理论依据
- 球形锚定trick：k-means得到的聚类质心天然落在单位球内部，会系统性低估MaxSim得分，将质心投影回单位球面即可零成本提升检索精度
- GLIE架构设计：单样本仅存储k个归一化后的锚定向量，查询时第一阶段用锚定向量做粗排，仅对top20候选用轻量解码器恢复全量嵌入做精排；编码器全程冻结，编解码器总参仅415K，训练仅需千级样本、3分钟GPU时间
### 关键实验
在ViDoRe v1/v2多模态检索基准上测试，对比所有冻结编码器的基线方案：
- 单页仅存4个向量（压缩250倍）时，ViDoRe v1上nDCG@5保留未压缩系统的79%，比最优基线高9个百分点，优于同训练预算下的编码器LoRA微调方案
- 球形锚定单独贡献nDCG@5提升0.031~0.093，存储预算越低增益越明显
### 核心结论
多向量嵌入的几何分布特性是压缩优化的核心抓手，零成本的归一化trick带来的收益往往超过复杂的重训方案

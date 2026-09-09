---
title: 'EigenLI: Spectral Approximations to Late Interaction'
title_zh: EigenLI：面向晚交互检索模型的谱近似压缩方法
authors:
- Archish S
- Sabyasachi Basu
- Ankit Garg
- Ravishankar Krishnaswamy
- Kirankumar Shiragur
affiliations:
- Temple University
- Microsoft Research India
arxiv_id: '2609.07561'
url: https://arxiv.org/abs/2609.07561
pdf_url: https://arxiv.org/pdf/2609.07561
published: '2026-09-07'
collected: '2026-09-09'
category: RecSys
direction: 晚交互检索 · 多向量压缩
tags:
- Late Interaction
- Multi-Vector Retrieval
- Model Compression
- ColBERT
- ANN
one_liner: 提出训练无关的晚交互检索谱压缩框架，效果效率优于聚类及MUVERA等主流基线
practical_value: '- 电商/搜索召回场景使用ColBERT类晚交互模型时，可直接用k≤32的EigenLI替换现有k-means/Ward聚类压缩方案，ColBERTv2上nDCG@10最高提升15%，压缩速度快6~17倍

  - 需对接现有ANN检索系统的场景，可采用EigenLI-SV单向量变体，相比主流MUVERA方案nDCG@10最高提升178%，维度更低且兼容PQ等标准量化策略

  - 多模态商品图文检索场景，ColQwen类视觉晚交互模型可尝试k=32的EigenLI压缩，nDCG@10相对聚类方案提升5.5%，大幅降低索引存储成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
晚交互模型（如ColBERT）检索效果远超单向量模型，但单文档需存储数百个token向量，索引、存储、MaxSim打分成本过高，现有训练无关压缩方案以k-means、Ward聚类为主，压缩速度慢且效果仍有提升空间。

### 方法关键点
- 发现文档token嵌入存在内在低秩结构，二阶矩矩阵特征值快速衰减，仅需保留top-k主特征方向即可覆盖大部分检索信号
- 提出k-EigenLI，用文档二阶矩矩阵的top-k特征向量表征文档，打分函数为查询token在该子空间投影的模长平方和，无需训练即可直接替换原MaxSim逻辑
- 延伸出EigenLI-SV单向量变体，通过张量外积将打分转化为高维向量点积，完美兼容现有ANN检索系统

### 关键结果
在BEIR文本检索数据集测试ColBERTv2等3款模型，ViDoRe-v3多模态数据集测试ColQwen3 4B模型，对比k-means、Ward聚类、MUVERA等基线：
- k=32时，ColBERTv2上EigenLI nDCG@10相对k-means提15%、相对Ward提8%，压缩速度比k-means快6.8倍、比Ward快17.5倍
- EigenLI-SV比MUVERA维度低19%，ColBERTv2上nDCG@10相对提78.9%，AnswerAI-ColBERT-small上相对提178.1%
- 多模态场景下k=32时EigenLI nDCG@10相对k-means提5.5%

### 核心结论
晚交互多向量表征普遍存在内在低秩结构，训练无关的谱压缩在大多数场景下性价比显著优于聚类类方案。

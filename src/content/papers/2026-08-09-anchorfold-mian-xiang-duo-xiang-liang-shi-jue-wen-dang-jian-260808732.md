---
title: 'AnchorFold: A Focus-Then-Fold Framework via Recursive Attention Propagation
  for Efficient Multi-Vector Visual Document Retrieval'
title_zh: AnchorFold：面向多向量视觉文档检索的无训练先聚焦后压缩索引框架
authors:
- Haoyu Zuo
- Yibo Yan
- Xin Zou
- Shuliang Liu
- Yi Cao
- Mingdong Ou
- Xuming Hu
affiliations:
- Hong Kong University of Science and Technology (Guangzhou)
- Alibaba Cloud Computing
- Hong Kong University of Science and Technology
arxiv_id: '2608.08732'
url: https://arxiv.org/abs/2608.08732
pdf_url: https://arxiv.org/pdf/2608.08732
published: '2026-08-09'
collected: '2026-08-11'
category: RAG
direction: 多模态RAG · 多向量索引压缩
tags:
- Multi-Vector Retrieval
- Index Compression
- Visual Document Retrieval
- Late Interaction
- Training-free
one_liner: 无训练多向量视觉文档检索索引压缩框架，20倍压缩下仍保留92.4%的全索引NDCG@5
practical_value: '- 存量多向量检索系统（如ColBERT系文本/多模态召回）可直接复用「先选高重要性锚点+相似度聚类加权聚合」范式，无需重新训练模型，适配任意Transformer
  backbone，快速实现降本

  - Recursive Attention Propagation token重要性计算方法可迁移到推荐系统用户/物品embedding压缩、短视频多帧embedding聚合场景，无需额外标注，仅用自注意力矩阵即可得到更准确的权重

  - 电商场景商详页、多模态商品内容、PDF合同检索召回可直接套用该框架，5倍压缩下仅损失1.7%的NDCG@5，基本不影响召回效果的前提下降低存储与查询算力成本

  - 压缩超参可通过SR（压缩前后MaxSim得分比）在少量无标注样本上自动校准，无需人工调参，工程落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多向量视觉文档检索（如ColPali）通过late interaction实现细粒度匹配，但单页需存储数百个视觉patch embedding，存储与查询算力成本随向量数线性增长；现有无训练压缩方案要么剪枝丢失关键信息，要么合并时不区分区域重要性，高压缩比下效果掉点严重，亟需无训练、高保准的压缩方案适配大规模落地。

### 方法关键点
- 整体为无训练的focus-then-fold两阶段范式，仅在离线建索引阶段执行，不修改查询编码和MaxSim打分逻辑，可插拔接入任意多向量检索backbone
- Focus阶段：从Transformer多层多头自注意力矩阵构建视觉注意力图，执行6步递归注意力传播，整合跨头跨层分数得到每个token的传播注意力中心性，选top-m个最高得分token作为锚点，m由目标压缩比决定
- Fold阶段：非锚点token在归一化检索空间分配给最相似的锚点，每个锚点组用中心性加权聚合得到最终压缩向量，保留非锚点贡献的同时集中容量给重要区域

### 关键结果
在ViDoRe v1/v2、REAL-MM-RAG 3个基准，ColPali、ColQwen2.5、Nemotron ColEmbed-3B 3个异构backbone上测试，对比SAP、DocPruner、语义聚类、1D池化等所有无训练baseline：
- 5倍压缩（保留20%向量）下平均保留98.3%的全索引NDCG@5，比最强baseline高2.7个百分点
- 20倍压缩（保留5%向量）下平均保留92.4%的全索引NDCG@5，比最强baseline高4.6个百分点
- 仅比全索引增加11%的离线建索引耗时，查询阶段完全无额外开销

最值得记住的一句话：无训练的多向量索引压缩只要做好「重要性合理分配+非重要信息有效聚合」，就能在极高压缩比下实现接近无损的效果，甚至优于需要额外训练的压缩方案。

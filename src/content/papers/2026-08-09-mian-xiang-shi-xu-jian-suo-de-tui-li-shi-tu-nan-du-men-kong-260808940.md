---
title: Difficulty-Gated Fusion of Reasoning Views for Temporal Retrieval
title_zh: 面向时序检索的推理视图难度门控融合方法
authors:
- Jamie Holdcroft
- Abdelrahman Abdallah
- Adam Jatowt
affiliations:
- UNSW Sydney
- University of Innsbruck
arxiv_id: '2608.08940'
url: https://arxiv.org/abs/2608.08940
pdf_url: https://arxiv.org/pdf/2608.08940
published: '2026-08-09'
collected: '2026-08-11'
category: RecSys
direction: 时序检索 · 多视图排序融合
tags:
- temporal retrieval
- rank fusion
- query expansion
- QPP
- dense retrieval
one_liner: 提出轻量难度门控融合方案，无需微调检索器/重排序即可提升全品类时序检索器性能
practical_value: '- 召回阶段多query改写（同义词扩展、时序/场景意图补全等）的排序融合可直接复用该方案：仅需基于每个query的检索结果分数分布提取8维QPP特征，用1k参数量的小MLP训练门控权重，完全不改动现有检索器，侵入性极低

  - 改写视图的权重分配无需人工规则，通过预测单视图检索质量的轻量门控自动适配，对弱检索backbone增益更明显，适合算力受限的端侧/低资源业务场景

  - 可直接复用z-normalization加分数兜底的跨视图分数校准方法：未出现在当前视图召回池的item统一打低于池内最低分1个标准差的分数，避免漏召回的item被误判为中等质量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
时序推理类检索任务的相关性不依赖词面匹配，需要对query做时序意图显式改写后再检索，但传统等权融合多改写视图的排序结果会稀释优质视图的收益，现有方案要么需要微调检索器、要么依赖重排序，落地成本高。

### 方法关键点
- 离线用LLM生成3种时序推理改写视图（变化追踪、基线对比、事件排序），加原query构成多视图集合，所有视图共用同一个冻结的检索器独立召回
- 对每个视图的Top-N召回结果做z-normalization，未被该视图召回的文档统一赋值为低于池内最低分1个标准差的分数，对齐不同视图的分数分布
- 提取每个视图的8维QPP特征（Top100分数softmax熵、前1/2/5/10位分数差、前100分数均值/标准差、分数衰减斜率、最高分数）作为难度表征
- 用约1k参数量的MLP门控网络将8维特征映射为单视图质量预测值，经温度softmax生成每个query的视图权重，加权融合得到最终排序，门控采用留一任务交叉验证训练，推理时无需标注

### 关键实验
在Tempo时序检索基准13个任务上测试6种不同架构/规模的检索器，所有检索器的nDCG@10均有提升，弱检索器最高提升6.3个点，最强的E5检索器从0.271提升到0.303，SFR检索器从0.265提升到0.297，增益显著（p<0.001）；比等权融合多提1.3个点的nDCG@10。

### 值得记住的一句话
多query改写的融合收益远不止于召回池的并集，基于检索分数分布的轻量质量预判可以在几乎无额外成本的前提下释放改写的潜在增益。

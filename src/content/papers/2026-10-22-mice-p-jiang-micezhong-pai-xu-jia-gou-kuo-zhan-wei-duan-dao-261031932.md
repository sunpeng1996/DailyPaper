---
title: 'MICE to Meet You: From Re-ranking Only to End-to-End Retrieval'
title_zh: MICE-P：将MICE重排序架构扩展为端到端神经检索系统
authors:
- Victor Morand
- Yuxuan Zong
- Mathias Vast
- Josiane Mothe
- Benjamin Piwowarski
affiliations:
- Sorbonne Université
- CNRS
- Sinequa by ChapsVision
- University of Toulouse
- IRIT
arxiv_id: '2610.31932'
url: https://arxiv.org/abs/2610.31932
pdf_url: https://arxiv.org/pdf/2610.31932
published: '2026-10-22'
collected: '2026-10-26'
category: RecSys
direction: 神经检索 · 效率效果帕累托优化
tags:
- NeuralRetrieval
- CrossEncoder
- LateInteraction
- PLAID
- ReRanking
one_liner: 适配PLAID索引实现MICE架构端到端检索，兼具cross-encoder效果与late-interaction效率
practical_value: '- 跨架构蒸馏trick：从已训好的cross-encoder checkpoint出发两阶段微调迁移到MICE类轻量化重排序架构，保留99%以上效果的同时大幅降低训练成本，可复用在业务重排序模型的轻量化迭代上

  - 多向量存储适配方案：给预计算的文档表示加128维线性投影+LayerNorm瓶颈层，适配PLAID压缩存储，效果仅下降0.2个nDCG@10，可直接复用在现有late-interaction检索系统的存储优化

  - 量化选型经验：带注意力交互的多向量检索模型选4bit量化可平衡存储与效果，避免2bit量化带来的3%以上效果损失，可套用到电商商品/内容检索的向量压缩场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前神经检索领域存在明显的效果效率trade-off gap：cross-encoder效果最优但推理延迟高，仅能用于小候选集重排序；以ColBERT为代表的late-interaction模型支持文档向量预计算、端到端检索，但效果弱于cross-encoder。此前提出的MICE重排序架构理论上可结合两者优势，但缺乏可落地的多向量索引存储方案，无法实现端到端检索。
### 方法关键点
- 新增低维适配瓶颈层：在MICE输出的文档上下文表示后加入128维线性投影+LayerNorm，适配PLAID索引的存储要求，压缩后的向量通过上投影恢复原维度送入交互层，避免效果损失
- 两阶段迁移训练：从预训练好的Ettin cross-encoder checkpoint出发，先适配MICE架构全参数微调，再冻结上下文层仅训练瓶颈层与交互层，规避反向传播导致的表征退化
- 检索链路设计：用SPLADEv3做第一阶段召回Top100候选，再从PLAID索引拉取压缩文档表示，解压缩后送入MICE交互层打分，兼顾召回效率与排序精度
### 关键结果
在去污染BEIR13、LoTTE-Search基准数据集上与同参数规模的cross-encoder、ColBERT变体对比：MICE-P-61m的BEIR13平均nDCG@10达57.8，仅比同规模cross-encoder低0.2，比同规模ColBERT高1.1；推理延迟与SOTA late-interaction模型LateOn持平，仅为同规模cross-encoder的40%，存储仅比LateOn高50%，达到全新的帕累托最优。
### 核心结论
通过架构适配和迁移训练，可将cross-encoder级别的重排序效果落地到端到端检索链路，实现效果和效率的最优平衡

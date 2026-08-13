---
title: 'Deciding When to Rely on Visual Information: Gated Multimodal Fusion in Sequential
  Recommendation'
title_zh: 序列推荐门控多模态融合：自适应判断视觉信息的使用时机
authors:
- Natalija Glisovic
- Danica Kragic
- Martin Tegner
affiliations:
- IKEA Retail (Ingka Group)
- KTH Royal Institute of Technology
arxiv_id: '2608.10700'
url: https://arxiv.org/abs/2608.10700
pdf_url: https://arxiv.org/pdf/2608.10700
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 多模态序列推荐 · 自适应门控融合
tags:
- Sequential-Recommendation
- Multimodal-Fusion
- Gating-Mechanism
- Visual-Aware-Rec
- Contrastive-Learning
one_liner: 提出VisGate自适应门控框架，动态融合视觉与协同信号，提升多模态序列推荐效果与可解释性
practical_value: '- 多模态融合不要使用全局静态权重，可借鉴VisGate的「物品特征+用户序列上下文」双条件门控设计，冷启动/交互稀疏场景增益尤其显著

  - 视觉特征预训练无需强制对齐到ID embedding空间，采用序列共现对比学习能保留模态互补性，进一步放大融合收益

  - 训练完成的门控权重可直接作为分析工具，量化不同品类/物品的视觉信息贡献度，指导商品素材优化与品类运营策略

  - 针对视觉独特但交互极少的商品，可叠加交互数阈值作为门控后修正规则，避免模态误用的bad case'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态序列推荐通常全局统一融合视觉与协同信号，忽略了视觉信息的效用随物品属性、用户交互稀疏度动态变化的特性，静态融合易引入冗余噪声，在冷启动、交互稀疏场景下表现受限，同时也无法解释不同场景下视觉信号的贡献差异。

### 方法关键点
- 提出VisGate三模块架构：共现对齐视觉投影层、上下文感知自适应门控、多目标联合训练
- 视觉投影层采用序列共现对比学习预训练，不将视觉特征对齐到ID embedding空间，保留两类模态的互补性
- 门控机制同时输入物品ID embedding、预训练视觉特征、用户当前序列上下文隐向量，动态生成每个物品的模态融合权重
- 训练损失在BERT4Rec的MLM损失基础上，增加门控稀疏损失和模态均衡损失，避免门控坍缩到单一模态

### 关键结果
在IKEA私有数据集+3个公开Amazon数据集上，对比BERT4Rec、VBPR、MMGCN、HM4SR等12个基线，稀疏场景（IKEA、Amazon Scientific）下Hit@10相对最优基线分别提升7.1%、7.7%，NDCG@10分别提升7.3%、22.8%，稠密场景下也有1%~6.5%的小幅增益。分析表明用户交互历史越短、物品ID信号越弱、视觉区分度越高，门控分配给视觉特征的权重越高。

最值得记住的一句话：多模态融合的核心不是让不同模态尽可能对齐，而是保留模态互补性的同时，在细粒度维度上动态匹配场景对各模态的信息需求。

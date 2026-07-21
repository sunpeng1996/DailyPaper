---
title: Learning Sparse Representations of Multimodal Content for Enhanced Cold Item
  Recommendation
title_zh: 面向冷启动商品推荐的多模态内容稀疏表示学习
authors:
- Gregor Meehan
- Johan Pauwels
affiliations:
- Queen Mary University of London
arxiv_id: '2607.17184'
url: https://arxiv.org/abs/2607.17184
pdf_url: https://arxiv.org/pdf/2607.17184
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 冷启动推荐 · 稀疏多模态表示学习
tags:
- ColdStartRecommendation
- SparseRepresentation
- MultimodalRecSys
- ContentBasedRec
- EmbeddingCompression
one_liner: 提出多模态稀疏嵌入学习方案，同等存储下显著提升冷启动推荐效果，尤其适配多兴趣用户
practical_value: '- 冷启动场景可直接替换现有稠密embedding为稀疏嵌入：同等存储成本下NDCG@20可提升16.6%-75.5%，多兴趣用户增益更明显，同时降低向量检索时延

  - 可复用预稀疏激活（PSAF）设计：稀疏化前加two-sided α-entmax激活，无需修改训练目标，仅增加15%-20%训练成本即可获得额外精度增益

  - 稀疏嵌入天然具备可解释性：每个激活维度可对应到商品语义类目，无需额外标注即可实现用户兴趣归因、商品分群运营

  - 工程实现兼容现有向量生态：pgvector已原生支持稀疏向量检索，不需要额外改造检索链路即可快速上线'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前平台商品规模快速增长，稠密embedding存储成本高、检索效率低，冷启动商品无交互历史难以生成有效表示；现有LLM类冷启动方案时延过高无法大规模落地，多兴趣用户的冷启动推荐效果退化严重，亟需兼顾效果、成本、效率的冷启动表示方案。

### 方法关键点
- 基于现有content-based冷启动框架SEMCo/ELSA改造，仅修改输出层稀疏化逻辑，不改动原有训练目标，迁移成本低
- 稀疏化策略：保留embedding绝对值top-k维度，其余置零，训练时用指数衰减策略逐步降低激活维度，避免出现死神经元
- 新增预稀疏激活层（PSAF）：先通过two-side拼接[y;-y]保留正负信号，再用α-entmax激活，诱导相似度分布具备锐化和降噪特性，无需额外监督信号

### 关键实验
在4个多模态推荐数据集（电商服饰、3C、音乐、短视频）上对比5种稠密冷启动baseline，同等存储成本下，稀疏方案冷启动NDCG@20最高提升75.5%；仅32个激活维度的稀疏嵌入效果优于1024维稠密嵌入，存储成本降低16倍；对拥有4类以上兴趣的用户，增益是单兴趣用户的2倍以上。

内容冷启动场景下，稀疏嵌入不是稠密嵌入的「压缩版」，而是效果更好、成本更低、可解释性更强的原生优选方案

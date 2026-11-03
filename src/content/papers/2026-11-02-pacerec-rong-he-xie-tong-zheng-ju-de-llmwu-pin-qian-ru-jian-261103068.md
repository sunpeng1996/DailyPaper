---
title: 'PACERec: Progressive Adaptation of LLM Item Embeddings with Collaborative
  Evidence for Recommendation'
title_zh: PACERec：融合协同证据的LLM物品嵌入渐进适配推荐框架
authors:
- Junzhao Huang
- Xi Wu
- Zihan Wang
- Zijing Wang
- Ming Wang
- Kang Liu
- Xiaocui Yang
- Shi Feng
- Daling Wang
- Yifei Zhang
affiliations:
- 东北大学
- 蚂蚁集团
arxiv_id: '2611.03068'
url: https://arxiv.org/abs/2611.03068
pdf_url: https://arxiv.org/pdf/2611.03068
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 无ID物品嵌入适配
tags:
- LLM4Rec
- Flow Matching
- Long-Tail Recommendation
- Sequential Recommendation
- Cold Start
one_liner: 提出无ID的流匹配适配框架，将LLM静态物品嵌入融合序列行为信号，提升全量与长尾推荐效果
practical_value: '- 可复用「用高频物品的序列转移行为训练共享适配流，迁移知识到长尾/冷启物品」的设计，无需为长尾物品单独训练ID embedding，大幅降低冷启成本

  - 工程落地trick：适配后的行为表示打分 + 原生LLM语义相似度加权融合，权重λ在验证集调优，长尾推荐增益明显，几乎无额外推理开销

  - 可迁移的训练策略：给物品表示加语义锚定损失+位移约束，避免适配后丢失物品原始语义，解决语义漂移问题

  - 流匹配轻量化实现：仅用2步欧拉迭代即可达到不错效果，无需复杂ODE求解，适配大商品库的离线预计算场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强的序列推荐存在两类缺陷：ID+LLM融合方案的长尾物品ID训练不充分，全局校准LLM嵌入的方案未融入用户序列转移规律（比如用户买相机后倾向买镜头而非同类相机）。统计显示静态LLM语义邻居对序列前置物品的覆盖率不足10%，远低于行为邻居的90%，直接导致长尾推荐效果差。

### 方法关键点
- 无ID架构：仅用LLM生成的物品文本静态嵌入作为输入，无需维护独立的item ID embedding
- 行为目标预计算：每个物品的目标表示是用户交互前L步前置物品的语义表示按近因加权聚合，训练全程固定不变
- 渐进适配流设计：用流匹配学习共享速度场，仅用训练样本数超阈值的高频物品做置信加权监督，给嵌入加位移约束避免语义漂移
- 推理优化：离线预计算全库适配后的物品表示缓存，在线融合序列backbone打分+原生LLM语义相似度打分，无额外计算开销

### 关键结果
在Beauty、Food、Yelp三个公开电商/本地生活数据集，覆盖SASRec、FMLP-Rec、LRURec三个主流序列backbone，对比ACE、FAERec等SOTA基线：整体NDCG@10平均提升13.53%，最高提升28.41%；长尾NDCG@10平均提升33.31%，零交互冷启物品的NDCG@10最高提升83%。

### 核心结论
静态LLM物品语义和用户序列行为转移存在本质差异，用高频物品的行为规律训练共享适配函数，是兼顾整体推荐效果和长尾/冷启性能的低成本路径

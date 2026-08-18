---
title: POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive
  Alignment
title_zh: 基于LLM增强多图学习与对比对齐的POI推荐方法
authors:
- Burak Tamer
- Wolfram Höpken
- Zehui Wang
affiliations:
- University of Applied Sciences Ravensburg-Weingarten, Germany
arxiv_id: '2608.16407'
url: https://arxiv.org/abs/2608.16407
pdf_url: https://arxiv.org/pdf/2608.16407
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: POI推荐 · 多图对比学习
tags:
- POI-Recommendation
- LightGCN
- Contrastive-Learning
- Multi-Graph-Learning
- Cold-Start
- LLM4Rec
one_liner: 为LightGCN增加LLM语义、地理两个item-item图，跨视图对比对齐缓解POI推荐冷启动
practical_value: '- 本地生活/到店推荐业务可直接复用双辅助item-item图构建逻辑：用LLM生成的商家/商品描述做语义相似度图，用地理位置/品类共现做属性邻接图，无需改召回链路即可补充冷启动信号

  - 跨视图对比对齐trick可直接迁移到现有GNN推荐框架：无需做随机扰动的图增强，直接对齐交互视图与语义/属性视图的item embedding，涨点明显，计算开销远低于多模态端到端训练

  - 冷启动场景下资源优先级明确： ablation显示去掉对比损失Recall@20下降22.9%，远高于去掉单个辅助图的损失，资源有限时可先上跨视图对齐模块，再逐步叠加辅助图'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GNN-based POI推荐高度依赖用户-商家交互数据，冷启动商家因缺乏交互信号无法得到有效表征，而商家的语义信息（品类、环境描述等）、地理位置信息都是不依赖交互的原生数据，未被充分利用来补全缺失的协同信号。

### 方法关键点
- 以LightGCN为基础框架，新增两个并行的item-item传播路径：1）语义图：基于LLM生成的商家照片摘要、关键词的Sentence-BERT embedding计算余弦相似度，取top10邻接构建；2）地理图：基于商家经纬度的Haversine距离，取10个最近邻、距离倒数做边权构建。
- 三个图（用户-商家交互图、语义图、地理图）的item embedding共享初始化，分别传播后相加融合，最终与user embedding做内积计算推荐得分。
- 新增双向InfoNCE对比损失，对齐交互视图与语义、地理视图的同一item embedding，增强表征一致性。

### 关键实验
在Yelp多模态推荐数据集上对比8个基线：相比LightGCN，Recall@20提升52.0%，NDCG@20提升64.8%；与当前最优对比基线SGL性能相当，但SGL同样受冷启动限制，本方法的语义/地理信号可覆盖冷启动商家。ablation显示去掉对比损失Recall@20下降22.9%，去掉任意一个辅助图性能仅下降1%以内，对比对齐是核心涨点来源。

### 核心结论
外部获取的LLM生成item语义知识可有效替代缺失的协同信号，跨视图对比对齐比单纯叠加辅助图对性能提升的贡献更大

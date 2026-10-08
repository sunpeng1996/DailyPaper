---
title: 'From High Recall to High Utility: Dataset-Adaptive Post-Processing of LLM-Generated
  Customer Intents'
title_zh: 从高召回向高可用转化：LLM生成客户意图的数据集自适应后处理架构
authors:
- Mahesh Viswanathan
- Joan Rossello
- Leticia Fernandes
- Paul Mutawe
affiliations:
- Cisco Systems, Inc.
arxiv_id: '2610.09039'
url: https://arxiv.org/abs/2610.09039
pdf_url: https://arxiv.org/pdf/2610.09039
published: '2026-10-06'
collected: '2026-10-08'
category: QueryRec
direction: 意图提取后处理 · 语义检索优化
tags:
- Intent Extraction
- LLM Post-processing
- Semantic Clustering
- Semantic Retrieval
- Cold Start
one_liner: 提出分阶段自适应后处理架构，将高召回LLM生成的冗余客户意图转化为稳定可复用的业务单元
practical_value: '- 高召回+后处理的两阶段架构可直接复用在搜索意图识别、用户评论语义聚合场景：先通过宽松prompt拉满召回避免漏召回，再通过后处理做语义去重聚合，平衡召回率和实用性

  - 数据集自适应聚类策略可直接借鉴：小候选集用相似度连通分量、中集用层次聚类、大集用UMAP+HDBSCAN，比固定单一聚类算法在不同规模候选集下的纯度、运行效率更均衡

  - 意图到业务结果的检索架构可迁移到电商query到商品匹配场景：先用bi-encoder做高召回粗排，再用cross-encoder做精排，实测F1@5和MRR和纯cross-encoder持平，latency仅增加0.004s，几乎和纯bi-encoder一致

  - 孤立意图的双重校验策略（embedding相似度+关键词相似度双阈值）可复用在语义匹配场景，减少误聚合同时保留低频有效意图，避免丢失长尾需求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM从多源异构企业数据（用户会话、运营记录、结构化表单等）提取客户意图时，为避免漏召回通常会生成大量冗余、粒度不均、语义重叠的候选，直接交付下游系统或人工审核的实用性极低；现有方案大多将后处理视为简单格式清洗，未形成体系化的语义聚合架构，也未保留溯源信息，无法满足企业级业务可解释、可追溯的要求。

### 方法关键点
- 分阶段解耦架构：前序抽取阶段优先保障召回，后处理阶段专门做语义降维提效，两个目标完全隔离；
- 8步自适应后处理流水线：先做确定性标准化去重，再通过可选的元数据拼接优化短文本embedding效果，根据候选集规模自适应选择聚类算法（≤20用相似度连通分量、20-50用层次聚类、≥50用UMAP+HDBSCAN），生成聚类关键词作为可解释层，孤立意图需同时满足embedding和关键词双相似度阈值才会被聚合，最后用约束式LLM生成每个聚类的精简意图，全程保留所有溯源、模型、参数元数据；
- 两大下游应用：一是冷启动客户的意图生成，通过同属性客户的历史意图做聚合推断；二是意图引导的语义检索，采用bi-encoder粗排+cross-encoder精排的混合架构匹配业务结果。

### 关键实验
在企业客户数据集上测试，意图提取SME评估准确率78%；意图到业务结果的检索任务上，混合架构F1@5达54.82%、MRR达0.87，和纯cross-encoder效果持平，latency仅0.06s，接近纯bi-encoder的0.056s，远优于零-shot分类器的1.213s；SME评估推荐的业务结果相关性100%，冷启动客户的同类用户匹配准确率81.6%。

### 最值得记住的一句话
确定性逻辑和大模型能力要各司其职，规则能搞定的去重、格式化、映射类问题不要用大模型，把大模型留给真正需要语义理解、生成的场景，既能降本提效还能提升可解释性。

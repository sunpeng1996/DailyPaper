---
title: 'Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document
  Deletion'
title_zh: Lightfoot：支持无模型精确文档删除的GraphRAG系统
authors:
- Uday Allu
arxiv_id: '2611.11010'
url: https://arxiv.org/abs/2611.11010
pdf_url: https://arxiv.org/pdf/2611.11010
published: '2026-11-07'
collected: '2026-11-10'
category: RAG
direction: GraphRAG 低开销无模型精确删除
tags:
- GraphRAG
- Retrieval-Augmented Generation
- Document Deletion
- Low-cost Indexing
- Multi-hop QA
one_liner: 提出低索引成本、检索无模型调用、支持精确无模型删除的GraphRAG系统Lightfoot
practical_value: '- 溯源绑定单文本抽取结果的GraphRAG设计可直接复用在电商合规场景，商品/内容下架仅需数据库操作，无需重新训练模型或生成汇总内容，满足被遗忘权要求

  - 单段落1次LLM抽取+检索无模型调用的架构，可大幅降低大流量场景下RAG的推理成本，适合电商智能客服、商品详情问答、个性化导购Agent等落地场景

  - Personalized PageRank召回结果与cross-encoder重排结果做Reciprocal Rank Fusion的方法，可直接迁移到搜索/推荐多源召回的排序融合环节，提升排序效果

  - 文档删除后的指纹比对验证方法，可用于合规场景下校验用户/商品数据的完全删除，避免残留信息被召回输出'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG研究多聚焦多跳问答准确率，忽略落地核心约束：一是索引构建成本高，多次LLM抽取、社区汇总等操作带来数倍开销；二是文档删除能力缺失，合规要求的被遗忘权难以满足，现有框架要么删除需大量模型调用，要么无法保证删除后索引与从未加入该文档的全新索引等价。
### 方法关键点
- 抽取层：每段文本仅调用1次LLM，输出压缩为最小格式JSON，抽取最多12个实体、12条事实，大幅降低token开销
- 溯源设计：所有图节点、边均为单段落抽取结果的确定性函数，无跨段落的模型生成汇总内容，删除文档仅需移除对应段落的抽取记录，重新计算关联实体组件，全程无模型调用
- 检索层：无LLM调用，基于query embedding匹配种子事实启动Personalized PageRank选候选段落，再与cross-encoder重排结果做Reciprocal Rank Fusion输出最终召回结果
### 关键结果
在MuSiQue、2WikiMultiHopQA、HotpotQA三个多跳QA数据集上对齐模型配置对比4个开源GraphRAG基线：
- 索引成本比HippoRAG 2低26~31%，比LightRAG、fast-graphrag低3~6倍，检索无模型调用延迟仅0.53s
- MuSiQue数据集recall@5比HippoRAG 2高2.8个百分点，HotpotQA exact match高7.7个百分点
- 删除10%文档仅需74秒、0模型调用，删除后索引与从零构建的存活文档索引完全等价，LightRAG删除相同规模文档需2187次模型调用、耗时3.7小时
> 最值得记住的一句话：GraphRAG落地的核心瓶颈从来不是上限准确率，而是索引成本、推理延迟和合规能力的平衡

---
title: 'STITCH-RAG: Spatio-Temporal Influence Tracing over Topic Hypergraphs for Multi-Hop
  Retrieval-Augmented Generation'
title_zh: STITCH-RAG：面向多跳RAG的主题超图时空影响追踪框架
authors:
- Haodong Yang
- Mengzhu Chen
- Jia Cai
affiliations:
- Guangdong University of Finance&Economics
arxiv_id: '2609.34127'
url: https://arxiv.org/abs/2609.34127
pdf_url: https://arxiv.org/pdf/2609.34127
published: '2026-09-28'
collected: '2026-09-29'
category: RAG
direction: 多跳检索增强生成 · 超图结构索引
tags:
- RAG
- Multi-hop Retrieval
- Hypergraph
- Personalized PageRank
- Information Retrieval
one_liner: 基于半融合主题超图的多跳RAG框架，显著提升跨文档证据链检索性能
practical_value: '- 半融合主题超图索引可直接复用在电商多跳关联检索场景（如"某电影主角同款外套"类跨实体query），通过保留分块级实体上下文+同名实体等价关联的设计，避免同名商品/人物的检索混淆

  - STIBP的频率自适应衰减机制可迁移到推荐系统的用户行为序列权重计算，高频实体的跨距离关联权重衰减更快，有效降低冗余召回

  - 用连续关联得分作为PPR扩散先验的思路，可优化现有图召回链路的初始化策略，替换传统二元匹配规则，提升跨实体关联召回的覆盖率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG存在两类核心缺陷：分块RAG易打断跨文档/跨分块的证据链，无标签成对关系图RAG无法同时保留主题级共现信息和实体逐次出现的上下文描述，导致跨实体多跳检索的准确率和召回率偏低，难以处理复杂关联类查询。
### 方法关键点
1. 构建半融合主题超图：以主题摘要为超边，分块级上下文感知实体描述为节点，通过标准名称等价链接关联同名实体的不同出现状态，同时保留全局身份关联和局部上下文信息
2. 时空影响桥接传播（STIBP）：空间维度在同主题超边内传播关联影响，时间维度基于实体出现频率自适应衰减，跨同名实体的不同分块状态传递关联得分
3. 连续先验PPR扩散：将STIBP输出的连续得分作为局部Personalized PageRank的先验，替换传统二元实体匹配的种子初始化策略，实现更精准的关联扩散
### 关键结果
在HotpotQA、2WikiMultiHopQA两个公开多跳QA数据集上测试，对比LightRAG、LinearRAG、HippoRAG等主流RAG方案，Contain-Acc相对最优基线分别提升3.9、5.6个百分点，Recall@8相对LinearRAG分别提升7.5、5.7个百分点，检索阶段无额外LLM调用，运行开销仅高于LinearRAG。
> 最值得记住的结论：多跳RAG的核心优化方向不是单纯提升单块检索相似度，而是通过结构索引保留跨实体、跨分块的关联关系，同时避免实体全合并带来的上下文信息损失。

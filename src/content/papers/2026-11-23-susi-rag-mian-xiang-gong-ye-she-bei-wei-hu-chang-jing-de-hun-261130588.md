---
title: 'SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance'
title_zh: SuSi-RAG：面向工业设备维护场景的混合Graph RAG架构
authors:
- Hansi Zhang+
- Wilma Johanna Schmidt+
- Wanlin Yang
- Xiaozhi Shen
- Adrian Paschke
- Evgeny Kharlamov
affiliations:
- Robert Bosch GmbH
- Freie Universität Berlin
- Fraunhofer Institute FOKUS
- Fudan University
- University of Oslo
arxiv_id: '2611.30588'
url: https://arxiv.org/abs/2611.30588
pdf_url: https://arxiv.org/pdf/2611.30588
published: '2026-11-23'
collected: '2026-11-24'
category: RAG
direction: 混合Graph RAG · 工业场景落地优化
tags:
- GraphRAG
- HybridRAG
- KnowledgeGraph
- RetrievalAugmentedGeneration
- IndustrialAI
one_liner: 提出融合子图相似度匹配、专家加权的混合Graph RAG，在工业维护场景落地验证优异效果
practical_value: '- 复杂多跳/跨域检索场景可复用「子图相似度+BM25+交叉编码器重排」的RRF融合排序方案，结合领域专家给实体加权，能大幅提升top-1检索准确率

  - 可借鉴偏匹配惩罚因子设计，避免仅匹配少量实体的文档获得过高排名，优化短/信息不全Query的检索效果

  - 部署层面可复用历史Query解析结果缓存的思路，减少LLM调用开销，显著提升检索响应速度

  - 可复用用户反馈闭环设计，区分知识缺口和映射错误两类bad case，定向优化知识库，实现系统效果的持续迭代'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业设备维护查询普遍存在复杂因果链推理、跨域信息融合需求，传统向量RAG上下文感知能力弱，检索准确率仅61.5%，无法满足生产场景对答案准确性、可追溯性的要求，且分散的异构维护知识难以被一线人员高效获取，亟需更适配领域特性的RAG架构。

### 方法关键点
- 混合检索架构：结合知识图谱子图检索与向量检索能力，兼顾结构化因果关系匹配与非结构化文本检索需求
- 子图相似度匹配：将用户Query与维护文档均解析为预定义schema的维护事件子图，模式类实体（如零件编号）做正则精确匹配，文本类实体做余弦相似度匹配，结合专家分配的实体类型权重计算匹配得分，再通过偏匹配惩罚因子修正得分，避免仅匹配少量实体的文档获得过高排名
- 多源排序融合：采用RRF方法融合子图相似度、BM25、BCEmbedding交叉编码器重排三类得分，输出最终文档排序
- 落地优化与闭环：缓存历史Query解析结果减少LLM调用开销，向量化工KG节点加速检索，压缩RDF数据降低Prompt长度；同时设计用户反馈闭环，区分知识缺口与映射错误两类bad case定向更新KG

### 关键实验
POC阶段基于26条专家标注的维护Query测试，对比向量RAG基线，Top-1检索准确率从61.5%提升至96.2%，专家评分的答案质量从44.9%提升至84.1%；落地阶段在博世量产产线稳定运行8个月，累计处理10664次Q&A交互，确认错误率仅3.75%。

### 核心结论
对于有明确schema和复杂关系的垂直领域场景，结合结构化知识匹配的混合RAG效果远优于纯向量RAG，引入领域专家知识做特征加权、搭配反馈闭环迭代是落地提效的核心。

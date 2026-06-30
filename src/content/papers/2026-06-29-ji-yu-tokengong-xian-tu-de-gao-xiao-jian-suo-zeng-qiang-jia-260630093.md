---
title: Efficient Retrieval-Augmented Generation via Token Co-occurrence Graphs
title_zh: 基于token共现图的高效检索增强生成框架TIGRAG
authors:
- Gianluca Bonifazi
- Christopher Buratti
- Michele Marchetti
- Federica Parlapiano
- Giulia Quaglieri
- Davide Traini
- Domenico Ursino
- Luca Virgili
affiliations:
- Università Politecnica delle Marche
- Università di Modena e Reggio Emilia
arxiv_id: '2606.30093'
url: https://arxiv.org/abs/2606.30093
pdf_url: https://arxiv.org/pdf/2606.30093
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: RAG · 多跳推理 · 知识图谱
tags:
- RAG
- GraphRAG
- Multi-hop Reasoning
- Knowledge Graph
- Token Co-occurrence
one_liner: 提出基于token共现图的轻量GraphRAG框架TIGRAG，解决多跳RAG的效率与精度问题
practical_value: '- 构建GraphRAG知识图谱无需LLM抽取实体关系，仅靠统计token共现即可完成，大幅降低离线索引成本，适合大语料电商知识库、企业知识库部署

  - 迭代实体驱动的多步检索策略，每次从已检索chunk提取新实体扩展查询，适合电商跨品类多跳导购、复杂用户意图拆解场景

  - 动态累积分数阈值截断候选chunk配合神经重排，可大幅压缩prompt token量，降低推理延迟同时减少LLM分心，适合线上低延迟RAG应用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统向量RAG处理多跳推理需要拼接分散证据，能力不足；现有GraphRAG方案普遍依赖大模型做实体和关系抽取，不仅离线构建计算成本极高，还会引入抽取错误导致级联失效，因此需要一种轻量高效又能保证精度的多跳RAG方案。

### 方法关键点
- 离线构建：滑动窗口切分语料chunk，过滤无效token后直接以token为节点、滑动窗口内共现频率为边权重构建知识图谱，预计算chunk embedding和token-chunk映射，无需任何LLM抽取步骤
- 单跳检索：对query预处理后用Personalized PageRank(PPR)基于query种子token做语义扩张，用PPR分数加权BM25计算候选chunk得分，通过累积分数阈值动态截断候选池，最后用余弦相似度做神经重排
- 多跳推理：迭代从每一轮top检索chunk提取未见过的命名实体，扩展query后继续检索，最终合并所有轮次结果取最高 relevance 排序

### 关键实验
在HotpotQA、2WikiMultiHopQA、MuSiQue三个主流多跳QA基准测试，对比NaiveRAG、GraphRAG、LightRAG、HippoRAG2等SOTA基线：平均R@2达到64.72%，比次优基线提升6.59个百分点；下游QA平均Exact Match 45.93%、F1 55.67%，均超过所有基线；索引时间比其他GraphRAG低1-3个数量级，平均推理延迟仅3.7s，比最快的GraphRAG基线RAPTOR快4倍，prompt token量比GraphRAG、LightRAG降低70%以上。

最值得记住的一句话：GraphRAG不需要依赖昂贵的LLM实体抽取，纯统计token共现就能高效实现高精度多跳RAG

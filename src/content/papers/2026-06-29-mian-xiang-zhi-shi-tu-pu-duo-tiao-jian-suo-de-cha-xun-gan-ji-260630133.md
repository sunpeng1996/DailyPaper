---
title: Query-Aware Spreading Activation for Multi-Hop Retrieval over Knowledge Graphs
title_zh: 面向知识图谱多跳检索的查询感知扩散激活方法
authors:
- Illia Makarov
- Mykola Glybovets
affiliations:
- National University of Kyiv-Mohyla Academy
arxiv_id: '2606.30133'
url: https://arxiv.org/abs/2606.30133
pdf_url: https://arxiv.org/pdf/2606.30133
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: Graph RAG 知识图谱多跳检索
tags:
- Graph RAG
- Knowledge Graph
- Multi-hop Retrieval
- Neo4j
- Spreading Activation
one_liner: 提出带查询感知语义门的扩散激活，单Cypher完成全检索，无需加载全图到内存
practical_value: '- 电商/Agent场景的知识图谱Graph RAG，可以直接复用每跳查询感知剪枝方案：用当前候选实体和查询的cosine相似度做语义门，同时提升检索精度、降低检索延迟

  - 工程上可借鉴全流程下沉到图数据库的设计：把整个检索逻辑封装为单条Cypher查询，一次往返完成计算，全图不流出数据库，无需把全图加载到应用内存，大幅简化生产部署

  - 多跳检索的深度调参可直接复用经验：固定3跳就足够达到精度峰值，深度继续增加不会提升精度，反而会让延迟飙升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Graph RAG方案大多仅在初始化种子节点时用到查询，后续多跳遍历完全依赖图结构，属于「查询盲」遍历；仅有的查询感知方案QAFD-RAG需要把全图加载到Python内存，还要用可变迭代次数的流扩散求解，无法适配原生图数据库，生产部署难度很高，亟需轻量可部署的查询感知多跳检索方案。

### 方法关键点
- 索引阶段：用LLM从语料提取实体和关系，经实体消歧对齐后存入Neo4j，每个实体存储描述文本的embedding并构建向量索引
- 检索阶段：从查询提取种子实体初始化激活值，固定传播迭代次数T=3；每次传播对候选节点计算查询embedding与实体描述embedding的cosine相似度作为语义门，仅保留增量超过阈值的节点更新激活值，提前剪枝无关分支
- 全流程从种子映射、传播到top-k结果选择，全部封装为单条Cypher查询，一次往返访问Neo4j，全图数据永远不流出数据库

### 关键实验结果
在MuSiQue、2WikiMultiHopQA两个多跳QA基准测试，对比GraphRAG、LightRAG、HippoRAG、QAFD-RAG四个 baseline：MuSiQue上Exact Match达到32.80，和SOTA查询感知方案QAFD-RAG的33.50几乎持平，比纯结构遍历的HippoRAG高5.3个EM、3.4个F1；关闭语义门后F1下降3.6~7.4个点，检索延迟升高1.5~4.9倍；传播深度T=3达到精度峰值，T继续增加精度不升反降，延迟翻倍。

最值得记住的一句话：每步查询感知剪枝可以同时提升精度、降低延迟，把检索计算下沉到图数据库内部可以大幅简化Graph RAG的生产部署。

---
title: A Matryoshka Hierarchical RAG for Efficient Multi-Hop Question Answering
title_zh: 基于套娃表示学习的分层RAG框架实现高效多跳问答
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
- Polytechnic University of Marche
- University of Modena and Reggio Emilia
arxiv_id: '2610.01767'
url: https://arxiv.org/abs/2610.01767
pdf_url: https://arxiv.org/pdf/2610.01767
published: '2026-10-01'
collected: '2026-10-02'
category: RAG
direction: RAG优化 · 多跳问答效率提升
tags:
- RAG
- Matryoshka Representation Learning
- Multi-hop QA
- Hierarchical Retrieval
- Efficiency
one_liner: 结合套娃表示学习与分层聚类RAG，低开销实现多跳QA效果与效率双提升
practical_value: '- 分层索引设计可复用：Matryoshka嵌入不同维度对应不同聚类粒度，上层粗聚类用短向量降计算量，无需LLM生成节点摘要，大幅压缩索引成本

  - 多轮检索漂移缓解可复用：动态调整原始query与累计上下文的权重β_t，随检索进度提升原始query权重，无需额外LLM规划调用即可降低漂移风险

  - 多跳场景重排trick可复用：轻量实体重叠特征（基于开源GLiNER做无schema NER）与语义相似度加权融合，α=0.5时效果最优，几乎无额外开销

  - 层次遍历鲁棒性优化可复用：聚类节点分配2个父节点增加路径冗余，可大幅降低贪心自上而下遍历的漏召回风险，提升检索稳定性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳QA的RAG方案要么依赖KG构建、LLM生成节点摘要实现分层/图索引，离线成本极高；要么靠LLM迭代规划检索，查询延迟高，难以落地大规模业务场景。

### 方法关键点
- 离线索引：用Matryoshka嵌入模型编码文档，HDBSCAN做层次聚类构建DAG索引，上层粗聚类节点存储低维嵌入前缀，下层文档节点保留全量嵌入，无需构建KG或调用LLM生成节点摘要
- 在线检索：自顶向下贪心遍历DAG，每一层匹配时query截断到对应层嵌入维度，大幅降低相似度计算成本
- 漂移控制：动态权重β_t随检索进度提升原始query占比，锚定搜索目标缓解query漂移
- 实体感知优化：按当前新增实体数动态分配每轮检索配额，文档重排融合语义相似度与实体Jaccard相似度，提升多跳匹配精度

### 关键实验
在HotpotQA、2WikiMultiHopQA、MuSiQue三个多跳基准上对比7个SOTA基线（含GraphRAG、LightRAG、RAPTOR等），EM/F1全数据集最优；Recall@5比NaiveRAG最高提升13.37%；索引成本比HippoRAG降低99.6%以上；查询延迟比FAISS flat索引降低35%~47%。

### 核心结论
嵌入策略与索引结构协同设计，可在不损失效果的前提下大幅压缩RAG的索引和查询成本，无需依赖KG或额外LLM调用

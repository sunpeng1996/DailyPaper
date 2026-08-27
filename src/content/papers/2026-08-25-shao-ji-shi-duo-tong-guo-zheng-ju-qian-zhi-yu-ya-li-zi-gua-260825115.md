---
title: 'Less can be More: Relieving RAG Bottlenecks via Evidence Frontloading and
  Pressure-Adaptive Budgeting'
title_zh: 《少即是多：通过证据前置与压力自适应预算缓解RAG瓶颈》
authors:
- Weibin Cai
- Reza Zafarani
affiliations:
- Syracuse University
arxiv_id: '2608.25115'
url: https://arxiv.org/abs/2608.25115
pdf_url: https://arxiv.org/pdf/2608.25115
published: '2026-08-25'
collected: '2026-08-27'
category: RAG
direction: RAG效率优化 · 动态重排策略
tags:
- RAG
- reranking
- evidence recall
- latency optimization
- multi-hop QA
one_liner: 提出无训练PACE框架，动态调整RAG重排预算，高负载下降p95延迟同时提升召回
practical_value: '- 电商导购Agent、搜索问答类RAG系统遇到高QPS重排瓶颈时，可直接复用PACE的证据前置策略：基于边际证据覆盖的贪心重排无需额外训练，且有(1-1/e)的最优近似保证，小重排预算下也能保留核心证据召回

  - 高负载RAG在线服务无需固定重排topK阈值，可照搬压力自适应预算策略：实时对比重排器、LLM的队列积压情况动态调整重排数量，可大幅降低p95延迟同时不跌业务效果

  - 多条件商品检索/推荐场景（如用户搜索“敏感肌可用的防晒品牌旗下保湿面霜”），可借鉴软锚点相关性修正方法，兼顾query直接匹配和跨商品/文档的关联证据，提升多跳需求的召回准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG优化大多聚焦下游LLM生成侧的加速、上下文压缩，但RAG是端到端系统，瓶颈会随QPS、重排预算动态变化：高QPS或大重排预算下，上游重排会成为核心瓶颈，单纯降低重排预算会丢失关键证据、降低召回，如何动态平衡重排效率和证据召回是未解决的痛点。

### 方法关键点
- 提出无训练的PACE框架，包含**证据前置**和**压力自适应预算**两个核心模块，无需微调任何模型即可落地
- 证据前置：将检索返回的候选按边际证据覆盖度贪心排序，同时引入软锚点机制修正相关性，既优先query直接相关文档，也保留能形成证据链的关联文档；该目标为单调次模函数，贪心选择可获得(1-1/e)的最优近似保证
- 压力自适应预算：实时统计重排器、LLM的队列积压时间，重排压力大于LLM时动态下调重排预算，否则用最大预算，优先保证高负载下的系统稳定性

### 关键结果
在3个多跳QA数据集（HotpotQA、MuSiQue、2WikiMultiHopQA）上对比MMR、Dartboard等主流无训练重排基线：
1. 小重排预算下，PACE在D=20的证据召回与基线D=40相当，仅需一半的重排算力
2. 高QPS重负载场景下，p95端到端延迟比固定D=100的基线低70%以上
3. 自适应缩减半重排预算的情况下，PACE的top5证据召回比全预算基线高20%

### 核心结论
RAG系统的重排预算并非越大越好，只要候选排序的证据密度足够高，更少的重排数量就能获得更高的最终召回，即“少即是多”

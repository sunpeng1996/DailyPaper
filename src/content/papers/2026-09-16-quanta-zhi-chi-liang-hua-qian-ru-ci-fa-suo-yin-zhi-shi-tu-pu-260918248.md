---
title: 'Quanta: A Self-Contained Python Library for Hybrid Retrieval over Quantised
  Embeddings, Lexical Indexes, and Knowledge Graphs'
title_zh: Quanta：支持量化嵌入/词法索引/知识图谱的混合检索Python库
authors:
- Ioannis E. Livieris
affiliations:
- Novelcore, Athens
- University of Peloponnese
arxiv_id: '2609.18248'
url: https://arxiv.org/abs/2609.18248
pdf_url: https://arxiv.org/pdf/2609.18248
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: RAG混合检索 · 量化向量+图谱扩召回优化
tags:
- Hybrid_Retrieval
- Quantized_Embedding
- RAG
- Knowledge_Graph
- BM25
one_liner: 开源单进程Python混合检索库，统一融合量化向量、BM25、知识图谱三类信号
practical_value: '- 混合检索融合优先选用RRF而非跨信号分数归一化，规避向量、BM25、结构信号分数分布不一致问题，无逐场景调优时默认效果更稳，适合中小业务快速落地

  - 知识图谱用于召回扩展而非直接排序的设计可复用：先从初始召回topK取种子做限定跳数遍历扩候选，再将新候选塞回向量/BM25重打分，既利用结构关联补召回，又避免结构分干扰内容相关性，适配电商关联推荐、领域知识库检索等场景

  - 4-bit量化嵌入+进程内精确检索方案适合小规模垂直场景（比如商品详情检索、客服知识库），无需单独部署向量数据库，内存占用仅为float32的1/8，检索延迟低于10ms，大幅降低部署成本

  - 检索前先解析元数据过滤条件得到合法ID白名单，再在白名单范围内做向量搜索，而非检索后过滤，可直接复用规避高选择性过滤条件下的召回率损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG系统的混合检索通常需要对接向量数据库、全文检索引擎、图数据库3-4套独立系统，集成成本高；不同检索信号的分数归一化依赖逐场景调优，知识图谱的结构信号要么独立检索要么直接参与排序，很容易干扰内容相关性，中小场景部署门槛极高。

### 方法关键点
- 单进程统一封装三类检索能力：4-bit量化向量检索（基于TURBOVEC实现，内存仅为float32的1/8，进程内精确搜索无需额外ANN服务）、Tantivy BM25全文检索、知识图谱遍历，所有组件都有null实现，可从纯向量检索逐步迭代增加信号，无需修改核心代码
- 信号融合采用加权RRF（倒数秩融合），无需对不同信号的分数做归一化，无逐场景调优的情况下默认效果优于CombSUM类分数融合方案
- 知识图谱仅作为候选扩展模块：先做初始内容召回得到topK种子，做限定跳数的BFS遍历扩展候选，再将新候选通过ID白名单塞回向量索引重打分，图谱仅决定哪些候选进入排序池，不直接参与打分，避免结构信号干扰内容相关性
- 原生支持元数据前置过滤：先解析过滤条件得到合法ID白名单，再在白名单范围内做向量搜索，避免后过滤导致的召回损失

### 关键结果数字
临床知识图谱部署验证：100万条768维向量4-bit量化仅占366MiB内存；2跳图谱扩展可将候选池扩大3.3倍，可召回更多关联内容（比如心衰query召回共病的糖尿病相关内容）；纯内容检索延迟7-9ms，开启图谱扩展后延迟44-115ms，占Agent整轮响应（19-32s）的占比不到5%；6个临床问题回答无错误。

### 核心结论
混合检索要明确区分候选生成和相关性排序的边界，知识图谱等结构信号应该优先用于扩大候选池而非直接干预排序，无调优场景下RRF是比分数归一化更鲁棒的融合方案

---
title: 'Fidelity Synopses: Pre-Execution Plan Selection for Approximate Vector Search'
title_zh: 保真概要：近似向量搜索的预执行计划选择方法
authors:
- Adithya Ramanatha
- Sanskar S. Singh
- Maya Ramanath
affiliations:
- NIT Calicut
- IIT Delhi
arxiv_id: '2610.41407'
url: https://arxiv.org/abs/2610.41407
pdf_url: https://arxiv.org/pdf/2610.41407
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 向量检索优化 · ANN动态配置选择
tags:
- ANN Search
- Vector Database
- Query Optimization
- Embedding Retrieval
- Cost Efficiency
one_liner: 提出基于嵌入空间分区的保真概要，为每ANN查询动态选最优配置，静态部署成本中位数降至0.72倍
practical_value: '- 向量召回层可直接复用思路：离线统计不同ANN配置/搜索参数在各嵌入空间分区的召回精度，线上按query所属分区动态选最低成本配置，在不降低召回效果前提下降低检索延迟、提升QPS

  - 跨模态检索场景（多模态商品搜图、文搜图）收益最高：静态配置通常为小部分难查询做冗余预留，该方法可让大部分简单查询用低成本配置，实测成本最高可降80%

  - 可轻量化落地：无需新增索引，仅需对现有同索引的不同搜索参数（如HNSW的efSearch、IVF的nprobe）做离线统计，即可实现单索引内的动态参数调优，无额外内存开销

  - 线上开销可忽略：仅新增一次最近地标查询，批处理下单查询开销仅21~32μs，对检索链路延迟影响极小'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前向量检索系统普遍采用离线选定的单一ANN索引配置服务所有查询，为满足小部分难查询的保真要求，不得不为所有查询付出冗余的算力/时间成本，跨模态检索场景下这种资源浪费尤为突出，理论最优的逐查询动态选配置可让成本中位数降至静态部署的一半。

### 方法关键点
- 离线阶段：对语料嵌入做球形k-means聚类生成地标，将嵌入空间划分为多个单元格；用采样查询跑一次精确检索，统计每个单元格下各ANN配置的平均保真、保真达标率直方图，构建轻量化保真概要
- 在线阶段：先匹配待处理向量的最近地标对应单元格，读取该单元格下所有候选配置的保真统计，通过预算规则（配置成本+未达标惩罚）选择最优配置执行，全程无在线精确检索开销

### 关键实验结果
在5.8M条LAION多模态数据集上，用4种主流嵌入模型、9种ANN配置（含HNSW、IVFPQ、O-IVFPQ三个系列）测试，对比同保真要求下的静态配置基线：
1. 16种模型+查询方向组合下均实现成本下降，中位数降至静态配置的0.72倍，跨模态场景最高降至0.2倍
2. 批处理下单查询新增开销仅21~32μs，若仅在单索引内动态调整搜索参数则无额外内存开销
3. 整体保真达标率与静态配置完全对齐，无明显检索效果损失

### 核心结论
向量检索的难度在嵌入空间上存在局部平滑性，利用该特性做分区级的统计优化，可在不损失检索效果的前提下大幅降低资源开销。

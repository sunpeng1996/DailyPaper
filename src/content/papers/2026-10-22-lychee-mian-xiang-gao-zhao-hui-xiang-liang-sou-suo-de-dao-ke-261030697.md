---
title: 'Lychee: Certified Screening of Inverted Lists for High-Recall Vector Search'
title_zh: Lychee：面向高召回向量搜索的倒排表可信筛选框架
authors:
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2610.30697'
url: https://arxiv.org/abs/2610.30697
pdf_url: https://arxiv.org/pdf/2610.30697
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 高召回向量检索 · IVF索引优化
tags:
- Vector Search
- IVF Index
- High Recall
- GPU Acceleration
- Tensor Core
one_liner: 基于倒排列表锚点与Tensor Core可信筛选，相同召回下IVF高召回向量检索最高提速185倍
practical_value: '- 高召回向量召回/RAG场景可直接复用可信筛选逻辑，将IVF全量精确打分改为先Tensor Core低维投影初筛，仅对幸存向量计算精确距离，大幅降低内存开销、提升QPS

  - 可迁移倒排列表本地锚点阈值设计，无需全局采样锚点，仅从当前查询的近邻倒排列表取锚点计算阈值，能大幅减少初筛幸存数，降低后续计算量

  - GPU工程实现可复用批量查询路由分组思路，将探测同个倒排列表的请求归为一组，最大化Tensor Core算力利用率，避免小批次算力浪费

  - 亿级大规模向量检索场景可采用「低维投影+锚点存GPU、全量向量存主机内存」的分级存储方案，在损失极小吞吐的前提下大幅降低GPU显存占用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高风险场景（风控、医疗、RAG、电商向量召回）要求召回率达0.999~0.9999，传统IVF索引为提召回需探测更多倒排列表，吞吐量与探测列表数成反比下降；图索引在高召回区间吞吐量饱和，量化索引需全量向量重排，无法兼顾高召回、高吞吐、低显存开销。
### 方法关键点
- 倒排列表本地锚点阈值：从查询探测的近邻倒排列表取锚点，计算锚点top-k精确距离作为筛选上界，保证真实top-k向量不会被初筛过滤
- Tensor Core路由初筛：批量查询按探测的倒排列表分组，用低维投影的可信下界在Tensor Core上批量初筛，仅保留下界低于阈值的候选
- 有序边界验证：初筛幸存向量按可信下界升序排序，逐个计算精确距离，当下界超过当前top-k最大距离时提前终止，大幅减少精确计算量
### 关键实验
在11个百万到十亿级向量数据集上对比10个CPU/GPU基线（IVF-Flat、CAGRA、IVF-PQ、ScaNN等）：相同召回下，200个探测列表时比cuVS IVF-Flat提速9.7~117倍，Deep-100M数据集召回0.9997时提速65倍，四GPU下十亿级BIGANN-1B数据集召回0.9999时提速44.5倍，最高提速达185倍，且完全不损失IVF-Flat的召回率。
### 核心结论
高召回IVF检索的瓶颈是倒排列表全量精确扫描，通过可信下界初筛+提前终止可将全量精确读数量从数十万降至百级，实现数量级吞吐提升

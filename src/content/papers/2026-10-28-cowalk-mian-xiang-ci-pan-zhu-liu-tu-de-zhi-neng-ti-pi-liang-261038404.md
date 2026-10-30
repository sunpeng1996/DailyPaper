---
title: 'CoWalk: Cooperative Walks for Agentic Batch Queries on Disk-Resident Graphs'
title_zh: CoWalk：面向磁盘驻留图的智能体批量查询协同游走框架
authors:
- Qiao Liang
- Zhiguang Chen
- Yue Yu
- Nong Xiao
affiliations:
- Sun Yat-sen University
- Pengcheng Laboratory
arxiv_id: '2610.38404'
url: https://arxiv.org/abs/2610.38404
pdf_url: https://arxiv.org/pdf/2610.38404
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: Agent 批量向量检索性能优化
tags:
- ANN
- Vector Retrieval
- Agent
- Graph Index
- SSD
- RAG
one_liner: 实现语义相关批量向量查询的协同游走，大幅降低磁盘ANN检索的I/O与计算开销
practical_value: '- 电商Query改写、HyDE生成的批量同义向量召回场景，可直接复用CoWalk的I/O去重、跨查询精确距离预计算逻辑，单批次召回
  latency 降低30%以上，I/O开销降低60%+

  - 智能导购、Deep Research类Agent的批量子任务召回，可复用单线程多查询异步调度逻辑，在latency持平的前提下将检索吞吐提升3~7倍，检索成本降低2/3以上

  - 批量向量检索架构选型优先选择图索引而非聚类索引，且无需跨查询共享图邻居，仅共享读取页面与精确距离即可获得最优投入产出比'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM Agent、Query改写、GRPO训练、HyDE等场景会生成大量同语义的批量向量查询，现有磁盘驻留图ANN系统独立处理每个查询，31%~67%的I/O请求为重复读取；仅增加批量页面缓存仅能提速1.1~1.2倍，因为未改变单查询游走路径与距离计算量，CPU计算仍是核心瓶颈。
### 方法关键点
- 基于磁盘Vamana图索引，单线程运行批量内所有查询的独立游走逻辑，每个查询保留私有候选列表，游走规则与单查询检索完全一致
- 批量内共享I/O请求：同一页面仅读取1次，所有请求该页面的查询共享读取结果，消除重复I/O
- 跨查询共享精确距离：每个读取到的节点仅计算1次全量批量查询的精确距离，存入共享表供所有查询最终排序使用，减少重复距离计算
- 单线程异步调度所有I/O请求，优先处理先返回的页面，最大化CPU与I/O重叠效率，不跨查询共享图邻居避免无效计算
### 关键实验
在OpenResearcher、QuAC+CANARD、NarrativeQA三个真实Agent检索数据集上对比PipeANN、GLRU两个最强基线，recall@10=0.95时，单线程批量查询 latency 降低1.6~1.9倍，I/O次数降低2.8~6.9倍；服务端部署时吞吐提升3.0~6.9倍，每美元查询量提升2~7倍，latency仅为基线的0.74~1.08倍。
> 最值得记住的结论：针对语义相关的批量向量检索，仅共享I/O和精确距离的轻量化协同设计，远比重构检索路径、共享中间结果的复杂设计性价比更高

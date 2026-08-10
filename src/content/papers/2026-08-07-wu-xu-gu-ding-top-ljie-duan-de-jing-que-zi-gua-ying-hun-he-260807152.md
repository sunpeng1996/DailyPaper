---
title: Exact Adaptive Hybrid Retrieval Without Fixed Top-L Cutoffs
title_zh: 无需固定Top-L截断的精确自适应混合检索方法
authors:
- Chunran Zhang
affiliations:
- Southwest Jiaotong University
arxiv_id: '2608.07152'
url: https://arxiv.org/abs/2608.07152
pdf_url: https://arxiv.org/pdf/2608.07152
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: RAG混合检索 · 无截断自适应召回
tags:
- Hybrid Retrieval
- RAG
- Rank Fusion
- Top-K Retrieval
- Vector Database
one_liner: 提出EAHR自适应混合检索框架，无需预设Top-L截断即可返回与全列表RRF完全一致的Top-K结果
practical_value: '- 混合召回场景可借鉴自适应深度判定逻辑，无需人工调优各召回通路固定Top截断阈值，避免阈值在query/语料变化时失效，保证召回结果一致性

  - 可复用PVS稠密检索、PBM稀疏检索的可恢复精确排序生成方案，适配增量拉取召回结果的需求，降低大语料下的检索计算开销

  - RAG系统召回层可直接落地EAHR替代原有固定Top-L截断的RRF融合，平均延迟最高可降30倍，同时保证召回结果与全量融合完全一致

  - 若业务场景下多召回通路排序相关性高（如电商同query下稠密稀疏召回重叠度高）收益更明显，通路强负相关时收益有限，可做分query路由'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统混合检索普遍采用固定Top-L截断各通路结果后做RRF融合的方案，截断阈值同时决定检索质量与计算成本。但固定阈值无法适配不同query的排序差异和语料更新，即使取较大L也常无法复现全列表融合的Top-K排序，甚至丢失正确候选，阈值调优成本极高。

### 方法关键点
- 定义全列表加权RRF得到的有序Top-K为固定检索目标，各通路检索深度作为请求级内部状态，无需预设Top-L截断
- PVS稠密检索生成器：基于单向量标量量化的得分区间判定，仅区间无法区分排序时才计算原始float32得分，支持断点续取精确排序
- PBM稀疏检索生成器：基于倒排块最大值的上界剪枝，优先扩展得分上界最高的块，支持增量输出精确排序
- 融合层实时计算未读位置的贡献上界，仅当已读结果无法确定Top-K的成员和顺序时才请求下一批结果，直到Top-K完全确定或通路耗尽

### 关键实验
在5个公开检索数据集、5个TREC-COVID时序语料快照上测试，对比固定Top-L截断、全量融合、全量批处理基线：
1. EAHR在150组query-快照组合下100%复现全列表加权RRF的Top-20结果
2. 暖缓存场景下，全量批处理平均延迟是EAHR的23.35倍（TREC-DL 2019）、30.28倍（TREC-DL 2020）
3. 仅当不同通路排序强负相关时，EAHR可能慢于全量批处理，但结果仍完全一致

### 核心结论
固定Top-L截断同时绑定了检索结果语义和执行成本，自适应检索可解耦结果正确性与性能优化，无需为了性能牺牲召回结果一致性。

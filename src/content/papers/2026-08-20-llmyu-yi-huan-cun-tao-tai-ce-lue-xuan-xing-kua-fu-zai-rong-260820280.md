---
title: Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads,
  Capacities, and Encoders
title_zh: LLM语义缓存淘汰策略选型：跨负载、容量、编码器的系统评估
authors:
- Yash Kulkarni
- Shubham Harkare
- Arvind Suresh Yogesh Babu
affiliations:
- University of Michigan
arxiv_id: '2608.20280'
url: https://arxiv.org/abs/2608.20280
pdf_url: https://arxiv.org/pdf/2608.20280
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: LLM语义缓存 · 淘汰策略选型评估
tags:
- semantic caching
- cache eviction
- LLM serving
- hit rate
- embedding
one_liner: 统一协议评估7种LLM语义缓存淘汰策略，证明LFU为最优简单基线，无策略较其提升超0.041pp
practical_value: '- 搭建LLM服务、RAG、Agent语义缓存时，默认选择LFU作为淘汰策略即可，复杂语义感知策略提升可忽略，反而会带来5-8倍的额外计算开销

  - 语义缓存的距离阈值不可跨embedding模型直接复用，必须针对所用编码器的向量分布做分位数重校准，避免出现命中率虚高或几乎无命中的问题

  - 不要仅用原始命中率评估缓存效果，需新增质量校验环节：通过LLM judge或人工标注统计答案可复用的有效命中率，尤其电商咨询、客服等场景相似query答案往往不可复用

  - 向量索引优先选择HNSW，相比精确Flat搜索可实现34倍速度提升，仅损失1.1pp的Recall@1，为Pareto最优选择'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM语义缓存的淘汰策略缺乏统一测试基准，不同研究的结论互相矛盾，没有通用选型指导；同时行业普遍只关注原始命中率，忽略embedding编码器差异、答案可复用性对缓存实际效果的影响，导致上线效果远低于预期。
### 方法关键点
- 搭建统一测试框架CLEVER，对齐语料顺序、索引结构、命中阈值、缓存容量等变量，确保策略对比公平
- 覆盖7种主流淘汰策略：FIFO、LRU、LFU、ARC、GDSF、流式SISO、语义冗余策略
- 测试维度包括3类数据集（LMSYS、QQP、MOSS）、3种缓存容量（总query量的10%/20%/30%）、2种常用编码器（MiniLM、gte-base）
- 新增质量校准环节，用Llama-3.1-8B作为judge评估命中的query对是否满足答案可复用
### 关键结果
- 所有测试场景下无策略较LFU的命中率提升超过0.041pp，而FIFO、流式SISO在10%低容量场景下最多比LFU低8.67、8.55pp，且流式SISO开销是LRU的2.8-5.2倍
- 相同数值阈值跨编码器迁移完全失效，MiniLM的阈值用于gte-base时会出现100%的虚高命中率
- MiniLM默认阈值下，LMSYS、QQP的原始命中率为51-60%，但质量校准后的有效命中率仅为1.1-2.2%
- HNSW索引相比精确Flat搜索实现34倍速度提升，仅损失1.1pp Recall@1，为Pareto最优
### 核心结论
LLM语义缓存优化优先级远高于淘汰策略的三个环节是：选型匹配业务的embedding模型、校准答案可复用的命中阈值、扩容缓存容量，淘汰策略直接用LFU即可

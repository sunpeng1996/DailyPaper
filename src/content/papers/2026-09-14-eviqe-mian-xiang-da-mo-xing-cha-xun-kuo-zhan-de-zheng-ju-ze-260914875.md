---
title: 'EviQE: Evidence Selection for LLM-Based Query Expansion'
title_zh: EviQE：面向大模型查询扩展的证据选择方法
authors:
- Hai Son Le
- Amin Bigdeli
- Shirin Seyedsalehi
- Morteza Zihayat
- Ebrahim Bagheri
affiliations:
- Toronto Metropolitan University
- University of Waterloo
- University of Toronto
arxiv_id: '2609.14875'
url: https://arxiv.org/abs/2609.14875
pdf_url: https://arxiv.org/pdf/2609.14875
published: '2026-09-14'
collected: '2026-09-16'
category: QueryRec
direction: 查询扩展 · 证据选择
tags:
- Query Expansion
- Evidence Selection
- Information Retrieval
- LLM
- Reranking
one_liner: 聚合多改写器召回的文档并做相关性证据选择，提升LLM查询扩展的检索效果
practical_value: '- 电商搜索query改写场景可直接复用多改写器互补思路：无需纠结选单一最优改写策略，将不同改写方法召回的商品/内容聚合后筛选证据，可提升相关结果覆盖率，召回率最高可提15%+

  - 证据选择阶段优先用轻量LLM judge做相关性打分，比RRF、频次投票等无监督方法增益更稳定，可直接对接现有query扩展pipeline，无需改动底层召回排序逻辑

  - 无需部署多轮迭代改写流程，只要筛选到高质量的证据文档，单轮扩展效果就优于多轮迭代，可大幅降低推理延迟，适配高并发的搜索/推荐场景

  - 多改写器组合无需贪多，4-6个主流改写策略（如CSQE、Query2Doc等）即可覆盖95%以上的增益，继续新增策略边际收益极低，可有效控制算力成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM-based查询扩展工作大多聚焦改写生成逻辑的优化，普遍忽略了生成时依赖的上下文证据文档的选择策略；不同改写策略对同一查询召回的文档互补性极强，仅选用单一改写策略会丢失大量相关文档，而多轮迭代扩展的增益本质上也来自更好的证据获取而非多次改写本身，因此将证据选择从生成流程中解耦优化能带来显著效果提升。
### 方法关键点
- 提出EviQE框架，将证据选择与生成完全解耦：先运行多个独立改写器得到不同查询变体，分别召回TopK文档后去重聚合为候选池
- 提供三类证据选择策略：频次投票（被越多改写器召回的文档得分越高）、RRF（融合跨来源排序位置打分）、LLM-Score（用LLM judge直接评估文档与原查询的相关性打分）
- 仅做单轮生成：选择Top-B最高得分文档喂给固定LLM生成扩展查询，拼接原查询后执行最终召回
### 关键实验
在3个TREC DL、5个BEIR基准数据集上测试，对比冷启动ThinkQE、单源改写、最优单一改写器等基线；采用LLM-Score选择策略时，相比冷启动基线，TREC DL平均nDCG@10提升4.8%，BEIR平均提升3.2%，所有数据集均实现正向增益；仅搭配4个主流改写器就能拿到95%以上的增益，多轮迭代扩展在获取到优质证据后效果反而出现下降。

LLM查询扩展的效果瓶颈很大概率不在生成逻辑，而在喂给模型的证据质量，优质单轮扩展效果远胜低质量多轮迭代。

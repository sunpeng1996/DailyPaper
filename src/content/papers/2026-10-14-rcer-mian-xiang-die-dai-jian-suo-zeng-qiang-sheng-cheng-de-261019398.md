---
title: 'RCER: Reconstructing Cross-Evidence Relations for Iterative Retrieval-Augmented
  Generation'
title_zh: RCER：面向迭代检索增强生成的跨证据关系重构方法
authors:
- Linyao Zheng
- Xuhang Shi
- Zhifang Mao
- Xiuquan Hou
- Sai Zhou
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2610.19398'
url: https://arxiv.org/abs/2610.19398
pdf_url: https://arxiv.org/pdf/2610.19398
published: '2026-10-14'
collected: '2026-10-15'
category: RAG
direction: 迭代RAG优化 · 跨证据推理
tags:
- Iterative RAG
- Cross-evidence Reasoning
- Multi-hop QA
- Information Retrieval
- LLM Reasoning
one_liner: 提出基于跨证据关系重构的迭代RAG框架，在多跳复杂QA任务上超越现有SOTA基线
practical_value: '- 迭代检索query生成逻辑可复用：电商导购Agent处理多条件复杂咨询时，可参考跨轮关系识别动态分解子问题，迭代检索商品属性、用户评价等多源信息，避免单次检索漏召回

  - 跨证据组合推理trick可迁移：生成式推荐场景融合用户历史、商品属性、实时活动信息时，可先预计算跨源实体对齐关系，再组合生成推荐理由，提升可信度

  - 效率优化方案可直接落地：多轮RAG系统可复用「跨证据分析+联合选段+提前终止」管线，实测降低45%+ token消耗、P95 latency降20%+，适配线上高并发场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有迭代RAG仅累计检索到的事实，无法动态挖掘跨文档的实体对应关系、推理依赖，导致多跳推理任务中容易漏召回关键证据、无法整合零散信息生成准确答案。

### 方法关键点
- 跨轮关系证据获取：每轮联合分析累计的所有检索段落，识别实体对齐、关系依赖，动态分解问题生成下一轮检索query，支持query重复时提前终止
- 推理上下文重构：检索结束后独立分析全量候选池，联合选择互补段落，预生成跨证据推理关联
- 跨证据组合推理：融合选中段落与预生成的跨证据关联，对齐实体、组合关系推导答案

### 关键实验
在HotpotQA、2WikiQA、MuSiQue等5个复杂QA数据集上测试，base模型用Qwen3.8-27B，对比GraphRAG、IRCoT、RetroRAG等12个SOTA基线；平均多跳EM提升2.83、F1提升3.06个点，P95 latency比RetroRAG低20.2%、token消耗降45.73%，适配9B小模型时仍领先次优基线2.06个F1点。

迭代RAG的核心瓶颈不是检索不到足够的证据，而是无法挖掘跨证据的隐式关联来整合信息、指导后续检索。

---
title: Bridging Static and Agentic RAG for Taiwanese Historical Question Answering
title_zh: 融合静态与Agentic RAG的台湾历史问答优化方法研究
authors:
- Kai-Hsin Chen
- Wei-Yu Chen
- Xuanjun Chen
- Jyh-Shing Roger Jang
affiliations:
- National Taiwan University
arxiv_id: '2609.23056'
url: https://arxiv.org/abs/2609.23056
pdf_url: https://arxiv.org/pdf/2609.23056
published: '2026-09-19'
collected: '2026-09-22'
category: RAG
direction: RAG范式对比与融合优化
tags:
- RAG
- Agentic RAG
- Retrieval Orchestration
- Answer Selection
- Question Answering
one_liner: 控制变量对比静态与Agentic RAG性能，提出事后选择器恢复60.34%的最优性能空间
practical_value: '- 不要盲目迷信Agentic RAG的性能增益，静态RAG在多数场景下是成本更低、可信度更高的基线，可优先作为业务落地的基础方案，避免不必要的多轮推理开销

  - 对于知识密集型的电商咨询、商品导购类Agent场景，可部署双RAG管线+事后选择器的架构，利用两类RAG的互补性提升整体效果，可恢复60%+的最优性能空间，ROI可观

  - Agentic RAG的增益核心来自查询重定向而非单纯多轮召回，设计检索逻辑时可重点优化查询改写的多样性，而非盲目增加召回轮次，降低无效开销

  - 业务系统选型不要只看聚合指标，要拆解单请求维度的性能差异，挖掘不同方案的互补性，通过路由/选择机制叠加的增益远高于单方案优化的收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有研究普遍预设Agentic RAG的自适应检索能力优于静态RAG，但缺乏控制变量下的公平性能对比，两类范式的互补性未被充分挖掘。历史问答这类知识密集、对答案可信度要求高的场景，迫切需要明确不同RAG架构的适用边界与融合路径。

### 方法关键点
- 共享混合检索基座：两类RAG共用相同的稠密（Qwen3-Embedding+Qdrant）+稀疏（BM25+Elasticsearch）召回、RRF融合、BGE重排链路，仅检索编排逻辑不同
- 检索编排差异：静态RAG一次生成多查询，召回Top15段落直接输入生成器；Agentic RAG通过LLM Agent自主控制检索时机与查询改写，每次调用返回Top5段落，支持多轮检索
- 事后选择器：输入原始问题、两类RAG的返回结果及其引用证据，通过GPT-5.5做成对对比，正反序校验一致时选择更优结果，否则返回平局

### 关键实验
数据集覆盖120道开放题的明清台湾行政档案数据集、102道客观题的台湾民俗文化词条数据集。核心结果显示：两类RAG的聚合性能无统计显著性差异，但70.83%的问题上表现不同，胜负基本持平；Oracle逐题选择最优结果比单最优管线得分高0.2417；事后选择器可恢复60.34%的Oracle性能空间，比Agentic RAG得分提升0.1458，提升统计显著。

### 核心结论
Agentic RAG不是静态RAG的升级替代品，而是互补的检索范式，挖掘单请求维度的性能差异做路由/选择，带来的增益远高于单架构的极致优化

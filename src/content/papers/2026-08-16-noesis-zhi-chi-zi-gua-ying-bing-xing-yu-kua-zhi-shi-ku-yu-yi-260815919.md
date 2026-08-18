---
title: 'Noesis: Bidirectional Graph-RAG with Adaptive Parallelism and Cross-Knowledge-Base
  Semantic Discovery'
title_zh: Noesis：支持自适应并行与跨知识库语义发现的双向Graph-RAG
authors:
- Nicola Cogotti
affiliations:
- Alpha Cogs
arxiv_id: '2608.15919'
url: https://arxiv.org/abs/2608.15919
pdf_url: https://arxiv.org/pdf/2608.15919
published: '2026-08-16'
collected: '2026-08-18'
category: RAG
direction: Graph-RAG 架构与性能优化
tags:
- Graph-RAG
- AIMD
- MoE Quantization
- Cross-KB Routing
- Bidirectional Traversal
one_liner: 提出解耦双向Graph-RAG架构，解决语义碎片化、并行僵化、跨域隔离三大落地痛点
practical_value: '- 双向图遍历可迁移到电商知识图谱构建：用语义边界切片+前向图反馈上下文+后向低度数节点重连，解决长商品详情、用户行为序列的跨chunk语义丢失问题，大幅提升图谱密度

  - AIMD自适应并发控制器可直接复用在RAG ingestion流水线：无需手动调优并行度，适配从消费级GPU到集群的异构硬件，避免OOM，实测可提升大规模商品/内容知识库入库速度23倍

  - Mesh跨KB路由可用于多域导购Agent：无需合并商品、评价、售后等独立知识库，自动发现跨域隐式关联（如用户痛点→对应商品功能），路由延迟<2ms，满足实时检索需求

  - Moēsis域感知MoE量化适合端侧/小GPU部署场景：基于业务域样本的专家激活频率做差异化量化，12GB消费级GPU即可运行35B MoE模型，prompt处理速度提升6.3倍，降低部署成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Graph-RAG落地存在三大核心瓶颈：静态分块切断长文档跨段语义关联，导致图谱碎片化无法支撑多跳推理；入库流水线并行度固定，要么出现OOM崩溃要么硬件利用率不足；多域部署要么合并知识库导致检索精度下降，要么需要用户手动选择知识库，无法发现跨域隐式关联。

### 方法关键点
- 双向图遍历：前向Pass模拟人类阅读的衰退记忆机制，按语义边界切片文档，每步带入相关历史节点做上下文；后向Pass重连早期低度数节点与后期语义相关节点，补全长距离依赖
- AIMD并发控制器：借鉴TCP拥塞控制的增/减机制，自适应调整文档级并行度，Redis持久化状态支持崩溃恢复，兼容本地GPU、云API等任意推理后端
- Moēsis域感知MoE量化：先基于业务域样本做激活profiling区分冷热专家，分层做差异化量化，采用只升不降的GPU放置策略减少CPU-GPU传输，支持域切换时从全精度模型重新量化避免精度损失
- Mesh跨KB路由：每个知识库预计算层级语义指纹，查询时多策略路由到相关知识库，运行时基于自适应Natural Break阈值发现跨域隐式关联，全在进程内执行延迟<2ms

### 关键实验结果
13.4MB语料入库速度提升23倍，全程0 OOM；12GB消费级GPU上35B MoE模型prompt处理速度提升6.3倍；HotpotQA 1000条多跳问答任务上，用35B本地模型建图的EM达59.5，比GraphRAG高27.8，仅比用GPT-4o建图的HopRAG低2.5 EM；193页长文档的长距离因果边提取源文验证精度达90%。

**最值得记住的一句话**：80%的QA性能贡献来自检索架构，仅20%来自大模型推理能力，优质的Graph-RAG架构可以让2.3B小模型达到GPT-4o级别的稠密检索效果。

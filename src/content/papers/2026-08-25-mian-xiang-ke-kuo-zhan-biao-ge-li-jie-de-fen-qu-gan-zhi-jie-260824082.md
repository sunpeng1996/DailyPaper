---
title: 'PARTAB: Partition-Aware Reasoning with Structured Evidence for Scalable Table
  Understanding'
title_zh: 面向可扩展表格理解的分区感知结构化证据推理框架PARTAB
authors:
- Md Mahadi Hasan Nahid
- Davood Rafiei
affiliations:
- University of Alberta
arxiv_id: '2608.24082'
url: https://arxiv.org/abs/2608.24082
pdf_url: https://arxiv.org/pdf/2608.24082
published: '2026-08-25'
collected: '2026-08-26'
category: Reasoning
direction: 大语言模型表格推理 · 结构化分区
tags:
- Table Reasoning
- LLM Reasoning
- Context Optimization
- Semantic Partition
- Evidence Retrieval
one_liner: 提出分层语义分区+结构化证据选择的LLM表格推理框架，提升大表格推理精度且大幅降低上下文开销
practical_value: '- 处理电商大尺寸商品属性表、用户行为报表、运营活动效果表时，可复用「语义列分组+固定行数分块+row_id跨块关联」的结构化拆分方法，避免全表加载的上下文冗余与注意力稀释问题

  - 搭建表格类RAG系统（比如商家经营分析Agent、商品合规规则查询Agent）时，可借鉴先选列组再选行块的分层检索策略，比纯TF-IDF相似度检索的证据召回率更高，尤其适合多维度组合查询场景

  - 性能敏感的表格推理场景可优先选用LLM驱动的分区选择策略，相比全表推理最多降低77%的上下文Token量，大表难例上推理精度最高提升34个百分点

  - 做复杂报表分析Agent时可新增路由逻辑：将需要全局聚合的查询路由到SQL执行引擎，将语义校验/事实核对类查询走分区推理，兼顾计算准确率与推理灵活性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM在表格推理任务上的效果会随表格尺寸、复杂度提升显著下降，无关上下文易引发注意力稀释、lost-in-the-middle、行列绑定错误等问题；现有全表推理方法上下文开销过高，单视图剪枝方法易丢失关键行列关联信息，无法兼顾大表格推理的精度与可扩展性。

### 方法关键点
- 预处理阶段为所有表格新增row_id作为跨分区统一关联键，避免不同分区信息无法对齐
- 分区构建：先将列按语义划分为多个相干组，再对每个列组按固定行块（默认5行）拆分，生成多个独立可寻址的结构化分区
- 分层选择：先基于问题分析结果筛选相关列组，再通过LLM从选中列组中筛选相关行块，仅将选中分区传给下游答案生成
- 执行阶段明确约束LLM仅使用选中分区内容、通过row_id关联跨分区信息，禁止调用外部知识

### 关键结果
在WikiTableQuestions（表格问答）、TabFact（事实校验）、TableBench（复杂表格推理）三个基准上测试，对比Chain-of-Table、TableMaster等SOTA方法：WikiTableQuestions EM达79.31，超出SOTA 1.18个点；TabFact准确率达90.48，超出SOTA 0.36个点；大/宽表难例上相比同算力全表推理最高提升34.04个百分点，上下文Token量平均降低75%以上。

### 最值得记住的一句话
表格推理优化的核心不是单纯剪枝上下文，而是通过结构化分区保留行列关联关系，实现精准证据定位。

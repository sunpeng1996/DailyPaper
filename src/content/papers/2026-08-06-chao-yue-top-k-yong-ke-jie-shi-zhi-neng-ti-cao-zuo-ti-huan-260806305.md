---
title: 'Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations'
title_zh: 超越Top-K：用可解释智能体操作替换黑盒检索
authors:
- Sagar Tamang
- Ayush Vyas
- Tabarakul Hazarika
affiliations:
- Indian Institute of Technology Patna
- TwoSpoon
arxiv_id: '2608.06305'
url: https://arxiv.org/abs/2608.06305
pdf_url: https://arxiv.org/pdf/2608.06305
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: RAG 智能体可解释检索优化
tags:
- RAG
- Agentic Retrieval
- Long Document QA
- Information Retrieval
- Interpretability
one_liner: 提出无嵌入可审计的READ智能体检索框架，在长结构化财务文档上显著优于传统嵌入型RAG
practical_value: '- 处理高结构化、数值密集的业务文档（比如电商财报、商家运营报表、广告投放账单）时，可优先测试BM25等无嵌入检索方案，避免嵌入对重复数值、上下文继承信息的适配缺陷，降低索引维护成本

  - 针对Agent检索场景，可封装归一化 lexical search、结构导航、定长范围读取三类基础操作替代黑盒top-k检索，同时天然支持操作轨迹审计，满足金融/电商合规场景的溯源要求

  - 做PDF转文本的结构化业务时，需先量化转换损伤（比如数值格式错误、表头继承断裂），单独标记转换受限的查询类别，避免将转换错误误判为检索/生成模块的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG的chunk-embed-top-k范式在处理财务报表、审计报告等高度结构化、数值密集的长文档时存在结构性缺陷：数值重复度高（测试集重复率3.68倍）导致嵌入检索混淆，表头/单位/年份信息需要继承多行上文（数值距离其单位表头中位数13行），固定chunk大小很容易割裂数值与其上下文，导致数值含义错误（比如印度货币单位lakh和crore差100倍），即便优化table-aware chunker，仍有27%-30%的数值chunk缺失年份表头，无法通过调参修复。

### 方法关键点
- 提出READ（Reliable Embedding-free Agentic Document-search）无嵌入检索框架，基于MCP协议封装三类确定性操作：归一化词法搜索、文档结构导航、定长范围读取，无向量索引、无学习组件
- 搜索前对文本做归一化处理，适配PDF转换导致的格式artifact（比如千分符、单元格拆分、格式标记），提升词法匹配准确率
- 智能体自主组合操作完成检索，每一步操作可回溯、可审计，答案支持机械校验groundedness（即所有数值都来自读取的文本范围）

### 关键结果
用780页印度古吉拉特邦2024-25财年财务报告做测试集，51个验证过的问答对，对比基线包括Dense检索、BM25、混合检索、带top-k工具的Agent等。结果：READ准确率58.8%，远超Dense检索的15.7%（调优后最高35.3%，仍低23.5个百分点）；带top-k工具的Agent准确率仅27.5%，证明性能增益来自检索接口而非迭代能力；BM25准确率51.0%，和READ无统计显著差异，成本仅为READ的1/3。

**最值得记住的一句话**：对于布局上下文决定数值含义的长结构化文档，查询前固定的chunk划分是根本性缺陷，无嵌入的检索方案在精度和成本上都优于嵌入型方案

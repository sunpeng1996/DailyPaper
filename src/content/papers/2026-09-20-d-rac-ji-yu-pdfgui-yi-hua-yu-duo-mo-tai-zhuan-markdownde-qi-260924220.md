---
title: 'Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion
  of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion'
title_zh: D-RAC：基于PDF归一化与多模态转Markdown的企业文档检索感知分块框架
authors:
- Uday Allu
- Abhivanth Sivaprakash
- Pratik Singh
- Aman Manocha
affiliations:
- Yellow.ai
arxiv_id: '2609.24220'
url: https://arxiv.org/abs/2609.24220
pdf_url: https://arxiv.org/pdf/2609.24220
published: '2026-09-20'
collected: '2026-09-22'
category: RAG
direction: RAG 企业文档分块与摄入优化
tags:
- RAG
- Document Chunking
- Multimodal LLM
- Enterprise KB
- PDF Processing
one_liner: 提出兼容任意企业文档的检索感知分块框架，通过PDF归一化+多模态转换大幅降低RAG摄入成本
practical_value: '- 电商商品手册/活动规则/客服知识库等PDF类内容摄入可直接复用D-RAC流程：先归一化转PDF再用多模态LLM转检索优化的Markdown，表格逐行转带列上下文的独立陈述句，解决传统分块下表格检索准确率低的问题

  - 分块阶段复用ID级规划思路，仅让LLM输出元素ID列表而非重写全文，可降低70%+分块成本与时延，尤其适合需要频繁调整分块策略的电商动态知识库场景，重新分块无需重新解析文档

  - 对于多格式（DOCX/PPTX/扫描件）的企业内部文档/商品素材，无需开发多格式解析器，统一转PDF后用同一套多模态转换pipeline处理，大幅降低工程维护成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
企业RAG系统需要摄入PDF/Office/扫描件等异构文档，传统规则提取会破坏阅读顺序、表格结构与标题层级，下游检索质量差；Agentic分块需要重写全文，token成本高、 hallucination风险高，此前的W-RAC仅支持结构化HTML输入，无法兼容非结构化企业文档。

### 方法关键点
- 统一归一化：所有可渲染文档先通过标准工具转成PDF，消除格式异构性，页面渲染为200DPI的PNG适配多模态输入要求
- 检索感知多模态转换：单轮多模态LLM调用将页面转优化的Markdown：表格逐行转带列上下文的独立陈述句、保留标题层级、忽略装饰性图片、每页加溯源注释
- ID级分块规划：将转换后的Markdown解析为带ID的标题/内容元素，LLM仅基于元素ID与截断预览生成分块ID列表，不重写原文，大文档递归按标题拆分后并行规划
- 无损校验：程序校验所有内容元素都被分块覆盖，缺失内容自动生成fallback分块

### 关键实验
基于RAG-Multi-Corpus的236份共795页PDF子集（覆盖5个企业领域），对比规则分块、Agentic分块基线：全量文档处理仅72分钟零错误，生成1748个检索可用分块；对比Agentic分块，输出token减少95.7%，GPT-4.1成本降77.8%，Gemini 2.5 Pro成本降85.6%，分块时延降75%，可线性扩展到500+页文档；检索效果Recall@6达0.798，比规则分块高11.3%，与Agentic分块持平，在时序/对比/分析类查询上增益最大。

### 核心结论
把多模态LLM仅用在不可替代的文档结构恢复环节，分块阶段转为ID级规划，是兼顾RAG摄入质量、成本与确定性的核心思路。

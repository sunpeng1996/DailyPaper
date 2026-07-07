---
title: Improving Access to Historical Archives with Real-time RAG-based Systems
title_zh: 基于实时RAG系统提升历史档案数字化资源的访问能力
authors:
- Stergios Konstantinidis
- Hayman Lotfy
- Alexis Erne
- Faruk Zahiragic
- Min-Yen Kan
- Michalis Vlachos
affiliations:
- University of Lausanne
- École Polytechnique Fédérale de Lausanne (EPFL)
- National University of Singapore (NUS)
arxiv_id: '2607.03440'
url: https://arxiv.org/abs/2607.03440
pdf_url: https://arxiv.org/pdf/2607.03440
published: '2026-07-03'
collected: '2026-07-07'
category: RAG
direction: RAG落地优化 · 低质文本检索
tags:
- RAG
- OCR Correction
- Cross-encoder
- Semantic Retrieval
- Low-latency Inference
one_liner: 提出端到端LLM增强历史档案处理框架，优化OCR修正与RAG链路，兼顾检索精度与实时交互需求
practical_value: '- 处理业务场景中的低质文本（如OCR识别的商品包装/票据文本、噪声大的用户UGC评论、多模态转写文本）时，可复用LLM校正选型逻辑：优先选择大参数、强指令跟随能力的LLM做文本校正，小模型易引入额外噪声，反而拉低下游任务效果

  - 实时RAG系统的 latency 优化可直接复用该方案：召回阶段用ANN索引保障检索速度，rerank阶段根据业务SLA选择轻量MiniLM系列模型平衡精度与耗时，搭配LLM流式生成降低首包响应时间，完美适配C端用户交互场景

  - 涉及语义模糊query的检索场景（如电商模糊搜、导购Agent咨询、历史订单语义检索），可复用「语义召回+BM25关键词召回+元数据过滤+cross-encoder
  rerank」的链路，实测NDCG@10较纯BM25提升31.9%，对低质文本、术语差异场景适配性更强'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
数字化历史档案的OCR文本存在大量识别噪声，传统关键词检索无法适配语义查询、跨年代术语差异等问题，而现有RAG方案处理低质文本效果差、延迟高，无法满足用户交互式检索的需求。
### 方法关键点
- 数据 ingestion 阶段：采用指令微调LLM做OCR后处理校正，通过prompt严格约束输出保留原始文本的语义与结构，避免过度修正篡改原始内容
- 检索链路：采用混合召回（语义向量召回+BM25关键词召回）+ 轻量cross-encoder rerank的架构，同时支持时间、地域、实体等元数据过滤缩小候选集
- 延迟优化：用ANN索引做向量检索保证召回效率，rerank阶段选用MiniLM系列轻量模型，搭配LLM流式生成降低用户感知延迟
### 关键实验
数据集为50万条1762-2001年的瑞士报纸片段，配套384条人工标注的自然语言测试query，对比基线包括纯BM25、纯语义检索、无rerank链路等方案。核心结果：OCR校正阶段大模型最高降低44.52% CER、60.95% WER；端到端检索链路NDCG@10较纯BM25基线提升31.9%（从65.99%到87.05%），上下文相关性提升24.28%，端到端响应时间控制在1.3秒，满足实时交互要求。
### 核心结论
针对低质文本的RAG系统，前置OCR校正主要提升生成答案的事实正确性，而cross-encoder rerank才是检索精度提升的核心来源，资源有限时优先优化检索链路而非前置文本校正

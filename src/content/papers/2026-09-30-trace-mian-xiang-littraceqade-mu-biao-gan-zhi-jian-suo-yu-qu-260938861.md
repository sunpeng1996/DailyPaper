---
title: 'TRACE: Target-Aware Retrieval, Attributed Evidence, and Contract-Constrained
  Extraction for LitTraceQA'
title_zh: TRACE：面向LitTraceQA的目标感知检索与约束抽取框架
authors:
- Sachin Gupta
- Divya Godara
affiliations:
- Independent Researcher
arxiv_id: '2609.38861'
url: https://arxiv.org/abs/2609.38861
pdf_url: https://arxiv.org/pdf/2609.38861
published: '2026-09-30'
collected: '2026-10-01'
category: RAG
direction: 检索增强生成 · 可溯源结构化问答
tags:
- RAG
- Structured Extraction
- Evidence Grounding
- Table Extraction
- Grounded QA
one_liner: 面向可溯源科学问答的TRACE框架，通过分层约束设计提升结构化输出与评估标准的一致性
practical_value: '- 做电商/广告场景的结构化RAG（比如商品参数抽取、评论观点聚合、广告素材合规校验）时，可复用「先确定观测单元再提取值」的设计，避免把来源容器（如详情页）和观测对象（如SKU、卖点）混淆，提升结构化输出准确率。

  - 多意图检索/推荐场景不要直接做全局排序融合，可先拆分query的目标组（如用户同时搜「上衣 裤子 运动鞋」时拆分三类目标），分别检索后按组优先级合并结果，避免长尾目标被高相关热门内容挤占。

  - LLM Agent输出结构化结果（如推荐理由、用户画像标签、搜索query改写）时加入fail-closed校验（schema合法性、来源绑定校验、哈希一致性校验），把静默错误转为可观测的预设fallback，避免输出看似合法实则错误的业务内容。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG pipeline仅追求答案语义正确，忽略LitTraceQA任务要求的「论文ID溯源、精确证据定位、符合评估Schema的结构化输出」三类硬约束，存在语义正确但评分极低的grounding contract gap问题：上游模块丢弃的目标标识、分组信息下游模型无法恢复，导致结构化输出与评估要求不匹配。
### 方法关键点
- 检索层：先解析query的目标分组、约束、语义角色，分目标组做多路检索（别名匹配、BM25、引用检索、角色信号、稠密检索），保留组内排名而非直接做全局融合，优先覆盖所有目标组再做全局排序。
- 证据定位：独立于答案生成做多模态证据定位，统一归一化证据标识（公式、引用、图表ID），按评估要求的粒度去重，避免答案生成漏掉未引用的有效证据。
- 结构化提取：先根据输出Schema的行键确定观测单元（如行对应方法还是论文），构造行标识白名单后再跨来源提取值，按评估用的归一化键合并单元格，避免行键语义改写导致的评分损失。
- 执行校验：全链路做Schema合法性、来源闭包、哈希一致性校验，失败直接返回合法占位符而非静默输出错误结果。
### 关键实验
在LitTraceQA官方71题测试集（27487篇论文候选池）上，TRACE综合得分0.7606，其中paper F1 0.9728，evidence F1 0.6847，多选准确率0.98，表格行F1 0.5423；11条公开开发集表格任务上，较基线行F1提升0.12，微单元格准确率提升0.259。
### 核心结论
Representation precedes ranking，上游接口丢失的身份、分组信息，下游模型再强也无法恢复。

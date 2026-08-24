---
title: 'Auditable by Construction: An Ontology-Driven Framework for Trustworthy LLM
  Analytics in Enterprise Finance'
title_zh: 内置可审计性：面向企业金融可信LLM分析的本体驱动框架
authors:
- Sergiy Lunyakin
affiliations:
- Independent Researcher, Seattle, USA
arxiv_id: '2608.20661'
url: https://arxiv.org/abs/2608.20661
pdf_url: https://arxiv.org/pdf/2608.20661
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: GraphRAG · 企业金融场景可审计性优化
tags:
- GraphRAG
- Ontology
- Auditability
- Knowledge Graph
- Enterprise Finance
one_liner: 提出本体驱动的知识分析框架KDAF，为金融LLM应用实现原生可审计性
practical_value: '- 对于有合规要求的生成式业务（如广告素材合规溯源、电商交易对账问答），可复用本体建模+硬边界约束的思路，将业务规则（如仅返回当前商家/商品的信息）内置到知识图谱检索逻辑而非事后过滤，避免跨主体信息泄露

  - 溯源要求高的RAG系统可借鉴CARP检索的设计，将检索轨迹（种子实体匹配原因、遍历路径、来源链路）作为一等输出，而非仅返回检索片段，降低人工审核成本

  - 业务评估不要仅看回答准确率，可根据场景需求新增可审计性相关指标（如溯源F1、有效路径率），优先保障合规性再优化效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业金融场景LLM应用的核心瓶颈不是生成流畅度，而是监管要求下的可信性：FP&A等受监管流程的输出必须可追溯至权威来源、可领域化解释、支持事后审计，但现有RAG系统仅以准确率为优化目标，缺失结构化溯源能力，难以满足合规要求。

### 方法关键点
- 提出6阶段迭代的知识驱动分析框架KDAF：包括面向业务问题的能力问句建模、最小可行图冷启动本体、schema引导的知识抽取、带相关性和来源标注的上下文表示、人在环混合验证、CARP图证据检索算法
- 核心检索算法CARP将检索轨迹作为一等输出，全程记录种子实体匹配原因、遍历路径、来源链路，融合词汇相似度、本体关系权重、概念/周期覆盖率完成证据排序，支持硬边界约束（如禁止跨主体检索）

### 关键实验
在FinanceBench的145个金融问答问题上对比5组基线：零上下文LLM、BM25稀疏检索、概念加权词汇检索、无本体图遍历、KDAF。核心结果：
1. 零上下文LLM正确率仅4.1%，远低于RAG类方案的10%-12%
2. 各RAG方案正确率无统计显著差异，KDAF比BM25仅低0.007，单文档查询场景下准确率无法覆盖结构化检索的建设成本
3. 可审计性指标上KDAF大幅领先：引用可追溯F1达0.515，比BM25高0.052，比无本体图遍历高0.027，所有检索结果无跨主体信息泄露，100%具备完整来源链路

**最值得记住的一句话**：对于强监管场景，可审计性而非问答准确率，才是结构化检索方案的核心价值锚点

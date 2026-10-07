---
title: 'DBRAG: Multi-Table Retrieval-Augmented Generation for Complex Database Queries'
title_zh: DBRAG：面向复杂数据库查询的多表检索增强生成框架
authors:
- Prince Larbi Ampofo
- Ryoji Kubo
- Djellel Difallah
affiliations:
- NYU Abu Dhabi
arxiv_id: '2610.07622'
url: https://arxiv.org/abs/2610.07622
pdf_url: https://arxiv.org/pdf/2610.07622
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: 检索增强生成 · 多表数据库问答
tags:
- RAG
- Multi-Table QA
- Chain-of-Thought
- Program-aided Reasoning
- Text-to-SQL
one_liner: 提出两阶段表检索+多表感知CoT推理的RAG框架，解决复杂跨表数据库问答问题
practical_value: '- 多源结构化数据检索的两阶段架构可复用：先用向量粗排选候选，再用LLM结合上下文精排，兼顾效率和相关性，适合电商用户/商品/订单多表自然语言查询场景

  - 元数据增强技巧可迁移：给表schema补充2-3条query相关样本行，能大幅提升LLM对表关联关系的判断准确率，可直接用于BI查询工具、推荐特征元数据管理

  - 程序辅助推理方案可落地：让LLM生成代码直接操作全量结构化数据，避免大表灌入LLM上下文的成本，适合大促场景下多表关联的ad-hoc数据分析需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有表问答方案多针对单表场景，或默认相关表已提前给出，实际业务中用户的自然语言查询常需要关联多表数据，直接喂入全量表会超过LLM上下文窗口，且单表独立检索容易遗漏需关联的辅助表，导致查询准确率低，无法支撑复杂跨表数据分析需求。

### 方法关键点
- 两阶段多表检索：第一阶段用预计算的表索引（表名+schema+随机行的向量嵌入）做粗排，召回Top-K候选表；第二阶段用预计算的行索引召回每张候选表的query相关行，生成带行上下文的表摘要，输入LLM做精排，精排要求同时考虑表的直接相关性、可关联属性、联合信息覆盖率，最终选出Top-M最相关表
- 多表感知推理：先从精排后的表中确认最终需要关联的表，再用多表专属CoT提示引导生成Python DataFrame操作代码，调用执行工具操作全量表数据，迭代生成结果，避免全表进入上下文的成本

### 关键实验
在Spider、GeoQuery、ATIS三个多表QA数据集上验证，对比Contriever、DTR、JAR等检索基线，以及ReadTable、MTQA等推理基线：Spider数据集上检索Recall@5达97.1%，较次优基线高0.3pct；Spider数据集上推理Table EM达44.9%，较ReadTable高15.3pct，较MTQA高34.3pct；精排阶段补充2条query相关行即可达到最优效果，继续增加行增益不明显。

### 核心结论
结构化多源数据的RAG系统，给元数据补充少量query相关的样本内容，同时让LLM在精排阶段考虑多源数据的关联价值，能以极低的成本大幅提升整体性能。

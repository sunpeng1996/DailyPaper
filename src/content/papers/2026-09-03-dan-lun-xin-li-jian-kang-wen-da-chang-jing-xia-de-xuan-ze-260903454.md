---
title: 'When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA'
title_zh: 单轮心理健康问答场景下的选择性检索RAG机制研究
authors:
- Hyunseo Oh
- Chong-Kwon Kim
- Yoonhyuk Choi
affiliations:
- Sookmyung Women’s University
- Korea Institute of Energy Technology
arxiv_id: '2609.03454'
url: https://arxiv.org/abs/2609.03454
pdf_url: https://arxiv.org/pdf/2609.03454
published: '2026-09-03'
collected: '2026-09-04'
category: RAG
direction: 自适应RAG · 安全敏感场景优化
tags:
- RAG
- Selective Retrieval
- QLoRA
- Safety Alignment
- Domain Adaptation
one_liner: 提出轻量混合门控选择性RAG策略，解决心理健康QA场景全量检索的安全风险问题
practical_value: '- 电商客服、合规咨询等安全敏感类Agent可复用「硬规则安全触发+多维度效用打分」的混合门控RAG策略，仅在必要时召回，避免引入噪音或合规风险

  - 可复用「预生成闭包草稿→复用现有生成模型打分→按需召回重生成」的流水线设计，无需额外训练路由模型，大幅降低工程落地成本

  - 领域RAG阈值可采用保守校准策略，优先控制风险而非追求召回率，本研究仅激活9%的检索请求即达到最优质量-安全平衡，可迁移到售后回复、合规商品推荐等场景

  - 领域RAG语料无需追求大而全，可按功能做细分类（如电商场景分为售后规则、商品参数、活动规则三类），召回时路由到对应子集，提升准确度同时降低干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG可提升LLM回复的事实性与落地性，但在心理健康QA这类安全敏感场景，全量检索会引入无关噪音、过度专业的医疗建议等安全风险；现有自适应RAG多基于事实不确定性、查询复杂度判断，未覆盖领域特定的安全与效用需求，亟需针对性的选择性检索机制。

### 方法关键点
- 控制变量设计：通过QLoRA在MentalChat16K数据集微调Gemma-4-E4B-it作为通用生成器，所有对比组共享该模型，仅变更检索策略
- 紧凑型语料库：仅收录40份权威领域文档，分为应对策略、心理教育、安全资源三类，采用BM25做轻量检索
- 混合门控触发：先生成闭包回复草稿，复用同一生成器打分心理教育需求、应对支持需求、回复特异性三个维度，叠加硬规则安全触发（自伤、自杀等高危query直接触发安全类资源召回），仅当得分超过阈值时触发检索并重生成

### 关键实验
在CounselBench-Eval（常规评估）、CounselBench-Adv（对抗安全测试）上对比闭包生成、全量检索RAG基线：对比全量检索，选择性检索仅触发9%的召回请求，整体质量分从4.12提升到4.17，医疗建议违规率从0.01降到0，对抗测试下宏观失败率从0.0917降到0.025，与闭包生成安全表现持平。

最值得记住的结论：**在安全敏感场景下，检索激活本身就是一项风险控制决策，保守的选择性检索比全量检索更能平衡效用增益与安全风险**

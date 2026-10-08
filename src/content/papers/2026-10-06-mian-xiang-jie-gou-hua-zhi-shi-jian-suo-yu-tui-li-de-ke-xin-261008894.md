---
title: Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning
title_zh: 面向结构化知识检索与推理的可信领域专属AI框架
authors:
- Ryan C. Barron
affiliations:
- University of Maryland, Baltimore County
- Los Alamos National Laboratory
arxiv_id: '2610.08894'
url: https://arxiv.org/abs/2610.08894
pdf_url: https://arxiv.org/pdf/2610.08894
published: '2026-10-06'
collected: '2026-10-08'
category: RAG
direction: 检索增强生成 · 结构化知识推理
tags:
- RAG
- Knowledge Graph
- HNMFk
- Topic Modeling
- Trustworthy AI
one_liner: 可落地的端到端架构，实现非结构化领域文本到可检索推理结构化知识的可信转化
practical_value: '- 可复用「事件同步的KG+向量库双知识层架构」搭建电商垂类RAG系统，适配商品规范、售后政策、合规说明等高准确率要求的问答场景，从架构层面降低幻觉

  - 迁移Binary Bleed优化的HNMFk层级主题建模能力，用于电商用户评论、商品标签的自动类目挖掘，无需人工预设类目数量与深度，大幅降低运营标注成本

  - 采用HEAL层级嵌入对齐损失微调垂域Embedding模型，让检索结果贴合业务类目层级逻辑，提升电商搜索、导购Agent的语义检索准确率

  - 借鉴T-SRAG动态路由逻辑，根据Query类型自动选择KG多跳推理或向量检索路径，平衡垂域QA系统的准确率与响应延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有领域知识处理pipeline碎片化，依赖脆弱的关键词提取、临时适配的主题建模与脱节的推理模块，普通RAG系统的向量库缺乏语义锚定，hallucination问题突出；同时传统主题建模需要人工预设参数，可解释性差，无法满足法律、医疗、电商合规等高可信场景的检索与推理需求。

### 方法关键点
- 语料加工：SME筛选的种子语料经引文网络扩展后，通过语义过滤、embedding超球筛选、LLM relevance投票的多阶段剪枝，得到高纯度领域语料
- 主题建模：Binary Bleed低秩搜索算法可将NMF秩搜索复杂度降低70%以上，基于此实现的HNMFk深度自适应主题建模，可自动生成可解释层级主题树，无需人工预设主题数与层级深度
- 知识层：采用KG+向量库双存架构，主题-文档关联关系通过事件驱动机制同步更新，保证符号表示与语义向量的一致性
- 检索推理：T-SRAG可根据Query特征动态路由到KG多跳推理、向量检索或混合路径，通过对比损失对齐embedding与层级主题结构，结合张量链路预测补全KG缺失关系，所有回答可溯源到原始语料

### 关键结果
跨网络安全、法律、材料科学、医疗4个领域验证：对比GPT-4o、Claude 3 Opus等SOTA模型，法律领域25道专业问题准确率提升27%，FactCC事实一致性得分提升32%，检索MRR提升19%，超导体链路预测任务Hit@1达89%。

> 最值得记住的一句话：高可信垂域AI系统的核心是符号推理与语义检索的紧耦合，可在不损失生成流畅性的前提下从根源降低幻觉风险

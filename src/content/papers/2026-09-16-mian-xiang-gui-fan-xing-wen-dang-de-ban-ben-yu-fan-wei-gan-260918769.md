---
title: 'Version- and Scope-Aware Question Answering over Normative Documents: A Deployed
  System and an End-to-End Evaluation at Production Scale'
title_zh: 面向规范性文档的版本与范围感知问答系统及生产规模端到端评估
authors:
- Liuyin Wang
- Shuaipeng Jin
- Jiwei Shi
- Jensen Hsu
affiliations:
- Beijing Caizhi Technology Co., Ltd.
- dknownAI
arxiv_id: '2609.18769'
url: https://arxiv.org/abs/2609.18769
pdf_url: https://arxiv.org/pdf/2609.18769
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: RAG增强 · 规范性知识问答落地
tags:
- RAG
- DocumentQA
- GovernanceLayer
- ProductionEvaluation
- VersionAware
one_liner: 为规范性文档问答设计显式版本范围治理层，较通用托管RAG精度提升9.6点已规模化落地
practical_value: '- 电商平台规则、活动政策、商家准入等多版本多适用范围的规则类知识库，可将版本、生效时间、适用人群/区域等元数据结构化抽取，检索前先用硬规则过滤，不要仅依赖语义相似度软排序，可大幅降低错误答案率

  - RAG系统评估不要局限于召回率等中间指标，需端到端评估用户实际收到的答案质量，同时区分空返回、无引用答案、带引用错误答案三类故障，便于定位问题根因

  - 客服、政策咨询等对答案严谨性要求高的场景，可在生成前增加证据充分性校验，证据不足时主动要求用户补充信息，避免生成无依据的误导性答案'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
规范性文档（政策、规则、条款等）的正确性高度依赖文档版本、适用范围、生效时间等元信息，通用托管RAG仅靠语义相似度检索，很容易召回已失效、范围不匹配的近文本内容，产生看似正确带引用的错误答案，在政务、企业服务等场景会造成严重后果。

### 方法关键点
- 新增前置治理层，文档入库时抽取发布主体、生效/失效时间、适用区域、适用主体、版本继承关系等元数据作为结构化字段
- 检索阶段先执行硬规则过滤，排除版本失效、范围不匹配的文档再进入语义排序环节，过滤规则可按顺序逐层放宽
- 生成前增加证据充分性校验，仅当过滤后的候选集满足问题的范围、版本要求时才生成答案，否则要求用户补充信息，所有生成内容带原文引用标记

### 关键实验
在7.3万份规范性文档的生产语料上，对比自研DeepKnown系统和Google Gemini File Search托管RAG服务，用分层抽样的200条带金标准的测试集评估：自研系统总得分97.7，托管服务得分88.1，领先9.6个百分点；其中部分答案类问题领先19.2分，复杂问题领先10.2分，简单问题领先7.9分；该系统已上线服务1126名注册用户，工作日峰值调用量达10万次。

### 核心结论
对于规则类、规范类知识的RAG场景，将版本、范围等约束做成检索前可解释的硬规则，远好过依赖黑盒排序和大模型自行理解上下文里的元信息。

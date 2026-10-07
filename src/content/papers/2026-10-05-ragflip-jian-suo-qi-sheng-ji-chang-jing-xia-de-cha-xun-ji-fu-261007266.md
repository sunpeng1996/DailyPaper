---
title: 'RAGFlip: Measuring Query-Level Negative Flips in Retriever Upgrades'
title_zh: RAGFlip：检索器升级场景下的查询级负翻转度量方法
authors:
- Elyas Irankhah
- Muhammad Arif
affiliations:
- Yale School of Medicine
arxiv_id: '2610.07266'
url: https://arxiv.org/abs/2610.07266
pdf_url: https://arxiv.org/pdf/2610.07266
published: '2026-10-05'
collected: '2026-10-07'
category: Eval
direction: RAG 检索器升级兼容性评估
tags:
- RAG
- Retrieval
- Model Upgrade
- Evaluation
- Negative Flip
one_liner: 提出查询级检索器升级兼容性评估框架，量化升级时原有有效查询的退化比例
practical_value: '- 搜索、RAG召回类系统升级时，不能仅依赖大盘聚合指标，必须新增查询级负翻转校验，避免原有高满意度query的效果退化，尤其适合电商搜索、导购Agent等用户体验敏感场景

  - 检索器升级上线时可直接采用RRF融合BM25与新检索器的排序结果，固定召回预算下可降低70%+的负翻转比例，仅损失10%-25%的净增益，性价比极高

  - 可对业务query分层：原有系统top1就能返回正确结果的高置信query优先保障兼容性，这类query的负翻转率最低，是用户体验的核心盘

  - 多轮导购、复杂商品问答等多跳搜索场景需采用全相关召回校验，这类场景负翻转率是普通单相关场景的6-8倍，需额外收紧评估标准'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索器升级普遍采用NDCG、召回率等聚合指标评估，会掩盖大量原有系统已正确响应的查询的效果退化（即负翻转），这类退化直接损害老用户体验，但目前缺乏面向查询级的兼容性度量体系，无法提前识别这类风险。

### 方法关键点
- 定义4类查询级转换状态：保留（新旧检索器都返回有效结果）、修复（旧检索器无效、新检索器有效）、负翻转（旧有效、新无效）、不变失效（新旧都无效）
- 提出4个核心度量指标：修复率（旧失效查询的修复占比）、负翻转率（旧有效查询的退化占比）、兼容性（旧有效查询的保留占比）、净增益（修复数-负翻转数）
- 验证3种负翻转缓解方案：排名交替拼接、RRF融合、保留两个召回结果的全集

### 关键实验结果
基于3个BEIR基准数据集（Natural Questions、HotpotQA、FiQA），以BM25为基准，对比BGE-large、E5-large-v2、SPLADE三个主流检索器，覆盖k=1~50共5种召回深度：
1. 所有场景下新检索器大盘指标均提升，但100%存在负翻转：k=1时负翻转率达8.6%~37.5%，k=10时为1.9%~12.4%
2. 固定召回预算下RRF融合可降低70%~80%的负翻转，仅损失10%~25%的净增益；保留新旧召回的全集可完全消除负翻转，仅需将召回预算翻倍
3. HotpotQA多跳问答场景采用全相关召回要求时，k=10的负翻转率提升至12.3%~17.3%，约为单相关要求的6倍

> 最值得记住的结论：检索器升级时聚合指标的提升完全不能替代查询级兼容性校验，负翻转是所有检索升级的必然现象，必须纳入上线前强制评估流程。

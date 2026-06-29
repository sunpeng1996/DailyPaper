---
title: A Sensitivity-Aware Test Collection for Search Among Personal Information
title_zh: A Sensitivity-Aware Test Collection for Search Amo
authors:
- Jack McKechnie
- Graham McDonald
- Craig Macdonald
arxiv_id: '2606.27559'
url: https://arxiv.org/abs/2606.27559
pdf_url: https://arxiv.org/pdf/2606.27559
published: '2026-06-25'
collected: '2026-06-29'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Traditional search tasks aim to satisfy user information needs by returning
  a subset of a colle...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Traditional search tasks aim to satisfy user information needs by returning a subset of a collection of documents, ranked by the documents' relevance to a user query. However, some collections that contain useful information also contain sensitive personal information. Recently, there has been increasing interest in the development of Sensitivity-Aware Search (SAS) retrieval models to provide users with effective retrieval results without revealing such sensitive information. To develop such systems, test collections containing both sensitive and non-sensitive information, a set of queries, and query-document relevance assessments are required. The Enron email corpus contains real business-related emails, where some emails also contain sensitive personal information. However, the original Enron collection does not contain queries or query-relevance assessments. To this end, we crowdsource 150 query formulations for 50 different topics and 11,471 query-relevance assessments for a subset of the Enron documents that have been manually labelled for sensitivity. We follow best practices for using large language models (LLMs) in Information Retrieval evaluation to extend the collection further with additional LLM judged query-relevance assessments and sensitivity labels. We present baseline performances for relevance, sensitivity classification, and sensitivity-aware search on the collection. We make the collection available, including through the popular ir_datasets package, and provide pre-built sparse and dense indices on Huggingface to facilitate easy experimentation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

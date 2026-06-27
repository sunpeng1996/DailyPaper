---
title: 'Scoring Is Not Enough: Addressing Gaps in Utility-fairness Trade-offs for
  Ranking'
title_zh: 'Scoring Is Not Enough: Addressing Gaps in Utility-'
authors:
- Shubham Singh
- Ian A. Kash
- Mesrob I. Ohannessian
arxiv_id: '2606.26369'
url: https://arxiv.org/abs/2606.26369
pdf_url: https://arxiv.org/pdf/2606.26369
published: '2026-06-24'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Scoring functions are used to represent the relevance of individual documents.
  In modern inform...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Scoring functions are used to represent the relevance of individual documents. In modern information retrieval or recommendation systems, they are often learned from data and play a pivotal role in ranking sets of documents or items in a way that maximizes utility to a query or user. With the recent interest in algorithmic fairness, the success of scoring has naturally led to methods that learn scores that simultaneously trade off fairness and utility. In this work, we show that in stark contrast with utility-centric objectives, scoring is sub-optimal in achieving all utility-fairness trade-offs. We establish this with a series of counter-examples with a generic fairness formulation. We show that the issue persists whether we have a deterministic scoring function or a randomized one, or whether we measure fairness at the scope of a single query or across multiple queries. On the positive side, we empirically demonstrate that semi-greedy post-processing has the potential to achieve much better trade-offs, often approaching the ideal of exhaustive post-processing in a tractable way.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

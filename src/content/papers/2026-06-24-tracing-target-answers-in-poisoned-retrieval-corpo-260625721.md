---
title: Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution
title_zh: Tracing Target Answers in Poisoned Retrieval Corpo
authors:
- Yan-Lun Chen
- Pin-Yu Chen
- Chia-Mu Yu
- Ying-Dar Lin
- Yu-Sung Wu
- Wei-Bin Lee
arxiv_id: '2606.25721'
url: https://arxiv.org/abs/2606.25721
pdf_url: https://arxiv.org/pdf/2606.25721
published: '2026-06-24'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning
  attacks that ma...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead. We present TRACE, a lightweight detection framework that identifies poisoning attacks by tracing answer-related tokens through token influence attribution. TRACE first discovers recurrent high-influence keywords across retrieved documents and then performs a secondary verification to confirm their influence on model predictions. Experiments on three QA benchmarks and six LLMs demonstrate strong detection performance while simultaneously uncovering attacker-specified target answers.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

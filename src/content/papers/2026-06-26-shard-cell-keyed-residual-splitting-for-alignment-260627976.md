---
title: 'SHARD: cell-keyed residual splitting for alignment-resistant private dense
  retrieval'
title_zh: 'SHARD: cell-keyed residual splitting for alignment'
authors:
- Sergey Kurilenko
arxiv_id: '2606.27976'
url: https://arxiv.org/abs/2606.27976
pdf_url: https://arxiv.org/pdf/2606.27976
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Dense embeddings underpin semantic search and RAG, yet a leaked vector
  store hands much of the...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Dense embeddings underpin semantic search and RAG, yet a leaked vector store hands much of the underlying text back to whoever holds it. The attacks that make this possible (few-shot alignment, zero-shot inversion, unsupervised cross-space translation) share one weakness: the protected store is a single global geometry that can be aligned to a known one. A secret global rotation, the usual lightweight defence, is no exception: orthogonal Procrustes recovers it once the attacker has about the subspace dimension in known pairs. We introduce Shard, a retrieval-preserving embedding transform that removes this weak axis. The centred embedding is split into a short public prefix (for stage-1 retrieval) and a private residual sharded into C cells under separate secret keys; the residual is reranked under CKKS, where the keys cancel and leave the inner product exact. A single parameter C runs the design from the global-linear baseline it replaces (C=1) to per-document micro-keys (C=N). Because the rerank is full-dimensional, Shard returns the raw-space nDCG@10 that half-SVD truncation gives up; and because the residual is keyed cell-locally, mapping it back to a common frame under a diffuse known-plaintext leak costs roughly C times more anchors (median 200 to 102,400 at C=256), for a few encrypted queries. The short public prefix leaks far less neighbour structure, and a micro-key limit drives the residual graph to zero with an unlinkable, renewable template. The barrier holds against learned, non-linear and unsupervised aligners, and where a matched-utility noise defence de-anonymises almost every probe, Shard de-anonymises none. We are plain about the limits: within a cell the keys cancel, a targeted attacker needs only about d_priv anchors, and an overlapping reference corpus still leaks through the prefix. Shard is an attack-aware geometric defence, not a cryptographic guarantee.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

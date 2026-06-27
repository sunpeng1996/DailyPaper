---
title: Exact and Deterministic Patch Descriptor Retrieval via Hierarchical Normalization
title_zh: Exact and Deterministic Patch Descriptor Retrieval
authors:
- Koichi Sato
arxiv_id: '2606.27280'
url: https://arxiv.org/abs/2606.27280
pdf_url: https://arxiv.org/pdf/2606.27280
published: '2026-06-25'
collected: '2026-06-27'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: We present a patch descriptor retrieval method that returns the exact nearest
  neighbour -- prov...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

We present a patch descriptor retrieval method that returns the exact nearest neighbour -- provably identical to exhaustive full-vector search -- while evaluating only a small fraction of the database, and does so deterministically: the same (database, query) pair always produces the same result, independent of run order, thread count, or hardware. This contrasts with approximate nearest-neighbour (ANN) approaches such as HNSW and IVF-PQ, which trade exactness for speed and may return different results across runs. The enabling mechanism is Hierarchical Normalization (HN): a normalisation scheme that splits the pre-normalisation feature vector into a K-dim major component (norm sqrt(1-alpha)) and a (128-K)-dim minor component (norm sqrt(alpha)). Since the minor inner product is bounded by alpha (Cauchy-Schwarz on the prescribed norms), the major similarity plus alpha is an admissible upper bound on the full similarity: the search scans the K-dim major component for all entries, then applies full 128-dim evaluation only to entries that cannot be pruned -- a provably exact branch-and-bound scan. We train HN-modified HardNet on the notredame split of the UBC patch dataset and evaluate on trevi and halfdome. With a cache-optimised Structure-of-Arrays layout and K=8, alpha=1/32, the search achieves 13.7x (trevi) / 12.7x (halfdome) speed-up over brute-force 128-dim search, with only 0.4% of entries requiring full evaluation. At K=16, alpha=1/8, FPR@95 rises from 0.0062 to 0.0064 on trevi at 7.2x speed-up, with 98.8% of entries bypassing full evaluation.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

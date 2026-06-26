---
title: 'Hybrid privacy-aware semantic search: SVD-truncated document geometry and
  CKKS-encrypted query reranking under a restricted threat model'
title_zh: 'Hybrid privacy-aware semantic search: SVD-truncate'
authors:
- Sergey Kurilenko
arxiv_id: '2606.26373'
url: https://arxiv.org/abs/2606.26373
pdf_url: https://arxiv.org/pdf/2606.26373
published: '2026-06-24'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Dense embeddings power semantic search and retrieval-augmented generation,
  but embedding-invers...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Dense embeddings power semantic search and retrieval-augmented generation, but embedding-inversion attacks can reconstruct source text from a vector: when a vector database leaks, the documents behind it leak too. The textbook defences are extremes - encrypting the whole search homomorphically is sound but too slow at million-document scale, while privacy noise degrades ranking long before it protects. We study a middle path exploiting the asymmetry between the static collection and the dynamic query. The collection is protected geometrically: each vector is truncated onto a lower-dimensional SVD subspace and rotated by a secret orthogonal transform known only to the owner. The query is protected cryptographically: it is reranked under CKKS homomorphic encryption, so an honest-but-curious server never sees the query or the scores. CKKS parameters come from a small offline benchmark. We prove a tight lower bound on the reconstruction error of any attacker confined to the protected subspace. On one million documents and five encoders the scheme preserves ranking quality (slightly improving it on strong encoders, as a linear denoiser) at sub-second latency, and an off-the-shelf inversion attack on the protected space collapses to the noise floor. We then test stronger adversaries: a known-plaintext attacker recovers the rotation by orthogonal Procrustes from about as many leaked pairs as the retained dimension; the public product-quantization codes preserve most nearest-neighbour structure; and random-projection, calibrated-noise and BEIR baselines show the truncation is an encoder-dependent accuracy cost, not a free denoiser. We state the limits: query confidentiality is cryptographic, but document protection is an empirical obfuscation layer (SVD truncation plus a secret rotation), not a cryptographic primitive, and we delimit the threat model for each claim.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

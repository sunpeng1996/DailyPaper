---
title: 'Hierarchical Muon: Tiled Newton-Schulz Updates for Efficient Muon Optimization'
title_zh: 'Hierarchical Muon: Tiled Newton-Schulz Updates for'
authors:
- Ziyuan Tang
- Tianshi Xu
- Yousef Saad
- Yuanzhe Xi
arxiv_id: '2606.27216'
url: https://arxiv.org/abs/2606.27216
pdf_url: https://arxiv.org/pdf/2606.27216
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Muon-type optimizers construct update directions for dense neural-network
  weights by applying a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Muon-type optimizers construct update directions for dense neural-network weights by applying a finite Newton-Schulz map to momentum-gradient matrices. For an $H \times W$ matrix, with $r=\min\{H,W\}$ and $s=\max\{H,W\}$, $K$ steps of the full-matrix Newton-Schulz update require $O(r^2 s K)$ work and couple all rows and columns through repeated Gram matrix products. We introduce Hierarchical Muon (HiMuon), a tiled Newton-Schulz scheme for Muon-type optimization. HiMuon partitions each momentum-gradient matrix into $T \times T$ tiles, applies the same finite Newton-Schulz map independently to each tile, and reassembles the results. For finite $T$ below the matrix dimensions, HiMuon defines a local matrix-function map rather than a convergent approximation to the full-matrix update: spectral interactions are preserved within tiles and discarded across tile boundaries. For fixed finite $T$, the leading Newton-Schulz work decreases to $O(H W T K)$, and the computation decomposes into independent small dense matrix operations. This structure enables tile-size-dependent GPU kernels, cross-layer batching, memory-bounded chunking, and runtime tile-size schedules. Experiments on transformer training and controlled matrix-function diagnostics show that HiMuon improves optimizer-step efficiency while keeping training behavior close to full-matrix Muon in the tested regimes.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

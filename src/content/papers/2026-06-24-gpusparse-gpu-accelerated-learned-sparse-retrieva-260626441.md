---
title: 'GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted
  Indices'
title_zh: 'GPUSparse: GPU-Accelerated Learned Sparse Retrieva'
authors:
- Ashutosh Sharma
arxiv_id: '2606.26441'
url: https://arxiv.org/abs/2606.26441
pdf_url: https://arxiv.org/pdf/2606.26441
published: '2026-06-24'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Learned sparse retrieval models such as SPLADE achieve retrieval quality
  competitive with dense...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Learned sparse retrieval models such as SPLADE achieve retrieval quality competitive with dense models while preserving the interpretability and exact-match advantages of sparse representations. However, inference-time scoring still relies on CPU-bound inverted index traversal algorithms (WAND, Block-Max WAND), creating a fundamental bottleneck for real-time serving at scale. We present GPUSparse, a system for GPU-accelerated exact learned sparse retrieval that introduces: (1) a GPU-parallel inverted index with block-aligned, warp-coalesced posting lists; (2) a batched scatter-add scoring algorithm that processes hundreds of queries simultaneously; and (3) fused Triton kernels with an analysis of the tradeoff between work-efficiency and hardware utilization. On MS MARCO passage ranking (8.8M passages) with real SPLADE embeddings, GPUSparse matches CPU exact scoring to three decimals (MRR@10=0.383, equal to Pyserini SPLADE at this precision; Recall@1000>=0.999 vs. dense matmul, the residual from floating-point tie-breaking) while providing a 235x speedup over Pyserini CPU at 8.8M documents (1.27ms vs. 298ms per query). Compared to Seismic (the fastest CPU sparse retrieval system), which trades 25% recall for speed (R@1000=0.738 vs. 0.983 exact), GPUSparse achieves exact scoring at 787 QPS throughput (batch 500) on the full 8.8M collection, with 1.3ms per query. Our document-parallel kernel reaches 62.6% of H100 peak HBM bandwidth, revealing a fundamental work-efficiency vs. bandwidth-efficiency tradeoff in GPU sparse retrieval. The reformulation of sparse scoring as scatter-add over an inverted index is shared with SPARe's iterative mode; our contribution is its fused-kernel realization, which we measure to be 23-270x faster than a faithful SPARe iterative reimplementation.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

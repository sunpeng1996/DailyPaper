---
title: 'TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product
  Quantization'
title_zh: 'TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimen'
authors:
- Ashutosh Sharma
arxiv_id: '2606.26439'
url: https://arxiv.org/abs/2606.26439
pdf_url: https://arxiv.org/pdf/2606.26439
published: '2026-06-24'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Multi-vector retrieval models such as ColBERT achieve state-of-the-art
  accuracy through fine-gr...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Multi-vector retrieval models such as ColBERT achieve state-of-the-art accuracy through fine-grained token-level MaxSim scoring, yet existing GPU implementations leave most hardware performance unused. We give a roofline analysis of MaxSim on modern GPUs and identify a severe bandwidth gap: naive implementations reach only 5-18% of peak HBM bandwidth because they materialize the Nq x Nd similarity matrix, wasting memory traffic on data that is consumed once and discarded. We present TileMaxSim, a family of IO-aware Triton kernels that close this gap via (1) multi-query SRAM tiling that streams document embeddings through shared memory while accumulating per-query-token maxima in registers, reading each embedding from HBM exactly once; (2) dimension tiling that partitions the embedding dimension into 128-wide chunks, enabling scoring for d > 128 embeddings that overflow shared memory; and (3) fused product-quantization scoring via shared-memory lookup tables, cutting HBM I/O by up to ~31x. On NVIDIA H100 GPUs, TileMaxSim reaches 80.2% of peak HBM bandwidth and scores 82M documents/second (71.6M/s on real MS MARCO passages), a 220x speedup over loop-based scoring, 6.5x over fused PyTorch, 6.6-8.5x over torch.compile, and 469x the scoring throughput of WARP's CPU engine on the same node. TileMaxSim preserves exact retrieval quality: on MS MARCO and three BEIR benchmarks, rankings match reference MaxSim. As a drop-in replacement in ColBERTv2/PLAID, it cuts scoring latency at 100K candidates from 268 ms to 1.2 ms (98% lower end-to-end latency). We further show constant throughput from 100K to 500K documents, data-parallel multi-GPU sharding, robustness across dimensions 64-768, and FP16/BF16/FP32 support. Concurrent work independently develops an IO-aware fused MaxSim kernel; we differ in dimension tiling for d > 128 and fused product-quantization scoring.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

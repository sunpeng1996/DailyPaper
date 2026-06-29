---
title: 'MLVC: Multi-platform Learned Video Codec for Real-World Deployment'
title_zh: 'MLVC: Multi-platform Learned Video Codec for Real-'
authors:
- Tanel Pärnamaa
- Martin Lumiste
- Ardi Loot
- Evgenii Indenbom
- Andrei Znobishchev
- Ando Saabas
arxiv_id: '2606.28027'
url: https://arxiv.org/abs/2606.28027
pdf_url: https://arxiv.org/pdf/2606.28027
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Neural video codecs have surpassed classical codecs in coding efficiency
  but remain impractical...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Neural video codecs have surpassed classical codecs in coding efficiency but remain impractical for deployment due to cross-platform incompatibility and high computational cost. Existing quantization-based solutions fail to produce deterministic results across diverse hardware platforms, leading to catastrophic decoding failures. We introduce MLVC, a hardware-robust neural video codec designed for practical cross-platform inference. The key idea is to explicitly transmit scale parameters through the hyperprior, which guarantees entropy coding consistency across devices without requiring bit-exact arithmetic. While this increases bitrate overhead, we recover most of the coding efficiency through architectural improvements (gated memory, ReGLU activation), a long-term reference recovery mechanism, and domain-specific perceptual training. On the VCD video conferencing benchmark, MLVC achieves >70% BD-rate (MOS) improvement over hardware HEVC, the strongest deployable baseline, while reaching subjective quality competitive with DCVC-RT, which cannot operate across diverse platforms. Both the encoder and decoder run at 100 FPS on average on commodity NPUs from Apple, Intel, and Qualcomm. MLVC is the first neural video codec to combine competitive compression performance, real-time speed, and cross-platform robustness across diverse consumer devices, making it suitable for widespread deployment. Code will be released.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

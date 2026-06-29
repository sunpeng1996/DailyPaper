---
title: Enhanced Neural Video Representation Compression across Extreme Complexity
  and Quality Scales
title_zh: Enhanced Neural Video Representation Compression a
authors:
- Ho Man Kwan
- Tianhao Peng
- Fan Zhang
- Mike Nilsson
- Andrew Gower
- David Bull
arxiv_id: '2606.28163'
url: https://arxiv.org/abs/2606.28163
pdf_url: https://arxiv.org/pdf/2606.28163
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Implicit neural representations (INRs) have recently emerged as a promising
  approach to video c...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Implicit neural representations (INRs) have recently emerged as a promising approach to video compression, delivering competitive rate-distortion performance alongside rapid decoding. However, existing neural video codecs struggle to balance complexity and scalability. Lightweight models often suffer from degraded compression performance when scaled to different bitrate/quality levels, whereas high-performance models exhibit limited scalability, as their model complexity typically increases with quality. This lack of a unified architecture capable of maintaining consistent complexity across a wide range of bitrates severely limits their diverse real-world deployment. To address these challenges, we introduce NVRC++, a novel INR-based video codec that utilizes a lightweight INR with multiple high-resolution feature grids, providing high scalability at any given complexity level. This is paired with an optimization framework that enables efficient overfitting on high-resolution grids for long video sequences, thereby exploiting spatio-temporal redundancies without prohibitive computational or memory overhead. Additionally, an advanced entropy model is designed for efficiently compressing the high-dimensional grid parameters. As a result, NVRC++ provides four complexity levels (from 7kMACs/pixel to 360kMACs/pixel), each spanning wide bitrate and quality ranges while supporting real-time decoding. The experimental results show that NVRC++ offers a much faster decoding speed (up to 7.6x) compared to the SOTA INR-based video codec, NVRC, while delivering comparable performance.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

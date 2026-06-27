---
title: An Evaluation of ABR Switching for Time-Shifted Clients in MoQ
title_zh: An Evaluation of ABR Switching for Time-Shifted Cl
authors:
- Abanisenioluwa Orojo
- Tanvir Redoy
- Samira Afzal
- Andrew C. Freeman
arxiv_id: '2606.26368'
url: https://arxiv.org/abs/2606.26368
pdf_url: https://arxiv.org/pdf/2606.26368
published: '2026-06-24'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Media over QUIC enables ultra low latency video streaming over QUIC, but
  its default quality-sw...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Media over QUIC enables ultra low latency video streaming over QUIC, but its default quality-switching semantics risk introducing playback gaps during periods of network congestion. The in-progress SWITCH specification for MOQ Transport aims to streamline rate adaptation for MoQ. In this work, we characterize the performance of SWITCH-style Adaptive Bitrate (ABR) for both live and time-shifted clients in a Mininet simulated topology. We validate that standard ABR algorithms can be directly applied to time-shifted playback without modification, yielding substantially higher throughput. We demonstrate that a subscriber can experience increased overall throughput after a rebuffering scenario, and we identify focal points for further optimizations of MoQ ABR switching.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

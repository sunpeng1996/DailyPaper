---
title: LLM-Driven Heuristic Frame-Level Quantization Parameter Adaptation for VVenC
title_zh: LLM-Driven Heuristic Frame-Level Quantization Para
authors:
- Liqiang He
- Yingwen Zhang
- Riyu Lu
- Meng Wang
- Shiqi Wang
arxiv_id: '2606.20847'
url: https://arxiv.org/abs/2606.20847
pdf_url: https://arxiv.org/pdf/2606.20847
published: '2026-06-18'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Optimal frame-level quantization parameter (QP) allocation remains a persistent
  challenge in mo...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Optimal frame-level quantization parameter (QP) allocation remains a persistent challenge in modern video encoders. The fixed-QP scheme widely adopted in practical systems is inherently content-agnostic, while classical Lagrangian rate-distortion optimization (RDO) methods often suffer from inaccurate multiplier settings. In this paper, we explore the use of large language models (LLMs) to automatically design RDO heuristics for frame-level QP adaptation. We construct a closed-loop evolutionary framework in which the LLM iteratively proposes RDO heuristics as algorithmic ideas with executable code, and these candidates are evaluated directly through encoding with the Fraunhofer Versatile Video Encoder (VVenC), where each heuristic acts as a scoring function that compares different QP choices based on the encoding statistics of past frames and current candidates. Experimental results across multiple test sets show that the evolved heuristic achieves promising rate-distortion improvements over both the fixed-QP scheme and the Lagrangian baseline. Further analysis reveals that the LLM can autonomously discover an adaptive heuristic that penalizes QP fluctuations via entropy-based terms, providing new insights into the design of RDO algorithms

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

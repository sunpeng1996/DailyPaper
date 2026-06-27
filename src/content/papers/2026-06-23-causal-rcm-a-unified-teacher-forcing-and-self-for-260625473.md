---
title: 'Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive
  Diffusion Distillation in Streaming Video Generation and Interactive World Models'
title_zh: 'Causal-rCM: A Unified Teacher-Forcing and Self-For'
authors:
- Kaiwen Zheng
- Guande He
- Min Zhao
- Jintao Zhang
- Huayu Chen
- Jianfei Chen
- Chen-Hsuan Lin
- Ming-Yu Liu
- Jun Zhu
- Qianli Ma
arxiv_id: '2606.25473'
url: https://arxiv.org/abs/2606.25473
pdf_url: https://arxiv.org/pdf/2606.25473
published: '2026-06-23'
collected: '2026-06-26'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Autoregressive video diffusion with causal diffusion transformers has emerged
  as a major paradi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in diffusion distillation. This philosophy naturally carries over to the autoregressive setting, where teacher-forcing (TF) provides an offline, forward-divergence causal training paradigm, while self-forcing (SF) corresponds to an on-policy, reverse-divergence refinement. Our contributions are: (1) through extensive experiments, we show that teacher-forcing CM is currently the best complement to self-forcing DMD as an initialization strategy (2) we present the first implementation of teacher-forcing-based continuous-time CMs (e.g., sCM/MeanFlow) for autoregressive video diffusion, enabled by our custom-mask FlashAttention-2 JVP kernel, achieving 10times faster convergence compared to discrete-time CMs (dCMs) (3) we introduce Causal-rCM, a leading, unified, and scalable algorithm-infrastructure open recipe for diffusion distillation and causal training (4) we achieve state-of-the-art streaming video generation performance in both frame-wise and chunk-wise settings, using only synthetic data for training. Notably, our distilled 2-step causal Wan2.1-1.3B model achieves a VBench-T2V score of 84.63 with only 1 or 2 sampling steps. We further apply Causal-rCM to Cosmos 3, an advanced omnimodal world foundation model for physical AI with action-conditioned generation capability, enabling an interactive world model.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

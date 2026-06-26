---
title: 'ShutterMuse: Capture-Time Photography Guidance with MLLMs'
title_zh: 'ShutterMuse: Capture-Time Photography Guidance wit'
authors:
- Jiayu Li
- Yixiao Fang
- Tianyu Hu
- Wei Cheng
- Ping Huang
- Zheheng Fan
- Gang Yu
- Xingjun Ma
arxiv_id: '2606.25763'
url: https://arxiv.org/abs/2606.25763
pdf_url: https://arxiv.org/pdf/2606.25763
published: '2026-06-23'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Real-world photography requires capture-time guidance for both camera framing
  and subject pose....
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

Real-world photography requires capture-time guidance for both camera framing and subject pose. Yet existing aesthetic cropping benchmarks mainly evaluate post-hoc crop prediction and overlook subject-side recommendations, leaving the capture-time guidance capabilities of multimodal large language models (MLLMs) underexplored. To address this gap, we introduce CaptureGuide-Bench, a benchmark with two complementary tasks: photographer-side composition decision and refinement, and subject-side scene-conditioned pose recommendation. Our evaluation reveals limitations: general-purpose MLLMs can make composition decisions but lack precise refinement localization, while specialized aesthetic cropping models localize crops effectively but are limited to refinement; neither provides actionable pose guidance. To support model development, we further construct CaptureGuide-Dataset, comprising 130K samples with textual rationales and structured visual annotations, and develop ShutterMuse, a unified MLLM trained with supervised and reinforcement fine-tuning. Experiments on CaptureGuide-Bench show that ShutterMuse achieves the best overall photographer-side performance among evaluated baselines and competitive subject-side pose recommendation with substantially lower inference cost, demonstrating the potential of MLLMs as interactive assistants for photography during image capture.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

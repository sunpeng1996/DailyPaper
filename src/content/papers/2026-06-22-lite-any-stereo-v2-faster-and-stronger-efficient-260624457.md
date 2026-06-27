---
title: 'Lite Any Stereo V2: Faster and Stronger Efficient Zero-Shot Stereo Matching'
title_zh: 'Lite Any Stereo V2: Faster and Stronger Efficient'
authors:
- Junpeng Jing
- Ronglai Zuo
- Zhelun Shen
- Shangchen Zhou
- Rolandos Alexandros Potamias
- Stefanos Zafeiriou
- Krystian Mikolajczyk
- Jiankang Deng
arxiv_id: '2606.24457'
url: https://arxiv.org/abs/2606.24457
pdf_url: https://arxiv.org/pdf/2606.24457
published: '2026-06-22'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Recent advances in stereo matching have achieved remarkable accuracy, but
  often rely on large m...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: huggingface-daily
depth: abstract
---

### 摘要

Recent advances in stereo matching have achieved remarkable accuracy, but often rely on large models, heavy computation, or additional foundation-model priors, making them difficult to deploy on resource-constrained platforms. In contrast, efficient stereo models offer faster inference but are commonly considered less capable of strong zero-shot generalization. In this paper, we challenge this assumption by introducing Lite Any Stereo V2 (LAS2), an ultra-fast model series designed for efficient zero-shot stereo matching. LAS2 is developed from both architecture and training perspectives. Architecturally, we revisit efficient stereo design under practical deployment settings and propose a 2D-only cost aggregation framework, optimized for real inference latency rather than theoretical MACs alone. For training, we develop a three-stage strategy that combines synthetic supervision, self-distillation, and real-world knowledge distillation. To improve the reliability of real-world pseudo supervision, we further introduce pseudo-label filtering and an error-clamping operation, enabling smoother synthetic-to-real transfer. We instantiate LAS2 as a family of models, including feed-forward variants for different efficiency budgets and an iterative variant for higher accuracy. Extensive experiments show that LAS2 achieves state-of-the-art accuracy among efficient stereo methods while maintaining significantly lower latency. Specifically, LAS2-H achieves stronger overall zero-shot performance than the iterative method Fast-FoundationStereo, with 1.8x and 2.7x faster inference on H200 and Orin, respectively. The project page, demos, and code are available at https://tomtomtommi.github.io/LiteAnyStereoV2/.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

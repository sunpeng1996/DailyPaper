---
title: 'UI-LIC: A Unified Framework for Evaluating Learned Image Compression Models'
title_zh: 'UI-LIC: A Unified Framework for Evaluating Learned'
authors:
- Nicholas J. Nolen
- Luc Trudeau
- Andrew C. Freeman
arxiv_id: '2606.23545'
url: https://arxiv.org/abs/2606.23545
pdf_url: https://arxiv.org/pdf/2606.23545
published: '2026-06-22'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: The evaluation and comparison of Learned Image Compression (LIC) systems
  is complicated by hete...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 摘要

The evaluation and comparison of Learned Image Compression (LIC) systems is complicated by heterogeneous software stacks, varying training conditions, and divergent evaluation methodologies. To address these challenges, we introduce UI-LIC, an open-source software framework for evaluating LIC models. We integrate six high-performance LIC models, and provide a centralized controller for performing training, inference, and analysis with shared configuration parameters. Our GUI program offers a streamlined interface to evaluate these models alongside traditional video intra-frame encoders, equalizing the compressed bitrates and calculating quality metrics such as PSNR, SSIM, VMAF, and LPIPS. Finally, we provide an interactive image analyzer with configurable quality heatmap overlays. Our framework lowers barriers to further LIC research, unlocking comparative metrics and subjective analysis with a single setup command. The open-source software is released under the MIT license and is available at github.com/BaylorMultimediaLab/UI-LIC.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

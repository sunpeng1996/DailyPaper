---
title: 'SPORT: Spherical-PSNR-Optimized tRuncaTion for Power-Efficient 360-Degree
  Video Systems'
title_zh: 'SPORT: Spherical-PSNR-Optimized tRuncaTion for Pow'
authors:
- Md. Sajjad Hossain
- Hasibur Rahman Hemel
- Kyle Mooney
- Yiwen Xu
- William Oswald
- Mario Renteria-Pinon
- Hritom Das
- Zhenlin Pei
- Jinhui Wang
- Na Gong
arxiv_id: '2606.24916'
url: https://arxiv.org/abs/2606.24916
pdf_url: https://arxiv.org/pdf/2606.24916
published: '2026-06-19'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Memory bandwidth accounts for 30-40% of total power consumption in standalone
  virtual reality (...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Memory bandwidth accounts for 30-40% of total power consumption in standalone virtual reality (VR) headsets, yet existing systems typically store the entire 360-degree frame at a uniform resolution regardless of viewer gaze. This paper presents SPORT (Spherical-PSNR Optimized tRuncaTion), a bit-truncation framework that reduces display-path memory power by storing only the most significant bits of pixels outside the user's field of view (FoV). Specifically, a new bit-truncation framework is developed to use weighted-to-spherically-uniform PSNR (WS-PSNR) directly in the optimization constraint, eliminating the metric inconsistency that arises when standard PSNR is used for a WS-PSNR quality target. Also, gaze-predictive tile classification compensates for the 9.33 ms end-to-end pipeline latency, reducing boundary misclassifications by 5.2 percentage points at a cost of only 0.01 ms. In addition, the developed SPORT-B variant, which keeps the FoV lossless, achieves 47.9% memory power saving and 47.9% bandwidth reduction across different 4K video sequences while satisfying all three per-region WS-PSNR thresholds and maintaining SSIM = 1.000 in the attended region. The full adaptive variant SPORT-A reaches 51.6% power saving, 3.1percentage points more than a PSNR-based optimizer at equal measured quality. SPORT is validated on the TrunMEM360 flexible SRAM Application-Specific Integrated Circuit (ASIC) fabricated in SkyWater 130 nm CMOS, confirming byte-exact silicon-software agreement, with WS-PSNR and SSIM matching within 0.1 dB and 0.001. CACTI-based analysis confirms 48.72% DRAM leakage reduction and 36.4%/36.7% read/write energy reduction. The total motion-to-photon latency of 9.33 ms satisfies the 20 ms VR comfort budget with a 53.3% safety margin.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

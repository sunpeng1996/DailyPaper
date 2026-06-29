---
title: 'RPM-Distill: Physiology-guided Adaptive Cross-modal Distillation for Robust
  Remote Physiological Measurement'
title_zh: 'RPM-Distill: Physiology-guided Adaptive Cross-moda'
authors:
- Jiyao Wang
- Qingyong Hu
- Duoxun Tang
- Xiao Yang
- Kaishun Wu
- Jiangbo Yu
arxiv_id: '2606.28089'
url: https://arxiv.org/abs/2606.28089
pdf_url: https://arxiv.org/pdf/2606.28089
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Video-based remote physiological measurement (RPM) is highly accessible
  but remains fragile und...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Video-based remote physiological measurement (RPM) is highly accessible but remains fragile under varying illumination, skin tones, and motion. Radio frequency (RF) radar is largely invariant to illumination and appearance, providing complementary cardio-respiratory micro-motion cues; however, requiring radar at inference is often impractical due to its limited ubiquity and deployment overhead. We propose RPM-Distill, a physiology-guided cross-modal distillation framework that leverages synchronized radar only during training while retaining video-only inference. Our key observation is that although RGB and RF waveforms differ in sensing physics and time-domain morphology, they share similar latent periodic rhythm in the frequency domain. We thus distill physiology-structured spectral evidence to improve robustness, via losses that (i) anchor the fundamental peak, (ii) match the off-peak background distribution, and (iii) preserve spectral morphology and sharpness. To avoid negative transfer under sample-level teacher quality and alignment uncertainty, a spectral policy network predicts sample-level distillation gates and component weights from the student--teacher spectral relation map, learned with a meta bilevel objective on a small labeled validation split. Through extensive experiments in challenging conditions and cross-dataset settings, RPM-Distill brings 81\% MAE and 21\% correlation improvement over unimodal baselines. Code is at https://github.com/WJULYW/RPM-Distill.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

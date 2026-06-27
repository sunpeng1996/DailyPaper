---
title: 'OctoSense: Self-Supervised Learning for Multimodal Robot Perception'
title_zh: 'OctoSense: Self-Supervised Learning for Multimodal'
authors:
- Anthony Bisulco
- Jeremy Wang
- Kostas Daniilidis
- Randall Balestriero
- Pratik Chaudhari
arxiv_id: '2606.27317'
url: https://arxiv.org/abs/2606.27317
pdf_url: https://arxiv.org/pdf/2606.27317
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We present OctoSense, an open-source sensor platform with stereo RGB and
  event cameras, LiDAR,...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 摘要

We present OctoSense, an open-source sensor platform with stereo RGB and event cameras, LiDAR, a thermal camera, an inertial measurement unit, RTK-corrected global positioning system, and proprioception (CAN bus data from a car, and joint angles for a quadruped robot). The eponymous OctoSense dataset contains 59 hours of time-synchronized driving data across different types of environments at different times of the day, including situations with highly degraded sensors. We demonstrate multi-modal self-supervised learning using such real-world robotics data, where sensors have different representations, frequencies, latencies and noise. Our approach, a "late-fusion" masked autoencoder, (i) uses modality-specific tokenizers to account for different spatiotemporal characteristics of these sensors, and (ii) caches modality-specific tokens at inference time to process new measurements as they come. This architecture (i) is fast (6.68 ms and 112 ms on NVIDIA 5090 and Orin NX respectively, to compute the representation), (ii) performs better than existing image-only foundation models on tasks such as estimation of optical flow, depth, semantic segmentation, and ego-motion (translation, rotation, and steering angle), and (iii) predicts robustly at nighttime or in situations where sensory data is degraded. See our project page for links to the dataset, code, and supplementary videos: https://abisulco.com/octosense/.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

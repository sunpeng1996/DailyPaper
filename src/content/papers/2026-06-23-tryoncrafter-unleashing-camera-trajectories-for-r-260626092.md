---
title: 'TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on
  via a Renderable 4D Try-on Proxy'
title_zh: 'TryOnCrafter: Unleashing Camera Trajectories for R'
authors:
- Hao Sun
- Hao Yan
- Mengting Chen
- Quanjian Song
- Yu Li
- Juan Cao
- Jinsong Lan
- Xiaoyong Zhu
- Bo Zheng
- Sheng Tang
arxiv_id: '2606.26092'
url: https://arxiv.org/abs/2606.26092
pdf_url: https://arxiv.org/pdf/2606.26092
published: '2026-06-23'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing
  realistic gar...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: huggingface-daily
depth: abstract
---

### 摘要

While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and 360-degree orbital viewing.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

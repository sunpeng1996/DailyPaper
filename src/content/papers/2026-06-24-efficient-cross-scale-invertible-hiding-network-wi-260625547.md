---
title: Efficient Cross-Scale Invertible Hiding Network with Spatial-Frequency Collaboration
  and Non-Invertible Mechanism
title_zh: Efficient Cross-Scale Invertible Hiding Network wi
authors:
- Junxue Yang
- Xin Liao
arxiv_id: '2606.25547'
url: https://arxiv.org/abs/2606.25547
pdf_url: https://arxiv.org/pdf/2606.25547
published: '2026-06-24'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Image hiding aims to conceal image-level messages within cover images at
  the same resolution. I...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Image hiding aims to conceal image-level messages within cover images at the same resolution. Invertible neural networks (INN)-based image hiding has emerged as an important branch. It treats concealing and revealing as a pair of inverse problems on image domain transformation and uses INN's forward and backward processes to address them. Due to architectural constraints, existing INN-based methods suffer from single-scale and single-domain feature extraction and limited nonlinear representation capability, resulting in inferior image quality. To mitigate these limitations, we propose an efficient cross-scale invertible hiding network with the spatial-frequency collaboration and the non-invertible mechanism, termed CrosInv. CrosInv exploits cross-scale and spatial-frequency collaborative features while enhancing nonlinear representation. Specifically, we introduce a cross-scale invertible module that bijectively maps inputs to cross-scale representations. To effectively integrate spatial and frequency information, the cross-scale invertible module employs pixel shuffle, Haar wavelet transformation, and their inverse operations for scale transformation. Furthermore, a non-invertible cross dense module is integrated to enhance the nonlinearity. Comprehensive experiments verify the effectiveness and superiority of the proposed CrosInv.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

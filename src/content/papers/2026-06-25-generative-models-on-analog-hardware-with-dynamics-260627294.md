---
title: Generative Models on Analog Hardware with Dynamics
title_zh: Generative Models on Analog Hardware with Dynamics
authors:
- Yu-Neng Wang
- Sara Achour
arxiv_id: '2606.27294'
url: https://arxiv.org/abs/2606.27294
pdf_url: https://arxiv.org/pdf/2606.27294
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Analog hardware platforms such as coupled oscillators and Analog Ising
  Machines naturally solve...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Analog hardware platforms such as coupled oscillators and Analog Ising Machines naturally solve differential equations at a fraction of the energy cost of digital computation, making them attractive for low-power generative modeling, yet a fundamental mismatch exists: modern generative models assume flexible, software-defined dynamics, whereas analog hardware imposes fixed, physics-determined differential equations with limited approximation capacity. This paper introduces Analog Interaction Systems (AIS), a unified framework for hardware-implementable dynamical systems, and empirically characterizes their expressivity gap relative to neural network baselines. Two hardware-compatible mechanisms are proposed to narrow this gap - time-varying piecewise parameters and hidden physical states - and a Wasserstein GAN training procedure is developed to enable training of these models without requiring them to follow a specific trajectory. We characterize how area and power scale with connection density and precision, showing that sparse connectivity and low-bit-width quantized parameters are necessary for practical implementation, and estimate an energy cost of 23uJ per generated image for the chosen architecture, representing a 2-orders-of-magnitude improvement over digital baselines. On MNIST and Fashion-MNIST, our oscillator-based AIS achieves FID scores of 27.6 and 80.8, outperforming the best prior hardware-implementable analog generative models by 3-4x with a 4-bit sparse architecture.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

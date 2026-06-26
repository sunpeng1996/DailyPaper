---
title: 'PhysiFormer: Learning to Simulate Mechanics in World Space'
title_zh: 'PhysiFormer: Learning to Simulate Mechanics in Wor'
authors:
- Yiming Chen
- Yushi Lan
- Andrea Vedaldi
arxiv_id: '2606.27364'
url: https://arxiv.org/abs/2606.27364
pdf_url: https://arxiv.org/pdf/2606.27364
published: '2026-06-24'
collected: '2026-06-26'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We present PhysiFormer, a diffusion transformer for physically-plausible
  3D object motion. Unli...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality, PhysiFormer shows that excellent results can be obtained without any such inductive biases, by casting vertex trajectory prediction as a single denoising diffusion process directly in world coordinates. The probabilistic formulation captures uncertainty in the learned dynamics, enabling diverse plausible futures from initial conditions, making this framework potentially useful for applications with unobserved uncertainty. The model features attention factorised over time, space, and objects for efficiency, enabling permutation-invariant multi-object reasoning without needing explicit object encoding. Trained on over 100k simulated trajectories, PhysiFormer generates rigid and elastic mechanics, and generalises to mixed-material settings, unseen real-world geometries, and larger object counts. It substantially outperforms autoregressive baselines in trajectory accuracy, rigidity preservation, and momentum-based physical consistency. Our results position coordinate-space diffusion as a promising step toward view-invariant, geometry-aware world modelling for robotics, graphics, and physical design. Visualisations, code, and models are available at https://yimingc9.github.io/physiformer.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

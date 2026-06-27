---
title: 'Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN'
title_zh: 'Sculpting NeRF Geometry: Human-Preference Fine-Tun'
authors:
- Archer Moore
- Mingming Gong
- Liam Hodgkinson
arxiv_id: '2606.27305'
url: https://arxiv.org/abs/2606.27305
pdf_url: https://arxiv.org/pdf/2606.27305
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Reinforcement learning from human feedback (RLHF) for 3D generation is
  now established across a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by converting radiance fields into meshes and training heavily on surface-supervised data. We instead fine-tune a pretrained 3D-aware generative model directly from a learned reward over radiance-field density ($σ$) values, with no externally supplied mesh or shape prior. The reward model requires no pretraining, trains easily on a small set of preference samples, and yields robust improvement in 3D geometry. Working on an unconditional 3D-aware face GAN (EG3D), our reward reads the continuous 3D density field of the neural radiance field (NeRF) directly and supplies a geometry-only learning signal, requiring neither text conditioning, mesh extraction, nor multi-view rendering. A density-consistency constraint keeps the 2D appearance qualitatively similar while the geometry is reshaped, at a measurable but bounded distributional cost (FID-50k rises from 4.09 to 6.66): the fine-tuned generator, trained from the preferences of a single annotator as a proof of concept, produces face geometries preferred by users in 74.4% of pairwise comparisons.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

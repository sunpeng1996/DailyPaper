---
title: 'RoPEMover: Depth-Aware Object Relocation via Positional Embeddings'
title_zh: 'RoPEMover: Depth-Aware Object Relocation via Posit'
authors:
- Ipek Oztas
- Duygu Ceylan
- Aybars Bugra Aksoy
- Aysegul Dundar
arxiv_id: '2606.27332'
url: https://arxiv.org/abs/2606.27332
pdf_url: https://arxiv.org/pdf/2606.27332
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Moving an object in a single image requires geometry-consistent spatial
  rearrangement, includin...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Moving an object in a single image requires geometry-consistent spatial rearrangement, including handling occlusions, revealing previously unseen regions, and maintaining coherent shadows and reflections. Existing approaches are not well suited to this setting and often fail to preserve such scene-level consistency. We address this problem by introducing a geometry-aware object motion method that operates directly on the positional representations of diffusion transformers. Our key insight is that rotary positional embeddings (RoPE) define a structured spatial field that can be explicitly manipulated to induce controlled motion. We extend 2D RoPE into a depth-aware formulation that encodes 3D spatial structure, enabling consistent object displacement and scene-aware updates. Our model is trained using synthetic data combined with a small set of real images via parameter-efficient fine-tuning. Despite minimal real supervision, it preserves object identity under large spatial displacements, generates plausible content in newly revealed regions, and consistently updates scene-dependent effects such as shadows and illumination. Experimental results on standard object motion benchmarks demonstrate state-of-the-art performance across all evaluation metrics.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

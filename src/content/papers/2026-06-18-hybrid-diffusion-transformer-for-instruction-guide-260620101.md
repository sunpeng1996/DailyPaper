---
title: Hybrid Diffusion Transformer for Instruction-Guided Audio Editing via Rectified
  Flow
title_zh: Hybrid Diffusion Transformer for Instruction-Guide
authors:
- Liting Gao
- Yonggang Zhu
- Yaru Chen
- Dongyu Wang
- Shubin Zhang
- Zhenbo Li
- Jean-Yves Guillemaut
- Wenwu Wang
arxiv_id: '2606.20101'
url: https://arxiv.org/abs/2606.20101
pdf_url: https://arxiv.org/pdf/2606.20101
published: '2026-06-18'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Audio editing aims to modify specific content in an existing audio clip
  according to a natural...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Audio editing aims to modify specific content in an existing audio clip according to a natural language instruction while preserving the remaining acoustic content. Despite the remarkable progress of diffusion models, existing training-based editing methods mainly rely on the local inductive biases and cross-attention interaction in convolutional U-Net backbones, which often hinder long-range semantic alignment and precise understanding and localization of instructions. In contrast, diffusion transformers provide stronger global modeling and multimodal fusion, but existing editing architectures usually adopt a simple stack of MMDiT and DiT blocks. Applying joint attention over concatenated audio and text tokens in all blocks results in quadratic complexity with respect to token length. To balance editing performance and efficiency, we propose a hybrid two-stage diffusion transformer architecture for instruction-guided audio editing based on rectified flow matching. It performs joint attention over audio and text tokens to establish coarse semantic alignment at low-resolution stage, then switches to alternating joint-attention and cross-attention blocks to refine editing details at high-resolution stage. This coarse-to-fine strategy enables efficient and accurate instruction-guided audio editing. Experiments show that the proposed framework achieves notable performance gains on challenging editing tasks involving overlapping audio events and complex instructions, while substantially improving editing efficiency with a compact model.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

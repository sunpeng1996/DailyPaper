---
title: Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow
  Models via Feature Self-Guidance
title_zh: Don't Settle at the Mode! Mitigating Diversity Col
authors:
- Pradhaan S Bhat
- Rishubh Parihar
- Abhijnya Bhat
- R. Venkatesh Babu
arxiv_id: '2606.27371'
url: https://arxiv.org/abs/2606.27371
pdf_url: https://arxiv.org/pdf/2606.27371
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: State-of-the-art flow models generate stunning images from text or image
  prompts. However, they...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 摘要

State-of-the-art flow models generate stunning images from text or image prompts. However, they suffer from diversity collapse when generating multiple samples under the same conditioning. Existing methods address this issue via either latent guidance, which has limited effectiveness, or sample selection, which relies on external reward models that incur significant inference-time overhead. In this work, we introduce an efficient, training-free self-guidance mechanism to mitigate diversity collapse without requiring additional reward models. Specifically, we disperse the internal features of the flow model during batch generation with feature self-guidance. Further, to keep the features close to the manifold, we introduce a manifold regularization step that projects these dispersed features back onto the data manifold, ensuring diverse generation without sacrificing alignment with the input conditions. Our method integrates seamlessly as a plug-and-play module into pretrained flow models, adding only a marginal inference cost. Experiments demonstrate significant improvements in diversity while preserving fidelity across several conditional flow models, including multi-step and few-step text-to-image, depth-to-image, and reference image generation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

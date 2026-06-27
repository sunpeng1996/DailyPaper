---
title: 'DanceOPD: On-Policy Generative Field Distillation'
title_zh: 'DanceOPD: On-Policy Generative Field Distillation'
authors:
- Wei Zhou
- Xiongwei Zhu
- Zelin Xu
- Bo Dong
- Lixue Gong
- Yongyuan Liang
- Meng Chu
- Leigang Qu
- Lingdong Kong
- Wei Liu
arxiv_id: '2606.27377'
url: https://arxiv.org/abs/2606.27377
pdf_url: https://arxiv.org/pdf/2606.27377
published: '2026-06-24'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Modern image generation demands a single model that unifies diverse capabilities,
  including tex...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD, an on-policy generative field distillation framework for flow-matching models that routes each sample to one capability field, queries one low-noise student-induced state, and trains with a simple velocity MSE objective. With each capability source defined as a velocity field over the shared flow state space, the student learns from fields queried on its own rollout states to compose expert capabilities. This formulation also absorbs operator-defined fields such as classifier-free guidance. Comprehensive experiments on T2I, editing, realism-field absorption, and CFG absorption show that our approach improves multi-capability composition, strengthening target capabilities while preserving anchor generation quality. We believe this work establishes a practical route for generative field distillation in flow-matching models.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

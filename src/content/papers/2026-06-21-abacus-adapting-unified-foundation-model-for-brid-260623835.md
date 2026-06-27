---
title: 'ABACUS: Adapting Unified Foundation Model for Bridging Image Count Understanding
  and Generation'
title_zh: 'ABACUS: Adapting Unified Foundation Model for Brid'
authors:
- Anindya Mondal
- Sauradip Nag
- Anjan Dutta
arxiv_id: '2606.23835'
url: https://arxiv.org/abs/2606.23835
pdf_url: https://arxiv.org/pdf/2606.23835
published: '2026-06-21'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: ABACUS is a unified vision-language model that handles object counting,
  crowd counting, referri...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: huggingface-daily
depth: abstract
---

### 摘要

ABACUS is a unified vision-language model that handles object counting, crowd counting, referring-expression counting, and count-faithful image generation without any benchmark-specific training required. Our model is built on existing 3B-parameter unified foundation model and is adapted for object localization tasks using three key innovations: density-aware adaptive zooming with objectness maps for spatial grounding; a boundary-aware count policy via GRPO to eliminate crop-boundary errors; and a cycle-consistent GRPO strategy where the understanding branch self-critiques generated outputs, closing the understanding-generation gap without any external annotations. ABACUS achieves state-of-the-art results across seven benchmarks, outperforming both task-specific specialists and larger generalist models.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

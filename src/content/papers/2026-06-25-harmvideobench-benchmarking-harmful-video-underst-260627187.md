---
title: 'HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal
  Models'
title_zh: 'HarmVideoBench: Benchmarking Harmful Video Underst'
authors:
- Jiajun Wu
- Haoyu Kang
- Yining Sun
- Jiacheng Hou
- Heng Zhang
- Danyang Zhang
- Zhenjun Zhao
- Haochi Zhang
- Leixin Sun
- Eric Hanchen Jiang
arxiv_id: '2606.27187'
url: https://arxiv.org/abs/2606.27187
pdf_url: https://arxiv.org/pdf/2606.27187
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Large vision-language models (LVLMs) have recently shown immense potential
  in automated content...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Large vision-language models (LVLMs) have recently shown immense potential in automated content moderation, sparking growing interest in developing harmful-video benchmarks. However, we identify two primary limitations in existing works: 1) The multi-layered characteristics of harmful videos are overlooked. Existing benchmarks predominantly formulate evaluation as a binary classification task, failing to capture implicit or deep contextual harms. 2) Explanatory rationales are completely absent. Current frameworks measure exclusively whether a model flags a video correctly rather than explaining why, turning evaluation into a black box where models can succeed through superficial shortcuts. To address these problems, we present HarmVideoBench, a multi-layered diagnostic benchmark comprising 1,379 videos paired with 4,137 multiple-choice questions. HarmVideoBench benchmarks three hierarchical dimensions: Observable Evidence, Clip-Internal Meaning, and Beyond-Clip Reasoning, aiming to evaluate models' deep understanding beyond surface cues with carefully balanced and curated samples. We evaluate 19 leading models on HarmVideoBench to assess their multidimensional understanding of harmful videos. Moreover, we introduce BCR, a benchmark-aligned method that predicts reasoning boundaries and dynamically retrieves context only when needed. Experimental results show that BCR substantially improves the base model's performance in harmful video understanding, raising the macro average from 61.7 percent to a state-of-the-art 84.4 percent.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

---
title: 'Catching Lies Without Sending the Video: Privacy-Preserving Multimodal Deception
  Detection'
title_zh: 'Catching Lies Without Sending the Video: Privacy-P'
authors:
- Nikita Sharma
- Pranav Sara
- Karan Singla
arxiv_id: '2606.22699'
url: https://arxiv.org/abs/2606.22699
pdf_url: https://arxiv.org/pdf/2606.22699
published: '2026-06-21'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Frontier multimodal models can guess whether a person is lying from a testimony
  video. To do so...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Frontier multimodal models can guess whether a person is lying from a testimony video. To do so, they stream that raw face and voice to a third-party model. We ask whether the heavy media is needed at all. On the Real-life Trial Deception dataset, Whissle on-device speech and vision stack extracts a compact digest: transcript, emotion, age, gender, intent distributions, a deception intent filter, fluency and rhythm, per-frame facial behaviour, and prosody. Under speaker-independent evaluation, we report three findings. A small classifier on this digest reaches AUC 0.741, matching Gemini 2.5 Pro on full video. Handing the digest to a frontier LLM reaches AUC 0.755 with Claude Opus 4.8 at 7.8X fewer input tokens, with no media leaving the device. The reported 75% accuracy is a speaker-leakage artifact. We release code and experiments.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

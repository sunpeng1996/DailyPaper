---
title: 'From Sounds to Scenes: A Benchmark for Evaluating Context-Aware Auditory Scene
  Understanding in Large Audio Language Models'
title_zh: 'From Sounds to Scenes: A Benchmark for Evaluating'
authors:
- Pengfei Zhang
- Hoang H Nguyen
- Kazi Shaharair Sharif
- Yutong Song
- Wenjun Huang
- Henry Peng Zou
- Pinxin Liu
- Honghui Xu
- Amir M. Rahmani
arxiv_id: '2606.25391'
url: https://arxiv.org/abs/2606.25391
pdf_url: https://arxiv.org/pdf/2606.25391
published: '2026-06-24'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Recent Large Audio Language Models (LALMs) have achieved remarkable progress
  in audio perceptua...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Recent Large Audio Language Models (LALMs) have achieved remarkable progress in audio perceptual tasks across individual acoustic layers, including speech, sound, and music. However, existing benchmarks predominantly evaluate these layers in isolation, overlooking the complex contextual relationships that arise when multiple acoustic sources co-occur in real-world auditory scenes. Real-world auditory interpretation requires Context-Aware Auditory Scene Understanding (CASU): the ability to comprehend the holistic scene by integrating sound layers. To evaluate this capability, we introduce the CASU benchmark, which assesses whether Audio LLMs can interpret auditory scenes composed of speech, acoustic events (e.g., announcements), and background environments (e.g., traffic), and reason about the logical relationships between these layers. We propose a scalable pipeline for constructing time-accurate, semi-synthetic audio streams by composing real-world scene sounds with synthetic speech. Building on this data, we design four tasks that probe scene understanding: contextual question answering, entity extraction from the scene, speaker role inference, and counterfactual reasoning where scene is manipulated. Experiments across multiple LALMs demonstrate that effective auditory scene understanding requires integration over all auditory layers, rather than reliance on speech or sound alone, underscoring the necessity of CASU for advancing complex audio understanding in LALMs.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

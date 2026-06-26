---
title: 'UnityShots: Memory-Driven Multi-Shot Audio-Video Generation with Boundary-Aware
  Gating'
title_zh: 'UnityShots: Memory-Driven Multi-Shot Audio-Video G'
authors:
- Jiehui Huang
- Yuechen Zhang
- Bin Xia
- Jiahao Wang
- Xu He
- Zhenchao Tang
- Meng Chu
- Xin Tao
- Pengfei Wan
- Jiaya Jia
arxiv_id: '2606.21661'
url: https://arxiv.org/abs/2606.21661
pdf_url: https://arxiv.org/pdf/2606.21661
published: '2026-06-18'
collected: '2026-06-26'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Generating a coherent multi-shot video requires structured cross-shot memory.
  Subject appearanc...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Generating a coherent multi-shot video requires structured cross-shot memory. Subject appearance, scene context, and speaker identity must persist across cuts. Existing approaches either train end-to-end over fixed-length sequences and cannot scale, generate shot-by-shot with memory banks that grow linearly, or orchestrate pretrained generators under an LLM planner without a multi-shot-aware backbone. We present UnityShots, a memory-driven multi-shot audio-video generation system built on LTX-2.3, trained on annotated cinematic and music-video shots. The video stream maintains two fixed-size slots, a long-term memory (LTM) slot anchored to the opening shot and a short-term memory (STM) slot holding the immediately preceding tail, both updated at every cut by a boundary-conditioned gate that fuses visual cut probability and beat-tracker signals. The audio stream injects a reference speaker token at every shot to preserve vocal timbre without a sliding audio bank. A discrete cut-type prior, learned through AdaLN, becomes an inference-time control knob over transition strength. We release a benchmark of 200 multi-cultural multi-shot sequences spanning six ethnic regions and ten or more languages, with per-shot reference identities, reference audio, and per-boundary transition labels. Evaluated across I2V, T2V, and R2V conditioning modes, UnityShots leads open-source baselines on every cross-shot coherence metric and matches the strongest closed-source system on the multi-shot axes.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

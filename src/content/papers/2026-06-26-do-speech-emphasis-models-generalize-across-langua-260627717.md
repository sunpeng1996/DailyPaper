---
title: Do Speech Emphasis Models Generalize across Languages and Emotions?
title_zh: Do Speech Emphasis Models Generalize across Langua
authors:
- Megan Wei
- Deepali Aneja
- Jiaqi Su
- Yunyun Wang
- Haonan Chen
- Zeyu Jin
arxiv_id: '2606.27717'
url: https://arxiv.org/abs/2606.27717
pdf_url: https://arxiv.org/pdf/2606.27717
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Prosodic emphasis varies across languages, emotions, and speaking styles,
  yet existing emphasis...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Prosodic emphasis varies across languages, emotions, and speaking styles, yet existing emphasis detection models are largely trained and evaluated on monolingual neutral read speech. We introduce MMEE (Multilingual Multi-Emotion Emphasis), a corpus of 10,000 professionally recorded expressive utterances (14.13 hours) across 7 languages and 34 emotion/style categories, with three-level perceptual labels (10 annotations per sample). We benchmark two state-of-the-art architectures under monolingual, cross-lingual, multilingual, cross-emotion, cross-dataset, and data-scale settings. Monolingual models show limited zero-shot transfer, degrading across typologically distant languages, while multilingual training substantially improves robustness. Models transfer robustly between high- and low-arousal emotions; bidirectional transfer between synthetic and perceptual benchmarks suggests shared prosodic structure; and performance stays robust even at smaller training scales.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

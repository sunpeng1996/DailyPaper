---
title: Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs
title_zh: Where Do Models Find Happiness? Emotion Vectors in
authors:
- Sinie van der Ben
- Raphaël Baur
- Yannick Metz
- Mennatallah El-Assady
arxiv_id: '2606.26987'
url: https://arxiv.org/abs/2606.26987
pdf_url: https://arxiv.org/pdf/2606.26987
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Recent work identified emotion vectors in Claude Sonnet 4.5, which are
  internal representations...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Recent work identified emotion vectors in Claude Sonnet 4.5, which are internal representations that encode emotion concepts, causally influence behavior, and exhibit geometry mirroring human psychological structure. We test the generality of these findings in two open-weight models, Apertus-8B-Instruct-2509 and Gemma-4-E4B-it, extracting emotion contrast vectors across all layers, using two model-generated corpora. We recover valence geometry for both models, with peak PC1--valence correlations of $r = 0.76$ and $r = 0.83$, approaching the $r = 0.81$ reported for Claude.Beyond replication, we observe notable differences in how valence representations emerge across model depth. In Gemma-4-E4B-it, valence is strongly encoded in early layers but collapses towards later layers, whereas Apertus-8B-Instruct-2509 exhibits the opposite pattern, with valence representations absent in early layers, but emerging at mid depths. Arousal encoding, in contrast, is sensitive to the extraction corpus: both models show stronger PC2--arousal alignment with Gemma-generated stories ($r$ up to $0.45$) than Apertus-generated ones ($r \leq 0.21$), suggesting arousal-relevant cues are unevenly distributed across generated corpora. We open-source our experiment code and dataset for reproducible investigation of emotion representations across language model architectures.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

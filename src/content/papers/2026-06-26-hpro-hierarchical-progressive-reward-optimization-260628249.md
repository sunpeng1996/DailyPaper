---
title: 'HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction
  for Emotional Text-to-Speech'
title_zh: 'HPRO: Hierarchical Progressive Reward Optimization'
authors:
- Sihang Nie
- Xiaofen Xing
- Rui Xing
- Haoming Li
- Ruitong Xiao
- Jingyuan Xing
- Baiji Liu
- Xiangmin Xu
arxiv_id: '2606.28249'
url: https://arxiv.org/abs/2606.28249
pdf_url: https://arxiv.org/pdf/2606.28249
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Recently, Large Language Model (LLM)-based Text-to-Speech (TTS) models
  have achieved remarkable...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Recently, Large Language Model (LLM)-based Text-to-Speech (TTS) models have achieved remarkable naturalness. However, the standard Supervised Fine-Tuning paradigm often converges to statistically averaged prosody, limiting emotional expressiveness. While preference-driven optimization offers a promising alternative, existing approaches suffer from two structural mismatches: information conflict, where content and emotion in a shared latent space produce conflicting gradients, leading to reward hacking and semantic degradation; and scale gap, where sparse sentence-level rewards struggle to guide dense frame-level generation. To overcome these challenges, we propose HPRO, a hierarchical progressive reward optimization framework. Within HPRO, we introduce the HD-Emo codec as a novel differentiable reward model to resolve the information conflict. It extracts speech into distinct content and style preference tokens, structurally isolating emotional optimization from semantic content. Building upon this structured preference space, HPRO bridges the scale gap by progressively aligning frame-, word- and sentence-level objectives. Experiments demonstrate that HPRO significantly enhances emotional expressiveness, while effectively preserving linguistic intelligibility. The code and audio samples are publicly available at https://xxh333.github.io/hpro-demo/.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

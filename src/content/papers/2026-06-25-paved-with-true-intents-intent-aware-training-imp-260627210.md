---
title: 'Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification
  Across Training Regimes'
title_zh: 'Paved with True Intents: Intent-Aware Training Imp'
authors:
- Jeremias Ferrao
- Niclas Müller-Hof
- Iustin Sîrbu
- Traian Rebedea
- Yftah Ziser
arxiv_id: '2606.27210'
url: https://arxiv.org/abs/2606.27210
pdf_url: https://arxiv.org/pdf/2606.27210
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: We argue that safety classifiers should model user intent as an explicit
  signal between the pro...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. Despite its size, AIMS enables competitive safety classifiers across training regimes: DPO from model-generated intent errors improves over SFT, and intent-conditioned distillation outperforms reasoning-only distillation in most teacher-student pairs. Most notably, directly rewarding intent faithfulness with GRPO yields the strongest average performance across five external safety benchmarks, while our intent-aware models form the inference latency-F1 Pareto frontier. These results show that faithful intent modeling is a compact, high-quality supervision signal for more robust safety classifiers.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

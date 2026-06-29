---
title: Tandem Reinforcement Learning with Verifiable Rewards
title_zh: Tandem Reinforcement Learning with Verifiable Rewa
authors:
- Difan Jiao
- Raghav Singhal
- Robert West
- Ashton Anderson
arxiv_id: '2606.28166'
url: https://arxiv.org/abs/2606.28166
pdf_url: https://arxiv.org/pdf/2606.28166
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Reinforcement learning with verifiable rewards (RLVR) has significantly
  improved the reasoning...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capability of large language models, reaching expert or even superhuman performance in domains such as competition math. However, whether weaker agents and humans can actually harness this capability is far less certain, with RLVR documented to drift reasoning toward idiosyncratic patterns such as poor readability and language mixing. Tandem training is a recently introduced paradigm that targets this compatibility problem: a trained, stronger senior co-generates each rollout with a frozen, weaker junior, and the two are rewarded as a team, so the senior is pushed to reason in ways the junior can follow. Yet this paradigm has so far been demonstrated only in proof-of-concept settings, leaving open whether it scales to the long chains of thought of the modern RLVR pipeline. In this work, we propose Tandem Reinforcement Learning (TRL), which carries the tandem training paradigm into RLVR. In TRL, the senior and a frozen junior alternate stochastically to co-generate the reasoning, the resulting generation is rewarded, and the standard GRPO loss is applied to the senior. Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. Our results demonstrate a promising route for RLVR with practical payoffs in multi-model communication and human compatibility.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

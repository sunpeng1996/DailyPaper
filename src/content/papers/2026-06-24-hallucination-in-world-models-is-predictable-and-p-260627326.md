---
title: Hallucination in World Models is Predictable and Preventable
title_zh: Hallucination in World Models is Predictable and P
authors:
- Nicklas Hansen
- Xiaolong Wang
arxiv_id: '2606.27326'
url: https://arxiv.org/abs/2606.27326
pdf_url: https://arxiv.org/pdf/2606.27326
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Modern generative world models render increasingly realistic action-controllable
  futures, yet t...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: huggingface-daily
depth: abstract
---

### 摘要

Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. We hypothesize that hallucination concentrates in low-coverage regions of the state-action space, where lightweight data-centric signals can both detect it and guide mitigation. To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. We identify three distinct hallucination modes: perceptual, action-marginalized, and scene-diverging -- each anchored to a different stage of the pipeline, and develop three signals that accurately predict where the model will fail. To close coverage gaps at training time, we develop a coverage-aware sampling technique; to close them online, our hallucination predictors serve as curiosity rewards for targeted data collection, yielding a data-efficient finetuning recipe that adapts the pretrained world model to entirely unseen environments with as few as 50 real environment trajectories. Overall, our findings reveal that hallucination in world models is inherently a data coverage issue, and that the same signals used to detect it can also be used for mitigation. An interactive web version of our paper is available at https://www.nicklashansen.com/mmbench2

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

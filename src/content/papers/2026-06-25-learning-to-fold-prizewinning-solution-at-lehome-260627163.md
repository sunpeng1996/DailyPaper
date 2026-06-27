---
title: 'Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place
  online, 2nd offline)'
title_zh: 'Learning to Fold: prizewinning solution at LeHome'
authors:
- Ilia Larchenko
arxiv_id: '2606.27163'
url: https://arxiv.org/abs/2606.27163
pdf_url: https://arxiv.org/pdf/2606.27163
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition
  on bimanual garme...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection. The work mostly recombines existing RL ideas with engineering and optimization contributions that can be used together as one recipe or individually: AWR + RECAP combined for flow-matching VLA; an asynchronous distributed training / rollout pipeline through HuggingFace Hub; inference-time hyperparameters optimization via Thompson sampling; a sim-to-real recipe with camera-alignment tooling, heavy augmentation and DAgger-like HIL data collection.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

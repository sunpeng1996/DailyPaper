---
title: 'E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation'
title_zh: 'E-TTS: A New Embodied Test-Time Scaling Framework'
authors:
- Wen Ye
- Peiyan Li
- Tingyu Yuan
- Yuan Xu
- Xiangnan Wu
- Chaoyang Zhao
- Jing Liu
- Nianfeng Liu
- Yan Huang
- Liang Wang
arxiv_id: '2606.27268'
url: https://arxiv.org/abs/2606.27268
pdf_url: https://arxiv.org/pdf/2606.27268
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Recently, a few works have made early attempts to study test-time scaling
  for embodied tasks. H...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Recently, a few works have made early attempts to study test-time scaling for embodied tasks. However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. To address these challenges, we introduce E-TTS, a modular and plug-and-play Embodied Test-Time Scaling framework that unifies reasoning and action scaling for robotic manipulation via history-aware iterative refinement with vision-language verifiers. To support joint reasoning-action scaling, E-TTS performs reasoning-action joint sampling and scoring in a pairwise manner. To better utilize historical information, E-TTS uses a history buffer to store historical context, which is then used by reasoning and action verifiers to evaluate the sampled candidates. Unlike conventional open-loop TTS methods, E-TTS introduces feedback generation into the sampling process to form a closed-loop iterative refinement mechanism, enhancing both inference efficiency and environmental adaptability. Each component functions as an independent and composable module, allowing flexible and adaptive configuration depending on task requirements. To evaluate the advantages of our framework, we conduct experiments across 4 different benchmarks, 6 environments, 3 embodiments, and 4 base vision-language-action models. The experimental results demonstrate that, without requiring additional expert data collection or retraining, E-TTS consistently improves performance, achieving up to a 33.14% increase in simulation and 26.62% in real-world scenarios.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

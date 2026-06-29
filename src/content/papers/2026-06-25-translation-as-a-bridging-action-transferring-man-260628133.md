---
title: 'Translation as a Bridging Action: Transferring Manipulation Skills from Humans
  to Robots'
title_zh: 'Translation as a Bridging Action: Transferring Man'
authors:
- Sijin Chen
- Kaixuan Jiang
- Haixin Shi
- Yanhui Wang
- Weiheng Zhong
- Haosheng Li
- Bo Jiang
- Yuxiao Liu
- Xihui Liu
arxiv_id: '2606.28133'
url: https://arxiv.org/abs/2606.28133
pdf_url: https://arxiv.org/pdf/2606.28133
published: '2026-06-25'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We study whether we can learn novel manipulation skills from human actions
  to a bi-manual robot...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

We study whether we can learn novel manipulation skills from human actions to a bi-manual robot with parallel grippers. Human action data is cheap, abundant, and diverse, making it one of the most promising resources for scaling up robot learning. Yet transferring skills from humans to robots remains hard: most prior work treats humans as just another bi-manual 6DoF embodiment, where hand-pose estimates are noisy and the contact patterns of human fingers differ fundamentally from those of a parallel gripper. We argue that learning rotation-inclusive action signals from human data is therefore sub-optimal, and instead propose a bridging action representation: the relative wrist translation within the initial head-camera frame, an action space shared by humans and robots. To handle the potential absence of certain action components in different embodiments, we build a $π_0$-like vision-language-action model with interleaved action tokens and attention masking. On a suite of novel bi-manual manipulation tasks, our bridging action transfers human manipulation knowledge to robots far more effectively than noisy 6DoF human actions and scales with the amount of human data.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

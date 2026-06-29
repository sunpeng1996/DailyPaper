---
title: 'SimFoundry: Modular and Automated Scene Generation for Policy Learning and
  Evaluation'
title_zh: 'SimFoundry: Modular and Automated Scene Generation'
authors:
- Nadun Ranawaka
- Josiah Wong
- Wei-Lin Pai
- Wei-Teng Chu
- Tianyuan Dai
- Masoud Moghani
- Hang Yin
- Yunfan Jiang
- Wesley Durbano
- Brandon Huynh
arxiv_id: '2606.28276'
url: https://arxiv.org/abs/2606.28276
pdf_url: https://arxiv.org/pdf/2606.28276
published: '2026-06-25'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Training and evaluating robot policies in the real world is costly and
  difficult to scale. We i...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Training and evaluating robot policies in the real world is costly and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction from a video. SimFoundry generates sim-ready digital twins and supports object, scene, and task editing, enabling the automated generation of diverse digital cousins: affordance-preserving variations of reconstructed real-world scenes. Policies trained on SimFoundry data transfer zero-shot to challenging real tasks involving multi-step manipulation, articulated object interaction, and bimanual interaction, and its digital cousins (variations of the original scene, objects, and tasks) facilitate generalization to new real-world conditions. Across 7 manipulation tasks and 5 policy architectures, SimFoundry simulation evaluations strongly predict real-world performance, with mean Pearson correlation 0.911 and mean maximum ranking violation 0.018. When evaluating sim-trained policies zero-shot in the real world, policies trained with object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively. Additional details at https://research.nvidia.com/labs/gear/simfoundry/ .

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'TuneJury: An Open Metric for Improving Music Generation Preference Alignment'
title_zh: 'TuneJury: An Open Metric for Improving Music Gener'
authors:
- Yonghyun Kim
- Junwon Lee
- Haiwen Xia
- Yinghao Ma
- Junghyun Koo
- Koichi Saito
- Yuki Mitsufuji
- Chris Donahue
arxiv_id: '2606.17006'
url: https://arxiv.org/abs/2606.17006
pdf_url: https://arxiv.org/pdf/2606.17006
published: '2026-06-15'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: We introduce TuneJury, an open, instance-level pairwise reward model for
  text-to-music that pre...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 摘要

We introduce TuneJury, an open, instance-level pairwise reward model for text-to-music that predicts a music preference score from a text prompt and an audio clip. The released checkpoint is trained on publicly available human-preference labels covering arena-style (A vs. B) votes, metric-alignment preference pairs, crowdsourced pairwise comparisons, and expert aesthetic ratings. The predicted score margin between two clips is well calibrated on our held-out test split, supporting data filtering via a simple score threshold. TuneJury generalizes to both held-out test pairs and out-of-distribution benchmarks, remaining competitive with prior baselines on the latter. For generators released after training, we introduce anchor calibration, a post-hoc, per-system Bradley-Terry calibration that recovers agreement at substantially better data efficiency than from-scratch retraining. The same frozen reward drives consistent reward-axis gains across three downstream applications: inference-time best-of-N selection, DITTO-style latent optimization, and expert-iteration post-training. TuneJury is available at https://github.com/yonghyunk1m/TuneJury.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

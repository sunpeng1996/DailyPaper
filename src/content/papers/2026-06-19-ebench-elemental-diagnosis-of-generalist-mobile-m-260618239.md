---
title: 'EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies'
title_zh: 'EBench: Elemental Diagnosis of Generalist Mobile M'
authors:
- Ning Gao
- Jinliang Zheng
- Xing Gao
- Haoxiang Ma
- Hanqing Wang
- Yukai Wang
- Jiantong Chen
- Zanxin Chen
- Shujie Zhang
- Mingda Jia
arxiv_id: '2606.18239'
url: https://arxiv.org/abs/2606.18239
pdf_url: https://arxiv.org/pdf/2606.18239
published: '2026-06-19'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: We present EBench, a simulation benchmark that diagnoses generalist mobile
  manipulation policie...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

We present EBench, a simulation benchmark that diagnoses generalist mobile manipulation policies beyond a single success-rate scalar. EBench comprises 26 diverse and challenging manipulation tasks annotated along 5 capability dimensions and 4 generalization dimensions. We evaluate state-of-the-art generalist manipulation models including π_0, π_{0.5}, XVLA, and InternVLA-A1, and reveal that models with near success rates exhibit strikingly different capability profiles: π_{0.5} achieves the highest test success rate and the best train--test retention, whereas InternVLA-A1 dominates mobile manipulation but collapses on dexterous tasks, and XVLA exhibits strengths on a disjoint set of atomic skills compared to other policies. Beyond capability profiling, EBench analyzes the generalization ability from 4 representative perspectives, identifying the impact of different distribution shift factors. The results reveal strengths and weaknesses of models behind an overall score. We hope this benchmark offers a broad set of diagnostic signals to guide iteration on generalist manipulation models.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

---
title: Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability
title_zh: Mechanism-Driven Monitors for Preemptive Detection
authors:
- Ruixuan Huang
- Yipei Wang
- Wenyi Fang
- Hantao Huang
- Yifan Huang
- Ansheng You
- Zhenxing Zhang
- Shuai Wang
- Fan Wu
- Yang Zheng
arxiv_id: '2606.28116'
url: https://arxiv.org/abs/2606.28116
pdf_url: https://arxiv.org/pdf/2606.28116
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Frontier large language model training consumes massive accelerator fleets
  and long wall-clock...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. We study mechanism-driven detection of training instability by deriving internal monitors from the functional role of each critical module and from the earliest computational sites where failures are expected to produce measurable signatures. For low-precision flash attention, we monitor the spectral entropy of a QK bilinear decomposition, whose first-order term becomes abnormal before the loss fully collapses. For MoE routers, we derive indicators from their role in expert selection. Our fault-injection experiments on low-precision attention, large learning-rate, and combined faults show that these signals provide distinct signatures for different failures, triggering thousands of steps before loss divergence.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

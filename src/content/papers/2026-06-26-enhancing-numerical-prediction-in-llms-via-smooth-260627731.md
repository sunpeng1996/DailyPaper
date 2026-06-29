---
title: Enhancing Numerical Prediction in LLMs via Smooth MMD Alignment
title_zh: Enhancing Numerical Prediction in LLMs via Smooth
authors:
- Zhuo Zuo
- Li Yue
- Wenhao Zheng
- Chenpeng Wang
- Xianggen Liu
arxiv_id: '2606.27731'
url: https://arxiv.org/abs/2606.27731
pdf_url: https://arxiv.org/pdf/2606.27731
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Despite their strong general capabilities, large language models (LLMs)
  often remain unreliable...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Despite their strong general capabilities, large language models (LLMs) often remain unreliable when outputs must be numerically precise. A key reason is the training objective: standard cross-entropy treats numeric tokens as unstructured categories and ignores the metric structure of their values. We address this mismatch with Smooth Maximum Mean Discrepancy (SMMD), which builds on the classic MMD by incorporating value-distance kernels over numeric tokens and graph-based smoothness. With this kernel defined over a numeric sub-vocabulary, SMMD aligns the predicted numeric distribution to the target via kernel matching and smooths the prediction-target residual over the induced kernel graph to encourage local consistency. We evaluate SMMD on four numeric-target tasks: mathematical reasoning, arithmetic calculation, clock-time recognition, and chart question answering, across multiple open-weight LLM and VLM backbones. SMMD consistently improves accuracy over both cross-entropy and recent numeric-target losses; analyses show complementary effects between MMD and smoothness and underscore the importance of distance-based kernel design. Code is available at https://github.com/Zuozhuo/smmd-loss.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

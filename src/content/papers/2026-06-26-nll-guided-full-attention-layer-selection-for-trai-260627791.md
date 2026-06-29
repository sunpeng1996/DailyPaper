---
title: NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window
  Adaptation
title_zh: NLL-Guided Full-Attention Layer Selection for Trai
authors:
- Qiong Tang
- Xiangkun Hu
- Xiangyang Liu
- Yiran Chen
- Yunfan Shao
arxiv_id: '2606.27791'
url: https://arxiv.org/abs/2606.27791
pdf_url: https://arxiv.org/pdf/2606.27791
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Hybrid attention models that mix full and sliding-window attention across
  layers offer a promis...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Hybrid attention models that mix full and sliding-window attention across layers offer a promising approach to efficient long-context inference, but the critical question of \emph{which layers} should retain full attention remains unsolved. Existing methods use either fixed periodic patterns or attention-based heuristics that may not capture what matters for downstream accuracy. We propose NLL-guided layer selection, a training-free method that directly measures each layer's importance by computing the negative log-likelihood degradation on answer tokens when that layer uses sliding-window instead of full attention. On LongMemEval with Qwen3-4B, our method achieves 64.6\% accuracy using only 1/4 full-attention layers, matching the 1/2-FA periodic baseline (65.0\%) while halving the computational budget. NLL-guided selection outperforms the SWAA-reported periodic 1/4-FA baseline by 10.4 percentage points and a matched LightTransfer-style baseline by 26.4 percentage points. De-confounding analysis shows the signal is consistent with long-range attention needs rather than generic layer sensitivity. The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

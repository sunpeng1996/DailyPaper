---
title: Intuition-Guided Latent Reasoning for LLM-Based Recommendation
title_zh: Intuition-Guided Latent Reasoning for LLM-Based Re
authors:
- Chang Liu
- Yimeng Bai
- Xiaoyan Zhao
- Yang Zhang
- Qifan Wang
- Fuli Feng
- Wenge Rong
arxiv_id: '2606.27684'
url: https://arxiv.org/abs/2606.27684
pdf_url: https://arxiv.org/pdf/2606.27684
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Large Language Models (LLMs) have demonstrated impressive reasoning capabilities
  in complex pro...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Large Language Models (LLMs) have demonstrated impressive reasoning capabilities in complex problem-solving tasks, motivating their use for preference reasoning in recommender systems. Latent reasoning, which operates in continuous hidden spaces rather than discrete tokens, has recently emerged as a promising paradigm for LLM-based recommendation. However, existing methods often start from unconstrained reasoning points, where hidden representations are misaligned with target item embeddings, leading to suboptimal reasoning trajectories. Inspired by cognitive neuroscience, which suggests that human multi-step reasoning is guided by intuition as a latent prior, we propose \emph{IntuRec}, a two-stage framework that anchors latent reasoning with \emph{recommendation intuition}. In the extraction stage, the LLM-based recommender generates a top-$K$ candidate set based on users' histories as the source of intuition. In the injection stage, the candidate set is transformed into a preference-aligned intuition embedding using self- and cross-attention mechanisms, which initializes the reasoning start point and guides subsequent latent reasoning. By providing a semantically grounded starting point, IntuRec efficiently explores the preference space along more accurate reasoning trajectories. Extensive experiments on multiple real-world datasets demonstrate that IntuRec consistently outperforms state-of-the-art baselines. We release our code at https://github.com/Ten-Mao/IntuRec.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

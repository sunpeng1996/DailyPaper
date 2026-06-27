---
title: Stabilizing black-box algorithms through task-oriented randomization
title_zh: Stabilizing black-box algorithms through task-orie
authors:
- Yali Wang
- Zhaojun Wang
arxiv_id: '2606.25269'
url: https://arxiv.org/abs/2606.25269
pdf_url: https://arxiv.org/pdf/2606.25269
published: '2026-06-24'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: As black-box models become foundational to modern research, ensuring their
  stability is paramou...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-stat.ML
depth: abstract
---

### 摘要

As black-box models become foundational to modern research, ensuring their stability is paramount for the realization of trustworthy artificial intelligence. The inherent diversity of inputs - ranging from structured Gaussian distributions to complex data with unknown structures - poses a significant challenge: how to stabilize black-box outputs while effectively leveraging available prior information. This paper introduces a task-oriented randomization methodology that adaptively tailors its strategy to the underlying generative mechanisms of the input data, specifically addressing unstructured complexities. A comprehensive suite of stability guarantees is proposed. Beyond establishing rigorous theoretical foundations for stability, the research provides a detailed analysis of the intrinsic trade-off between stability and exploration. Motivated by the architecture of Large Language Models, the framework is further extended to top-k ranking problems. The validity and effectiveness of the proposal are demonstrated through extensive numerical simulations and applications to the real-world dataset.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

---
title: 'Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation
  via Self-Consistency Rewards'
title_zh: 'Ask, Solve, Generate: Self-Evolving Unified Multim'
authors:
- Ritesh Thawkar
- Shravan Venkatraman
- Omkar Thawakar
- Abdelrahman Shaker
- Fahad Khan
- Hisham Cholakkal
- Salman Khan
- Rao Muhammad Anwer
arxiv_id: '2606.27376'
url: https://arxiv.org/abs/2606.27376
pdf_url: https://arxiv.org/pdf/2606.27376
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Most unified large multimodal models (LMMs) that support both visual understanding
  and image ge...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Most unified large multimodal models (LMMs) that support both visual understanding and image generation still rely on curated post-training supervision, such as human annotations, preference labels, or external reward models. We ask whether a unified LMM can improve both abilities autonomously using only unlabeled images. We propose a self-evolving training framework with three internal roles: a Proposer that generates visual questions, a Solver that answers and evaluates them, and a Generator that synthesizes images. Training uses only self-derived consistency signals, without human annotations, preference labels, or task-trained external reward/judge models. To stabilize learning, we introduce Solver Token Entropy (STE), a continuous difficulty signal based on token-level prediction uncertainty that remains useful even when sample-level consistency becomes unreliable. For image generation, we design a multi-scale internal evaluation scheme that combines question-answer fidelity scoring with cycle-consistent captioning. This creates a solver-mediated coupling, where better visual understanding enables more reliable generation assessment and stronger internal training signals. The framework preserves the same role decomposition, reward logic, and training schedule across diffusion-based BLIP3o, rectified-flow BAGEL, and autoregressive VARGPT-v1.1 architectures, requiring only each backbone's native prompting and generation interface. Across eight understanding metrics, our method consistently improves over the corresponding base models. On BAGEL, it achieves a $+3.5\%$ absolute gain on MMMU and improves GenEval image generation performance from $82\%$ to $85\%$. Code and models are publicly released.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

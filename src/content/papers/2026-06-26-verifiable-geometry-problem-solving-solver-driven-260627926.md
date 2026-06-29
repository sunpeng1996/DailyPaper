---
title: 'Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem
  Proposing'
title_zh: 'Verifiable Geometry Problem Solving: Solver-Driven'
authors:
- Can Li
- Ting Zhang
- Junbo Zhao
- Hua Huang
arxiv_id: '2606.27926'
url: https://arxiv.org/abs/2606.27926
pdf_url: https://arxiv.org/pdf/2606.27926
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Geometry Problem Solving have increasingly adopt the neuro-symbolic paradigm,
  combining neural...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Geometry Problem Solving have increasingly adopt the neuro-symbolic paradigm, combining neural intuition with symbolic rigor. However, current frameworks suffer from severe bottlenecks in two core stages: autoformalization, which treats multimodal translation as a static task decoupled from downstream solver compatibility, and theorem prediction, where solvers frequently hit a deductive impasse due to fixed rule libraries. To address these, we propose SD-GPS, a solver-driven framework that treats the symbolic solver as an execution oracle throughout both formalization and deduction. First, Solver-Driven Autoformalization unifies supervised formal-language adaptation and solvability-guided reinforcement learning into a single module built on QwenVL3-2B, making executability the central training signal. Second, Verified Theorem Proposing introduces an impasse-aware agent that proposes local auxiliary lemmas from current proof states, ensuring soundness by filtering all proposals through symbolic verification. Empirical evaluations on Geometry3K and PGPS9K demonstrate that SD-GPS consistently outperforms existing MLLM, neural, and neuro-symbolic methods across standard completion, multiple-choice, and cross-modal reference regimes, proving that closing the loop between multimodal perception and symbolic execution significantly improves geometric reasoning, offering profound insights into how neural agents can be grounded by formal systems to achieve verifiable problem-solving capabilities.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference
title_zh: End-to-End Dynamic Sparsity for Resource-Adaptive
authors:
- Yuhang Chen
- Jinhao Duan
- Ruichen Zhang
- Mingfu Liang
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Parish Aggarwal
- Frank Shyu
arxiv_id: '2606.27743'
url: https://arxiv.org/abs/2606.27743
pdf_url: https://arxiv.org/pdf/2606.27743
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Large Language Models (LLMs) inference is typically deployed under a static
  resource assumption...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Large Language Models (LLMs) inference is typically deployed under a static resource assumption, where models execute a fixed computational graph regardless of the runtime environment. However, real-world cloud infrastructure is inherently dynamic, characterized by fluctuating availability (e.g., spot instance preemption) and tiered Quality-of-Service requirements. In such volatile settings, static models are inflexible: they either crash under resource constraints or waste compute on redundant operations. To bridge this gap, we propose Learning to Allocate (L2A), an end-to-end framework for resource-adaptive inference. Unlike prior methods that condition only on input difficulty, we formulate inference as a constrained allocation problem conditioned on both the input and the runtime resource budget itself. We introduce lightweight, budget-conditioned and input-aware gating networks integrated into the LLM. These gates are trained via a unified objective that jointly optimizes task performance, logical consistency, and resource costs along three axes matching how real-world dynamics manifest: layer skipping for memory and depth pressure, head pruning for throughput contention, and reasoning-token reduction for latency tightening. This lets the model learn a budget-aware policy beyond input difficulty alone: it adaptively configures its computational footprint with respect to real-time resource dynamics, maximizing reasoning depth when resources permit while enforcing strict frugality when budgets tighten. A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence
  Gating for Fine-Grained Visual Reasoning'
title_zh: 'V-Zero: Answer-Label-Free On-Policy Distillation w'
authors:
- Haoxiang Sun
- Zhihang Yi
- Langxuan Deng
- Yuhao Zhou
- Peiqi Jia
- Jian Zhao
- Li Yuan
- Jiancheng Lv
- Tao Wang
arxiv_id: '2606.25319'
url: https://arxiv.org/abs/2606.25319
pdf_url: https://arxiv.org/pdf/2606.25319
published: '2026-06-23'
collected: '2026-06-26'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Fine-grained visual reasoning requires multimodal large language models
  (MLLMs) to identify tas...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Fine-grained visual reasoning requires multimodal large language models (MLLMs) to identify task-relevant visual evidence and ground their reasoning in local image regions. Existing agentic methods typically rely on reinforcement learning with verifiable rewards or supervised fine-tuning on large-scale annotated reasoning traces, leading to costly exploration, hand-designed verification rules, or heavy dependence on textual supervision. A natural way to avoid such external answer labels is to learn from trajectories sampled by the student itself, which points to On-Policy Distillation (OPD). To understand what OPD can and cannot provide for visual reasoning, we revisit it as negative-free stop-gradient alignment. This perspective shows that, although OPD provides effective token-level correction, its ceiling is constrained by the absence of trajectory-level discrimination. Motivated by these observations, we propose V-Zero, an answer-label-free framework for visual reasoning with contrastive evidence gating. V-Zero uses no annotated textual answer labels; instead, during training it pairs a question-relevant regional crop with a negative visual view to evaluate student-sampled trajectories and gate dense token-level distillation. Experiments on multiple visual reasoning benchmarks show that V-Zero consistently improves fine-grained visual reasoning while preserving strong generalization. Notably, V-Zero is more than 5times faster than previous supervised fine-tuning methods and more than 10times faster than reinforcement learning baselines. Code and dataset will be released at https://github.com/eVI-group-SCU/V-Zero

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

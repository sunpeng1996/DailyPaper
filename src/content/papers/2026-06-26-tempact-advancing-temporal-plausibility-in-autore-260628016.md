---
title: 'TempAct: Advancing Temporal Plausibility in Autoregressive Video Generation
  via Planner-Executor RL'
title_zh: 'TempAct: Advancing Temporal Plausibility in Autore'
authors:
- Jing Wang
- Xiangxin Zhou
- Jiajun Liang
- Kaiqi Liu
- Wanyun Pang
- Zhenyu Xie
- Tianyu Pang
- Xiaodan Liang
arxiv_id: '2606.28016'
url: https://arxiv.org/abs/2606.28016
pdf_url: https://arxiv.org/pdf/2606.28016
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Autoregressive (AR) video diffusion models enable low-latency streaming
  generation by synthesiz...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Autoregressive (AR) video diffusion models enable low-latency streaming generation by synthesizing videos chunk by chunk with cached visual context, but this chunk-wise formulation makes temporal instruction following ambiguous. A single global prompt does not specify which sub-event should be realized in each chunk, while naively switching to step-wise prompts often leads to delayed reactions, blended step semantics, and error propagation across prompt transitions. These failures are difficult to address with supervised fine-tuning or distillation alone: SFT suffers from exposure bias, while rollout-based distillation still optimizes low-level denoising or teacher-distribution matching rather than directly enforcing action ordering and prompt-transition correctness. We address these challenges with TempAct, a planner--executor reinforcement learning framework that jointly optimizes temporal decomposition and step-conditioned execution for temporally plausible AR video generation. TempAct uses an LLM planner to explore span-aware step prompts that are executable by the video model, and trains an AR diffusion executor to follow these prompts under its own generated histories. Its key mechanism is hierarchical group exploration: candidate plans form planning groups, and each plan induces an execution group of multiple continuations from a shared visual context, enabling plan-level credit assignment for long-horizon temporal outcomes and executor-level credit assignment for prompt-switch behavior. We further design hierarchical rewards that combine plan-quality and full-video temporal feedback for the planner with local transition-level step-following rewards, aesthetic regularization, and KL constraints for the executor. Experiments on Self-Forcing and LongLive show that TempAct improves temporal consistency while preserving overall visual quality.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

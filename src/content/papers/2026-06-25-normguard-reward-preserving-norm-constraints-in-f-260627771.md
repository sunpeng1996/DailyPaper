---
title: 'NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement
  Learning'
title_zh: 'NormGuard: Reward-Preserving Norm Constraints in F'
authors:
- Tianlin Pan
- Lianyu Pang
- Cheng Da
- Huan Yang
- Changqian Yu
- Kun Gai
- Wenhan Luo
arxiv_id: '2606.27771'
url: https://arxiv.org/abs/2606.27771
pdf_url: https://arxiv.org/pdf/2606.27771
published: '2026-06-25'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Reinforcement learning (RL) post-training improves the reward alignment
  of flow-based generator...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: huggingface-daily
depth: abstract
---

### 摘要

Reinforcement learning (RL) post-training improves the reward alignment of flow-based generators, but often degrades perceptual quality in ways that are not captured by the reward proxy. We identify a simple structural signature of this drift: across three post-training methods (NFT, AWM, DPO), RL fine-tuning inflates the per-step velocity norm |v_θ| by 5% to 15% relative to the reference. A form of norm inflation has been studied in classifier-free guidance (CFG), where rescaling the velocity back to a reference norm at inference time can mitigate the resulting artifacts. However, this inference-time correction does not transfer cleanly to RL: rescaling v_θ to match |v_{ref}| at inference time neither improves reward nor fixes the quality degradation, because the inflation is co-adapted into the model weights. Furthermore, an adjoint sensitivity analysis shows that velocity magnitude rescaling carries no coherent first-order reward signal at the batch level, indicating that suppressing norm inflation is unlikely to remove a consistently reward-carrying component. Since inference-time renormalization fails while norm suppression carries no reward cost, training-time intervention is the appropriate strategy. Together, these findings motivate \methodname, a hinge penalty that activates only when |v_θ| exceeds |v_{ref}| and composes additively with any velocity-local base loss. Across two base models, three post-training methods, and two reward proxies, \methodname consistently improves MLLM-judged image quality and forensic realism while preserving reward, with gains that amplify under few-step inference and are not explained by early stopping.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

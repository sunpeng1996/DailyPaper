---
title: Qwen-Image-2.0-RL Technical Report
title_zh: Qwen-Image-2.0-RL Technical Report
authors:
- Yixian Xu
- Kaiyuan Gao
- Yuxiang Chen
- Yilei Chen
- Zecheng Tang
- Zihao Liu
- Zikai Zhou
- Deqing Li
- Hao Meng
- Kuan Cao
arxiv_id: '2606.27608'
url: https://arxiv.org/abs/2606.27608
pdf_url: https://arxiv.org/pdf/2606.27608
published: '2026-06-24'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement
  learning from...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: huggingface-daily
depth: abstract
---

### 摘要

We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. To provide reliable reward signals, we construct task-specific composite reward models by fine-tuning vision-language models with a pointwise scoring paradigm and chain-of-thought reasoning. For text-to-image generation, the reward models cover alignment, aesthetics, and portrait fidelity dimensions. For image editing tasks, the reward system addresses instruction-following accuracy and face identity preservation. Building on this reward system, we develop a scalable GRPO-based RL training framework, incorporating a hybrid classifier-free guidance (CFG) strategy to preserve pre-trained knowledge, prompt curation via intra-group reward range filtering, and per-category reward weight calibration. To merge the task-specialized RL policies for T2I and editing, we propose on-policy distillation as the final training stage, which consolidates multiple teachers into a single student model through trajectory-level velocity matching. Extensive evaluation shows that Qwen-Image-2.0-RL achieves 57.84 overall score on Qwen-Image-Bench (+2.61 over the base model), Elo ratings of 1193 in text-to-image arena (+78) and 1349 in image edit arena (+93), demonstrating consistent gains in aesthetic quality, prompt adherence, and editing accuracy.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

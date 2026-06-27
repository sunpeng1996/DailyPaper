---
title: In-Context World Modeling for Robotic Control
title_zh: In-Context World Modeling for Robotic Control
authors:
- Siyin Wang
- Junhao Shi
- Senyu Fei
- Zhaoyang Fu
- Li Ji
- Jingjing Gong
- Xipeng Qiu
arxiv_id: '2606.26025'
url: https://arxiv.org/abs/2606.26025
pdf_url: https://arxiv.org/pdf/2606.26025
published: '2026-06-24'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Modern Vision-Language-Action (VLA) models often fail to generalize to
  novel setups, such as al...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: huggingface-daily
depth: abstract
---

### 摘要

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

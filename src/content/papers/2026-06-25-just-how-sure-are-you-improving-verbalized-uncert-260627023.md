---
title: Just how sure are you? Improving Verbalized Uncertainty Calibration in Medical
  VQA
title_zh: Just how sure are you? Improving Verbalized Uncert
authors:
- Eren Senoglu
- Federico Toschi
- Nicolo Brunello
- Andrea Sassella
- Mark James Carman
arxiv_id: '2606.27023'
url: https://arxiv.org/abs/2606.27023
pdf_url: https://arxiv.org/pdf/2606.27023
published: '2026-06-25'
collected: '2026-06-27'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Multimodal large language models (MLLMs) applied to Medical Visual Question
  Answering (VQA) ten...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Multimodal large language models (MLLMs) applied to Medical Visual Question Answering (VQA) tend to produce overconfident outputs regardless of actual correctness, and existing verbalized confidence calibration methods, developed primarily for text only LLMs, do not account for the multimodal nature of medical image understanding. This work proposes a training based framework that finetunes MLLMs to improve their calibration using a composite loss function combining a Brier style calibration term, an anchor regularizer that prevents confidence collapse toward extreme values, a contrastive image text alignment term, and a KL based model stabilization term. The alignment signal is derived from a $2 \times 2$ factorial perturbation design that crosses image presence with text integrity, probing the reliance of the model on visual modality input versus language priors. Finally, a top K KL divergence regularizer is used to protect the answering ability of the model during finetuning. Across three Medical VQA benchmarks and two architectures (MedGemma 4B IT and Qwen2 VL 7B Instruct), our method reduces calibration error by 60% or more, and improves discrimination by 26% or more, while preserving predictive accuracy. On average across benchmarks, the technique outperforms prompting based, sampling based, and training based approaches, and ablation experiments confirm that each component of the loss function is indeed necessary for improving the calibration. All code for the experiments is publicly available.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

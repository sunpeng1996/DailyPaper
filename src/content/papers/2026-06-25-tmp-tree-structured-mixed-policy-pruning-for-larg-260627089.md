---
title: 'TMP: Tree-structured Mixed-policy Pruning for Large-scale Image Generation
  and Editing'
title_zh: 'TMP: Tree-structured Mixed-policy Pruning for Larg'
authors:
- Peizhen Zhang
- Yang Li
- Xunsong Li
- Songtao Liu
- Zewen Liu
- Qiangqiang Hu
- Guotong Guo
- Jupeng Ding
- Yifu Sun
- coopersli
arxiv_id: '2606.27089'
url: https://arxiv.org/abs/2606.27089
pdf_url: https://arxiv.org/pdf/2606.27089
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Modern image generation model rapidly grows their sizes to meet high-fidelity
  image synthesis....
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Modern image generation model rapidly grows their sizes to meet high-fidelity image synthesis. However, they gradually become unaffordable for their enormous parameter consumption and computation budget that lead to massive resources requirement and gpu memory footprint. In this paper, we propose TMP, the first Tree-structured Mixed-policy Pruning framework that generalizes prevalent image tasks (T2I and TI2I) and architectures (Mixture-of-Experts (MoE) and Diffusion transformer (DiT)). It could be applied to the step-distilled models and contribute as the last stage. We perform experiments upon current open-sourced SOTA HunyuanImage-3.0 instruct and a popular efficient model Z-Image turbo. The proposed pruning framework manages to compress HunyuanImage 3.0 from 80B to 20B parameters at 75% reduction ratio, sacrificing limited generation quality. We also optimize to enable the inference of the pruned 20B version of HunyuanImage 3.0 on a single 24GB 4090 GPU by engineering skills. The inference script and model weight have been integrated into the existing HunyuanImage3.0 open-source github and huggingface repository. Besides, we prove the efficacy of TMP by compressing Z-Image turbo from 6B to 4B (33% reduction) with negligible degradation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

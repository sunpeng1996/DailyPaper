---
title: 'SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation
  in Retrieval-Augmented Generation'
title_zh: 'SHIFT: Gate-Modulated Activation Steering for Know'
authors:
- Ruochang Li
- Pengcheng Huang
- Zhenghao Liu
- Yukun Yan
- Huiyuan Xie
- Yu Gu
- Ge Yu
- Maosong Sun
arxiv_id: '2606.27786'
url: https://arxiv.org/abs/2606.27786
pdf_url: https://arxiv.org/pdf/2606.27786
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Retrieval-augmented generation (RAG) enhances LLMs by incorporating external
  knowledge to suppo...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Retrieval-augmented generation (RAG) enhances LLMs by incorporating external knowledge to support response generation. However, conflicts between retrieved context and parametric knowledge have emerged as a critical challenge in RAG systems. To mitigate such conflicts, numerous studies have attempted to identify and edit knowledge-related internal neurons, aiming to improve the ability of LLMs to rely on contextual evidence during generation. However, these neuron-level approaches may introduce unintended cascading effects that compromise the general capabilities of LLMs, as the modified neurons are often entangled with broader model behaviors and functionalities. In this paper, we introduce SHIFT, a novel framework that reformulates neuron-level modification as learnable gate modulation, allowing LLMs to adaptively regulate internal activations for knowledge conflict resolution. Technically, our SHIFT equips LLMs with a lightweight gate module and optimizes fewer than 0.01% trainable parameters while keeping the backbone model frozen. During generation, the gate module adjusts the model's internal representations to adaptively leverage contextual and parametric knowledge. Extensive experiments on six datasets validate the effectiveness of our SHIFT in comparison with various competing baselines. All datasets and code are available at https://github.com/OpenBMB/SHIFT.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

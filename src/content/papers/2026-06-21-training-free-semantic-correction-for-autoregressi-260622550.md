---
title: Training-Free Semantic Correction for Autoregressive Visual Models
title_zh: Training-Free Semantic Correction for Autoregressi
authors:
- Junhao Chen
- Chanyu Zhu
- Zheqi Lv
- Keting Yin
- Shengyu Zhang
arxiv_id: '2606.22550'
url: https://arxiv.org/abs/2606.22550
pdf_url: https://arxiv.org/pdf/2606.22550
published: '2026-06-21'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Autoregressive visual models (AVMs) based on next-scale prediction have
  emerged as a prominent...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Autoregressive visual models (AVMs) based on next-scale prediction have emerged as a prominent paradigm for image and video synthesis. However, decomposing the generation process into discrete scales with varying granularities in AVM makes semantic errors difficult to identify and correct, thereby undermining the quality of the final output. Prior efforts to enhance AVM can be categorized into training-based and training-free approaches. Although training-based efforts to enhance AVM generation quality come at substantial computational cost, existing training-free methods neglect intermediate generation states, leaving semantic errors undiagnosed and allowing them to accumulate into the final output. In this paper, we focus on training-free paradigms and propose Gazer, a framework that integrates multimodal large language model feedback into the AVM sampling loop for in-generation semantic correction. Concretely, Gazer operates via two cooperating stages: the Reflective Diagnosis stage diagnoses semantic errors from intermediate states, while the Semantic Correction stage rewinds and rectifies the generation trajectory to realign with the target prompt. Experiments on compositional image and video benchmarks demonstrate that Gazer improves semantic alignment and compositional accuracy across multiple AVMs without additional training.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

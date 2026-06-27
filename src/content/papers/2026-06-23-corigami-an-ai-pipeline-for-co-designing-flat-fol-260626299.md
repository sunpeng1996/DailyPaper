---
title: 'COrigami: An AI Pipeline for Co-Designing Flat-Foldable Visually Recognisable
  Origami'
title_zh: 'COrigami: An AI Pipeline for Co-Designing Flat-Fol'
authors:
- Tom Zahavy
- Shaobo Hou
- Thomas Tumiel
- James Doran
- Francesco Faccio
- Xidong Feng
- Alex Havrilla
- Igor Khytryi
- Chenglei Li
- Lisa Schut
arxiv_id: '2606.26299'
url: https://arxiv.org/abs/2606.26299
pdf_url: https://arxiv.org/pdf/2606.26299
published: '2026-06-23'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: While generative AI has achieved remarkable success in solving problems
  with verifiable solutio...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: huggingface-daily
depth: abstract
---

### 摘要

While generative AI has achieved remarkable success in solving problems with verifiable solutions, generating physical art that satisfies both strict geometric constraints and subjective visual aesthetics remains a challenge. This paper presents an approach to tackle these difficulties in the domain of computational origami, a mathematically rigid environment that grounds artistic design within the equations of flat foldability. We present COrigami, an end-to-end AI-driven pipeline that assists the design cycle by generating crease patterns from natural language. Our pipeline involves generating a semantic stick figure, computing a base packing, solving for a flat-foldable crease pattern, shaping the flat-folded crease pattern, and refining the generated model using reinforcement learning driven by an autonomous aesthetic evaluation loop. Our system acts as a highly effective collaborative assistant, generating structural starting points that human artists can further expand and shape. By integrating algorithmic optimisation with autonomous aesthetic critique, this work demonstrates how AI systems can satisfy multi-objective physical constraints to enable reliable, mathematically grounded co-creativity.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'TextDS: Parameter-Efficient Representation Alignment for Scene Text Detection
  under Distribution Shifts'
title_zh: 'TextDS: Parameter-Efficient Representation Alignme'
authors:
- Boyuan Chen
- Zichen Dang
- Chuang Yang
- Lap-pui Chau
- Yi Wang
arxiv_id: '2606.28077'
url: https://arxiv.org/abs/2606.28077
pdf_url: https://arxiv.org/pdf/2606.28077
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: In real-world deployments, scene text detectors inevitably face distribution
  shifts beyond the...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 摘要

In real-world deployments, scene text detectors inevitably face distribution shifts beyond the training distribution. Prior work often depends on large-scale scene-text pretraining, yet evaluation under cross-domain changes and real-world imaging degradations remains limited. We propose TextDS, an efficient framework for scene text detection under distribution shifts. First, we propose a data-efficient dual-encoder design with visual foundation models, eliminating the reliance on large-scale scene-text pretraining. Second, we introduce Step-wise LoRA adaptation (SWLoRA), which performs progressive low-rank refinement with a dynamic early-exit mechanism for effective feature adaptation. Third, we propose Common Subspace Fusion (CSF) to align and fuse the two branches in a shared subspace while retaining complementary, shift-robust information. Finally, we construct adverse-condition scene text detection datasets to address the gap in evaluating under imaging degradation. Experiments show that TextDS achieves competitive performance in scene text detection, demonstrating robustness across domains and adverse imaging conditions with only 4.9M trainable parameters.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

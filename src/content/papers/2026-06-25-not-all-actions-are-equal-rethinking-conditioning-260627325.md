---
title: 'Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model'
title_zh: 'Not All Actions Are Equal: Rethinking Conditioning'
authors:
- Zizhao Yuan
- Zhengtu Liang
- Taowen Wang
- Qiwei Liang
- Yichi Wang
- Yunheng Wang
- Yuetong Fang
- Lusong Li
- Zecui Zeng
- Renjing Xu
arxiv_id: '2606.27325'
url: https://arxiv.org/abs/2606.27325
pdf_url: https://arxiv.org/pdf/2606.27325
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Recent advances in action-conditioned world models show promising progress
  in modeling complex...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Recent advances in action-conditioned world models show promising progress in modeling complex interactions and forecasting future states under diverse action sequences. While these models are often driven by stronger visual representations and model capacity, action conditioning itself remains underexplored. Most existing approaches compress the entire action sequence into a single representation, which works well for low-DoF control but becomes less reliable in high-DoF scenarios. We observe that high-DoF dexterous actions are inherently heterogeneous, spanning multiple orders of magnitude, where large-scale motions coexist with subtle but important signals. When uniformly aggregated, optimization exhibits an imbalance across action components, which hinders the modeling of fine-grained effects and affects action fidelity. We therefore propose DexAC-WM, which treats action conditioning as a structured process rather than global compression. DexAC preserves dimension-level semantics via action tokenization and aligns action signals with visual dynamics through local refinement and global modulation. To address the limited high-level semantic grounding in existing world models, we further introduce a semantic branch that provides rich object-scene priors, which enables world model to capture dynamic visual details while supporting high-DoF action-conditioned video prediction. Experiments on EgoDex and EgoVerse show that combining the semantic branch with DexAC significantly improves FID, FVD, and PCK, demonstrating gains in visual-temporal realism and action-following consistency. We further verify that DexAC extends to other backbones, showing the scalability of our structured action-conditioning design. These results suggest that scaling world models to high-DoF control requires both structured action modeling and semantic grounding.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'ReScene: Structured Indoor Scene Reconstruction from Multi-View Captures'
title_zh: 'ReScene: Structured Indoor Scene Reconstruction fr'
authors:
- Haoran Xu
- Lechao Zhang
- Daoguo Dong
- Yan Gao
- Xin Tan
arxiv_id: '2606.28060'
url: https://arxiv.org/abs/2606.28060
pdf_url: https://arxiv.org/pdf/2606.28060
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Constructing simulation-ready 3D scenes from multi-view captures is a key
  bottleneck for Embodi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Constructing simulation-ready 3D scenes from multi-view captures is a key bottleneck for Embodied Artificial Intelligence, as downstream tasks require object-level structure, explicit inter-object relations, and physical plausibility. Existing approaches either rely on specialized capture hardware, suffer from single-view bias in object reconstruction, or yield layouts that are geometrically reasonable but physically inconsistent. We identify that the problem is not single-object reconstruction but cross-view relation fusion and physically plausible scene assembly. To address this challenge, we present ReScene, a framework that threads multi-view geometry throughout the pipeline as a unifying prior. Our method consists of two main components: HierView prioritizes reconstruction views based on semantic consistency and 3D coverage completeness, replacing the largest-mask heuristic that conflates image occupancy with object coverage; and Relation-Aware Assembly fuses multi-frame relation predictions from a vision-language model with geometric and room-shell priors into a confidence-weighted scene graph, enabling physically consistent scene assembly. ReScene sets a new state of the art across geometry, rendering, and perceptual quality on a set of ScanNet scenes, achieving a 17% reduction in Chamfer Distance and 26% in LPIPS over the strongest prior baseline, while running up to 10x faster than prior multi-view methods. Based on the reconstructed scenes, we also generate an embodied visual question answering dataset, on which fine-tuned Qwen-VL approaches the performance of strong closed-source models on several spatial reasoning tasks.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

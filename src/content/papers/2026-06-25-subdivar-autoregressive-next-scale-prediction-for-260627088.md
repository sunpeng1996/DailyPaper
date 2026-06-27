---
title: 'SubdivAR: Autoregressive Next-Scale Prediction for Neural Mesh Subdivision'
title_zh: 'SubdivAR: Autoregressive Next-Scale Prediction for'
authors:
- Huipeng Guo
- Zikai Song
- Hang Long
- Jielei Zhang
- Wenbing Li
- Junkai Lin
- Tianhao Zhao
- Jinshen Zhang
- Tianle Guo
- Wei Yang
arxiv_id: '2606.27088'
url: https://arxiv.org/abs/2606.27088
pdf_url: https://arxiv.org/pdf/2606.27088
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Mesh subdivision is a fundamental operation for converting coarse, editable
  meshes into high-re...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Mesh subdivision is a fundamental operation for converting coarse, editable meshes into high-resolution surfaces, with broad applications in digital asset creation. Classical rule-based schemes rely on fixed local refinement rules and often produce over-smoothed surfaces. Recent neural subdivision methods improve detail synthesis, but remain constrained by local modeling and exhibit limited generalizability. We present SubdivAR, a neural mesh subdivision framework based on our proposed Mesh Autoregressive Representation (MAR). MAR arranges meshes at different subdivision levels into an ordered scale sequence, reformulating subdivision as autoregressive next-scale prediction. To support this formulation, we introduce a Hybrid Topology-Aware Transformer that combines global semantic attention with topology-constrained local feature aggregation. SubdivAR adopts a next-scale coordinate prediction paradigm, regressing vertex offsets at each refinement stage to preserve subdivision topology while recovering fine-grained geometric details. To enable reliable learning, we construct FII-40K, a curated dataset of nearly 40,000 high-quality meshes with multi-level subdivision supervision. Experiments show that SubdivAR outperforms state-of-the-art baselines, reducing Hausdorff Distance and Chamfer Distance by 18.8% and 14.2%, respectively, and demonstrates strong robustness on complex open-surface geometries.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

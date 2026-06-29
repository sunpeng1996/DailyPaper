---
title: 'Beyond Sparse Supervision: Diffusion-Guided Learning for Few-Shot Graph Fraud
  Detection'
title_zh: 'Beyond Sparse Supervision: Diffusion-Guided Learni'
authors:
- Liming Liu
- Chao Hu
- Mingfei Lu
- Yiwei Ge
- Xingle Li
- Heyuan Shi
arxiv_id: '2606.28134'
url: https://arxiv.org/abs/2606.28134
pdf_url: https://arxiv.org/pdf/2606.28134
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Graph-based fraud detection is essential for safeguarding large-scale transaction
  systems, wher...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Graph-based fraud detection is essential for safeguarding large-scale transaction systems, where undetected anomalies may lead to substantial financial losses and security risks. Real-world fraud graphs pose two coupled challenges: sparse and imbalanced supervision, where verified fraudulent labels are scarce and heavily skewed toward benign accounts, and representation dilution, where spatial message passing may oversmooth camouflaged anomalies while spectral filters may suppress fraud-relevant mid- and high-frequency irregularities. To address these challenges, we propose ADC-GNN, short for Attention-guided Diffusion-Contrastive Graph Neural Network, a unified framework that combines diffusion-guided feature augmentation, contrastive representation learning, and multi-hop spectral attention for few-shot graph fraud detection. The diffusion component is formulated as a feature-space denoising augmentation mechanism rather than a full topology-generative graph diffusion model: it constructs noise-perturbed node-feature views under a cosine schedule and uses contrastive learning to stabilize node representations across perturbations. The spectral attention module further adaptively emphasizes fraud-relevant hop-level and relation-level cues. We evaluate ADC-GNN primarily on three public benchmarks and additionally report a proprietary real-world telecom transaction dataset with approximately 60,000 records as a private case study. Under the 1% training setting, ADC-GNN achieves consistent improvements over original graph fraud baselines and four protocol-consistent recent graph anomaly/fraud baselines on the public benchmarks. Additional analyses on split stability, training ratios, oversampling alternatives, module-level ablations, diffusion schedules, and runtime and memory-consumption comparisons further characterize the effective operating regime of ADC-GNN.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

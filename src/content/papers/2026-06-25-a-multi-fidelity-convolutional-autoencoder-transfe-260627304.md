---
title: A Multi-Fidelity Convolutional Autoencoder-Transfer Learning Framework for
  Guided-Wave-Based Damage Diagnosis Using Large Simulated and Limited Experimental
  Datasets
title_zh: A Multi-Fidelity Convolutional Autoencoder-Transfe
authors:
- Santosh Kapuria
- Abhishek
arxiv_id: '2606.27304'
url: https://arxiv.org/abs/2606.27304
pdf_url: https://arxiv.org/pdf/2606.27304
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Guided wave-based structural health monitoring (GWSHM) with onboard transducers
  offers signific...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Guided wave-based structural health monitoring (GWSHM) with onboard transducers offers significant potential for the early diagnosis of damage in engineering structures. However, the practical deployment of deep learning models is often hindered by the limited availability of labelled experimental data and the high computational cost of generating large-scale high-fidelity simulation datasets. This study presents a multifidelity transfer learning framework that integrates lightweight physics-based simulations, convolutional autoencoder (CAE)-based deep feature learning, a feed-forward neural network, and limited experimental measurements for accurate damage localisation and sizing in plate-like structures instrumented with piezoelectric transducers. A computationally efficient one-dimensional time-domain spectral element model is employed to generate a large synthetic dataset for pretraining, while transfer learning adapts the model to experimental domains using only a small amount of labelled data. The CAE-based transfer learning framework significantly outperforms its CNN-based counterpart in damage localisation accuracy. The model achieves excellent predictive performance with $R^2$ scores exceeding 0.93 for damage localisation and 0.99 for damage sizing. Its generalisation capability is demonstrated on previously unseen data, showing high prediction accuracy for damage scenarios not represented during pretraining or fine-tuning. The results establish the proposed framework as an accurate, computationally efficient, and practically viable solution for real-world GWSHM applications.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

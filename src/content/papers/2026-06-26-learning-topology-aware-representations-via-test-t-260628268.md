---
title: Learning Topology-Aware Representations via Test-Time Adaptation for Anomaly
  Segmentation
title_zh: Learning Topology-Aware Representations via Test-T
authors:
- Ali Zia
- Usman Ali
- Abdul Rehman
- Umer Ramzan
- Kang Han
- Muhammad Faheem
- Shahnawaz Qureshi
- Wei Xiang
arxiv_id: '2606.28268'
url: https://arxiv.org/abs/2606.28268
pdf_url: https://arxiv.org/pdf/2606.28268
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Test-time adaptation (TTA) has emerged as a promising paradigm for mitigating
  distribution shif...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Test-time adaptation (TTA) has emerged as a promising paradigm for mitigating distribution shifts in deep models. However, existing TTA approaches for anomaly segmentation remain limited by their reliance on pixel-level heuristics, such as confidence thresholding or entropy minimisation, which fail to preserve structural consistency under noise and texture variation. Moreover, they typically treat anomaly maps as flat intensity fields, ignoring the higher-order spatial relationships that characterise complex defect geometries. We introduce TopoTTA (Topological Test-Time Adaptation), a novel framework that integrates persistent homology, a tool from topological data analysis, into the TTA pipeline to enforce geometric and structural coherence during adaptation. By applying multi-level cubical complex filtration to anomaly score maps, TopoTTA derives robust topological pseudo-labels that guide a lightweight test-time classifier, enhancing segmentation quality without retraining the backbone model. The approach avoids reliance on method-specific raw-score thresholding for mask binarisation, preserves connectivity, and generalises across both 2D and 3D modalities. Extensive experiments across six standard benchmarks (MVTec AD, VisA, Real-IAD, MVTec 3D-AD, AnomalyShapeNet, and MVTec LOCO) demonstrate an average 15% F1 improvement over state-of-the-art unsupervised anomaly detection and segmentation methods, with the largest gains on anomalies exhibiting complex geometric or structural variations. These findings suggest that integrating topological reasoning into test-time adaptation provides a principled route to structure-aware generalisation, bridging the gap between geometric learning and robust adaptation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

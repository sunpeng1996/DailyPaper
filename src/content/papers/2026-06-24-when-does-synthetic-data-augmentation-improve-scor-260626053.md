---
title: When Does Synthetic Data Augmentation Improve Score-Based Imbalanced Classification?
title_zh: When Does Synthetic Data Augmentation Improve Scor
authors:
- Zhengchi Ma
- Pengfei Lyu
- Anru R. Zhang
arxiv_id: '2606.26053'
url: https://arxiv.org/abs/2606.26053
pdf_url: https://arxiv.org/pdf/2606.26053
published: '2026-06-24'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Synthetic data augmentation is widely used to mitigate class imbalance,
  but its theoretical eff...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Synthetic data augmentation is widely used to mitigate class imbalance, but its theoretical effects on score-based classification remain poorly understood. This paper develops a framework for characterizing when synthetic minority augmentation can improve threshold-integrated and threshold-optimized metrics, including AUROC, AUPRC, best-threshold balanced accuracy, and best-threshold \(\F_1\) score. We separate the effect of augmentation into two components: a change in effective class weighting and a discrepancy between the synthetic and true minority distributions. Under well-specified score models, the raw estimator already targets the likelihood-ratio ordering, which is population-optimal for the metrics considered. Consequently, augmentation cannot provide a fundamental population-level improvement beyond possible finite-sample variance reduction, and may introduce additional bias through synthetic distributional error. We further establish minimax lower bounds showing that the raw estimator already achieves the optimal metric-regret rate in the well-specified regime. Under misspecification, however, augmentation can play a qualitatively different role: by changing the effective class balance, it can alter the restricted-class projection and correct ranking errors induced by the raw imbalanced objective. We provide explicit improvement bounds quantifying the roles of approximation error, finite-sample estimation error, and synthetic distributional error. Simulation studies corroborate the theory, demonstrating limited gains under well-specification and nontrivial but nonmonotone improvements under misspecification.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

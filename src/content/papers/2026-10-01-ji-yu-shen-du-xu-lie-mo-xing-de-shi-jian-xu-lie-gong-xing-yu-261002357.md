---
title: Conformal Prediction for Time Series with Deep Sequence Models
title_zh: 基于深度序列模型的时间序列共形预测方法
authors:
- Junghwan Lee
- Jonghyeok Lee
- Yao Xie
affiliations:
- H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute
  of Technology
arxiv_id: '2610.02357'
url: https://arxiv.org/abs/2610.02357
pdf_url: https://arxiv.org/pdf/2610.02357
published: '2026-10-01'
collected: '2026-10-05'
category: Other
direction: 时间序列预测 · 不确定性量化
tags:
- Conformal Prediction
- Time Series
- Deep Sequence Model
- Uncertainty Quantification
- Transformer
one_liner: 系统探究三类深度序列模型适配时序共形预测的方案，给出理论保证及实验验证
practical_value: '- 电商大促销量预测、用户长短期行为序列预测场景可直接复用三类深度序列模型结合Conformal Prediction的框架，产出带置信度的预测区间，降低备货、流量调度的决策风险

  - 时序类预测任务需要不确定性量化能力时，可参考本文三类方案的选型逻辑，无需额外假设数据分布，大幅降低落地成本

  - 若业务对预测结果的覆盖性有合规要求，可复用本文的渐近条件覆盖理论验证思路，快速对齐业务指标要求'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
深度学习时序预测落地对可靠不确定性量化的需求激增，Conformal Prediction作为无分布假设、可提供覆盖性保证的预测区间构建框架，核心依赖数据可交换性假设，而时序数据天然违反该假设；同时现有研究缺乏深度序列模型适配时序Conformal Prediction的系统性分析。
### 方法关键点
系统探究三类深度序列模型结合时序Conformal Prediction的实现路径：1）条件分位数回归；2）条件分位数函数估计；3）局部化Conformal Prediction，从理论层面证明三类方案在合理假设下均具备渐近条件覆盖保证。
### 关键结果
在多组真实世界时序数据集上的实验表明，三类结合深度序列模型的方案效果均显著优于传统基线，预测区间的实际覆盖率与理论保证值偏差小于2%，同时区间宽度更窄，实用性更强。

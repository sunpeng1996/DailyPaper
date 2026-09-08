---
title: 'MomentQuant: an even more minimalist interval method with linear time complexity
  for time series classification'
title_zh: MomentQuant：线性时间复杂度的极简时间序列分类区间方法
authors:
- Johann Faouzi
affiliations:
- Univ Rennes
- Ensai
- CNRS
- CREST - UMR 9194
arxiv_id: '2609.05136'
url: https://arxiv.org/abs/2609.05136
pdf_url: https://arxiv.org/pdf/2609.05136
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 时间序列分类 · 轻量推理效率优化
tags:
- TimeSeriesClassification
- EfficientInference
- QuantileApproximation
- FeatureExtraction
- LowComplexity
one_liner: 优化Quant算法并采用Cornish-Fisher近似分位数，实现线性时间的高性价比时间序列分类方法
practical_value: '- 电商用户行为序列分类、流量时序异常检测等轻量时序任务，可复用Cornish-Fisher近似分位数trick，省去排序步骤降低推理时延

  - 线上高QPS时序特征提取链路优化时，可参考本文的近似思路，在精度损失可接受的前提下大幅提升吞吐

  - 推理频次远高于训练的时序分类场景，可直接复用MomentQuant的极简架构，平衡效果与计算成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
时间序列分类广泛应用于各领域，现有方案普遍存在预测性能与计算成本的权衡问题；此前的区间分位数算法Quant精度高、速度快，但仍有推理效率优化空间，尤其适配推理频次远高于训练的线上业务场景。
### 方法关键点
1. 对原Quant算法做工程层面的无精度损失优化实现，无算法逻辑改动
2. 推出MomentQuant，采用Cornish-Fisher展开生成近似分位数替代精确分位数，完全省去时序排序步骤，将时间复杂度降至线性
### 关键结果
优化后的Quant实现速度显著高于原版本；MomentQuant比优化后的Quant推理速度更快，仅伴随可忽略的微小预测性能下降。

---
title: 'Drift and Dependence: Layer-wise Information-Theoretic Bounds for Replay-Based
  Continual Learning'
title_zh: 漂移与依赖：基于回放的持续学习的分层信息论边界
authors:
- Tieliang Gong
- Zhongbo Zhang
- Wen Wen
- Yong-Jin Liu
arxiv_id: '2608.11690'
url: https://arxiv.org/abs/2608.11690
pdf_url: https://arxiv.org/pdf/2608.11690
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 持续学习 · 回放机制泛化性分析
tags:
- Continual Learning
- Experience Replay
- Information Theory
- Generalization Bound
- Wasserstein Distance
one_liner: 提出分层信息论框架拆分回放式持续学习泛化误差，给出遗忘在线诊断方法
practical_value: '- 跨域/多场景持续学习推荐模型调优时，可借鉴分层稳定策略，优先冻结漂移敏感度最低的中间层，降低旧场景遗忘

  - 多任务迭代训练链路可引入曲率感知梯度对齐统计量，在线监测旧任务遗忘程度，省去额外离线评估开销

  - 小样本回放buffer大小规划可参考论文给出的内存缩放规律，平衡存储成本与遗忘控制效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
基于回放的持续学习是解决 catastrophic forgetting 的主流方案，但现有分析未拆分「有限样本回放导致的分布偏移」和「优化轨迹耦合」两个耦合效应对泛化的影响，无法指导实践调优。

### 方法关键点
1. 提出分层信息论框架，将泛化误差拆分为回放诱导的表征漂移项和优化依赖项，后者进一步拆解为稳定性、可塑性、交互、残差耦合四个子项；
2. 用Wasserstein松弛漂移项，得到分层漂移-敏感度trade-off，可直接定位需要稳定的中间层；
3. 基于SGLD实现优化项计算，导出曲率感知梯度对齐统计量，可在线诊断任务级遗忘。

### 关键结果
控制实验和基准测试验证了理论预测的内存缩放规律、中间层漏斗效应，以及梯度对齐信号与遗忘的强关联。

---
title: Correlation-Aware Evidential Fusion for Trusted Multi-View Classification
title_zh: 面向可信多视图分类的相关性感知证据融合框架
authors:
- Tianyang Wang
- Mengchi Zuo
- Cai Xu
- Yilin Zhang
- Ziyu Guan
- Wei Zhao
affiliations:
- School of Computer Science and Technology, Xidian University, China
arxiv_id: '2611.33900'
url: https://arxiv.org/abs/2611.33900
pdf_url: https://arxiv.org/pdf/2611.33900
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 多视图分类 · 可信证据融合
tags:
- Multi-View Classification
- Evidence Fusion
- Uncertainty Calibration
- Correlation Awareness
- Trusted AI
one_liner: 提出相关性感知证据融合框架CAFE，解决多视图分类中相关证据重复计数与不确定性校准偏差问题
practical_value: '- 多模态/多特征推荐场景融合用户行为、内容、上下文等视图特征时，可引入相关性感知约束，避免高相关特征重复加权导致的推荐偏差

  - 推荐系统不确定性校准优化时，可复用CAFE的互补性信任折扣逻辑，提升高风险场景（如高客单价商品、信贷推荐）的决策可靠性

  - 多Agent协作决策流程中，融合多Agent输出结果时可参考样本自适应权重机制，根据任务上下文动态调整各Agent输出权重'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有可信多视图分类方法默认各视图为独立信息源，忽略视图间相关性，导致高相关证据被重复计数、互补证据权重被压低，既限制分类精度，也会引发不确定性估计校准偏差。
### 方法关键点
- 对各视图私有专家输出的证据做基于互补性的信任折扣，引入相关性感知约束降低相似证据的重复贡献
- 从全局多视图上下文学习样本级自适应权重，将相关性调整后的私有证据与跨视图协作证据做自适应融合
### 关键结果
在6个真实数据集上稳定提升分类与校准性能，当视图间存在强相关性时性能增益尤其显著

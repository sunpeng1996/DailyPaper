---
title: Optimal Recalibration of an Online Predictor
title_zh: 在线预测器的最优重校准方法
authors:
- Lunjia Hu
- Kevin Tian
- Chutong Yang
affiliations:
- Northeastern University
- University of Texas at Austin
arxiv_id: '2607.19689'
url: https://arxiv.org/abs/2607.19689
pdf_url: https://arxiv.org/pdf/2607.19689
published: '2026-07-22'
collected: '2026-07-25'
category: Training
direction: 在线学习 · 预测器校准优化
tags:
- Online Learning
- Calibration
- Proper Loss
- Distribution Shift
- Online Prediction
one_liner: 提出最优在线预测器重校准算法，实现(ε,ε²)重校准，同时达成近最优校准与calibeating速率
practical_value: '- 推荐/广告CTR/CVR排序模型在线预测阶段可复用该重校准方法，解决分布漂移下的置信度偏差问题，降低proper loss下的额外误差

  - 多基线模型融合场景可适配多hint序列扩展版算法，在保证校准性的同时最小化相对原始基线的误差损失

  - 对校准性要求高的预估任务，可参考(ε,ε²)误差权衡关系做精度与收敛速度的tradeoff调优'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有在线预测器重校准方案无法同时满足高校准度、低额外误差要求，校准与calibeating指标优化往往分离，收敛速率差，分布漂移场景下性能受限。

### 方法关键点
基于不平衡扩展的同步Blackwell可达性归约框架设计在线重校准算法，支持单/多hint预测序列输入，适配Lipschitz proper损失。

### 关键结果
1. 针对Lipschitz proper损失仅需T≈ε⁻³轮即可实现(ε,ε²)重校准，该权衡在平方损失下被证明最优；
2. K₂重校准变体仅增加对数因子开销，同时实现ε级校准、ε²级calibeating，解决了此前学界开放问题；
3. 分布漂移分类数据集上验证了算法有效性。

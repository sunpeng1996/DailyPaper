---
title: 'AdaPixFlow: Learning Continuous-Time 3D Dynamics Across Scenes from Sparse
  Multi-view Observations'
title_zh: AdaPixFlow：基于稀疏多视角观测的跨场景连续3D动态学习
authors:
- Hrishikesh Viswanath
- Aniket Bera
affiliations:
- Purdue University
arxiv_id: '2611.26433'
url: https://arxiv.org/abs/2611.26433
pdf_url: https://arxiv.org/pdf/2611.26433
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 3D动态建模 · 跨场景时序预测
tags:
- 3D Dynamics
- Multi-view Learning
- Temporal Prediction
- Motion Prior
- Voxel Fusion
one_liner: 提出无需预定义运动模型的跨场景连续时间3D动态预测方法AdaPixFlow
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D动态预测方案要么依赖单场景优化的速度场，要么需预定义物理/运动学假设，泛化性差，无法跨场景复用运动先验。
### 方法关键点
1. 无需单场景优化和预定义运动模型，仅从多视角RGB-D观测学习跨场景连续时间动力学算子
2. 多相机观测先融合为世界坐标下的共享voxel grid，再预测连续时间velocity field，跨场景训练习得的运动先验可迁移到未知场景
3. 基于观测状态积分velocity field，可预测观测区间内及观测序列外的物体位置
### 关键结果
- PhysInOne留存场景：较最优基线帧间预测F1提升2.5%，未来预测F1提升15%；较单场景速度场方法分别提升30%、85%
- 零样本迁移到Spring-Gaus数据集，未来预测F1提升12%

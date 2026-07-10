---
title: 'Unraveling Machine Behavior by Multi-Level Bias Analysis and Detection: Methodology
  and Application to Computer Vision'
title_zh: 多层次偏差分析检测方法解析机器学习行为及计算机视觉应用
authors:
- Ignacio Serna
- Aythami Morales
- Julian Fierrez
affiliations:
- Max Planck Institute for Human Development
- BiometricsAI, UAM Madrid
- Department of Mathematics, ULPGC
arxiv_id: '2607.07236'
url: https://arxiv.org/abs/2607.07236
pdf_url: https://arxiv.org/pdf/2607.07236
published: '2026-07-08'
collected: '2026-07-10'
category: Other
direction: 机器学习模型偏差检测与可解释性分析
tags:
- Bias Detection
- Latent Space
- Activation Analysis
- Model Interpretability
- Computer Vision
one_liner: 从潜空间、激活、权重三级提出可解释偏差检测方法，性能优于传统黑盒检测方案
practical_value: '- 可将三级偏差检测思路迁移到推荐模型公平性优化：分别从召回层语义潜空间、排序层神经元激活、模型参数三个维度检测不同人群/商品的曝光偏差

  - SpaceBias的组间分布KS检验方法可直接复用，用于评估推荐系统不同用户群体的候选集分布差异，快速定位马太效应问题

  - 欠代表群体激活值更低的结论可用于冷启动用户/商品识别，针对性调整激活阈值或补充训练样本，提升冷群推荐效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统模型偏差检测多为黑盒式仅评估输出结果，无法定位偏差在神经网络内部的传播路径，难以指导针对性优化。
### 方法关键点
建立潜空间、层激活、模型参数三级偏差分析框架，对应三种检测方法：
1. 全新SpaceBias基于分类前潜空间的邻域概率分布，用Kolmogorov-Smirnov检验量化组间偏差；
2. ActivationBias扩展现有InsideBias方法，用Mann-Whitney U检验分析卷积层激活，识别激活值偏低的欠代表群体；
3. WeightBias扩展现有IFBiD方法，训练小模型直接从任务模型参数中识别偏差模式。
### 关键结果数字
在DiveFace人脸性别分类、带控偏差彩色MNIST数据集上验证，共测试超12.7万个不同偏差程度的模型，检测准确率随训练数据分布失衡程度正相关，偏差识别精度优于传统黑盒方法

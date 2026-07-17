---
title: 'Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise'
title_zh: Fisher秩膨胀：标签噪声下模型记忆化的谱特征
authors:
- Satwik Bathula
- Anand A. Joshi
affiliations:
- University of Southern California, Department of Electrical and Computer Engineering
arxiv_id: '2607.12438'
url: https://arxiv.org/abs/2607.12438
pdf_url: https://arxiv.org/pdf/2607.12438
published: '2026-07-14'
collected: '2026-07-17'
category: Training
direction: 模型训练 · 标签噪声检测
tags:
- Label Noise
- Memorization Detection
- Fisher Matrix
- Spectral Analysis
- Model Training
one_liner: 发现标签噪声下模型记忆脏标签过程的Fisher秩膨胀谱特征，可高效定位标注错误样本
practical_value: '- 推荐/广告排序模型训练时，可监控最后一层梯度的Fisher有效秩变化，提前发现标注脏数据（如点击作弊、标注错误），无需等测试效果下降再响应

  - 数据清洗场景可优先提取秩贡献TopN样本做校验，实验中Top100样本脏标签占比最高达96.2%，大幅降低人工核验成本

  - 标注质量评估可通过Fisher有效秩峰值量化噪声严重程度，峰值越高噪声占比越高，无需人工抽样即可快速判断数据集质量'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
带噪声标签训练深度模型时，模型会先学习有效结构再记忆脏标签，缺乏低成本方法在效果下降前提前定位记忆化阶段和脏样本。

### 方法关键点
1. 观测到样本级最后一层梯度的中心散度谱存在特征：记忆脏标签阶段Fisher有效秩先膨胀，拟合完脏标签后收缩，定义为Fisher秩膨胀现象
2. 推导一阶留一法归因公式，可快速计算每个样本对秩膨胀的贡献度，无需逐样本移除重训

### 关键结果
跨CIFAR数据集、CNN/ViT架构，Top100秩贡献样本的脏标签占比达69.2%~96.2%，自然噪声数据集CIFAR-10N上达94.4%±1.9%；Fisher有效秩峰值随噪声占比单调上升，干净训练峰值28.88±1.95，60%噪声时达97.09±1.78；秩膨胀起始点比可观测的测试效果下降更早出现。

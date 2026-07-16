---
title: Statistical Non-linear Reconstruction Loss for Image Anomaly Detection
title_zh: 面向图像异常检测的统计非线性重建损失
authors:
- Nguyen Minh Tri
- Hoang Khuong Duy
- Huynh Cong Viet Ngu
affiliations:
- AIC-Lab, FPT University
arxiv_id: '2607.12866'
url: https://arxiv.org/abs/2607.12866
pdf_url: https://arxiv.org/pdf/2607.12866
published: '2026-07-14'
collected: '2026-07-16'
category: Other
direction: 图像异常检测 · 损失函数优化
tags:
- Anomaly Detection
- Reconstruction Loss
- Outlier Leakage
- Industrial Inspection
- Autoencoder
one_liner: 提出带统计校准的sigmoid非线性重建损失，解决重建类图像异常检测的离群值泄露问题
practical_value: '- 离群值抑制思路可迁移至推荐系统样本清洗/损失优化场景，解决异常样本主导模型训练的问题

  - 基于正态分布置信区间的超参数校准方法可复用，避免人工调参不确定性，适配数据驱动超参选择

  - 非线性梯度抑制机制可用于召回/排序模型长尾样本训练，降低极端样本对通用特征的扰动'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于重建的无监督图像异常检测方法普遍存在离群值泄露问题：标准MSE损失会驱动模型还原异常模式，同时工业场景单模型适配多品类的统一框架需求下，传统损失鲁棒性不足。
### 方法关键点
- 非线性重建损失对高幅值特征施加基于sigmoid的压缩函数，抑制离群值主导优化过程，同时保留对正常模式的敏感度
- 引入统计校准方案，从正常特征分布的置信区间（CI）中选择缩放因子k，数据驱动控制抑制强度
### 关键结果
在MVTec-AD数据集上达到99.0% Image-AUROC、97.3% Pixel-AUROC，在VisA数据集上达到95.3% Image-AUROC、99.0% Pixel-AUROC，性能优于或持平SOTA方案。

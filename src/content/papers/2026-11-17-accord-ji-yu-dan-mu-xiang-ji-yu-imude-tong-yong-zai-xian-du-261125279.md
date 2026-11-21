---
title: 'Accord: Universal Online Metric Localization and Dense Mapping from one Camera
  and an IMU'
title_zh: Accord：基于单目相机与IMU的通用在线度量定位与稠密建图
authors:
- Jaafar Mahmoud
- Arthur Movsesyan
- Cuong Huynh
- Mikhail Iumanov
- Sergey Zagoruyko
- Sergey Kolyubin
affiliations:
- ITMO University
arxiv_id: '2611.25279'
url: https://arxiv.org/abs/2611.25279
pdf_url: https://arxiv.org/pdf/2611.25279
published: '2026-11-17'
collected: '2026-11-21'
category: Other
direction: 单目视觉惯性SLAM · 稠密度量建图
tags:
- SLAM
- VIO
- Dense Mapping
- Depth Foundation Model
- Factor Graph
one_liner: 提出通用单目相机+IMU稠密建图框架，无需逐数据集调优即可在多平台取得5cm精度领先F-score
practical_value: '- 多源信号自一致性校验思路可复用：如推荐系统跨召回源结果一致性校验，修正单路召回的系统性偏差

  - 通用无逐场景调优的架构设计思路：可借鉴到跨品类/跨场景推荐系统，降低不同业务的适配成本

  - 时序窗口多帧融合的因子图优化方法：可迁移到用户长短期行为序列的多兴趣建模与偏好对齐

  - 若业务涉及AR电商、线下门店商品定位，本框架可直接用于单设备低成本稠密空间建模'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
单目相机+IMU的稠密度量建图存在核心矛盾：VIO可输出度量级位姿但仅能生成稀疏几何信息，前馈深度基础模型可预测稠密结构但无法保证度量尺度一致性，现有方案需逐场景调优泛化性极差。

### 方法关键点
1. 以VIO输出的度量位姿为锚点，将关键帧窗口锚定到三角化得到的度量3D点上，锁定全局尺度基准；
2. 利用共视图像间的双向稠密深度一致性，在保留锚点度量尺度的前提下，估计并修正单图深度预测的尺度误差；
3. 引入上下文关键帧优化深度预测效果，最终通过因子图融合多个子图得到全局一致的稠密度量地图。

### 关键结果
单组固定配置跨5个公开数据集+自研手机/GoPro数据集测试，无需逐数据集调优、仅靠自身轨迹对齐，在所有平台的5cm精度指标下均取得最优或次优的平均F-score，框架及数据集已开源。

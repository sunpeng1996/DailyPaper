---
title: 'OC-GS: Gaussian Splatting for Irregular Turntable Capture'
title_zh: OC-GS：面向不规则转台采集的对象中心高斯溅射重建方法
authors:
- Jae Joong Lee
- Bedrich Benes
affiliations:
- Purdue University
arxiv_id: '2609.31572'
url: https://arxiv.org/abs/2609.31572
pdf_url: https://arxiv.org/pdf/2609.31572
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 3D重建 · 高斯溅射优化
tags:
- Gaussian Splatting
- 3D Reconstruction
- Pose Optimization
- Turntable Capture
- Sparse View Reconstruction
one_liner: 提出带轨道一致性优化的对象中心高斯溅射方法，提升不规则转台稀疏采集的3D重建精度
practical_value: '- 电商商品3D数字化场景可直接复用OC-GS方案，解决低成本转台采集时丢帧、转速不均导致的3D重建精度下降问题

  - 稀疏视角采集时同步优化角度和几何的思路，可降低商品3D建模的拍摄成本，仅需6~12张不规则采样图即可完成重建

  - 共享运动约束+初始估计联合优化的架构，可迁移至固定约束下的多视角重建任务（如货架扫拍商品建模）'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
转台采集是商品、文物、工业零件等3D建模的主流方案，但稀疏采样、转速不均、丢帧会导致传统等角度假设失效，现有无姿态高斯溅射方法在该场景下重建精度不足。
### 方法关键点
提出对象中心的OC-GS框架，在固定共享相机、旋转轴、支点的约束下做轨道一致性优化，联合优化图像推导的几何信息与每张图的实际采集角度，同时保留图像角度初始化和共享运动模型两个核心模块提升稳定性。
### 关键结果
12/8/6张不规则视角渲染数据上，前景PSNR分别达21.26/19.36/15.83dB，优于所有4个无姿态高斯溅射基线；固定训练器下，角度优化比固定初始估计提升PSNR 7.88dB，真实采集场景下提升0.70dB

---
title: 'InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion'
title_zh: InitFree-SfM：无初始化光束平差与学习式运动恢复结构结合方案
authors:
- Simon Weber
- Mateo de Mayo
- Je Hyeong Hong
- Carl Olsson
- Daniel Cremers
- Ronald Clark
affiliations:
- University of Oxford
- Technical University of Munich
- Munich Center for Machine Learning
- Hanyang University
- Lund University
arxiv_id: '2611.31516'
url: https://arxiv.org/abs/2611.31516
pdf_url: https://arxiv.org/pdf/2611.31516
published: '2026-11-22'
collected: '2026-11-28'
category: Other
direction: 三维重建 · 无初始化运动恢复结构
tags:
- Structure-from-Motion
- Bundle Adjustment
- 3D Reconstruction
- Depth Estimation
- Optimization
one_liner: 提出融合度量深度约束的无初始化SfM管线，性能优于现有无初始化BA方法，精度对标成熟SfM方案
practical_value: '- 电商3D商品建模场景可借鉴无初始化BA思路，降低对拍摄初始参数的要求，简化普通用户上传商品图的3D重建流程；

  - 3D重建优化目标可参考dOSE设计，在原有重投影误差基础上增加深度约束，提升低重叠度商品实拍图的重建精度；

  - 零散用户上传商品图的3D重建任务，可复用其深度一致轨迹构建+联合度量优化的管线，提升零散数据重建成功率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
传统Bundle Adjustment（BA）依赖良好的初始全局估计，现有无初始化BA方案优化代理目标Object Space Error（OSE）时，存在优化目标值低但重建精度差的gap，复杂场景下3D重建效果远低于成熟SfM管线。
### 方法关键点
1. 构建完整无初始化SfM管线，融合学习得到的匹配对、度量深度、深度一致轨迹构建、联合度量优化四大模块；
2. 设计深度增强的OSE目标dOSE，在OSE的方向约束基础上补充沿视线方向的地标位置约束，弥补代理目标与真实重建精度的偏差。
### 关键结果
性能大幅优于现有无初始化BA方法，精度与成熟SfM管线达到可比水平，在低重叠度图像集上仍具备竞争力；同时验证几何约束是高精度重建的核心，OSE优化仅提供辅助增益。

---
title: 'HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention
  Fusion'
title_zh: HandMvNet：基于多视图交叉注意力融合的实时3D手部姿态估计
authors:
- Muhammad Asad Ali
- Nadia Robertini
- Didier Stricker
affiliations:
- German Research Center for Artificial Intelligence (DFKI)
- University of Kaiserslautern-Landau (RPTU)
arxiv_id: '2608.20093'
url: https://arxiv.org/abs/2608.20093
pdf_url: https://arxiv.org/pdf/2608.20093
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 3D手部姿态估计 · 多视图特征融合
tags:
- 3D-Pose-Estimation
- Cross-Attention
- Multi-view-Fusion
- Real-time-Inference
- Computer-Vision
one_liner: 提出无相机参数依赖的多视图注意力融合网络，实现高精度实时3D手部姿态与形状估计
practical_value: '- 主要为计算机视觉方向学术贡献，电商/推荐/Agent业务直接可落地场景有限

  - 无先验参数的多视图跨注意力融合思路，可迁移至多模态推荐的多源异构特征融合模块设计

  - 低延迟推理的模型结构优化逻辑，可参考用于实时推荐链路的模型轻量化改造'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单视图3D手部姿态估计存在固有尺度-深度歧义问题，传统多视图方案依赖相机参数作为输入，且推理延迟高，无法满足AR/VR、人机交互等实时场景的落地要求。
### 方法关键点
1. 设计多视图交叉注意力融合模块，高效整合多视角图像特征，从底层解决单视图的深度/尺度歧义问题；
2. 无需额外输入相机校准参数即可自主学习3D几何信息，大幅降低部署门槛；
3. 对模型推理链路做轻量化优化，在精度损失可控前提下压缩推理耗时。
### 关键结果
公开数据集测试中，定性、定量指标全面优于同期SOTA方法，同时实现实时推理性能，适配低延迟交互场景。

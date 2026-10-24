---
title: 'HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction'
title_zh: HiP3R：面向长时序3D重建的分层位姿图优化方法
authors:
- Zunnan Xu
- Shangchen Zhou
- Yihang Luo
- Chen Change Loy
affiliations:
- S-Lab, Nanyang Technological University
- Imperial College London
- ACE Robotics
arxiv_id: '2610.31635'
url: https://arxiv.org/abs/2610.31635
pdf_url: https://arxiv.org/pdf/2610.31635
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 长时序3D重建 · 位姿图优化
tags:
- 3D Reconstruction
- Pose Graph Optimization
- Long Video Processing
- Hierarchical Modeling
one_liner: 提出分层位姿图架构，兼顾长视频3D重建全局一致性与局部精度，无需额外训练
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
前馈模型可在短视频窗口下精准估计相机运动与3D几何，但受计算、内存限制无法直接处理数千帧长序列；分块处理会导致局部重建坐标系不一致、共享相机估计重复。现有位姿图优化存在层级权衡：块级图可高效解决尺度漂移、闭合大回环，但无法修正内部误差；帧级优化局部灵活，但全局扩展计算成本高、易破坏度量尺度。
### 方法关键点
提出HiP3R分层位姿图架构：1. 先优化鲁棒的块级Sim(3)图，确立全局布局与尺度；2. 固定全局布局，逐帧估计共享SE(3)相机参数，将重叠窗口预测整合为单条轨迹；无需额外训练或微调，支持分块、流式两种后端。
### 关键结果
在多基准测试集上验证可有效提升相机轨迹精度与3D重建效果。

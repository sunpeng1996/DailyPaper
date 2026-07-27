---
title: 'GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and
  Spatial Decomposition'
title_zh: GLAM-SLAM：基于光流稠密化与空间分解的实时大规模高斯建图
authors:
- Panagiotis Mermigkas
- Argyris Manetas
- Petros Maragos
arxiv_id: '2607.21416'
url: https://arxiv.org/abs/2607.21416
pdf_url: https://arxiv.org/pdf/2607.21416
published: '2026-07-23'
collected: '2026-07-27'
category: Other
direction: 3D高斯泼溅 · 大场景实时SLAM
tags:
- 3D Gaussian Splatting
- SLAM
- Large-scale Mapping
- Real-time System
- Flow Densification
one_liner: 提出面向大尺度户外场景的解耦实时3D高斯泼溅SLAM系统，重建精度较次优方案高15%且支持长序列
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于3D Gaussian Splatting的单目SLAM系统仅适配短序列、非实时、GPU内存开销过高，无法落地长时序真实大场景任务。
### 方法关键点
1. 采用解耦架构，前端基于鲁棒特征SLAM实现轻量跟踪，映射端用结构化稀疏锚点网格表征，兼顾可扩展性与长序列场景一致性；
2. 提出基于极线约束的几何光流稠密化锚定策略，满足3DGS的稠密初始化需求；
3. 引入空间划分策略，将大场景建图转化为多子场景问题，通过MLP初始化注入空间归纳偏置生成局部高斯。
### 关键结果
在KITTI Odometry、Oxford RobotCar、M'alaga长序列数据集测试，重建精度较次优方案提升15%，同时保持实时性能，可支持更长序列建模

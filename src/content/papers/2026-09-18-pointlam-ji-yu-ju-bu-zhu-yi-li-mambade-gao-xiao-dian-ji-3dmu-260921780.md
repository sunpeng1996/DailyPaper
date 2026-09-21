---
title: 'PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection'
title_zh: PointLAM：基于局部注意力Mamba的高效点基3D目标检测方法
authors:
- Xuanming Shang
- Weijia Zhang
- Chao Ma
affiliations:
- MoE Key Lab of Artificial Intelligence, Institute of AI, Shanghai Jiao Tong University
arxiv_id: '2609.21780'
url: https://arxiv.org/abs/2609.21780
pdf_url: https://arxiv.org/pdf/2609.21780
published: '2026-09-18'
collected: '2026-09-21'
category: Other
direction: 3D点云目标检测 · Mamba效率优化
tags:
- 3D Object Detection
- Point Cloud
- Mamba
- Efficient Model
- Autonomous Driving
one_liner: 提出LPS采样器与LHA聚合器优化点基3D检测效率，性能媲美优化体素方案且小目标检测更优
practical_value: '- 稀疏数据下的LPS结构感知采样思路可迁移到用户行为序列下采样场景，替代FPS/随机采样，保留高价值行为的同时降低计算量

  - LHA的空间索引与特征解耦、Hadamard门控聚合思路可复用在推荐系统邻域召回/特征聚合模块，降低k-NN类动态查询的计算开销

  - 局部注意力+Bi-Directional Mamba的长短依赖融合架构可借鉴到长序列用户行为建模任务，平衡效果与推理效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
点基3D点云检测保留几何保真度，但FPS下采样、k-NN邻域查询与连续交互计算开销极高；体素基方法效率高但存在几何量化损失，两类方案存在精度与效率的权衡困境。
### 方法关键点
1. 设计Laplacian Point Sampler（LPS）：基于隐式离散拉普拉斯高通滤波+双重排序采样，实现结构感知的快速前景保留下采样，解决下采样瓶颈。
2. 提出Local Hadamard Aggregator（LHA）：用临时网格解耦空间索引与特征表示，通过Hadamard门控实现拓扑感知的注意力调制，替代复杂连续交互，降低局部建模延迟。
3. 融合局部门控与Bi-Directional Mamba（BDM）层构建LAM块，兼顾局部细粒度特征与全局序列依赖建模。
### 关键结果
在nuScenes、Waymo数据集上性能达到点基检测器SOTA水平，媲美高度优化的体素基方案，计算量仅为其数分之一，小实例检测、极稀疏数据处理性能优势显著。

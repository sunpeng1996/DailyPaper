---
title: 'Foundation4D: Towards a unified perception and reconstruction model for autonomous
  vehicles'
title_zh: Foundation4D：面向自动驾驶的统一感知与重建模型
authors:
- NVIDIA
- Sérgio Agostinho
- Maximilian Apodaca
- Emmanuel Attia
- Guillem Braso
- George Dong
- Ilya Fedorov
- Michele Fenzi
- Gang Huang
- Jiahui Huang
affiliations:
- NVIDIA
arxiv_id: '2610.30340'
url: https://arxiv.org/abs/2610.30340
pdf_url: https://arxiv.org/pdf/2610.30340
published: '2026-10-20'
collected: '2026-10-25'
category: Other
direction: 自动驾驶多任务感知与3D重建
tags:
- AutonomousDriving
- MultiTaskLearning
- SpatiotemporalAttention
- 3DReconstruction
- Benchmark
one_liner: 提出统一多任务感知模型Foundation4D，实现自动驾驶多摄像头视频的多维度场景感知与重建
practical_value: '- 多任务联合训练的收益思路可迁移至多目标推荐场景：相关任务联合训练相比单任务训练可提升核心指标，可复用该范式设计召回/排序多目标联合训练逻辑

  - 因子化spatiotemporal attention的高效建模方法可迁移至用户长行为序列建模，降低跨时空特征融合的计算开销

  - 任务专属benchmark的构建思路可复用至推荐系统效果评测，针对业务场景定制标注pipeline和垂直评测数据集'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
自动驾驶场景需同时完成几何估计、3D检测、semantic occupancy等多类感知重建任务，现有单任务模型复杂度高、信息复用率低，缺乏统一基准评测体系。

### 方法关键点
1. 提出统一前馈模型Foundation4D，共享骨干网络采用因子化spatiotemporal attention，高效融合多摄像头、多时间步观测信息；
2. 推理pipeline引入姿态图优化校准相机轨迹，跨输入窗口聚合对象跟踪结果；
3. 配套构建标注pipeline，发布含1253段驾驶片段密集深度、semantic occupancy标签的PAI-Foundation4D基准。

### 关键结果
微调后在Waymo、nuScenes上取得最低深度AbsRel，nuScenes最高检测mAP，OpenOccupancy最高occupancy mIoU；多任务联合训练相比单任务，检测mAP提升1.2个点，相机到rig平移误差降低13.4%。

---
title: 'X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras'
title_zh: X-Lens：适配异构相机的实时度量深度估计模型
authors:
- Heng Zhou
- Shuhong Liu
- Yonghao He
- Bohao Zhang
- Fa Fu
- Chenhui Hou
- Xianbao Hou
- Lijun Han
- Wei Sui
affiliations:
- D-Robotics
- The University of Tokyo
- Soochow University
arxiv_id: '2607.12993'
url: https://arxiv.org/abs/2607.12993
pdf_url: https://arxiv.org/pdf/2607.12993
published: '2026-07-14'
collected: '2026-07-16'
category: Other
direction: 异构相机实时3D度量深度估计
tags:
- Depth Estimation
- Heterogeneous Cameras
- Real-time Perception
- 3D Vision
- Lightweight Model
one_liner: 用仅0.04B参数的轻量模型实现异构鱼眼/针孔相机的实时高精度度量深度估计
practical_value: '- 若开展AR电商导购、虚拟试穿、无人零售货柜3D感知业务，可借鉴可学习校准token方案实现不同规格采集相机的空间对齐，降低硬件适配成本

  - 端侧部署3D感知任务时可复用其紧凑架构设计，用Jacobian参数化畸变偏置替代复杂辅助重建任务，兼顾推理速度与精度

  - 跨设备视觉模型泛化训练可参考「公开真实数据集+大规模合成数据集」混合训练范式，降低真实场景标注成本

  - 无3D视觉相关业务的电商/推荐从业者可借鉴点有限'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有异构相机（鱼眼+针孔）度量深度估计方案参数量大、推理延迟高，依赖复杂辅助重建任务，难以满足实时下游感知需求，且跨相机泛化性差
### 方法关键点
1. 架构层面引入可学习校准token完成鱼眼与针孔投影空间粗对齐，在cross-attention中注入Jacobian参数化畸变偏置建模局部投影变化，提升跨相机一致性
2. 直接输出稠密深度与全局度量尺度，省略高计算量的辅助重建目标，降低推理与训练复杂度
3. 构建包含26.6万同步6视角帧、103个室内外场景的大规模合成数据集OmniScene，支撑跨场景泛化训练
### 关键结果
仅0.04B参数，推理速度达41FPS；在OmniScene-Full数据集上AbsRel相比最优基线降低25.4%，参数量减少88.9%，单鱼眼/单针孔场景性能也具备竞争力

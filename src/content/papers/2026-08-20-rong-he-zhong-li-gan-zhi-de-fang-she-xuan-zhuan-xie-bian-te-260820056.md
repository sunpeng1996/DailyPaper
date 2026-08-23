---
title: Gravity-aware partially calibrated absolute pose estimation from affine- or
  rotation-covariant features
title_zh: 融合重力感知的仿射/旋转协变特征部分校准绝对位姿估计
authors:
- Marcus Valtonen Örnhag
- Alberto Jaenal
- Stefan Adalbjörnsson
affiliations:
- Ericsson Research
- University of Zaragoza
arxiv_id: '2608.20056'
url: https://arxiv.org/abs/2608.20056
pdf_url: https://arxiv.org/pdf/2608.20056
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 视觉惯性融合绝对位姿估计
tags:
- Pose Estimation
- IMU
- Visual Localization
- RANSAC
- Feature Descriptor
one_liner: 利用IMU重力向量与特征局部几何构造低采样求解器，实现更快更准的定位与焦距估计
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统位姿估计方法未利用SIFT等特征描述子内嵌的局部几何信息，半校准绝对位姿方案需4个点对应关系，采样需求高、计算开销大；IMU已成为消费级设备标配，视觉+惯性融合可大幅提升定位系统的速度与鲁棒性，但部分校准场景下的绝对位姿估计优化方向尚未被探索。
### 方法关键点
基于IMU输出的重力向量与特征诱导的局部几何推导全新约束，支持绝对位姿与焦距联合估计，构造两款高效求解器：仅需1个仿射对应关系的UP1PfAC、仅需2个方向协变特征的UP2PfORI，大幅降低采样需求，适配RANSAC类框架简化鲁棒估计流程。
### 关键结果
在大规模公开数据集上与SOTA方法对比验证，所提方案实现了更快、更精准的定位与焦距估计效果，计算成本远低于传统半校准绝对位姿方法。

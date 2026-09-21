---
title: 'RawSLAM: Online HDR Gaussian SLAM from Linear Radiance'
title_zh: RawSLAM：基于线性辐射度的在线HDR高斯SLAM框架
authors:
- Marina Orozco González
- Luis Merino
affiliations:
- Universidad Pablo de Olavide (UPO), Spain
arxiv_id: '2609.20589'
url: https://arxiv.org/abs/2609.20589
pdf_url: https://arxiv.org/pdf/2609.20589
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 三维视觉 · HDR高斯SLAM在线重建
tags:
- SLAM
- Gaussian Splatting
- HDR
- 3D Reconstruction
- Online System
one_liner: 首个直接基于单曝光16位线性HDR图像的在线高斯SLAM框架，提升极端光照下鲁棒性
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有密集视觉SLAM系统几乎全部依赖8位LDR输入，极端光照场景下阴影、高光易引发跟踪漂移、建图崩溃；现有RAW/HDR重建管线均为离线实现，依赖SfM预处理，不支持大帧间运动场景。

### 方法关键点
1. 架构无关的HDR Gaussian Splatting模块，采用无MLP的高斯颜色特征对数参数化；
2. 基于Reinhard范围压缩的光度损失目标；
3. 结构引导的空间梯度加权策略。

### 关键结果
对比MonoGS的直接HDR适配版本，轨迹、重建精度均更优，可原生输出线性场景辐射度用于后期渲染处理；相同方案可直接跑8位输入，将MonoGS基线误差降低约50%；HDR高斯模块可无缝迁移到SplaTAM、Gaussian SLAM、DROID-W，完全消除高难度光照序列下的跟踪失败；配套开源10组真实室内序列数据集，包含16位RAW图像、对齐深度、IMU测量值、OptiTrack真值位姿。

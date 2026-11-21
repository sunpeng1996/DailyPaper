---
title: 'The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation'
title_zh: 掩码不是对象：面向3D高斯分割的体监督方法
authors:
- Jeonghwan Cho
- Minsu Kim
- Junyoung Hong
- Seon Joo Kim
affiliations:
- Yonsei University
arxiv_id: '2611.21383'
url: https://arxiv.org/abs/2611.21383
pdf_url: https://arxiv.org/pdf/2611.21383
published: '2026-11-15'
collected: '2026-11-21'
category: Other
direction: 3D高斯分割 · 体监督优化
tags:
- 3D Gaussian Splatting
- Segmentation
- Volumetric Supervision
- Benchmark
- 3D Vision
one_liner: 提出即插即用VODA体监督目标与Removal-3D基准，解决3D高斯分割体完整性不足问题
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D高斯分割方法依赖渲染2D掩码做监督与评估，梯度仅分配给渲染贡献高的高斯，导致遮挡/低贡献高斯监督不足，得到的掩码精度达标但3D实体选择不完整，无法支撑对象移除等3D编辑操作。
### 方法关键点
1. 提出即插即用的VODA监督目标，利用局部深度结构聚类像素对应的贡献高斯，直接监督深度簇内所有高斯，绕过传统贡献加权的梯度分配逻辑
2. 推出Removal-3D合成对象移除基准，配套RDE指标量化分割的体完整性，通过对比预测与真实深度变化完成评估
### 关键结果
在4个渲染类基线方法上，VODA在Removal-3D基准上持续提升体分割效果，同时在LERF、ScanNet数据集上性能保持或提升；可有效召回低贡献高斯，效果优于简单梯度重加权、空间传播方案

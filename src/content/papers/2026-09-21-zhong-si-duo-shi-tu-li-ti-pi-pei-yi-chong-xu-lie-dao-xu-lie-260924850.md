---
title: 'Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation'
title_zh: 重思多视图立体匹配：一种序列到序列建模方法
authors:
- Aoxiang Fan
- Corentin Dumery
- Nicolas Talabot
- Pascal Fua
affiliations:
- CVLab, EPFL, Switzerland
arxiv_id: '2609.24850'
url: https://arxiv.org/abs/2609.24850
pdf_url: https://arxiv.org/pdf/2609.24850
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 计算机视觉·多视图三维重建
tags:
- Multi-View Stereo
- 3D Reconstruction
- Transformer
- Sequence-to-Sequence
one_liner: 将多视图立体匹配重构为序列到序列任务，用带相机先验的Transformer架构实现SOTA性能
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有前馈MVS模型即便输入真值相机参数，也存在重建歧义导致的几何畸变；传统MVS采用序列到单映射范式，仅预测单参考视图深度，全局一致性差。

### 方法关键点
1. 重构MVS任务为序列到序列任务，联合预测所有输入视图的几何信息，打通传统MVS与前馈方法的技术路径；
2. 提出全局Transformer架构，嵌入两类相机先验模块：ray-map embeddings将相机参数注入图像patch token，实现相机感知能力；统一全局代价体替换传统单视图代价体，跨全视图联合捕获3D结构。

### 关键结果
在多个公开基准数据集上达到SOTA性能，效果全面超越现有传统MVS与前馈重建基线。

---
title: Quaternion Approximate Networks for Enhanced Image Classification and Oriented
  Object Detection
title_zh: 四元数近似网络：增强图像分类与定向目标检测性能
authors:
- Bryce Grant
- Peng Wang
arxiv_id: '2509.05512'
url: https://arxiv.org/abs/2509.05512
pdf_url: https://arxiv.org/pdf/2509.05512
published: '2026-10-26'
collected: '2026-10-29'
category: Other
direction: 四元数网络 · 定向目标检测与图像分类
tags:
- Quaternion Network
- Object Detection
- Image Classification
- CUDA Optimization
- Batch Normalization
one_liner: 提出基于实值运算分解汉密尔顿积的四元数近似网络，实现高效旋转等变图像分类与定向目标检测
practical_value: '- 四元数参数压缩思路可迁移至多模态embedding建模，大幅降低高维特征存储与计算开销，适合电商多模态召回、粗排场景

  - 用实值运算近似超复数运算的设计思路，可直接复用现有CUDA生态优化复杂特征算子，避免全栈重构

  - 独立分域Batch Norm的设计可借鉴至多模态特征归一化，提升跨域（文本/图像/商品属性）特征训练稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
常规CNN轴对齐检测框丢失关键旋转信息，传统四元数神经网络全四元数域运算部署难度高、效率低，无法满足资源受限场景旋转感知视觉任务需求。
### 方法关键点
1. 提出QUAN框架，通过实值运算分解汉密尔顿积近似四元数卷积，保留几何属性的同时可基于自定义CUDA kernel高效实现
2. 设计独立四元数批归一化（IQBN）提升训练稳定性，将四元数运算拓展至空间注意力机制
### 关键结果
分类任务较现有卷积、四元数模型精度更高、参数量更少、收敛更快；定向目标检测任务参数效率、旋转处理能力优于标准CNN，拿下四元数CNN在该任务SOTA。

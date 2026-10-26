---
title: 'Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction'
title_zh: Easy-3Dfy：面向单图像3D场景构建的对象级几何组合方法
authors:
- Ziang Zhang
- Wenyou Yi
- Zehan Wang
- Jiachen Xu
- Xintong Han
- Chunchao Guo
- Zhou Zhao
affiliations:
- Zhejiang University
- Tencent
arxiv_id: '2610.32250'
url: https://arxiv.org/abs/2610.32250
pdf_url: https://arxiv.org/pdf/2610.32250
published: '2026-10-22'
collected: '2026-10-26'
category: Other
direction: 3D场景构建 · 对象级几何组合
tags:
- 3D_Reconstruction
- Single_Image_3D
- Geometric_Composition
- Scene_Generation
- Foundation_Model
one_liner: 提出解耦3D对象生成与布局估计的组合工作流，单图3D场景重建效果全面优于SAM-3Dfy
practical_value: '- 电商虚拟展厅/AR商品展示场景搭建可参考解耦生成+布局对齐的架构，分别复用成熟的3D商品生成模型与空间感知大模型，降低端到端训练成本

  - 多3D资产拼接的场景生成任务可复用RPF对齐器的几何对应方法，提升对象摆放精度，无需全场景标注即可落地

  - 业务迭代时可分别升级3D对象生成器、空间理解模型，无需重构整个工作流，适配技术迭代速度更快'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有端到端单图3D场景重建方法（如SAM-3Dfy）难以同时兼顾精细场景几何精度与3D资产质量，而专用3D对象生成器、3D大模型分别在资产细节、空间理解上有独特优势，缺乏高效的组合框架融合两类能力。
### 方法关键点
1. 采用解耦式工作流，将3D对象生成与场景布局估计拆分，让两类专用模型各自发挥能力优势
2. 设计基于RPF的对齐模块，建立对象局部网格与部分场景点云的几何对应关系，恢复对象布局完成场景组合
3. 无需完整场景级标注即可训练，降低数据门槛
### 关键结果数字
在Scene-Maker、3D-FUTURE200两个基准数据集上，多个几何评估指标全面优于SAM-3Dfy，对象摆放精度、资产质量均有显著提升。

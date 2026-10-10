---
title: 'asdex: Automatic Sparse Differentiation in JAX'
title_zh: asdex：JAX生态下的自动稀疏微分工具包
authors:
- Adrian Hill
- Guillaume Dalle
affiliations:
- BIFOLD – Berlin Institute for the Foundations of Learning and Data
- Machine Learning Group, Technical University of Berlin
- LVMT, ENPC, Institut Polytechnique de Paris
arxiv_id: '2610.12336'
url: https://arxiv.org/abs/2610.12336
pdf_url: https://arxiv.org/pdf/2610.12336
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: 模型训练 · JAX 稀疏微分工具
tags:
- JAX
- Automatic Differentiation
- Sparse Matrix
- Training Optimization
- Hessian
- Jacobian
one_liner: JAX生态首个独立自动稀疏微分工具，可直接替换原生稠密雅克比、海森计算接口
practical_value: '- 用JAX做二阶优化（如推荐稀疏模型训练、多目标优化海森计算）的团队，可直接用asdex替换原生jax.hessian/jacobian，大幅降低大维度导数矩阵的内存占用与计算耗时

  - 稀疏模型（如稀疏特征召回/排序模型、MoE门控梯度计算）场景，可复用其「稀疏模式检测+图着色分组AD pass+压缩计算」pipeline优化自定义微分算子

  - 涉及大维度雅可比计算的任务（如Agent决策灵敏度分析、生成式推荐对抗训练梯度计算），可借鉴AD pass数与问题维度解耦的设计思路避免维度灾难'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
JAX原生自动微分接口计算雅克比/海森矩阵时生成稠密矩阵，AD pass数随矩阵维度线性增长，大维度稀疏导数场景下存在严重内存瓶颈与计算效率问题，此前JAX生态无独立可用的自动稀疏微分工具。

### 方法关键点
基于自动稀疏微分四步流程实现：1）检测与输入无关的导数稀疏模式；2）对图着色分组可共享AD pass的行/列；3）按颜色分组执行压缩微分，每类颜色仅需1次AD pass；4）解压缩还原为原始稀疏模式，AD pass数仅与稀疏结构相关，与矩阵维度完全解耦。

### 关键结果
提供asdex.jacobian、asdex.hessian两个接口，可无修改直接替换JAX原生对应稠密计算接口；针对带状雅克比场景，仅需与带宽相等的AD pass数，完全不受矩阵大小影响。

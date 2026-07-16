---
title: 'RFMSR: Residual Flow Matching for Image Super-Resolution'
title_zh: RFMSR：面向图像超分辨率的残差流匹配方法
authors:
- Shuwei Huang
- Tianyao Luo
- Jicheng Liu
- Daizong Liu
- Pan Zhou
affiliations:
- Huazhong University of Science and Technology
- Wuhan University
arxiv_id: '2607.12753'
url: https://arxiv.org/abs/2607.12753
pdf_url: https://arxiv.org/pdf/2607.12753
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 多模态生成 · 图像超分辨率优化
tags:
- Flow Matching
- Image Super-Resolution
- Generative Model
- Two-phase Training
- Residual Learning
one_liner: 提出以低清隐变量为源分布的残差流匹配超分框架，兼顾单步推理速度与多步优化能力
practical_value: '- 电商商品低清主图/短视频封面修复场景可复用残差流匹配思路，以低清输入为源分布缩短生成路径，同时提升超分速度与结构保真度

  - 生成类任务可借鉴两阶段训练策略：先预训练速度场，再端到端监督单步输出同时保留全时间步损失，兼顾单步推理效率与多步调优能力

  - 无需依赖大参数量T2I预训练模型，纯视觉小模型即可达到SOTA超分效果，适合端侧/低算力场景的图像质量优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有流匹配超分方案从纯高斯分布出发做分布迁移，丢失低清输入的固有结构信息；单步加速技术会牺牲多步推理能力，基于T2I大模型的超分方案参数量大、训练成本过高，难以落地。
### 方法关键点
1. 提出纯视觉超分框架RFMSR，将流匹配的源分布锚定在低清输入的隐空间，大幅缩短分布迁移距离，全程保留低清图的结构先验
2. 设计两阶段训练策略：阶段一通过条件流匹配预训练速度场；阶段二对单步预测做端到端监督，同时保留全时间步的速度损失，无需牺牲多步细化能力即可实现高质量单步生成
### 关键结果
在公开超分基准数据集上，感知质量优于或持平现有SOTA方法，代码已开源。

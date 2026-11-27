---
title: Transferring Architecture as an Optimization Prior
title_zh: 将架构作为优化先验进行迁移
authors:
- Vighnesh Subramaniam
- Boris Katz
- Brian Cheung
affiliations:
- MIT CSAIL
- UCSF
arxiv_id: '2611.34816'
url: https://arxiv.org/abs/2611.34816
pdf_url: https://arxiv.org/pdf/2611.34816
published: '2026-11-25'
collected: '2026-11-27'
category: Training
direction: 模型训练 · 跨架构优化先验迁移
tags:
- Initialization
- Optimization Prior
- Cross-Architecture Transfer
- Representation Geometry
- Model Training
one_liner: 通过跨架构初始化对齐表征几何，无标签无特征迁移即可提升目标网络性能
practical_value: '- 浅召回/排序模型训练前，可对齐预训练深guide网络的表征几何，在不增加线上推理成本的前提下提升浅模型效果

  - 粗粒度用户/物品表征模型，可通过对齐细粒度guide网络的初始化几何，提升表征分辨能力，无需额外标注数据

  - LLM小模型蒸馏时可引入该初始化对齐方法，减少蒸馏阶段的训练步数，降低训练成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统初始化仅关注参数尺度稳定性，忽略了初始表征几何带来的优化先验会直接决定模型训练的收敛方向与效果，而架构属性（深度、分辨率）直接决定该先验，此前无法跨架构迁移。

### 方法关键点
1. 提出无监督初始化对齐流程，在下游训练前将目标网络的表征几何与随机初始化的引导网络对齐，过程不迁移已学习特征、不使用标签、引导网络不参与梯度更新。
2. 支持两类跨架构迁移：将深层网络的深度优化优势迁移给浅层网络；将细分辨率网络的表征粒度优势迁移给粗粒度网络。

### 关键结果
两类迁移场景下，目标网络的下游任务性能均获得稳定提升，证明模型架构属性可与物理结构解耦，通过初始化显式修改。

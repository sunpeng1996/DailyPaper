---
title: 'BrickFlow: Connectivity-Guided Brick Reconstruction'
title_zh: BrickFlow：连接性引导的乐高积木装配重建方法
authors:
- Peter Kulits
- Cordelia Schmid
affiliations:
- Inria, École Normale Supérieure, CNRS, PSL Research University
- Max Planck Institute for Intelligent Systems, Tübingen
arxiv_id: '2611.17321'
url: https://arxiv.org/abs/2611.17321
pdf_url: https://arxiv.org/pdf/2611.17321
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 三维重建 · 零件装配姿态推断
tags:
- 3D Reconstruction
- Flow Matching
- Pose Estimation
- Test-time Guidance
- Generative Prior
one_liner: 提出融合SE(3)流模型与测试时连接性场引导的乐高零件姿态推断框架，仅用1%数据即可完成图像条件微调
practical_value: '- 强约束生成任务可复用「大规模合成数据预训练通用先验 + 1%量级业务数据微调适配」的范式，大幅降低标注成本

  - 推理阶段叠加轻量解析规则场引导的思路，可解决生成/预测结果不满足业务硬约束的问题，无需重新训练模型

  - 对组合优化类业务（如电商套装搭配、DIY商品装配导购），可通过学习组件拼接先验+约束引导的方式降低组合搜索空间'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统3D重建未考虑离散物理约束，乐高零件装配属于高组合度优化问题，对姿态误差极敏感，现有SE(3)流模型输出无法保证零件连接合规性。

### 方法关键点
1. 在大规模程序化生成的装配数据集上训练集合条件的SE(3)流匹配模型，学习零件拼接通用先验；
2. 仅用1%规模的标注数据微调模型，注入图像条件，实现从单张成品图到各零件6D姿态的映射；
3. 推理阶段叠加解析连接性场引导，将预测结果向满足连接约束的合规装配方向对齐。

### 关键结果
通过模型扩容、预训练范式、测试时引导三个维度优化，显著提升装配重建质量，相关模型与数据集已开源。

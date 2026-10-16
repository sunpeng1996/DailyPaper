---
title: 'One Size Does Not Fit All: Curvature-Aware Adaptive Perturbation for SAM'
title_zh: 通用参数并非最优：面向SAM的曲率感知自适应扰动方法
authors:
- Alessia Rossi
- Felipe Campelo
- Gabriel L. Oliveira
affiliations:
- School of Engineering Mathematics and Technology, University of Bristol
arxiv_id: '2610.20415'
url: https://arxiv.org/abs/2610.20415
pdf_url: https://arxiv.org/pdf/2610.20415
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: 深度学习训练 · 优化器算法改进
tags:
- SAM
- Optimization
- Generalization
- Sharpness-Aware Minimization
- Training
one_liner: 提出基于曲率动态调整扰动半径的CAP-SAM优化器，在多类数据集上效果优于SAM及主流变体
practical_value: '- 训练搜索/推荐/广告排序大模型时，可替换原有SAM优化器为CAP-SAM，动态调整扰动半径，避免固定ρ导致的收敛差/泛化差问题，提升离线AUC及线上泛化表现

  - 曲率感知的动态超参数调整思路可复用至其他训练优化模块，如学习率调度、正则项强度动态适配，无需手动调参即可适配不同训练阶段的损失曲面特性

  - 电商垂类小样本模型训练场景下，CAP-SAM引导收敛到平坦极小值的特性可有效降低过拟合风险，提升冷启动场景下的模型效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
深度模型泛化性差往往与收敛到尖锐极小值相关，SAM通过同时优化训练损失和损失曲面局部尖锐度引导模型收敛到平坦极小值，但固定扰动半径ρ未适配局部曲率，易出现扰动过小无法跳出尖锐极小值盆地、扰动过大无法收敛到损失-尖锐度权衡最优解的低效问题。
### 方法关键点
提出曲率感知自适应扰动SAM（CAP-SAM），将ρ重定义为扰动信号强度，基于局部尖锐度比例动态调制扰动半径，可在非凸随机训练场景下保持与标准SAM一致的收敛速率，无显著额外计算开销。
### 关键结果
在CIFAR-10、CIFAR-100、ImageNet三类公开数据集上，跨ResNet、ViT等多种主流网络架构，效果均稳定优于标准SAM及当前主流SAM变体，泛化性表现优于同类自适应SAM改进方案。

---
title: 'Ananke: Contractive Torus Attractor Networks'
title_zh: 《Ananke：压缩环面吸引子网络》
authors:
- Zhongping Ji
arxiv_id: '2609.24737'
url: https://arxiv.org/abs/2609.24737
pdf_url: https://arxiv.org/pdf/2609.24737
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 表征学习 · 高维隐空间建模
tags:
- Representation Learning
- Feature Encoding
- Parameter Efficiency
- Dynamical System
- Manifold Learning
one_liner: 提出基于乘积环面先验的表征学习框架Ananke及视觉骨干CTAN，实现极高参数效率的表征建模
practical_value: '- 多模态推荐场景的图像特征编码可参考CTAN架构，用仅0.27M级参数量实现高精度图像表征，大幅降低推理与存储成本

  - 高维用户/物品表征建模可借鉴环面分解思路，将高维隐空间拆分为正交二维相平面，保留语义不变性的同时抑制特征噪声

  - 在线推荐实时特征更新场景可复用ELSF闭式映射方法，无需数值积分仅单次前向传播即可完成特征迭代，提升实时性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有连续深度表征模型存在核心矛盾：保守哈密顿/辛流可保留能量与语义，但缺乏降噪能力；全局压缩流可降噪但易丢失核心语义信息，且多数依赖数值积分推理效率低。
### 方法关键点
1. 提出Ananke表征学习框架，将高维隐空间分解为多个正交二维相平面的直和，采用解耦双相连续流更新特征：斜对称哈密顿传输沿能级切向移动以保留语义相位不变性，带符号梯度耗散横向压缩扰动到目标不变流形。
2. 针对冻结参数的圆形势族设计Exact Log-Symplectic Flow（ELSF）闭式映射，无需数值积分仅单次前向传播即可完成计算，对数半径误差实现指数级衰减。
### 关键结果数字
仅0.27M参数的CTAN在Kvasir-v2数据集上准确率达90.52%，性能优于25M+参数量的ResNet-50、DenseNet-161；缩放版本在CIFAR-100上top-1准确率达80.32%。

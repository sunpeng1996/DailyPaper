---
title: Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport
title_zh: 基于纤维最优传输的模型感知生成调度优化方法
authors:
- Luyi Jia
- Boyan Zhang
- Yilun Liu
- Steffen Rulands
affiliations:
- Arnold-Sommerfeld-Center for Theoretical Physics, LMU Munich
- Institute of Informatics, LMU Munich
- Munich Center for Machine Learning
arxiv_id: '2609.11842'
url: https://arxiv.org/abs/2609.11842
pdf_url: https://arxiv.org/pdf/2609.11842
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 扩散模型 · 训练推理调度优化
tags:
- Diffusion Model
- Flow Matching
- Optimal Transport
- Generation Scheduling
- FID Optimization
- Model Training
one_liner: 提出基于纤维最优传输的模型感知调度，大幅提升扩散、流匹配模型的生成效率与效果
practical_value: '- 电商场景下用扩散生成商品图/营销文案的业务，可直接替换原有模型无关调度，相同推理步数下降低生成误差，提升出图/出文质量

  - 线上低时延推理场景可复用本文冻结解析分配模板，无需额外风险估计或模型定制拟合，即可拿到大部分调度优化收益

  - 扩散类生成式推荐模型训练时，可基于早期checkpoint估计风险剖面，动态调整训练调度，降低训练成本同时提升模型生成效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有扩散、流匹配的信号/噪声系数调度均为模型无关设计，未考虑模型实际预测误差，无法实现生成效率与质量的最优平衡。
### 方法关键点
基于纤维最优传输构建模型感知调度：固定概率路径的时间与状态时，在兼容信号/噪声分解的仿射纤维内，计算真实与预测器诱导分解的最优传输成本均值得到纤维预测风险；结合系数路径动力学动作推导得到闭式最优时间分配，风险剖面可通过早期基线checkpoint估计，支持通用线性预测目标。
### 关键结果
- 流匹配在CIFAR-10数据集16次函数评估下，FID相对降低38.6%
- 不同设置下独立训练模型的归一化纤维风险剖面、训练调度变形高度对齐，具备经验通用性
- 冻结解析分配模板可保留大部分调度优化收益，无需额外风险估计或模型定制拟合

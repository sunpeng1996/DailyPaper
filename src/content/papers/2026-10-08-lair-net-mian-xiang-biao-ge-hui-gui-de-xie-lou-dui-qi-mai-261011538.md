---
title: 'LAIR-Net: Leaky Alignment-Impulse Residual Networks for Tabular Regression'
title_zh: LAIR-Net：面向表格回归的泄漏对齐脉冲残差网络
authors:
- Rahul Goswami
- Aryan Bhambu
- Bittu Karmakar
affiliations:
- Indian Institute of Technology Guwahati
- SAFIR, Sorbonne University Abu Dhabi
- Indian Institute of Technology Bombay
arxiv_id: '2610.11538'
url: https://arxiv.org/abs/2610.11538
pdf_url: https://arxiv.org/pdf/2610.11538
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 表格回归 · 轻量随机神经网络优化
tags:
- Tabular Regression
- Randomized Neural Network
- Residual Connection
- Lightweight Model
- Nonlinear Fitting
one_liner: 提出融合浅层学习锚点的泄漏残差随机网络，在23个表格回归数据集上性能优于20种基线模型
practical_value: '- 电商/推荐场景下的表格回归任务（如CTR校准、用户价值预测、库存预估）可直接复用LAIR-Net作为轻量基线，仅优化读出头训练成本远低于端到端DNN

  - 浅层有监督锚点+泄漏残差融合的trick可直接迁移到现有RVFL类随机网络优化，无需改动训练pipeline即可提升非线性目标拟合效果

  - 可根据业务数据特性选择适配场景：目标非线性强、噪声可控的场景收益显著，接近线性目标或高噪声场景无需替换现有方案'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
深度随机神经网络仅优化输出层、隐藏层参数随机固定，堆叠深度时无目标感知的隐状态调控机制，输入扰动敏感性不可控，表格回归场景泛化性不稳定。
### 方法关键点
1. 引入浅层有监督学习的对齐锚点，每层通过泄漏残差转移将当前隐状态与锚点混合，实现目标感知的隐状态演化控制
2. 推导输入扰动敏感性的深度一致界，证明架构稳定性不会随深度增加明显劣化
### 关键结果
在23个公开表格回归基准数据集上，LAIR-Net在8种随机网络、12种传统模型中平均排名第一；收益完全来自锚点设计而非额外参数量，非线性目标强、噪声可控的场景增益明显，接近线性目标或噪声主导场景增益消失。

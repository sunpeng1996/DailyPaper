---
title: Characterizing the Edge of Stability in Variational Training Without Priors
title_zh: 无先验变分训练的稳定边界特性表征
authors:
- Juraj Marusic
- Jonathan Wenger
- Beau Coker
- John P. Cunningham
affiliations:
- Columbia University
arxiv_id: '2611.15990'
url: https://arxiv.org/abs/2611.15990
pdf_url: https://arxiv.org/pdf/2611.15990
published: '2026-11-11'
collected: '2026-11-15'
category: Training
direction: 变分训练优化 · 超参数隐式正则
tags:
- Variational Training
- Implicit Regularization
- Hyperparameter Tuning
- OOD Generalization
- Edge of Stability
one_liner: 从理论与实验层面揭示无先验变分训练中优化超参数对隐式正则化的作用规律
practical_value: '- 训练变分结构的推荐/排序模型时，可省略先验正则项，通过调大学习率、减少参数采样数获取更平缓损失极小值，提升OOD泛化能力

  - 无先验变分训练调参时，可参考梯度估计信噪比、蒙特卡洛采样数判断是否处于最优稳定边界，大幅降低调参成本

  - 跨域推荐、冷启动推荐等OOD场景的模型训练，可引入该无先验变分训练范式提升模型鲁棒性'
score: 5
source: arxiv-stat.ML
depth: abstract
---

### 动机
变分深度学习通过推断权重分布提升不确定性量化与OOD泛化能力，但需依赖与人工预设先验的 divergence 做正则，先验选取难度极高，工业界普遍弱化甚至移除该显式正则项，仅依靠优化器的隐式正则训练，但其核心优化超参数的作用机制缺乏理论支撑，调参无据可依。
### 方法关键点
推导无先验变分训练的修正稳定边界，证明边界由梯度估计信噪比、蒙特卡洛采样数两个核心指标共同决定；系统分析学习率、参数采样数对损失曲面平坦度的影响规律。
### 关键结果
更大的学习率与更少的参数采样数可得到泛化性更优的平缓损失极小值，OOD基准数据集实验充分验证了理论结论的实用价值

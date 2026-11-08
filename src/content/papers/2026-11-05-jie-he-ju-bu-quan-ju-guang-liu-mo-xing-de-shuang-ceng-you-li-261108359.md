---
title: A Theoretical Analysis of a Bilevel Optimization Formulation for Combined Local-Global
  Optical Flow Models
title_zh: 结合局部-全局光流模型的双层优化公式理论分析
authors:
- El Mostafa Kalmoun
affiliations:
- Al Akhawayn University in Ifrane
arxiv_id: '2611.08359'
url: https://arxiv.org/abs/2611.08359
pdf_url: https://arxiv.org/pdf/2611.08359
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 双层优化理论分析 · 光流模型参数学习
tags:
- Bilevel Optimization
- Optical Flow
- Regularization Learning
- Total Variation
one_liner: 推导CLG光流模型双层正则参数学习的存在性、正定性与局部最优充分条件
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
光流变分估计的正则权重α对结果质量影响极强，α过小会导致流场噪声大，α过大会过度平滑运动边界，现有基于双层优化的自动调参方案缺乏完备理论支撑。

### 方法关键点
采用有限维设定+满秩假设保证下层CLG光流求解唯一；下层任务基于Lucas-Kanade数据项搭配二次/TV正则器计算光流，上层任务通过最小化与真值流的平方距离优化正则参数α。

### 关键结果
对二次正则模型推导了最优参数存在性、全最优参数正定、严格局部最优三类充分条件；对TV正则模型证明最优参数恒存在，同时给出考虑局部结构张量耦合效应的参数正定性充分条件；合成实验完整覆盖了条件成立及失效的不同场景。

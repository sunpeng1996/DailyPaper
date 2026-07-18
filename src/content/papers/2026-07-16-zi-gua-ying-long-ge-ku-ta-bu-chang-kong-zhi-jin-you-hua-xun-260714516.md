---
title: 'Adaptive Runge-Kutta Step Control Buys Training Loss, Not Generalization:
  An Honest Compute-Matched Study of RK-Adam Optimizers'
title_zh: 自适应龙格-库塔步长控制仅优化训练损失不提升泛化：RK-Adam等算力对比研究
authors:
- Akhilesh Gogikar
affiliations:
- Independent Researcher
arxiv_id: '2607.14516'
url: https://arxiv.org/abs/2607.14516
pdf_url: https://arxiv.org/pdf/2607.14516
published: '2026-07-16'
collected: '2026-07-18'
category: Training
direction: 优化器训练 · 高阶/一阶优化器性能对比
tags:
- Optimizer
- Runge-Kutta
- Adam
- Generalization
- Training Efficiency
one_liner: 严格等算力下验证自适应RK-Adam泛化弱于调优一阶优化器，仅梯度平均有微弱正则效果
practical_value: '- 业务场景下不要盲目尝试高阶RK系优化器，等算力下其泛化表现不如调优的Adam/NAdam/RMSprop等一阶优化器，无落地价值

  - 可复用梯度平均的正则效果：在现有训练流程中低成本加入多步梯度平均，可在不显著增加算力的前提下提升模型泛化性

  - 训练优化器选型优先调优成熟一阶基线，不要为追求高阶优化的理论收益浪费算力，优先保障业务迭代性价比'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
此前研究将优化器视为梯度流离散化，催生高阶Runge-Kutta（RK）整合器应用于神经网络优化，但相关研究普遍缺少严格等算力对比，结论可信度不足。
### 方法关键点
基于Bogacki-Shampine 3(2) RK对、FSAL复用、局部误差步长控制构建RK-Adam变体，严格控制所有对比方法的梯度评估预算一致，对比不同优化器的训练损失、泛化表现。
### 关键结果
1. 原始RK-Adam表现弱于普通Adam，98%~100%步长锁死增长上限，等价于成本提升3~4倍的固定步长Adam；
2. 修复后RK-Adam全batch训练损失比调优Adam低40倍，但泛化性反而低1.3~3.4个百分点；
3. 梯度平均的正则效果优于同学习率的Adam/AdamW，但NAdam/RMSprop仅用1/3算力成本即可达到同等甚至更优效果。

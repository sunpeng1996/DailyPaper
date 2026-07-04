---
title: 'Generalization in offline RL: The structure is more important than the amount
  of pessimism'
title_zh: 离线强化学习的泛化性：悲观约束的结构比程度更重要
authors:
- Max Weltevrede
- Matthijs T. J. Spaan
- Wendelin Böhmer
affiliations:
- Delft University of Technology
arxiv_id: '2607.02288'
url: https://arxiv.org/abs/2607.02288
pdf_url: https://arxiv.org/pdf/2607.02288
published: '2026-07-02'
collected: '2026-07-04'
category: Training
direction: 离线强化学习 · 泛化性训练优化
tags:
- Offline RL
- Generalization
- Pessimism Constraint
- Data Augmentation
- Consistency Loss
one_liner: 证明离线RL泛化性取决于悲观约束结构而非程度，提出策略提取阶段加一致性损失的DA方案
practical_value: '- 做基于离线RL的推荐排序/广告出价策略优化时，不要盲目降低悲观约束程度，优先对齐最优解的对称结构（比如用户行为周期性、同档位商品等价性）设计悲观正则，可获得更好的跨场景泛化性

  - 离线RL训练的数据增强不要直接做全量数据集扩增，改为在策略提取阶段加一致性损失约束，能降低数据分布偏移带来的性能衰减，适配电商样本分布不均衡的场景

  - 落地时可先挖掘业务固有对称性（如同兴趣用户决策相似性、同属性商品价值等价性），再设计对应对称价值函数约束，ROI远高于盲目调优悲观系数'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离线RL普遍引入悲观约束缓解高估偏差，过往研究默认过度悲观会损害泛化性，多围绕降低悲观程度做优化，缺乏底层理论支撑。
### 方法关键点
1. 理论证明上下文MDP中，泛化性核心取决于悲观约束结构是否匹配最优解的底层对称性，而非悲观程度：轻度悲观但非对称的价值函数，泛化表现反而弱于过度悲观但对称的价值函数；
2. 离线RL的悲观结构由数据集覆盖结构决定，无需在训练阶段直接使用扩增数据集，改为在策略提取阶段引入一致性损失实现数据增强，即可高效对齐对称约束。
### 关键结果
在具备旋转对称性的reacher环境中，对IQL、CQL两种主流离线RL算法的验证显示，所提数据增强方案泛化效果显著优于常规扩增数据集训练方案。

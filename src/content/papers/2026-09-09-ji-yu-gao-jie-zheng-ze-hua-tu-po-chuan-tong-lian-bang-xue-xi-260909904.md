---
title: Beyond Conventional Federated Learning via High-Order Regularization
title_zh: 基于高阶正则化突破传统联邦学习的性能瓶颈
authors:
- Alireza Kabgani
- Masoud Ahookhosh
affiliations:
- University of Antwerp
arxiv_id: '2609.09904'
url: https://arxiv.org/abs/2609.09904
pdf_url: https://arxiv.org/pdf/2609.09904
published: '2026-09-09'
collected: '2026-09-11'
category: Training
direction: 联邦学习 · 训练正则策略优化
tags:
- Federated Learning
- Regularization
- HiFedProx
- Distributed Training
- Optimization
one_liner: 提出采用p≥2幂次正则的HiFedProx联邦学习算法，压力场景较FedProx损失最高降23.16%
practical_value: '- 跨端联邦推荐训练场景（隐私合规需求下的用户端模型训练），可直接将FedProx的二次正则替换为p=5~7的幂次正则，压力场景下可降低10%+的训练损失

  - 同minibatch Armijo回溯技巧可复用到联邦训练的本地优化步骤，有效降低客户端梯度偏移带来的全局模型波动

  - 联邦训练中客户端参数位移差异大的场景，无需最大化正则指数压缩位移，选择中间区间指数即可平衡效果和计算成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
联邦学习客户端多步本地优化后返回的参数位移差异极大，FedProx的二次正则对超大位移约束能力不足，无法有效管控普通与异常客户端更新的差异。
### 方法关键点
1. 提出HiFedProx，将FedProx的二次惩罚替换为p≥2的尺度匹配幂次正则：参考位移R处所有幂次的正则梯度量级一致，p>2时R以下正则响应更弱、R以上响应更强，可压缩位移差异
2. 结合有限预算随机客户端优化、同minibatch Armijo回溯策略降低训练成本
### 关键结果
FEMNIST 60用户子集实验显示：干净场景下与p=2的FedProx效果相当；中等压力下p=7时损失较FedProx降低11.44%，重度压力下p=6时损失降低23.16%；最优正则指数区间为p=5~7，无需取极大值。

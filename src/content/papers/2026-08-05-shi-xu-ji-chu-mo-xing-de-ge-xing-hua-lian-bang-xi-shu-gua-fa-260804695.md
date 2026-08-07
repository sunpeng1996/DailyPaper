---
title: Personalized Federated Sparse Adaptation of Time-Series Foundation Models
title_zh: 时序基础模型的个性化联邦稀疏适配方法
authors:
- Priyanka Nihalchandani
- Naman Srivastava
- Varun Ojha
- Pandarasamy Arjunan
affiliations:
- Robert Bosch Centre for Cyber-Physical Systems, Indian Institute of Science
- School of Computing, Newcastle University
arxiv_id: '2608.04695'
url: https://arxiv.org/abs/2608.04695
pdf_url: https://arxiv.org/pdf/2608.04695
published: '2026-08-05'
collected: '2026-08-07'
category: Training
direction: 时序基础模型 · 联邦个性化适配
tags:
- Federated Learning
- MoE
- Time-Series Foundation Model
- Adapter
- Personalization
one_liner: 提出带异质时序MoE适配器的个性化联邦稀疏适配框架，提升非IID场景下时序基础模型联邦适配性能
practical_value: '- 电商非IID时序预测场景（如用户消费时序、商家销量预测）可复用异质时序MoE适配器结构，用序列级路由适配不同主体的时序特征，兼顾全局迁移和个性化

  - 联邦学习场景下可参考「全局共享+客户端私有专家混合」的参数共享策略，相比全共享/全本地方案平衡效果和通信开销

  - 大模型下游适配时可针对不同backbone选择最优稀疏适配策略，无需强制统一方案，可同时提升效果并降低计算量'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
时序基础模型（TSFM）联邦适配是建筑能耗预测等隐私敏感时序任务的主流方案，但现有全共享适配器会抑制客户端个性化时序特征，全本地适配无法利用跨客户端迁移信息，且单一参数共享策略无法适配所有预训练TSFM backbone。

### 方法关键点
在预训练TSFM输出层后插入异质时序MoE适配器，用序列级路由器将168小时时序窗口映射到对应周期性、长程交互、局部波动、趋势残差、多分辨率特征的top-k专用专家子集，支持全局共享/客户端私有两种专家库的个性化联邦学习变体。

### 关键结果
在50个建筑数据集、3种TSFM backbone（MOMENT/Chronos-2/Moirai）上，最优个性化稀疏适配策略相比全局FL-MoE分别降低NRMSE 8.2%/7.1%/12.5%，同时通过选择性参数共享降低通信开销，且最优策略随backbone和评价指标动态变化。

---
title: 'FedTaste: Topology-Aware Structural Transfer for Multimodal Federated Learning
  with Missing Modalities'
title_zh: FedTaste：面向模态缺失多模态联邦学习的拓扑感知结构迁移框架
authors:
- Haochen Liang
- Jie Zhang
- Hideya Ochiai
affiliations:
- The University of Tokyo
- Great Bay University
arxiv_id: '2607.23245'
url: https://arxiv.org/abs/2607.23245
pdf_url: https://arxiv.org/pdf/2607.23245
published: '2026-07-25'
collected: '2026-08-01'
category: Training
direction: 多模态联邦学习 · 缺失模态适配
tags:
- Multimodal-Federated-Learning
- Missing-Modality
- Structural-Transfer
- Semantic-Topology
- Parameter-Efficient
one_liner: 提出参数高效的FedTaste框架，解决多模态联邦学习模态缺失与Non-IID场景下的表征漂移问题
practical_value: '- 跨端多模态推荐场景（如不同用户端仅采集图文/视频单一模态）可复用拓扑级语义对齐思路，规避显式模态补全的隐私与计算成本

  - 模态缺失场景下放弃一阶特征对齐、转用组级语义关系对齐的trick，可直接迁移至多模态召回/粗排的端侧联合训练

  - 模态自适应结构Prompt+谱一致性正则的轻量适配方案，可大幅降低跨端联邦训练通信开销，适合端侧多模态RecSys落地'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态联邦学习（MFL）普遍存在任意模态缺失、数据Non-IID分布问题，易引发严重表征漂移，现有方案依赖生成式补全、外部辅助数据等，存在通信计算成本高、隐私泄露风险。
### 方法关键点
1. 放弃易受扰动的一阶特征对齐，聚焦更稳定的组级语义关系；
2. 基于冻结基础模型从全模态客户端提取联合多模态拓扑，由服务端聚合生成全局结构蓝图；
3. 设计模态自适应结构Prompt+谱一致性正则，实现缺模态客户端局部分表征与全局蓝图的轻量对齐，无需显式模态补全。
### 关键结果
在多数据集、复杂Non-IID设置下性能始终优于现有SOTA，通信开销相比现有方法大幅降低。

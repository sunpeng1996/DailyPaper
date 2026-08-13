---
title: 'Beyond Parameter Space: NTK-Guided Personalized Aggregation for Robust Federated
  Learning'
title_zh: 超越参数空间：面向鲁棒联邦学习的NTK引导个性化聚合
authors:
- Mirko Konstantin
- Stefan Zachow
- Anirban Mukhopadhyay
affiliations:
- Zuse Institute Berlin (ZIB)
- Technical University of Darmstadt
arxiv_id: '2608.12108'
url: https://arxiv.org/abs/2608.12108
pdf_url: https://arxiv.org/pdf/2608.12108
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 联邦学习·鲁棒个性化聚合训练
tags:
- Federated Learning
- Neural Tangent Kernel
- Personalized Aggregation
- Non-IID
- P2P
one_liner: 提出基于NTK函数空间匹配的P2P联邦学习框架LIGHTYEAR，解决非IID场景下聚合劣化问题
practical_value: '- 电商跨地域/商家联邦训练推荐模型时，可借鉴NTK函数空间相似性替代参数相似性做更新筛选，避免非IID数据下聚合劣化

  - 跨端隐私合规要求高的推荐场景，可复用P2P拓扑+本地验证集评估更新有效性的方案，无需上传数据到中心节点

  - 多业务线联合训练推荐/广告模型时，可直接套用个性化聚合规则，每个业务仅选取对自身效果有增益的其他业务更新'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
联邦学习（FL）跨分布式客户端协同训练时，现有基于参数空间的更新相似性判定方法，在非IID异构数据场景下无法准确反映模型预测行为的一致性，容易聚合异质数据/故障客户端产生的有害更新，导致本地模型效果劣化；且传统中心化FL架构无法在聚合前获取函数空间信息做筛选。
### 方法关键点
1. 提出LIGHTYEAR联邦学习框架，基于NTK构造一致性分数，在函数空间衡量更新对本地目标域的适配性，为每个客户端生成个性化聚合子集
2. 采用P2P拓扑，客户端直接交换更新，用本地私有验证集评估传入模型效果，规避中心化架构的信息限制
3. 搭配正则化聚合规则，进一步提升异质性场景下的训练稳定性
### 关键结果
在5个数据集、9个基线方法上，LIGHTYEAR效果始终优于中心化FL基线和现有P2P FL方法

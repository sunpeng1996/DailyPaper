---
title: 'FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space'
title_zh: FlatLand：基于定制洛伦兹空间的个性化图联邦学习
authors:
- Jiahong Liu
- Ram Samarth B B
- Xinyu Fu
- Menglin Yang
- Weixi Zhang
- Rex Ying
- Irwin King
affiliations:
- The Chinese University of Hong Kong
- Yale University
- Huawei Technologies Co., Ltd.
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2608.21096'
url: https://arxiv.org/abs/2608.21096
pdf_url: https://arxiv.org/pdf/2608.21096
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 联邦学习 · 图异构客户端训练优化
tags:
- Federated Learning
- Graph Learning
- Hyperbolic Geometry
- Personalized Training
- Privacy Preserving
one_liner: 利用双曲洛伦兹空间时空维度参数解耦，实现异构客户端高性能个性化图联邦学习
practical_value: '- 多端隐私合规的推荐场景可复用时空参数解耦策略，不用预估客户端相似度即可直接聚合跨端公共特征，降低额外计算开销

  - 存在用户/商品图异质性的低维嵌入场景，可尝试引入双曲洛伦兹空间适配图的负曲率特性，提升嵌入表征精度

  - 跨区域/跨商家的联邦协同训练场景，可借鉴用洛伦兹时间维度编码客户端异构属性的思路，减少异质性对聚合效果的干扰'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有个性化联邦学习（PFL）方法未考虑异构客户端图结构的内在几何属性，跨端数据异质性高导致聚合效果差，且多数需要额外的客户端相似度计算模块，落地成本高。
### 方法关键点
1. 提出FlatLand框架，将不同客户端数据嵌入定制化双曲洛伦兹空间，利用双曲几何天然适配真实世界图普遍存在的负曲率特性
2. 采用参数解耦策略，将客户端异构信息编码在时间类参数中，跨端公共知识保存在空间类参数中，无需客户端相似度预估即可直接完成参数聚合，无额外计算模块
### 关键结果
在多类联邦图学习任务上性能显著优于现有基线方法，低维嵌入设置下优势尤为突出。

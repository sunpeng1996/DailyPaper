---
title: Understanding the Robustness of Distributed Self-Supervised Learning Frameworks
  Against Non-IID Data
title_zh: 分布式自监督学习框架对非独立同分布数据的鲁棒性分析
authors:
- Xuanyu Chen
- Nan Yang
- Shuai Wang
- Dong Yuan
affiliations:
- The University of Sydney
- Northwestern Polytechnical University
arxiv_id: '2607.02447'
url: https://arxiv.org/abs/2607.02447
pdf_url: https://arxiv.org/pdf/2607.02447
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 分布式自监督 · 非IID场景训练优化
tags:
- Distributed-SSL
- Non-IID
- MIM
- Contrastive-Learning
- Federated-Learning
one_liner: 从理论层面分析分布式自监督框架的非IID鲁棒性差异，提出MAR损失优化MIM预训练效果
practical_value: '- 跨域/联邦推荐场景做分布式用户/物品表征自监督预训练时，优先选MIM范式，比CL更适配Non-IID数据分布

  - 联邦学习场景部署分布式SSL任务时，优先采用高连通性组网架构，鲁棒性高于纯去中心化部署

  - 分布式MIM预训练时可直接复用MAR loss，加入局部-全局对齐正则降低Non-IID带来的表征偏移'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
分布式自监督学习（D-SSL）可高效利用海量去中心化无标注数据，但当前缺乏不同D-SSL框架对Non-IID数据鲁棒性的理论支撑，无法指导实际场景的框架选型与优化。
### 方法关键点
对不同SSL范式（MIM/CL）、不同分布式架构（联邦学习FL/去中心化学习DecL）的Non-IID鲁棒性开展严格理论推导；基于分析结论提出MAR loss，在MIM预训练目标中加入局部-全局对齐正则项。
### 关键结果
- 理论+多场景实验验证MIM预训练对异构数据的鲁棒性天生优于CL
- 分布式SSL鲁棒性随平均网络连通性提升而上升，FL鲁棒性不低于DecL
- MAR loss在多种模型架构、分布式设置下均可稳定提升MIM的Non-IID场景表现

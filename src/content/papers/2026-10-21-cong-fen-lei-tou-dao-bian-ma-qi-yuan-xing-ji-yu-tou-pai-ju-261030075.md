---
title: 'From Classifier Heads to Encoder Prototypes: Personalized Federated Learning
  with Head-Derived Clustering'
title_zh: 从分类头到编码器原型：基于头派生聚类的个性化联邦学习
authors:
- Amirardalan Dehghanpour
- Arian Noori
- Ehsan Tanghatari
- Naimeh Omidvar
- Hamid R. Rabiee
affiliations:
- Sharif University of Technology
- Tehran Institute for Advanced Studies (TeIAS)
arxiv_id: '2610.30075'
url: https://arxiv.org/abs/2610.30075
pdf_url: https://arxiv.org/pdf/2610.30075
published: '2026-10-21'
collected: '2026-10-23'
category: Training
direction: 联邦学习 · 个性化训练优化
tags:
- Federated Learning
- Personalized Training
- Clustering
- Long-tail Optimization
- Encoder Prototype
one_liner: 提出HDC-FL个性化联邦学习方法，基于客户端分类头聚类生成编码器原型，优化长尾客户端效果
practical_value: '- 跨端隐私推荐、多商家联邦训练场景，可复用分类头聚类的思路做客户端分群，无需上传原始用户/商家特征，在保护隐私的前提下提升个性化效果

  - 长尾商家、冷启动用户的联邦训练优化，可参考编码器原型软混合策略，在不改动客户端侧分类头的前提下提升弱侧效果

  - 联邦训练工程实现可复用该方法的周期刷新逻辑，无需新增本地优化目标或后微调步骤，降低落地复杂度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
个性化联邦学习需解决非IID数据下客户端表征共享的匹配问题，现有方案多需新增优化目标、后微调流程，还存在客户端分类头信息泄露风险。

### 方法关键点
HDC-FL复用共享编码器训练天然产出的客户端分类头信号，定期将服务端缓存的分类头投影到归一化低秩描述空间聚类，每簇基于缓存的客户端编码器生成1个原型，向各客户端返回匹配原型的软混合结果；客户端保留自有分类头不共享、不平均，不改动原有共享编码器训练轨迹，无额外优化步骤或后微调要求。

### 关键结果数字
覆盖标签子集、Dirichlet、旋转异构的11组CIFAR-10/100实验中，宏平均精度与SOTA个性化/聚类基线持平，最差客户端、后20%客户端的宏平均精度为所有参评方法最高，协变量偏移场景下头相似度与编码器兼容性的正相关性最显著。

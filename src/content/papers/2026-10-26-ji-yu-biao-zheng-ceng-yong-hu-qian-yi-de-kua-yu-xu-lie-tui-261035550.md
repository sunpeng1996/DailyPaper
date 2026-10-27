---
title: Cross-Domain Sequential Recommendation with Representation-Level User Transfer
title_zh: 基于表征层用户迁移的跨域序列推荐框架FLADRec
authors:
- Abdulaziz Samra
- Nikita Sukhorukov
- Alexey Grishanov
- Alexey Vasilev
- Evgeny Frolov
affiliations:
- Skolkovo Institute of Science and Technology
- Higher School of Economics
- Sber AI Lab
arxiv_id: '2610.35550'
url: https://arxiv.org/abs/2610.35550
pdf_url: https://arxiv.org/pdf/2610.35550
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 跨域序列推荐 · 表征迁移与联邦学习
tags:
- Cross-Domain-RecSys
- Sequential-Recommendation
- Federated-Learning
- User-Representation
- SASRec
one_liner: 仅通过用户表征迁移实现合规跨域序列推荐，同时提升共享与非共享用户性能
practical_value: '- 跨域数据隔离场景下可直接复用表征迁移方案，仅交换用户embedding和梯度，无需泄露原始交互数据/物品ID，适配同集团多业务线的合规需求

  - 可复用轻量融合层设计：源域用户表征经LayerNorm+MLP投影后逐元素加至目标域item embedding序列，无额外算力开销，兼容SASRec/BERT4Rec等任意主流序列推荐backbone

  - 无需为非跨域用户单独维护模型，联合训练带来的隐式正则化效应可直接提升仅目标域用户的推荐效果，非共享用户NDCG@10相对提升可达25.8%

  - 训练效率比LoRA类跨域方案高3.68~11.57倍，适配百万级用户/物品的工业级规模部署，无需改动现有单域序列推荐架构'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有跨域序列推荐方案普遍要求共享原始交互数据、对齐物品空间，无法满足业务中跨业务线数据隔离的合规要求，且大多仅支持高重叠率的跨域用户，无法覆盖仅在目标域活跃的用户，甚至存在负迁移风险。

### 方法关键点
- 提出FLADRec框架，仅通过源域用户表征实现知识迁移，源/目标域的原始交互数据、物品 embedding 完全隔离，符合垂直联邦学习约束
- 轻量化融合层设计：源域用户表征经 LayerNorm + MLP 投影到目标域空间后，逐元素加至每个目标域 item embedding，作为全局上下文输入目标编码器
- 无跨域数据的用户自动跳过融合步骤，退化为标准单域序列推荐；联合训练的隐式正则化效应仍能提升这部分用户的模型泛化性
- 采用垂直联邦训练协议，仅在域间交换用户表征和对应梯度，双向更新源域编码器和目标域模型参数

### 关键实验
在3组Amazon公开跨域数据集、TenRec、Zvuk&MegaMarket工业数据集上验证，对比SASRec、BERT4Rec、FedDCSR、ABXI等基线：公开数据集上所有域全指标领先；工业数据集上相对SASRec，NDCG@10提升7.4%~24.1%，HR@50最高提升20.4%，训练速度比ABXI快3.68~11.57倍；非共享用户NDCG@10相对提升仍可达25.8%。

### 核心结论
跨域推荐无需共享原始数据，仅通过对齐的用户表征迁移即可同时为共享和非共享用户带来稳定增益，且训练成本远低于参数迁移类方案

---
title: Discovering Topics from Linear Autoencoders
title_zh: 从线性自编码器中挖掘用户-物品交互的隐含主题
authors:
- Jutiyakhun Srisoparp
- Donlapark Ponnoprat
affiliations:
- Chiang Mai University
arxiv_id: '2610.34739'
url: https://arxiv.org/abs/2610.34739
pdf_url: https://arxiv.org/pdf/2610.34739
published: '2026-10-26'
collected: '2026-10-28'
category: RecSys
direction: 线性推荐模型 · 可解释性主题挖掘
tags:
- linear-autoencoder
- EASE
- topic-model
- recommender-system
- normalization
one_liner: 提出无需额外训练的TEA线性自编码器，同时实现优效推荐与高质量主题挖掘
practical_value: '- 可直接复用TEA的无超参用户归一化方案，降低高活跃用户对共现矩阵的干扰，无需额外调参即可提升推荐结果稳定性与主题合理性

  - 已上线EASE类线性推荐的业务场景，可直接复用本文主题抽取pipeline，无需额外训练主题模型就能生成可解释的物品聚类，支撑推荐理由生成、品类运营等需求

  - 做冷启动/小众物品推荐时，可结合TEA输出的主题相关性做召回补充，同时规避热门物品对主题分布的过度主导

  - 主题质量评估指标TQ（多样性×一致性）可直接复用在业务的物品聚类、用户兴趣标签挖掘的离线评估流程中'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
线性推荐与主题模型均基于用户-物品共现信号建模，但两类模型的关联研究较少，现有将主题融入推荐的方案普遍需要额外训练主题模型、依赖物品文本数据，无法直接从已训好的线性推荐权重中挖掘可解释主题，同时热门物品、高活跃用户的存在会严重干扰主题的合理性。
### 方法关键点
- 理论证明在加权隐因子模型（wLFM）假设下，闭式线性自编码器的权重矩阵可直接恢复隐含主题，无需额外训练
- 提出TEA架构：物品侧按流行度做指数归一化，削弱热门物品对共现矩阵的主导；用户侧提出无超参归一化方案，降低高活用户带来的共现矩阵方差
- 主题抽取pipeline：取TEA权重矩阵的前K大特征向量，通过ppSPA算法得到物品主题分布，每类主题归一化为物品的概率分布
### 关键结果
在6个公开数据集（amazon-books、amazon-cds、gowalla、ml-1m、online-retail-ii、steam）上对比17个基线模型：
1. 主题质量（TQ）显著优于所有专用主题模型，平均提升超30%；在amazon-cds、steam数据集上比EASE的TQ分别高73%、123%
2. 推荐效果与最优调参的线性推荐器持平，NDCG@10最多比最优基线低0.004，Recall@10差距稳定在0.01以内
### 核心结论
已训练完成的线性自编码器本身隐含高质量的物品主题信息，无需额外引入文本数据或训练新模型即可挖掘，可同时兼顾推荐效果与结果可解释性

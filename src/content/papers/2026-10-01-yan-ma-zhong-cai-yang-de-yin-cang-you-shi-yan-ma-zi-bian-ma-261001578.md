---
title: 'The hidden advantage of mask resampling: a theory of masked autoencoders'
title_zh: 《掩码重采样的隐藏优势：掩码自编码器理论研究》
authors:
- Jorge Medina Moreira
- Lorenzo Bardone
- Lenka Zdeborová
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL)
- Statistical Physics of Computation Laboratory
arxiv_id: '2610.01578'
url: https://arxiv.org/abs/2610.01578
pdf_url: https://arxiv.org/pdf/2610.01578
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 预训练优化 · 掩码自编码器训练策略
tags:
- MAE
- Masked Pretraining
- Mask Resampling
- Representation Learning
- Training Strategy
one_liner: 从理论层面证明MAE掩码重采样的统计优势，拆分掩码预测目标与掩码多样性的独立收益
practical_value: '- 做用户行为序列、商品文本的掩码预训练（如RecBERT类模型）时，优先采用动态重采样掩码替代固定掩码，可降低样本量需求，提升下游召回/排序效果

  - 多模态商品表征预训练若使用随机裁剪、翻转等强数据增强，无需额外配置动态掩码，二者效果重叠会浪费算力；无强增强时动态掩码收益显著

  - 新垂类小样本预训练场景下，提升掩码多样性可有效降低样本复杂度，减少域内数据收集/标注成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
掩码预训练（MAE、BERT）的掩码重采样机制实际收益缺乏量化理论支撑，标准训练流程中的强数据增强会掩盖其优势，现有研究未拆分掩码预测目标与掩码多样性的独立贡献。
### 方法关键点
基于带共享隐结构、异质噪声的高维MAE模型推导，量化每样本固定K个掩码的策略对特征恢复、下游性能的影响，从理论层面刻画掩码多样性的作用边界。
### 关键结果
- 无掩码重建（等价PCA）失效的场景下，掩码线性重建仅需线性样本复杂度即可恢复隐特征
- 更高掩码多样性可有效降低特征恢复所需的样本复杂度
- 移除图像训练的随机裁剪/翻转增强后，动态掩码相对静态掩码的下游收益可观测，语言任务也验证了掩码多样性的正向作用

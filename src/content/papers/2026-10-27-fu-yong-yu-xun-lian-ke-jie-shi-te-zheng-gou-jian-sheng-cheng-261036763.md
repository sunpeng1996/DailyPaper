---
title: 'The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features
  for Generative Recommendation'
title_zh: 复用预训练可解释特征构建生成式推荐天然语义ID词表
authors:
- Ziluowen Luo
- Ruochen Liu
- Jun Yin
- Hao Yan
- Zhengxuan Hu
- Xinze Shi
- Chaozhuo Li
- Chengqi Zhang
- Senzhang Wang
affiliations:
- 中南大学
- 香港科技大学（广州）
- 香港理工大学
- 伦敦玛丽女王大学
- 微软
arxiv_id: '2610.36763'
url: https://arxiv.org/abs/2610.36763
pdf_url: https://arxiv.org/pdf/2610.36763
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 可解释语义ID复用
tags:
- Generative Recommendation
- Sparse Autoencoder
- Semantic ID
- Interpretability
- Vocabulary Reuse
one_liner: 复用预训练稀疏自编码器特征作为生成式推荐语义ID词表，免额外训练且天然可解释
practical_value: '- 可直接复用开源预训练SAE（如SAELens、Gemma Scope提供的模型）作为生成式推荐的语义ID词表，省去跨域词表拟合的训练成本，跨业务迁移门槛极低

  - PID构造的特征优先级trick可直接复用：用激活强度log值乘以特征领域流行度的逆log值排序，既保留强语义特征又降低通用特征挤占，可压缩ID长度同时减少碰撞

  - 推荐可解释性落地路径可直接参考：将预测得分拆解到每个可解释特征维度，结合SAE自带的语义标注，即可生成用户可理解的推荐理由

  - 多域生成式推荐场景可优先采用该架构：共享预训练SAE词表，仅需适配SPA轻量适配器，无需为每个域单独训练词表，落地效率远高于UTGRec等方案'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的Semantic ID需要在业务数据上单独拟合词表，不仅增加训练成本，跨域适配性差，且生成的ID无天然可解释性，无法直接输出推荐理由。预训练稀疏自编码器（P-SAE）可将PLM激活拆解为人类可解释的语义特征，天然具备作为SID词表的潜力，但直接复用存在短序列SID易丢失相似物品区分度、可解释性无法延伸到排序决策两个核心问题。

### 方法关键点
- 构造PID（预训练可解释ID）：物品文本输入冻结的PLM+P-SAE得到特征激活强度，用「激活强度log值 * 特征流行度逆log值」作为优先级排序，选Top K个特征作为ID序列，同时保留相对激活强度区分相似物品
- 设计SPA（语义预测适配器）：编码用户历史交互的所有候选特征及激活强度，同时预测下一个物品的特征序列和对应激活强度，损失结合特征序列似然、强度匹配度，再加偏好对齐Loss让目标物品得分高于候选集
- 可解释排序机制：将物品得分拆解到每个特征维度，结合SAE自带的语义标注，直接输出各特征对排序结果的贡献值

### 关键实验
在Amazon公开的Beauty、Sports、Toys三个数据集上对比GRU4Rec、Bert4Rec、TIGER、UTGRec等10个基线，API在12个数据集-指标组合中拿到9个最优，Toys数据集全指标第一，比最优基线Recall@5最高提升4.2%；PID构造在K=4的短序列下，把平均碰撞率从80.76%降到17.09%；跨域迁移场景下比RVQ等需要词表拟合的方案时间成本降低99%以上。

**最值得记住的一句话**：生成式推荐不需要单独训练语义ID词表，预训练SAE提供的可解释特征字典就是天然的跨域通用词表，既降本又提升可解释性。

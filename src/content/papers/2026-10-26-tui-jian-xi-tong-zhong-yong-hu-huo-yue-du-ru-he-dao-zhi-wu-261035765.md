---
title: Do Similarity Measures Measure Similarity? How User Activity Creates Phantom
  Correlation in Recommender Systems
title_zh: 推荐系统中用户活跃度如何导致物品相似度的伪相关偏差
authors:
- Marco Favier
- Noah Daniëls
- Jens Leysen
- Sander Marinus
- Bart Goethals
affiliations:
- University of Antwerp
arxiv_id: '2610.35765'
url: https://arxiv.org/abs/2610.35765
pdf_url: https://arxiv.org/pdf/2610.35765
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 推荐系统 · 物品相似度与流行度偏差
tags:
- item-based CF
- similarity measure
- popularity bias
- Rasch model
- implicit feedback
one_liner: 揭示物品相似度的伪相关效应，量化用户活跃度对相似度信号的贡献占比
practical_value: '- 计算物品相似度前可基于本文Rasch模型生成活跃度基线，减去基线后得到的相似度才反映真实用户偏好，避免将高活跃用户的随机共现误判为物品相似

  - 相似度度量选型需匹配业务场景：长尾推荐慎用lift/PMI（其伪相关基线对长尾物品更高）；通用推荐慎用cosine（其伪相关基线随流行度升高，会加剧热门品
  bias）

  - 做推荐模型效果验证时，需将活跃度伪相关基线作为对照组，排除活跃度带来的共现增益干扰，准确衡量模型对真实用户偏好的捕捉能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
物品-物品相似度是协同过滤的核心基础信号，行业默认物品共现反映用户共同偏好，但用户活跃度分布极不均匀的场景下，共现可能仅来自高活跃用户的大量行为，而非真实偏好匹配，这一长期被忽略的偏差会严重误导相似度的落地应用。

### 方法关键点
- 定义「伪相关」：无任何偏好结构、仅用户活跃度存在差异时，标准相似度度量仍会检测到的虚假物品关联
- 基于3个极简假设推导活跃度驱动模型，对应心理测量学的Rasch模型，仅用物品流行度和用户历史长度分布即可拟合出仅由活跃度带来的物品共现概率
- 设计泊松偏差、分块标准化误差两个指标，量化真实数据中相似度信号来自伪相关的占比

### 关键实验
在MovieLens-1M、MovieLens-20M、Amazon Books三个公开数据集上验证：MovieLens数据集里81%的物品对共现偏差可被活跃度单独解释，lift、cosine、Pearson相关、EASE模型的相似度信号中，平均98%以上的系统性偏差来自伪相关；Amazon图书数据集里活跃度也能解释50%左右的共现偏差。

**最值得记住的一句话**：任何基于隐式反馈计算的物品相似度都混合了真实偏好和活跃度基线，只有偏离基线的部分才反映用户的共同喜好。

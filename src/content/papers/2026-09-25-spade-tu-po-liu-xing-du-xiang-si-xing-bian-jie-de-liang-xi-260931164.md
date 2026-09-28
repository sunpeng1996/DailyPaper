---
title: 'SPADE: Escaping the Popularity-Similarity Frontier to Measure Serendipitous
  Recommendations'
title_zh: SPADE：突破流行度-相似性边界的惊喜度推荐度量方法
authors:
- Tobias Vente
- Maarten Peirsman
- Noah Daniëls
- Hannu Toivonen
- Bart Goethals
affiliations:
- University of Antwerp
- University of Helsinki
- Froomle
arxiv_id: '2609.31164'
url: https://arxiv.org/abs/2609.31164
pdf_url: https://arxiv.org/pdf/2609.31164
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 推荐系统评估 · 惊喜度度量
tags:
- Serendipity
- Recommendation Evaluation
- Pareto Frontier
- Offline Metric
- Beyond-Accuracy
one_liner: 提出基于Pareto距离的联合考量流行度、相似性、相关性的惊喜度推荐离线度量指标SPADE
practical_value: '- 电商/内容推荐场景做惊喜度相关的AB实验离线评估时，可直接复用SPADE框架，避免传统单一维度度量的假阳性问题，比如不会将用户未见过的热门爆品误判为高惊喜度推荐

  - 构建流行度-相似度二维空间时，可参考论文的非归一化平滑PPMI作为相似度度量，避免相似度与流行度正相关导致Pareto Frontier失效，保证度量的区分度

  - 做多目标推荐优化时，可将SPADE得分作为惊喜度目标项加入损失函数，从机制上避免算法通过推送随机长尾无关物品刷高惊喜度指标的作弊问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有惊喜度离线度量普遍只孤立考量「和用户历史的相似度」或「全局流行度」单一维度，存在三类核心缺陷：一是会把用户没见过的热门爆品误判为惊喜推荐，二是会把与用户偏好完全无关的长尾冷门品标记为高惊喜度，三是无法过滤不相关的推荐结果，导致算法极易通过无效推荐刷高指标，无法有效衡量同时满足「相关、意外、非热门」的真正惊喜度推荐。
### 方法关键点
- 将所有候选item映射到[0,1]归一化的二维空间：x轴为全局流行度（商品/内容交互次数归一化），y轴为与用户历史交互的相似度（采用非归一化平滑PPMI，从机制上避免与流行度正相关）
- 为每个用户构建专属Pareto Frontier：前沿上的item是当前维度下的最优项（同等相似度下最流行，或同等流行度下最相似），属于最不具备惊喜度的常规推荐池
- SPADE得分仅针对推荐结果中命中用户测试集的相关item计算，取这些item到Pareto Frontier的最小欧氏距离的平均值，得分越高惊喜度越高
### 关键实验
在CiteULike、MIND、MovieLens-1M/20M、Netflix共5个跨域数据集上，对比EASE、SLIM、ItemKNN、Popularity、Random共5类基线算法：Random算法在MIND数据集NDCG仅为0.0006时，传统Prirmitivity、Co-Occurrence指标得分接近最高，但SPADE得分仅0.0036，完美过滤无效随机推荐；EASE在MIND数据集NDCG达0.5286，SPADE得分0.2345，为所有基线最高，可有效识别高相关高惊喜度的推荐结果。
### 核心结论
真正的惊喜度推荐必须同时满足「用户觉得相关」「不在用户熟悉的偏好范围」「不是大众熟知的热门内容」三个条件，缺一不可。

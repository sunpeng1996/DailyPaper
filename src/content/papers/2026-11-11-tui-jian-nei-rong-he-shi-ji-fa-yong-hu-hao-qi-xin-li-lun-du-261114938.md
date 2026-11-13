---
title: When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field
  Evidence
title_zh: 推荐内容何时激发用户好奇心：理论、度量与落地实证
authors:
- Pan Li
- Alexander Tuzhilin
affiliations:
- Georgia Tech
- New York University
arxiv_id: '2611.14938'
url: https://arxiv.org/abs/2611.14938
pdf_url: https://arxiv.org/pdf/2611.14938
published: '2026-11-11'
collected: '2026-11-13'
category: RecSys
direction: 推荐系统 · 好奇心感知优化
tags:
- Recommender System
- Curiosity Modeling
- Information Gap
- User Engagement
- Axiomatic Framework
one_liner: 将信息差理论落地为可计算的好奇心度量，融入推荐系统后在工业场景获显著业务收益
practical_value: '- 可直接复用好奇心度量的三因子计算框架，在现有推荐系统的重排层新增好奇心得分作为优化目标，无需重构底层召回/排序模型，改造成本极低

  - 采用「相关度得分 + 用户个性化好奇心权重 * 好奇心得分」的线性加权效用函数，可针对不同用户分群（如高活跃/新用户）调优权重系数，平衡推荐准确性和探索性

  - 经离线和线上验证的好奇心度量效果优于传统的多样性、意外性、Wundt曲线等探索类 proxy 指标，可直接用来优化推荐探索性，缓解信息茧房问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流推荐系统过度追求相关性，导致信息茧房、消费多样性下降、用户留存受损；而好奇心作为驱动用户主动探索的核心动机，长期缺乏可落地的量化计算模型，现有意外性、多样性、Wundt曲线 arousal 等 proxy 指标无法准确刻画用户对特定物品的动态好奇心，无法直接集成到工业推荐系统中。

### 方法关键点
- 基于信息差理论提出5条好奇心公理，推导出唯一可计算的规范度量公式：$C(u,i,t) = f \cdot \exp\left( -\frac{(g - \tau(1-f))^2}{2\sigma^2} \right)$，其中$g$为用户状态向量与物品向量的欧氏距离（信息差），$f$为用户历史行为中与待推荐物品相近内容的高斯核密度和（周边上下文），$\tau$为用户近期历史信息差的指数加权平均值（自适应参考差）
- 设计好奇心感知推荐框架，采用标准化后的「相关性得分 + 个性化好奇心权重 × 好奇心得分」线性加权作为排序效用，支持无缝接入任意现有推荐模型，无需重构底层架构

### 关键结果
- 离线在Yelp、MovieLens、阿里优酷三个公开/工业数据集上测试，对比DIN、MF基础模型，以及意外性优化、MMR/DPP多样性重排、PCC Wundt曲线模型等基线，好奇心增强的推荐在HR@10上最高提升91%（阿里优酷数据集DIN基线从0.113提升至0.216），同时NDCG、多样性、Novelty均为全指标最优
- 线上在亚洲头部流媒体平台开展大流量A/B测试，相比现有生产系统，CTR、播放量、用户停留时长均显著提升，方案已全量上线

### 核心结论
用户的好奇心不是固定的群体特质，而是随其已有知识储备和近期探索行为动态变化的瞬时状态，仅当推荐内容匹配用户可感知的信息差时，才能同时提升推荐准确性和用户参与度。

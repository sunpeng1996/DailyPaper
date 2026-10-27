---
title: Theoretically Sound Item Similarity Measures for Recommender Systems
title_zh: 推荐系统中具备理论支撑的物品相似度度量方法
authors:
- Noah Daniëls
- Joey De Pauw
- Bart Goethals
affiliations:
- University of Antwerp
- Froomle
arxiv_id: '2610.34402'
url: https://arxiv.org/abs/2610.34402
pdf_url: https://arxiv.org/pdf/2610.34402
published: '2026-10-25'
collected: '2026-10-27'
category: RecSys
direction: 邻域协同过滤 · 物品相似度度量
tags:
- Item Similarity
- Collaborative Filtering
- Implicit Feedback
- Naive Bayes
- kNN
one_liner: 基于概率建模推导两种适用于隐式反馈的物品相似度，为传统启发式度量提供理论解释
practical_value: '- 隐式反馈场景优先选用Multinomial Naive Bayes相似度，相比余弦/条件概率启发式度量，电商/新闻场景Recall@25最高提升28.5%，计算耗时仅为EASE的4%左右，兼顾效果与落地效率

  - 相似度平滑优先选择经验贝叶斯平滑而非均匀加性平滑，尤其对长尾物品多的电商场景，可减少共现稀疏导致的得分不稳定问题，同时缓解流行度偏差

  - 若仍使用传统余弦/条件概率相似度，可参考本文优化视角调整正则项：将余弦相似度正则系数从√(n(i)n(j))替换为n(j)即可消除列维度的流行度偏差'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
邻域协同过滤（item-kNN）因简单、可解释、推理效率高至今是工业界常用推荐方案，但传统余弦、条件概率等相似度均为启发式设计，缺乏理论支撑，存在流行度偏差、对稀疏数据鲁棒性差等问题，从业者只能依靠试错调优，无法系统性优化度量效果。
### 方法关键点
- 将物品相似度构造转化为Naive Bayes分类器的参数优化问题，针对隐式反馈数据特性分别推导了基于Bernoulli和Multinomial事件模型的两种相似度，其中Multinomial模型天然将交互矩阵的0值作为缺失值处理，更适配隐式反馈场景。
- 将相似度平滑对应为贝叶斯估计的先验项，提供了均匀平滑、经验贝叶斯平滑两种落地方案，同时推导了传统余弦、条件概率相似度对应的优化目标形式，从理论层面解释了其流行度偏差的来源。
### 关键实验
在Amazon Books、MIND新闻、ML25M三个公开数据集上对比EASE、传统kNN（余弦/条件概率） baseline：Multinomial NB相似度在Amazon Books上Recall@25达0.324，比余弦相似度提升28.5%，比条件概率提升42.7%；在MIND上Recall@25达0.274，接近SOTA模型EASE的0.276，而计算耗时仅为EASE的4.9%。
### 核心结论
工业界可优先选择具备理论支撑的Multinomial NB相似度替代传统启发式度量，在几乎不增加计算成本的前提下大幅提升推荐效果

---
title: Multi-criteria Rating and Review based Recommendation Model
title_zh: 融合多维度评分与用户评论的推荐模型MRRRec
authors:
- Emrul Hasan
- Chen Ding
- Alfredo Cuzzocrea
affiliations:
- Toronto Metropolitan University
- University of Calabria
arxiv_id: '2611.02019'
url: https://arxiv.org/abs/2611.02019
pdf_url: https://arxiv.org/pdf/2611.02019
published: '2026-11-01'
collected: '2026-11-03'
category: RecSys
direction: 多维度推荐 · 评分与评论融合
tags:
- Multi-criteria Recommendation
- Review-based Recommendation
- Rating Prediction
- DNN
- Attention
one_liner: 融合显式多维度评分与评论隐式维度特征，大幅提升评分预测精度
practical_value: '- 业务侧如果同时拥有用户显式多维度评分（如电商的商品、物流、服务评分）和评论数据，可直接复用双路融合架构：分别处理显式评分特征与评论特征后拼接预测，效果优于单用任意一类特征

  - 评论的词嵌入优先选择Word2Vec，实验验证其比GloVe在该场景下MSE低4.7%、MAE低11%，无需盲目上大模型嵌入可节省成本

  - 显式用户/物品ID的embedding维度选256，融合层DNN隐藏层用[256→128→64]的结构即可，可作为调优基准减少试错成本

  - 从评论提取的隐式维度数量尽量和业务现有显式评分维度数量对齐，可获得最优效果，避免过多隐式维度引入噪声'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多维度推荐方法要么仅使用从评论提取的隐式维度特征，要么仅使用用户显式填写的多维度评分，两类特征的互补性未被充分利用，无法同时捕捉用户的显式偏好和评论中隐含的细粒度偏好，评分预测精度受限，也难以缓解数据稀疏问题。

### 方法关键点
- 双路并行架构：一路通过注意力机制从用户、物品的历史评论中学习维度级表示，计算隐式维度评分；另一路基于用户ID、物品ID的嵌入输入DNN，预测缺失的显式多维度评分
- 融合层：将两路输出的隐式、显式维度评分做拼接归一化，输入三层DNN预测最终整体评分
- 针对词嵌入方案、隐藏层结构、ID embedding维度、隐式维度数量做了全链路消融实验验证最优参数

### 关键实验
基于公开TripAdvisor酒店数据集，对比ANR、DeepCoNN、Nassar多维度推荐三个SOTA基线：MRRRec实现MSE降低19%、MAE降低23%，precision提升7%、recall提升1%、F1提升3.8%；消融实验验证单路只用评论或只用显式评分效果均低于双路融合，隐式维度数量与显式维度对齐（K=5）时效果最优。

### 核心结论
多维度显式评分和评论隐式特征的融合增益远高于单类特征的单独优化，业务中不要浪费任意一类用户反馈数据。

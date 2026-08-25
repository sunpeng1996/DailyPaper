---
title: 'Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active
  Learning Selection'
title_zh: 基于多样性的主动学习：主动学习样本选择的度量空间效果评估
authors:
- Siddharth Chilamkur
- Dorit S. Hochbaum
affiliations:
- University of California, Berkeley
arxiv_id: '2608.23461'
url: https://arxiv.org/abs/2608.23461
pdf_url: https://arxiv.org/pdf/2608.23461
published: '2026-08-24'
collected: '2026-08-25'
category: Training
direction: 主动学习 · 训练样本优化
tags:
- Active Learning
- Greedy K-center
- Sample Selection
- Metric Space
- Entropy Weighting
one_liner: 对比不同度量空间下Greedy K-center主动学习采样效果，验证概率空间加熵加权的最优性
practical_value: '- 电商/广告场景的CTR预估、用户意图分类等标注成本高的任务，可直接采用Greedy K-center做主动学习样本选择，降低标注预算

  - 主动学习采样阶段优先将未标注样本映射到当前模型的预测概率空间，结合熵加权做多样性采样，效果远优于原始特征/LDA空间采样

  - 小样本冷启动模型训练场景，可复用该采样策略，在有限标注量下快速提升模型精度，缩短冷启动周期'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前分类模型训练依赖大量高质量标注数据，电商细分垂类、金融、医疗等场景下标注成本高、效率低，是模型落地的核心瓶颈。池化主动学习通过筛选高信息含量的未标注样本做标注，可大幅降低标注成本，但不同度量空间下基于多样性的采样策略效果差异缺乏系统评估。
### 方法关键点
聚焦多样性驱动的Greedy K-center主动学习采样方案，对比三类不同度量空间下的采样效果：1）原始特征空间；2）LDA降维后的特征空间；3）模型输出的预测概率空间（分别测试无加权、熵加权两种模式）。以随机森林作为基准分类器，在合成数据集与多个真实公开数据集上做对照实验。
### 关键结果
将未标注样本映射到模型预测概率空间、再结合熵加权的Greedy K-center采样方案，效果显著优于其他所有对比方案，在90%的测试数据集上精度排名第一，同等标注预算下分类精度比原始特征空间采样方案平均提升8%~13%

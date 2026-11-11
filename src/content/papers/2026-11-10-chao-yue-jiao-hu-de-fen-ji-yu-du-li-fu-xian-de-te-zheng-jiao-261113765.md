---
title: 'Beyond Interaction Scores: Selecting Feature Interactions via Independent
  Replication'
title_zh: 超越交互得分：基于独立复现的特征交互选择方法
authors:
- Jincheng Gao
- Shuo Sun
affiliations:
- HKUST(GZ)
arxiv_id: '2611.13765'
url: https://arxiv.org/abs/2611.13765
pdf_url: https://arxiv.org/pdf/2611.13765
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 特征交互筛选 · 可解释机器学习
tags:
- Feature_Interaction
- Model_Agnostic
- Interpretable_ML
- Hypothesis_Testing
- Reproducibility
one_liner: 提出模型无关的LENS框架，通过独立复现筛选可复用的真实特征交互，避免拟合噪声
practical_value: '- 电商CTR/CVR建模做特征交叉筛选时，可复用LENS的拆分数据集独立训练+复现校验机制，替代人工定阈值的排序方法，大幅降低噪声交叉的误选概率

  - 无论特征量级多大仅需两次模型训练即可完成筛选，工程实现成本远低于需多次重训的方法，适配电商大特征量的业务场景

  - 筛选出的高置信特征交叉可直接融入LR、GBDT等浅模型，无需引入复杂大模型即可提升预测精度，同时增强模型可解释性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有特征交互筛选方法存在两类缺陷：排序法需人工设定截断阈值，测试法依赖多次模型重训或特征联合分布假设，高交互得分往往对应拟合噪声而非可复现的真实模式。

### 方法关键点
1. 模型无关的LENS框架，拆分数据集为两份，用相同算法训练两个独立模型，仅通过预测结果访问
2. 对每个特征对剥离主效应，分离出独立交互模式，按强度排序后验证是否在第二个模型中达到有效强度
3. 仅需两次训练，通过一次多重检验校正确定保留的特征对，不受特征数量影响

### 关键结果数字
16组合成数据上，召回91%真实交互，远高于DIAMOND的45%，无假阳选择；大规模车险数据上恢复全交叉90%的偏差增益；两个信用数据集上仅筛选少量交互，性能比加性基线持平或微升

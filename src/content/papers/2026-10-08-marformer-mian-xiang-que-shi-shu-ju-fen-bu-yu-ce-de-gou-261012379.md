---
title: 'Marformer: A Transformer for Predicting Missing Data Distributions'
title_zh: Marformer：面向缺失数据分布预测的Transformer架构
authors:
- Prabhav Singh
- Xiheng Tom Wang
- Haojun Shi
- Jason Eisner
affiliations:
- The University of Texas at Austin
- Johns Hopkins University
- Yale University
arxiv_id: '2610.12379'
url: https://arxiv.org/abs/2610.12379
pdf_url: https://arxiv.org/pdf/2610.12379
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 缺失数据处理 · 条件边际分布预测
tags:
- Transformer
- Missing Data
- Conditional Marginal
- Value of Information
- Distribution Prediction
one_liner: 提出无需建模全联合分布的Marformer，单前向传播即可预测任意观测下缺失变量的条件边际分布
practical_value: '- 推荐系统冷启动/稀疏场景下，可复用Marformer思路，仅用少量观测特征单前向pass预测用户/物品缺失属性的分布，无需建模全联合分布，大幅降低算力开销

  - 电商动态决策场景（如是否发优惠券、是否补采用户行为），可基于Marformer输出的条件边际分布计算VOI，辅助判断额外采集数据的投入产出比

  - 商品/内容标注任务中，可利用Marformer预测缺失标注的分布，减少人工标注成本，推理速度远优于传统生成式基线'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
真实业务与科学场景普遍存在数据缺失问题，传统缺失数据处理方法要么需要建模全联合分布、依赖数据生成过程先验知识，要么推理速度慢，无法满足实时决策要求。
### 方法关键点
1. 参考BERT掩码预训练思路，为每个变量的分布生成隐向量表示，通过注意力机制迭代优化表示
2. 无需建模全联合分布，也不需要数据生成领域知识，所有预测仅需单次前向传播即可完成
### 关键结果数字
- 在贝叶斯网络、离散多元高斯、结构化标注3类合成数据集上，效果持平或优于已知真实生成先验的传统缺失数据方法
- 真实标注数据集上，训练规模最大时效果超过所有对比基线
- 推理速度显著优于所有生成式基线

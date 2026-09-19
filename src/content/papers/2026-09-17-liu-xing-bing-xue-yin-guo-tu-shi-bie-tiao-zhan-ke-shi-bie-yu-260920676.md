---
title: 'Epidemiological Causal Graph Identification: Challenges, Identifiability and
  Algorithms'
title_zh: 流行病学因果图识别：挑战、可识别性与算法
authors:
- Sambit Mishra
- Yingying Wang
- Christine K. Johnson
- Urbashi Mitra
affiliations:
- University of Southern California
- University of California, Davis
arxiv_id: '2609.20676'
url: https://arxiv.org/abs/2609.20676
pdf_url: https://arxiv.org/pdf/2609.20676
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 因果发现 · DAG结构学习
tags:
- Causal Discovery
- DAG
- Exponential Family
- Structure Learning
- Ordinal Distribution
one_liner: 拓展混合序分类与指数族变量的因果边可识别性，给出两种DAG求解算法
practical_value: '- 混合类型变量（用户评分/行为计数/连续特征）的因果方向识别方法可复用，优化用户建模特征归因

  - 大规模DAG求解的带掩码连续优化框架可迁移到多变量因果召回的结构学习工程实现

  - 序分类变量（用户满意度/商品等级）的因果建模逻辑可用于广告归因、转化路径分析'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有因果发现可识别性研究多聚焦加性噪声下的连续变量，难以适配含序分类、计数、连续测量的混合数据集，无法满足真实场景多类型变量的因果建模需求。
### 方法关键点
1. 证明序分类（有序logit建模）与单参数指数族分布变量间的因果边在通用参数下具备分布可识别性，将原有有序-泊松结论泛化到全指数族
2. 小图采用基于评分的穷举搜索，大图适配DAGMA提出带掩码的连续优化框架实现高效求解
### 关键结果
实验验证方法可识别经典结构方程模型无法区分的马尔可夫等价类内的边方向，理论结论完全成立

---
title: Score-Based Learning of Cluster DAGs from Interventions
title_zh: 基于评分的干预场景下聚类有向无环图（DAG）学习方法
authors:
- Gaetano Tedesco
- Alex Markham
affiliations:
- University of Amsterdam
- University of Copenhagen
arxiv_id: '2610.11947'
url: https://arxiv.org/abs/2610.11947
pdf_url: https://arxiv.org/pdf/2610.11947
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 因果结构发现 · 聚类DAG学习
tags:
- Causal Discovery
- DAG Learning
- Score-based Method
- Clustering
- Interventional Data
one_liner: 提出首个面向聚类DAG学习的评分法COARSE，边学习阶段速度较SOTA最高快两个数量级
practical_value: '- 做用户行为/商品属性的因果聚类时，可复用先聚类后学边的两阶段框架，降低大规模DAG学习的计算复杂度

  - 做营销归因、策略效应评估等因果分析时，可采用集群级BIC评分做局部搜索的思路，大幅提速边学习过程

  - 线性高斯假设下的干预数据因果结构学习场景，可直接替换原有约束式边学习模块，精度持平SOTA'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有因果抽象生成的聚类DAG可解释性强，但传统约束式两阶段学习方法计算效率极低，难以适配数百节点的稠密图场景，无法满足大规模因果分析需求。
### 方法关键点
提出首个评分式聚类DAG学习方法COARSE，保留先聚类后学边的两阶段框架，在线性高斯假设下将原约束式边学习模块替换为评分式方案；利用干预数据直接推导聚类间因果序，每个聚类仅需基于聚类级BIC评分做一次局部搜索即可完成边学习，算法为多项式时间复杂度且一致收敛。
### 关键结果
在合成和真实干预数据集上，样本量充足时边恢复效果与SOTA持平，边学习阶段速度最高提升2个数量级，可稳定支撑数百节点的稠密图学习任务。

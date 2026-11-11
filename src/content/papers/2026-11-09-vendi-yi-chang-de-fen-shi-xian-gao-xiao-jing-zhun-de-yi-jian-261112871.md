---
title: Vendi Anomaly Scores for Efficient and Accurate Anomaly Detection
title_zh: Vendi 异常得分：实现高效精准的异常检测
authors:
- Amey Pasarkar
- Adji Bousso Dieng
affiliations:
- Princeton University
- Lewis-Sigler Institute for Integrative Genomics
- Vertaix
arxiv_id: '2611.12871'
url: https://arxiv.org/abs/2611.12871
pdf_url: https://arxiv.org/pdf/2611.12871
published: '2026-11-09'
collected: '2026-11-11'
category: Other
direction: 嵌入空间异常检测 · 无参算法
tags:
- AnomalyDetection
- VendiScore
- Embedding
- NonParametric
- DataCuration
one_liner: 从多样性视角提出无参无需调参的VAS异常检测方法，多数据集下性能达SOTA
practical_value: '- 可复用VAS方法做推荐/广告训练样本的异常清洗，识别脏数据、错标样本，无需调参即可适配不同embedding空间

  - 可借鉴「移除样本后多样性变化」的思路做冷启动item质量评估，判断新上架商品是否为离群异常品

  - 大规模数据集下VAS线性复杂度的工程实现可直接复用，适配亿级embedding的异常检测场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有异常检测方法依赖局部密度、孤立启发式或分布拟合，对邻域尺度、划分规则敏感，且需超参数调优，不适合大规模embedding空间的异常检测需求。
### 方法关键点
1. 从多样性视角定义异常，提出VAS得分，通过量化单样本被移除后数据集Vendi多样性得分的变化幅度判断异常程度
2. 无参设计，自动适配数据的谱结构，同时捕捉局部冗余与全局结构，复杂度随数据集规模线性增长
### 关键结果
在148个覆盖10个源数据集、4种embedding架构的基准数据集上取得SOTA性能；大规模ImageNet实验中，随污染率、数据集规模提升仍保持鲁棒性

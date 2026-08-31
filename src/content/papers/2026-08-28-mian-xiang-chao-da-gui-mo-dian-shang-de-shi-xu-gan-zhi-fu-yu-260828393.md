---
title: 'Timing-Aware Repurchase Prediction for Web-Scale E-Commerce: Survival Models
  for Multi-Surface Grocery Recommendation'
title_zh: 面向超大规模电商的时序感知复购预测：多入口杂货推荐的生存模型
authors:
- Akshay Kekuda
- Shreeranjani Srirangamsridharan
- Ishan Bhatt
- Yanan Cao
- Sinduja Subramaniam
- Evren Korpeoglu
- Kaushiki Nag
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.28393'
url: https://arxiv.org/abs/2608.28393
pdf_url: https://arxiv.org/pdf/2608.28393
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 电商复购推荐 · 生存分析建模
tags:
- Survival Analysis
- Repurchase Recommendation
- Accelerated Failure Time
- XGBoost
- Multi-horizon Recommendation
one_liner: 用单生存模型替代3个分时间窗口的二分类复购模型，提升多入口排序精度同时降低3倍计算资源消耗
practical_value: '- 多时间窗口的复购/补购场景，可直接用XGBoost AFT生存目标替代原有多套二分类模型，压缩3倍训练和服务成本，同时排序精度不输甚至超过基线

  - 按场景选型AFT分布：纯排序需求用Log-Normal AFT；需输出校准概率的场景（广告出价、补购标签透出、 propensity 融合）选Exponential
  AFT，其ECE低至1e-4，校准精度比Log-Normal高10倍

  - 特征迭代优先做渠道节奏、近7天复购间隔类特征，生存目标下这类特征重要性远高于3个月总订单这类聚合频次特征；切记不要删除右截断样本，会直接导致模型泛化性崩溃

  - 可复用4参数跨窗口校准方法，共享shape参数+分窗口截距，天然保证7/14/28天复购概率单调性，无需额外后处理裁剪'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有电商复购推荐多按不同入口的时间窗口（7天首页购物清单、14天APP补货轮播、30天邮件 pantry 规划）单独训练二分类模型，需维护3套独立训练、服务链路，成本高且丢失复购时序结构，无法适配多窗口需求。

### 方法关键点
- 引入AFT（加速失效时间）生存模型，直接预测用户-商品对的复购时间，单模型可支撑所有时间窗口的排序需求，排序规则为预测复购时间越短排名越高，可直接替换原有二分类模型的推理链路
- 配套4参数参数化校准方案：共享shape参数+分窗口截距，天然保证跨窗口复购概率单调性，零冲突
- 可选离散时间（DT）生存模型，通过person-period数据扩增输出分窗口的独立排序

### 关键结果
在沃尔玛千万级用户的杂货电商数据集上，对比3套分窗口的XGBoost二分类基线：
1. 单AFT模型（约700棵树）在7/14/28天P@h指标上均超过基线，其中Log-Normal AFT的14天P@h达0.3788，比基线高0.82%
2. 计算资源降低3倍：从原3套模型共2400棵树压缩到单模型约700棵树
3. 校准性能上Exponential AFT的14天ECE低至1.3e-4，比Log-Normal低约6倍

最值得记住的结论：复购预测问「什么时候买」比问「会不会买」，效果更好、成本更低。

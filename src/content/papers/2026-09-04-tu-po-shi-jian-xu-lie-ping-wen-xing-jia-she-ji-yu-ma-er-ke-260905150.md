---
title: 'Beyond Stationarity in Time Series: Discovering Causal Structures and Latent
  Regimes via Markov Blankets'
title_zh: 突破时间序列平稳性假设：基于马尔可夫毯的因果结构与隐状态识别
authors:
- Lei Zan
- Charles K. Assaad
- Emilie Devijver
- Eric Gaussier
affiliations:
- Univ. Grenoble Alpes, CNRS, Grenoble INP, LIG, Grenoble, France
- Sorbonne Université, INSERM, Institut Pierre Louis d’Epidémiologie et de Santé Publique,
  Paris, France
arxiv_id: '2609.05150'
url: https://arxiv.org/abs/2609.05150
pdf_url: https://arxiv.org/pdf/2609.05150
published: '2026-09-04'
collected: '2026-09-07'
category: Other
direction: 非平稳时间序列 · 因果发现
tags:
- Causal Discovery
- Time Series
- Markov Blanket
- Non-stationarity
- Regime Shift
one_liner: 提出RCBNB-MB算法，可识别非平稳时间序列的隐因果状态及各状态下的因果结构
practical_value: '- 电商用户行为、流量时序普遍存在大促/平日等 regime 切换，可借鉴基于因果 regime 分段的思路，拆分不同场景下的特征因果关系，提升推荐模型场景适配性

  - 特征选择环节可借鉴 Markov Blanket 替代直接父节点的思路，提升特征鲁棒性，减少噪声特征对排序/召回模型的干扰

  - 业务根因分析（如流量下跌、转化率异常）场景，可复用该算法的 regime 切换检测+分场景因果图定位能力，加快异常根因定位效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时间序列因果发现方法普遍假设因果结构平稳不变，但真实动态系统的时序数据存在大量 regime 切换，静态因果假设会导致较大误差，无法满足时序分析、预测、根因定位的需求。

### 方法关键点
提出RCBNB-MB算法，采用迭代策略：首先将时序切分为多个隐因果regime（同一regime内因果结构稳定），再分别挖掘每个regime内的因果图；引入Markov Blanket替代直接父节点做因果挖掘，提升抗噪性同时保留全量预测信息，理论上可保证正确恢复regime切换点与对应因果图。

### 关键结果
在模拟数据集和真实IT监控数据集上，RCBNB-MB在regime切换检测、因果图识别精度两个核心指标上均全面优于所有基线方法。

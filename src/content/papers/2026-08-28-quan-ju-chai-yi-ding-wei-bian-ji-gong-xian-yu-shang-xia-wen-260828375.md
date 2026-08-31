---
title: 'Localizing Global Discrepancies: Marginal Contributions and Contextual Anomaly
  Detection'
title_zh: 全局差异定位：边际贡献与上下文异常检测框架
authors:
- Tommaso dorigo
affiliations:
- INFN, Sezione di Padova
- Luleå University of Technology
arxiv_id: '2608.28375'
url: https://arxiv.org/abs/2608.28375
pdf_url: https://arxiv.org/pdf/2608.28375
published: '2026-08-28'
collected: '2026-08-31'
category: Other
direction: 上下文异常检测 · 全局差异定位框架
tags:
- Anomaly Detection
- Data Valuation
- MMD
- Goodness-of-Fit
- Statistical Framework
one_liner: 提出基于边际贡献与随机上下文的全局差异定位框架，可定位驱动样本偏离参考分布的异常观测
practical_value: '- 可复用上下文感知的异常检测思路，用于推荐/广告系统样本分布偏移根因定位，快速识别导致全局效果下降的异常流量、用户或物料

  - 边际贡献计算范式可迁移到训练数据估值场景，为推荐模型训练样本做重要性打分，辅助高效筛选高质量训练样本降低训练成本

  - 匹配上下文抵消无关波动的trick可用于A/B测试效果校验，排除全局随机波动对单组实验效果评估的干扰，提升显著性判断准确率'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统全局拟合优度与差异统计仅能判断样本是否偏离参考分布，无法定位具体哪些观测驱动了偏离，缺乏统一的定位技术框架。
### 方法关键点
1. 为每个观测分配随机统计上下文下的条件/边际贡献，系统性打通重采样诊断、数据估值与投影理论、事件级异常检测的关联；
2. 针对对称统计、U统计、光滑分布泛函、无偏已知背景MMD等不同场景，给出对应贡献的计算范式；
3. 提出匹配上下文抵消无关波动的优化策略，针对成对MMD给出轻量化定位器。
### 关键结果
在LHC奥运会异常检测基准上，当batch size=1000、batch数=5e6时，成对estimator与直接经验MMD witness相关度达0.9993，AUC几乎一致；共享隐变量玩具模型下，仅依赖样本间上下文关联信息即可实现AUC>0.5，突破单事件分类器的理论上限。

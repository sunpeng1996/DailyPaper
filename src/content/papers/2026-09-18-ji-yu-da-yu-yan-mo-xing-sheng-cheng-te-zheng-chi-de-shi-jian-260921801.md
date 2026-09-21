---
title: LLM-Generated Feature Pools for Time Series Anomaly Detection
title_zh: 基于大语言模型生成特征池的时间序列异常检测方法
authors:
- Youssef Attia El Hili
- Malik Tiomoko
- Corinne Ancourt
affiliations:
- Huawei Noah’s Ark Lab
- Centre de Recherche en Informatique, Mines Paris, PSL University
arxiv_id: '2609.21801'
url: https://arxiv.org/abs/2609.21801
pdf_url: https://arxiv.org/pdf/2609.21801
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 时序异常检测 · LLM特征生成
tags:
- TimeSeriesAnomalyDetection
- LLM
- FeatureEngineering
- MultimodalLLM
- StatisticalModel
one_liner: 用多模态LLM生成时序异常检测特征池，与手工池合并后达到公开数据集SOTA水平
practical_value: '- 做电商流量/销量异常检测、用户行为序列异常识别等时序任务时，可优先验证特征池天花板效应，不用先堆复杂模型，优先扩充特征池性价比更高

  - 特征工程阶段可引入多模态LLM做In-Context特征生成，将生成特征与手工特征取并集，能覆盖更多模式，提升下游任务效果

  - 小样本/跨域时序任务中，可直接用LLM基于域内示例生成专属特征池，降低手工特征的跨域适配成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
时序异常检测领域默认复杂深度/预训练大模型效果优于统计方法，但调优后传统统计方法仍有竞争力，ablation验证特征池是决定性能上限的核心因素，特征选择、聚合策略的影响远低于特征池本身。

### 方法关键点
1. 搭建轻量统计baseline：滑动窗口提取统计特征，用MAD鲁棒模型打分，按域在验证集选择特征子集
2. 构造带域内示例窗口的prompt调用多模态LLM，按域生成专属特征池，将生成池与手工池取并集后再做特征筛选

### 关键结果
- 纯手工特征池baseline在TSB-AD-U数据集VUS-PR达0.529，优于榜单最优神经（0.45）、统计（0.44）方法，仅比最强预训练大模型低0.06
- 生成+手工特征池合并后VUS-PR达0.588，匹配公开榜单最优水平，该增益在12组生成种子实验中全部成立

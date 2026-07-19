---
title: 'Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment
  Classifier'
title_zh: 基于区块链活动的市场情绪解码：数据驱动的情感分类器
authors:
- Arthur G. Bubolz
- Abreu Quevedo
- Giancarlo Lucca
- Rafael A. Berri
- Eduardo Borges
- Bruno L. Dalmazo
affiliations:
- Federal University of Rio Grande (FURG), Brazil
arxiv_id: '2607.15258'
url: https://arxiv.org/abs/2607.15258
pdf_url: https://arxiv.org/pdf/2607.15258
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 市场情绪分析 · 多源数据融合
tags:
- Sentiment Analysis
- XGBoost
- SHAP
- On-Chain Data
- Multi-source Fusion
one_liner: 融合链上、金融、社交媒体多源数据训练XGBoost分类器，实现比特币市场情绪分类F1达0.84
practical_value: '- 多源异构特征（行为/交易/公域舆情）融合做分类任务时，可优先测试XGBoost作为baseline快速拿到性能基准

  - 业务模型上线需要可解释性支撑时，可引入SHAP量化各维度特征贡献，满足监管/运营复盘需求

  - 做用户购买情绪/消费舆情相关预测任务时，可参考「行为数据+交易数据+公域舆情」的特征组合范式'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
比特币作为去中心化数字资产的投资需求快速增长，现有研究多聚焦价格预测，缺乏可解释的市场情绪分析方案，无法支撑投资者决策。
### 方法关键点
1. 融合三类异构特征：区块链链上交易数据、比特币历史价格等金融数据、Twitter日度情感分类结果，归一化后构建分析数据集；
2. 对比多种机器学习模型，选择XGBoost作为最优情绪分类器；
3. 引入基于博弈论的SHAP方法量化各特征对预测结果的贡献，提升模型透明度与可解释性。
### 关键结果
经交叉验证，XGBoost分类器平均F1得分达0.84，多源特征组合可产出有效预测信号，可支撑数据驱动的加密货币市场分析。

---
title: 'Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine
  Learning'
title_zh: 基于机器学习的Solana链欺诈性迷因币撤池风险早期检测
authors:
- Jianghai Li
- Pavel Kuznetsov
- Yury Yanovich
- Konstantin Nott-Whaley
- Igor Vodolazov
affiliations:
- Higher School of Economics
- Moscow State University
- Skolkovo Institute of Science and Technology
- Independent Researcher
arxiv_id: '2608.20271'
url: https://arxiv.org/abs/2608.20271
pdf_url: https://arxiv.org/pdf/2608.20271
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 链上风控 · 欺诈行为早期检测
tags:
- Fraud Detection
- Solana
- Memecoin
- XGBoost
- DeFi
- Risk Control
one_liner: 基于7个月640万代币数据，用XGBoost仅需上线前5分钟交易数据即可检测Solana迷因币撤池欺诈
practical_value: '- 实时风控类任务（如电商新商家欺诈检测、广告虚假流量识别）可优先验证XGBoost等轻量梯度提升模型，仅需目标对象极早期行为数据即可拿到鲁棒效果，落地成本远低于大模型方案

  - 跨域风险检测场景（如多流量源反作弊、多渠道交易风控）可采用多源数据融合方案，有效缓解不同域的分布偏移问题，提升模型泛化性能

  - 缺失静态特征（如新品类资质、新账号历史数据）的风控任务，可基于纯时序行为特征建模，无需依赖代码、资质等静态信息即可完成风险预判'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
Solana是当前迷因币交易量、发行数量最高的公链，其撤池欺诈主要由流动性操纵、社交动态驱动，不存在以太坊场景下的智能合约后门特征，现有研究覆盖极少；且绝大多数欺诈在代币上线1小时内发生，亟需超短周期的早期检测能力。
### 方法关键点
构建覆盖7个月、640万枚代币的大规模标注数据集，仅提取代币上线前5分钟的交易行为特征，无需代码级静态特征，采用XGBoost等经典机器学习模型建模，验证PumpFun、Raydium两大交易平台的跨域泛化效果，通过多源数据融合缓解领域偏移问题。
### 关键结果
仅用前5分钟交易数据的XGBoost模型即可实现鲁棒的撤池欺诈检测效果；多源数据融合可显著缓解领域偏移，大幅提升跨平台检测可靠性，绝大多数迷因币的欺诈特征在上线1小时内即可被捕捉。

---
title: 'Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for
  Financial Anomaly Detection'
title_zh: Semantic Pareto-DQN：面向金融异常检测的多目标强化学习框架
authors:
- Cláudio Lúcio do Val Lopes
- Lucca Machado da Silva
affiliations:
- A3Data
arxiv_id: '2607.09641'
url: https://arxiv.org/abs/2607.09641
pdf_url: https://arxiv.org/pdf/2607.09641
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: 多目标强化学习Agent · 金融异常检测
tags:
- Reinforcement-Learning
- Multi-Objective-Optimization
- LLM
- Fraud-Detection
- Pareto-Optimization
one_liner: 将异质交易特征转为自然语言叙事经LLM编码，构建多目标RL金融异常检测框架平衡漏判与用户摩擦
practical_value: '- 电商风控/反欺诈场景可复用「结构化特征转自然语言叙事+LLM编码」的state构造方法，避免特征缩放、缺失带来的鲁棒性问题

  - 多目标优化场景可直接借鉴Pareto-DQN的向量reward拆分思路，将业务多个冲突目标（如GMV、用户体验、合规）解耦单独建模

  - 极端样本不平衡场景无需依赖重采样，通过多目标RL动态调整决策边界的思路可迁移到低曝光冷启item召回、小众需求推荐场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
金融异常检测（含电商交易欺诈、信用卡违约）存在极端类别不平衡问题，传统单目标算法易出现「欺诈坍缩」，全部预测为多数类，无法平衡异常拦截率与误判带来的用户摩擦，常用数据重采样方法还会引入分布扭曲。

### 方法关键点
1. 将异质交易特征合成连贯自然语言叙事，经LLM编码生成鲁棒、尺度不变的状态表示，无需特征标准化预处理
2. 设计向量式奖励，将金融收益、运营摩擦、语义发现三个冲突目标显式解耦单独建模
3. 基于Pareto-DQN拟合连续帕累托最优前沿，动态权衡漏判异常和误判的不对称成本，全程无需数据重采样

### 关键结果
在电商欺诈数据集、UCI Credit数据集上验证，成功打破零召回陷阱，相比标量化基线模型，少数类（异常样本）召回率显著提升，可在运营摩擦可控的前提下大幅提升异常发现能力。

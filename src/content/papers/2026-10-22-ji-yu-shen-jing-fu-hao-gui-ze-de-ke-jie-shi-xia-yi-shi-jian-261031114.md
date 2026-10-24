---
title: 'What Comes Next and Why: Interpretable Next-Event Prediction with Neuro-Symbolic
  Rules'
title_zh: 基于神经符号规则的可解释下一事件预测方法
authors:
- Tim Nico Bauerschmidt
- Isabel Valera
- Jilles Vreeken
affiliations:
- Saarland University
- CISPA Helmholtz Center for Information Security
arxiv_id: '2610.31114'
url: https://arxiv.org/abs/2610.31114
pdf_url: https://arxiv.org/pdf/2610.31114
published: '2026-10-22'
collected: '2026-10-24'
category: RecSys
direction: 可解释时序行为预测 · 神经符号学习
tags:
- Neuro-Symbolic Learning
- Interpretability
- Next-Event Prediction
- Sequential Recommendation
- Rule Mining
one_liner: 提出融合可解释序列规则与残差网络的RUNES框架，兼顾时序预测精度与可解释性
practical_value: '- 电商用户行为预测场景可复用「规则模块+残差网络」的加性融合架构：规则部分输出的高置信度时序规律可直接支撑运营策略制定，残差网络兜底保证整体预测精度

  - 冷启动场景可直接部署RULES模块输出的紧凑时序规则到规则引擎，无需复杂模型推理即可实现基础的用户行为预判，降低冷启动成本

  - 监管合规要求高的推荐/营销场景，可直接输出触发预测的活跃规则作为结果解释依据，满足审计与用户知情权要求'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有时序事件预测方法普遍优先优化精度，牺牲可解释性；神经符号方法虽能通过学习符号规则提升可解释性，但难以适配时序依赖复杂的序列预测场景，电商、医疗等合规敏感场景对可解释预测需求迫切。
### 方法关键点
1. 提出RULES神经符号模块，直接从原始序列数据中自动学习紧凑、可解释的时序规则
2. 构建RUNES框架，将RULES的规则输出与残差网络的预测结果加性融合，同时保留可解释性与复杂时序模式建模能力
### 关键结果
RULES在合成数据集上可100%还原真实规则；RUNES在真实业务数据集上精度与纯SOTA神经网络模型持平，同时支持透明查询触发预测的活跃规则、以及残差网络对预测结果的调整幅度。

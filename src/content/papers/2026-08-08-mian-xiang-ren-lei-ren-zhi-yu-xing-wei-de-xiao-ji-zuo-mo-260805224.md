---
title: Small Foundation Models of Human Cognition and Behaviour
title_zh: 面向人类认知与行为的小基座模型
authors:
- Nick Oh
- Fernand Gobet
affiliations:
- socius labs
- London School of Economics and Political Science
arxiv_id: '2608.05224'
url: https://arxiv.org/abs/2608.05224
pdf_url: https://arxiv.org/pdf/2608.05224
published: '2026-08-08'
collected: '2026-08-11'
category: LLM
direction: 小基座LLM · 认知行为拟合
tags:
- Small LLM
- Scaling Law
- Cognitive Modeling
- Behaviour Simulation
- Out-of-distribution Generalization
one_liner: 在10.7M条人类认知行为数据上验证小模型分布内拟合能力与大模型分布外泛化优势
practical_value: '- 分布内的用户行为拟合场景可优先选用0.6B~1B小参数模型，成本远低于70B大模型但效果相当，适配用户点击/购买决策预判等同分布任务

  - 跨新业务场景的用户行为建模优先选择大参数模型，其分布外泛化能力显著优于小模型

  - 用户行为建模特征设计时，优先保留实时反馈、当前场景刺激特征（如商品信息、活动文案），仅依赖历史行为特征的模型效果损失超75%'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
基于人类行为数据微调的LLM作为认知代理存在规模成本高、决策依赖信息不明确的问题，需明确不同参数规模模型的适用边界与信息依赖逻辑。
### 方法
训练覆盖4类架构、135M~14B参数的14个模型，在包含160项实验、10.7M条试次级选择数据的Psych-101数据集上训练，分别测试分布内/分布外表现，通过Prompt通道掩码、试次顺序打乱实验诊断模型信息依赖。
### 关键结果
分布内模拟时规模效应极弱，0.6B~1B参数模型即可达到70B基线效果；分布外泛化时规模梯度极陡，大模型优势明显；掩码刺激与反馈信息会损失75.7%的学习信息，模型表现低于随机水平，验证仅靠历史行为不足以支撑决策效果。

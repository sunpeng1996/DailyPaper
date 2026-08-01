---
title: 'INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models'
title_zh: INTACT：面向无搜索世界模型的同构意图-动作学习
authors:
- Junhan Sun
- Hao Zhao
- Guofeng Zhang
affiliations:
- State Key Laboratory of CAD&CG, Zhejiang University
- Institute for AI Industry Research (AIR), Tsinghua University
- InSpatio
- RoboParty Lab
arxiv_id: '2607.26056'
url: https://arxiv.org/abs/2607.26056
pdf_url: https://arxiv.org/pdf/2607.26056
published: '2026-07-27'
collected: '2026-08-01'
category: Agent
direction: Agent 世界模型意图到动作映射
tags:
- World Model
- JEPA
- Intent Alignment
- Action Generation
- Efficient Inference
one_liner: 提出同构架构的端到端JEPA模型INTACT，实现无搜索的意图到动作直接映射，降低推理开销提升控制成功率
practical_value: '- 意图到动作的同构参数共享架构可迁移到推荐系统的用户意图→召回/排序动作映射链路，降低多场景适配成本

  - 无搜索直接输出策略的思路可复用在推荐实时推理链路，替代现有重排序阶段的候选集搜索，大幅降低推理延迟

  - 异构意图（局部/目标）统一表征方法可借鉴到用户多模态意图建模，提升不同场景下意图识别的一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
前向隐式世界模型需要在测试阶段通过昂贵的搜索才能为目标状态匹配对应动作，推理开销高、落地难度大。

### 方法关键点
1. 提出端到端JEPA架构INTACT，基于四槽语法和参数共享实现局部/目标运动意图的同构表征；
2. 用同一预测器诱导的动作规则语义替代逐点隐层匹配，实现RGB观测到动作有效隐意图坐标的跨域迁移；
3. 非对称端点梯度锚定目标状态，无需逐点隐层匹配或全局线性动态即可联合表征学习与控制，输出的分布动作规则均值可直接作为无搜索策略。

### 关键结果
在4项LeWM基准任务上，单epoch零搜索模型成功率分别达85.78%、100%、97.67%、97.89%；可选局部CEM仅用384个候选序列就达到96.86%的宏观成功率，采样量降低23.44倍，比纯CEM提升16个百分点；直接推理延迟仅2.9~5.5ms，比传统CEM方案降低约300倍。

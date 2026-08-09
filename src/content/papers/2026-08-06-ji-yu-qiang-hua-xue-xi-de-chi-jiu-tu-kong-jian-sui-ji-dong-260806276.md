---
title: Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning
title_zh: 基于强化学习的持久图空间随机动力学建模
authors:
- Farzana Nasrin
affiliations:
- Department of Mathematics, University of Tennessee, Knoxville
arxiv_id: '2608.06276'
url: https://arxiv.org/abs/2608.06276
pdf_url: https://arxiv.org/pdf/2608.06276
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 拓扑数据分析 · 强化学习驱动持久图建模
tags:
- Persistence Diagram
- Topological Data Analysis
- Reinforcement Learning
- Stochastic Dynamics
- Probabilistic Modeling
one_liner: 提出RL驱动的持久图空间随机演化框架，支持拓扑感知编辑与结构保留的复杂度压缩
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有持久图（PD）统计分析框架多将PD视为静态对象，缺乏PD空间上的概率建模与随机演化能力，无法同时满足核心拓扑结构保留与图复杂度压缩的需求。
### 方法关键点
1. 提出RL驱动的PD空间随机动力学框架，通过拓扑感知局部编辑操作演化PD，定义可变基数有限PD空间上的受控马尔可夫过程；
2. 证明诱导马尔可夫链满足不可约、非周期、几何遍历条件，保证PD空间上存在唯一平稳概率分布；
3. 设计融合分布匹配、任务专属拓扑统计、结构保留压缩的奖励函数，平衡任务目标、PD保真度与复杂度下降要求。
### 关键结果
在合成数据、神经影像PD实验中，框架可在保留核心拓扑结构的前提下降低PD复杂度。

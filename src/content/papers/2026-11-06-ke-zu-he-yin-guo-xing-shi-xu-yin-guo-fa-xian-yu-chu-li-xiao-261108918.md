---
title: 'Composable Causality: A Toolkit for Systematic Time-Series Causal Discovery
  and Treatment-Effect Benchmarking'
title_zh: 可组合因果性：时序因果发现与处理效应基准测试工具包
authors:
- Muhammad Hasan Ferdous
- Md Osman Gani
affiliations:
- University of Maryland, Baltimore County
- Causal AI Lab, Department of Information Systems
arxiv_id: '2611.08918'
url: https://arxiv.org/abs/2611.08918
pdf_url: https://arxiv.org/pdf/2611.08918
published: '2026-11-06'
collected: '2026-11-09'
category: Other
direction: 时序因果发现 · 处理效应评估工具
tags:
- Causal_Discovery
- Time_Series
- Treatment_Effect
- Benchmarking
- Synthetic_Data
one_liner: 推出组件化可配置的DTCD时序因果数据生成库，配套因果发现与处理效应基准测试能力
practical_value: '- 做电商营销、推荐策略的因果效应评估时，可用DTCD生成可控属性的模拟时序数据，提前验证新因果模型的鲁棒性，降低真实流量试错成本

  - 可复用其反事实孪生生成逻辑：缓存事实序列的随机因子，干预时回注即可得到精准的个体处理效应，适配个性化补贴、定向推荐的效果量化需求

  - 其单变量控制实验的设计思路，可迁移到推荐AB测的变量隔离场景，精准定位策略效果的真实影响因子，排除混淆变量干扰'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
真实多变量时序无标注因果结构，现有合成因果数据不可修改或属性固定，无法支持控制变量实验；反事实评估工具多为论文定制化实现，仅能生成观测数据，无法满足通用验证需求。
### 方法关键点
1. 推出DTCD组件化数据生成库，拓扑、生成机制、噪声、观测掩码、干预策略为独立可配置组件，支持单独修改单一属性
2. 通过缓存事实推演的随机实现、干预推演时回注的方式生成配对反事实孪生，可得到数值精准的个体处理效应
### 关键结果
在81种配置下测试8种因果发现算法、18种配置下测试4种处理效应估计器，发现标准因果发现方法对缺失值鲁棒性差，且存在边际方差捷径可通过标准化消除

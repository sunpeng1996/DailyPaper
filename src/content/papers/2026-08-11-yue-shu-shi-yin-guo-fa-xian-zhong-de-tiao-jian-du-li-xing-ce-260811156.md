---
title: 'Conditional Independence Tests for Constraint-Based Causal Discovery: A Survey'
title_zh: 约束式因果发现中的条件独立性测试研究综述
authors:
- Pavel Averin
- Theodoros Moysiadis
- Ioannis Katakis
affiliations:
- University of Nicosia
arxiv_id: '2608.11156'
url: https://arxiv.org/abs/2608.11156
pdf_url: https://arxiv.org/pdf/2608.11156
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 因果发现 · 条件独立性测试综述
tags:
- Causal Discovery
- Conditional Independence Test
- Constraint-based Method
- Survey
- High-dimensional Data
one_liner: 系统梳理6类条件独立性测试方法，关联测试特性与因果发现图误差，总结开源实现与待解挑战
practical_value: '- 做电商推荐/广告场景的因果消偏、特征因果关系挖掘时，可直接参考6类CI测试的适用场景选型，规避不同方法的固有缺陷

  - 处理高维、混合类型特征（用户属性离散+连续、行为数据多模态）的因果建模任务时，可复用文中提到的鲁棒性优化手段降低CI测试误差

  - 工程落地时可直接参考文中整理的Python/R现有库的CI测试实现，减少重复开发成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
约束式因果发现（PC、FCI等算法）的核心决策依赖条件独立性(CI)测试输出，但不同CI测试在高维、混合类型数据场景下的适用边界、鲁棒性、扩展性缺乏系统梳理，阻碍因果方法落地。
### 方法关键点
将主流CI测试划分为偏相关、列联表、回归、最近邻、核方法、机器学习驱动6大类，逐类分析其适配的数据分布与失效场景，直接关联CI测试层面的性能（如条件集增大时的功效衰减、I/II类误差不对称性）与因果图层面的骨架恢复、v结构定向误差。
### 关键结果
对比了主流R、Python库对各类CI方法的支持度，总结三大待解挑战：无需离散化的混合类型CI测试、小样本下的误差控制、CI测试的扩展性优化

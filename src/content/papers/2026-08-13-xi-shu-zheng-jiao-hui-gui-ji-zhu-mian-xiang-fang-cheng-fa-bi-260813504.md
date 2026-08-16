---
title: 'Sparse Orthogonal Regression Technique: A Spectral Framework for Equation
  Discovery, Approximation, and Integration'
title_zh: 稀疏正交回归技术：面向方程发现、逼近与积分的谱框架
authors:
- Sabin Roman
- Ljupco Todorovski
- Saso Dzeroski
affiliations:
- Department of Knowledge Technologies, Jožef Stefan Institute
- Faculty of Mathematics and Physics, University of Ljubljana
arxiv_id: '2608.13504'
url: https://arxiv.org/abs/2608.13504
pdf_url: https://arxiv.org/pdf/2608.13504
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 方程发现 · 稀疏正交回归谱框架
tags:
- Sparse Regression
- Orthogonal Basis
- Spectral Learning
- Equation Discovery
- System Identification
one_liner: 提出SORT稀疏谱框架，可从噪声非均匀采样数据学习正交基展开，支持方程发现、逼近与积分
practical_value: '- 电商用户行为时序、流量波动等序列建模可复用SORT的L1正则化正交基学习思路，降低噪声数据干扰

  - 稀疏采样业务数据（如用户间歇行为、区域零星单量）建模可参考其鲁棒系数估计方法，避免显式积分计算

  - 供需预测、转化率动态建模等动态系统类任务可借鉴其可复用中间谱表示思路，支撑下游多任务复用'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有数据驱动方程发现方法依赖有限预定义项库选择，泛化性差，在稀疏采样、带噪声、基不匹配场景下性能退化严重，且需显式积分或解析内积计算，适配性弱。

### 方法关键点
- SORT稀疏谱框架直接通过L1正则化回归从观测数据估计正交基展开系数，无需显式求积或解析内积计算；
- 先学习紧凑谱表示再指导简单解析形式搜索，将问题从通用项脆性选择转为面向领域的基设计。

### 关键结果
动态系统实验中，基适配时性能持平或优于基于库的稀疏回归基线；稀疏采样、导数估计噪声、表示不匹配场景下性能退化更稳定；低阶主导系数随模型阶数提升保持稳定，支持阶数一致的模型扩展，还可直接用于高维积分估计。

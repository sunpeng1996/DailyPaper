---
title: On the estimation and validity of AI time horizons---a statistical look at
  the METR plot
title_zh: AI时间地平线的估计与有效性：METR评估范式的统计视角
authors:
- Drew T. Nguyen
- William Fithian
affiliations:
- UC Berkeley Department of Statistics
arxiv_id: '2610.12466'
url: https://arxiv.org/abs/2610.12466
pdf_url: https://arxiv.org/pdf/2610.12466
published: '2026-10-08'
collected: '2026-10-11'
category: Eval
direction: AI能力评估 · 时间地平线度量
tags:
- AI Evaluation
- Item Response Theory
- Spline Fitting
- METR Benchmark
- Capability Measurement
one_liner: 采用样条与项目反应理论优化METR AI时间地平线估计，修正线性假设偏差并配套有效性诊断工具
practical_value: '- 搭建代码生成/任务执行类Agent内部Benchmark时，可借鉴该研究的非线性转换方法校准任务难度-人类耗时映射，避免线性假设带来的能力评估偏差

  - 评估Agent迭代效果时，可复用「样条拟合+项目反应理论」的评估范式，提升评估结果的置信度与跨版本可比性

  - 设定大模型/Agent业务迭代目标时，可参考「相同倍数时间跨度提升难度差异极大」的结论，合理匹配研发资源与预期'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有METR AI时间地平线评估默认任务AI难度与人类耗时对数呈线性相关，假设存在偏差，导致AI能力评估结果误差大，无法支撑合理的AI进展判断与迭代目标设定。
### 方法关键点
基于228个软件工程任务、26个AI模型的实测数据，引入样条拟合+项目反应理论框架，放松原线性假设，拟合人类耗时到AI难度的非线性转换函数，同时配套构念有效性诊断图。
### 关键结果
1. 转换函数在2-30分钟人类耗时区间几乎平坦，其余区间接近线性；相同10倍时间跨度下，3分钟到30分钟的能力提升难度远低于30分钟到5小时
2. 优化后的时间地平线点估计在交叉验证proper scoring规则下表现显著优于原方法

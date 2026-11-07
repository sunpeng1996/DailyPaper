---
title: 'TestBED: An Open-Source Toolkit for Bayesian Experimental Design'
title_zh: TestBED：面向贝叶斯实验设计的开源工具包
authors:
- Gavin Kerrigan
- Marcel Hedman
- Sahel Iqbal
- Tom Rainforth
affiliations:
- Department of Statistics, University of Oxford
arxiv_id: '2611.06633'
url: https://arxiv.org/abs/2611.06633
pdf_url: https://arxiv.org/pdf/2611.06633
published: '2026-11-04'
collected: '2026-11-07'
category: Other
direction: 贝叶斯实验设计 · 开源工具与基准测试
tags:
- Bayesian Experimental Design
- Open Source Toolkit
- Benchmarking
- Modular Design
- Intelligent Data Acquisition
one_liner: 开源模块化贝叶斯实验设计工具包，配套基准套件降低工业化落地门槛
practical_value: '- 电商/广告A/B实验优化场景可直接复用TestBED内置的期望信息增益估计实现，提升小流量实验的统计显著性，缩短实验周期

  - 推荐/广告策略冷启动阶段，可基于TestBED的模块化组件快速搭建贝叶斯最优采样流程，降低冷启动数据采集成本

  - 算法迭代基准对比流程可参考TestBED的解耦设计思路，将任务、目标、模型、评估模块拆分，提升算法迭代效率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
贝叶斯实验设计（BED）是智能数据采集的成熟框架，可覆盖科研、工业多场景落地需求，但现有BED方法均采用定制化代码实现，缺乏标准化软件与基准套件，导致方法复现、横向对比、扩展落地的门槛极高，限制了BED的工业化应用。
## 方法关键点
TestBED将BED全流程拆解为任务、优化目标、训练机制、策略架构、评估流程五大模块化可复用组件，内置期望信息增益估计等核心原语的高可扩展实现，支持组件自由组合：既可在统一框架下复现现有BED方法，也可快速搭建未经验证的新配置、新方法并完成评估。
## 关键结果
基于TestBED完成了当前主流BED方法的大规模基准测试，通过对照实验明确了策略架构中时间嵌入等易被低估的设计选择对效果的显著影响，可将新BED方法的开发验证周期从周级压缩至天级。

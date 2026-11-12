---
title: Time Series Change Point Detection with Gaussian Processes
title_zh: 基于高斯过程的时间序列变点检测方法
authors:
- Olga Isupova
- Danil Kuzin
- Fredrik Gustafsson
- Lyudmila Mihaylova
arxiv_id: '2611.13295'
url: https://arxiv.org/abs/2611.13295
pdf_url: https://arxiv.org/pdf/2611.13295
published: '2026-11-09'
collected: '2026-11-12'
category: Other
direction: 时间序列分析 · 变点检测
tags:
- Gaussian Process
- Change Point Detection
- Time Series
- Hypothesis Testing
- Anomaly Detection
one_liner: 提出基于高斯过程先验超参数变化判定的通用变点检测框架，支持离线/在线多变点检测
practical_value: '- 可直接复用至电商用户行为时序、流量时序的异常/突变点识别场景，无需提前预设变点前后的时序函数形式，大幅降低先验假设成本

  - 框架同时支持离线批量检测、在线实时检测双模式，可直接适配离线大盘趋势分析、在线流量异动告警两类业务需求

  - 基于统计假设检验的判定逻辑具备理论性能保证，可解释性远优于黑盒模型，适合风控、流量运营等需可解释结论的场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有时间序列变点检测方法多依赖数据分布、变点性质的强先验假设，或需提前明确变点前后的时序函数形式，泛用性差，在电商流量、用户行为这类非平稳时序上的适配成本极高。
### 方法关键点
1. 将变点定义为高斯过程先验的超参数变化，无需预设变点前后的时序函数形式，超参数直接从数据中学习；
2. 基于统计假设检验框架建模问题，提供可证明的性能理论保证；
3. 同时支持离线批量多变点检测、在线实时多变点检测两种部署模式。
### 关键结果
在合成数据集、公开真实数据集上的综合验证显示，该框架的检测准确率、运行效率均优于传统CUSUM等同类型基线方法。

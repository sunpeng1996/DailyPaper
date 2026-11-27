---
title: Change Point Detection with Generative Models
title_zh: 基于生成模型的变点检测方法
authors:
- Tigran Ramazyan
- Denis Derkach
- Mikhail Hushchyn
affiliations:
- HSE University
arxiv_id: '2611.34228'
url: https://arxiv.org/abs/2611.34228
pdf_url: https://arxiv.org/pdf/2611.34228
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 时间序列变点检测 · 生成式数据增广
tags:
- ChangePointDetection
- GenerativeModel
- TimeSeries
- DataAugmentation
- SampleEfficiency
one_liner: 通过生成模型增广时间窗口样本，解决窗口式变点检测的样本量瓶颈，提升检测效果
practical_value: '- 电商流量/交易/用户行为序列的变点检测场景，可复用生成式窗口增广思路解决小窗口样本量不足问题，提升异动识别准确率

  - 小样本时序分类任务中，可借鉴本方案用生成模型增广局部窗口数据，降低简单分类器的预测方差，无需上复杂深度模型即可提升效果

  - 线上实时变点检测场景，增广后用轻量分类器即可达标，可降低推理耗时，兼顾时序精度与算力成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
窗口式变点检测(CPD)是工业界时序异动识别的主流方案，存在固有样本量瓶颈：为保证时间精度需采用小窗口，小样本会导致CPD得分方差高、误判多，现有深度检测模型也无法从根本上解决该问题，落地成本高且效果不稳定。

### 方法关键点
不对检测模型做复杂改造，而是引入生成模型对时间窗口样本做生成式增广，在不扩大窗口尺寸、不损失时间精度的前提下，扩充有效数据量，稳定CPD得分分布，仅搭配简单分类器即可完成高精度检测。

### 关键结果
在合成数据与真实数据集上验证，增广后简单分类器效果显著超过复杂深度学习基线，整体CPD误判率大幅下降，推理成本仅为深度CPD模型的1/10以下

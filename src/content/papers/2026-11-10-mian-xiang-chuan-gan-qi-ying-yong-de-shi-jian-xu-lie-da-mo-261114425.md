---
title: Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models
  for Sensor Data Applications
title_zh: 面向传感器应用的时间序列大模型采样频率不变性量化
authors:
- Sourish Gunesh Dhekane
- Abinaya Kumar
- Torsten Woertwein
- Yan-Bo Lin
- Thomas Ploetz
- Shabnam Ghaffarzadegan
affiliations:
- Bosch Research (Bosch Center for Artificial Intelligence, USA)
- Georgia Institute of Technology, USA
arxiv_id: '2611.14425'
url: https://arxiv.org/abs/2611.14425
pdf_url: https://arxiv.org/pdf/2611.14425
published: '2026-11-10'
collected: '2026-11-12'
category: Eval
direction: 时间序列大模型 · 采样频率不变性评测
tags:
- Time-Series-Foundation-Model
- Sampling-Frequency-Invariance
- Model-Evaluation
- Sensor-Data
- Forecasting
one_liner: 首次将采样频率不变性作为TSFM核心评测维度，量化4款主流模型表现并给出落地指引
practical_value: '- 电商用户行为序列建模、销量/库存时序预测场景可复用本文的评测框架，测试序列模型在埋点上报频率变化、端侧采样异构场景下的鲁棒性，避免策略调整导致的效果掉点

  - 可将本文提出的FSI、FDI、CDI三类指标迁移到推荐系统序列模型鲁棒性评测，量化序列采样密度变化时的用户/物品嵌入偏移、排序预测效果退化程度

  - 选型TSFM落地电商时序类任务时，可参考本文的压力测试结论，优先选择SF不变性更优的模型，降低跨场景适配的微调成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传感器场景下时间序列大模型(TSFM)部署时普遍面临跨设备、跨运行模式的采样频率(SF)异构问题，现有TSFM评测体系未将SF不变性作为核心评估维度，无法支撑落地选型决策。
### 方法关键点
选取MOMENT、Chronos-2、Moirai-MoE、TimesFM 4款主流TSFM开展压力测试，从嵌入偏移、时序预测性能退化、下游任务性能退化3个维度，设计FSI、FDI、CDI 3个全新量化指标评估SF不变性。
### 关键结果
1. SF不变性核心由信号原生采样率与任务所需带宽的余量决定；
2. 不同TSFM的SF不变性差异显著，选型对鲁棒性表现有强解释性；
3. 低SF下的性能退化大部分源于信息损失，仅小部分来自模型本身能力缺陷。

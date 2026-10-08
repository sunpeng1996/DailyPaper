---
title: Towards Calibrated Probabilistic Forecasts for Events of Interest via Outcome-Conditional
  Recalibration
title_zh: 基于结果条件重校准的感兴趣事件概率预测校准方法
authors:
- Jakob Benjamin Wessel
- Sam Allen
affiliations:
- University of Leipzig, Institute for Meteorology
- Karlsruhe Institute of Technology, Institute of Statistics
arxiv_id: '2610.10076'
url: https://arxiv.org/abs/2610.10076
pdf_url: https://arxiv.org/pdf/2610.10076
published: '2026-10-07'
collected: '2026-10-08'
category: Other
direction: 概率预测校准 · 极端事件后处理优化
tags:
- Probabilistic_Forecast
- Calibration
- Post-hoc_Recalibration
- Extreme_Event
- Regression
one_liner: 提出面向用户自定义结果区域的后处理重校准方法，提升特定事件概率预测校准度
practical_value: '- 电商大促爆单、库存预警等极端事件概率预测可直接复用该后校准方法，在不损失整体预测准确率的前提下提升极端场景校准度

  - 推荐系统低概率高价值事件（如高客单转化、用户流失）的预估分校准，可采用分区域重校准思路，替代全局校准避免低概率区域误差被掩盖

  - 该方法无模型依赖，可直接接入现有任意概率预测pipeline，工程实现成本极低'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有后处理重校准方法易掩盖结果空间特定区域的校准误差，而极端事件等用户关注的特定结果的预测校准度直接影响决策有效性，全局校准无法满足这类场景需求。
### 方法关键点
提出结果条件重校准后处理方案，无模型依赖可适配任意预测分布：先对条件预测分布应用经典分位数重校准，再重缩放条件分布使预测事件概率匹配经验发生频率，输出各关注区域内均校准的连续有效预测分布。
### 关键结果
- 回归基准集上，相比现有条件/无条件重校准方法，目标区域校准度显著提升，整体校准度保持竞争力
- 日前电价预测任务中，负电价预测校准度大幅提升，预测准确率损失可忽略

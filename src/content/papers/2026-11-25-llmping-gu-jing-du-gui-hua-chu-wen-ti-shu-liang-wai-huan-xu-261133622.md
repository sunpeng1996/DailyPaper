---
title: 'How Many Sources, Not Just How Many Problems: Planning the Precision of LLM
  Evaluations from Earlier Results'
title_zh: LLM评估精度规划：除问题数量外还需考量来源数量
authors:
- Guang Qiu
affiliations:
- Department of Statistics, Florida State University
arxiv_id: '2611.33622'
url: https://arxiv.org/abs/2611.33622
pdf_url: https://arxiv.org/pdf/2611.33622
published: '2026-11-25'
collected: '2026-11-26'
category: Eval
direction: LLM评估方案优化
tags:
- LLM Evaluation
- Sampling Design
- Benchmarking
- Statistical Calibration
one_liner: 基于试点数据预测LLM评估中问题来源聚类对结果标准差的影响，给出可落地的评估采样校准方法
practical_value: '- 做LLM4Rec、电商Agent的离线能力评估时，不要仅堆砌测试case总量，需保证测试case来源（如用户query场景、商品类目、任务类型）的多样性，避免同来源case重复拉高结果方差

  - 可复用文中的设计效应校准方法，用少量试点测试数据预评估当前测试集的结果标准差，在固定评估预算下优化来源/问题数的采样比例，降低评估误差

  - 评估结果校验时，按case来源划分试点与留存集而非按难度划分，可大幅提升评估精度预估值的准确率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前LLM基准测试普遍存在同来源问题聚类现象（如同一模板衍生的数学题、同一仓库衍生的代码任务），仅控制问题总数的评估方案会导致结果标准差偏高、置信度不足，且无法提前预估评估精度。
### 方法关键点
复用经典设计效应公式，基于与测试集无关的试点数据估计组内相关系数，提前预测相同预算下不同来源/问题数分配方案的得分标准差；评估置信区间时用试点设计效应的平方根修正iid假设下的区间宽度。
### 关键结果数字
在GSM-Symbolic数据集上，10模板×10变体的100题评估标准差为9.2pp，是100个独立模板方案（2.7pp）的3.52倍，试点数据预测比值误差仅0.85%；SWE-bench上仅用3份提交的试点数据就能将预测误差控制在3%以内；修正后的置信区间在集中采样设计下pass@1的覆盖率提升至0.93-0.98。

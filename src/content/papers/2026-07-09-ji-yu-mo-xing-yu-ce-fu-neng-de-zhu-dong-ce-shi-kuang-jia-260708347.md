---
title: Prediction-Powered Active Testing
title_zh: 基于模型预测赋能的主动测试框架
authors:
- Kianoosh Ashouritaklimi
- Valentin Kilian
- Daolang Huang
- Tom Rainforth
- François Caron
affiliations:
- University of Oxford
- Aalto University
arxiv_id: '2607.08347'
url: https://arxiv.org/abs/2607.08347
pdf_url: https://arxiv.org/pdf/2607.08347
published: '2026-07-09'
collected: '2026-07-11'
category: Eval
direction: 模型风险评估 · 低标注主动测试
tags:
- Active Testing
- Risk Estimation
- Label Efficiency
- Unbiased Estimation
- Confidence Interval
one_liner: 结合无偏LURE估计器与预测驱动控制变量，实现标注高效的无偏低方差风险估计
practical_value: '- 电商/推荐模型离线评估时，可复用已有黑盒基线模型的预测结果作为控制变量残差化损失，在不引入评估偏差的前提下降低方差，减少人工标注测试样本的成本

  - 落地PPAT的自适应采样规则筛选需标注的测试样本，可比随机采样用少得多的标注量达到相同的评估置信度，适合大流量模型A/B测试的前置离线验证

  - 可复用其渐近正态性推导的置信区间方法，对推荐/搜索/广告模型的离线评估结果做不确定性量化，避免小样本标注导致的评估结果误判'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有主动测试方法做风险估计时未利用已有的黑盒模型预测信息，在标注成本高昂的场景下效率偏低，也无法给出可靠的评估不确定性量化结果。
### 方法关键点
1. 提出PPAT框架，结合无偏LURE估计器与预测驱动控制变量，通过残差化损失而非直接使用伪标签的方式，同时保证估计无偏性、降低方差；
2. 推导适配该估计器的最优及实用代理采样规则，定向筛选能最大程度降低估计方差的样本进行标注；
3. 证明其渐近正态性，可输出渐近有效的置信区间，实现评估结果的不确定性量化。
### 关键结果
在表格回归、图像分类任务上，PPAT风险估计效果优于所有现有基线；其置信区间达到目标覆盖率所需标注量远低于基线，区间宽度也更小。

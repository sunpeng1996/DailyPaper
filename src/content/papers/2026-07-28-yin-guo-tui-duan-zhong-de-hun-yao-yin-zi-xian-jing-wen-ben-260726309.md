---
title: 'The Confounder Trap: Treatment-Encoding Representations in Causal Inference
  with Text'
title_zh: 因果推断中的混淆因子陷阱：文本表征的处理效应编码问题
authors:
- Marie Neubrander
- Graham Tierney
- Alexander Volfovsky
affiliations:
- Duke University
arxiv_id: '2607.26309'
url: https://arxiv.org/abs/2607.26309
pdf_url: https://arxiv.org/pdf/2607.26309
published: '2026-07-28'
collected: '2026-07-30'
category: Other
direction: 文本因果推断 · 混淆因子消除
tags:
- Causal_Inference
- Text_Representation
- Confounder_Adjustment
- Masking
- Treatment_Effect_Estimation
one_liner: 提出掩码预处理方案消除文本处理信号，解决文本因果推断的表征诱导重叠失效问题
practical_value: '- 做电商评价、运营话术的因果效应评估（如好评对销量影响、客服话术对转化率影响）时，可先用掩码消除与处理变量直接相关的token，避免表征混淆处理信号与混淆变量，降低效应估计偏差

  - 基于用户评论、搜索Query构建因果用户画像/偏好建模时，可借鉴删除/替换掩码思路，过滤目标特征相关词汇，保留的上下文表征更贴合真实混淆因子分布

  - 大模型微调处理因果效应预测任务时，优先采用替换掩码方案保留语序与上下文，比直接删除特征词的效果更稳定，尤其适配长文本业务场景'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
文本因果推断场景（如评估电商评价、运营话术对用户行为的因果效应）中，现有方案直接从全文学习表征捕捉潜在混淆因子，但当处理效应本身由文本中特定词汇编码时，表征会直接混入处理信号，引发混淆因子陷阱：即使原始因果问题满足重叠假设，丰富的表征也会让处理组和对照组完全可分，违反重叠性要求，导致效应估计出现偏差。
### 方法关键点
1. 形式化定义了表征诱导的重叠失效问题；
2. 提出两类掩码预处理方案：删除掩码直接移除处理相关词汇，理论证明其对词袋/主题模型表征可保留重叠性；替换掩码用特殊token替换处理相关词，适配大模型场景，隐藏处理特征的同时保留语序与上下文信息。
### 关键结果
多组仿真实验验证，相比无掩码的基准调整方法，掩码方案可显著提升重叠诊断指标，稳定处理效应估计值，有效降低估计偏差。

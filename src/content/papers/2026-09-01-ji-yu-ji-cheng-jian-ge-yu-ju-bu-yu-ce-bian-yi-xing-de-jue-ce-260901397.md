---
title: 'Measuring consistency via ensemble margin and local prediction variability:
  Auditing decision systems in the presence of predictive multiplicity'
title_zh: 基于集成间隔与局部预测变异性的决策系统一致性审计方法
authors:
- Sinjini Banerjee
- Tim Marrinan
- Anand D. Sarwate
affiliations:
- Rutgers University
- Pacific Northwest National Lab
arxiv_id: '2609.01397'
url: https://arxiv.org/abs/2609.01397
pdf_url: https://arxiv.org/pdf/2609.01397
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: AI决策系统评估 · 预测多样性审计
tags:
- Rashomon Effect
- Ensemble Learning
- Consistency Audit
- Model Evaluation
- Predictive Multiplicity
one_liner: 提出结合集成间隔与局部预测变异性的一致性指标，审计存在预测多样性的决策系统
practical_value: '- 推荐/广告模型上线前一致性校验场景，可复用集成间隔+局部预测变异性的组合指标，识别易出错的待人工审核样本，降低bad case漏审风险

  - 用Rashomon集内多个同精度模型做集成审计，不需要太大的集成规模即可逼近全集合审计效果，工程上可基于现有多版本模型快速落地，算力开销可控

  - LLM4Rec/Agent决策系统鲁棒性评估场景，可直接套用该一致性度量方法，比现有指标更贴合预测多样性下的真实错误风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
机器学习Rashomon效应（同精度模型对相同输入输出不同预测）会导致决策系统错误漏审，现有研究多聚焦单模型内预测多样性，复杂集成决策系统下的审计方法存在缺口。
### 方法关键点
构建结合集成margin与单模型局部预测变异性的一致性评分，作为样本是否转人工审核的判定标准；理论证明有限集成的一致性评分随集成规模、局部变异性采样数增加，可收敛到Rashomon集期望模型的对应评分。
### 关键结果
对比单模型审计，Rashomon集模型集成审计可大幅降低错误预测漏检风险，仅带来中等幅度的人工审核量提升；中等规模有限集成即可逼近全Rashomon集审计效果，部分数据集下漏检风险接近0；该指标与现有成熟预测多样性度量的匹配度优于已有方案。

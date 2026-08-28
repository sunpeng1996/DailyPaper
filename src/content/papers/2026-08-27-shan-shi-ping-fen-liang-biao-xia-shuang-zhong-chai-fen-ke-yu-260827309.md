---
title: 'Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect:
  Evidence from a Pre-Registered LLM-Judge Audit'
title_zh: 删失评分量表下双重差分可产生伪效应：预注册LLM评审审计证据
authors:
- Shuyi Fan
- Boyuan Deng
- Mengyu Xu
- Xinhong Xie
- Chenyang Li
- Hongyang Zhang
affiliations:
- Columbia University
- Johns Hopkins University
- The University of Chicago
- The Pennsylvania State University
- The Hong Kong Polytechnic University
arxiv_id: '2608.27309'
url: https://arxiv.org/abs/2608.27309
pdf_url: https://arxiv.org/pdf/2608.27309
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: LLM评估 · LLM Judge审计方法校准
tags:
- LLM-Judge
- Difference-in-Differences
- Evaluation
- Censored-Scale
- Pre-registration
one_liner: 揭示有界评分量表下的双重差分设计会因删失干扰生成虚假的LLM评审偏好效应
practical_value: '- 用LLM Judge评估推荐/广告文案、Agent回复质量时，避免直接基于有界量表的双重差分做显著性检验，防止误判策略效果

  - 若需用双重差分分析LLM打分结果，先检验评分是否触及量表上下界，对删失数据做截断校正后再计算效应值

  - 内部审计业务策略效果（如用户分层对推荐满意度的LLM打分差异）时，优先预注册检验方法，补充pairwise偏好标注做交叉验证'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM Judge审计广泛采用「有界评分量表+双重差分」设计验证偏好偏差，该方法的统计有效性未被系统验证，频繁出现难以复现的假阳性显著结果。
### 方法关键点
1. 数理推导证明双重差分各分项会被自身删失比例衰减，当两个对比项距离量表边界距离不同时，共同的severity偏移会制造虚假交互效应；
2. 基于预注册的LLM教学评审审计（共990次调用）验证该机制，通过零偏好构造实验量化伪效应占比。
### 关键结果
1. 预注册主效应（学习者档案对评审脚手架偏好的影响）为null，效应值+0.085，p=0.684；
2. 名义显著的交互效应（+0.378，p=0.002）中79%~85%可完全由量表下界删失和severity偏移解释，无真实偏好贡献。

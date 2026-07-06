---
title: Adapting CCDF Plots for Visualizing Ordinal Regression Results
title_zh: 适配CCDF图用于序回归分析结果可视化
authors:
- Abhraneel Sarma
affiliations:
- Graz University of Technology
arxiv_id: '2607.01747'
url: https://arxiv.org/abs/2607.01747
pdf_url: https://arxiv.org/pdf/2607.01747
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 序回归结果可视化 · 统计分析工具优化
tags:
- Ordinal Regression
- CCDF
- Data Visualization
- Likert Scale
- Statistical Analysis
one_liner: 提出改进型互补累积分布函数图mCCDF，降低序回归结果可视化与结论传递门槛
practical_value: '- 电商/推荐A/B测试的用户满意度Likert量表分析，可替换原有ANOVA+柱状图的方案，采用序回归+mCCDF可视化，结论更严谨且直观

  - 用户分层反馈（差评/一般/好评等有序分类）的模型效果评估，引入mCCDF可快速定位不同群体的分布差异

  - 多目标排序的有序标签（点击/加购/下单等序级）模型分析，用mCCDF替代传统混淆矩阵做bad case快速排查'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
序回归对Likert量表等有序数据的假设比线性模型、ANOVA更宽松，适合用户调研、满意度评估等场景，但因结果可视化难度高、结论传递不直观，行业普及率极低。
### 方法关键点
对互补累积分布函数（CCDF）做针对性改造得到mCCDF，专门适配序回归模型的输出结构，可直观展示不同分组下各有序分类的概率分布差异。
### 关键结果
无需将有序数据强行假设为连续度量值，即可传递和传统分析方法完全一致的核心结论，大幅降低序回归的落地应用门槛。

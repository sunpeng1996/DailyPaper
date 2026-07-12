---
title: 'ImputeViz: A Visual Analytics Dashboard for Diagnosing Missing Data and Comparing
  Imputation Methods'
title_zh: ImputeViz：缺失数据诊断与插补方法比对可视化分析面板
authors:
- Aitik Dandapat
- Lalith Punepalle Raveendrareddy
- Mithilesh Kumar Singh
- Klaus Mueller
affiliations:
- Stony Brook University
arxiv_id: '2607.08579'
url: https://arxiv.org/abs/2607.08579
pdf_url: https://arxiv.org/pdf/2607.08579
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 缺失值插补 · 可视化分析工具
tags:
- missing_data
- imputation
- visual_analytics
- gKNN
- data_preprocessing
one_liner: 提出集成式可视化分析面板ImputeViz，支持缺失值诊断、插补模型配置与跨方法效果比对
practical_value: '- 推荐特征工程场景可借鉴其跨插补方法对比的MAE/RMSE/运行时间指标框架，快速选型适配业务的插补方案

  - 处理带地理位置的用户/商家特征时，可复用gKNN方法，融合空间距离与社会经济特征做插补，提升特征质量

  - 搭建特征工程工具时可参考结果缓存、锁定坐标轴刻度的设计，降低方法切换时的用户认知成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
科研、公共卫生等领域普遍存在缺失数据问题，易导致分析偏差，现有工具难以同时支持缺失模式诊断、多插补方法效果比对与溯源分析。
### 方法关键点
1. 集成MICE、Random Forest、XGBoost、kNN等主流插补方法，提供热图、共缺失摘要、分布诊断等可视化组件，可识别MCAR/MAR/MNAR等缺失模式
2. 提出融合社会经济与空间距离的gKNN插补变体，支持溯源显示插补结果的贡献区域，实现可解释的插补 accountability
3. 内置跨方法对比面板，输出MAE、RMSE、运行时间等指标，支持变量级差异分析，采用单方法结果缓存、坐标轴锁定设计降低认知负担
### 关键结果
案例验证显示该工具可帮助分析师快速选择有效插补策略、识别敏感变量、评估模型鲁棒性

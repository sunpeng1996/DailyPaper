---
title: 'Impression Share Prediction: An Offline Evaluation Task for Ranking Systems'
title_zh: 曝光占比预测：面向排序系统的离线评估任务
authors:
- Mohsen Malmir
- Houssam Nassif
- Danish Nasir Shaikh
- Taher Rahgooy
- Murat Ali Bayir
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2608.16872'
url: https://arxiv.org/abs/2608.16872
pdf_url: https://arxiv.org/pdf/2608.16872
published: '2026-08-17'
collected: '2026-08-18'
category: Eval
direction: 排序系统离线评估 · 反事实预测
tags:
- Offline-Evaluation
- Ranking-System
- Impression-Share
- Counterfactual-Prediction
- Auction-Dynamics
one_liner: 提出曝光占比预测离线评估任务，结合因果框架与时序编码器预判新排序模型上线后的曝光分配偏移
practical_value: '- 上线新排序/广告模型前，可基于模型的预测分数分布+当前系统运力（容量、pacing乘数、活动数）特征，预判不同优化目标的曝光占比，提前拦截会导致高优先级目标（如转化）曝光占比下降的劣化模型，降低A/B试错成本

  - 针对从未上线过的全新模型预测不准的冷启动问题，可借鉴PatchTST风格的时序编码器，摄入最近2小时的拍卖运力动态数据，相比仅用瞬时快照的模型，首小时预测L1误差可提升42%以上

  - 做离线指标建设时，不要只看AUROC、GAUC等预测精度指标，需补充曝光占比类的分配指标，避免出现离线指标涨但线上高价值目标曝光被挤压、整体收益下降的情况'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统排序/广告模型的离线评估仅依赖AUROC、GAUC等预测精度指标，无法预判模型上线后在共享拍卖、运力pacing等系统因素影响下的曝光分配偏移，常常出现离线指标上涨但高优先级优化目标（如转化）的曝光占比被挤压、最终线上收益下降的问题，目前没有方法能在A/B测试前提前识别这类偏移。

### 方法关键点
- 基于结构因果模型（SCM）建模排序模型状态、系统运力状态、曝光占比的因果关系，证明模型状态不受系统运力影响，无需逆倾向加权等复杂操作即可从观测数据识别反事实效应
- 预测框架输入两类特征：一是候选模型的预测分数直方图、均值/方差、支持的优化目标覆盖向量，二是系统各优化目标的总容量、已消耗容量、剩余容量、pacing乘数、活动数等运力特征
- 针对全新模型冷启动预测失效问题，设计基于PatchTST的编码器条件架构：用Transformer编码最近2小时的分钟级运力时序数据，再结合模型特征输出24小时曝光占比预测

### 关键实验结果
基于Meta内部150个不同家族的排序模型、5周的分钟级快照数据测试，对比固定均值基线：
- 训练集中见过的模型：随机森林使用全特征集，L1误差降低48.6%
- 从未见过的新模型上线首小时：仅用瞬时快照的随机森林比基线差20.5%，而加入2小时时序编码的架构L1误差较基线降低22.1%，相对随机森林提升42.6个百分点

最值得记住的一句话：排序模型的线上效果不仅取决于预测精度，其预测分数分布带来的不同优化目标间的曝光分配偏移，对最终收益的影响往往被严重低估。

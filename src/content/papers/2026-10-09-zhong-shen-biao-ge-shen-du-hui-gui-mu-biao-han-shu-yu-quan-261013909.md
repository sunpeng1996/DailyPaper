---
title: 'Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early
  Stopping'
title_zh: 重审表格深度回归：目标函数与全局早停的局限性
authors:
- Danil Rudenko
- Georgii Bulgakov
- Nikolay Kartashev
- Ivan Rubachev
- Daniil Krasylnikov
- Artem Babenko
affiliations:
- Yandex Research
- BRAInLab
- HSE University
arxiv_id: '2610.13909'
url: https://arxiv.org/abs/2610.13909
pdf_url: https://arxiv.org/pdf/2610.13909
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 表格深度学习 · 回归训练优化
tags:
- TabularDeepLearning
- RegressionLoss
- EarlyStopping
- QuantileLoss
- Heteroskedasticity
one_liner: 系统测评表格深度回归损失函数，提出感知异方差的改进分位数损失，指出全局早停的局限性
practical_value: '- 电商推荐/广告的CTR/CVR、用户价值预估等回归任务可直接替换MSE为分位数损失，无需大幅调参即可获得稳定效果提升

  - 训练回归模型时避免盲目使用全局早停，可针对不同噪声水平的样本子群分别设置早停阈值，减少不同子群的效果折衷

  - 针对用户行为标签噪声不均的场景，可复用输入依赖的标签平滑技巧优化分位数损失，进一步提升异方差场景下的回归精度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格深度回归任务的损失函数选型缺乏统一测评基准，不同研究的结论受数据集、backbone、测评协议影响难以复用，且主流全局早停策略未考虑样本异方差带来的最优训练epoch差异问题，易造成不同噪声子群的效果折衷。
### 方法关键点
跨10+公开表格数据集、5+主流表格深度学习backbone系统测评MSE、分位数损失等10余种回归目标函数；针对全局早停的局限性，设计融合输入依赖标签平滑的异方差感知分位数损失。
### 关键结果数字
多数改进损失相对调优后的MSE增益不稳定或低于1%，分位数损失相对MSE在所有测试backbone上均获得平均2.3%的精度提升；改进的异方差感知分位数损失相对原生分位数损失进一步获得平均1.7%的精度提升，有效缓解全局早停带来的不同噪声样本子群的效果折衷。

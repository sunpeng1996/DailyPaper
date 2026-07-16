---
title: 'Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters'
title_zh: Hindcast：基于预测市场回测的无泄漏LLM预测能力评估框架
authors:
- Xiao Ye
- Jacob Dineen
- Evan Zhu
- Shijie Lu
- Kevin Song
- Ben Zhou
affiliations:
- School of Computing and Augmented Intelligence, Arizona State University
arxiv_id: '2607.14051'
url: https://arxiv.org/abs/2607.14051
pdf_url: https://arxiv.org/pdf/2607.14051
published: '2026-07-15'
collected: '2026-07-16'
category: Eval
direction: LLM预测评估 · 信息泄漏防控
tags:
- LLM Evaluation
- Forecasting
- Information Leakage
- Prediction Market
- Backtesting
one_liner: 提出阻断训练/检索信息泄漏的Hindcast框架，解决LLM预测能力评估误将记忆认作预测能力的问题
practical_value: '- 做时间敏感类任务（电商大促预测、流行趋势预判、热点选品）的Agent离线评估时，可复用按任务设时间cutoff、冻结历史数据快照的方法，避免未来信息泄漏导致评估虚高

  - 构建RAG增强的趋势预测类应用时，可参考结论：先判断检索库是否存在事件前置有效讨论，仅在有有效信息时触发RAG，避免无价值推测内容拉低效果

  - 推荐/搜索系统的离线A/B测试可借鉴该思路，按测试任务粒度设置数据时间窗口，杜绝特征穿越问题，提升评估结果可信度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM预测能力回测存在两类信息泄漏：一是RAG可能检索到事件发生后的报告，二是新模型训练数据常包含过往预测任务的真实结果，导致评估实际测试的是记忆而非预测能力，结果严重失真。
### 方法关键点
1. 按每个预测任务单独设置时间截止点$t_0$，冻结$t_0$前的公开Reddit数据作为唯一检索源，禁止模型访问$t_0$后的数据，同时控制训练数据时间窗口阻断两类泄漏
2. 基于已结算的Polymarket预测市场构造测试集，同时用真实事件结果、$t_0$时刻的市场预测价格两个维度打分，基准对齐人类基于同期信息的预测结果
3. 数据集快照固定，可随模型迭代持续复用评估，不会过时
### 关键结果
阻断泄漏后，RAG仅在Reddit存在事件前置讨论的场景下对多数模型有增益；若存档仅有无依据猜测，RAG反而会降低预测准确率

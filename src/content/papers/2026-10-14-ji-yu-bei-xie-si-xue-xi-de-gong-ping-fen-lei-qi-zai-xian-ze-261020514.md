---
title: Bayesian Learning to Select Fair Classifiers
title_zh: 基于贝叶斯学习的公平分类器在线选择方法
authors:
- Saatvik Kher
- Hyungrok Do
- Judy Zhong
- Padhraic Smyth
affiliations:
- University of California, Irvine
- New York University
- Weill Cornell Medicine
arxiv_id: '2610.20514'
url: https://arxiv.org/abs/2610.20514
pdf_url: https://arxiv.org/pdf/2610.20514
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent在线选择 · 多目标公平决策
tags:
- Bayesian Optimization
- Thompson Sampling
- Multi-Armed Bandit
- Fairness
- Online Learning
one_liner: 将在线流场景下公平分类器选择建模为贝叶斯多臂老虎机，平衡精度与子群公平性且支持标签延迟
practical_value: '- 电商/广告场景的多模型路由可复用该框架，将精度、不同人群曝光公平性、调用成本作为多臂老虎机的reward维度，快速迭代出最优路由策略

  - 支持标签延迟的Thompson Sampling实现可直接复用到冷启动Agent/分类器的在线评估场景，无需等待全量标签即可完成模型择优

  - 多目标（性能+公平）平衡的贝叶斯更新逻辑可迁移到流量分配、人群定向策略的在线优化，规避离线评估的分布偏移问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统分类器/Agent批量评估要求所有候选对全量测试样本打标，成本极高，无法适配在线流场景下的标签延迟、精度与敏感属性子群公平性多目标权衡需求，离线批量评估结果往往和线上实际表现存在分布偏移。
### 方法关键点
将在线公平分类器选择问题建模为贝叶斯多臂老虎机问题，基于Thompson Sampling实现自适应查询策略：每轮根据当前观测到的精度、子群公平性指标的后验分布选择最优Agent，待延迟返回的真实标签可用后更新对应后验分布，持续迭代优化选择策略。
### 关键结果
在表格分类器、LLM、人类标注三类真实场景数据集上验证，相比现有基线方法实现大幅regret降低，同时提供精度与公平性双维度的性能理论保证。

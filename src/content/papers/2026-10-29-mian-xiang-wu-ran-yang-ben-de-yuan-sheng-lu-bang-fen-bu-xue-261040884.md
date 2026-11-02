---
title: Robust-by-Design Distributional Learning from Contaminated Samples
title_zh: 面向污染样本的原生鲁棒分布学习方法
authors:
- Nevena Gligić
- Arya Farahi
affiliations:
- Department of Statistics and Data Science, The University of Texas at Austin
- NSF-Simons AI Institute for Cosmic Origins
arxiv_id: '2610.40884'
url: https://arxiv.org/abs/2610.40884
pdf_url: https://arxiv.org/pdf/2610.40884
published: '2026-10-29'
collected: '2026-11-02'
category: Training
direction: 分布学习 · 污染样本鲁棒训练
tags:
- Distributional Learning
- Robust Training
- MMD
- Noisy Data
- Sample Contamination
one_liner: 设计CC-MMD估计器，仅需少量审计标注即可校正污染样本的分布学习偏差
practical_value: '- 推荐系统召回/排序训练遇到爬虫/低质污染样本时，可复用「少量审计标注+全量proxy分数校正」框架，无需丢弃大部分低质数据，提升训练样本利用率

  - 生成式推荐（GenRec）训练时，若训练语料/物品特征存在大量污染，可替换原生MMD loss为CC-MMD，无需假设污染分布即可对齐干净目标分布，降低生成结果偏差

  - 处理用户行为噪声标注时，可借鉴CC-MMD的无校准假设校正逻辑，降低对噪声标签校准度的要求，减少人工标注成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前大规模数据集多由爬虫、自动过滤生成，常存在未知分布的样本污染，传统方法要么忽略污染拟合错误目标，要么仅保留小部分可信样本浪费大量数据。

### 方法关键点
CC-MMD（污染校正最大均值差异）估计器，结合全量样本的噪声成员分数与小部分审计精确标签的残差校正，无需对proxy分数做校准假设、也无需对污染分布做结构假设（仅需满足常规核正则性），即可还原仅用干净样本计算的oracle MMD。

### 关键结果
理论上证明校正后的核和有限总体设计无偏、审计校正项渐近正态、对目标MMD一致；实验中污染占比提升时CC-MMD始终接近oracle表现，污染回归任务的参数恢复与预测效果显著提升，重度污染混合集训练的生成模型可完美恢复干净目标分布。

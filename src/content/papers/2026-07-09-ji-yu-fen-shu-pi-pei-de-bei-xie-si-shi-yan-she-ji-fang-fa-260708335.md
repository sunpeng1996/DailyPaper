---
title: Bayesian Experimental Design via Score Matching
title_zh: 基于分数匹配的贝叶斯实验设计方法
authors:
- Angus Phillips
- Gavin Kerrigan
- Tom Rainforth
affiliations:
- Department of Statistics, University of Oxford
arxiv_id: '2607.08335'
url: https://arxiv.org/abs/2607.08335
pdf_url: https://arxiv.org/pdf/2607.08335
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 贝叶斯实验设计 · 训练效率优化
tags:
- BED
- Score Matching
- EIG
- Policy Optimization
- Training Efficiency
one_liner: 解耦贝叶斯实验设计EIG双重不可解问题，将策略训练的乘法级计算成本转为加法级
practical_value: '- 电商/广告AB实验策略迭代时，可复用解耦思路：将实验信息增益评估的复杂计算预训练为独立模块，降低策略调优、超参搜索的重复计算成本

  - Agent多轮决策策略迭代场景下，这种将核心评估目标与策略训练解耦、乘法成本转加法的设计，可大幅降低多策略对比训练的开销

  - 涉及EIG（期望信息增益）优化的任务（如推荐系统主动探索、冷启动样本选择），可直接复用「先训独立分数匹配模型再优化策略」的流程'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
基于策略的贝叶斯实验设计（BED）可基于历史数据学习自适应深度决策网络，但核心优化目标期望信息增益（EIG）存在双重不可解问题，需依赖高成本近似计算，严重限制策略调优、架构搜索、多策略迭代等场景的效率。
### 方法关键点
1. 将EIG的双重不可解计算与策略学习完全解耦，先训练和当前策略无关的分数匹配模型，得到通用的EIG近似分数；
2. 用预训练的分数近似结果训练策略，将原本策略训练阶段的乘法级计算成本转化为加法级，显著降低策略迭代的计算负担。
### 关键结果
训练多个竞争策略时无需承担似然评估的乘法级成本，即使不执行额外的超参搜索或架构搜索，仅通过最优策略选择即可直接提升效果。

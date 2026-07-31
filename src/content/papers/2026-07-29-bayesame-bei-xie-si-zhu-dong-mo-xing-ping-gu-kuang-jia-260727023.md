---
title: 'BayesAME: Bayesian Active Model Evaluation'
title_zh: BayesAME：贝叶斯主动模型评估框架
authors:
- Paula Cordero Encinar
- Taylan Cemgil
- Arnaud Doucet
- Virginia Aglietti
- Silvia Chiappa
affiliations:
- Imperial College London
- Google DeepMind
arxiv_id: '2607.27023'
url: https://arxiv.org/abs/2607.27023
pdf_url: https://arxiv.org/pdf/2607.27023
published: '2026-07-29'
collected: '2026-07-31'
category: Eval
direction: 大模型评测 · 主动采样coreset优化
tags:
- Model Evaluation
- Coreset
- Bayesian Model
- Active Sampling
- Generative Model
one_liner: 提出可自动确定coreset大小的贝叶斯主动评估框架，大幅降低生成式模型基准评估成本
practical_value: '- 可复用BayesAME的自动coreset大小确定逻辑，优化推荐/大模型离线A/B评测的采样规模，降低计算成本

  - 可借鉴信息增益驱动的样本选择策略，替代随机采样做模型效果评测，相同样本量下评估准确度更高

  - 多目标扩展的性能相关性建模思路可复用，同时评测多个召回/排序模型时进一步压缩测试样本量

  - 用连续log-likelihood替代二元打分做评估指标的结论可直接复用，提升生成式推荐/Agent回复的评测精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
大生成模型全量基准评测耗时与算力成本极高，现有coreset采样评估方法需人工指定样本量，无法自适应匹配精度优先级与效率要求。

### 方法关键点
1. 提出序贯贝叶斯评估框架BayesAME，对具备相同历史模型表现的item组定义latent ability，引入目标模型与历史模型行为相似性的联合先验
2. 基于latent ability后验输出性能估计、量化不确定性，通过信息增益准则迭代选择新增coreset样本，直到估计波动、不确定性低于用户预设阈值自动停止，无需人工指定样本量
3. 支持多目标扩展，建模多个目标模型间的性能相关性，进一步压缩所需coreset规模

### 关键结果
多基准实验显示BayesAME效果显著优于现有方法的序贯适配版本；验证非随机coreset选择效果优于随机采样，回应了领域现有质疑；采用连续响应log-likelihood替代传统二元打分，评估估计精度大幅提升。

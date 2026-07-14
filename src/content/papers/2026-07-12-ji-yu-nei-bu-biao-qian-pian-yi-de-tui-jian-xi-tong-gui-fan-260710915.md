---
title: Normative Alignment of Recommender Systems via Internal Label Shift
title_zh: 基于内部标签偏移的推荐系统规范对齐方法NAILS
authors:
- Johannes Kruse
- Kasper Lindskow
- Michael Riis Andersen
- Ryotaro Shimizu
- Julian McAuley
- Pierre-Alexandre Mattei
- Jes Frellsen
affiliations:
- JP/Politikens Media Group
- Technical University of Denmark
- University of California San Diego
- Inria, Université Côte d'Azur
- Copenhagen Business School
arxiv_id: '2607.10915'
url: https://arxiv.org/abs/2607.10915
pdf_url: https://arxiv.org/pdf/2607.10915
published: '2026-07-12'
collected: '2026-07-14'
category: RecSys
direction: 推荐系统全局规范对齐·轻量后处理
tags:
- Recommender-Systems
- Alignment
- Post-processing
- Label-Shift
- Fairness
- Diversity
one_liner: 无需重训原有推荐模型，通过后处理加权实现全局规范目标对齐，对用户参与度影响极小
practical_value: '- 无需重训现有推荐模型，仅在排序层对item的所属属性（品类、价格带、内容赛道等）做加权调整，即可快速落地平台级品类分布管控，适配电商大促规则、内容平台编辑价值观等场景

  - 可通过超参数λ灵活调节对齐强度与用户体验的平衡，当目标分布接近用户自然偏好时（如电商货架占比分布），甚至可小幅提升AUC，避免生硬调控导致的指标下跌

  - 相比传统贪心重排方法CaliRec，NAILS计算成本极低，仅需预计算每个item的加权系数，推理时直接叠加logit即可，适配高QPS线上推荐场景

  - 若需要提升长尾商品/内容曝光，可设置更均衡的目标分布，搭配NAILS-stoch采样策略可实现100%候选池覆盖率，缓解推荐马太效应'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统单纯优化用户参与度，容易出现品类分布失衡、马太效应、不符合平台/社会规范目标的问题，传统校准方法多以用户为中心，无法满足平台级全局对齐需求，且多需要重训模型或复杂重排，落地成本高。

### 方法关键点
- 将全局规范对齐问题转化为内部层级分类的标签偏移问题，假设item给定属性下的用户偏好分布不变，仅对属性的边际分布做调整
- 仅在原有推荐模型输出的`pθ(i|u)`基础上，乘以预计算的属性加权系数`w_i=Σc (p̃(c)/p(c) * p(c|i))`，再做归一化即可得到对齐后的排序分数
- 新增超参数λ∈[0,1]混合原始分数与对齐后分数，灵活调节对齐强度；提供确定性排序（NAILS-det）和概率采样（NAILS-stoch）两种推理模式

### 关键实验
在EB-NeRD新闻推荐数据集（3700万impression、100万+用户）上测试，base模型为NRMS，对比基线为CaliRec：
1. 对齐编辑目标分布时，λ=0.7下NAILS-det的KL散度0.054、覆盖率92.3%，AUC仅下降0.3%，最优λ下AUC甚至小幅超过基线
2. 对齐均匀分布时，NAILS-stoch实现100%候选覆盖率，KL散度0.0143，AUC下降控制在2%以内，远高于CaliRec77.4%的覆盖率

### 核心结论
推荐系统的规范对齐不需要以大幅牺牲用户体验为代价，选择贴合用户自然偏好的目标分布，甚至可以实现对齐效果和参与度的双赢

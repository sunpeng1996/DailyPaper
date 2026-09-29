---
title: Recommendation Ranking Off-Policy Evaluation under Ranking-Dependent Examination
  via Examination-Relevance Decomposition
title_zh: 基于曝光-相关性分解的排序依赖场景推荐排序离策略评估
authors:
- Riki Okamura
- Toshiharu Sugawara
affiliations:
- Waseda University
arxiv_id: '2609.35034'
url: https://arxiv.org/abs/2609.35034
pdf_url: https://arxiv.org/pdf/2609.35034
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 推荐排序 · 离策略评估去偏
tags:
- Off-Policy Evaluation
- Ranking
- Click Model
- Doubly Robust
- Recommender System
one_liner: 提出两种基于点击分解的无偏OPE estimator，ED-DR在大样本排序依赖场景下MSE最低
practical_value: '- 电商搜索/推荐的排序策略离线评估，当曝光受相邻商品影响（比如爆品引流周边）时，可引入ED-DR estimator降低OPE偏差，避免线上A/B测试风险

  - 点击建模可复用曝光-相关性分解思路，相关性模型可跨位置pooling数据，显著提升长尾item的相关性估计精度

  - 线上流量充足的大样本场景优先用ED-DR，小样本/用户浏览符合强cascade行为（比如信息流短平快浏览）场景仍用现有RIPS/cascade DR更合适

  - 日志策略需保留一定随机性（避免温度τ0过低），否则曝光概率无法识别，所有基于权重的OPE方法都会出现方差爆炸'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐排序OPE方法假设曝光仅依赖位置，当曝光受排序全局影响（比如高吸引力的头部商品挤占后续商品曝光）时，无法区分未曝光和曝光后未点击，会产生严重偏差，导致离线评估结果和线上效果不一致，而线上A/B测试成本高、影响用户体验，亟需适配排序依赖曝光场景的无偏OPE方案。

### 方法关键点
- 基于经典点击模型将点击拆解为曝光O和相关性R两个独立隐变量，点击Y=O*R，其中曝光e_k可依赖全量排序，相关性r仅和当前位置item有关
- 提出LE-IIPS estimator：在IIPS权重基础上引入评估策略和日志策略的曝光概率比值，修正排序依赖场景下的IIPS偏差
- 扩展得到ED-DR estimator：结合doubly robust框架，只要曝光概率估计准确就无偏，或在排序无关曝光场景下即使模型估计不准也无偏，相关性估计误差仅影响方差不影响偏差
- 用回归EM估计曝光和相关性模型，搭配cross-fitting降低过拟合风险

### 关键实验
采用合成数据集，对比IIPS、RIPS、cascade DR、AIPS等7个baseline，在排序依赖曝光场景下，大样本（n>1600）时ED-DR相对MSE比IIPS低38%，比DR-IIPS低12%；仅在小样本（n<400）、强cascade行为（ρ→1）、日志策略接近确定性（τ0<0.2）场景下表现弱于现有方法。

排序依赖曝光场景下的OPE偏差主要来自曝光估计误差，相关性估计误差不会引入偏差，大样本下优先选择考虑全局排序曝光的ED-DR estimator。

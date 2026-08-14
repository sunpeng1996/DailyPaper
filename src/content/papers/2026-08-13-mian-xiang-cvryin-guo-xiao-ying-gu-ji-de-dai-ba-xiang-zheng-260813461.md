---
title: Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization
title_zh: 面向CVR因果效应估计的带靶向正则化双鲁棒方法
authors:
- Jiayi Dan
- Bo Li
- Lu Deng
- Yong Wang
affiliations:
- Tsinghua University
- Tencent Inc.
arxiv_id: '2608.13461'
url: https://arxiv.org/abs/2608.13461
pdf_url: https://arxiv.org/pdf/2608.13461
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: CVR因果效应估计 · 双鲁棒学习
tags:
- Causal Inference
- Doubly Robust
- CVR Estimation
- Targeted Regularization
- Uplift Modeling
one_liner: 针对CVR因果估计的选择偏差问题，提出带靶向正则化的双鲁棒框架，兼顾理论保障与落地可行性
practical_value: '- 业务侧做CVR因果效应评估（如优惠券、营销活动效果）时，不要仅使用点击样本建模，可复用本文推导的双鲁棒修正项，纳入全量样本消除选择偏差

  - 低CTR场景下优先选用靶向正则化的软修正方案替代传统DR的硬修正，避免CTR作为分母过小导致的数值爆炸，无需交叉拟合，工程落地更简单

  - 可直接复用多任务联合训练CTR+CVR因果效应的架构，共享特征底座不增加额外推理成本，同时保证μ2<μ1的业务合理性约束

  - 不要迷信损失去偏思路，直接面向最终CVR因果估计量设计损失，比间接用IPS加权损失的方案效果提升更显著，有理论保障'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
电商广告场景中，CVR因果效应估计是优惠券投放、营销策略评估的核心依据，现有方案存在两大痛点：一是仅用点击样本建模引入严重选择偏差，二是基于损失去偏的方法无理论保证最终估计量无偏，无法满足业务决策的高准确性要求。

### 方法关键点
- 基于半参数理论推导适配CVR链式结构的双鲁棒估计器，仅要求CTR、转化概率、倾向得分3个 nuisance参数达到n^-1/4收敛，即可实现最终估计的√n一致性，可容忍神经网络等非参数模型的估计误差
- 设计适配CVR估计量的靶向正则化项，用低维可学习参数ϵ替代传统DR的硬修正，避免低CTR场景下分母过小导致的数值不稳定，无需交叉拟合，支持端到端训练
- 构建多任务框架联合估计CTR和CVR的因果效应，共享特征底座，且显式约束μ2=μ1*μ'2保证μ2<μ1符合业务逻辑

### 关键实验
在合成数据、News半合成数据、CRITEO真实数据集上对比DragonNet、VCNet、ECUP等7个主流基线，合成数据上CVR估计AMSE较最优基线ECUP低69.6%，News数据集上AMSE低56.7%，CRITEO真实数据集上AUUC较最优基线ECUP高16%。

### 核心结论
CVR因果估计的核心是直接面向最终估计量设计修正方案，仅对损失去偏无法保证最终估计的无偏性，双鲁棒软正则化是兼顾效果和稳定性的落地最优选择。

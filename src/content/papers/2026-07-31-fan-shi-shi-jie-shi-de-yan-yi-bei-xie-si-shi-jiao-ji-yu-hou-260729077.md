---
title: 'A Generalized-Bayes Perspective on Counterfactual Explanations: Posterior-Based
  Decision-Making and Evaluation'
title_zh: 反事实解释的广义贝叶斯视角：基于后验的决策与评估
authors:
- Keita Kinjo
affiliations:
- Kyoritsu Women’s University
arxiv_id: '2607.29077'
url: https://arxiv.org/abs/2607.29077
pdf_url: https://arxiv.org/pdf/2607.29077
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 反事实解释 · 广义贝叶斯决策框架
tags:
- Counterfactual Explanation
- Generalized Bayes
- MAP
- CVaR
- Model Multiplicity
one_liner: 将距离最小化反事实解释统一到广义贝叶斯框架，提出新决策规则、多模型融合及评估方法
practical_value: '- 可将DP-GBCE框架迁移到电商推荐的算法救济场景，给用户输出可落地的行动引导（如调整消费门槛、收货地址）提升转化

  - 风险厌恶型CVaR-CE决策规则可用于高风险推荐场景（如信贷、保险相关商品推荐），降低解释失效概率

  - 多模型后验融合方法可解决多召回排序模型并存下的反事实解释一致性问题，避免不同模型给出冲突解释'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统反事实解释（CE）普遍采用距离最小化形式，但缺乏统一理论支撑，且现有方法大多仅输出单个最优解释，未考虑决策风险、多模型并存等实际场景问题。
### 方法关键点
1. 证明距离最小化CE等价于广义贝叶斯框架下带距离先验的Gibbs后验MAP估计，提出统一框架DP-GBCE
2. 扩展出两类新决策规则：最小化期望损失的贝叶斯决策、风险厌恶型CVaR-CE
3. 支持基于贝叶斯模型权重融合多模型后验分布，解决多模型性能接近时的解释一致性问题，同时定义了单CE及后验分布的完整评估指标
### 关键结果
在模拟数据与Google Trends数据集上完成验证，量化了不同决策规则间的性能权衡，证明了框架的通用性和有效性

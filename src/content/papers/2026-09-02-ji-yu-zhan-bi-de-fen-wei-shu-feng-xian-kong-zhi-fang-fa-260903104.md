---
title: Occupancy-based Quantile Risk Control
title_zh: 基于占比的分位数风险控制方法
authors:
- Zihao Shi
- Huajun Xi
- Bingyi Jing
- Hongxin Wei
affiliations:
- Southern University of Science and Technology
- Mohamed bin Zayed University of Artificial Intelligence
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2609.03104'
url: https://arxiv.org/abs/2609.03104
pdf_url: https://arxiv.org/pdf/2609.03104
published: '2026-09-02'
collected: '2026-09-05'
category: Other
direction: 可信机器学习部署 · 风险控制
tags:
- Conformal Risk Control
- Quantile Risk
- Finite-sample Guarantee
- Trustworthy ML
- Risk Bound
one_liner: 提出OQRC分位数风险控制方法，解决现有方案过保守或无有限样本保证的缺陷
practical_value: '- 推荐/广告模型上线前的风险校验可引入OQRC框架，在有限样本下严格控制预估误差、误推风险的分位数阈值，避免过保守的规则导致性能损耗

  - 对于LLM生成推荐文案、Agent决策的风险控制场景，可复用其损失空间分箱+占比估计的思路，在保证风险不超阈值的前提下最大化生成/决策灵活度

  - 可复用其收敛速度证明思路，为业务端风险控制策略的样本量需求提供理论依据，减少校准数据投入'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有分位数风险控制方法要么过度保守导致性能损耗，要么缺乏严谨有限样本保证，无法满足高风险场景下模型可信部署的要求

### 方法关键点
1. 将风险控制转化为有限占比问题，用排序后的校准损失对损失空间分箱
2. 估计测试损失在各分箱的分布，取每个分箱内的最大损失作为风险上界
3. 选择参数λ使得风险上界以1-δ的高概率不超过预定义阈值α

### 关键结果
理论上证明有限样本下风险控制边界收敛到最优界的速率为$
\mathcal{O}_p(n^{-1/2})
$，通用基准实验中最高降低78.64%的风险gap

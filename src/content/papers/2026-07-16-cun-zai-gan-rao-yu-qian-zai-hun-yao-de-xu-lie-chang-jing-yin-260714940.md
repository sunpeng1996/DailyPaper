---
title: Causal Inference for Sequential Settings under Interference and Latent Confounding
title_zh: 存在干扰与潜在混淆的序列场景因果推断方法
authors:
- Phevos Paschalidis
- Constantinos Daskalakis
- Devavrat Shah
affiliations:
- MIT
- EECS
- LIDS
- CSAIL
- IDSS
arxiv_id: '2607.14940'
url: https://arxiv.org/abs/2607.14940
pdf_url: https://arxiv.org/pdf/2607.14940
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 序列场景因果推断 · 干扰与混淆处理
tags:
- Causal Inference
- Sequential Modeling
- Latent Confounding
- Interference
- MPLE
one_liner: 提出基于MPLE的高效估计方法，实现序列观测场景下带干扰与潜在混淆的因果量准确估计
practical_value: '- 电商/推荐场景中存在用户间社交干扰、未观测混淆因子（如区域消费趋势）时，可借鉴Ising模型+低秩潜在混淆结构建模因果效应，避免SUTVA假设不成立导致的A/B测试结果偏差

  - 多群体序列策略效果评估（如不同运营策略对多区域用户的长期转化影响）可复用MPLE高效参数估计方案，降低高维序列因果建模的计算成本

  - 跨区域运营策略归因时，可参考单样本高维分布因果估计思路，无需多组重复实验即可得到相对可靠的因果结论'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有因果推断普遍依赖SUTVA假设，无法处理序列观测场景中单元间存在干扰、同时存在未观测潜在混淆因子的情况，这类场景在社交传播、公共政策、电商区域运营中广泛存在。
### 方法关键点
1. 用Ising模型建模N个单元T时间步的二进制结果依赖关系，外部场同时捕捉treatment效应与潜在混淆因子，潜在混淆采用低秩因子结构建模
2. 基于最大伪似然估计（MPLE）实现高效参数学习，仅需单样本高维分布数据即可完成估计
### 关键结果
1. 温和假设下参数估计具备非渐近一致性，采样后得到的因果量估计偏差可控
2. 美国郡县疫苗率对新冠死亡率的真实案例验证了方法有效性，合成实验中参数估计误差随样本量提升稳定下降

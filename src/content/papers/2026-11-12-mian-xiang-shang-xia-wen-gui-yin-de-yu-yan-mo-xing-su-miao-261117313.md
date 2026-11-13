---
title: Sketching Language Models for Context Attribution
title_zh: 面向上下文归因的语言模型素描算法研究
authors:
- Christopher Liaw
- Aranyak Mehta
- Grigoris Velegkas
- Felix Zhou
affiliations:
- Google Research
- Yale University
arxiv_id: '2611.17313'
url: https://arxiv.org/abs/2611.17313
pdf_url: https://arxiv.org/pdf/2611.17313
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 大语言模型 · 上下文归因优化
tags:
- Context_Attribution
- Sketching_Algorithm
- Leave_One_Out
- Query_Complexity
- LLM_Optimization
one_liner: 提出低复杂度上下文归因LOO值估算方法，证明匹配的理论复杂度下界
practical_value: '- 做RAG/LLM推荐的prompt归因时，可复用该算法替代逐token评估，大幅降低调用开销，尤其适合长prompt的用户兴趣归因、query归因场景

  - 稳定性假设下的泰勒系数衰减验证结论，可直接用于约束LLM推理的归因误差，适配推荐系统的prompt特征重要性打分需求

  - 前向微分作用于反向传播电路的trick，可迁移到小样本LLM微调的梯度估算场景，降低梯度计算的资源开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
计算prompt各token的leave-one-out（LOO）上下文归因值，逐token评估需O(n)次LLM调用，长prompt场景下开销极高，现有素描方法复杂度仍达Õ(log(n)/ε²)，落地成本高。
### 方法关键点
基于泰勒系数满足稳定性条件的算术电路素描框架，创新性将前向微分作用于反向传播电路，仅需同阶泰勒度前向素描的常数级开销，大幅降低估算方差。
### 关键结果
满足稳定性假设下，仅需O(√(log(1/ε))/ε)次模型调用即可将所有LOO值误差控制在ε量级，同时证明该复杂度为理论下界；实验验证泰勒系数衰减符合稳定性假设，在小规模LLM检索任务上效果匹配理论预期。

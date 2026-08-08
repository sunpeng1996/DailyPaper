---
title: 'Hypothesis Testing with Conditional Queries: Learnability and the Value of
  Interaction'
title_zh: 带条件查询的假设检验：可学习性与交互价值
authors:
- Zonghuan Xu
affiliations:
- Fudan University
arxiv_id: '2608.06262'
url: https://arxiv.org/abs/2608.06262
pdf_url: https://arxiv.org/pdf/2608.06262
published: '2026-08-06'
collected: '2026-08-08'
category: Eval
direction: 模型评估 · 自适应测试效率对比
tags:
- Hypothesis Testing
- Adaptive Evaluation
- Query Complexity
- Learnability
- Distribution Testing
one_liner: 量化条件查询假设检验中自适应交互相比非自适应测试的查询效率优势为二次级
practical_value: '- 做LLM/推荐系统离线评估时，可参考本文非自适应查询构造方法，用O(N²(T+log(1/ρ)))的查询量逼近自适应评估效果，降低交互工程成本

  - 交互评估仅能带来二次级查询效率提升，业务上无需过度追求多轮交互的指数级增益，可平衡工程复杂度和评估精度做取舍

  - 做A/B测试、分布差异校验时，可参考类间条件概率分离度判据，判断两类分布是否可被可靠区分，避免无效测试'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前模型评估存在静态非自适应、交互式自适应两种模式，二者的可学习性边界、查询效率差异缺乏明确的理论量化结论，尤其缺少条件查询场景下的严格推导。
### 方法关键点
在大小为N的有限结果空间下的条件查询假设检验框架内，首先推导两类分布可被可靠区分的充要条件，其次构造可逼近自适应测试效果的随机非自适应查询策略，再匹配下界推导二者的最坏情况自适应差距。
### 关键结果数字
1. 可学习性充要条件为两类分布的成对条件概率存在正分离度，分离度为0时任意有限查询预算下最坏误差恒为1/2；
2. 非自适应策略仅需O(N²(T+log(1/ρ)))次查询即可在总变差ρ内逼近T轮自适应策略的效果；
3. 最坏情况固定误差下的自适应差距为Θ_ε(N²)，交互仅能带来二次级查询量降低，无指数级优势。

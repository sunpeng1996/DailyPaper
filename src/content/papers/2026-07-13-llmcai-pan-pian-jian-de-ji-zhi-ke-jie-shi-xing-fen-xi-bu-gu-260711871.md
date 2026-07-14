---
title: 'Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge
  Bias'
title_zh: 《LLM裁判偏见的机制可解释性分析：不公平评估的内在原理》
authors:
- Zixiang Xu
- Sixian Li
- Huaxing Liu
- Xiang Wang
- Shuai Li
- Zirui Song
- Xiuying Chen
affiliations:
- Alibaba Group
- Mohamed bin Zayed University of Artificial Intelligence
- University of Southern California
- University of Michigan, Ann Arbor
arxiv_id: '2607.11871'
url: https://arxiv.org/abs/2607.11871
pdf_url: https://arxiv.org/pdf/2607.11871
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: LLM可解释性 · LLM-as-Judge 偏差治理
tags:
- LLM-as-Judge
- Mechanistic Interpretability
- Bias Mitigation
- Activation Geometry
- Representation Learning
one_liner: 从隐层激活几何角度揭示LLM裁判偏见的底层机制，支持偏差干预与失效预判
practical_value: '- 做Agent自动评测、生成式推荐结果打分时，可通过隐层线性投影提前识别LLM裁判的失效样本，大幅降低评测结果误差

  - RLHF训练中Reward Model的偏差优化，可直接干预偏差子空间对应的隐层激活，修正打分的成本远低于prompt调优且效果更可控

  - 电商场景下LLM商品文案审核、商家评级等大模型落地场景，可复用低维偏差子空间识别+隐层投影的方案治理偏差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM-as-Judge偏差研究仅聚焦输入输出层面，通过扰动输入、调整prompt缓解偏差，缺乏底层机制解释，无法实现精准的偏差干预与失效预判。

### 方法关键点
从隐层激活的几何结构角度分析偏见机制：识别不同类型偏差对应的低维专属子空间，通过沿该子空间调整隐层状态实现偏差的因果控制，基于偏差方向特征的线性投影实现裁判失效预判。

### 关键结果
跨7个LLM裁判、7种偏差类型、9个基准测试验证：①沿偏差子空间正向偏移可让干净输入产生偏差打分，反向偏移可消除偏差输入的打分偏移，效果比随机方向高1个数量级；②基于偏差特征的线性投影对3个完全unseen基准的裁判失效预判效果，显著优于文本类基线方法。

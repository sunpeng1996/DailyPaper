---
title: Training Stability under Adaptive Curricula
title_zh: 自适应课程学习下的训练稳定性研究
authors:
- Johan Obando-Ceron
- Walter Mayor
- Michael Dennis
- Aaron Courville
- Pablo Samuel Castro
affiliations:
- Mila – Québec AI Institute
- Université de Montréal
- CIFAR
- Google DeepMind
arxiv_id: '2611.08787'
url: https://arxiv.org/abs/2611.08787
pdf_url: https://arxiv.org/pdf/2611.08787
published: '2026-11-05'
collected: '2026-11-09'
category: Training
direction: 自适应课程学习 · RL训练稳定性优化
tags:
- Reinforcement_Learning
- Adaptive_Curriculum
- UED
- Training_Stability
- Zero_Shot_Generalization
one_liner: 揭示UED自适应课程训练中RL智能体的三类退化问题，证明优化学习者稳定性可提升长程性能与零样本泛化能力
practical_value: '- 做基于课程学习的推荐Agent、广告出价Agent训练时，不要仅优化课程设计，需同步监控参数膨胀、表征多样性下降两类退化指标，提前干预避免性能停滞

  - 针对长周期训练的个性化推荐模型、多模态检索Agent，可复用本文的退化缓解手段，无需改动训练数据分布即可提升长程泛化性能，降低交互采样成本

  - 采用自适应负采样、自适应困难样本挖掘的推荐排序场景，可参考本文将学习者训练稳定性作为核心设计指标，补充到现有课程类优化框架中'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前UED自适应课程学习领域研究均聚焦课程构造逻辑，未关注学习者自身训练稳定性对最终效果的影响，长周期训练下普遍存在性能停滞、泛化能力下降的问题。
### 方法关键点
覆盖多类UED机制、不同环境复杂度、超长训练周期场景，系统识别出三类学习者侧的退化病理：参数无意义膨胀、价值-结果排序错乱、表征多样性丧失，明确上述问题与优化失效的强关联，针对性设计退化缓解干预方案。
### 关键结果
在不修改课程规则、不增加环境交互量的前提下，优化学习者稳定性可有效提升长程训练性能与零样本泛化能力，证明学习者可训练性是UED框架的核心互补设计原则。

---
title: Challenges in Evaluating Explanation Methods for Static and Evolving Data
title_zh: 静态与演化数据场景下XAI可解释方法的评估挑战
authors:
- Jerzy Stefanowski
affiliations:
- Poznan University of Technology, Institute of Computing Sciences, Poland
arxiv_id: '2608.06351'
url: https://arxiv.org/abs/2608.06351
pdf_url: https://arxiv.org/pdf/2608.06351
published: '2026-08-06'
collected: '2026-08-07'
category: Eval
direction: XAI可解释性评估 · 演化数据流适配
tags:
- XAI
- Evaluation
- Counterfactuals
- Concept Drift
- Debiasing
one_liner: 梳理XAI可解释方法在静态、含概念漂移的演化数据流场景下的评估痛点与核心挑战
practical_value: '- 评估推荐/广告模型的XAI解释时，可参考文中human-grounded评估范式，替代纯离线指标，提升解释的用户接受度

  - 应对电商实时流数据的概念漂移（如大促前后用户偏好突变）时，可复用反事实解释适配思路，动态更新解释逻辑

  - 迭代模型版本时可参考数据-模型-解释协同追踪框架，保障解释结果一致性，规避合规风险'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前XAI可解释方法缺乏统一有效的评估体系，在高风险决策场景以及存在概念漂移的演化数据流场景下，解释的可靠性、时效性、适配性无法得到保障，严重制约可信AI落地。
### 方法关键点
1. 以DetoxAI图像识别系统为案例，梳理偏见检测、概念遗忘场景下XAI解释的现有评估局限性；
2. 引入human-grounded评估范式用于图像分类解释的效果验证；
3. 探索演化数据流下的解释适配方法，总结反事实解释在概念漂移场景的落地经验；
4. 提出数据、模型、解释三者协同追踪的核心研究挑战。
### 关键结果
本文为观点类综述，无公开量化实验结果，核心是梳理了XAI评估领域的四类未解决问题，为后续评估体系设计提供了清晰的研究框架。

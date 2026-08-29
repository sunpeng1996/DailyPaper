---
title: 'ICON Decomposition: Multivariate Concept-Level Explanations of Deep Representations
  for Model Auditing'
title_zh: ICON分解：面向模型审计的深度表示多变量概念级解释
authors:
- Roshan Prakash Rane
- Marco Simnacher
- Manuel Pfeuffer
- Marc-Andre Schulz
- Nys Tjade Siegel
- Maximilian Dreyer
- Frederik Pahde
- Wojciech Samek
- Sonja Greven
- Kerstin Ritter
affiliations:
- Hertie Institute for AI in Brain Health, University of Tübingen
- Charité - Universitätsmedizin Berlin
- Humboldt-Universität zu Berlin
- Fraunhofer Heinrich Hertz Institute
- Technische Universität Berlin
arxiv_id: '2608.26083'
url: https://arxiv.org/abs/2608.26083
pdf_url: https://arxiv.org/pdf/2608.26083
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: 可解释AI · 模型特征审计
tags:
- XAI
- Concept Explanation
- Model Auditing
- Shortcut Learning
- Spurious Correlation
one_liner: 提出多变量概念解释方法ICON，消除概念相关性干扰，精准识别模型实际依赖的特征用于审计
practical_value: '- 排查推荐/广告模型的shortcut学习问题时，可借鉴ICON的多变量校正思路，避免把特征间相关性误判为模型实际依赖的信号

  - 做模型特征重要性归因时，可复用「控制其他变量+任务输出后计算单个特征解释方差占比」的逻辑，提升归因结果可信度

  - 开展模型合规审计（如排查是否依赖性别、地域等敏感特征）时，ICON的稀疏解释输出可降低审计工作量'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于概念的可解释方法单独评估单概念解码性，易将概念间相关性误判为模型依赖该概念的证据，无法精准识别shortcut学习（即模型利用训练数据伪关联）问题，不适用于高风险场景的模型审计。
### 方法关键点
1. ICON分解框架计算单概念对网络层表示方差的解释度时，先校正其余所有概念与任务输出的影响，消除概念相关性干扰；
2. 可量化所有给定概念无法解释的表示占比，输出稀疏的概念重要性结果。
### 关键结果数字
- 合成数据集上概念重要性恢复精度优于7种基线方法；
- 皮肤病变、脑影像场景下成功分离模型真实依赖的概念，解释结果经重训练、分布外测试验证有效。

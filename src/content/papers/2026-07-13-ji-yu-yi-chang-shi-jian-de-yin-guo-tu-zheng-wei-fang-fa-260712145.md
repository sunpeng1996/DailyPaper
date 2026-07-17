---
title: Falsifying Causal Graphs With Outlier Events
title_zh: 基于异常事件的因果图证伪方法
authors:
- William Roy Orchard
- Philipp M. Faller
- Dominik Janzing
affiliations:
- University of Cambridge
- Karlsruhe Institute of Technology
- Amazon Research
arxiv_id: '2607.12145'
url: https://arxiv.org/abs/2607.12145
pdf_url: https://arxiv.org/pdf/2607.12145
published: '2026-07-13'
collected: '2026-07-17'
category: Reasoning
direction: 因果推理 · 因果图可靠性评估
tags:
- Causal Graph
- Outlier Detection
- Causal Reasoning
- Statistical Test
- Falsification
one_liner: 基于弱异常极少引发强异常原则，提出无需ground truth的候选因果图证伪统计检验方法
practical_value: '- 推荐/广告系统的链路故障、用户行为异常根因分析可复用「弱异常极少引发强异常」原则，优化现有根因定位逻辑

  - 构建业务因果图（如流量转化链路、用户决策路径）时，可引入该统计检验验证候选图合理性，降低专家经验偏差

  - 仅需单个异常样本即可完成检验，适配电商大促、突发事件等少样本场景下的因果链路正确性校验'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有因果图学习或专家构造的因果图缺少ground truth时，无法验证其正确性，是因果方法落地业务的核心瓶颈。
### 方法关键点
1. 反向复用根因分析领域的「弱异常极少引发强异常」原则，判断候选因果图隐含的异常传播规则是否与实际观测数据匹配，以此证伪错误因果图
2. 提出首套针对「候选因果图为真实因果图」假设的统计检验框架
### 关键结果
检验方法具备可控的假阳性率，对错误因果图的识别能力有理论保障，仅需单个异常样本即可运行

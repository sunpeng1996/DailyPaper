---
title: Trust Guided Decision Transformer
title_zh: 信任引导的决策Transformer（TGDT）模型
authors:
- Chainesh Gautam
- Raghuram Bharadwaj Diddigi
- Chandramouli Kamanchi
- Pankaj Dayama
- Sumanta Mukherjee
- Kameshwaran Sampath
affiliations:
- International Institute of Information Technology Bangalore
- IBM Research Bangalore
arxiv_id: '2609.31586'
url: https://arxiv.org/abs/2609.31586
pdf_url: https://arxiv.org/pdf/2609.31586
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent序列决策 · 上下文可靠性校准
tags:
- Decision Transformer
- Conformal Prediction
- Context Selection
- Offline RL
- Sequence Decision Making
one_liner: 基于滚动状态预测误差校准筛选可信上下文，解决Decision Transformer长推理序列性能衰减问题
practical_value: '- 序列推荐场景可复用滚动预测误差方法筛选用户最近的可信行为子序列，解决长行为序列分布漂移拉低推荐效果的问题，无需改动模型结构即可上线

  - split conformal prediction校准方法可直接迁移到离线场景的模型可靠性阈值设定，比如广告召回bad case阈值、推荐结果相关性阈值，仅需holdout数据无需额外标注

  - 基于LLM的Agent决策流程可参考「先筛可信上下文再做价值排序」的逻辑，替换现有先生成候选再校验的流程，大幅降低不可信上下文带来的决策错误'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Decision Transformer（DT）长序列推理时，自生成的上下文会逐步偏离训练分布（rollout context mismatch），导致性能骤降，现有仅靠价值排序或硬重置上下文的方案无法兼顾可靠性和决策效果。

### 方法关键点
1. 用模型自身滚动下一状态预测误差作为上下文可靠性的直接可观测信号，通过split conformal prediction在离线holdout数据上校准可信误差阈值；
2. 推理时先枚举多个最近上下文后缀，仅保留误差低于阈值的可信后缀，再用冻结critic从可信后缀生成的动作中选价值最高的，反转了现有先选动作再校验的逻辑，避免不可信上下文生成的动作干扰决策。

### 关键结果
在D4RL导航、运动任务上验证：单靠状态预测、critic引导、硬上下文重置仅能解决部分问题；TGDT相比原生DT、硬重置上下文控制、仅价值导向上下文选择三类基线，持续高误差运行占比显著下降，累计回报实现一致提升。

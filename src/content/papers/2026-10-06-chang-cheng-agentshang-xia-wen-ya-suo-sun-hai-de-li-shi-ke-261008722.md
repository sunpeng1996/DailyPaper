---
title: Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded
  Effect on the TRACE Paired-Replay Corpus
title_zh: 长程Agent上下文压缩损害的历史可预测性研究：TRACE语料库实证
authors:
- Egor Pakhomov
- Erik Nijkamp
affiliations:
- Salesforce AI Research
arxiv_id: '2610.08722'
url: https://arxiv.org/abs/2610.08722
pdf_url: https://arxiv.org/pdf/2610.08722
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 长程Agent · 上下文压缩优化
tags:
- Long-Horizon Agent
- Context Compaction
- TRACE Corpus
- Trigger Policy
- Agent Evaluation
one_liner: 基于TRACE语料库实证Agent前置行为对上下文压缩损害的预测效果有限，给出选择性压缩策略基准
practical_value: '- 电商导购/客服Agent等长会话场景做上下文压缩时，优先规避首次压缩、前置历史短、最近有执行错误、上条返回结果为空的高风险场景，这类场景压缩损害率可达70%~90%

  - 可复用风险-覆盖率评估思路做选择性压缩：在保留80%以上压缩机会的前提下，简单2特征策略就能规避20%左右的有害压缩，平衡token成本和执行效果

  - 做压缩触发特征工程时，注意「是否有写操作」这类标签本质是轨迹阶段的代理变量，需和前缀长度、压缩次数做混淆控制，不能直接作为因果特征使用

  - 评估压缩策略效果可借鉴TRACE的成对回放设计，同一个边界同时测试压缩/不压缩的执行差异，避免任务成功率这类粗指标的干扰'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长程Agent普遍依赖固定规则（如token阈值）做上下文压缩，完全忽略Agent当前执行状态，经常导致执行错误、重复调用等问题，但此前没有方法能精准预测压缩时机的损害，也缺乏反事实评估基准。

### 方法关键点
- 基于TRACE公开语料库的590个AppWorld任务压缩边界数据，每个边界都有压缩（POST）和不压缩（PRE）两种场景的成对回放结果，损害指标定义为压缩后新增的错误调用+重复调用之和dU@3
- 对比三类触发策略：简单决策树、2特征逻辑回归（是否有写操作+最近错误数）、梯度提升模型（17个工程特征/144个细粒度特征），采用任务级五折交叉验证，核心指标为压缩机会保留率、有害压缩规避率
- 以同一边界的拆分回放结果作为上限基准，衡量模型可达到的预测天花板

### 关键结果
- 2特征逻辑回归在保留83.7%压缩机会的前提下，可规避20.6%的有害压缩，仅比随机规则高4.4个百分点；最优144特征提升模型held-out AUROC仅0.66，远低于拆分回放的上限0.72
- 业界常用的「前置是否有写操作」特征本质是轨迹阶段的代理变量，控制前缀长度、压缩次数后对损害无预测效果

> 最值得记住的一句话：当前可观测的Agent前置行为对压缩损害的预测效果非常有限，优先规避已知的高风险场景比训练复杂触发策略的投入产出比更高

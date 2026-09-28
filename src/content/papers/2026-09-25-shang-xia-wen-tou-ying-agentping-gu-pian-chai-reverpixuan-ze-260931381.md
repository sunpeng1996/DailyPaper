---
title: 'Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context
  Projection'
title_zh: 上下文投影Agent评估偏差：ReVerPi选择性上下文投影案例研究
authors:
- Guangzhe Zhang
affiliations:
- Independent AI Researcher
arxiv_id: '2609.31381'
url: https://arxiv.org/abs/2609.31381
pdf_url: https://arxiv.org/pdf/2609.31381
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent上下文管理 · 评估方法论
tags:
- ContextProjection
- AgentEvaluation
- MemoryManagement
- SelectiveContext
- EfficiencyOptimization
one_liner: 揭示仅统计完成配对会掩盖Agent上下文投影的真实效果，提出严谨的分层评估方法
practical_value: '- 做Agent上下文压缩/投影优化时，不得剔除触发资源上限（token/请求次数/超时）的失败样本，仅统计成功完成的任务会严重高估优化收益，业务A/B测必须纳入全量触发策略的样本

  - 上下文效率优化的收益不能仅看单轮token减少，需统计全链路交互次数、总逻辑token、KV cache命中率变化：投影压缩可能触发多轮检索/工具调用，导致总资源消耗反而上升

  - 策略selector评估必须严格拆分拟合集与非拟合集，论文中基于历史字节的投影selector在非拟合集上比全上下文多8.6% token消耗、多1次失败，避免把拟合收益当成通用效果

  - 多组策略对照实验需为每组预留独立资源配额，不得因其中一组先失败就中止另一组执行，否则会引入缺失数据偏差，无法准确估计策略的真实表现'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent上下文投影通过压缩旧工具观测减少输入token，是降低推理成本的常用方案，但现有评估普遍只统计两组都完成的配对任务，刻意忽略触发资源上限（如请求次数、token限制）的失败案例，导致收益被严重高估，甚至会选到实际效果更差的策略。
### 方法关键点
- 构建ReVerPi框架，基于Pi编码Agent harness扩展历史存档能力，在相同任务前缀节点分叉为全上下文（F）、投影上下文（P）两组执行，配置12次请求上限、≥10KiB且曝光2次以上的观测才触发投影的规则
- 采用分层分析方法，区分拟合集、边界任务（触发投影的任务）、联合成功层（两组均成功的任务）三类样本，用部分识别区间处理未执行的配对任务结果，避免缺失数据干扰
- 全维度统计请求次数、逻辑token总量、缓存分类token、成功率，避免单维度token减少的误导
### 关键实验
基于86次源码阅读任务、共641次模型请求的实验：
- 仅统计15组完成配对时，F/P成功率均为12/15，看似持平；纳入全部27组边界任务后，P的成功率区间比F低33.3pp到高3.7pp，最多仅领先1个任务
- 11组联合成功任务中，P总逻辑token减少25%，但中位数token增加29%，总请求次数从35升至55（+57%）
- 拟合的投影selector在13组非拟合任务上，比全上下文多1次失败，多消耗8.6%逻辑token

最值得记住的一句话：Token reduction is not cost reduction，上下文优化的效果必须在完整资源约束下、覆盖所有触发策略的任务做全链路评估。

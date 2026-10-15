---
title: 'BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent
  Systems'
title_zh: BLADE：面向LLM多智能体系统的失败归因审计框架
authors:
- Xiaoguang Guo
- Yaohao Long
- Chuxu Zhang
affiliations:
- University of Connecticut
arxiv_id: '2610.18780'
url: https://arxiv.org/abs/2610.18780
pdf_url: https://arxiv.org/pdf/2610.18780
published: '2026-10-13'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体系统 · 失败归因优化
tags:
- MultiAgent
- FailureAttribution
- LLM
- DependencyTracing
- TrainingFree
one_liner: 训练免的LLM多智能体失败归因框架，通过审计信息使用而非仅依赖追踪提升准确率
practical_value: '- 电商导购、广告策略制定等多Agent协同场景可复用BLADE的「依赖追踪+交接审计」思路，快速定位流程失败的责任节点，降低调试成本

  - 无需训练的架构可直接落地，用业务现有LLM替代Jev做结构化多分类判断，无需额外标注数据即可搭建归因能力

  - 选择性审计设计仅检查Top2高概率依赖的交接点，可减少77%~87%的审计调用量，适合线上高并发Agent流程监控场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM多智能体系统通过角色分工、工具调用协同完成复杂任务，但错误会在多Agent间传播，仅追踪信息依赖无法区分错误是上游传入还是当前节点引入，快速定位首个决定性错误、分配责任是多Agent落地的核心痛点，现有方法要么需要训练、要么依赖全量轨迹重放，成本高准确率不足。

### 方法关键点
- 训练免架构分三步：首先重构执行轨迹的依赖图，用多分类判断识别事件间的依赖、重复、矛盾、修复四类关系，保留概率≥0.3的边；
- 基于依赖概率选Top2高概率的上下游交接点做审计，判断信息使用类型（忠实使用、错误引入、错误传播、修复等），构建责任归因图；
- 全局可推翻诊断，所有步骤均保留为候选，不限制最终归因范围，结合全量轨迹和责任图输出首个决定性错误节点。

### 关键实验
在1228条失败轨迹（覆盖Who&When、Who&When Pro 5个子集，含自然失败和注入失败，覆盖Magentic-One、DyLAN、MetaGPT三类多Agent架构）上和7种现有方法对比，BLADE的step准确率达57.6%，比最强基线All-at-once高5.6个百分点，仅需审计13%~23%的交接点即可达到或超过全量审计效果，全数据集推理成本仅约1.9美元。

### 核心结论
仅追踪信息来源不足以定位错误，审计信息的使用方式才是多Agent失败归因的核心。

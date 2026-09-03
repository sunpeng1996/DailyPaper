---
title: Adaptive Test-Time Inference for Text2Cypher with Trace Budgeting and Selective
  Refinement
title_zh: 面向Text2Cypher的带迹预算与选择性优化的自适应测试时推理
authors:
- Makbule Gulcin Ozsoy
affiliations:
- Neo4j
arxiv_id: '2609.02324'
url: https://arxiv.org/abs/2609.02324
pdf_url: https://arxiv.org/pdf/2609.02324
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: LLM测试时推理 · 自适应预算分配
tags:
- Text2Cypher
- Test-Time Inference
- Adaptive Computation
- Query Generation
- LLM Optimization
one_liner: 为Text2Cypher提出自适应测试时推理策略，动态分配预算+选择性纠错，大幅降本保效
practical_value: '- 可复用轻量规则式难度分级方案：通过关键词（聚合/比较/多跳/长度等）预判定用户请求复杂度，动态调整Best-of-N采样预算，可直接迁移到电商Query生成、用户意图理解、搜索推荐的候选生成环节降本

  - 可借鉴选择性纠错策略：仅对高难度请求和过滤空结果触发执行引导的自纠错流程，避免简单请求的冗余推理开销，适合智能导购Agent、电商知识库查询、订单查询等交互场景

  - 纠错模块可跨模型家族复用：无需与生成模型同系列，可选用低成本小参数模型做统一纠错器，降低部署和推理成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Text2Cypher等Text2Query任务的测试时推理普遍采用固定候选生成预算与全量纠错策略，未区分请求复杂度，既导致简单请求浪费大量计算资源，也可能因高复杂度请求预算不足降低生成质量，全量纠错进一步加剧了冗余开销，亟需自适应策略在保障生成质量的前提下降低推理成本。
### 方法关键点
- 自适应迹预算：通过轻量规则提取输入请求的9类二进制复杂度特征（聚合/最高级/比较/时序/多跳/否定/属性过滤/长度/命名实体），求和得到难度分后划分为易/中/难三级，分别匹配不同的候选生成数量，难度预估开销仅0.07ms/请求。
- 选择性执行引导纠错：仅对过滤阶段的空输出、中/高难度请求触发执行验证流程，若执行失败则将错误反馈输入小参数修正模型生成优化后的查询，简单请求直接跳过纠错环节。
### 关键结果
在含789条样本的公开Text2Cypher测试集上验证：
1. 自适应迹预算降低平均生成候选数30.7%，推理时延降21-25%，执行成功率仅下降0.9%以内，无统计显著性差异。
2. 选择性纠错相比全量纠错仅损失0.2-0.5%的执行成功率，几乎保留全部性能收益，且修正模型可跨LLM家族复用，无需与生成模型同系列。
### 核心结论
针对请求复杂度做差异化计算资源分配，是兼顾LLM服务性能与成本的高性价比落地方向。

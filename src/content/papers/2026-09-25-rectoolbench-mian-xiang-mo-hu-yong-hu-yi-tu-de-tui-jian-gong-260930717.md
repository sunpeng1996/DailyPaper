---
title: 'RecToolBench: Benchmarking Recommendation-Specific Tool Orchestration under
  Fuzzy User Intent'
title_zh: RecToolBench：面向模糊用户意图的推荐工具编排基准测试集
authors:
- Xiao Chen
- Yicheng Zhao
- Yingying Wu
- Zhendong Chu
- Changyi Ma
- Qingsong Wen
- Xuan Song
affiliations:
- The Hong Kong Polytechnic University
- Jilin University
- Squirrel AI Learning
arxiv_id: '2609.30717'
url: https://arxiv.org/abs/2609.30717
pdf_url: https://arxiv.org/pdf/2609.30717
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: 推荐Agent · 工具编排基准构建
tags:
- RecAgent
- Tool Calling
- Benchmark
- MCP
- Fuzzy Intent
one_liner: 首个基于MCP的推荐工具编排基准，覆盖模糊意图与4级难度共1200+可执行任务
practical_value: '- 可复用论文的模糊查询生成方法：基于业务历史交互数据，通过欠指定、软冲突、模糊量词等5类模糊策略生成真实测试用例，大幅降低人工标注成本

  - 推荐Agent可按4级难度分阶段迭代：优先搞定单工具调用的语义正确性，再优化并行/串行工具编排的依赖跟踪，最后解决混合场景的证据整合问题

  - 工具调用评估不能仅看语法合规、执行成功等指标，需新增参数语义对齐、信息接地、最终推荐与模糊意图匹配度的校验，避免无效调用

  - 可直接复用Candidate Bus架构，将候选物品元数据存储在prompt外，减少上下文占用，支持长轮次工具编排'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent化推荐系统正从被动过滤转向主动工具调用范式，但现有基准普遍假设用户意图明确、工具环境简化、函数调用孤立，忽略了真实电商/本地生活场景中用户指令模糊、需要多工具协同编排的核心痛点，无法有效衡量推荐Agent的实际落地能力。

### 方法关键点
- 基于MCP协议构建标准化工具调用层，覆盖电商、到店、本地生活3个推荐域，13个MCP服务器，共32个可执行工具，涵盖检索、过滤、情感分析、个性化推荐、地理推理、网页搜索6类核心能力
- 采用`synthesize-fuzzify-judge`可扩展任务生成pipeline：从真实用户交互序列生成明确任务后，通过5类模糊策略生成符合真实习惯的查询，最终经过质量过滤和人工校验
- 任务分为4级难度梯度：L1单工具调用、L2并行工具调用、L3串行依赖工具链、L4混合编排，复杂度和意图模糊度逐层提升
- 评估体系结合规则校验（调用合规性、执行成功率、Hit Ratio等）和LLM-as-judge评分（参数合理性、依赖感知、信息接地等），避免语法正确但语义无效的评估偏差

### 关键实验
测试9款主流LLM：6款3B-8B量级SLM、3款闭源大模型。核心结果：1）L1单工具场景下，闭源模型工具选择准确率达100%，最优SLM仅58%，格式合规率远高于语义正确率；2）L4混合编排场景下，最优闭源模型Hit Ratio仅54%，SLM仅20%-28%，编排复杂度提升会大幅拉大性能差距；3）高难度任务两大核心失败原因：54.1%为跨步骤依赖推理错误，53.6%为目标召回缺失。

### 核心结论
推荐Agent的核心瓶颈不是工具调用的语法正确性，而是模糊用户意图下的参数接地、多步骤证据整合和推荐结果落地能力

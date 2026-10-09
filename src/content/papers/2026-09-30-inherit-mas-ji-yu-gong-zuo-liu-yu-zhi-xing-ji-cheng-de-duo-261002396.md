---
title: 'Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and
  Execution Inheritance'
title_zh: Inherit-MAS：基于工作流与执行继承的多智能体系统测试时进化
authors:
- Songtao Wei
- Yi Li
- Zhichun Guo
- Bingzhe Li
affiliations:
- University of Texas at Dallas
- Independent Researcher
arxiv_id: '2610.02396'
url: https://arxiv.org/abs/2610.02396
pdf_url: https://arxiv.org/pdf/2610.02396
published: '2026-09-30'
collected: '2026-10-09'
category: MultiAgent
direction: 多智体测试时进化 · 继承优化
tags:
- Multi-Agent System
- Test-Time Evolution
- Workflow Optimization
- Token Efficiency
- Inheritance Mechanism
one_liner: 通过工作流、执行双层继承机制，降低推理开销同时提升多智能体系统测试时进化性能
practical_value: '- 电商多Agent导购、售后工单处理系统可复用工作流继承机制：每次迭代仅修改judge判定的缺陷节点，保留已验证有效的角色分工（如意图理解、RAG检索、答案生成节点），避免全链路重构的性能波动

  - 执行继承的精确缓存策略可直接落地：对Agent链路中无状态只读节点（如商品属性召回、用户意图识别），用完整请求+上下文指纹做key缓存结果，实测可降低30%左右worker
  token开销且不影响效果

  - 多Agent迭代后的排序策略可复用：不默认取最后一轮迭代结果，保留所有历史候选，按错误数、输出有效性、质量分多维度排序选最优，可提升6%左右最终效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体系统（MAS）测试时进化要么全链路修改破坏已有有效组件，要么重复执行未变更节点导致冗余推理开销，无法平衡进化效果和推理成本，在电商客服、商品推荐等需要低延迟、高可用的落地场景下实用性受限。

### 方法关键点
- 工作流继承：每次迭代基于上一轮最优工作流，仅删除judge判定无效的节点，做1次针对性的有效编辑（如改prompt、增删节点、调整拓扑），其余节点完全保留
- 执行继承：仅当节点的完整请求、上游输入、执行上下文指纹完全匹配历史记录时，才复用缓存结果，否则实时执行，避免缓存错误
- 保留所有迭代候选，按错误数、输出有效性、质量分、覆盖率多优先级排序选最优结果，不默认取最后一轮

### 关键实验
在WorkBench、HotpotQA FullWiki两个基准测试，用GPT-4o-mini做worker时，WorkBench完成率达55.4%，HotpotQA joint F1达49.7%，优于EvoAgent、EvoMAS、TacoMAS等基线；执行继承相比禁用场景，分别降低29.1%、34.6%的worker token开销，总token开销降低5.3%、18.1%。

最值得记住的一句话：多智能体系统进化不需要每次从零重构，在有效组件继承的基础上做最小修改，能同时收获效果提升和成本下降。

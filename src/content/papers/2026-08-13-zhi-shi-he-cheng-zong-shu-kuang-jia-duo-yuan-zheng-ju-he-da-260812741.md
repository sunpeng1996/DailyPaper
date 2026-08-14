---
title: 'Knowledge Synthesis Review Framework: Task-Level Benchmarking of LLM-Based
  Systems for Multi-Source Evidence Synthesis'
title_zh: 知识合成综述框架：多源证据合成大模型系统的任务级基准评估
authors:
- Wafa Shafqat
- Mark Patterson
- Steven N. Liss
affiliations:
- Toronto Metropolitan University
- Magnet
- Future Skill Center
- Queen’s University
- Stellenbosch University
arxiv_id: '2608.12741'
url: https://arxiv.org/abs/2608.12741
pdf_url: https://arxiv.org/pdf/2608.12741
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 多源证据合成 · LLM任务级基准评测
tags:
- Evidence Synthesis
- Human-in-the-loop
- LLM Benchmark
- Task Routing
- Knowledge Synthesis
one_liner: 提出人在环KSR框架，拆分证据合成任务、分任务评测并路由到最优大模型系统
practical_value: '- 电商多源信息聚合（评论/舆情/商品资料）场景可复用「任务拆分+分模型路由」思路，将任务拆分为筛选、抽取、分析、合成4类，分别测试不同LLM表现后路由最优模型，兼顾效果与成本

  - 内部LLM选型评测可复用论文的污染校验方案，用训练截断日期后的样本验证模型真实表现，避免数据泄露导致的效果虚高

  - 人在环LLM系统可将校验资源集中在分析、跨源合成等高复杂度任务，结构化抽取、粗筛类低难度任务可全自动化，平衡业务效率与准确率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
快速迭代领域的证据分散在学术论文、产业报告、政策文件、媒体等多源渠道，质量结构差异大，人工合成效率低，现有LLM在合成各认知任务上的可靠性缺乏明确基准。
### 方法关键点
提出人在环KSR框架，将多源证据合成拆解为筛选、抽取、分析、合成4个独立任务，针对每个任务用专家金标准基准测试不同LLM系统，在持续专家校验下将任务路由到表现最优的系统。
### 关键结果
测试数据集为AI与就业领域1893篇文档中的244篇基准子集，专家金标准inter-rater一致性92.2%、kappa=0.80；Claude Sonnet 4筛选准确率最高（82.8%），GPT-5筛选召回最高（91.8%）但特异性更低；标题/来源字段抽取一致性超90%，作者/参考文献抽取、跨源分析合成效果明显下降，后者仍需专家判断；全量语料运行路由工作流可发现单源合成遗漏的劳工福利、小型企业、南半球等盲区。

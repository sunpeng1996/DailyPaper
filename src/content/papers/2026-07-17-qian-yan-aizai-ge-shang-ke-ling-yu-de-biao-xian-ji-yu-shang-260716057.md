---
title: 'Frontier AI performance across the business disciplines: a case-grounded benchmark
  of knowledge work and analytical reasoning'
title_zh: 前沿AI在各商科领域的表现：基于商业案例的知识工作与分析推理基准
authors:
- Ajay Patel
- Kartik Hosanagar
- Ramayya Krishnan
- Chris Callison-Burch
- Karim Lakhani
- Mitch Weiss
affiliations:
- The Wharton School, University of Pennsylvania
- Heinz College of Information Systems and Public Policy, Carnegie Mellon University
- Department of Computer and Information Science, University of Pennsylvania
- Harvard Business School, Harvard University
arxiv_id: '2607.16057'
url: https://arxiv.org/abs/2607.16057
pdf_url: https://arxiv.org/pdf/2607.16057
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: 大模型评测 · 商科知识推理能力评估
tags:
- LLM
- Benchmark
- Analytical Reasoning
- Knowledge Work
- Evaluation
one_liner: 构建覆盖18个商科领域的BusinessCaseBench，评估前沿LLM的知识工作与分析推理能力
practical_value: '- 可复用「业务真实案例+专家评分rubric」的评估框架，替代人工盲评来检测LLM在电商运营分析、定价策略、广告投放决策等场景的输出质量

  - 设计推荐/广告Agent的评测数据集时，可参考该基准的多利益相关方权衡、不确定信息下决策的考题逻辑，补全现有能力评估维度

  - 业务中调用LLM做复杂分析类任务时，优先选择近两年迭代的前沿模型，其信息合成、策略分析能力已有大幅提升'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM基准多聚焦事实召回、数学、代码、Agent工具使用等窄场景能力，缺少对白领日常开展的复杂信息合成、不确定场景决策、多利益相关方权衡、结构化分析等知识工作能力的度量，主观类任务的效果评估空白尤为突出。
### 方法关键点
基于顶尖商学院的案例教学框架，构建BusinessCaseBench基准，覆盖18个商科领域的数百道案例问题，每道题配套由专家编写的教学案例答案导出的标准化评分rubric。
### 关键结果
前沿LLM在该基准上已取得较高评分，同模型家族的分析推理能力2年内提升幅度显著，证明LLM已具备较高的商科分析能力，可支撑大量入门级专业分析类工作需求。

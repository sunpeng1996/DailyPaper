---
title: 'Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research
  Agents'
title_zh: 面向高效深度研究Agent的边际价值估计与上下文剪枝
authors:
- Harshitha Kolukuluru
- Reshma Ashok
- Kirat Arora
- Evan William Ciccarelli
- Nischal Ashok Kumar
- Lunyiu Nie
- Franck Dernoncourt
- Samyadeep Basu
- Ryan A. Rossi
- Nedim Lipka
affiliations:
- University of Massachusetts Amherst
- The University of Texas at Austin
- Adobe Research
arxiv_id: '2608.08389'
url: https://arxiv.org/abs/2608.08389
pdf_url: https://arxiv.org/pdf/2608.08389
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent 长周期任务上下文剪枝优化
tags:
- Agent
- Context Pruning
- Marginal Value Estimation
- Token Efficiency
- Long-horizon Reasoning
one_liner: 系统对比长周期研究Agent三阶段剪枝策略，证实剪枝位置比规则更重要，轻量启发式可降73%token成本
practical_value: '- 电商多轮导购、商品咨询类Agent可直接复用三阶段剪枝架构：优先落地Post-Retrieval剪枝，用MMR这类无需训练的轻量启发式，无需复杂LLM判断即可降60%+token与
  latency，质量损失控制在3%以内

  - 若追求质量优先，可叠加Pre-Synthesis阶段混合剪枝（如CD+SC策略），可在降63%token的同时小幅提升生成内容的整体质量

  - 极致成本控制场景可再加Pre-Retrieval剪枝，三阶段MMR组合可实现73%的token节省，适合C端大流量Agent场景

  - 无需盲目上复杂的学习式或LLM-based剪枝，选对剪枝阶段的收益远高于优化剪枝算法本身，大部分业务场景轻量启发式即可覆盖需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长周期检索Agent需通过迭代检索、聚合、合成完成开放式复杂任务，但运行过程中上下文快速膨胀，新增内容边际价值持续下降，既推高token成本与 latency，也会给最终合成阶段引入噪声，现有方案缺乏跨剪枝阶段的系统性对比，无法明确哪个阶段剪枝、用什么策略的投入产出比最高。

### 方法关键点
- 定位三个剪枝干预点：Pre-Retrieval（检索前过滤低价值子查询，避免检索成本）、Post-Retrieval（检索后过滤低价值上下文，阻止无意义的分支扩张）、Pre-Synthesis（合成前压缩最终上下文，降低生成阶段成本），支持1/2/3阶段组合配置
- 统一基于边际价值评分框架，对比7类剪枝策略：包括MMR、GRN、CD、DPP、SC等无训练的轻量启发式，以及LLM judge、学习式剪枝，保留评分超过阶段阈值的候选

### 关键实验结果
基于DeepResearchGym的100个复杂研究查询，基线为无显式剪枝的GPT-Researcher pipeline：
1. 单阶段Post-Retrieval用MMR可降69.5%token、59.7% latency，仅损失2.1%的报告质量
2. 两阶段Post-Retrieval+Pre-Synthesis用CD+SC策略，降63.4%token的同时报告质量比基线高1.64分
3. 三阶段全链路MMR可实现73.3%的token削减，保留96.7%的基线质量

### 最值得记住的一句话
剪枝的阶段位置比具体评分规则的影响大得多，早期剪枝优先控成本，后期剪枝优先提质量，大部分场景下轻量启发式的收益远高于复杂的LLM或学习式剪枝

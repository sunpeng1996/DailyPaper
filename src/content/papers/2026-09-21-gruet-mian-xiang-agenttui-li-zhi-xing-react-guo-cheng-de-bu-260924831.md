---
title: 'GRUET: Quantifying Uncertainty of Agentic Reasoning-and-Acting Processes'
title_zh: GRUET：面向Agent推理执行（ReAct）过程的不确定性量化方法
authors:
- Shuang Liang
- Xin-Yu Hu
- Shao-Qun Zhang
affiliations:
- National Key Laboratory for Novel Software Technology, Nanjing University
- School of Intelligent Science and Technology, Nanjing University
arxiv_id: '2609.24831'
url: https://arxiv.org/abs/2609.24831
pdf_url: https://arxiv.org/pdf/2609.24831
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 推理执行过程不确定性量化
tags:
- Agent
- ReAct
- Uncertainty Quantification
- LLM
- Graph Modeling
one_liner: 基于推理空间DAG建模的ReAct轨迹不确定性量化方法，性能远超现有UQ基线
practical_value: '- 电商导购/客服Agent场景可复用GRUET的轨迹可信度打分，筛选高置信度的ReAct决策路径，降低错误回复/操作概率

  - 工程上可优先选用first-turn+K=10采样的轻量化实现，仅需1/总轮数的采样成本就能接近全轮聚合的UQ性能，平衡效果和开销

  - 多步推理类Agent的UQ不要直接复用单轮LLM UQ方法（如Perplexity、Verbalized Confidence），这类方法普遍表现接近随机，无实用价值'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent多采用ReAct范式完成多轮推理与环境交互，相同任务下常产出发散轨迹，高不确定性轨迹会导致不可预期的错误行为，严重降低Agent可信度；而现有单轮LLM UQ方法迁移到ReAct轨迹量化时性能接近随机，缺乏有效、通用的轨迹级不确定性量化方案。

### 方法关键点
- 建模层：将每轮推理的所有潜在分支（多次采样得到）建模为DAG，通过NLI双向蕴含合并语义等价的推理节点、用任务专属嵌入的余弦相似度合并等价动作节点，完整刻画推理空间拓扑
- 轮级UQ：融合token级分布统计与DAG拓扑信息，将DAG等价为FNN做不确定性传播，计算得到每轮推理的不确定性得分
- 轨迹级聚合：提供6种轻量聚合策略，包括全轮平均、Top 25%高不确定性轮平均、首/尾轮得分等，无需监督训练即可完成轨迹级可信度量化

### 关键实验
覆盖9款不同规模LLM（Qwen3.5、Gemma4系列）、5个Agent基准（SWE-bench系列、InterCode系列），对比10种主流单轮UQ基线（包括Verbalized Confidence、Perplexity、Semantic Entropy等）；GRUET的AUROC平均达75.49，比最强基线高17.11，AUPRC达61.10，比最强基线高16.42，所有指标均满足3σ显著性要求。

### 核心结论
现有单轮LLM UQ方法在ReAct轨迹不确定性量化任务上普遍表现接近随机，基于推理空间拓扑建模的多轮不确定性聚合才是有效路径。

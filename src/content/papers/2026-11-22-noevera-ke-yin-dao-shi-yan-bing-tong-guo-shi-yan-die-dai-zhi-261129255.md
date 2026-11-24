---
title: 'NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?'
title_zh: NoeVera：可引导实验并通过实验迭代知识的Agent第二大脑
authors:
- Pinaki Prasad Guha Neogi
- Spyros Mastorakis
- Ankur Mallick
- Saravan Rajmohan
- Victor Rühle
affiliations:
- Microsoft M365 Copilot Research
- The Ohio State University
arxiv_id: '2611.29255'
url: https://arxiv.org/abs/2611.29255
pdf_url: https://arxiv.org/pdf/2611.29255
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 知识-实验闭环优化
tags:
- Agentic RAG
- Second Brain
- LLM Serving
- Knowledge Base
- Closed Loop
one_liner: 提出三层架构的Agent第二大脑，实现知识引导LLM服务调优、实验结果反哺知识库迭代
practical_value: '- 知识库架构可直接复用：拆分为原始证据层、合成知识层、Agent记忆层三层，所有合成结论溯源到原始证据，大幅降低RAG幻觉，适合电商规则、推荐运营策略知识库搭建

  - 工具调度逻辑可迁移：仅当现有知识无法回答定量问题时才触发模拟器/AB测工具调用，检索排序新增权威度、适用场景维度，降低不必要的算力开销，适合推荐调优Agent的工具流设计

  - 实验沉淀范式可落地：所有实验结论绑定适用场景（流量特征、硬件、约束条件）回写知识库，冲突结论并列存储不覆盖，过泛化率从28%降至8%，适合推荐策略迭代的经验沉淀体系搭建'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM服务调优需要在海量配置中搜索满足吞吐、延迟、内存约束的最优解，现有贝叶斯优化等搜索方法调用模拟器成本高，通用Agent知识零散、实验结果无法复用，过泛化率高达28%，无法形成知识引导实验、实验反哺知识的正向循环。

### 方法关键点
- 三层持久化第二大脑架构：Evidence Plane存原始资料、溯源信息和权威度信号；Synthesis Plane蒸馏可复用的技术结论、决策矩阵，所有结论绑定原始证据；Agent Memory Plane存知识使用痕迹用于问题排查
- 决策感知检索：混合BM25、语义检索、知识图谱检索多路召回，按相关性、权威度、适用场景、用户角色加权排序，在token预算下生成去重的证据包
- 三角色Agent协作：Scout发现证据、Investigator分析技术细节输出候选实验、Synthesizer生成面向角色的结论，仅当无适用定量证据时调用Vidur/GAUSS模拟器
- 闭环回写机制：所有实验结果附带适用范围（硬件、模型、流量特征）作为结构化证据记录回写，冲突结论并列存储不覆盖

### 关键结果
- 配置搜索场景：中位数6-7次模拟器调用即可达到最优解95%性能，比贝叶斯优化少3次，比无知识Agent少9次；生成的配置在A100上比vLLM默认吞吐高1.3×，满足所有延迟SLO
- 知识复用场景：实验结论过泛化率仅8%，比通用Agent记忆Mem0低20个百分点；查询流上模拟器调用量下降64%
- 72任务NoeVeraBench 48个留出任务上，得分比同等配置Agent高29%，比单轮RAG高36%

最值得记住的结论：知识组织和实验闭环比单纯的检索或Agent编排更能提升复杂系统调优效率，所有结论必须绑定适用场景才能安全复用

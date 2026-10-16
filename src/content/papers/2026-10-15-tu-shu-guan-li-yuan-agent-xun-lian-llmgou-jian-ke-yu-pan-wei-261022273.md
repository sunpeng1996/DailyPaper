---
title: 'Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate
  Future Queries'
title_zh: 图书管理员Agent：训练LLM构建可预判未来查询的长上下文工作空间
authors:
- Anikait Singh
- Teresa Zhang
- Yoonho Lee
- Roshen Sanjay Nair
- Aviral Kumar
- Chelsea Finn
affiliations:
- Stanford University
- Carnegie Mellon University
arxiv_id: '2610.22273'
url: https://arxiv.org/abs/2610.22273
pdf_url: https://arxiv.org/pdf/2610.22273
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 长上下文记忆预构建优化
tags:
- Agentic RAG
- Long Context Reasoning
- Reinforcement Learning
- Memory Curation
- Workspace Optimization
one_liner: 提出Builder Agent预构建分层文件系统工作空间，大幅提升长上下文多轮问答的准确率与成本效率
practical_value: '- 电商知识库、商品属性库、售后问答库等高复用查询场景可复用该框架，将离线构建成本分摊到海量用户查询中，用RL优化知识库分层结构，比固定规则的知识图谱/索引覆盖更多长尾查询

  - RAG系统的离线预处理阶段可引入「合成文件+原始源链接」的双轨结构，既保证高频查询的快速响应，又保留原始文档溯源能力，解决合成摘要丢失细节的问题，适配大促、新品上市等集中查询场景

  - 可复用GRPO优化离线预处理策略的思路，直接用下游查询准确率作为奖励信号端到端优化索引/摘要结构，无需人工标注预处理规则，可迁移到个性化推荐的用户历史记忆构建场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RAG、知识图谱方案要么是查询时被动检索，重复计算跨文档关联信息导致推理延迟高；要么基于固定规则预构建结构，灵活性差，无法适配未知长尾查询需求。尤其在企业知识库、电商商品库等高复用查询场景下，大量重复检索算力被浪费，亟需可预判查询需求的主动预构建记忆方案，将计算成本分摊到多轮查询中。

### 方法关键点
- 双Agent框架：Builder Agent将原始文档转换为带源引用链接的分层合成文件系统工作空间，回答Agent固定，仅遍历该工作空间完成查询响应
- 工作空间构建形式化为MDP，定义CreateFile、MergeFiles、Delete、Stop 4种原子操作，用GRPO强化学习优化Builder策略，奖励直接关联下游回答准确率，支持加入构建成本、查询遍历成本的权重控制
- 采用间隔8步探测回答准确率的稠密奖励设计，解决长序列操作的信用分配问题，Builder构建过程完全看不到下游查询，保证方案泛用性

### 关键实验
在BrowseComp-Plus深度研究问答数据集上，比GraphRAG、Agentic RAG等最强基线准确率平均高33个百分点；零样本迁移到BRIGHT跨领域问答基准时，平均准确率比基线高31个百分点。成本分摊效果上，单语料查询次数达10次时，每正确回答的token消耗比基线低33.8%，查询次数超过31次时完全覆盖预构建成本。

最值得记住的一句话：将长上下文处理的计算量从查询时转移到预构建阶段，用RL端到端优化记忆结构，是大幅降低高复用场景下长上下文推理成本的有效路径。

---
title: 'Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents'
title_zh: 将检索视为遍历：面向有状态长上下文Agent的价值索引内存
authors:
- Daniel Strauß
- Zhenshan Bing
- Alois Knoll
affiliations:
- Technical University of Munich
- Nanjing University
arxiv_id: '2610.40545'
url: https://arxiv.org/abs/2610.40545
pdf_url: https://arxiv.org/pdf/2610.40545
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 长上下文Agent · 内存检索优化
tags:
- LongContextAgent
- MemoryRetrieval
- ValueIndexedMemory
- TraversalRetrieval
- StatefulRetrieval
one_liner: 价值索引内存架构将长上下文检索转为地址空间持久遍历，大幅提升学习效率
practical_value: '- 电商导购/客服Agent的长会话记忆检索可借鉴价值索引思路，将互补性强的记忆（如用户同次咨询的需求点）存储在相邻地址，冗余记忆分开存储，降低重复检索开销

  - 推荐系统用户长期兴趣记忆模块可复用遍历式检索机制，相邻推荐请求复用前次检索到的兴趣记忆集合，减少全局检索次数，提升推理效率

  - 电商场景RAG系统的知识库索引可参考成本正则化目标，同时衡量记忆的业务价值与检索成本，替代固定top-k截断规则，提升召回性价比'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长上下文模型现有检索机制（注意力、全局检索、循环压缩）均未利用相邻步骤检索记忆高度重叠的特性，要么每次重新全量扫描导致效率低下，要么提前压缩丢失关键信息，难以平衡检索成本与信息保留效果。
### 方法关键点
- 分离内存内容与存储地址，地址空间基于检索效用构建而非语义相似性，互补记忆就近存储，冗余记忆相互隔离
- 设计成本正则化索引目标，在保留局部邻域信息价值的同时，为每个可访问内存收取固定检索成本，自动平衡检索规模与收益
- 采用持久遍历式检索机制，维护持续移动的检索头，相邻步骤复用前次检索状态，无需每次发起全局查询
### 关键实验
在MiniGrid Memory环境下测试固定几何地址的遍历检索头，对比无检索头基线、高斯绝对寻址、分类绝对寻址三类基准方案，仅使用5 token上下文时，遍历式检索头达到0.95平均回报仅需0.59M训练步，远低于高斯寻址的0.94M步与分类寻址的2M+步，效果接近64 token全上下文基线的性能。
### 核心结论
检索地址的组织应优先考虑记忆的决策价值与互补性，而非单纯的内容相似性，持久化局部遍历可大幅降低连续检索的重复开销。

---
title: 'Mandol: An Agglomerative Agent Memory System for Long-Term Conversations'
title_zh: Mandol：面向长对话Agent的聚合式统一记忆系统
authors:
- Yuhan Zhang
- Zhiyuan Guo
- Ziheng Zeng
- Wei Wang
- Wentao Wu
- Lijie Xu
affiliations:
- Institute of Software, Chinese Academy of Sciences
- Microsoft Research
arxiv_id: '2606.29778'
url: https://arxiv.org/abs/2606.29778
pdf_url: https://arxiv.org/pdf/2606.29778
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent 长对话记忆系统
tags:
- Agent Memory
- Long Conversations
- Retrieval
- RAG
- Semantic Graph
one_liner: 构建统一原生架构的Agent长时记忆系统，兼顾检索精度与低交互延迟
practical_value: '- 电商客服/导购类长期交互Agent，可借鉴分层统一语义图结构，存储跨会话用户偏好、交互历史、订单信息，解决多源记忆碎片化问题

  - 针对用户偏好动态更新的场景，可复用本文的冲突解决策略：基于MAD动态阈值过滤噪声，通过「相关性+时间新鲜度+源可信度」加权仲裁解决偏好冲突

  - 对交互式低延迟要求高的Agent服务，可采用同进程内统一内存结构替代异构多数据库架构，消除跨库I/O开销，可获得数倍的检索插入速度提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长对话Agent记忆系统依赖异构向量库+图库的混合存储，存在记忆碎片化、跨库I/O延迟高的问题；传统RAG检索容易引入噪声、丢失关联线索，且缺乏Token预算控制，在跨会话多跳推理、用户状态更新类查询上准确率低，还会浪费LLM上下文窗口，无法满足长期交互式Agent的需求。

### 方法关键点
- 分层记忆模型：记忆分为基础层（存储原始交互信息）和高层抽象层（聚合成情景记忆、语义记忆、用户偏好记忆），两层统一用结构化语义图表示，抽象记忆保留回基础层的可追溯链接，兼顾抽象推理和证据可追溯
- 聚合语义数据结构：融合SemanticMap和SemanticGraph，在同一进程地址空间原生融合key-value、向量、图结构，提供统一混合检索算子，消除跨库I/O开销，冷数据用嵌入式DuckDB异步持久化
- 量化检索机制：流程分为查询自适应路由（按意图选记忆源控候选量）、MAD动态阈值去噪、多源冲突仲裁、MMR优化的Token约束上下文生成，检索全程不调用LLM

### 关键实验结果
在LoCoMo、LongMemEval两个主流长对话记忆基准测试，对比Mem0、Zep、MemOS、EverMemOS等基线，Mandol取得SOTA精度：LoCoMo准确率92.21%，LongMemEval准确率88.40%；10QPS并发下，相比最快基线获得5.4×检索加速、4.8×插入加速，消费级硬件仍保持低延迟。

### 核心结论
统一内存原生架构+量化无LLM检索，是兼顾Agent长时记忆精度和低延迟的有效方案

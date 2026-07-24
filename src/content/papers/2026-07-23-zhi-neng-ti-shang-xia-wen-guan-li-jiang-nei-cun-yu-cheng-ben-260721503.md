---
title: 'Agentic Context Management: Solving Agent Memory and Cost by Treating Them
  as Lifecycle and Architecture Problems'
title_zh: 智能体上下文管理：将内存与成本作为生命周期与架构问题解决
authors:
- Gaurav Dadhich
affiliations:
- Maximem
arxiv_id: '2607.21503'
url: https://arxiv.org/abs/2607.21503
pdf_url: https://arxiv.org/pdf/2607.21503
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 上下文生命周期管理优化
tags:
- Agent Memory
- Context Management
- RAG
- LLM
- Production Agent
one_liner: 将Agent内存问题重新定义为全生命周期管理问题，提出5个核心原语与工业级参考实现
practical_value: '- 电商导购/客服Agent的长会话场景可复用「验证式压缩」设计，在将token成本从O(n²)降至O(n)的同时避免信息丢失，解决多轮会话召回率低、成本爆炸的问题

  - 多租户商家运营Agent可复用「用户→客户→平台」三层scope分层机制，严格隔离不同商家数据的同时共享平台通用规则知识，避免跨租户数据泄露

  - RAG检索模块可参考「向量+关键词+知识图谱」混合检索设计，用向量解决语义gap，用关键词+图谱补全多跳推理的桥接信息，提升多轮推荐/客服的信息召回充分度

  - 实时交互Agent可借鉴「预判式预取」思路，根据用户当前行为提前加载下一步所需上下文，将检索操作从响应关键路径移除，降低端到端延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业界Agent落地率不足10%，核心瓶颈并非推理能力不足，而是上下文管理混乱：naive全量追加上下文的模式下token成本随会话长度平方级增长，粗暴摘要压缩又会导致准确率断崖下跌，传统仅聚焦存储与检索的内存框架无法覆盖生产级Agent全链路上下文需求。

### 方法关键点
- 提出Agentic Context Management（ACM）框架，将上下文管理拆解为5个核心原语：架构设计（为每个Agent定制专属内存schema）、摄入（异步提取结构化信息+实体归一化）、范围界定（用户/客户/平台三层scope分层检索，严格隔离）、预判（投机式预取下一轮所需上下文，减少关键路径延迟）、压缩与合并（带信息丢失校验的验证式压缩，压缩失败自动降级重试）
- 参考实现Maximem Synap采用多语言存储栈，向量+关键词+知识图谱混合检索，覆盖不同场景召回需求
- 会话token成本控制为线性，相比全量追加模式，200轮会话成本可降低13倍

### 关键结果
在LongMemEval（500道长会话内存基准）上达到92.0%准确率，在LoCoMo（平均300轮长会话基准）上达到93.2%准确率，显著优于现有同类内存系统。

### 最值得记住的一句话
Agent落地的核心瓶颈不是推理能力，而是上下文管理能力，未来的竞争不是谁存的数据多，而是谁管理上下文的效果最好。

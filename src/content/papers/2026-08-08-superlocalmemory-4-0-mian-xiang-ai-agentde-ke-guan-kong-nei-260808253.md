---
title: 'SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents'
title_zh: SuperLocalMemory 4.0：面向AI Agent的可管控内存操作系统
authors:
- Varun Pratap Bhardwaj
- Garima Singh
- Arun Pratap Bhardwaj
affiliations:
- Qualixar, India
- Independent Researcher, India
arxiv_id: '2608.08253'
url: https://arxiv.org/abs/2608.08253
pdf_url: https://arxiv.org/pdf/2608.08253
published: '2026-08-08'
collected: '2026-08-11'
category: Agent
direction: Agent内存系统 · 本地优先可管控
tags:
- AgentMemory
- LocalFirst
- MultiTenant
- VerifiableTransaction
- RetrievalFusion
one_liner: 提出本地优先、多租户可管控的AI Agent内存操作系统，整合检索、学习、时序与合规治理能力
practical_value: '- 多租户管控机制可直接复用：RBAC+生成围栏的内存隔离方案，适配电商多店铺/多品牌Agent集群部署，从写入路径杜绝不同租户的上下文泄露风险

  - 多路召回融合框架可迁移：5路候选（语义/BM25/时序/Hopfield联想/图传播）+ RRF融合的检索链路，叠加Ebbinghaus近因衰减排序逻辑，可直接优化推荐系统用户短期兴趣召回效果

  - 跨存储一致性方案可落地：异构存储（向量/全文/时序库）写入带哈希校验完成凭证+自动对账重试的机制，可解决推荐系统用户行为数据多存储同步的一致性问题

  - Agent技能迭代管控逻辑可抄：五阶段校验+资源预算控制的自演化流水线，默认隔离到 quarantine 再上线，可降低电商客服/运营类Agent自动迭代的故障风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前AI Agent从单用户助手演进为企业级共享设施，现有内存方案均为单点能力实现，缺乏统一的本地优先、多租户隔离、可验证、带合规治理的运行时；企业部署Agent时要么依赖云内存存在数据泄露风险，要么自行拼接组件无法保障一致性与GDPR、EU AI Act等合规要求。

### 方法关键点
- 采用7层架构，底层基于6个SQLite数据库+向量/图投影，支持CLI/HTTP/MCP等多种接入方式，适配9种主流Agent框架，提供全本地/本地模型/云辅助三种运行模式
- 多通道检索：语义（Fisher-Rao重打分，无方差时fallback余弦相似度）、BM25、时序、Hopfield联想、图传播5路候选生成，经RRF融合后叠加双时态过滤与Ebbinghaus近因衰减排序
- 可管控技能演化：采用screen→confirm→mutate→blind-verify→persist五阶段流水线，配置资源预算约束（每天最多3次迭代、10次LLM调用、30分钟时长），默认隔离到验证区，经配置开关才能上线并支持故障回滚
- 治理原生能力：内置多租户隔离+RBAC，GDPR数据删除带哈希链式审计 trail，跨BM25/时序/向量三类存储实现可验证事务。

### 关键结果
11个故障注入场景各重复200次，全部通过预期组件特性校验；1.23GB内存库测试下，60秒内存占用稳定在436.4-440.7MB无内存泄漏，并发压测零写锁错误；带管控的写路径相比无管控路径的额外开销p50为1.687ms，p99为2.728ms。

**最值得记住的一句话**：租LLM，own内存——企业的核心资产是Agent积累的上下文、技能与决策数据，必须部署在自身可控的基础设施上。

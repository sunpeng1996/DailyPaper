---
title: 'FedWorld: Scope-Aware Federation of Agent World Models'
title_zh: FedWorld：支持作用域感知的智能体世界模型联邦协议
authors:
- Yuchao Hou
affiliations:
- Shanxi Normal University
arxiv_id: '2608.01561'
url: https://arxiv.org/abs/2608.01561
pdf_url: https://arxiv.org/pdf/2608.01561
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 跨端世界模型联邦共享
tags:
- LLM Agent
- Federated Learning
- World Model
- Knowledge Transfer
- Negative Transfer
one_liner: 提出作用域感知的联邦世界模型共享协议，避免跨智能体知识迁移的负向转移
practical_value: '- 多租户电商Agent（不同商家的客服/运营Agent）共享业务规则时，可借鉴scope过滤机制：先将本地交易/售后规则归一化抽象，再根据跨租户支持/矛盾证据给规则打全局/集群/私有标签，避免主流商家规则覆盖小众商家的差异化规则，减少负向迁移

  - Agent跨场景经验复用架构可参考local-first设计：优先使用本地已验证的世界模型规则，仅在本地无覆盖时才引入外部对齐后的兼容规则，既填补经验缺口又不破坏本地已有正确知识

  - 规则冲突判定方法可复用：对相同抽象动作的不同效果，统计跨客户端支持率、矛盾率，用拉普拉斯平滑算置信度，区分共享/集群/私有/未解决规则，替代粗暴的多数投票逻辑'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM Agent依赖本地交互经验构建的世界模型做规划决策，但单客户端经验覆盖范围有限，跨端知识共享是必然需求。现有联邦学习聚合参数、记忆共享直接合并轨迹的方案，均未校验规则对目标端的适用性，相同抽象动作在不同业务政策/环境下效果差异大，多数派规则容易覆盖少数端的正确知识，导致严重负向转移。

### 方法关键点
- 客户端侧将私有状态转移数据映射为归一化抽象规则（含动作类型、前置状态、条件集、效果、异常结构），仅共享抽象规则，原始交互数据不离开本地，满足隐私要求
- 服务端对齐语义相关的规则，统计每条规则的跨客户端支持/矛盾证据，通过拉普拉斯平滑计算置信度，将规则划分为全局共享、集群特有、私有、未解决四类
- 采用本地优先更新策略：目标端优先保留本地已有的高置信度规则，仅当本地无对应规则覆盖时，才引入作用域兼容的联邦规则，未解决/不兼容规则直接过滤

### 关键实验
在τ-bench（零售/航空业务场景）、ALFWorld（具身家庭场景）上测试，对比LocalWM（仅用本地规则）、NaiveUnion（无差别合并所有规则）等基线：
- 跨客户端缺口场景（S3）：τ-bench上比LocalWM准确率高12.4pp，ALFWorld上高21.2pp
- 严格冲突场景（S4 strict）：比NaiveUnion准确率高16.6pp（τ-bench）、25.0pp（ALFWorld），负向转移基本被消除
- 线上任务：τ-bench任务成功率从LocalWM的51.2%提升至62.4%，ALFWorld从44.7%提升至59.3%，状态回退、重复动作、多余步骤均下降40%左右

### 核心结论
跨Agent知识共享的核心不是最大化经验合并量，而是在不破坏本地正确知识的前提下精准填补缺口，scope过滤的收益远高于无差别知识合并的收益。

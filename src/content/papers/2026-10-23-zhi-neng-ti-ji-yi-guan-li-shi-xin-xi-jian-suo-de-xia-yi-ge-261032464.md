---
title: Agentic Memory Management Is the Next Frontier of Information Retrieval
title_zh: 智能体记忆管理是信息检索的下一个前沿方向
authors:
- Qingyao Ai
affiliations:
- Tsinghua University
arxiv_id: '2610.32464'
url: https://arxiv.org/abs/2610.32464
pdf_url: https://arxiv.org/pdf/2610.32464
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: 智能体记忆管理 · IR延伸框架
tags:
- Agentic_Memory
- Information_Retrieval
- LLM_Agent
- RAG
- Memory_Management
one_liner: 提出智能体记忆管理为IR新研究方向，给出系统框架、分类体系与落地研究路线
practical_value: '- 可直接复用记忆对象三级分类（常量/函数/算子）搭建电商导购Agent记忆系统：常量存用户偏好事实、函数存下单/查物流等执行技能、算子存平台合规/优先级规则，解决现有Agent记忆混乱、错用规则的问题

  - 记忆的学习/遗忘/利用三段流程可迁移到用户长短期兴趣建模，遗忘策略基于用户行为频率/时效性设计，替代现有固定时间窗口的兴趣衰减规则，提升长周期推荐准确率

  - 参考记忆效用原则优化RAG检索排序逻辑，不再仅按语义相似度排序，而是结合记忆对下游任务的预期贡献度排序，适配Agent调用RAG的场景，减少无关上下文干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统IR研究默认信息消费者是人类，所有算法、评估体系都围绕人类认知特性设计。随着LLM Agent普及，超37%用户已用AI工具替代搜索引擎完成任务，大量信息不再直接触达人类，而是作为Agent内部状态被消费、存储、使用。当前Agent记忆管理多为零散工程实践，缺乏系统理论框架，也未复用IR领域几十年的信息管理、评估方法论，落地时容易出现记忆错乱、规则错配、用户偏好泄漏等问题。

### 方法关键点
- 正式定义Agentic Memory Management (AMM) 为IR在Agent时代的自然延伸，研究Agent内部信息的结构、组织、存储、检索、使用全链路
- 提出计算视角的记忆对象三级分类：常量（离散事实，如用户收货地址）、函数（可执行技能/工作流，如优惠券核销流程）、算子（高阶规则/偏好，如优先推荐本地现货），三类对象对应不同的检索匹配逻辑
- 拆解AMM核心流程为学习（判断哪些信息值得存储）、遗忘（动态删除低价值信息）、利用（按需检索并适配Agent上下文）三类，构建包含对象、流程、应用、优化的四层系统框架
- 梳理AMM与传统IR的对应关系，给出四大研究议程：标准化评估协议、记忆效用理论、混合参数/非参数优化、人在回路治理

### 关键结果
本研究为视角类论文，无量化对比实验结果，核心框架来自IR领域60年方法论沉淀与现有Agent记忆系统的归纳总结。

### 核心结论
IR最初的愿景是为人类构建外部记忆系统，下一个要组织的记忆，是智能体内部的记忆。

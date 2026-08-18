---
title: 'Agentic Transaction: Towards ACID-Compliant Agent Systems'
title_zh: 《智能体事务：面向具备ACID合规性的LLM智能体系统》
authors:
- Zhaoyan Sun
- Xiaoxiao Wang
- Guoliang Li
affiliations:
- Tsinghua University
arxiv_id: '2608.13900'
url: https://arxiv.org/abs/2608.13900
pdf_url: https://arxiv.org/pdf/2608.13900
published: '2026-08-13'
collected: '2026-08-18'
category: Agent
direction: Agent 系统 · ACID语义执行保障
tags:
- Agent System
- ACID
- Reliability
- Semantic Transaction
- LLM Agent
one_liner: 将数据库ACID语义适配到LLM智能体执行，构建可靠智能体框架，性能超SOTA 10.6%
practical_value: '- 电商多Agent执行场景（如大促自动化运营、多部门协同选品）可复用语义隔离机制，按子任务依赖选择独立/协作/竞争隔离策略，避免无效中间状态污染全局上下文，降低执行方差

  - Agent执行的工具调用、工作流操作可借鉴语义原子性设计，将「探索-执行-校验」作为最小事务单元，仅提交校验通过的结果，失败步骤自动回滚，避免错误结果向下游传播（推荐系统的智能调价、创意生成Agent可直接套用）

  - 可复用轻量级本地小模型做置信度校验的方案：用小模型输出token log概率计算决策/代码置信度分歧，触发重试，不用改动大模型API，低成本降低大模型幻觉、提升执行稳定性，适合业务级Agent落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent逐步从对话助手落地到长周期生产任务，但存在执行不可靠、结果不一致、并发冲突、状态管理混乱等问题，和早年数据库系统面临的挑战高度相似，现有Agent框架缺乏类似数据库ACID的标准化可靠性保障机制，难以支撑企业级生产场景落地。

### 方法关键点
- 重新定义适配Agent执行的4项语义ACID属性：语义原子性（仅提交校验通过的事务单元效果，失败回滚）、语义一致性（输出必须符合任务目标与证据约束）、语义隔离（并发Agent事务不产生无效干扰）、语义持久性（提交的状态、证据持久化存储可追溯）
- 落地实现ACID合规数据Agent：离线端构建带事务保障的可复用技能hub，通过测试用例校验技能可靠性；在线端将每轮「探索-执行-校验」作为最小语义事务单元，基于LLM token置信度分歧做一致性校验，按子任务依赖自适应配置多Agent隔离策略，采用事务感知的知识图谱内存+追加式工作区实现状态持久化

### 关键实验
在KramaBench数据Agent基准（104个跨6领域的真实数据科学任务）上，对比Claude Code、DA-Agent等SOTA方案，基于Qwen3.5-397B backbone的ACID-Agent整体得分比Claude Code高10.6%，执行方差降低40%，且效果优于更大参数的GLM-5.2+Claude Code组合。

数据库领域沉淀数十年的事务设计思想，是解决LLM Agent生产落地可靠性问题的核心可行路径之一。

---
title: 'τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction'
title_zh: ττ-Bench：面向端到端真实业务Agent构建的评测基准
authors:
- Quan Shi
- Keshav Dhandhania
- Karthik Narasimhan
- Victor Barres
affiliations:
- Sierra
- Princeton University
arxiv_id: '2609.04611'
url: https://arxiv.org/abs/2609.04611
pdf_url: https://arxiv.org/pdf/2609.04611
published: '2026-09-03'
collected: '2026-09-07'
category: Agent
direction: Agent开发评测 · 端到端真实场景
tags:
- Agent-Benchmark
- LLM-Agent
- Developer-Agent
- Agent-Construction
- Eval
one_liner: 首个以Agent构建为核心任务的基准，还原真实业务开发全链路约束评测开发者Agent能力
practical_value: '- 业务Agent开发可复用需求挖掘链路：优先交叉验证多源异质业务文档（聊天记录、邮件、截图）+ 主动对齐stakeholder隐性需求，避免仅靠关键词搜索遗漏核心规则

  - 工程落地可参考约束校验逻辑：上线前强制验证单会话token成本、延迟、输出合规性三重约束，避免仅优化准确率忽略落地经济性

  - 内部Agent开发工具可引入自测试校验机制：禁止修改测试用例匹配Agent输出，强制要求测试用例对齐业务真实场景，避免自欺式测试

  - Agent架构选型可参考结论：当前大模型默认倾向单LLM工具环架构，主动引入意图路由、策略守卫等确定性脚手架可大幅提升效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent已广泛落地客服、纠纷处理等业务场景，但现有评测基准仅聚焦成品Agent的运行效果，未覆盖开发者Agent自主构建可落地Agent的能力，也没有还原真实开发中需求分散在多源异构文档、有明确成本/模型约束、需要对接存量系统的真实场景，无法衡量当前AI系统自主构建生产级Agent的真实水平。

### 方法关键点
- 任务设计1:1还原真实Agent开发全链路：开发者Agent需从多源异质业务文档（手册、聊天记录、截图、音视频等）+ 可交互模拟客户处挖掘需求，在给定成本、延迟、可选模型约束下，对接客户提供的可能存在缺陷的REST API，基于可选的初始代码库开发完整Agent
- 评测体系完全对齐生产标准：构建完成的Agent通过和模拟用户的多轮对话效果打分，需同时满足业务逻辑正确、信息传递准确、成本不超预算三个要求，最终得分是任务平均通过率减去超预算惩罚
- 基准覆盖航空、零售、电信、银行4个领域共53个任务，包含106套公开/私有评测集，2868个真实业务artifacts总token量超550万

### 关键实验
对比6种主流开发者Agent配置（GPT-5.6-sol/Claude Opus 5/Kimi K3等搭配对应代码脚手架），最强的Claude Opus 5 + Claude Code组合仅达到23.9%的任务通过率，远低于专家编写的参考基线82.2%；主动询问客户4次以上的开发流程得分是完全不询问的3倍；当前开发者Agent普遍仅使用不到72%的预算配额，默认选择熟悉的低成本模型而非优化成本效果比。

**最值得记住的一句话**：当前AI自主构建生产级Agent的能力还远未到落地水平，核心短板不是代码能力，而是需求挖掘不全、不主动对齐stakeholder、不做架构探索、自测试自欺的工程思维缺失。

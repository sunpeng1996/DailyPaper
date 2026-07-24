---
title: 'NVIDIA-labs OO Agents: Native Python Object-Oriented Agents'
title_zh: NVIDIA OO Agents：原生Python面向对象AI Agent开发框架
authors:
- Paul Furgale
- Severin Klingler
- James Nolan
- Matt Staats
- Gaia Di Lorenzo
- Elisa Martinez Abad
- Christian Schüller
- Razvan Dinu
- Alessio Devoto
- Pascal Berard
affiliations:
- NVIDIA Labs
arxiv_id: '2607.20709'
url: https://arxiv.org/abs/2607.20709
pdf_url: https://arxiv.org/pdf/2607.20709
published: '2026-07-21'
collected: '2026-07-24'
category: Agent
direction: Agent开发框架 · 面向对象编程范式
tags:
- Agent-Framework
- Python
- CodeAct
- LLM-Agent
- Memory-Management
one_liner: 将Agent抽象为Python对象，复用原生语法实现低门槛高性能的模型无关Agent开发
practical_value: '- 可复用「Agent=Python对象」的设计思路，将电商客服、推荐决策Agent的状态、确定性规则、LLM调用封装为单个类，用@strategy装饰器区分单轮预测/多轮执行逻辑，大幅降低Agent维护成本

  - 工程上可借鉴pass-by-reference+变量预览的设计，处理电商大订单、用户长行为序列等大对象时，仅在prompt中放入类型、长度等预览信息，LLM通过代码直接操作内存对象，避免上下文窗口浪费

  - 可复用混合内存系统设计：采用Agent主动调用+触发式自发注入的混合召回机制，存储用户偏好、历史会话等长期记忆，比纯RAG召回更贴合Agent主动管理记忆的需求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent开发框架普遍依赖自定义DSL，拆分的prompt模板、工具schema、回调代码不仅抬高开发者学习门槛，还与常规软件工程范式割裂，难以测试、调试、迭代，同时无法复用LLM已有的大量Python代码理解能力。

### 方法关键点
- 核心抽象：Agent对应Python类，字段为可访问状态，带常规代码的方法为确定性逻辑，body为`...`的方法为Agent执行入口，docstring自动转为prompt，类型注解作为输入输出校验契约
- 内置两种执行策略：PredictStrategy（单轮LLM调用，适配分类/抽取类短任务）、CodeActStrategy（多轮Python REPL循环，适配复杂推理任务）
- 上下文优化：静态+事件+动态三区块布局，最大化KV cache复用；大对象采用传引用+截断预览机制，支持处理远超上下文窗口的海量数据
- 可选内存子系统：支持Agent主动管理记忆+触发式自发注入，采用ACT-R激活排序+异步合并压缩，记忆可关联活对象避免 stale 数据

### 关键结果
- 基础能力测试：10款主流模型平均通过率97.9%，frontier模型通过率99.2%，验证接口对LLM无额外学习成本
- SWE-bench Verified：GPT-5.5 xhigh推理下通过率达82.2%，比同配置OpenCode高3.6个百分点，单任务token消耗低15.4%
- ARC-AGI-3：内置NOOA框架的GPT-5.6-sol得分达85.1%，是原始模型的6.4倍，单游戏成本不到20美元

### 最值得记住的一句话
复用成熟编程语言原生抽象做Agent开发，是同时降低人类开发者门槛、提升LLM接口友好度的最优路径。

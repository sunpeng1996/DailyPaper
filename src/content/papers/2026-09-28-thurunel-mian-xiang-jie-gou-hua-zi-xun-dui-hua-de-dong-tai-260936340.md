---
title: 'ThuRunel: Dynamic Decoupling for Structured Advisory Dialogue'
title_zh: ThuRunel：面向结构化咨询对话的动态解耦框架
authors:
- Yuyan Chen
affiliations:
- ModelsLive Inc.
arxiv_id: '2609.36340'
url: https://arxiv.org/abs/2609.36340
pdf_url: https://arxiv.org/pdf/2609.36340
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 人机协作咨询优化
tags:
- Task-Oriented-Dialogue
- Human-in-the-loop
- LLM-Adapters
- CoT
- Belief-State-Tracking
one_liner: 提出动态解耦咨询范式，结合有限状态管理与CoT合成，实现高效人机分流咨询Agent
practical_value: '- 垂直领域售前/咨询Agent可复用**Tier分层槽位+待槽位寄存器**设计，优先收集决策关键信息，减少无效对话轮次，提升转化效率

  - 低资源垂直场景可复用CoT教师合成协议，单条基础对话生成3路并行监督信号，同时适配多任务目标，大幅降低人工标注成本

  - 人机分流场景可用有限状态信念管理框架做确定性边界校验，通过动作守卫拦截LLM幻觉越权输出（如虚假承诺、超范围诊断），同时自动生成结构化交接Brief，降低人工重复信息收集成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高风险咨询领域（医美、法律、教育规划）天然分两阶段：前期以共情引导、信息收集为主，专业要求低但耗时长；后期以专家判断为主，专业要求高但信息密度大。纯AI系统易越权输出错误结论，纯人工模式成本高、无法规模化，现有系统未解决「AI该问什么、什么时候停止收集、什么内容自主处理、什么内容转专家」的核心分流问题。

### 方法关键点
- 提出动态解耦任务范式，将交互拆为4个决策模块：回复生成、阶段切换、用户画像合成、专家Brief生成；槽位按优先级分3层，Tier1为决策必填信息，收集完成才触发转专家流程
- 用6步CoT教师合成协议，单条基础对话生成3路并行监督信号，基于Qwen2.5-32B-Instruct训练3个QLoRA适配器，分别负责用户端回复生成、画像/Brief生成、任务路由
- 有限状态信念管理框架搭配待槽位寄存器、动作守卫，确定性管控交互边界，禁止LLM输出诊断、定价、承诺类幻觉内容

### 关键实验
在医美领域400条测试集上对比11个baseline（含GPT-5.5、Claude-4.6、ReAct、AutoGen等）：ThuRunel平均人工评分94.9，超次优9.1分；Tier1槽位填充率90.3%，超次优12.1pct；完成Tier1信息收集仅需5.2轮，比次优少3.3轮；边界合规性得分96.0，超次优10.7pct。

> 最值得记住的结论：垂直咨询场景中，边界合规性和响应结构化对整体会话质量的影响远高于共情度和回答准确性。

---
title: 'AgentSWE: Can Coding Agents Build the Agent You Actually Want?'
title_zh: AgentSWE：编码Agent能否生成符合真实需求的定制Agent
authors:
- Jiahao Wang
- Hongjin Qian
- Yuyang Hu
- Jiajun Zhang
- Zheng Liu
affiliations:
- Beijing Academy of Artificial Intelligence
- Institute of Automation, Chinese Academy of Sciences
- Renmin University of China
arxiv_id: '2610.13361'
url: https://arxiv.org/abs/2610.13361
pdf_url: https://arxiv.org/pdf/2610.13361
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 全生命周期开发能力评估基准
tags:
- Coding Agent
- Agent Engineering
- Benchmark
- Requirement Fidelity
- Evaluation
one_liner: 提出覆盖Agent开发全生命周期的AgentSWE基准，评估编码Agent生成定制Agent的需求符合度
practical_value: '- 搭建业务推荐/客服Agent时，不要仅依赖少量开发样例的测试结果，需额外构造覆盖全需求的held-out测试集，避免过拟合开发样例导致线上表现滑坡

  - 用编码Agent生成业务Agent时，不要仅做静态代码审核，必须增加端到端运行态校验，避免代码看似完整实际功能缺失的空心运行时问题

  - 评估自研编码Agent的工程能力时，可复用AgentSWE的任务范式：开发反馈仅给少量样例，验收用独立held-out集打分，更贴近真实业务委托场景

  - 优化编码Agent生成Agent的效果时，可给编码Agent增加「自行构造测试用例并端到端自测」的prompt指令，能缩小开发/线上效果差距，降低结果方差'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有编码Agent基准要么仅测代码补丁正确性，要么仅测现成Agent的任务表现，完全未覆盖「用编码Agent根据自然语言需求开发定制Agent」的真实场景，也无法衡量生成的Agent是否真的符合原始需求、能泛化到未见过的case，行业缺乏对应的评估体系。

### 方法关键点
- 覆盖Agent开发全生命周期3类共25个任务：10个Creation（从0构建完整Agent）、10个Editing（给生产环境Agent新增功能）、5个Optimization（优化现有Agent的可量化指标）
- 评估范式完全模拟真实委托：编码Agent仅能拿到需求+少量公开开发样例，验收时用完全独立的held-out测试集，无参考实现，按需求衍生的评分规则打分
- 硬有效性校验：Creation/Editing任务设准入门限，无法启动、超时、输出不可解析的直接得0分；Optimization任务用原生指标评估优化的gap闭合率

### 关键结果
测试了5个主流大模型搭配Codex编码Agent框架的表现：最强的DeepSeek-V4-Pro在Creation任务平均得分仅19.1，Editing任务平均31.6，Optimization任务平均仅能闭合不到5%的目标gap；开发样例得分90+的Agent，held-out测试平均得分仅9.9。

### 核心结论
编码Agent开发的Agent，其开发样例表现和实际交付表现的差距是常态，而非特例。

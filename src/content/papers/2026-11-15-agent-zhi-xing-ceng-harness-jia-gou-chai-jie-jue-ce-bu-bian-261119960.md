---
title: 'Anatomy of an Agent Harness: Decisions, Invariants and Corner Cases'
title_zh: Agent 执行层（Harness）架构拆解：决策、不变量与边界异常
authors:
- Resham Joshi
affiliations:
- codeburn.app
arxiv_id: '2611.19960'
url: https://arxiv.org/abs/2611.19960
pdf_url: https://arxiv.org/pdf/2611.19960
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: Agent 执行层可靠性设计与测试
tags:
- Agent Harness
- Invariant Testing
- Fault Tolerance
- System Design
- Reliability
one_liner: 梳理Agent Harness的30项可测试决策规则、不变量与异常用例，降低重复踩坑概率
practical_value: '- 可直接复用文中梳理的30项Harness决策检查清单，快速排查自家Agent执行层的可靠性漏洞，比如工具调用重复执行、超时未杀死进程等业务高发问题

  - 参考文中的信任边界划分模型，把LLM输出、工具返回内容、第三方扩展都归为不可信输入，加权限校验，避免Agent在电商营销、客诉处理、广告投放场景下误执行高危操作（比如批量改价、发优惠券）

  - 用文中的故障分类与测试方法，构造脚本化的故障注入测试，模拟模型断连、工具超时、返回异常，覆盖推荐Agent、广告投放Agent的核心异常分支

  - 做Agent持久化时直接采用append-only日志的设计，先写日志再执行工具，崩溃重启后可快速恢复状态，避免电商场景下Agent执行订单操作的幂等性问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent Harness（包裹LLM、调度工具、处理异常、管理会话的执行层）的决策逻辑大多散落在代码里没有统一规范，不同团队开发Harness时会反复遇到相同的边界问题，没有可复用的校验规则与测试方案。

### 方法关键点
- 定义Agent Harness的系统组成与6类信任边界：模型输出、工具/网页内容、项目文件、扩展、其他Agent文本、无人值守触发的任务，所有跨边界输入默认不可信
- 梳理6大类共30张决策卡片，每张包含决策选项、成本收益、必须满足的不变量、击穿规则的边界异常、对应测试用例，覆盖会话流转、故障处理、Prompt组装、状态管理、权限控制、界面展示6个维度
- 提出基于脚本化Provider、行为录制、故障注入的测试方法，配套可落地的Harness自检checklist

### 关键结果数字
全部83条不变量条款中，56条已在作者自研的Crewroom Harness中验证通过，12条为理论推导未全量验证，15条仍为待解决开放问题；作者用checklist自检Crewroom的30项规则，11项完全符合，14项不符合，5项未测试。

### 核心结论
Agent的可靠性90%以上不来自LLM本身，而来自包裹它的Harness层对每一个边界决策的严谨处理与可测试的不变量约束。
